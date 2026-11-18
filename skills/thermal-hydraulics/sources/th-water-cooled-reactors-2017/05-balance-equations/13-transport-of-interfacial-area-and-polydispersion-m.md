# Transport of interfacial area and polydispersion models
<!-- source PDF pages 68-71 -->

<!-- page 234 (PDF 68) -->
Since this form is close to the formulation suggested by Stuhmiller (1977), it was
accepted and it was chosen to satisfy this condition in Cathare. One can see that
the added mass force does not play here any role in the hyperbolicity, and one may
obtain an hyperbolic system of equation without added mass force provided that:
fi > fihyp = α 1−α
ð
Þρgρl VG −Vl
ð
Þ2
ρm
The Athlet code (Lerchl and Austcberegesilo, 2013) uses a slightly different form
of fi as:
fi = Cαρ VG −Vl
ð
Þ2
where the C value can also provide hyperbolicity and stability.
5.13
Transport of interfacial area and
polydispersion models
Two-phase flow have a complex nature with a large diversity of length scales associated
to bubbles size, droplet size, distance between bubbles or droplets, film thickness, turbulenteddysizes
, wavelength at a free surface or a film surface. Similarly a large variety
of time scales can be identified. All basic processes such as mass momentum and energy
transfers at walls and interfaces which have to be modeled depend on the length scales
whichalsodependontheflowregime.Transportequationsmaybe addedtopredict evolution
of some scales such as turbulent scales. The first approach in two-phase flow
modeling was to write an equation for interfacial area concentration ai which may be
definedastheratioofinterfacearea(IA)tothevolumeofatwo-phasemixture.Transport
equationforinterfacial(TIA)wasdevelopedinbothsystemcodesina1-Dapproachand
3-D CMFD. TIA focused on bubbly flow and on droplet flow. Three main reasons promoted
the use of a transport equation for interfacial area (TIA) in system codes.
Nonestablished flows: it was observed that dispersed bubbly flow and droplet flows
have a mean bubble and drop size which depends on several mechanisms such as
break up, coalescence, nucleation, collapse, and interfacial mass transfer. Some of
these phenomena have relatively long relaxation times which are larger than convective
time scales so that the “average size” is not an “equilibrium size” which can be
expressed based only on local principal variable of the two-fluid 6-equation model
used in current system codes. TIA is capable to better model such nonestablished
flows by taking relaxation times into account provided that source and sink terms
are modeled and validated.
Flow regime transitions: it was observed that many flow regime transitions are
corresponding to a change of IA: bubbly-to-slug flow or bubbly-to-churn flow result
from a coalescence process which decreases IA, bubbly-to-stratified flow transition
also results from bubble sedimentation and coalescence of bubbles. Therefore TIA
should be used for a prediction of some flow regime transition and could also model

<!-- page 235 (PDF 69) -->
intermediate states between two flow regimes. Other flow regime transitions such as
the onset of droplet entrainment increases IA dramatically but the governing phenomenon
is an interfacial instability. One may distinguish transitions which result from a
change on IA from transitions which induce a change of IA.
Interfacial transfers: interfacial transfers of mass, momentum, and energy depend
on IA (or on drop/bubble size, for example). Therefore a dynamic prediction of IA
would also improve the prediction of interfacial friction and interfacial heat transfers
which control void fraction and slip between phases and also phase temperatures and
mass transfers by vaporization and condensation.
Usual expressions of interfacial friction and interfacial heat transfers in system
codes are of the form:
τi = −aiCi
ρ
2 Vv −Vl
j
j Vv −Vl
ð
Þ
qik = aihik Tsat −Tk
ð
Þ
Let us consider a dispersed flow with a continuous phase c and a dispersed phase d
(bubbles or drops) with a particle number density nd and a Sauter mean diameter δ32.

## 5.13.1 Monodispersed approximation:

The simplest assumption is to consider a population of uniform size spherical particles
. In this case simple relations exist between ai, dispersed phase fraction αd, δ32,
and nd.
ai = 6αd
δ32
; nd = 6αd
πδ3
Usual expressions for interfacial friction and heat transfer coefficients hid in dispersed
flow are:
τid = −Cd Red
ð
Þπδ2
4 nd
ρc
2 Vd −Vc
j
j Vd −Vc
ð
Þ
= − 3αd
4δ32
Cdρc Vd −Vc
j
j Vd −Vc
ð
Þ
qid = 6αd
δ32
hik Tsat −Td
ð
Þ = 6αd
δ32
λcNud
δ32
Tsat −Td
ð
Þ
with:
Nud = aRed
pPrc
q; Red = ρc Vd −Vc
ð
Þδ32
μc
; Prc = μcCpc
λc
Both models need expressions for δ32 or ai or nd.

<!-- page 236 (PDF 70) -->
## 5.13.2 Monodispersed approximation with algebraic interfacial area:

In standard industrial fully validated versions of system codes only algebraic expressions
of δ32 or ai or nd are available. It is often assumed that a droplet or bubble diameter
is equal to the limiting value corresponding to a critical Weber number:
Wecrit = ρc Vd −Vc
ð
Þ2δ32
σ
This assumes that all droplets or bubbles have reached the maximum diameter above
which they would be broken. It is clear that this is a very strong assumption which
cannot be valid except in some particular situations.

## 5.13.3 Monodispersed approximation with dynamic interfacial area modeling

A more general approach within the monodispersed approximation consists in writing
a transport equation for ai or nd. The derivation of such equations can be found in Ishii
and Hibiki (2011), or in Morel (2015).
∂nd
∂t + r · ndvn = ΦNuc
n
+ ΦCol
n
+ ΦCoa
n
+ ΦBU
n
∂ai
∂t + r · aivi = 2ai
3αdρd
Γid −αd
∂ρd
∂t −αdVdrρd
(
+ ΦNuc
ai
+ ΦCol
ai + ΦCoa
ai
+ ΦBU
ai
vn or vi have to be modeled and the dispersed phase velocity vd is most often used. The
following source and sink terms have also to be modeled.
Φn
Nuc is the source term of nd due to nucleation (creation of bubble by flashing or boiling
or drop creation by condensation)
Φn
Col is the sink term of nd due to collapse (vaporization of a drop or condensation
of a bubble)
Φn
Coa is the sink term of nd due to coalescence
Φn
BU is the source terms of nd due to break up
ΦNuc
ai
is the source term of ai due to nucleation
ΦCol
ai
is the sink term of ai due to collapse
ΦCoa
ai
is the sink term of ai due to coalescence
ΦBU
ai
is the source terms of nd due to break up
with the relations:
ΦCoa
ai
= 12π αd
ai
(
ΦCoa
n
; ΦBU
ai = 12π αd
ai
(
ΦBU
n

<!-- page 237 (PDF 71) -->
## 5.13.4 Polydispersed dynamic modeling with the method of statistical moments

A more complex modeling consists in predicting the bubble or drop size distribution
along the flow.
The bubble diameter distribution function f(δ;x,t) is defined such that f(δ;x,t)dδd3x
represents the probable number of bubbles in a volume element d3x at time t, having
their diameters in the interval δ, δ + dδ
½
□
The jth order moment of the bubble diameter distribution function is defined by:
Sj x, t
ð
Þ≜
ð∞
δjf δ; x, t
ð
Þdδ
The four first-order moments give the bubble number density, the product of the bubble
number density nd by the mean bubble diameter δ10, the IA ai, and the fraction of
dispersed phase αd:
S0 = nd; S1≜ndδ10;S2 = ai
π ;S3 = 6αd
π
The Sauter mean diameter is the ratio:
δ32 = S3
S2
A transport equation for the moment Sj can be written as:
∂Sj
∂t + r · Sjvj
−j _Dj−1Sj−1 = Pj
where closure relations are necessary for the transporting velocity vj, the mean bubble
or drop growth rate _Dj, and the source term Pj.
Selecting a law of distribution function and writing transport equations for some
moments, one can predict the evolution with x and t of the distribution. This was tested
with log-normal and quadratic laws by Zaepffel et al. (2012), since these are simple
laws which can be defined by the knowledge of only two statistical moments.
When a bubble size distribution function is known one can express the liquid-tointerface
heat transfers as:
qil = ndπ
ðδmax
δmin
δ f δ
ð ÞNu δ
ð Þdδ
λc Tsat −Tc
ð
Þ
which is likely to be more precise that the monodispersed expression.
