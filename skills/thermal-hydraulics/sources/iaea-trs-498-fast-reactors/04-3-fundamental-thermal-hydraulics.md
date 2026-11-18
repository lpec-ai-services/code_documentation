# 3. FUNDAMENTAL THERMAL HYDRAULICS
<!-- source PDF pages 23-26 -->

<!-- page 11 (PDF 23) -->
# 3. FUNDAMENTAL THERMAL HYDRAULICS

## 3.1. HEAT TRANSFER AND FRICTION FACTOR CORRELATIONS

For the thermal hydraulics assessment of nuclear reactors (e.g. using a
system code or subchannel analysis), theoretical and empirical correlations are
the backbone of the analysis. Such correlations (e.g. for the friction factor or the
heat transfer) have been developed since the dawn of the nuclear programme, and
some even earlier.
Iida and Guthrie [14] mention that “all liquid metals are believed to be
Newtonian”. This would mean that, at any given temperature, there exists a
linear dependency of the applied shear stress on the shear rate experienced by the
liquid, and the slope of this dependency represents the constant shear viscosity.
However, reasonable doubts about the assumption of Newtonian behaviour in
sodium have been raised in the past few years [15]. Nevertheless, in this section,
it is assumed that at least the few liquid metals under consideration as coolants
in fast nuclear reactors (i.e., sodium, lead, or alloys of sodium or lead) can be
considered Newtonian fluids.
Even in that case, large amounts of data are needed as input for the
development of correlations. Huge programmes for this ran worldwide in the
1950s and 1960s, especially in the Russian Federation [16] and the United States
of America (USA) [17]. Data were built up from relatively simple and standard
geometries, like flat plates and pipe flow, to more relevant configurations like
annular channels and rod bundles that are representative of a nuclear core or a heat
exchanger. Note that new data continue to be added to the already large database
of friction factors and heat transfer correlations. International organizations like
the OECD/NEA and the IAEA are now undertaking efforts to collect and evaluate
such data in order to serve the nuclear community and provide an international
standard for properties and correlations. The most recent examples are the
database on lead alloys from the OECD [12] and the Natrium Property Database
under publication at the IAEA, as summarized in Passerini et al. [18].
The application of friction factor and heat transfer correlations to actual
designs requires careful consideration of the applicability range of these
correlations. Whereas Mikityuk [19] tries to derive a general correlation for
liquid metal heat transfer covering various design choices, Pacio et al. [20] focus
their work on the licensing support for the Belgian MYRRHA reactor design,
specifically regarding the friction factor correlations of wire wrapped fuel

<!-- page 12 (PDF 24) -->
assemblies employing lead bismuth as coolant. This is a detailed work presenting
a methodology that can also be applied to other reactor designs.
However, Kuzina et al. [16] make clear that numerical analyses cannot be
limited to a ‘cold’ or ‘paper’ design. In reality, components, especially fuel pins
and elements, will be subjected to forces, even during normal operation, that
may cause them to deform. This is in addition to the situations that need to be
considered when accidents play a role. It is important to realize that a component
like a fuel assembly as it was designed on paper will be subject to various changes.
First, the assumed smooth surface (which may not be smooth at all because of
manufacturing limitations) may be affected by coolant chemistry, corrosion and
erosion, impacting the friction and heat transfer. Second, the fuel pins and the
wrapper or housing of the fuel element may deform as a result of temperature
increases, prestress and irradiation effects. It is known that these phenomena take
place (e.g. Katsuyama et al. [21] or Sorokin et al. [22]), but little is known about
how they affect the overall deformed bundle friction and heat transfer. It remains
challenging to accurately predict the development and shape of the deformation,
making it difficult to simulate this in a numerical test benchmark. Taking this into
account, a clear need can be identified to generate new experimental data or high
resolution numerical data for distorted subchannel geometries with fuel swelling
and/or bowing, with or without errors in the standard wire spacer position, as
well as for bent and deformed bundles under operational and accident conditions.
These data can be used as a reference for the development of correlations and for
the validation of simulation approaches.

## 3.2. TURBULENT HEAT AND MASS TRANSFER

In the field of computational fluid dynamics (CFD), one of the key challenges
remains the modelling of turbulence and turbulent heat transfer, especially in the
efficient and most commonly used Reynolds averaged Navier–Stokes (RANS)
approach. Within this field, the RANS equations are typically closed either
by modelling the Reynolds stresses using one or two equation eddy viscosity
models or by six equation Reynolds stress models. The industry mostly uses
linear eddy viscosity models because they are computationally efficient and
robust. However, these linear models are based on the assumption of isotropy in
turbulence; that is, it is assumed that turbulent characteristics are the same in all
directions. This assumption, however, is not true in many nuclear applications,
driving the need for the development of non-linear eddy viscosity models or
robust Reynolds stress models. A straightforward example of anisotropic flow
where such models are needed is the flow in a nuclear fuel bundle, as explained,
e.g. by Kuzina et al. [16]. They show that secondary flows occur in a grid spaced

<!-- page 13 (PDF 25) -->
bundle, which impacts heat transfer. They also mention that such anisotropic
flows probably play a role in the edge channels of a closed fuel assembly and
in fuel bundles with deformations. On the other hand, many studies have shown
that, to simulate the turbulent flow in a wire wrapped bundle, an isotropic eddy
viscosity model may be sufficient [23].
When heat transfer is considered, the most widely used and robust
approach is the standard gradient diffusion hypothesis, along with the Reynolds
analogy, which assumes a similarity between turbulent momentum and heat
transfer. This assumption uses the turbulent Prandtl number in most codes,
with a constant default value of 0.85. This value provides sufficiently accurate
results for flows using water or air as a medium. However, for liquid metals,
the Reynolds analogy no longer holds, and it is important to consider that the
value of the turbulent Prandtl number changes in the flow field. In order to take
into account the effect of liquid metal heat transfer, some authors propose using
a constant value of the turbulent Prandtl number of the order of 1.5 or 2 [24].
Another option is to introduce a variable Prandtl number that depends on the
Péclet number (see e.g. Ref. [25]). Such solutions might provide improvements
compared with the standard Reynolds analogy and yield reasonable results
for forced convection flows. However, to achieve real accuracy, the standard
gradient approach cannot be used, and a general gradient diffusion hypothesis
approach is applied [26]. This academic approach is accurate, but it comes at the
cost of robustness and computational efficiency. An approximate solution can be
found in the application of algebraic heat transfer models. There are many such
models to be found in the literature for specific applications where the Reynolds
analogy is known to fail. In recent years, the applications to liquid metals have
also been under development [27]. The main challenge for these models is that
they are very sensitive to proper calibration, and therefore their application
range is typically restricted. Additionally, many models to date require a priori
knowledge of the flow field (e.g. because they use the Reynolds or Rayleigh
numbers as input). Here, the challenge is to develop a model that will not require
a priori knowledge of the flow field but will set its coefficients based on local
parameters [28]. Another option is to use artificial intelligence. As an example,
Fiore et al. [29] use a machine learning strategy for the modelling of the turbulent
heat flux. They derive a comprehensive, algebraic, mathematical structure and
impose physical constraints to achieve applicability, robustness and stability. The
closure coefficients of the model are predicted by an artificial neural network
trained with direct numerical simulation (DNS) data at different Prandtl numbers.
For all approaches, experimental and high resolution reference data are
needed for model development, calibration, training and/or validation. A recent
list of available data was collected by Roelofs [30]. However, a quick inspection

<!-- page 14 (PDF 26) -->
shows that the data available mostly refer to forced convection cases. There is a
clear need for additional data on natural and mixed convection regimes.

## 3.3. NATURAL AND MIXED CONVECTION

As mentioned in the previous section, the behaviour of turbulent heat
transfer under natural and mixed convection conditions demands more data.
However, this is the case not only for turbulent heat transfer. In general, the
behaviour of liquid metals under natural and mixed convection conditions
needs more data, especially regarding the transition from forced to natural
convection and the onset of natural convection. These are focal points in large
scale experimental loops and set-ups like the Natural Circulation Experiment
(NACIE) [31], Circolazione Eutettico (CIRCE) [32] and E-SCAPE [33]. Such
experimental data are being used to validate numerical codes at different scales,
ranging from system thermal hydraulics (STH) codes to three dimensional (3-D)
CFD codes. Special attention is being paid to the simulation capabilities of STH
and 3-D CFD codes under asymmetric conditions, as well as to the feasibility
of using 3-D CFD approaches for long transients, given their requirements for
computational resources. To this end, multiscale coupled approaches are also
being studied, in which STH codes are coupled to 3-D CFD codes in cases where
3-D effects are assumed to be important (e.g. Refs [34, 35]).

## 3.4. FLUIDS WITH INTERNAL HEAT GENERATION

A special type of fundamental flow to be studied involves fluids that
include internal heat generation. This is a peculiar and unique feature of liquid
fuelled molten salt reactors, although it is important to mention that other
reactor types also exhibit non-negligible gamma heating outside the core of the
reactor. In order to develop and validate numerical tools for such applications,
reference data are needed for validation. Unfortunately, there are hardly any data
available from experiments. The most used data are from the Molten Salt Reactor
Experiment that was in service in the USA in the late 1960s [36]. System thermal
hydraulics codes are now being developed that can handle these types of flows
(e.g. see Ref. [37]).
However, these experiments, even if they were well described, took place
half a century ago. Not all knowledge has been preserved, and the complete reactor
system was quite complex. Additionally, the experiments included various effects
that may not be well known or described. Therefore, there is a clear need for new
validation data regarding fluids with internal heat generation. Obviously, this is
