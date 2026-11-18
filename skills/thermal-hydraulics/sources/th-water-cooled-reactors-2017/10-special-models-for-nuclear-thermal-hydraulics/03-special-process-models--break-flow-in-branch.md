# Special process models — Break flow in branch
<!-- source PDF pages 19-24 -->

<!-- page 613 (PDF 19) -->
l
FRIGG Rod Loop Tests (Sweden)
l
GE 9-Rod Bundle Tests (NRC/General Electric)
l
NRU Rod Bundle Tests (Canada)
l
ACHILLES Reflood Tests (United Kingdom)
l
Lehigh 9-Rod Bundle Tests (NRC/Lehigh University)
l
PERICLES Reflood Tests (France)
While these tests do simulate flow in the rod bundles, they have limitations, as pointed
out by Hochreiter et al. (2010), that will make it difficult to either develop correlations
or validate the models as were identified in this report and listed earlier. The tests did
not measure void fractions, droplet size and velocity, and vapor temperatures. They
also have different materials for clad than in the reactors. USNRC has supported a test
program in Penn State University, Rod Bundle Heat transfer Test facility. This facility
was designed based on the H2TS scaling approach (Zuber, 1991; Wulff, 1996). The
top-down approach identified different phenomena through the transfer terms on the
right side of the balance equations. Scaling estimate identified three possible scale
distortions—the presence of housing containing rod bundles that will act as an additional
heat sink, electrically heated rods and gap, and finally clad material that has an
effect on Tmin.

## 10.2.5 Break flow in branch

There are two flow situations that differ from broken pipe flows—flow from a tank
and flow through a branch. Depending on the location of break or branch, and flow
regime in the main pipe, there could be either gas pull through or entrainment of the
liquid. This section will address these phenomena.
One class of accidents that is simulated with system codes is small break in cold or
hot legs. The break size is smaller than pipe area and could be any part of the pipe. The
location of such a small break determines the loss of mass and energy from the primary
system. During the transient with loss of inventory, there may be stratification of flow
in the pipe with break. The flow through the break will be vapor for break at the top
and with some entrainment of liquid and in case of break at the bottom, there will be
liquid flow with some vapor pull through. The break in the middle will have liquid or
vapor primary flow with either entrainment or gas pull through. The flow from the
bottom of tank such as accumulator may have vapor pull through with vapor vortex
as the level decreases. Fig. 10.8 shows various possibilities for liquid entrainments and
vapor pull through.
It is essential that correct mass and energy discharge are calculated to characterize
the fluid condition in the reactor system.
There have been studies that provided analytical models and experimental data,
e.g., Zuber (1980), Reimann and Khan (1984), Schrock et al. (1986), Majumdar
et al. (1999), Levy (1999), Cho and Jeun (2004), and Chung et al. (2000). Furthermore,
Zuber (1980) provided initial analyses for entrainment and vapor pull through the
break. There are revised analyses with validation with data from Reimann and
Khan (1984). Schrock team also conducted tests and provided revised correlation
for initiation of pull through for vapor and for entrainment.

<!-- page 614 (PDF 20) -->
Vapor pull through and liquid entrainment require flow stratification and the presence
of level for the liquid interface.

### 10.2.5.1 Vapor pull through

As shown earlier, there are two mechanisms of vapor pull through with vortex
and without vortex. In the case of flow at the bottom of tank, there will be vapor
pull through with vortex and in the case of branch in hot or cold leg, the vapor pull
through will be without vortex. A study by Schrock group (Schrock et al., 1986) noted
that even in the pipe flow branch, there is initially a vortex but as level decreases the
vortex disappears. In some cases there is no vortex as the circulation could not be
established.
The vortex free onset of vapor pull through is given by Lubin and Horwitz (1966):
Fr
ρl
ρl □ρg
!0:5
= 3:25 hb
d
□
□2:5
For the case of vortex vapor pull through the correlation by Reimann and Khan (1984)
is given here.
Fr
ρl
ρl □ρg
!0:5
= 0:2 hb
d
□
□2:5
g
d
D
Lg
Lg
g
g
g
l
l
l
WIb
WIb
Wgb
Wgb
Wgb
(A)
(B)
Vapor pull-through due to vortex formation
g
d
D
LI
g
g
g
Wg
Wg
WI
WI
I
I
I
Vapor pull-through in vortex-free flow
WIb
WIb
WIb
WIb
WIb
Wgb
Wgb
Wgb
Wgb
I
I
Fig. 10.8 Various possibilities for break flow from branches. (A) Illustration of liquid
entrainment in break flow due to Bernoulli effect. (B) Illustrations of mechanisms for vapor
pull-through a break.

<!-- page 615 (PDF 21) -->
These correlations were compared with the data for three-flow configuration. In the
case of configurations (a) and (b) there is no continuous flow such as in hot or cold
legs. The pipe either has no flow or is closed on one side. The figure shows clearly the
vapor pull through vortex and at lower liquid pull through without vortex. For pipe
with flow higher than in the branch, there is hardly any vortex formation as shown
in Fig. 10.9 for initiation of vapor pull through.
Reimann (Reimann and Khan, 1984) also provided a correlation for flow through
the break as function of liquid level.
Gbreak
Gbreak,b
=
h
hb
□
□1:62
Schrock et al. (1986) developed a correlation that accounts for viscosity and surface
tension in correlation for initiation of pull through as given here along with quality at
the break as function of liquid level.
FrlBo2N□0:5
μ
ρl
ρl□ρg
ð
Þ
!0:5
= 19:4
hb
σ
g ρl□ρg
ð
Þ
!0:5
2:2
X = e□3:1 h=hb
□
□
1□
h=hb
□3:5
d = 12 mm
Onset of
vortex-free
gas pull-through
Onset of
vortex-induced
gas pull-through
hb/d
hb/d
Fr
pl
pl−pg
0.5
= Flow geometry (a)
= Flow geometry (b)
d (mm)
,
,
Continuous gas pull-through
Flow geometry (c)
Onset of
first bubble pull-through
(
)
,
(
)
,
Fr
pl
pl−pg
0.5
Fig. 10.9 Vapor pull through making reference to flow configurations (a), (b), and (c) in
Fig. 10.7.

<!-- page 616 (PDF 22) -->
Most of flow will be liquid but flow can be quickly choked. With information on
quality a two-phase choked flow calculation can be performed.
The data from UCB, INL, and KFK are shown in Fig. 10.10.

### 10.2.5.2 Upward oriented break

In upward oriented break the vapor flow may entrain liquid through the break.
As the liquid level decreases the entrainment will cease. Schrock et al. (1986)
provided correlation based on their data, and data from INL and KFK
(Fig. 10.10).
Frg
ρl
ρl□ρg
ð
Þ
!0:5
= 0:395 hb=d
□
□2:5
X =
h=hb
3:25 1□ h=hb
□
□
□
□2
Steam/water
Air/water
Incipient pull through data
Present
I-DN
IB-DN
2-DN
INEL
KfK
Data fit
correlation
hb/(s/Δrg)0.5
FrIBo
2Nm
-0.5(rI/Δr)
0.5
Fig. 10.10 Vapor pull through data from UCB, KfK, and INL test facilities.

<!-- page 617 (PDF 23) -->
### 10.2.5.3 Side break

Sometimes there are breaks at the side of the pipe and the vapor pull through or liquid
entrainment will depend on the relative location of the liquid level with respect to
the break.
When the liquid level is above the break initiation of vapor pull through is given by
following correlation that is similar to correlation for bottom break; experimental data
and results from the application of the correlation are given in Fig. 10.11.
FrlBo2N□0:5
μ
ρl
ρl□ρg
ð
Þ
!0:5
= 40:6
hb
σ
g ρl□ρg
ð
Þ
!0:5
2:1
When the liquid level is below the break, the initiation of entrainment is given by the
following correlation. It looks similar to the correlation for top break.
Frg
ρl= ρl□ρg
ð
Þ
0:5
= 3:25 hb=d
□
□2:5
T/S
Air-water
2-UP
IB-UP
KfK Air-water
data
Steam-water
hb/d
Frg (rg/Dr)0.5
Fig. 10.11 Vapor pull through
data for upward oriented break.

<!-- page 618 (PDF 24) -->
The correlation for quality at the break was also derived from the data (Schrock
et al., 1986):
X = X
1 + h
hb
0:7
1□C
h
hb
1 + h
hb
□
□
where X0=0.06 and,
C = 1, for h
hb
≡ 0 Liq entrainment; C = 0 for h
hb
> 0, Vap pull

### 10.2.5.4 Models in system codes

RELAP5 (USNRC, 1998) and TRACE (USNRC, 2013) codes model the branch
flow or offtake, based on Smoglie’s work (Smoglie, 1984). The model for liquid
level with respect to branch point at the initiation of entrainment of vapor pull
through is similar for all three orientations except for a constant. The expression
is given here.
hb =
CW0:4
k
gρk ρl □ρg
h
i0:2
Here subscript k is either l for liquid or g for gas.
Furthermore,
C =1.67 for top offtake for liquid entrainment
=1.50 for bottom offtake, vapor pulls through
=0.75 for side offtake, vapor pull through with liquid level above the break
=0.69 for side offtake for liquid entrainment with liquid level below the break
The expression for quality at the break is different for different orientation.
For top break with liquid entrainment the expression for quality is given as
follows:
X =
h
hb
□
□3:25
1□ h
hb
For bottom break with vapor pull through, the expression for quality is as follows:
X = e
□3:1 h
hb
1□
h
hb
□
□2
!3:5
