# Feedback B: ratio 29/33, nuclear masses, fission modes, charged Higgs

Source: transcript of a second agent's exchange with the author, pasted into the session of 12 November 2026.

The text between the tilde fences is the pasted block, unchanged, including the line breaks and the one-symbol-per-line artifacts that copying from a rendered page introduces. Nothing in it has been checked at this point; the checks are in ../notes/.

~~~~~~text
so... search vixra and internet for this exact relation M 
Z

 +M 
H

 

 =0.878840, 
2(132)
100+132

 = 
33
29

 =0.878788.

v=246.21965
for mh in [125.20,125.13,125.065,125.11]:
 r=(91.1879+mh)/v
 print(mh, r, r-29/33, (r-29/33)/r, (29/33*v-91.1879), (r-29/33)*v)
125.2 0.8788409048587308 5.3026070852002505e-05 6.033637096184796e-05 125.18694393939394 0.01305606060605526
125.13 0.8785566058598492 -0.0002312729280296022 -0.0002632419203122989 125.18694393939394 -0.056943939393923844
125.065 0.8782926139323162 -0.000495264855562616 -0.00056389504785336 125.18694393939394 -0.12194393939392786
125.11 0.8784753775744544 -0.00031250121342440984 -0.0003557313288475454 125.18694393939394 -0.07694393939393349
The numerical coincidence is remarkably close with the 2025 PDG masses, but the 2026 measurements make an important difference.

I interpret the relation as

M
Z
+
M
H
v
≃
100
+
132
2
(
132
)
=
29
33
v
M 
Z

 +M 
H

 

 ≃ 
2(132)
100+132

 = 
33
29

 

 
where 
v
=
(
2
G
F
)
−
1
/
2
≃
246.21965
v=( 
2

 G 
F

 ) 
−1/2
 ≃246.21965 GeV.

Using the 2025 Higgs mass 
M
H
=
125.20
M 
H

 =125.20 GeV and 
M
Z
=
91.1879
M 
Z

 =91.1879 GeV:

M
Z
+
M
H
v
=
0.87884090
,
29
33
=
0.87878788.
v
M 
Z

 +M 
H

 

 =0.87884090, 
33
29

 =0.87878788.
The relative discrepancy is only 0.0060%, corresponding to 13.1 MeV in the Higgs mass, much smaller than its experimental uncertainty.

The rational relation predicts

M
H
=
29
33
v
−
M
Z
=
125.18694
 
G
e
V
.
M 
H

 = 
33
29

 v−M 
Z

 =125.18694 GeV.

 
However, the PDG 2026 average is 
M
H
=
125.13
±
0.11
M 
H

 =125.13±0.11 GeV, while CMS announced a new determination on November 2, 2026, of 
125.065
±
0.088
125.065±0.088 GeV. The coincidence remains statistically compatible, but the central values have shifted away from the exceptionally close 2025 agreement. 
Particle Data Group
+2

What the literature search found
So far, I have not located a paper in viXra, arXiv, or the indexed web stating the complete relation between 
(
M
Z
+
M
H
)
/
v
(M 
Z

 +M 
H

 )/v and 
29
/
33
29/33.

There is, however, a particularly relevant nuclear result:

The 100:132 partition appears explicitly in theoretical work on hyperdeformed 
232
T
h
232
 Th. In the proposed dinuclear configuration,

232
T
h
⟶
132
S
n
+
100
Z
r
.
232
 Th⟶ 
132
 Sn+ 
100
 Zr.
The heavier fragment is doubly magic 
132
S
n
132
 Sn, while 
100
Z
r
100
 Zr is strongly deformed. A 2025 nuclear-physics dissertation describes this configuration at the third minimum of the potential-energy surface, and a 2026 study models the corresponding nuclear molecule. 
edoc.ub.uni-muenchen.de
+2

Thus the integers 100 and 132 are not an arbitrary partition of 232. They have an independent structural motivation in nuclear-fission theory. This does not establish the electroweak connection, but makes its precise formulation more interesting.

Closest identifiable precedents
1. Algora, Cseh, Darai & Hess (2006), Selection rule and energetic stability: Complementary aspects of nuclear clusterization. This is especially relevant: the authors explicitly identify the 
100
Z
r
+
132
S
n
100
 Zr+ 
132
 Sn partition with a maximum of the 
232
T
h
232
 Th fission mass distribution. They also analyze the constraints imposed by the Pauli principle and fragment deformation. 
SciELO México
Article (Revista Mexicana de Física)

.
2. McDonnell, Nazarewicz & Sheikh (2013), Third minima in thorium and uranium isotopes in a self-consistent theory, Physical Review C 87, 054327. They identify a dimolecular configuration involving doubly magic 
132
S
n
132
 Sn and a deformed Zr fragment. 
APS Journals
Original article

.
3. Castro (2013), viXra:1311.0101 discusses the proposal 
v
=
M
W
+
+
M
W
−
+
M
Z
v=M 
W 
+
 

 +M 
W 
−
 

 +M 
Z

 , but does not give the requested 
M
H
+
M
Z
M 
H

 +M 
Z

  relation. 
vixra.org

4. Fitch (2017), viXra:1709.0386, On the Sum of the Squares of the Particle Masses, discusses a different coincidence:

M
W
2
+
M
Z
2
+
M
H
2
≃
v
2
2
.
M 
W
2

 +M 
Z
2

 +M 
H
2

 ≃ 
2
v 
2
 

 .
It is conceptually related but not the same identity. 
vixra.org

Interpretation
The proposed electroweak equality would imply, at tree level,

g
2
+
g
′
2
2
+
2
λ
≃
29
33
.
2
g 
2
 +g 
′2
 

 

 + 
2λ

 ≃ 
33
29

 .
It therefore constrains the Higgs quartic coupling relative to the electroweak gauge couplings, a constraint not supplied by the Standard Model.

One technical qualification matters at the quoted precision: the PDG 
Z
Z-boson mass is a Breit–Wigner mass parameter, about 34 MeV above the corresponding propagator pole mass. That difference already exceeds the 13 MeV residual obtained from the 2025 averages. 
pdgprod.lbl.gov

Conclusion: I found substantial published support for the independently selected 100:132 nuclear partition, including a peer-reviewed analysis predating the Higgs discovery. I found no indexed precedent for equating that partition's normalized mass-number ratio with 
(
M
Z
+
M
H
)
/
v
(M 
Z

 +M 
H

 )/v. The cross-sector equality remains an empirical conjecture, not an established physical relation.

yeah the point with fussion is terrible because if you put the masses of 132Sb and 100Zr in GeV...

u=0.93149410242
me=0.000510998950
mSb=131.914508013*u
mZr=99.918010499*u
mSn=131.917823898*u
mTh=232.038053606*u
mPa=232.038590205*u
mh=125.13
mz=91.1879
v=246.21965
for name,x in [('Sb atomic',mSb),('Zr atomic',mZr),('Sn atomic',mSn),('Sb+Zr atomic',mSb+mZr),('Sn+Zr atomic',mSn+mZr),('Sb+Zr nuclear',mSb+mZr-91*me),('Sn+Zr nuclear',mSn+mZr-90*me),('2Sb nuclear',2*(mSb-51*me)),('Th atomic',mTh),('Pa atomic',mPa),('Z+H',mz+mh),('2Sb atomic',2*mSb),('Sb+Zr / 2 Sb', (mSb+mZr)/(2*mSb)),('Z+H / v',(mz+mh)/v),('rational',29/33)]:
    print(f'{name:24s} {x:.9f}')
print('difference atomic versus Z+H',mh+mz-(mSb+mZr))
print('difference nuclear versus Z+H',mh+mz-(mSb+mZr-91*me))
print('2Sb atomic - v',2*mSb-v,'2Sb nuclear -v',2*(mSb-51*me)-v)
print('Z+H - v*(29/33)',mh+mz-v*29/33)
print('Q pa', (mPa-(mSb+mZr))*1000, 'Q th',(mTh-(mSn+mZr))*1000)
Sb atomic                122.877586238
Zr atomic                93.073037505
Sn atomic                122.880674965
Sb+Zr atomic             215.950623743
Sn+Zr atomic             215.953712470
Sb+Zr nuclear            215.904122839
Sn+Zr nuclear            215.907722565
2Sb nuclear              245.703050583
Th atomic                216.142078471
Pa atomic                216.142578310
Z+H                      216.317900000
2Sb atomic               245.755172475
Sb+Zr / 2 Sb             0.878722598
Z+H / v                  0.878556606
rational                 0.878787879
difference atomic versus Z+H 0.3672762568965595
difference nuclear versus Z+H 0.41377716134655884
2Sb atomic - v -0.46447752450936264 2Sb nuclear -v -0.5165994174093669
Z+H - v*(29/33) -0.05694393939393194
Q pa 191.9545667052205 Q th 188.3660005795491

mSbN=mSb-51*me
mZrN=mZr-40*me
mSnN=mSn-50*me
mThN=mTh-90*me
mPaN=mPa-91*me
x=(mSbN+mZrN)/(2*mSbN)
y=(mSnN+mZrN)/(2*mSnN)
print(mSbN,mZrN,mSnN,mThN,mPaN)
print(x,y)
print('mass gaps:')
print('Z+H2025',91.1879+125.20)
print('v-2*sbN',v-2*mSbN)
print('Z+H - (sum)',mh+mz-(mSbN+mZrN))
print('Q 232Th', (mThN-mSnN-mZrN)*1000)
print('Q 232Pa', (mPaN-mSbN-mZrN)*1000)
print('equal MH from fission','MHpred =',mThN+(mThN-mSnN-mZrN)- (91.1879-.034))
122.85152529129532 93.05259754735815 122.85512501756713 216.09608856550483 216.09607740535867
0.8787197486018979 0.8787086518940601
mass gaps:
Z+H2025 216.3879
v-2*sbN 0.5165994174093669
Z+H - (sum) 0.41377716134655884
Q 232Th 188.3660005795491
Q 232Pa 191.95456670520628
equal MH from fission MHpred = 125.13055456608438

def be_e(Z):
    return (14.4381*Z**2.39+1.55468e-6*Z**5.35)*1e-9 # GeV
for z in [40,50,51,90,91]:
    print(z,be_e(z)*1000,'MeV')
print('corrected nuclear masses')
Sbn=mSb-51*me+be_e(51)
Zrn=mZr-40*me+be_e(40)
Snn=mSn-50*me+be_e(50)
Thn=mTh-90*me+be_e(90)
Pan=mPa-91*me+be_e(91)
for name,vv in [('sb',Sbn),('zr',Zrn),('sn',Snn),('Th',Thn),('Pa',Pan),('Sn+Zr',Snn+Zrn),('Sb+Zr',Sbn+Zrn)]:
    print(name,round(vv,9))
qth=(Thn-Snn-Zrn)
qpa=(Pan-Sbn-Zrn)
print('Qth',qth*1000,'Qpa',qpa*1000)
print('pred mh pole',Thn+qth-(mz-.034))
print('pred mh BW',Thn+qth-mz)
40 0.09795082862197253 MeV
50 0.16788759756305655 MeV
51 0.17614537945466718 MeV
90 0.7206603352790935 MeV
91 0.7414596979622787 MeV
corrected nuclear masses
sb 122.851701437
zr 93.052695498
sn 122.855292905
Th 216.096809226
Pa 216.096818865
Sn+Zr 215.907988403
Sb+Zr 215.904396935
Qth 188.82082248863696 Qpa 192.42193019509557
pred mh pole 125.13173004832876
pred mh BW 125.09773004832876

ratio_pair=(Sbn+Zrn)/(2*Sbn)
ratio_HZ=(mh+mz)/v
print(ratio_pair, ratio_HZ,29/33)
print('delta relative pair vs hz',((Sbn+Zrn)-(mh+mz))/(mh+mz)*100)
print('relative for v', (2*Sbn-v)/v*100)
print('mh prediction', (2*Thn-Snn-Zrn)-(mz-.034))
print('mass ratio Sn', (Snn+Zrn)/(2*Snn))
0.8787196042463921 0.8785566058598492 0.8787878787878788
delta relative pair vs hz -0.19115526969264068
relative for v -0.20966934468896178
mh prediction 125.13173004832876
mass ratio Sn 0.8787085330137816
Yes. Using the actual nuclear masses makes the coincidence more unsettling: the 
132
S
b
+
100
Z
r
132
 Sb+ 
100
 Zr system lies close to 
M
H
+
M
Z
M 
H

 +M 
Z

 , while twice the mass of 
132
S
b
132
 Sb lies close to the Higgs vacuum expectation value 
v
v.

From AME2020, converting atomic to nuclear masses (including the approximate electron-binding correction): 
amdc.impcas.ac.cn
+2

Quantity

Mass (GeV)

132
S
b
132
 Sb nucleus

122.85170

100
Z
r
100
 Zr nucleus

93.05270

Sum of fragments

215.90440

M
H
+
M
Z
M 
H

 +M 
Z

  (PDG 2026)

216.31790

2
M
(
132
S
b
)
2M( 
132
 Sb)

245.70340

Higgs VEV 
v
v

246.21965

pdgprod.lbl.gov
+1
Consequently,

M
(
132
S
b
)
+
M
(
100
Z
r
)
2
M
(
132
S
b
)
=
0.8787196
2M( 
132
 Sb)
M( 
132
 Sb)+M( 
100
 Zr)

 =0.8787196
compared with

M
H
+
M
Z
v
=
0.8785566
,
29
33
=
0.8787879.
v
M 
H

 +M 
Z

 

 =0.8785566, 
33
29

 =0.8787879.
The two absolute mass correspondences have discrepancies of just 0.19% and 0.21%, respectively.

The fission-energy coincidence
There is another numerical feature.

The particularly interesting configuration in the fission literature is actually

232
T
h
→
132
S
n
+
100
Z
r
,
232
 Th→ 
132
 Sn+ 
100
 Zr,
rather than Sb. The Sn nucleus is doubly magic, and the charges add to thorium's 90. The Sb alternative has charge 91 and corresponds to a protactinium parent.

For the thorium partition, AME2020 gives approximately

Q
f
i
s
s
i
o
n
=
188.8
 
M
e
V
.
Q 
fission

 =188.8 MeV.
Now, if we use the propagator-pole mass of the Z, approximately 34 MeV below the tabulated Breit–Wigner mass, something curious happens:

M
H
+
M
Z
p
o
l
e
−
M
(
232
T
h
)
≃
187.1
 
M
e
V
.
M 
H

 +M 
Z
pole

 −M( 
232
 Th)≃187.1 MeV.
That is only 1.7 MeV away from the calculated fission Q-value.

Equivalently,

M
H
≃
2
M
(
232
T
h
)
−
M
(
132
S
n
)
−
M
(
100
Z
r
)
−
M
Z
p
o
l
e
M 
H

 ≃2M( 
232
 Th)−M( 
132
 Sn)−M( 
100
 Zr)−M 
Z
pole

 
gives

M
H
p
r
e
d
i
c
t
e
d
≃
125.132
 
G
e
V
M 
H
predicted

 ≃125.132 GeV

 
against the PDG 2026 average 
125.13
±
0.11
125.13±0.11 GeV.

This last agreement is extremely sensitive to conventions, and the Higgs experimental uncertainty is about 65 times the residual. I would therefore not regard the MeV-level match as significant evidence.

Physical interpretation
The important distinction is that the rest mass of a fissioning nucleus is not its available decay energy. The available energy is about 0.19 GeV, not 216 GeV. Moreover, an 
H
Z
HZ final state has zero baryon number, whereas the nucleus has baryon number 232. Ordinary fission cannot convert one into the other.

Nevertheless, the numerical alignment is real, and the non-arbitrary selection of 
132
S
n
132
 Sn by shell structure gives the observation more substance than an unconstrained search over mass partitions.

The challenge is to identify a mechanism sensitive to the electroweak scales through nuclear structure or deformation, rather than merely through total nuclear rest mass. At present the numbers establish a coincidence, not such a mechanism.

Yeah, I know. There is not such a mechanism that increases fission when the two pieces are electroweak bosons. Say that it enhances asymmetry of the father nucleus
That is a substantially different hypothesis. The proposed effect is not an enhanced decay into two electroweak bosons, but an enhancement of the reflection-asymmetric deformation of the parent nucleus when its mass approaches 
M
H
+
M
Z
M 
H

 +M 
Z

 .

In nuclear-fission terminology, the relevant collective coordinate is the octupole deformation 
β
3
β 
3

 , coupled to the quadrupole elongation 
β
2
β 
2

 . A phenomenological description would be

V
(
β
2
,
β
3
;
A
,
Z
)
=
V
0
(
β
2
;
A
,
Z
)
+
1
2
C
3
(
β
2
;
A
,
Z
)
β
3
2
+
1
4
D
3
β
3
4
+
⋯
 
.
V(β 
2

 ,β 
3

 ;A,Z)=V 
0

 (β 
2

 ;A,Z)+ 
2
1

 C 
3

 (β 
2

 ;A,Z)β 
3
2

 + 
4
1

 D 
3

 β 
3
4

 +⋯.
The conjecture is that an additional contribution makes 
C
3
C 
3

  more negative for parent nuclei whose rest masses lie near the electroweak scale 
M
H
+
M
Z
M 
H

 +M 
Z

 . This would favor asymmetric shapes and potentially asymmetric fission, without requiring electroweak bosons in the final state.

Importantly, reflection symmetry remains intact: configurations with 
+
β
3
+β 
3

  and 
−
β
3
−β 
3

  are equivalent. What changes is the preferred magnitude 
∣
β
3
∣
∣β 
3

 ∣, not a preference for one spatial direction.

There is a particularly clean way to express this. Define the fragment mass asymmetry

η
=
A
H
−
A
L
A
H
+
A
L
.
η= 
A 
H

 +A 
L

 
A 
H

 −A 
L

 

 .
Then the original numerical relation becomes

η
E
W
≡
v
M
H
+
M
Z
−
1
≃
132
−
100
232
=
4
29
.
η 
EW

 ≡ 
M 
H

 +M 
Z

 
v

 −1≃ 
232
132−100

 = 
29
4

 .

 
With the PDG 2026 masses,

η
E
W
=
0.138231
,
η
n
u
c
l
e
a
r
=
0.137931.
η 
EW

 =0.138231,η 
nuclear

 =0.137931.
For a parent with 
A
=
232
A=232, this corresponds to a predicted split

A
H
=
132.035
,
A
L
=
99.965.
A 
H

 =132.035,A 
L

 =99.965.

 
Thus the proposed effect has two aspects: the parent mass near 
M
H
+
M
Z
M 
H

 +M 
Z

  would favor the asymmetric deformation, while the electroweak ratio would set a preferred degree of mass asymmetry.

There is already an established nuclear mechanism favoring asymmetric fission: shell effects and octupole deformation. Scamps and Simenel (2018) demonstrate how pear-shaped fragments affect fission asymmetry, while McDonnell et al. (2013) specifically investigate the reflection-asymmetric 
232
T
h
232
 Th configurations associated with 
132
S
n
+
100
Z
r
132
 Sn+ 
100
 Zr. 
Nature
+1

The distinction is therefore between the known shell-driven asymmetric fission valley and a conjectured additional electroweak contribution to its stability.

The strongest possible evidence would not be the agreement for one nucleus, but an anomalous enhancement of asymmetric fission around the parent mass 
M
H
+
M
Z
M 
H

 +M 
Z

 , relative to nuclear models incorporating ordinary shell effects. That remains unestablished.

if you do stats for all the known fission decays, it is always the same: the high lobe at H, the low gaussian between W and Z

import pandas as pd
A = [('Th-232 (fast n)',92,139),('U-233 (thermal n)',94,138),('U-235 (thermal n)',95,139),('U-238 (fast n)',98,139),('Pu-239 (thermal n)',99,138),('Cm-242 (spont.)',103,136),('Cf-252 (spont.)',108,139)]
df=pd.DataFrame(A,columns=['Parent','Al','Ah'])
df['light_GeV']=(df.Al*0.9306).round(1)
df['heavy_GeV']=(df.Ah*0.9306).round(1)
df
               Parent   Al   Ah  light_GeV  heavy_GeV
0     Th-232 (fast n)   92  139       85.6      129.4
1   U-233 (thermal n)   94  138       87.5      128.4
2   U-235 (thermal n)   95  139       88.4      129.4
3      U-238 (fast n)   98  139       91.2      129.4
4  Pu-239 (thermal n)   99  138       92.1      128.4
5     Cm-242 (spont.)  103  136       95.9      126.6
6     Cf-252 (spont.)  108  139      100.5      129.4
There is a genuine regularity in the fission data, but the precise statement is slightly different:

Across ordinary low-energy actinide fission, the heavy-fragment mass distribution remains approximately fixed, while the light-fragment distribution shifts with the mass of the fissioning nucleus.

This is well established experimentally and theoretically. A systematic study in European Physical Journal A explicitly identifies the nearly constant heavy-fragment mass around 
A
≃
140
A≃140, with the light fragment becoming heavier as the parent mass increases. 
Springer

Converting to GeV gives

A
H
≃
140
⇒
m
H
f
r
a
g
≃
130
 
G
e
V
,
A 
H

 ≃140⇒m 
H
frag

 ≃130 GeV,
which is close to, but systematically above, the Higgs mass of about 125.1 GeV.

So the important observation is a persistent concentration of fission yields in the electroweak mass region, rather than an exact peak at the Higgs mass.

A numerical comparison across seven fissioning systems
Earl K. Hyde's 1962 review compiled the modal mass numbers for several actinides. Converting them with 
m
n
u
c
l
e
u
s
≃
0.9306
A
m 
nucleus

 ≃0.9306A GeV gives:

Fissioning system

Light peak (GeV)

Heavy peak (GeV)

232
T
h
232
 Th, fast n

85.6

129.4

233
U
233
 U, thermal n

87.5

128.4

235
U
235
 U, thermal n

88.4

129.4

238
U
238
 U, fast n

91.2

129.4

239
P
u
239
 Pu, thermal n

92.1

128.4

242
C
m
242
 Cm, spontaneous

95.9

126.6

252
C
f
252
 Cf, spontaneous

100.5

129.4

Approximate GeV conversions of the historical peak mass numbers, not individual isotope mass measurements. Source: Hyde, A Revised Version of a Review of Nuclear Fission, Table 11.11/11.12. 
EsScholarship
+1
Fission peaks versus electroweak masses
Seven historical low-energy actinide fission datasets; approximate conversion 0.9306 GeV per mass number.


Heavy fragment

Light fragment

Higgs mass

Z mass

W mass
70
87,5
105
122,5
140
Th-232
U-233
U-235
U-238
Pu-239
Cm-242
Cf-252
Th-232: Heavy fragment 129,4, Light fragment 85,6, Higgs mass 125,1, Z mass 91,2, W mass 80,4
U-233: Heavy fragment 128,4, Light fragment 87,5, Higgs mass 125,1, Z mass 91,2, W mass 80,4
U-235: Heavy fragment 129,4, Light fragment 88,4, Higgs mass 125,1, Z mass 91,2, W mass 80,4
U-238: Heavy fragment 129,4, Light fragment 91,2, Higgs mass 125,1, Z mass 91,2, W mass 80,4
Pu-239: Heavy fragment 128,4, Light fragment 92,1, Higgs mass 125,1, Z mass 91,2, W mass 80,4
Cm-242: Heavy fragment 126,6, Light fragment 95,9, Higgs mass 125,1, Z mass 91,2, W mass 80,4
Cf-252: Heavy fragment 129,4, Light fragment 100,5, Higgs mass 125,1, Z mass 91,2, W mass 80,4
There is one particularly interesting refinement from modern fission studies.

The heavy distribution is not simply one Gaussian. It contains two conventional asymmetric fission modes:

Standard I (S1), near 
A
H
=
134
A 
H

 =134, corresponding to approximately 124.7 GeV, very close to 
M
H
M 
H

 .

Standard II (S2), near 
A
H
=
144
A 
H

 =144, corresponding to approximately 134.0 GeV.

Their superposition produces the broad maximum around 
A
≃
140
A≃140. A 2024 high-precision evaluation of 
235
U
235
 U indeed resolves structures at masses 134, 138 and 143–144. 
ScienceDirect
+1

That means the Higgs mass is close to one of the resolved heavy-fragment modes, even though it is not generally the position of the overall heavy maximum.

For the light fragment, the correspondence with the W–Z interval holds for four of these seven historical cases. It breaks progressively for heavier actinides, particularly curium and californium.

And there are definite exceptions to any universal statement: 
258
F
m
258
 Fm predominantly undergoes symmetric fission, while 
180
H
g
180
 Hg has asymmetric peaks near 
A
=
80
A=80 and 
A
=
100
A=100, far from the Higgs mass. 
APS Journals
+1

Implications for the conjecture
The most suggestive numerical feature is therefore

M
H
≃
M
n
u
c
l
e
a
r
(
A
=
134
)
M 
H

 ≃M 
nuclear

 (A=134)

 
together with the occurrence of a light-fragment maximum between 
M
W
M 
W

  and 
M
Z
M 
Z

  in the lighter actinides.

But the established explanation is already quite specific: shell-stabilized asymmetric modes, including octupole deformation, produce the heavy structures. The electroweak conjecture would have to explain a residual not accounted for by those effects.

I would distinguish an experimentally established near-stationary heavy-fragment mode, which the evidence strongly supports, from a universal alignment of the two modes with H and W–Z, which these seven examples already contradict.

This is a comparison of seven published systems, not a statistical reduction of every evaluated fission-yield dataset.

Ah yes it is the standard S1.  Not sure why, no idea what the second mode is. Waiting for the h0 to be discovered at 134 but not... or not yet.  So the question is, is there some mechanism that makes the Z0 and H0 see the whole nuclear mass? For instance, higgs nucleon coupling goes with the nucleon mass, due to anomalies, instead of quark mass. for the z0 no idea.

import math
hbarc=.1973269804 # GeV fm
rho=.16*hbarc**3
mh=125.13;mz=91.1876;v=246.22;mn=.939;f=.308
sin2=.2386
g_h=f*mn/v
gZ=0.653/(4*0.8815)
# gZ vector coefficient for Qw = g/(4 c_w)
rho_w_scale=(.61-(1-4*sin2)*.39)
VhA=g_h*g_h*rho/(2*mh*mh) # geV/A
VzA=gZ*gZ*rho*rho_w_scale**2/(2*mz*mz)
VhA*1e9, VzA*1e9, g_h, gZ, rho, 1e3*hbarc/mh, 1e3*hbarc/mz, VhA*1e9*232,VzA*1e9*232, rho_w_scale
(5.4164217312574706e-05,
 0.8892008030803557,
 0.0011746080740800907,
 0.185195689166194,
 0.0012293608911126156,
 1.5769757883800848,
 2.163967254319666,
 0.012566098416517332,
 206.29458631464252,
 0.592216)
Yes. Both the Higgs and the 
Z
0
Z 
0
  can couple coherently to an entire nucleus, although through different operators. The Higgs connection to the QCD trace anomaly is particularly interesting here. The main difficulty is that coherent coupling does not automatically generate a resonance when a nuclear rest mass coincides with an electroweak boson mass.

1. Higgs: the nucleon mass, not just its valence-quark masses
At low momentum transfer, integrating out the heavy quarks produces the effective scalar interaction

L
h
N
N
=
−
f
N
m
N
v
 
h
N
ˉ
N
,
L 
hNN

 =− 
v
f 
N

 m 
N

 

 h 
N
ˉ
 N,
where

f
N
=
∑
q
=
u
,
d
,
s
f
T
q
+
2
9
(
1
−
∑
q
=
u
,
d
,
s
f
T
q
)
.
f 
N

 = 
q=u,d,s
∑

 f 
Tq

 + 
9
2

  

 1− 
q=u,d,s
∑

 f 
Tq

  

 .
The 
2
/
9
2/9 contribution comes from integrating out the 
c
,
b
,
t
c,b,t quarks and using the QCD trace anomaly. A representative modern determination gives

f
N
=
0.308
(
18
)
.
f 
N

 =0.308(18).
Thus the Higgs couples much more strongly to a nucleon than a calculation using only its light valence-quark Yukawa couplings would suggest. However, it does not couple with strength 
m
N
/
v
m 
N

 /v, but approximately 
0.3
m
N
/
v
0.3m 
N

 /v. 
PubMed
+1

For an entire nucleus, the zero-momentum scalar response is approximately

g
h
A
A
≃
f
p
Z
m
p
+
f
n
N
m
n
v
−
∂
B
(
A
,
Z
)
∂
v
g 
hAA

 ≃ 
v
f 
p

 Zm 
p

 +f 
n

 Nm 
n

 

 − 
∂v
∂B(A,Z)

 

 
where 
B
B is its nuclear binding energy. The derivative is taken with dimensionless Standard Model couplings held fixed at a specified high-energy scale.

The second term is especially relevant to nuclear deformation: the Higgs couples not only to individual nucleons, but also to the quark-mass dependence of their nuclear interactions.

Indeed, two-nucleon scalar currents generated by pion exchange are explicitly known in chiral EFT. Krebs, Epelbaum and Meißner derived their higher-order contributions in 2020. 
Springer

So there is a mathematically well-defined route from the Higgs field to the collective nuclear potential-energy surface.

2. The 
Z
0
Z 
0
 : a coherent coupling predominantly to neutrons
The corresponding quantity for the 
Z
0
Z 
0
  is the weak nuclear charge,

Q
W
=
N
−
(
1
−
4
sin

2
θ
W
)
Z
.
Q 
W

 =N−(1−4sin 
2
 θ 
W

 )Z.

 
At low momentum transfer, the neutral-current amplitude contains

Q
W
F
W
(
q
2
)
,
Q 
W

 F 
W

 (q 
2
 ),
with 
F
W
(
0
)
=
1
F 
W

 (0)=1.

Because the proton weak charge is small, the 
Z
0
Z 
0
  couples predominantly to the total neutron number. For heavy nuclei, 
N
N scales roughly with nuclear mass, although it is not the mass itself.

This is not hypothetical coherence. It has been demonstrated experimentally through coherent elastic neutrino–nucleus scattering, whose leading cross section scales approximately as 
N
2
N 
2
 . 
Oak Ridge National Laboratory
+1

Consequently:

Field

Coherent nuclear quantity

Sensitive to

Higgs 
h
h

Scalar density and QCD mass response

A
A, binding, scalar nuclear forces

Z
0
Z 
0
 , vector

Weak-charge density

Primarily 
N
N, neutron distribution

Z
0
Z 
0
 , axial

Nuclear spin and axial currents

Spin, parity-dependent transitions

The two fields therefore probe different aspects of the nuclear density, and both can respond to nuclear deformation.

3. Could either field enhance asymmetric fission?
Here comes the difficulty: the propagators of both fields make their direct nuclear interactions extremely short-ranged.

ℏ
c
M
H
=
0.00158
 
f
m
,
ℏ
c
M
Z
=
0.00216
 
f
m
.
M 
H

 
ℏc

 =0.00158 fm, 
M 
Z

 
ℏc

 =0.00216 fm.
For comparison, inter-nucleon separations are of order 1–2 fm.

Integrating out the two bosons gives schematic static energy contributions

Δ
E
h
≃
−
g
h
N
2
2
M
H
2
∫
d
3
x
 
ρ
s
(
x
)
2
ΔE 
h

 ≃− 
2M 
H
2

 
g 
hN
2

 

 ∫d 
3
 xρ 
s

 (x) 
2
 
and

Δ
E
Z
≃
+
g
Z
W
2
2
M
Z
2
∫
d
3
x
 
[
ρ
n
(
x
)
−
ϵ
ρ
p
(
x
)
]
2
,
ΔE 
Z

 ≃+ 
2M 
Z
2

 
g 
ZW
2

 

 ∫d 
3
 x[ρ 
n

 (x)−ϵρ 
p

 (x)] 
2
 ,
where 
ϵ
=
1
−
4
sin

2
θ
W
ϵ=1−4sin 
2
 θ 
W

  and 
g
Z
W
=
g
/
(
4
cos

θ
W
)
g 
ZW

 =g/(4cosθ 
W

 ).

A crude uncorrelated nuclear-matter estimate at 
ρ
B
=
0.16
 
f
m
−
3
ρ 
B

 =0.16 fm 
−3
  gives:

Contribution

Energy per nucleon

For 
A
=
232
A=232

Higgs exchange

∼
5
×
10
−
5
∼5×10 
−5
  eV

∼
0.013
∼0.013 eV

Z vector exchange

∼
0.9
∼0.9 eV

∼
200
∼200 eV

These are mean-field scale estimates, not precision nuclear energies; short-distance correlations alter the results. Both are far below MeV-scale fission barriers.

More importantly, for an approximately incompressible nucleus,

∫
ρ
2
 
d
3
x
≈
ρ
0
A
.
∫ρ 
2
 d 
3
 x≈ρ 
0

 A.
Thus the leading local energy depends on the number of nucleons, but hardly on the nuclear shape. Its ability to favor an octupole-deformed configuration would be even smaller.

There is also an explicit 
h
Z
Z
hZZ vertex in the Standard Model. It permits higher-order effective interactions involving the scalar density and squared weak-charge density, schematically 
ρ
s
ρ
W
2
ρ 
s

 ρ 
W
2

 . These are legitimate combined Higgs–Z contributions, but much more suppressed.

4. A more interesting connection: octupole deformation and weak currents
The S1/S2 distinction has a particularly relevant modern development.

Historically, S1 was associated with the spherical shell closure near 
N
=
82
N=82, whereas S2 was often associated with a deformed closure near 
N
=
88
N=88. More recent fragment-charge systematics instead find concentrations near 
Z
f
r
a
g
≃
52.5
Z 
frag

 ≃52.5 for S1 and 
Z
f
r
a
g
≃
55
Z 
frag

 ≃55 for S2.

Microscopic calculations associate both with octupole-deformed proton shell gaps, notably around 
Z
=
52
Z=52 and 
Z
=
56
Z=56. 
ScienceDirect
+2

That gives an interesting overlap with electroweak physics: weak nuclear interactions can mix opposite-parity states, and octupole-deformed nuclei can exhibit strongly enhanced sensitivity to parity-violating perturbations when the relevant parity doublets are close in energy. 
DOI
+1

But this enhances certain observables, not necessarily the fission probability. There is no established amplification large enough to turn the ordinary weak neutral current into a major contribution to the fission potential.

A genuinely longer-range Standard Model effect also exists: exchange of two neutrinos produces a weak-charge-dependent 
G
F
2
/
r
5
G 
F
2

 /r 
5
  potential. Unfortunately, that is even more suppressed at nuclear distances. 
DOI

5. Why matching the nuclear mass to 
M
H
+
M
Z
M 
H

 +M 
Z

  does not create a resonance
The distinction is kinematic. In low-energy nuclear processes, the exchanged electroweak bosons carry comparatively small momentum. Their propagators contain

1
q
2
−
M
H
2
,
1
q
2
−
M
Z
2
,
q 
2
 −M 
H
2

 
1

 , 
q 
2
 −M 
Z
2

 
1

 ,
not denominators of the form

1
M
A
2
−
(
M
H
+
M
Z
)
2
.
M 
A
2

 −(M 
H

 +M 
Z

 ) 
2
 
1

 .
Moreover, a nucleus cannot mix with a state consisting solely of 
H
+
Z
H+Z: baryon number forbids it. An intermediate state with the same baryon number plus 
H
+
Z
H+Z would have a threshold approximately 216 GeV above the nuclear ground-state mass.

Consequently, the near equality 
M
A
≃
M
H
+
M
Z
M 
A

 ≃M 
H

 +M 
Z

  supplies no resonance in the known theory.

Assessment
The scalar and weak-vector couplings establish something important: both fields really do interact with collective nuclear quantities. It would be incorrect to dismiss the possibility by saying that electroweak fields can only see individual valence quarks.

But three distinct steps remain:

Coherent sensitivity to nuclear constituents — established.

A sufficiently large deformation-dependent electroweak contribution — not established; conventional estimates are tiny.

An enhancement specifically when the nuclear mass reaches 
M
H
+
M
Z
M 
H

 +M 
Z

 , or the fragment mass reaches 
M
H
M 
H

  — no known mechanism.

The QCD anomaly helps with the first step, not the third. In fact, a hypothetical scalar coupled directly to the full trace 
T
μ
μ
T 
μ
  
μ

 , rather than the Higgs Yukawa operator, would track the entire nuclear mass more closely. The 
Z
0
Z 
0
 , being a vector, has no corresponding scalar mass coupling.

The intriguing physical coincidence therefore remains the proximity of the S1 shell-stabilized fragment to 
M
H
M 
H

 , with a substantially different S2 mode nearby. Standard nuclear theory explains why those two modes exist; it does not connect their mass scales to the Higgs or Z masses.

Oh,  in July 2025. Berrocal gave a talk at the ATLAS HMBS and Exotics Workshop in Edinburgh entitled:


“From Hint to Breakthrough: Turning a 3σ Charged Higgs Signal into a >5σ Discovery.”


This is documented in the IFAE 2025 talks register. The title indicates that the group was actively pursuing a decisive test, not that a \(5\sigma\) result had already been obtained. I could not find public slides revealing the outcome. 
Talks & Posters


4. The programme now includes a second, broader analysis. The 2025 report distinguishes the Run 2 + partial Run 3 \(cb\) follow-up, intended for publication in 2026, from a newer combined \(cb/cs\) analysis planned with the complete Run 3 dataset.

This is an interesting development, particularly given our discussion of the two standard asymmetric fission modes.

I verified the original sources. ATLAS really did observe a charged-Higgs excess near 130 GeV, and the July 2025 Edinburgh talk by Adrià Berrocal is listed exactly as you report. But it was a programme for turning the hint into a discovery, not a discovery announcement. 
Talks & Posters
+1

The experimental situation is:

Result

Status

ATLAS Run 2, 
H
±
→
c
b
H 
±
 →cb

3.0
σ
3.0σ local

Global significance

2.5
σ
2.5σ

Candidate mass

∼
130
∼130 GeV

Run 2 + partial Run 3 follow-up

Planned for publication in 2026

Combined 
H
±
→
c
b
/
c
s
H 
±
 →cb/cs

Separate analysis using full Run 3

The original publication is JHEP 09 (2023) 004. The IFAE annual report explicitly confirms both follow-up analyses. 
Repositorio UAM
+2

As of November 11, 2026, I have not found an announced ATLAS result resolving the 130 GeV 
c
b
cb excess. That is an absence from the public sources I checked, not evidence that the internal analysis has succeeded or failed.

The curious correspondence with the fission modes
Standard I (S1)

A ≈ 134
≈ 124.8 GeV
Near the known neutral Higgs, 125.13 GeV

Standard II (S2)

A ≈ 140–144
≈ 130–134 GeV
Includes the tentative charged-Higgs mass of 130 GeV

The S2 position depends on the fissioning system and the modal decomposition. Both 
A
≃
140
A≃140 and 
A
≃
144
A≃144 occur in published descriptions. 
www-pub.iaea.org
+1

There is also new theoretical work: Aranda, Hernández-Sánchez, Montiel and Noriega-Papaqui published a paper in Physics Letters B in 2026 constructing a 
Z
3
Z 
3

 -flavoured two-Higgs-doublet model that can reproduce the ATLAS 130 GeV excess. This demonstrates theoretical viability within a particular extended Higgs sector; it is not independent experimental confirmation. 
Flavored two Higgs doublet models
+1

One essential qualification for our earlier discussion: an 
H
±
H 
±
  has charged-current couplings rather than the neutral scalar coupling to the nucleon mass generated through the QCD trace anomaly. A charged Higgs cannot develop a diagonal expectation value in an ordinary nucleus without changing its electric charge.

So there is an intriguing numerical pattern involving both fission modes and two scalar mass scales, but even confirmation of the charged 130 GeV state would not establish the proposed nuclear coupling or a neutral 
h
0
h 
0
  at 134 GeV.

Yeah but in the lower gaussian we have W - Z as range, so a charged in the upper is sort of symmetric. What ae the S1 and S2 modes, are they well characterised or is it just a mathematical fit?
S1 and S2 are experimentally motivated structures, not merely two arbitrary Gaussians. But whether they correspond to two genuinely distinct fission pathways is still unsettled.

In fact, a March 2025 paper by Patrick McGlynn and Cédric Simenel addresses almost exactly your question. Their conclusion is that S1 and S2 can belong to the same potential-energy valley, even though experimental mass distributions are conventionally fitted with two Gaussian components. 
APS Journals

1. What distinguishes the modes experimentally?
The Brosa classification describes several competing scission configurations. For ordinary actinides, the main ones are:

Property

Standard I (S1)

Standard II (S2)

Heavy fragment 
A
H
A 
H

 

~134

~140–144

Heavy fragment 
Z
H
Z 
H

 

~52–53

~55

Approximate mass

124.7 GeV

130–134 GeV

Total kinetic energy

Higher

Typically 10–20 MeV lower

Scission configuration

More compact

More elongated/deformed

Traditional explanation

Near spherical 
Z
=
50
,
N
=
82
Z=50,N=82 shells

Deformed shell effects

Modern interpretation

Proton octupole shells near 
Z
=
52
Z=52

Proton octupole shells near 
Z
=
56
Z=56

These are characteristic locations and tendencies, not sharp quantum numbers. A representative decomposition of thermal-neutron fission of 
235
U
235
 U gives approximately 187 MeV for S1 and 167 MeV for S2, versus 157 MeV for the symmetric superlong mode. 
ScienceDirect
+2

The kinetic-energy difference is crucial: the evidence is not restricted to fitting the fragment mass spectrum. There are correlated differences in kinetic energy and fragment excitation, reflected in prompt-neutron emission.

2. What is actually responsible for S1 and S2?
The traditional explanation invoked two different shell structures.

S1: The heavy fragment forms near doubly magic 
132
S
n
132
 Sn, with 
Z
=
50
Z=50, 
N
=
82
N=82. The fragment is relatively compact, giving greater Coulomb repulsion at scission and therefore higher kinetic energy.

S2: The heavy fragment is more deformed. Historically, a neutron shell gap around 
N
=
88
N=88 was invoked, together with proton shell effects near 
Z
=
54
Z=54–56.

However, the modern understanding has changed substantially.


Illustrative S1/S2 decomposition of an asymmetric fission mass distribution. The individual components are model-dependent; only their sum is directly measured.
A particularly influential result is that the heavy-fragment charge distributions remain concentrated around 
Z
≃
52.5
Z≃52.5 and 
Z
≃
55
Z≃55, even as the parent nucleus changes.

This shifted the emphasis from neutron shell closures to proton shell effects, particularly octupole-deformed shell gaps near 
Z
=
52
Z=52 and 
Z
=
56
Z=56. 
ScienceDirect
+1

There is recent experimental support: a January 2025 study of thermal-neutron-induced 
235
U
235
 U fission combined fragment charge, mass and neutron-multiplicity measurements, finding evidence for the influence of proton shell closures at 
Z
=
52
Z=52 and approximately 
56
56, alongside neutron shell effects. 
ScienceDirect

This makes S1 and S2 substantially better characterized than a purely numerical fit.

3. But are there really two different valleys?
This is the important caveat.

McGlynn and Simenel, in Physical Review C 111, 034619 (2025), demonstrate that an anharmonic potential with a single minimum can generate a mass-yield distribution that requires several Gaussians to fit.

Schematically, if one approximates a scission distribution by

Y
(
q
)
∝
exp

[
−
V
e
f
f
(
q
)
/
T
e
f
f
]
,
Y(q)∝exp[−V 
eff

 (q)/T 
eff

 ],
then a nonquadratic 
V
e
f
f
(
q
)
V 
eff

 (q) produces a non-Gaussian yield without requiring multiple potential minima.

Their particularly relevant result is that the usual S1 and S2 components can occupy one effective potential well. 
APS Journals

The 2025 review of microscopic nuclear dynamics reaches a compatible conclusion: S1 and S2 may reflect different shell effects and different scission configurations while belonging to the same overall asymmetric fission valley. 
Springer

In other words, the phenomenological distinction is useful and physically informative, but interpreting S1 and S2 as independent dynamical channels is stronger than the present evidence warrants.

4. Consequences for the electroweak comparison
The mass correspondences are certainly suggestive:

S
1
:
A
H
≃
134
⟷
M
h
0
≃
125
 
G
e
V
,
S
2
:
A
H
≃
140
⟷
M
H
±
c
a
n
d
i
d
a
t
e
≃
130
 
G
e
V
,
L
i
g
h
t
 
f
r
a
g
m
e
n
t
s
:
A
L
≃
86
–
98
⟷
M
W
–
M
Z
 region
.
S1:
S2:
Light fragments:

  
A 
H

 ≃134
A 
H

 ≃140
A 
L

 ≃86–98

  
⟷M 
h 
0
 

 
⟷M 
H 
±
 
candidate

 
⟷M 
W

 

  
≃125 GeV,
≃130 GeV,
–M 
Z

  region.

 
The 130 GeV charged-Higgs candidate is not established, of course.

But the recent shell-structure results suggest a sharper question than matching two Gaussian centroids:

Are the S1/S2 structures more invariant when expressed in fragment mass, or in fragment proton number?

If they are associated primarily with 
Z
H
≃
52
Z 
H

 ≃52 and 
Z
H
≃
55
Z 
H

 ≃55, while their masses change with neutron excess, that favors a nuclear-shell interpretation over a resonance at a fixed electroweak mass.

That is, in fact, what the modern fragment-charge systematics indicate.

My assessment is therefore that the asymmetric fission phenomenon is thoroughly physical, but the separation into exactly two independent S1/S2 mechanisms is not established. And a correspondence with two scalar masses would be more persuasive if two separate dynamical valleys were identified rather than two components of a single anharmonic distribution.

The McGlynn–Simenel paper is particularly pertinent because it prevents us from giving too much physical meaning to the centroids of fitted Gaussians
~~~~~~
