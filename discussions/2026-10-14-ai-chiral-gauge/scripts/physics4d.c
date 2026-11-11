/* 4D overlap-projector curvature on homogeneous, NONCOMMUTING SU(5)
 * backgrounds. Independent diagnostic of chiral anomaly cancellation;
 * NOT an implementation of Craig's reconstructed measure/current.
 * The same kernels also evaluate Weyl-pair and direct Dirac determinants.
 * gcc -O3 -std=c11 -Wall -Wextra -Werror physics4d.c
 *     -l:liblapack.so.3 -l:libblas.so.3 -lm -o physics4d
 */
#define _POSIX_C_SOURCE 200809L
#include <complex.h>
#include <inttypes.h>
#include <math.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <unistd.h>
typedef double complex Z;
#define PI 3.141592653589793238462643383279502884
#define AT(a,i,j,n) ((a)[(i)+(n)*(j)])
#define MAXD 40
#define VERSION 3
extern void zheev_(char*,char*,int*,Z*,int*,double*,Z*,int*,double*,int*);
extern void zgemm_(char*,char*,int*,int*,int*,Z*,const Z*,int*,const Z*,int*,Z*,Z*,int*);
extern void zgetrf_(int*,int*,Z*,int*,int*,int*);
static uint64_t rng;
static Z gamma[5][16],K[4][25],X[4][25],Y[4][25];
static const Z sigma[4][4]={{1,0,0,1},{0,1,1,0},{0,I,-I,0},{1,0,0,-1}};
typedef struct { double logabs,phase; } Logdet;
typedef struct {
    long double omega[2],omega_right[2],omega_abs[2],dirac[2],weyl[2];
    long double delta_dirac[2],delta_weyl[2],roundoff_proxy[2];
    double gap[2],max_pair_error,max_det_log_error,max_det_phase_error,max_dirac_phase;
    uint64_t done,total; int N;
} Level;
typedef struct { uint64_t magic,seed; int version,nmax,level; Level rows[4]; } Checkpoint;
static void fail(const char*s){fprintf(stderr,"%s\n",s);exit(2);}
static double uniform(void){rng^=rng<<13;rng^=rng>>7;rng^=rng<<17;return (rng>>11)*0x1.0p-53;}
static void mm(int n,char ta,char tb,const Z*a,const Z*b,Z*c){
    Z one=1,zero=0;zgemm_(&ta,&tb,&n,&n,&n,&one,a,&n,b,&n,&zero,c,&n);
}
static void eig(int n,Z*a,double*e){
    char v='V',u='U';int lw=64*n,info;Z w[64*MAXD];double rw[3*MAXD];
    zheev_(&v,&u,&n,a,&n,e,w,&lw,rw,&info);if(info)fail("LAPACK eigenproblem failed");
}
static Logdet logdet(int n,const Z*src){
    Z a[MAXD*MAXD];int ip[MAXD],info;memcpy(a,src,sizeof(Z)*n*n);
    zgetrf_(&n,&n,a,&n,ip,&info);if(info)fail("singular determinant in AP/AP/AP/AP diagnostic");
    Logdet ans={0,0};for(int i=0;i<n;i++){ans.logabs+=log(cabs(AT(a,i,i,n)));ans.phase+=carg(AT(a,i,i,n));if(ip[i]!=i+1)ans.phase+=PI;}
    ans.phase=remainder(ans.phase,2*PI);return ans;
}
static void init_gamma(void){
    for(int mu=0;mu<5;mu++)for(int i=0;i<4;i++)for(int j=0;j<4;j++){
        int a=mu<3?1:(mu==3?2:3),b=mu<3?mu+1:0;
        AT(gamma[mu],i,j,4)=AT(sigma[a],i/2,j/2,2)*AT(sigma[b],i%2,j%2,2);
    }
}
static void generator(Z*a){
    memset(a,0,25*sizeof(Z));double tr=0,norm=0;
    for(int i=0;i<5;i++){AT(a,i,i,5)=2*uniform()-1;tr+=creal(AT(a,i,i,5));
        for(int j=i+1;j<5;j++){Z z=(2*uniform()-1)+I*(2*uniform()-1);AT(a,i,j,5)=z;AT(a,j,i,5)=conj(z);}}
    for(int i=0;i<5;i++)AT(a,i,i,5)-=tr/5;
    for(int i=0;i<25;i++)norm+=creal(conj(a[i])*a[i]);
    for(int i=0;i<25;i++)a[i]/=sqrt(norm);
}
static void field(uint64_t seed){
    rng=seed?seed:1;
    for(int mu=0;mu<4;mu++){generator(K[mu]);for(int j=0;j<25;j++)K[mu][j]*=1.25;}
    memset(X,0,sizeof(X));memset(Y,0,sizeof(Y));generator(X[0]);generator(Y[1]);
}
static double sinc(double x){return fabs(x)<1e-7?1-x*x/6:sin(x)/x;}
/* Derivative of exp(i h K), evaluated by the exact divided difference. */
static void gauge_link(double h,const Z*k,const Z*x,const Z*y,Z*u,Z*ux,Z*uy){
    Z v[25],tmp[25],xx[25],yy[25],ee[25]={0};double ev[5];memcpy(v,k,sizeof(v));eig(5,v,ev);
    mm(5,'N','N',x,v,tmp);mm(5,'C','N',v,tmp,xx);
    mm(5,'N','N',y,v,tmp);mm(5,'C','N',v,tmp,yy);
    for(int i=0;i<5;i++){AT(ee,i,i,5)=cexp(I*h*ev[i]);for(int j=0;j<5;j++){
        Z f=I*h*cexp(I*h*(ev[i]+ev[j])/2)*sinc(h*(ev[i]-ev[j])/2);
        AT(xx,i,j,5)*=f;AT(yy,i,j,5)*=f;}}
    mm(5,'N','N',v,ee,tmp);mm(5,'N','C',tmp,v,u);
    mm(5,'N','N',v,xx,tmp);mm(5,'N','C',tmp,v,ux);
    mm(5,'N','N',v,yy,tmp);mm(5,'N','C',tmp,v,uy);
}
static void exterior(const Z*u,const Z*du,Z*out,Z*dout){
    int a[10],b[10],z=0;for(int i=0;i<5;i++)for(int j=i+1;j<5;j++){a[z]=i;b[z++]=j;}
    for(int i=0;i<10;i++)for(int j=0;j<10;j++){
        int p=a[i],q=b[i],r=a[j],s=b[j];
        AT(out,i,j,10)=AT(u,p,r,5)*AT(u,q,s,5)-AT(u,p,s,5)*AT(u,q,r,5);
        AT(dout,i,j,10)=AT(du,p,r,5)*AT(u,q,s,5)+AT(u,p,r,5)*AT(du,q,s,5)-AT(du,p,s,5)*AT(u,q,r,5)-AT(u,p,s,5)*AT(du,q,r,5);
    }
}
typedef struct {int r;Z u[4][100],x[4][100],y[4][100];} Links;
static void sample(int N,Links*r5,Links*r10){
    r5->r=5;r10->r=10;
    for(int mu=0;mu<4;mu++){
        Z u[25],x[25],y[25];gauge_link(1./N,K[mu],X[mu],Y[mu],u,x,y);
        for(int j=0;j<25;j++){r5->u[mu][j]=conj(u[j]);r5->x[mu][j]=conj(x[j]);r5->y[mu][j]=conj(y[j]);}
        exterior(u,x,r10->u[mu],r10->x[mu]);exterior(u,y,r10->u[mu],r10->y[mu]);
    }
}
static void kernel(const Links*l,const double*p,Z*h,Z*dx,Z*dy){
    int r=l->r,n=4*r;memset(h,0,sizeof(Z)*n*n);memset(dx,0,sizeof(Z)*n*n);memset(dy,0,sizeof(Z)*n*n);
    for(int a=0;a<4;a++)for(int b=0;b<4;b++)for(int i=0;i<r;i++)AT(h,a*r+i,b*r+i,n)=3*AT(gamma[4],a,b,4);
    for(int mu=0;mu<4;mu++){
        Z ep=cexp(I*p[mu]);
        for(int a=0;a<4;a++)for(int b=0;b<4;b++){
            Z f=(-I*AT(gamma[mu],a,b,4)-AT(gamma[4],a,b,4))/2;
            Z g=( I*AT(gamma[mu],a,b,4)-AT(gamma[4],a,b,4))/2;
            for(int i=0;i<r;i++)for(int j=0;j<r;j++){
                int row=a*r+i,col=b*r+j;
                AT(h,row,col,n)+=f*ep*AT(l->u[mu],i,j,r)+g*conj(ep*AT(l->u[mu],j,i,r));
                AT(dx,row,col,n)+=f*ep*AT(l->x[mu],i,j,r)+g*conj(ep*AT(l->x[mu],j,i,r));
                AT(dy,row,col,n)+=f*ep*AT(l->y[mu],i,j,r)+g*conj(ep*AT(l->y[mu],j,i,r));
            }
        }
    }
}
static void point(const Links*l,const double*p,Level*acc,int rep){
    int n=4*l->r,m=n/2;Z v[1600],dx[1600],dy[1600],tmp[1600],xx[1600],yy[1600];double ev[40];
    kernel(l,p,v,dx,dy);eig(n,v,ev);
    int neg=0;for(int i=0;i<n;i++){if(ev[i]<0)neg++;acc->gap[rep]=fmin(acc->gap[rep],fabs(ev[i]));}
    if(neg!=m)fail("nonzero momentum-block index: this fixture leaves the calibrated rank domain");
    mm(n,'N','N',dx,v,tmp);mm(n,'C','N',v,tmp,xx);
    mm(n,'N','N',dy,v,tmp);mm(n,'C','N',v,tmp,yy);
    long double left=0,right=0,ab=0;
    for(int i=m;i<n;i++)for(int j=0;j<m;j++){
        double d=ev[i]-ev[j],z=-2*cimag(AT(xx,i,j,n)*conj(AT(yy,i,j,n)))/(d*d);
        left+=z;ab+=fabs(z);
    }
    /* Independent negative-band sum, not defined as minus left. */
    for(int i=0;i<m;i++)for(int j=m;j<n;j++){
        double d=ev[i]-ev[j];right+=-2*cimag(AT(xx,i,j,n)*conj(AT(yy,i,j,n)))/(d*d);
    }
    acc->omega[rep]+=left;acc->omega_right[rep]+=right;acc->omega_abs[rep]+=fabsl(left);
    acc->roundoff_proxy[rep]+=ab*2.220446049250313e-16;
    acc->max_pair_error=fmax(acc->max_pair_error,(double)fabsl(left+right));
    /* Independent full Dirac matrix D=1+gamma5 sign(H), then direct LU. */
    for(int i=0;i<n;i++)for(int j=0;j<n;j++)AT(tmp,i,j,n)=AT(v,i,j,n)*(j<m?-1:1);
    mm(n,'N','C',tmp,v,xx);
    for(int i=0;i<n;i++)for(int j=0;j<n;j++)AT(xx,i,j,n)=(i==j?1:0)+(i<m?1:-1)*AT(xx,i,j,n);
    Logdet direct=logdet(n,xx);
    /* Fixed gamma5 rows, positive/negative-H columns. D maps each sector
     * exactly to its fixed reference: blocks are 2*corresponding V rows.
     * The basis determinant is essential to the full phase comparison. */
    for(int i=0;i<m;i++)for(int j=0;j<m;j++){
        AT(xx,i,j,m)=2*AT(v,i,j+m,n);AT(yy,i,j,m)=2*AT(v,i+m,j,n);
    }
    Logdet dl=logdet(m,xx),dr=logdet(m,yy),basis=logdet(n,v);
    /* Reordering negative/positive eigencolumns has sign (-1)^(m*m)=+1. */
    double pairlog=dl.logabs+dr.logabs;
    double pairphase=remainder(dl.phase+dr.phase-basis.phase,2*PI);
    acc->max_det_log_error=fmax(acc->max_det_log_error,fabs(direct.logabs-pairlog));
    acc->max_det_phase_error=fmax(acc->max_det_phase_error,fabs(remainder(direct.phase-pairphase,2*PI)));
    acc->max_dirac_phase=fmax(acc->max_dirac_phase,fabs(direct.phase));
    double mass=-1,sin2=0;for(int mu=0;mu<4;mu++){mass+=1-cos(p[mu]);sin2+=sin(p[mu])*sin(p[mu]);}
    double ee=sqrt(mass*mass+sin2),freelog=2*l->r*log(2*(1+mass/ee));
    acc->dirac[rep]+=direct.logabs;acc->weyl[rep]+=pairlog;
    acc->delta_dirac[rep]+=direct.logabs-freelog;acc->delta_weyl[rep]+=pairlog-freelog;
}
static double plaquette(const Links*l){
    int n=l->r;double worst=0;Z a[100],b[100],c[100];
    for(int mu=0;mu<4;mu++)for(int nu=mu+1;nu<4;nu++){
        mm(n,'N','N',l->u[mu],l->u[nu],a);mm(n,'N','C',a,l->u[mu],b);mm(n,'N','C',b,l->u[nu],c);
        double norm=0;for(int i=0;i<n;i++)for(int j=0;j<n;j++){Z z=AT(c,i,j,n)-(i==j?1:0);norm+=creal(z*conj(z));}
        worst=fmax(worst,sqrt(norm));
    }return worst;
}
static void rowjson(FILE*f,const Level*a){
    fprintf(f,"{\"N\":%d,\"momenta_done\":%"PRIu64",\"momenta_total\":%"PRIu64",\"complete\":%s,",a->N,a->done,a->total,a->done==a->total?"true":"false");
    fprintf(f,"\"omega_anti5_left\":%.18Lg,\"omega_10_left\":%.18Lg,\"omega_chiral_sum\":%.18Lg,",a->omega[0],a->omega[1],a->omega[0]+a->omega[1]);
    fprintf(f,"\"omega_vectorlike_sum\":%.18Lg,\"absolute_momentum_sums\":[%.18Lg,%.18Lg],",a->omega[0]+a->omega[1]+a->omega_right[0]+a->omega_right[1],a->omega_abs[0],a->omega_abs[1]);
    fprintf(f,"\"arithmetic_scale_proxy_not_error_bound\":[%.18Lg,%.18Lg],",a->roundoff_proxy[0],a->roundoff_proxy[1]);
    fprintf(f,"\"min_wilson_gap\":[%.17g,%.17g],\"max_point_vectorlike_curvature_error\":%.17g,",a->gap[0],a->gap[1],a->max_pair_error);
    fprintf(f,"\"dirac_logabs\":[%.18Lg,%.18Lg],\"weyl_pair_logabs\":[%.18Lg,%.18Lg],",a->dirac[0],a->dirac[1],a->weyl[0],a->weyl[1]);
    fprintf(f,"\"dirac_minus_free_logabs\":[%.18Lg,%.18Lg],\"weyl_pair_minus_free_logabs\":[%.18Lg,%.18Lg],",a->delta_dirac[0],a->delta_dirac[1],a->delta_weyl[0],a->delta_weyl[1]);
    fprintf(f,"\"max_point_dirac_weyl_logabs_error\":%.17g,\"max_point_dirac_weyl_phase_error\":%.17g,\"max_point_dirac_phase\":%.17g}",a->max_det_log_error,a->max_det_phase_error,a->max_dirac_phase);
}
static void writejson(const char*path,const Checkpoint*c,int complete){
    char tmp[4096];snprintf(tmp,sizeof(tmp),"%s.tmp",path);FILE*f=fopen(tmp,"w");if(!f)fail("cannot open JSON output");
    fprintf(f,"{\"version\":%d,\"seed\":%"PRIu64",\"completed\":%s,\"observable\":\"4D fixed-frame homogeneous-background projector curvature, not Craig full current\",\"amplitude_frobenius_each_K\":1.25,\"spin\":\"AP/AP/AP/AP\",\"levels\":[",VERSION,c->seed,complete?"true":"false");
    for(int i=0;i<4&&c->rows[i].N;i++){if(i)fprintf(f,",");rowjson(f,&c->rows[i]);}
    fprintf(f,"]}\n");fflush(f);fsync(fileno(f));fclose(f);if(rename(tmp,path))fail("cannot commit JSON output");
}
static void checkpoint(const char*base,const Checkpoint*c){
    char path[4096],tmp[4096];snprintf(path,sizeof(path),"%s.checkpoint.bin",base);snprintf(tmp,sizeof(tmp),"%s.checkpoint.tmp",base);
    FILE*f=fopen(tmp,"wb");if(!f)fail("cannot open checkpoint");if(fwrite(c,sizeof(*c),1,f)!=1)fail("checkpoint write failed");fflush(f);fsync(fileno(f));fclose(f);if(rename(tmp,path))fail("checkpoint rename failed");
    snprintf(path,sizeof(path),"%s.progress.json",base);writejson(path,c,0);
}
static void calibrate(uint64_t seed){
    /* Test the link derivative, gauge covariance, Clifford algebra, and
     * zero-field curvature with the SAME observable used in the campaign. */
    double cliff=0;Z a[16],b[16];for(int mu=0;mu<5;mu++)for(int nu=0;nu<5;nu++){
        mm(4,'N','N',gamma[mu],gamma[nu],a);mm(4,'N','N',gamma[nu],gamma[mu],b);
        for(int i=0;i<4;i++)for(int j=0;j<4;j++)cliff=fmax(cliff,cabs(AT(a,i,j,4)+AT(b,i,j,4)-(mu==nu&&i==j?2:0)));
    }
    Z u[25],dx[25],dy[25],up[25],um[25],kp[25],km[25],zz[25]={0},junk[25];double eps=1e-5,derr=0;
    for(int i=0;i<25;i++){kp[i]=K[0][i]+eps*X[0][i];km[i]=K[0][i]-eps*X[0][i];}
    gauge_link(1./3,K[0],X[0],Y[0],u,dx,dy);gauge_link(1./3,kp,zz,zz,up,junk,dy);gauge_link(1./3,km,zz,zz,um,junk,dy);
    for(int i=0;i<25;i++)derr=fmax(derr,cabs((up[i]-um[i])/(2*eps)-dx[i]));
    Links r5,r10;sample(3,&r5,&r10);double p[4]={.37,.89,1.23,2.17};Level before={0},after={0};before.gap[0]=before.gap[1]=after.gap[0]=after.gap[1]=1e9;
    point(&r5,p,&before,0);point(&r10,p,&before,1);
    Z gen[25],rot[25],tmp[25];generator(gen);gauge_link(.83,gen,zz,zz,rot,junk,dy);
    for(int mu=0;mu<4;mu++){
        mm(5,'N','N',rot,K[mu],tmp);mm(5,'N','C',tmp,rot,K[mu]);
        mm(5,'N','N',rot,X[mu],tmp);mm(5,'N','C',tmp,rot,X[mu]);
        mm(5,'N','N',rot,Y[mu],tmp);mm(5,'N','C',tmp,rot,Y[mu]);
    }
    sample(3,&r5,&r10);point(&r5,p,&after,0);point(&r10,p,&after,1);
    double cov=fmax((double)fabsl(before.omega[0]-after.omega[0]),(double)fabsl(before.omega[1]-after.omega[1]));
    printf("calibration seed=%"PRIu64" Clifford=%.3g dU=%.3g gauge_curvature=%.3g Dirac_Weyl_log=%.3g phase=%.3g pair=%.3g\n",seed,cliff,derr,cov,before.max_det_log_error,before.max_det_phase_error,before.max_pair_error);
    if(cliff>1e-12||derr>1e-8||cov>1e-10||before.max_det_log_error>1e-9||before.max_det_phase_error>1e-9)fail("calibration failed");
    field(seed);
}
int main(int argc,char**argv){
    uint64_t seed=20261014;const char*out=NULL;int nmax=27;
    for(int i=1;i<argc;i++){
        if(!strcmp(argv[i],"--seed")&&i+1<argc)seed=strtoull(argv[++i],NULL,10);
        else if(!strcmp(argv[i],"--output")&&i+1<argc)out=argv[++i];
        else if(!strcmp(argv[i],"--nmax")&&i+1<argc)nmax=atoi(argv[++i]);
        else fail("usage: physics4d --seed INTEGER --output FILE [--nmax 3|9|27|81]");
    }
    if(!out||(nmax!=3&&nmax!=9&&nmax!=27&&nmax!=81))fail("output and supported nmax required");
    setvbuf(stdout,NULL,_IOLBF,0);init_gamma();field(seed);calibrate(seed);
    Checkpoint c={0};c.magic=UINT64_C(0x4352414947344403);c.seed=seed;c.version=VERSION;c.nmax=nmax;
    char path[4096];snprintf(path,sizeof(path),"%s.checkpoint.bin",out);FILE*f=fopen(path,"rb");
    if(f){Checkpoint old;if(fread(&old,sizeof(old),1,f)!=1)fail("bad checkpoint");fclose(f);if(old.magic!=c.magic||old.seed!=seed||old.version!=VERSION||old.nmax!=nmax)fail("checkpoint mismatch");c=old;printf("resuming level=%d\n",c.level);}
    const int ns[4]={3,9,27,81};clock_t start=clock();
    for(int lev=c.level;lev<4&&ns[lev]<=nmax;lev++){
        int N=ns[lev];Level*t=&c.rows[lev];
        if(!t->N){memset(t,0,sizeof(*t));t->N=N;t->total=(uint64_t)N*N*N*N;t->gap[0]=t->gap[1]=1e9;}
        Links anti,ten;sample(N,&anti,&ten);
        printf("level N=%d nodes=%"PRIu64" plaquette_Frobenius_anti5=%.9g 10=%.9g\n",N,t->total,plaquette(&anti),plaquette(&ten));
        for(uint64_t ix=t->done;ix<t->total;ix++){
            uint64_t rem=ix;double p[4];for(int mu=0;mu<4;mu++){p[mu]=2*PI*((rem%N)+.5)/N;rem/=N;}
            point(&anti,p,t,0);point(&ten,p,t,1);t->done=ix+1;
            if((t->done%1024)==0)checkpoint(out,&c);
        }
        c.level=lev+1;checkpoint(out,&c);
        printf("complete N=%d omega_anti5=%.12Lg omega10=%.12Lg chiral=%.12Lg vectorlike=%.3Lg Dirac_Weyl_max=%.3g CPU=%.1f\n",N,t->omega[0],t->omega[1],t->omega[0]+t->omega[1],t->omega[0]+t->omega[1]+t->omega_right[0]+t->omega_right[1],t->max_det_log_error,(double)(clock()-start)/CLOCKS_PER_SEC);
        if(t->max_det_log_error>1e-7||t->max_det_phase_error>1e-7||t->max_pair_error>1e-9)fail("implementation control failed: retain checkpoint and investigate");
    }
    writejson(out,&c,1);printf("finished seed=%"PRIu64" CPU_seconds=%.3f\n",seed,(double)(clock()-start)/CLOCKS_PER_SEC);return 0;
}
