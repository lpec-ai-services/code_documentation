# Developing and validating closure relations
<!-- source PDF pages 63-63 -->

<!-- page 701 (PDF 63) -->
11.11
Developing and validating closure relations
Physical models are required to close the system of equations. Closure relationships
concern mass, momentum, and energy exchanges between phases and between each
phase and the wall. In a first step, code developers look at the scientific literature to find
such models. When they exist, they were often developed based on theoretical work and
from rather academic experimental data such as air-water flow in a circular pipe with a
large length to diameter ratio. They must be later confronted to more industrial flow
conditions, with steam-water data in larger ducts of various shapes. Specific separate
effect tests (SETs) were performed and analyzed to investigate two-phase flows in conditions
more representative of the reactor transients to be simulated. Based on these data
new correlations were developed when existing models were not satisfactory. The
degree of empiricism depends on the understanding of the physical mechanisms
involved. In the domain where experimental and theoretical knowledge was still missing
, extrapolations or interpolations were adopted by making simple assumptions.
Thermal and mechanical transfers are interconnected in steam-water two-phase
flows. However, it was often assumed in a first approximation that mechanical interactions
do not strongly depend on thermal exchanges. A step-by-step method was then
used. Mechanical terms were first derived from experiments where thermal nonequilibrium
is negligible. Interfacial heat transfer terms were then derived. Finally
wall to fluid heat fluxes are correlated.
One may distinguish four different approaches used to establish the closure
relations:
1. The fully empirical approach: representative experiments are carried out in the required
range of parameters and a transfer term of the system of equations is measured together with
the main variables. A correlation is then established between the transfer term and the main
variables of the flow by using some fitting technique or interpolation technique. CATHARE,
TRACE, and RELAP use CHF look up tables for the CHF prediction. This method may be
the most accurate but it requires a lot of experimental data and it does not allow extrapolations
out of the domain covered by data.
2. Empirical approach with dimensional analysis: correlations are here expressed with dimensionless
numbers. Since many dimensionless numbers exist in two-phase flows, a preliminary
analysis may allow to identifying the controlling physical processes and only the
dimensionless parameters which are assumed to play a role are used in the correlation. This
method was used to establish “full-range drift flux correlations” by EPRI (Chexal and
Lellouche, 1986) or the Kataoka and Ishii (1987) drift flux correlation.
3. The phenomenological or mechanistic approach: A governing physical mechanism is
assumed and an expression of the transfer term is derived theoretically. Expressions of
the added mass force, or of the interfacial friction for dispersed droplet flows are examples
of this method. The validity is verified a posteriori by comparison with experimental data.
The quality depends on the appropriateness of the basic assumptions made on the governing
processes. Very few models are of this type. The added mass force was developed from analytical
calculations of a potential flow around a sphere in acceleration. The pressure difference
term in stratified flow was derived from simple assumption of a transverse gravitational
pressure gradient in a horizontal channel (de Crecy, 1986; Bestion and Serre, 2012).
