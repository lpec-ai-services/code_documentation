# The use of flow regime maps
<!-- source PDF pages 60-62 -->

<!-- page 698 (PDF 60) -->
A dynamic modeling of liquid turbulence and bubble interfacial area could be used to
model precisely the time scales associated with the transition from bubbly to stratified
flow. It could be more convenient to use a dynamic modeling of turbulence to better
model interfacial heat transfers in all situations, particularly for direct contact
condensation.
A four-field model with a continuous liquid field, a continuous gas field, a dispersed
bubble field, and a dispersed droplet field, has many capabilities to
improve the prediction of flow regimes, the dynamics of flow regime transitions,
the mechanical behavior, and the interfacial transfers in complex situations when
a phase is split into two fields. In addition it could provide a better characterization
of the flow with a more precise vertical void repartition. Three-field models
with two liquid fields are already being implemented in CATHARE-3 and SPACE
codes. Four models already exist in the petroleum industry for liquid-gas flows in
pipelines and could probably be implemented in system codes in the medium-term
future.
11.10
The use of flow regime maps
Every flow regime has its internal structure and its transfer mechanisms. So it
seems natural to use a flow pattern map in a code and to develop correlations
for mass momentum and energy transfers which depend on the flow pattern. This
is usually done via flow regime maps where specific two-phase flow patterns are
identified as functions of input data such as superficial gas and liquid velocities,
flow rates, or more complex dimensionless parameters. The highly empirical
flow regime maps are based on a large amount of measured data for different
fluids, vertical, and horizontal flow conditions and different pipe diameters.
Typical examples are the flow pattern maps of Mandhane et al. (1974) and
Taitel and Dukler (1976). Nevertheless, all these flow regime maps are valid
only
for
steady
state—or
quasi-steady
state—and
fully
developed—or
quasi-developed—flow conditions although rapid transient and nonestablished
flows also exist in nuclear reactors under accident conditions. Having these
restrictions in mind it might be justified to further simplify the flow maps as is
usually done in all the codes.
As an example, the flow regime map as used in RELAP5/MOD3 for horizontal
flow is shown in Fig. 11.22. Major selection parameters are void fraction αg and total
mass flux Gm.
Specifically modeled are the bubbly, slug annular-mist, mist, and stratified flow
regimes. Transition criteria are also algebraic relations between flow parameters.
To avoid discontinuities, some transition regions are included where all parameters
are interpolated from the adjacent flow regime boundaries. This only provides artificially
smooth transitions but cannot take into account the relaxation time scale
associated with the flow process responsible for the transition.

<!-- page 699 (PDF 61) -->
## 11.10.1 Transition criteria

Horizontal stratified flow conditions are assumed to exist for Gm < 3000 kg
m2 =s and
Vg ≡Vl
□□
□□ < Vcrit, with the critical velocity according to Taitel and Dukler (1976):
vcrit = 1
ρl ≡ρg
gαgA
ρgDsinθ
1≡ cosθ
ð
Þ
where θ represents the angle between the vertical axis and the pipe axis.
The criteria for bubbly to slug, slug-to-annular mist, and annular mist to mist flow
regimes are just given by limiting values of void fraction and mass flux. A classical
slug-to-annular transition criterion is:
J*
g =
Jg
gDΔρ
ρg
"
#1)
2 □ 1
Other flow regime maps are applied for vertical flow separating pre-CHF and post-dryout
conditions. Flow regime maps provide a necessary information on interfacial
Bubbly
Slug
Transition
Horizontal stratified
Void fraction (ag)
Mass flux (kg / m2 s)
a BS
a SA
Mist
a AM
Annual mist
Transition
|vg –vf|=0.5 vcrit
|vg – vf|=vcrit
a DE
Fig. 11.22 RELAP5 flow regime map for horizontal flow.

<!-- page 700 (PDF 62) -->
structure and interfacial area based on experimental observation and with some theoretical
basis and allows a mechanistic modeling of interfacial transfers.
The most important transitions correspond to interfacial area changing by several
orders of magnitude, for example, at the onset of droplet entrainment or when phase
stratification occurs in a bubbly flow in a horizontal pipe.
Several models are used in the various codes for the onset of droplet entrainment,
for example, Steen-Wallis (Wallis, 1969) model:
Jg0 = 2:1·10≡4 σ
μg
ffiffiffiffiffiffiffiffiffi
ρg=ρl
q
E = 1≡ exp Jg0 ≡Jg
□
□
E being the entrainment rate (droplet flow rate divided by total liquid flow rate).
The Ishii and Mishima (1984) model gives:
E = tanh 7:25e≡7We1:25
e
Re0:25
l
□
□
Wee =
ρgJ2
gDh
σ
Δρ
ρg
!1)
or a limiting value of the Kutateladze number:
Kug =
Jg
gσΔρ
ρ2
g
"
#1)
4 □ 3:2
The main reason for codes not having converged to the same correlation is probably
that the validation could not clearly identify which model was the most appropriate
since measurements of E is very difficult particularly in complex geometry (fuel
assembly) and high pressure and temperature.

## 11.10.2 The limitations of flow regime maps

The main limitations of using such flow regime maps are:
l
Range of validity: no observations are available in high pressure steam water flows to validate
the flow maps in such reactor conditions. Also data in large diameter pipes are very
limited.
l
Flow geometry: very limited observation of flows in complex geometry (rod bundle) is available
although geometrical effects are likely to be significant. Also effects of some singularities
are not taken into account.
l
Steady and established flows are necessary to establish such maps, and they are extrapolated
in transient or nonestablished conditions. History effects and relaxation time constants associated
with regime transitions are not taken into account.
