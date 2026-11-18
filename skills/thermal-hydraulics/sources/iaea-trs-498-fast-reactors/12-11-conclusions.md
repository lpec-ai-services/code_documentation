# 11. CONCLUSIONS
<!-- source PDF pages 81-83 -->

<!-- page 69 (PDF 81) -->
experiments or simulations could be conducted with variations in the parameters
to study their effects on the results. However, this is not always possible.
Especially for long running experiments or simulations (examples include long
running transients for normal operations, design basis conditions and design
extension conditions in STH code, 3-D CFD simulations, and coupled multiscale
or multiphysics simulations), more efficient methods need to be used. Such
methods are under development and being tested. Overviews on uncertainty
evaluations can be found in Refs [202–204]. An example of how uncertainties
can be quantified in CFD is elaborated by Lascar et al. [205], and examples of
uncertainty quantification for STH codes are summarized in Ref. [206]. Some
best practices in uncertainty quantification are provided in Ref. [201]. The
textbook by Roelofs [23] includes a section specifically dedicated to uncertainty
quantification in liquid metal thermal hydraulics.

# 11. CONCLUSIONS

As is the case with any nuclear reactor, thermal hydraulics is an important
topic in the development and safety analysis of fast reactors. Since it has become
clear that water cannot be used as a coolant in fast reactors, all previous studies
and conclusions from water experiments should be considered with care. This
starts with the fundamental revisiting of the correlations for friction or pressure
drop and heat transfer and the related turbulence models. These topics need to
be analysed in all flow regimes, ranging from natural convection to mixed and
forced convection for different geometries, from round tubes to rod bundles, for
fuel bundles with wire and with grid spacers, and for single- and multiphase flow
conditions. With respect to correlations, one challenge lies in the interpretation
of existing correlations based on experiments dating back to the 1960s, 1970s
and 1980s. Another challenge is to go beyond standard operational conditions
and include geometrical deformations of fuel assemblies, pin structures
and other effects (e.g. blockages). Increasingly, it is important to study this
using a combination of experiments and numerical analysis. With respect to
turbulence modelling, designers and modellers are aiming to develop a model
that can predict heat transfer for different coolants with reasonable accuracy.
To achieve this, a combination of experimental and high resolution numerical
data is being generated. Progress is ongoing, but a final acceptable solution
for the turbulence model has not yet been found. Therefore, most analysts use
very rough approximations while recognizing that this may lead to decreased
accuracy. A specific topic to be studied is internal heat generation, which plays an

<!-- page 70 (PDF 82) -->
important role in molten salt fuelled reactors. The main challenge here is the lack
of experimental data and the difficulty of obtaining more.
For the other design and safety analysis related aspects, experiments
are widely used to increase understanding and to support the development of
correlations and models, and experimental data also support validation. However,
since fast reactors utilize different coolants from the more commonly used
water or air, these experiments often become complex, and the instrumentation
may lack accuracy or may not be available at all (e.g. because of the high
operating temperatures, specific chemical effects, or the opacity of the coolant
in use). Sharing information and experiences related to operating such facilities
is crucial to the development of fast reactors, as is the sharing of progress in
instrumentation that can be operated under the harsh environmental conditions
found in fast reactors.
While much can be discussed regarding computational modelling and
simulation across different levels of computational efficiency and accuracy, a key
aspect is the necessity for close interaction with experimentalists to establish trust
in the simulations. A variety of experiments is needed, ranging from fundamental
tests that focus on individual phenomena to integral tests where the combination
and interaction of various effects becomes crucial.
With growing computational power, the role and impact of high resolution
simulations merits attention. These simulations can furnish validation data
alongside experimental results. As confidence in simulations increases, their
scope of applicability may transition from supporting design to aiding in
licensing. Another crucial aspect involves determining the subject of the
simulation. Although operational situations and accidents traditionally receive
considerable attention, events following an accident should not be overlooked.
This pertains to severe accident and containment analysis, posing a challenge
for water cooled reactors and an even greater one for fast reactors using diverse
coolants. Acquiring experimental data for model development and validation
in these scenarios is intricate. Here again, high resolution simulations may
increasingly offer valuable support.
Increasing computer power also empowers the development of multiscale
and multiphysics simulation tools. There seems to be some consensus that the
development of integrated generic coupling tools, in which various separate scale
or physics tools can be coupled, will be needed for several reasons. First, and
perhaps most importantly, a generic coupling tool will enhance the likelihood
of acceptance by designers and/or regulators. Second, it will allow users to
become familiar with this tool, which is supposed to reduce user and code effects
in the analysis chain. Finally, such integrated generic tools will allow for easier
maintenance and help prevent unexpected anomalies. A short overview has been
provided on code coupling platforms currently under development worldwide

<!-- page 71 (PDF 83) -->
(Table 6). Future directions for development have been identified as follows:
(a) improving the acceleration and robustness of the platform; (b) including phase
change models (e.g. with respect to solidification); (c) including multiphase flow;
(d) allowing full core analysis, including bypass; (e) expanding to severe accident
conditions; (f) improving thermomechanical solvers; (g) developing uncertainty
quantification methods for coupled simulations; (h) developing modern fuel
performance tools; (i) supporting high resolution (fidelity) experiments and
tools to create additional, complementary reference data; (j) validation (towards
licensing); and (k) developing integrated pre- and postprocessing tools.
Obviously, the V&V of simulation tools is essential to the licensing process.
In this regard, international benchmarks organized by the IAEA contribute to
the level of V&V of a specific code. The outcomes and lessons learned of five
benchmarks organized by the IAEA have been discussed. Key observations
are as follows:
— It would be worthwhile to develop a complete validation process for the
numerical codes used in the prediction of natural convection decay heat
removal in different tests: analytical, reduced scale and full scale.
— Small geometric details and meshing may have a major impact on
simulation results; therefore, careful consideration and documentation of
assumptions are needed.
Finally, the utilization of legacy nuclear reactor data has been discussed,
and its potential to address the requirements for experimental validation
acknowledged. In this regard, it can significantly contribute to the incorporation
of thermal hydraulics knowledge and tools into the licensing procedures for
emerging fast reactors.
This publication is anticipated to serve as a valuable resource for
students and professionals actively engaged in the intricate field of thermal
hydraulics analysis for fast reactors. As a comprehensive repository of insights,
methodologies and findings, it is designed to cater to the diverse needs of
individuals seeking a deeper understanding of the complexities inherent in fast
reactor thermal hydraulics.
