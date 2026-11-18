# Interfacial drag
<!-- source PDF pages 22-28 -->

<!-- page 570 (PDF 22) -->
Brown droplet model (Brown, 1951) for the drops, and the modified Theofanous interfacial
condensation model (Theofanous, 1979) for the film.
Table 9.3 summarizes the correlations for the IHTC in the RELAP5 code (USNRC,
1998a). As can be seen in Table 9.3, some of the IHTC models are on an ad hoc basis,
and these need to be assessed against experimental data. Very large IHTC puts the
liquid and vapor phases in thermal equilibrium. This can lead to making the system
TH code numerically more stable, but with less physical results.
The formulation of the interfacial heat transfer in the TRACE code (USNRC, 2013)
is basically the same as that in RELAP5, Eqs. (9.23), (9.24). However, for the special
case where the liquid is superheated with respect to saturation at the total pressure,
rapid nucleation will occur at any surface, and the resulting IHTC will increase dramatically
as the level of liquid superheat increases. Under these conditions, Eq. (9.24)
is modified to add an additional term for flashing, which is,
QB
if = hif ai Ts Pv
ð
Þ·Tf
□
(
+ hflashai Ts ·Tf
□
(
:
(9.35)
When noncondensable gases are present, several modifications are made to the IHTC
models to consider the additional heat transfer resistance associated with the diffusion
of the noncondensable gas.
In the TRACE code, the IHTCs (hig, hif, and hflash) and IAC (ai) are dependent upon
the flow regime. Each flow regime has its correlations for ai, hig, hif, and hflash. Unlike
the RELAP5 code that uses different IHTCs according to fluid temperature, one set of
correlations is used for each flow regime and, if needed, the effect of fluid temperature
is accounted. Tables 9.4 and 9.5 summarize the IAC and IHTC correlations of the
TRACE code, respectively.
9.5
Interfacial drag
The equations of motion in the two-fluid six-equations are coupled by two interfacial
terms: one resulting from the interfacial drag force between the phases (Fik) and the
other from the momentum transfer associated with mass transfer (VikΓik). The interfacial
drag determines the slip between liquid and vapor phases, phase separation,
two-phase mixture level, etc. This term is very important in a slow two-phase flow
transient, such as a small-break LOCA.
The interfacial drag between the phases is generally represented as
Fik = ·1
ð
ÞkCi Vg ·Vf
 Vg ·Vf
□
(
,
(9.36)
where Ci is the interfacial drag coefficient. Two different models are widely used for
the phasic interfacial drag computation in system TH codes: the drift-flux method and
the drag coefficient method.

<!-- page 571 (PDF 23) -->
Table 9.3 The IHTC correlations in the RELAP5 code
Flow regime
Interfaces
Superheated liquid (SHL)
Subcooled liquid (SCL)
Superheated
vapor/gas (SHG)
Subcooled
vapor/gas (SCG)
Bubbly
Small
bubble
Max (Plesset and
Zwick (1954), modified Lee
and Ryley (1968))
Modified by Unal (1976),
Lahey (1978)
hig = 104W=m2K
ai: bubbly SHL
Bubbly SHG
Slug
Taylor
bubble
Large HTC
Special model
Modified by Lee and
Ryley (1968)
hig: bubbly SHG
Small
bubble
Bubbly SHL
Bubbly SCL
hig: bubbly SHG
ai,bub: slug SHL
Slug SHG
Annular mist
Film
Large HTC
Modified by Theofanous
(1979)
Dittus and Boelter
(1930)
hig: bubbly SHG
ai,ann: annular-mist
SHL
Droplets
Quadratic function
Modified by Brown
(1951)
Lee and Ryley (1968)
hig: bubbly SHG
ai,drp: annular-mist
SHG
Inverted
annular
Small
bubble
Bubbly SHL
Bubbly SCL
hig: bubbly SHG
ai,bub: inverted annular
SHL
Inverted annular
SHG
Liquid
core
Large HTC
Dittus and Boelter (1930)
hig = kg
D
ai,ann: inverted annular
SHL
Inverted slug
Liquid
slug
Large Nu
Brown (1951)
hig = kg
D
ai,ann: inverted slug
SHL
Modified
Lee-Ryley
Inverted slug SHG
Continued

<!-- page 572 (PDF 24) -->
Table 9.3 Continued
Flow regime
Interfaces
Superheated liquid (SHL)
Subcooled liquid (SCL)
Superheated
vapor/gas (SHG)
Subcooled
vapor/gas (SCG)
Dispersed
Droplets
Large Nu
Brown (1951)
Modified by
Lee-Ryley
hig: bubbly SHG
agf: dispersed SHG
Horizontally
stratified
Large Nu
Dittus and Boelter (1930)
Dittus-Boelter and
large Nu
hig: bubbly SHG
agf: horizontally
stratified SHG
Vertically
stratified
Hif = Hif,REG (unclear)
McAdams
McAdams
Hif = Hif ,REG
(unclear)

<!-- page 573 (PDF 25) -->
Table 9.4 The IAC model in the TRACE code
Flow
regime
Interfaces
Interfacial area per unit volume
Bubbly
Dispersed
bubble,
ai,DB
ai,DB = 6α
dDB
, αg < αDB
where
dDB = 2
ffiffiffiffiffiffiffiffi
σ
gΔρ
r
,
αDB =
0:3
for G □ 2000 kg=m2s
□
(
,
0:3 + 0:2
G·2000
2700·2000
□
□
for 2000 < G < 2700 kg=m2s
□
(
,
0:5
for G □ 2700 kg=m2s
□
(
:
>
>
<
>
>
:
Cap
bubble/
slug
Large
bubble,
ai,LB
ai,LB = C*
D*
α·αDB
1·αDB
□
□
, αDB < αg < 0:5
where
C* =
4:5; Dh < Dh,crit
16; Dh □ Dh,crit
□
D* =
Dh;
Dh < Dh,crit
Dh, crit; Dh □ Dh,crit
□
Dh,crit
 50 □ La = 50 □
ffiffiffiffiffiffiffiffi
σ
gΔρ
r
Dispersed
bubble,
ai,DB
ai,DB = 6·αDB
dDB
1· αg
1·αDB
□
□
, αDB < αg < 0:5
Annular
mist
Film, ai
ai = 4
Dh
ffiffiffiffiffi
αg
p
fwet
where fwet: the fraction of the surface wetted by the film.
Droplets,
ai,drop
ai,drop =
6αgαd
1·αd
ð
Þdd
where αd: the fraction of annular core region occupied by
droplets.
Stratified
ai = Si
A,
Si: the width of the stratified two-phase interface

<!-- page 574 (PDF 26) -->
## 9.5.1 Drift-flux method

In RELAP5, TRACE, and CATHARE 2, the drift-flux approach is used in the bubbly
and slug flow regimes for vertical flow. This is because lots of reliable drift-flux data
are available in vertical bubbly and slug flows.
The drift-flux model specifies the distribution coefficient (Co) and the vapor drift
velocity (Vgj). By using appropriate assumptions, these two quantities are converted
into a constitutive relation for the interfacial frictional force per unit volume (USNRC,
1998a,b, 2013).InRELAP5,thedrift-fluxmethodleadstothefollowinginterfacialdrag:
Fi = ·1
ð
ÞkCi C1Vg ·C0Vf
 C1Vg ·C0Vf
□
(
,
(9.37)
where
Ci =
αgα3
f ρf ·ρg
□
□
g
V2
gj
,
(9.38)
C1 = 1·αgC0
1·αg
:
The drift-flux correlations (Co and Vgj) from the literature based on Putney (1988a,b,c,
1989, 1991) and Chexal and Lellouche (1986) are used, which had been developed for
Table 9.5 The IHTC correlations in the TRACE code
Flow
regime
Interfaces
Liquid side
Vapor/gas side
Bubbly
Dispersed
bubble
Ranz and Marshall (1952)
Constant HTC
hvi = 1000 W=m2K
□
(
Cap
bubble/
Slug
Large
bubble
Dispersed
bubble
Ranz and Marshall (1952)
Constant HTC
hvi = 1000 W=m2K
□
(
Annular
mist
Film
hli, film =
hli, lam
ð
Þ2 + hli, turb
ð
Þ2
h
i1=2
Laminar—Kuhn et al. (1994)
Turbulent—Gnielinski (1976)
Max [Dittus-Boelter, 4.0]
Droplets
Kronig and Brink (1950)
Ryskin (1987)
Stratified
hli = Min 25,000, kl
hl
Nuli
hl: the height of liquid layer
Nuli: Nusselt number used for liquid
film in annular flow
Unclear

<!-- page 575 (PDF 27) -->
rod bundles, small pipes (D<0.018 m), intermediate pipes (0.018 m<D<0.08 m),
and large pipes (0.08 m<D) for a wide range of flow rates.
A similar approach is used in the TRACE code for bubbly/slug flow regime in pipes
and rod bundles. Meanwhile Eq. (9.36) is used instead of Eq. (9.37) and the friction
coefficient Ci is given by
Ci =
αgα3
f ρf ·ρg
□
□
g
V2
gj
PS,
(9.39)
where PS =
1·C0αg
1·αg
Vg ·C0Vf
□
□2
V2
gj
. The profile slip factor, PS, can be considerably
less than unity.
The term comes from the fact that the velocities used in the field equations in
TRACE are the void-weighted area-averaged phase velocities (Brooks et al.,
2012). The drift-flux parameters C0 and Vgj are prepared for dispersed bubbly/slug
flow and Taylor cap bubble flow in pipes (Zuber and Findlay, 1965; Wallis, 1969;
Ishii, 1977; Kataoka and Ishii, 1987) and for bubbly/slug flow in rod bundles
(Bestion, 1985; Salay, 2001; Coddington and Macian, 2002). It is known that the
Bestion model, Vgj =
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
gΔρDh=ρg
q
and Co=1.2, did a reasonably good job for the
low-flow low-pressure conditions in rod bundles. Based on a study by Salay
(2001) the Bestion model was extended to high-pressure boil-off conditions in
TRACE. However, for the BWR conditions, the value of distribution parameter Co
was set to unity, as recommended by Coddington and Macian (2002) to correct the
underprediction of the void fraction.
CATHARE 2 also uses a drift-flux model to compute the interfacial drag on the
bubbles in bubbly flow, where configuration-dependent parameters are additionally
taken into account for the flows in rod bundles, pipes, and annuli (Bestion,
1985, 1990).

## 9.5.2 Drag coefficient method

The drag coefficient method, using Eq. (9.36), is used in all flow regimes except for
the flow regimes that use the drift-flux method. Correlations for the drag coefficients
and the IAC (see Tables 9.2 and 9.4) are needed in this method. For illustration, a
description of the RELAP5 drag coefficient method follows below.
The constitutive relation for the frictional force on a body moving relative to a fluid
is given by
F = 1
2ρV2CDA,
(9.40)

<!-- page 576 (PDF 28) -->
where
F is the drag force,
ρ is the fluid density,
V is the velocity of body relative to the fluid,
CD is the drag coefficient,
A is the projected area of the body.
Expressing the frictional force for a group of bodies moving relative to a fluid (e.g.,
bubbles moving through liquid or droplets moving through vapor) in terms of the frictional
force for each body leads to the following constitutive relation for the frictional
force per unit volume:
Fi =1
8ρcCDSFai Vg ·Vf
 Vg ·Vf
□
(
= Ci Vg ·Vf
 Vg ·Vf
□
(
,
(9.41)
where
Ci = 1
8ρcCDSFai,
ρc is the density of continuous phase,
SF is the shape factor.
The additional factor of 1/4 in Eq. (9.41) comes from the conversion of the projected
area of spherical particles (πr2) into the interfacial area (4πr2) and the shape factor is
included to account for nonspherical particles. As can be seen in Eq. (9.41), the drag is
proportional to the IAC. The IAC models in Table 9.2 are used to obtain the IAC for a
specific flow regime. This again shows that the flow regime map is very important for
two-phase flow computations.
The drag coefficient to be used in nonvertical bubbly flow and all droplet flow
situations is given by Ishii and Chawla (1979) for the viscous regime, as
CD =
24 1:0 + 0:1Re0:75
p
□
□
Rep
,
(9.42)
where the particle Reynolds number, Rep, is defined as
Rep = Vg ·Vf
d0ρc
μm
:
(9.43)
The density, ρc, is given by ρf for bubbles and ρg for drops. The mixture viscosity, ρm,
is for the continuous phase. It is given by μm = μf =αf for bubbles and μm = μg
α2:5
g
for mist
pre-CHF, mist, and mist-post-CHF droplets. It can be seen from Eqs. (9.41), (9.43),
the average bubble (or droplet) diameter is very important for determining the
interfacial drag.
