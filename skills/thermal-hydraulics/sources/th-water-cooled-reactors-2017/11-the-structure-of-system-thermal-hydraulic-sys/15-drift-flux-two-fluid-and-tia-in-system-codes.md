# Drift flux, two-fluid, and TIA in system codes
<!-- source PDF pages 76-81 -->

<!-- page 714 (PDF 76) -->
many transients a better modeling and a SET validation is required (Bestion, 2014).
The wall friction and interfacial friction terms have to be modeled in a core with a
more general formulation of friction tensors taking into account the nonisotropy of
the geometry. Radial transfers (Chandesris et al., 2013) in a quasi-vertical flow have
to be better modeled and validated. Radial transfers of phase momentum may be
due to:
l
Transport by mean transverse velocity when there are crossflows
l
Radial diffusion (molecular+turbulent) of momentum
l
Radial dispersion of momentum by subscale transverse velocity
l
Interfacial transfers between phases due to radial void dispersion force
The radial transfers of phase enthalpy may be due to:
l
Transport terms by mean transverse velocity if there are crossflows
l
Radial diffusion (molecular+turbulent) of energy
l
Radial dispersion of energy by subscale transverse velocity
11.15
Drift flux, two-fluid, and TIA in system codes

## 11.15.1 The point of view of time scale analysis

The time scale analysis of physical processes is a useful tool to justify or not some
simplifying assumptions made in the modeling of the complex two-phase flow
phenomena.
When several processes are coupled in a sequential way, the processes with the
largest time scales play the major role and require a good modeling, whereas the processes
with the smallest time scales may be simplified. Let us take an example.
The slip between phases in bubbly-slug-churn flows depends first on the
bubble size which is controlled by coalescence, break up nucleation, collapse.
A relaxation time scale τAieq to reach an equilibrium bubble size (or bubble size distribution
) or more generally an equilibrium interfacial area density exists which is not
necessarily well known.
For a given bubble size, an equilibrium slip is obtained with a relaxation time scale
τΔVeq. This is the same as the particle interaction time τd in dispersed flow which is the
time scale for a particle submitted to steady gravity and pressure forces to reach an
equilibrium velocity difference with the continuous phase
τd = ρdδd
ρcCdVr
These two time scales may be compared to a transit time scale τtr = L=V in a reactor
component of length L. Comparing these time scales one may identify various
situations:

<!-- page 715 (PDF 77) -->
l
If τAieq > τtr > τΔVeq or if τAieq > τΔVeq > τtr it may be better to write a transport of interfacial
area (TIA) equation to model the relaxation process which controls the evolution of the size
distribution.
l
If τAieq≪τtr and τAieq≪τΔVeq one may use an equilibrium algebraic expression of the interfacial
area Ai. This approximation is used in current two-fluid models either with
two-momentum equations or with a drift flux where it is assumed that τAieq is zero.
l
If τtr < τΔVeq the use of two separate momentum equations is better than the drift flux algebraic
relation to model this relaxation process which controls the slip between phases.
l
If τΔVeq≪τtr then one may use an equilibrium algebraic expression of the slip between phases
such as the drift flux model. τΔVeq is assumed equal to zero.
The experience gathered so far allows a picture of those time scales depending on the
flow regime:
Flow regime
τΔVeq=τtr
τAieq=τtr
τAieq=τΔVeq
Drift flux/
two-momentum
equations
TAI
Bubbly-slugchurn

τΔVeq≪τtr
τAieq 	 τtr
τAieq≫τΔVeq
Drift flux: OK
TAI may
be better
Droplet flow
(post-CHF)
τΔVeq > τtr
τAieq 	 τtr
τAieq 	 τΔVeq
Two-momentum
equations
TAI may
be better
Annular flow
τΔVeq < τtr
τAieq < τtr
τAieq < τΔVeq
Two-momentum
equations
No need
of TAI
Stratified
flow
τΔVeq > τtr
τAieq≪τtr
τAieq < τΔVeq
Two-momentum
equations
No need
of TAI
Annular-mist
flow
τΔVeq > τtr
τAieq 	 τtr
τAieq 	 τΔVeq
Two-momentum
equations
TAI may
be better
Only the bubbly-slug-churn flows could be well modeled by the drift flux approach.
Droplet flows (such as in a reflooding process) and separate-phase flow (annular
and stratified flows) have a rather long time scale τΔVeq before reaching an equilibrium
slip and the use of two-momentum equations in the six-equation models provided a
clear added value compared to previous drift flux models.
The relaxation time scale τAieq to reach an equilibrium interfacial area density may
be rather long in dispersed flow such bubble-slug-churn and droplet flows. In such
cases, the use of TIA may bring an added value. However, this would require an extensive
experimental program to measure τAieq in all the geometries and all the flow
regime of interest, which is not yet available.

## 11.15.2 Comparing drift flux with two-momentum equations

The prediction of interfacial transfers of mass, momentum, and heat depends a lot on
our capacity to predict the nature of interfaces—which depend on the flow regime—
and of the velocity difference between phases. The dispersed flows, bubbly flow or

<!-- page 716 (PDF 78) -->
droplet flows, may have various bubble and drop sizes and predicting the slip between
phases and thermal nonequilibrium depends a lot on the capacity to predict these sizes.
A drag force on a single bubble may be easily modeled if we know the size δ of the
bubble through correlations of this type:
D = ≡πδ2Cd Reb
ð
Þρl vb ≡vl
j
j vb ≡vl
ð
Þ
where D is the drag force, Reb is the bubble Reynolds number, Cd is the drag coefficient
, ρl is the liquid density, vb is the bubble velocity, and vl is the liquid velocity.
Similar drag force models are available for droplets.
If there is two-phase flow with a population of n bubbles per unit volume having the
same size—called a monodispersed flow—one may easily express the resulting
interfacial friction per unit volume τi in 1-D two-fluid set of equations:
τi = ≡nπδ2Cd Reb
ð
Þρl vb ≡vl
j
j vb ≡vl
ð
Þ
One can obtain a “cross-momentum equation” by eliminating the pressure gradient
term between the two-phase momentum equations:
A αl
∂αvϱvVv
∂t
≡αv
∂αlϱlVl
∂t
□
(
+ αl
∂AαvϱvVvVv
∂z
≡αv
∂AαlϱlVlVl
∂z
= ≡ Afi
∂αv
∂z ≡ gvαl ≡αvgl
½

∂A
∂z ≡Aαvαl ϱl ≡ϱv
½

gz
≡Aτiv ≡Cvαlτwv + Clαvτwl ≡Aαvαl
δPvsing ≡δPlsing
δz
□
□
+ AFAM
v
+ AΓivVi
Let us consider a quasi-steady flow
∂
∂t ffi0
□
□
and quasi-established flow
∂αv
∂z ffi0; ∂Vk
∂z ffi0 without strong geometrical complexity
gv ffi0;δPksing ffi0
□
□
and
without
big
interfacial
mass
transfer
(ΓivVi
term
is
negligible)
this
cross-momentum equation is simplified:
A τiv ffi≡A αvαl ϱl ≡ϱv
½

gz ≡Cvαlτwv ≡Clαvτwl
In such conditions, the force balance between phases is reduced to an equilibrium
between drag force, the buoyancy (gravity force-Archimedes force), and wall friction
forces. Considering a dispersed gas phase and a continuous liquid as encountered in
bubbly, slug and churn flow, in a vertical channel at moderate velocity, wall friction
terms may be significantly smaller than interfacial friction due to a much higher interfacial
area than wall friction area. Then a rough approximation in vertical upward
oriented flow leads to:
τiv ffiαvαl ϱl ≡ϱv
½

g

<!-- page 717 (PDF 79) -->
This simple balance between buoyancy and drag forces has a clear similarity with the
drift flux models where the drift velocity models are of the following form:
Vgj = C
ffiffiffiffiffiffiffiffiffiffi
gΔρδ
ρl
s
where δ is a length scale characteristic of the bubble size. This expression can be
obtained from a balance between buoyancy B and drag force D applied to a bubble
of size:
B □ gΔρδ3; D □ Cdρlδ2V2
gj
If the drag coefficient is assumed constant and if δ is proportional to the Laplace
scale, one obtains the form of Zuber and Findlay (1965) model for churn-turbulent
bubbly flow:
Vgj □ gΔρσ
ρ2
l
□
(0:25
If the drag coefficient is assumed constant and if δ is bounded by the duct diameter,
one obtains the form of Zuber and Findlay model for slug flow:
Vgj □
ffiffiffiffiffiffiffiffiffiffiffiffi
gΔρD
ρl
s
From the drift flux equation, Vgj general expression and simplified cross-momentum
equation, one can obtain an expression of the interfacial friction which is consistent
with a drift flux model:
τiv = αvαl
V2
gj
C2δ = αvαlϱl 1≡Coαv
ð
Þ2 Vv ≡CαVl
ð
Þ2
C2δ
Cα = Co 1≡αv
ð
Þ
1≡Coαv
ð
Þ
This simply shows that a drift flux approach can be equivalent to a full two-fluid
six-equation model when the approximations made in the simplified cross-momentum
equation are valid. When some simplifications are not justified a full two-fluid
six-equation model may have better capabilities.
In situations where inertial forces are not negligible compared to buoyancy, drag,
and friction forces, the drift flux may be significantly worse than the full six-equation
model. For example:

<!-- page 718 (PDF 80) -->
l
Droplet flow: a water droplet created at a quench front during a core reflooding process is
entrained by steam but it does not reach an equilibrium slip within the core (see Fig. 11.29).
l
Stratified flow: in a stratified flow, due to a weak coupling between phases, many situations
cannot be predicted precisely by an algebraic slip since the Afi
∂αv
∂z term is not negligible and
also some acceleration terms may play a significant role in the phase slip.
l
Transient flow: when ∂
∂t ffi0 is no more valid in cross-momentum equation, the algebraic slip
relation is not valid.
l
Nonestablished flow: when ∂αv
∂z ffi0; ∂Vk
∂z ffi0 is no more valid in cross-momentum equation,
the algebraic slip relation is not valid.
l
High condensation and flashing flows: such flows are usually accelerating flows and the
term ΓivVi is no more negligible.

## 11.15.3 Polydispersion effects

Dispersed flows, bubbly flow or droplet flows, usually have a population of bubbles or
droplets covering a rather large range of sizes. There may be a maximum size beyond
which an instability will break the bubble or droplet. Below the maximum size, the
size distribution may depend on many processes including nucleation, vaporization,
condensation, coalescence, entrainment from films or droplet creation by film
sputtering in a reflooding process and deposition.
A size repartition may be defined by a probability density function f(δ) such that:
n =
ð∞
f δ
ð Þdδ
When f(δ) is known one can express the liquid-to-interface heat transfers as:
qil =
ðδmax
δmin
πδ2 f δ
ð ÞNu δ
ð Þdδ
□
(
λl Tsat ≡Tl
ð
Þ
Z
Vd
ΔVeq
ΔV
QF
Vv
Vdeq
HC
ZQF
Fig. 11.29 Qualitative and
simplified droplet velocity
evolution within a core
during a reflooding process.
At quench front (QF), the
initial drop velocity may be
close to zero. Then Vd
increases as droplet is
entrained by vapor at
velocity Vv. The equilibrium
velocity difference Dveq is
not reached at the elevation
Hc at top of the core.

<!-- page 719 (PDF 81) -->
which is expected to be more precise than the monodispersed expression calculated for
a Sauter mean diameter d32:
qil = Aihil Tsat ≡Tl
ð
Þ = nπ d2
32Nu λl Tsat ≡Tl
ð
Þ = 6αd
d32
Nuλl Tsat ≡Tl
ð
Þ
Similarly
τi =
ðδmax
δmin
πδ2
4 f δ
ð ÞCd Reb δ
ð Þ
ð
Þρl vb δ
ð Þ≡vl
j
j vb δ
ð Þ≡vl
ð
Þdδ
is expected to be more precise than the monodispersed expression:
τi = ≡n πd2
4 Cd Reb
ð
Þρl vb ≡vl
j
j vb ≡vl
ð
Þ
However, taking the polydispersion into account induces a huge modeling effort and
many experimental data which are not available. A monodispersion approximation
able to predict an average or an equivalent bubble size or droplet size may be a more
reasonable compromise. One may notice that the equivalent size for heat transfers
may be different from the equivalent size for interfacial friction. The prediction of
a slip between phase depends mainly on the larger drops or bubbles while the total
interfacial heat and mass transfers are dominated by the smallest drops or bubbles.

## 11.15.4 Perspective for using TIA in future system codes

A dynamic modeling of interfacial area (IA) in system codes may be a way to go
beyond limitations of current codes by taking into account time scales associated with
coalescence, break up phenomena, and flow regime transitions. The experience
gained in developing a dynamic modeling of IA was summarized by Bestion and
Serre (2013):
l
The analysis of some flow regimes with new measurement giving access to IA and bubble
size distribution has confirmed that almost all flows have nonestablished bubble size repartition
. In such condition an algebraic IA modeling has limitations, a TIA equation may bring
some added value, and a polydispersion modeling would be necessary to get a very significant
progress.
l
The IA data and TIA models available cannot yet improve system codes since the validation
covers only a very small fraction of the flow situations of interest.
l
A mechanistic modeling of polydispersion still requires a very long effort and requires that
many new data are produced. This may be envisaged only in a long-term perspective.
l
The modeling of some important flow regime transitions such as onset of droplet entrainment
or bubbly-to-stratified flow would require first a multifield modeling to separate the
dispersed field (bubbles or drops) from continuous liquid or gas before benefiting from
the use of TIA for the dispersed field.
