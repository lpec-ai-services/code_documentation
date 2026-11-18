# Three-field models in system codes
<!-- source PDF pages 82-84 -->

<!-- page 720 (PDF 82) -->
However, in a medium term perspective TIA may be used in a more heuristic way to
improve system code predictions provided that:
l
The modeling is simplified to use also SET data without IA measurement. This does not
allow complex modeling with many additional transport equations and many closure laws.
l
One must accept some empiricism in TIA equation closure laws.
l
A step-by-step strategy may be used for TIA implementation in system codes where TIA
may be used in one component whereas algebraic IA models are still used in other
components.
l
Investigations are focused on some important flow conditions such as core flow.
The void fraction range [0; 0.8] in core rod bundle geometry (probably in some kind of
bubbly-slug-churn flow) might benefit from TIA by taking into account the effect of
boiling on the bubble size distribution. It is observed that the slip ratio is smaller when
there is depressurization than at constant pressure due to many small bubbles being
created by flashing. Such effect cannot be modeled with algebraic IA and could be
modeled by a simple TIA equation. In this case, the unknown would be empirically
fitted on rod bundle data with various heat fluxes and with both constant pressure and
during slow blowdown.
In order to support this modeling effort, new experiments in core geometry
would be necessary starting with a characterization of a flow regime map for
rod bundle. Very few data were reported and only in adiabatic low pressure low
temperature air-water conditions. All effects of pressure, temperature, and boiling
or flashing must be investigated before having reliable information in reactor
conditions.
Multifield models have to be developed in parallel to be able to improve modeling
of annular-mist flow, stratified-mist flow, bubbly-to-stratified flow regime transition,
and stratified to stratified-mist flow transition. In all these flow conditions, one phase
is split into a continuous field and a dispersed field and TIA could be used for the
dispersed field provided that both fields are treated separately.
11.16
Three-field models in system codes

## 11.16.1 The situations of interest for three-field models

The annular-mist flow is clearly better described by a three-field model with separate
balance equations for droplets and continuous liquid. This approach has been developed
for a long time in the context of dry-out investigations for BWRs. The
COBRA-TF (Thurgood et al., 1981; Gl€uck, 2008a, 2008b) component code has been
developed with a three-field model for a long time. The NASCA component code
(Ninokata et al., 2000) also uses a three-field model. COBRA-TF was used in combination
with system codes in COBRA-TRAC or in the MARS system code (Jeong
et al., 1999). Fig. 11.30 shows a typical evolution of flow regimes in a boiling channel.
The domain of annular-mist flow is characterized by the splitting of the liquid phase
into two separate fields:

<!-- page 721 (PDF 83) -->
l
the films along the walls with low velocities due to friction along walls;
l
the droplets in the steam core with much higher velocities.
Characteristic transit times of the two liquid fields may be different by one or two
orders of magnitude. A countercurrent flow of films and droplets may also happen
in some transient cases. Droplets are entrained from the crest of waves at the surface
of liquid films. Droplets are then entrained in the steam flow, and may be radially dispersed
by steam turbulent eddies. Some droplets may later be deposited on films by
turbulent eddies. The rate of entrainment E (ratio of droplet mass flow rate to total
liquid mass flow rate) is the result of the combined effects of deposition and entrainment
. In boiling flow, the dry-out occurs when the deposition does not compensate the
film vaporization and droplet entrainment. In two-fluid models with a single-liquid
field models are necessary for predicting:
l
The rate of entrainment E: E models need to assume some kind of equilibrium between
entrainment and deposition to be able to express E as a function of only local values of
Vv, Vl, and α although almost all situations of interest in boiling flow are nonequilibrium
situations with a region where entrainment is larger than deposition followed by a region
with more deposition than entrainment when the film thickness decreases. This is the main
drawback of the one-liquid field modeling of annular-mist flows. Also countercurrent flow
of films and droplets is not predicted by existing correlations.
l
Interfacial friction: models must be able to predict an average liquid velocity of film and
droplets and a total liquid fraction for film and droplets. Although good mechanistic models
exist for drag force applied to droplets and for interfacial friction on film interface, it is very
difficult to find the right combination of both models to express the interfacial friction since
the velocity of each liquid field is not known.
Fig. 11.30 Flow regime evolution in boiling channel with a zoom on the phenomena in the
annular-mist flow.

<!-- page 722 (PDF 84) -->
The three-field model has much better capabilities in such annular-mist flow provided
that good entrainment and deposition models are available. Dry-out investigation
benefited a lot from such three-field models (see Frepoli et al., 2003; Jayanti and
Valette, 2005).
In CATHARE-3, a three-field model has been developed in order to improve the
simulation of the reflooding phase of an LB LOCA (see Fig. 11.31) at different locations
such as the core, the vessel UP, and the HLs. This requires additional experimental
data for validation with information on droplet entrainment and deposition in
such components. The interest for PWR was shown when revisiting LBLOCA with a
three-field model (Valette et al., 2011). Oscillatory reflooding is observed at the
beginning of the process of a gravity driven reflooding. When water from the accumulators
first enters the core, a large quantity of vapor is generated due to the heat
transfer from the hot rod cladding. This initiates flow oscillations between the downcomer
and the core. At each oscillation, some water may be lost at the break on one
side and some water is entrained out of the core to the UP on the other side. The
amount of coolant lost at the break depends on the oscillation amplitude and affects
the core reflooding efficiency, by reducing the water head in the downcomer. On the
other hand, droplets entrained out of the core are vaporized when meeting hot walls
in the UP, in HLs or in the SG tubes. This is unfavorable for the reflooding because
Countercurrent
flow of drops and
films
Stratified
mist flow
Fig. 11.31 Sketch of a reflooding phase of a PWR LBLOCA. Separate drops and continuous
liquid field coexist at top of the core, in upper plenum in hot legs and in SG headers.
