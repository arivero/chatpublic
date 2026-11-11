/* Independent finite tests of Craig arXiv:2610.09093v1.
 * C11, LAPACK/BLAS; gcc -O3 -std=c11 -Wall -Wextra check.c -l:liblapack.so.3 -l:libblas.so.3 -lm -o check
 * No author code or saved numerical results are used.
 */
#include <complex.h>
#include <math.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
typedef double complex Z;
#define PI 3.141592653589793238462643383279502884
#define A(a,i,j,n) ((a)[(i)+(n)*(j)])
extern void zheev_(char*,char*,int*,Z*,int*,double*,Z*,int*,double*,int*);
extern void zgemm_(char*,char*,int*,int*,int*,Z*,const Z*,int*,const Z*,int*,Z*,Z*,int*);
static double lowest_gap=1e9;
static void eigen(int n,Z *a,double *ev,int vectors) {
    char job=vectors?'V':'N',up='U'; int lwork=40*n,info;
    Z *work=malloc(sizeof(Z)*lwork); double *rw=malloc(sizeof(double)*3*n);
    zheev_(&job,&up,&n,a,&n,ev,work,&lwork,rw,&info);
    free(work);free(rw); if(info){fprintf(stderr,"zheev failed %d\n",info);exit(2);}
}
static void mm(int n,char ta,char tb,const Z *a,const Z*b,Z*c) {
    Z one=1,zero=0; zgemm_(&ta,&tb,&n,&n,&n,&one,a,&n,b,&n,&zero,c,&n);
}
static double gap(int n,Z *h) {
    double *ev=malloc(sizeof(double)*n);eigen(n,h,ev,0);double g=1e9;
    for(int i=0;i<n;i++)if(fabs(ev[i])<g)g=fabs(ev[i]);
    free(ev);return g;
}
static uint64_t rng=UINT64_C(20261013);
static double uniform(void) {rng^=rng<<13;rng^=rng>>7;rng^=rng<<17;return (rng>>11)*0x1.0p-53;}
static Z pauli[4][4]={{1,0,0,1},{0,1,1,0},{0,I,-I,0},{1,0,0,-1}};
static Z G[5][16];
static void init_gamma(void) {
    for(int mu=0;mu<5;mu++)for(int i=0;i<4;i++)for(int j=0;j<4;j++) {
        int x=mu<3?1:(mu==3?2:3), y=mu<3?mu+1:0;
        A(G[mu],i,j,4)=A(pauli[x],i/2,j/2,2)*A(pauli[y],i%2,j%2,2);
    }
}
static void free_h(const double*p,Z*h) {
    double m=-1;for(int mu=0;mu<4;mu++)m+=1-cos(p[mu]);
    for(int i=0;i<16;i++){h[i]=m*G[4][i];for(int mu=0;mu<4;mu++)h[i]+=sin(p[mu])*G[mu][i];}
}
static double gap4(const double *p,double s,int omit,double *normerr) {
    const int n=324;Z *h=calloc(n*n,sizeof(Z)),hc[16],hf[81][16];double w[81],sum=0;
    free_h(p,hc);
    for(int q=0;q<81;q++){int rem=q;double k[4];w[q]=1;
        for(int mu=0;mu<4;mu++){k[mu]=(p[mu]+2*PI*(rem%3))/3;rem/=3;w[q]*=(1+2*cos(k[mu]))/3;}
        sum+=w[q]*w[q];free_h(k,hf[q]);
    }
    if(fabs(sum-1)>*normerr)*normerr=fabs(sum-1);
    for(int q=0;q<81;q++)for(int r=0;r<81;r++)for(int i=0;i<4;i++)for(int j=0;j<4;j++) {
        Z z=omit?0:s*w[q]*w[r]*(A(hc,i,j,4)-A(G[4],i,j,4));
        if(q==r)z+=(1-s)*A(hf[q],i,j,4)+s*A(G[4],i,j,4);
        A(h,4*q+i,4*r+j,n)=z;
    }
    double g=gap(n,h);free(h);return g;
}
static void test4(void) {
    double min=1e9,at[5]={0},err=0;int count=0;double p[4];
    /* All 16 momentum corners, including p=0, and 11 s values. */
    for(int corner=0;corner<16;corner++)for(int j=0;j<=10;j++) {
        for(int mu=0;mu<4;mu++)p[mu]=(corner>>mu&1)*PI;
        double s=j/10.,g=gap4(p,s,0,&err);count++;
        if(g<min){min=g;memcpy(at,p,sizeof(p));at[4]=s;}
    }
    for(int r=0;r<256;r++) {
        for(int mu=0;mu<4;mu++)p[mu]=(2*uniform()-1)*PI;
        double s=uniform(),g=gap4(p,s,0,&err);count++;
        if(g<min){min=g;memcpy(at,p,sizeof(p));at[4]=s;}
    }
    printf("4D gap scan: %d matrices of size 324; minimum %.15g at p=(%.9g,%.9g,%.9g,%.9g), s=%.9g\n",count,min,at[0],at[1],at[2],at[3],at[4]);
    printf("4D inclusion max |sum w^2-1| = %.3g\n",err);
    memset(p,0,sizeof(p));printf("4D omitted-rank-correction control at p=0,s=1/2: gap %.15g\n",gap4(p,.5,1,&err));
    if(min<1e-8 || err>1e-12)exit(3);
}
/* Flat one-site torus, refined to 3x3, in inherited frames. Internal
 * links are 1, seam links are exp(i*q*a_mu) with spin sign applied once.
 * Columns index spinor input, rows output. gamma=(sigma1,sigma2), gamma5=sigma3.
 */
static void wilson2(int L,double q,double a,double b,double da,double db,int spinx,int spiny,Z*h,Z*dh) {
    int n=2*L*L;memset(h,0,sizeof(Z)*n*n);memset(dh,0,sizeof(Z)*n*n);
    Z gg[2][4]={{0,-1,1,0},{0,-I,-I,0}}; // gamma5*gamma_mu, column-major
    for(int site=0;site<L*L;site++){
        A(h,2*site,2*site,n)+=1;A(h,2*site+1,2*site+1,n)-=1;
        int xy[2]={site%L,site/L};
        for(int mu=0;mu<2;mu++){
            int dst=mu==0?(xy[0]+1)%L+L*xy[1]:xy[0]+L*((xy[1]+1)%L);
            int seam=xy[mu]==L-1;double theta=mu==0?a:b,dtheta=mu==0?da:db;
            int bc=mu==0?spinx:spiny;Z u=seam?bc*cexp(I*q*theta):1,du=seam?I*q*dtheta*u:0;
            for(int i=0;i<2;i++)for(int j=0;j<2;j++){
                Z g5=i==j?(i==0?1:-1):0;
                Z f=(A(gg[mu],i,j,2)-g5)/2,back=(-A(gg[mu],i,j,2)-g5)/2;
                A(h,2*site+i,2*dst+j,n)+=f*u;A(dh,2*site+i,2*dst+j,n)+=f*du;
                A(h,2*dst+i,2*site+j,n)+=back*conj(u);A(dh,2*dst+i,2*site+j,n)+=back*conj(du);
            }
        }
    }
}
static void comparison(double q,double t,double s,Z*h,Z*hs,Z*ht,int omission) {
    double a=.23+.17*cos(t),b=.37+.17*sin(t),da=-.17*sin(t),db=.17*cos(t);
    Z hc[4],dc[4],hf[324],df[324];wilson2(1,q,a,b,da,db,-1,-1,hc,dc);wilson2(3,q,a,b,da,db,-1,-1,hf,df);
    for(int x=0;x<9;x++)for(int y=0;y<9;y++)for(int i=0;i<2;i++)for(int j=0;j<2;j++) {
        int ix=2*x+i,jy=2*y+j;Z g5=i==j?(i==0?1:-1):0;
        Z ec=(A(hc,i,j,2)-g5)/9+(x==y?g5:0);
        A(h,ix,jy,18)=(1-s)*A(hf,ix,jy,18)+s*ec;
        A(hs,ix,jy,18)=ec-A(hf,ix,jy,18);
        A(ht,ix,jy,18)=(1-s)*A(df,ix,jy,18)+(omission?0:s*A(dc,i,j,2)/9);
    }
}
static double curvature(int n,Z*h,const Z*hs,const Z*ht) {
    double ev[n];Z tmp[n*n],aa[n*n],bb[n*n];eigen(n,h,ev,1);
    mm(n,'N','N',hs,h,tmp);mm(n,'C','N',h,tmp,aa);
    mm(n,'N','N',ht,h,tmp);mm(n,'C','N',h,tmp,bb);
    double ans=0;
    for(int i=0;i<n;i++){
        if(fabs(ev[i])<lowest_gap)lowest_gap=fabs(ev[i]);
        if(ev[i]<=0)continue;
        for(int j=0;j<n;j++)if(ev[j]<0){double d=ev[i]-ev[j];ans-=2*cimag(A(aa,i,j,n)*conj(A(bb,i,j,n)))/(d*d);}
    }
    return ans;
}
static void gauss(int n,double*x,double*w) {
    for(int i=0;i<(n+1)/2;i++) {
        double z=cos(PI*(i+.75)/(n+.5)),old,pp;
        do{double p1=1,p2=0;for(int j=1;j<=n;j++){double p3=p2;p2=p1;p1=((2*j-1)*z*p2-(j-1)*p3)/j;}
           pp=n*(z*p1-p2)/(z*z-1);old=z;z=old-p1/pp;}while(fabs(z-old)>2e-15);
        x[i]=(1-z)/2;x[n-1-i]=(1+z)/2;w[i]=w[n-1-i]=1/((1-z*z)*pp*pp);
    }
}
static double current(double q,int nt,int ns,int omission) {
    double x[ns],w[ns],sum=0;gauss(ns,x,w);
    for(int it=0;it<nt;it++)for(int is=0;is<ns;is++){
        Z h[324],hs[324],ht[324];comparison(q,2*PI*it/nt,x[is],h,hs,ht,omission);
        sum+=w[is]*curvature(18,h,hs,ht)*2*PI/nt;
    }return sum;
}
static Z determinant(int n,Z*a) {
    Z ans=1;
    for(int j=0;j<n;j++){
        int p=j;for(int i=j+1;i<n;i++)if(cabs(A(a,i,j,n))>cabs(A(a,p,j,n)))p=i;
        if(cabs(A(a,p,j,n))<1e-14){fprintf(stderr,"singular overlap\n");exit(4);}
        if(p!=j){for(int k=j;k<n;k++){Z t=A(a,p,k,n);A(a,p,k,n)=A(a,j,k,n);A(a,j,k,n)=t;}ans=-ans;}
        Z pivot=A(a,j,j,n);ans*=pivot;
        for(int i=j+1;i<n;i++){Z f=A(a,i,j,n)/pivot;for(int k=j+1;k<n;k++)A(a,i,k,n)-=f*A(a,j,k,n);}
    }return ans;
}
static void occupied(int L,double q,double a,double b,int sx,int sy,Z*v) {
    int n=2*L*L;Z h[n*n],dh[n*n];double ev[n];wilson2(L,q,a,b,0,0,sx,sy,h,dh);eigen(n,h,ev,1);
    int m=0;for(int j=0;j<n;j++)if(ev[j]>0){for(int i=0;i<n;i++)A(v,i,m,n)=A(h,i,j,n);m++;}
    if(m!=n/2){fprintf(stderr,"unexpected occupied rank\n");exit(5);}
}
static double phase(double q,int L,int nt) {
    int n=2*L*L,m=n/2;Z first[n*m],prev[n*m],next[n*m],ov[m*m],prod=1;
    occupied(L,q,.23+.17,.37,-1,-1,first);memcpy(prev,first,sizeof(first));
    for(int k=1;k<=nt;k++){
        double t=2*PI*k/nt;
        if(k==nt)memcpy(next,first,sizeof(first));else occupied(L,q,.23+.17*cos(t),.37+.17*sin(t),-1,-1,next);
        for(int i=0;i<m;i++)for(int j=0;j<m;j++){Z z=0;for(int r=0;r<n;r++)z+=conj(A(next,r,i,n))*A(prev,r,j,n);A(ov,i,j,m)=z;}
        Z d=determinant(m,ov);prod*=d/cabs(d);memcpy(prev,next,sizeof(prev));
    }return carg(prod);
}
static double chern(double q,int N,int sx,int sy,int rephase) {
    Z *v=malloc(sizeof(Z)*2*N*N);double sum=0;
    for(int y=0;y<N;y++)for(int x=0;x<N;x++){
        int j=x+N*y;occupied(1,q,2*PI*x/N,2*PI*y/N,sx,sy,v+2*j);
        if(rephase){Z u=cexp(2*PI*I*uniform());v[2*j]*=u;v[2*j+1]*=u;}
    }
    for(int y=0;y<N;y++)for(int x=0;x<N;x++){
        int ids[5]={x+N*y,(x+1)%N+N*y,(x+1)%N+N*((y+1)%N),x+N*((y+1)%N),x+N*y};Z prod=1;
        for(int k=0;k<4;k++){Z *a=v+2*ids[k],*b=v+2*ids[k+1];Z u=conj(b[0])*a[0]+conj(b[1])*a[1];prod*=u/cabs(u);}
        sum+=carg(prod);
    }free(v);return sum/(2*PI);
}
static void test2(void) {
    Z h0[4]={1,0,0,-1};double orient=curvature(2,h0,pauli[1],pauli[2]);
    printf("2D orientation calibration: %.15g (expected -0.5)\n",orient);
    if(fabs(orient+.5)>1e-13)exit(6);
    /* Independent analytic flat-spectrum calibration, and a directional
     * finite-difference check of the FULL comparison derivative. */
    Z hh[324],dd[324];double ev[18],expected[18],maxspec=0;
    wilson2(3,3,.4,.37,0,0,-1,-1,hh,dd);eigen(18,hh,ev,0);
    int ne=0;
    for(int x=0;x<3;x++)for(int y=0;y<3;y++){
        double kx=(3*.4+PI+2*PI*x)/3,ky=(3*.37+PI+2*PI*y)/3;
        double e=sqrt(1+2*(1-cos(kx))*(1-cos(ky)));expected[ne++]=e;expected[ne++]=-e;
    }
    for(int i=0;i<18;i++)for(int j=i+1;j<18;j++)if(expected[j]<expected[i]){double t=expected[i];expected[i]=expected[j];expected[j]=t;}
    for(int i=0;i<18;i++)maxspec=fmax(maxspec,fabs(ev[i]-expected[i]));
    double eps=1e-5,maxder=0;Z hs[324],ht[324],plus[324],minus[324],dummy[324];
    comparison(3,.71,.42,hh,hs,ht,0);
    comparison(3,.71+eps,.42,plus,dummy,dd,0);comparison(3,.71-eps,.42,minus,dummy,dd,0);
    for(int i=0;i<324;i++)maxder=fmax(maxder,cabs((plus[i]-minus[i])/(2*eps)-ht[i]));
    printf("2D analytic flat-spectrum max discrepancy %.3g; comparison derivative finite-difference discrepancy %.3g\n",maxspec,maxder);
    if(maxspec>1e-12 || maxder>1e-8)exit(8);
    /* Actual weights: anti5=(-2,-2,-2,3,3); 10=(4,4,4,-1,-1,-1,-1,-1,-1,-6).
     * 3 left anti5 and one right 10; neutral spectators have zero response. */
    const double q[5]={-2,3,4,-1,-6},mult[5]={9,6,-3,-6,-1};
    double cur[3],ph[3];
    printf("2D loop: a=0.23+0.17 cos(t), b=0.37+0.17 sin(t), AP/AP; 1x1 -> 3x3\n");
    printf("nt,ns,current,coarse_phase_minus_fine_phase,residual,coarse_phase,fine_phase\n");
    for(int run=0;run<3;run++){
        int nt=128*(1<<run),ns=run==0?16:(run==1?24:40);double c=0,pc=0,pf=0;
        for(int i=0;i<5;i++){c+=mult[i]*current(q[i],nt,ns,0);pc+=mult[i]*phase(q[i],1,nt);pf+=mult[i]*phase(q[i],3,nt);}
        cur[run]=c;ph[run]=pc-pf;
        printf("%d,%d,%.15g,%.15g,%.6g,%.15g,%.15g\n",nt,ns,c,pc-pf,c-(pc-pf),pc,pf);fflush(stdout);
    }
    double extrap=(4*ph[2]-ph[1])/3;
    printf("2D Richardson endpoint estimate %.15g; current discrepancy %.6g\n",extrap,cur[2]-extrap);
    double wrong=0;for(int i=0;i<5;i++)wrong+=mult[i]*current(q[i],128,24,1);
    printf("2D missing-coarse-derivative control %.15g; discrepancy %.6g\n",wrong,wrong-extrap);
    printf("2D minimum sampled comparison gap %.15g\n",lowest_gap);
    printf("2D parameter Chern numbers: N,spin_x,spin_y,anti5,right10,physical,extra_anti5,random_frame_change\n");
    double maxerr=0;
    for(int N=32;N<=64;N*=2)for(int sx=-1;sx<=1;sx+=2)for(int sy=-1;sy<=1;sy+=2){
        double a=3*chern(-2,N,sx,sy,0)+2*chern(3,N,sx,sy,0);
        double b=-(3*chern(4,N,sx,sy,0)+6*chern(-1,N,sx,sy,0)+chern(-6,N,sx,sy,0));
        double ar=3*chern(-2,N,sx,sy,1)+2*chern(3,N,sx,sy,1);
        double err=fmax(fabs(a-30),fabs(b+90));if(err>maxerr)maxerr=err;
        printf("%d,%d,%d,%.12g,%.12g,%.6g,%.12g,%.3g\n",N,sx,sy,a,b,3*a+b,4*a+b,ar-a);
    }
    if(fabs(cur[2]-extrap)>1e-6 || fabs(wrong-extrap)<1e-4 || maxerr>1e-9)exit(7);
}
int main(int argc,char**argv) {
    init_gamma();setvbuf(stdout,NULL,_IOLBF,0);clock_t start=clock();
    if(argc==1 || strcmp(argv[1],"2d"))test4();
    if(argc==1 || strcmp(argv[1],"4d"))test2();
    printf("CPU seconds %.3f\n",(double)(clock()-start)/CLOCKS_PER_SEC);return 0;
}
