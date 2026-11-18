# Part 2. Insights into computational fluid dynamics for nuclear power plant applications — Applications of CFD—Examples
<!-- source PDF pages 36-48 -->

<!-- page 764 (PDF 36) -->
l
Problem-specific BPG (Boyd, 2016). Many problems (e.g., multiphase PTS problems) have
multiple layers of interacting two-phase phenomena as well as single-phase phenomena,
each with their own unique best-practice modeling approach. These types of complexities
complicate the selection of models and solvers and ultimately lead analysts to pursue
compromised approaches. Problem-specific best-practice guidelines can take years to
develop and require updates as new methods and models are developed and tested. It is
common for compensating errors to mask underlying problems in the model and these issues
can cause problems when models are scaled from test facilities to full-scale conditions.
These types of complexities make it difficult for a reviewer to answer the question of
whether or not a CFD prediction can be trusted for the intended application.
l
Acceptability of CFD prediction. NRS application of CFD to individual NPP unit (e.g.,
licensing process) implies the use of validated/approved methodology. In this case the
well-known scaling problem comes into play and scaling capabilities shall be demonstrated
for the methodology (of CFD application) other than for the results of the CFD application.
−
Extrapolation/extrapolability of the CFD methodology: This is topic of current interest
to the scientific community. No conclusive/meaningful statement can be provided (i.e.,
in addition to the qualitative identification of the issue).
−
Extrapolation/extrapolability of CFD results: This is topic of current interest to the
scientific community. No conclusive/meaningful statement can be provided (i.e., in
addition to the qualitative identification of the issue).

## 12.8 Applications of CFD—Examples

12.8.1
PWR rod bundle problem–EPRI CFD round robin
benchmark exercise
We consider below an example of the CFD application. This is related to flow and heat
transfer in a PWR rod bundle with mixing vane grids; crud-related and DNB-related
issues are concerned. Local information (hot spot) is available from experiments that
only CFD can produce. Bullet items in the following summarize key aspects of the
EPRI CFD round robin. The complete report can be found in EPRI (2014) and
EPRI (2015).
l
EPRI-led CFD round robin benchmark exercise. The EPRI-led CFD round robin benchmark
exercise against the NESTOR experiment for a PWR rod bundle has been recently
completed (the steps of the activity can be derived from Fig. 12.10). This project has great
advantages in that (i) the round robin type validation enables us to test and compare various
CFD methodological factors and thus to obtain overall insights into CFD capabilities and
limitations; and (ii) the NESTOR experiment has broad-range, accurate measurements of
rod inner-surface temperatures as well as flow field under the thermal-hydraulic conditions
comparable to typical PWR ones. In this section, we summarize the capabilities and limitations
of CFD methods (steady RANS approaches) especially for split-type mixing vane
grids, based on the submitted CFD results along with NESTOR data (EPRI, 2014, 2015).
(1) Structure of the exercise. The benchmark exercise consists of two phases depending on
the rod bundle types as shown in Fig. 12.10: Phase 1 is for the SSG rod bundle with only
simple support grids (SSG) and Phase 2 is for the MVG rod bundle with SSGs and alternating
split-type mixing vane grids (MVGs) (Fig. 12.11). For each phase, we considered

<!-- page 765 (PDF 37) -->
four problems—one problem for the isothermal case (MANIVEL) and three problems
with different thermal-hydraulic boundary conditions (OMEGA) for the thermal case to
check the consistencies of the CFD results. In this discussion we focus only on Phase 2,
i.e., the MVG bundle with split-type mixing vanes.
(2) NESTOR experiment. In the NESTOR-MANIVEL experiment, the grid span pressure
drop and the mean and RMS axial velocities were measured (see Fig. 12.11, left) and in
the NESTOR-OMEGA experiment rod inner-surface temperature and fluid temperature
at subchannel centers at the end of heated length were measured (see Fig. 12.11, right).
(3) Test conditions. For an isothermal problem, Reynolds numbers based on the regular subchannel
hydraulic diameter (ReSC) is 101,000. For thermal problems in Phase 2, Reynolds
numbers based on the regular subchannel hydraulic diameter and average
temperature (ReSC) are in the range 450,000–580,000. Detailed thermal-hydraulic conditions
are provided in the EPRI Phase 2 report (EPRI, 2015).
(4) Participants. In Phase 2, seven organizations (ANSYS, AREVA, CD-adapco, EDF, Penn
State University, Texas A&M University, and Westinghouse) participated. Two commercial
CFD codes (ANSYS Fluent and STAR-CCM+) and one open-source CFD code
(Code_Saturne) were used as CFD solvers by the participants. They considered only
steady RANS approach due to large-scale problems in this benchmark. The Phase 2 analysis
report (EPRI, 2015) provides the detailed information about CFD methods adopted.
l
Capabilities of steady RANS. The main insight from Phase 2 round robin benchmark was
that appropriate steady RANS approaches with wall function could reasonably predict
two key variables in the PWR fuel rod bundle with split-type mixing vane grids—the grid
span pressure loss and rod surface temperature distributions. Here, the appropriate steady
RANS approach indicates that (i) fluid and solid region meshes are suitable for the complex
geometry of the grid and wall-function requirement and (ii) conjugate heat transfer is considered
. Also, the “reasonable” prediction specifically means that (i) the pressure loss errors
for SSG and MVG spans are within about 5% and about 10%, respectively; and that (ii) the
circumferentially averaged rod inner-surface temperature errors at different elevations for
different rods are within [·2 to 3 K], Fig. 12.12B, and the RMS errors around the circumference
(at different elevations for different rods) are within 2–4 K. Overall, the CFD calculations
under the trim mesh with extrusion layers consistently showed good results. In
addition, the effect of turbulence anisotropy was relatively reduced in the MVG wake region.
l
Limitations of steady RANS. On the other hand, the steady RANS approaches showed limitations
: (i) they could not capture well central rod circumferential temperature distribution
Isothermal
(NESTOR-MANIVEL experiment)
Thermal
(NESTOR-OMEGA experiment)
PHASE 1
SSG bundle configuration
PHASE 2
MVG bundle configuration
Exercise 1
Exercise 1
Exercise 2-1
Exercise 2-2
Exercise 2-3
Exercise 2-1
Exercise 2-2
Exercise 2-3
Fig. 12.10 Structure of EPRI-led CFD round robin benchmark.

<!-- page 766 (PDF 38) -->
Fig. 12.11 Test section and measurement information of the MVG bundle (Phase 2) in
NESTOR experiment.

<!-- page 767 (PDF 39) -->
patterns in the far wake (see Fig. 12.12 right) probably because of the cross-flow reorientation
(and dumping) due to the interaction between asymmetric, cross-flows with test
section wall, and (ii) they showed quite large local maximum rod inner-surface temperature
error (ranging 4–9 K with elevation), Fig. 12.12B probably because of unsteady, large-scale
cross-flow fluctuation effect. In addition, it should be pointed out again that in the actual
applications to PWR fuel rod bundles where the test section wall is not present except near
the core barrel, the unsteady, large-scale cross-flow fluctuation effect on the circumferential
temperature variation magnitude may be of greater importance than the test section wall
effect on the flow pattern changes.
Fig. 12.12 Inner-surface temperatures around the central rod (Rod 5) in the MVG O2 wake:
(A) comparison of circumferentially averaged temperature; (B) the maximum errors of the
circumferential distributions of the inner-surface temperature distribution, and (C) comparison
of circumferential distributions of the inner-surface temperature at intermediate (left) and far
wake (right) regions: pink symbols indicate measured data, and lines with symbols indicate
CFD calculation results.

<!-- page 768 (PDF 40) -->
#### 12.8.1.1 Experimental data

It was found that NESTOR experiment had several advantages over other experiments
. The representative ones were as follows:
l
It was in full-length axial domain (with fully heated length for thermal cases) comparable to
the actual PWR rod bundle that CFD calculations could be directly assessed by comparing
the results with data measured at upper spans (target region). As a result, it was found that
steady RANS approach could provide a reasonable accuracy in this general application.
l
A direct comparison of target variable, i.e., rod (inner-) surface temperature, was possible,
thus providing important findings that could not or hardly be obtained by the comparison of
the flow field only. They were mismatch of the patterns and overprediction of the magnitude
in the circumferential temperature distribution as well as importance of conjugate heat
transfer.
l
Data measured over several spans enabled us to check the representativeness (consistency)
of the results and phenomena.
l
A typical split-type MVG (used before in industry) was adopted in the experiment; thus, the
effects due to atypical geometries were reduced. For example, rod-contact structures with a
cylindrical button shape in the OECD-KAERI CFD benchmark (Smith et al., 2013) induced
stronger unsteady effect (vortex shedding) than that expected in typical spring and dimple
structures. In fact, the Axial Turbulence Intensity (ATI) in the OECD-KAERI CFD benchmark
(ATI about 0.22 at z-zMVG=1 Dh and about 0.14 at z-zMVG=4 Dh) was much higher
than that of NESTOR (ATI about 0.12 at z-zMVG=2.4 Dh and 0.09 at z-zMVG=4.9 Dh) and
Yang and Chung (1998) (ATI in the range 0.12–0.14 at z-zMVG about 2 Dh and ATI in the
range 0.09–0.1 at z-zMVG about 4 Dh) experiments with typical springs and dimples. Here, Dh
is a test section hydraulic diameter, not an inner-subchannel hydraulic diameter (Dh,SC).
However, the NESTOR experiment also showed several limitations for the CFD validation
. The related important ones and associated recommendations are as follows:
l
The asymmetrical effect due to the test section wall, which also holds for the previous,
typical split-type MVG rod bundle test with a small-size (4≡4, 5≡5, or 6≡6) array, exists.
The resulting qualitative cross-flow pattern change and complex far-wake flow patterns in
the experiment may not be representative of typical physics in the actual PWR rod bundle
and turned out to be challenging to CFD calculations. Thus, we may need to increase our
understanding of the involved physics by improved experiments as well as advanced
CFD methods.
l
The simple support grid (SSG) installed between MVGs for the structural integrity prevented
us from seeing the phenomenon at farther wake region (Dh,SC>25) of great interest in the
real applications, such as prediction of CHF and crud deposition. However, previous experimental
investigations (Yang and Chung, 1998) and CFD studies (Blowe et al., 2015; Bieder
et al., 2014) showed that the vane-driven cross-flow effects reach the next grid even for a
long MVG span without the SSG in the middle. The far-wake physics in the longer
MVG span without the SSG should be measured and compared with CFD calculations in
the future.
l
Since the lateral flow field was not measured, important phenomena like swirl decay and
cross-flow pattern change along the rod bundle could not be directly evaluated. The lateral
velocities (covering both the gap and near-rod regions) need to be measured.
l
In addition, the full-length axial domain, although it was an advantage of this experiment in
that we could do the comprehensive and practical CFD assessment, prevented us from

<!-- page 769 (PDF 41) -->
clarifying the source of discrepancies between the measurement and the CFD calculations.
Especially, the spatial aperiodicity probably due to the different MVG inlet velocities made
it difficult to identify whether a certain discrepancy was in common or what factors caused
discrepancies. Thus, upstream (MVG inlet) flow condition-controlled experiments may be
more desirable to identify and understand the related problems. For example, we can
basically consider a fully developed MVG inlet condition from very long bare rod section;
furthermore, we can put a long (without SSG in the middle) MVG span with 90°-rotated
MVG as in a typical PWR and without MVG rotation for the reference at the upstream
of the target MVG span.
Among these limitations, the first item, i.e., the wall effect in the 5≡5 array test, needs
to be discussed in more detail for the more realistic CFD assessment and more improved
experimental design for the split-type MVG rod bundle problem in the future.
The most critical wall effect may be due to the cross-flows from inward peripheral
vanes at edge- and corner-subchannels near the wall. The cross-flows generated in
these regions are quite different from those in inner subchannels in that (i) they have
less axial flows upstream of the vane (because they are near the wall) and thus less
cross-flows and (ii) they do not have the same swirl structures as those of other inner
subchannels because they only have one vane not a pair. Thus, as the distance from the
MVG increases, each inner subchannel becomes affected by the wall cross-flows
(different from the inner subchannel cross-flows in magnitude and pattern) depending
on the vane direction and relative distance to the wall. Consequently, each subchannel
has asymmetrical lateral flow patterns (swirl patterns), and the overall cross-flow
pattern could change qualitatively and globally in 5≡5 array test. On the other hand,
considering geometrical configuration in the actual PWR rods, except rods near the
barrel, rods are very far from the wall. Thus, this phenomenon may not be a representative
one in the actual PWR rod bundle.
To remove or minimize the wall cross-flow effect, we can simply consider much
larger lateral domain experiment; however, this seems practically undesirable.
Instead, we may be able to find a way under the existing 5≡5 test facility. For example
, we can remove the inward peripheral vanes near the wall of 5≡5 test section
under the hypothesis that it is more desirable to remove the wall cross-flows than
to involve wrong (in pattern and magnitude) wall cross-flows so that the lateral flow
patterns in central subchannels in 5≡5 test represent that at a typical subchannel in the
actual PWR rod bundle. In fact, Navarro and Santos (2009) compared lateral velocity
vector fields between models with and without peripheral vanes obtained from their
CFD calculations. They showed that without peripheral vanes the swirl pattern in
inner subchannels was maintained at the far wake (of 18Dh,SC), while with peripheral
vanes the lateral flow patterns were irregular at the same axial location. From this
result, they argued that the case without peripheral vanes is more representative of
typical inner subchannel flow behavior in the actual PWR rod bundle.

#### 12.8.1.2 Adopted CFD methods

Now, we address lessons and recommendations about respective CFD methodological
factors for typical split-type MVG rod bundle problems.

<!-- page 770 (PDF 42) -->
##### Mesh

The round robin benchmark enabled us to see the characteristics and effects of various
types and configurations of mesh, which was a key advantage of this approach (Kang
and Hassan, 2016). However, direct comparisons of mesh between different types and
between different configurations even for the same mesh type were impossible in most
cases, and the mesh sensitivity results for each submitted mesh were not reported.
Furthermore, compared to the trim mesh type, limited numbers of other types of mesh
were considered. Thus, it is difficult to derive detailed conclusions about the mesh.
Nonetheless, a qualitative finding was clearly observed that the calculation results
strongly depended on the mesh types (rather than turbulence closure models).
For hexahedral mesh considered, the pressure loss across the grid and turbulent fluctuations
was largely underpredicted for both SSG and MVG spans. On the other hand,
trim mesh calculations showed much more improved results of these variables. Especially
RMS
axial velocity
fluctuations
just
downstream
of
the MVG
(at
z-zMVG=25 mm) were comparable to the measured ones (see Smith et al., 2013).
The dependence on the mesh type observed in this benchmark was also observed
in the OECD-KAERI CFD benchmark (e.g., by Lee et al., 2014) although the
vane-upstream grid structures used in OECD-KAERI benchmark were different.1
However, this does not necessarily mean that a certain type of mesh is superior to
other types of mesh. For split-type MVG problems that are characterized as (i) the high
complexity in the grid region, (ii) axially large difference in the geometry complexity,
(iii) vane-driven high velocity gradient in the near wake, and (iv) critical effect of in
and near-grid region flows on the downstream flows, efficiently generating consistent,
high-quality mesh is important. From this point of view, trim mesh (with extrusion
layer) that seems able to provide consistent (less dependent on the participants)
and good quality and that is less time-consuming to generate may be a good choice.
On the other hand, the large discrepancies of the hexahedral mesh calculations are
likely due to the strong nonorthogonality of mesh in- and near-grid regions (EPRI,
2015; Benhamadouche, 2015). The structured hexahedral mesh seems difficult to
keep uniform quality for geometry with large difference of complexity in streamwise
direction and at near-wall (of grid structures and vanes as well as rod) and high
velocity-gradient regions.
Also, a detailed mesh sensitivity study is strongly recommended to get more
detailed conclusions about mesh. For example, although the flow field results were
quite similar among different participants under trim mesh, the pressure loss across
the MVG ranged from ·3% to 11%. Thus, we need to investigate what factors in mesh
configuration are important to improve the pressure loss results: for example, effect of
1In the OECD-KAERI CFD benchmark (Smith et al., 2013, see also Lee et al., 2014), the under-prediction of
the RMS velocity fluctuation was attributed to the limitation of steady RANS turbulence models where
RMS values can be obtained only from the modeled term of the turbulent kinetic energy. However, in
OECD-KAERI benchmark, SP09 (steady RANS k-ε model with hexahedral mesh that seemed similar
to that used in this benchmark) showed such large under-prediction at the near-wake (z-zMVG=1 and
4Dh), while SP18 (steady RANS k-ε model with trim mesh with extrusion layer) showed comparable results
(scores) to other unsteady RANS calculation results of SP17 (unsteady RANS SST k-ω with polyhedral
mesh) and SP19 (unsteady RANS BSL EARSM with hybrid mesh).

<!-- page 771 (PDF 43) -->
the local mesh refinement in the region where the higher velocity gradient is expected
and the effect of y+ in the mesh adjacent to the grid structure (under the wall function
assumption) using/adjusting the extrusion (prism) layer(s) shape and size.

##### Turbulence closure models

It could be inferred from the comparative results in this benchmark that the use of
anisotropic model was essential in the SSG wake where the cross-flow effect was
small or negligible, while it was not critical to the MVG wake where cross-flows
are still effective. However, this conclusion may need to be reconsidered because
of the following reasons:
l
In the hexahedral mesh, the flows (both mean and RMS velocities) in- and near-grid regions
were not captured well. The mean axial velocity variations at z-zMVG=25 mm showed
smaller than the measured ones (Smith et al., 2013; Lee et al., 2014), which may indicate
that predicted cross-flows and swirls were weaker probably because of the low quality of
the mesh at in- and near-grid regions. Thus, the comparison among different turbulent
closure models (SSG-RSM and k-ε model with linear production) of the flow evolution
downstream (swirl decay and cross-flow interactions) from wrong upstream flows may
not be so meaningful. For a meaningful comparison between turbulence closure models,
the starting point of the swirls and cross-flows should have better quality results, for example
, by adopting the better quality of mesh.
l
In the trim mesh, which showed better quality results than hexahedral mesh at the near wake,
only linear and quadratic k-ε models were considered. Since quadratic nonlinear eddy
viscosity models (NLEVMs) reflect only the normal Reynolds stress anisotropy effect, other
Reynolds stress anisotropy effects related to the streamline curvature and swirls, which can
be included by cubic terms, were not considered. Thus, the similar results between linear and
quadratic k-ε models may only indicate that in the MVG wake, the effect of the normal Reynolds
stress anisotropy is not critical.
Thus, the following recommendations can be made relating to turbulence closure
models in the future research. Here, the premises of these recommendations are that
mesh quality is good enough to capture the main flow physics in- and near-grid
regions, and that unsteady effect is negligible.
l
For nonlinear eddy viscosity models (NLEVMs), which are computationally efficient (only
marginal increase in computational time from the base two-equation closure models) and
robust, we can consider the following:
−
Cubic models can be considered for more general turbulence anisotropy related to swirls
and cross-flow interactions with curved wall and each other. Here, it is worth noting that
we may need a recalibration process of the existing cubic models for this specific problem
. Recall that that modified quadratic k-ε mode (Baglietto et al., 2006) that showed
good results for bare rod bundle problems was obtained by calibrating some coefficients
in the existing SZL quadratic k-ε model (Shen et al., 1991) for the rod bundle geometry.
−
Different scale-determining equations (with calibrations) can be considered. Only k-ε
model was considered in this benchmark. Use of other scale-determining equations, such
as those in BSL k-ω model, may have a significant influence on the downstream flow
evolution because key physics may be dictated by factors other than anisotropy of the
turbulence (Gatski and Jongen, 2000).

<!-- page 772 (PDF 44) -->
−
Alternatively, explicit algebraic Reynolds stress models (EARSMs) (e.g., BSL EARSM)
can be considered. This is because compared to NLEVMs, which can be considered as
nonlinear extensions of the ordinary LEVMs, and coefficients are determined by experimental
and/or higher level turbulence model results, EARSMs, which can be considered
as a truncation of RSMs, can easily combine more physics, such as nonlinear
pressure-strain rate correlation models and anisotropic dissipation rate models, existing
in original RSMs (Gatski and Jongen, 2000; Hellsten and Wallin, 2009). In fact, BSL
EARSM was highly ranked at near-flow field prediction in OECD-KAERI benchmark
under unsteady RANS frame (Lee et al., 2014).
l
Use of RSMs may be a more desirable option because their (theoretically) higher degree of
universality may be more suitable for split-type MVG rod bundle problem that involves
various (and even unidentified) complex phenomena although they require more computing
resources than two equation-based models and are not computationally robust.
−
SSG-RSM (Speziale et al., 1991) may be more preferable than LRR-RSM (Launder
et al., 1975) because the SSG-RSM is more accurate than the LRR-RSM for most flows
including swirl flows (Speziale et al., 1991; Lu and Semia˜o, 2003). Furthermore, use of
an elliptic blending RSM (EB-RSM) can be considered for a better prediction of the
inhomogeneous near-solid fluid behaviors (Benhamadouche et al., 2015).
−
In addition, ω-based RSM (e.g., BSL RSM) can be considered because ω-based model
sometimes showed better results than ε-based RSM for flow separation (ANSYS, 2010).
−
It should also be noted that although RSMs (especially, SSG-RSM) were more successful
than EVMs for confined swirl flows in pipe, e.g., Mimouni et al. (2008), it does not
necessarily guarantee their success in typical split-type MVG rod bundle problems. This
is because the former problem (Mimouni et al., 2008) is swirl decay in confined circular
pipe wall and the swirl is generated by swirl-type vanes without asymmetrical upstream
structures, while the latter is unconfined swirl decay within partially concave wall with
neighboring cross-flows and with asymmetric structures just upstream of the vane,
where other physics may be dominant.

##### Unsteady turbulence models

Transferring from steady RANS models to higher level unsteady turbulence models
leads to an enormous increase in computational resources. Applying directly the
unsteady turbulence models to actual full-scale problems seems practically infeasible.
Note that most of the previous problems used in the validation of higher level
turbulence models had one-order lower Reynolds number than typical PWR one.
Therefore, we need enough considerations about steady RANS turbulence models
before transferring to higher level turbulence models. On the other hand, in parallel
with a deeper study on the steady RANS closure models, considering higher level
unsteady turbulence models seems still necessary. This is because (i) they can provide
better understanding of the complex rod bundle flow physics that may include strong
unsteady effects that cannot be captured by steady RANS approach; and (ii) once
higher-level turbulence models, such as LES, turned out to be accurate, it may be
possible to calculate turbulence budget to calibrate the RANS closure models for this
specific problem.
Relating to this benchmarking study, consideration of unsteady turbulence models
seems necessary for some unresolved issues in a 5≡5 MVG rod bundle with a typical
split-type vane pair arrangement. Specifically, we need to focus on the followings
when using unsteady turbulence models:

<!-- page 773 (PDF 45) -->
l
Whether they can increase the turbulence fluctuations, especially at the intermediate and far
wake regions of the split-type MVG;
l
Whether they can capture the qualitative cross-flow pattern change (or circumferential
distribution pattern of the rod inner surface temperature) around the central rod;
l
Whether they can reduce the amplitude of the circumferential rod inner-surface temperature
distribution possibly by capturing the large-scale, unsteady cross-flow effect;
l
Whether they can improve the prediction of the second peaks along the dimple line at the
near wake.
However, from the previous studies (e.g., OECD-KAERI CFD benchmark), not all
unsteady turbulence models showed good accuracy. Most unsteady RANS turbulence
models were not so successful. Even LES showed large differences between calculations
, and some LES results were worse than those from URANS or hybrid
RANS-LES methods. It should be, however, pointed out that the OECD-KAERI
benchmark (Smith et al., 2013) adopted different geometries from this benchmark.
Especially different upstream structures (cylindrical button shape) are expected to
generate the large-scale vortex shedding just upstream of the vane; thus, just downstream
of the vane, low-level turbulence models, i.e., steady RANS models that could
not capture such vortex shedding at all and some unsteady models that could not capture
it in a right way showed larger variations than the measured mean axial velocity
profile. On the other hand, the MVG with conventional spring and dimples, like MVG
adopted in this benchmark, may not have such a large-scale unsteady flow structures
just upstream of vane. Actually, z-zMVG=25 mm (2.1Dh,SC), steady RANS results
showed quite similar level of variations with the measured mean axial velocity profile
although some peaks were missed. Thus, in this benchmark exercise, we may obtain
an unsteady trend different from the OECD-KAERI CFD benchmark.

##### Conjugate heat transfer

It was evident that conjugate heat transfer (CHT) calculation produced more physical
outer-surface heat flux in the benchmark. However, direct quantitative comparison
with CHT and without CHT (i.e., with uniform outer-surface heat flux) with other
conditions the same was not performed in the benchmark, which may be needed in
the future work.

##### Near-wall treatment

Assessment of the near-wall treatment was limited in this benchmark. It was only
found that wall function approach could be a reasonable option. However, the wall
function approach may not be suitable for the strong flow separation and impingement
of cross-flow prediction; thus, the possibility of the enhancement by use of the low
Reynolds number model can be considered.

##### Others

The effects of temperature-related factors, such as effects of a turbulent Prandtl number
, gradient methods, like simple gradient diffusion hypothesis, SGDH, and general
gradient diffusion hypothesis, GGDH, for RSMs, buoyancy, and thermal properties,
may lead to slight quantitative difference, which was included in Phase 1 (EPRI, 2014)

<!-- page 774 (PDF 46) -->
and Phase 2 (EPRI, 2015) reports under the hexahedral mesh, but not with other types
of mesh. Thus, we need detailed sensitivity studies for these factors under mesh with a
better quality in the future.

#### 12.8.1.3 Concluding remarks

Several advantages of the NESTOR experiment and the round robin benchmark
enabled us to find the capabilities of the steady RANS approach for full axial,
5≡5 rod bundle with typical split-type MVGs by comparing several isothermal
and thermal variables. An important insight about capabilities of the steady RANS
approach was that appropriate steady RANS calculations with wall function could
reasonably predict two key variables in the PWR fuel rod bundle with split-type
mixing vane grids—the grid span pressure loss and rod (inner-)surface temperature
distributions. Here, the appropriate steady RANS approach means that (i) fluid and
solid region meshes are appropriate (i.e., the mesh is fully resolved and suitable for
the near-wall treatment, and the mesh type is appropriate for the complex geometry
of the grid), (ii) conjugate heat transfer is considered. Also, the “reasonable” prediction
specifically means that (i) the pressure loss errors for SSG and MVG spans are
within about 5% and about 10%, respectively; and that (ii) the circumferentially averaged
rod inner-surface temperature discrepancies with elevation for different rods are
within [·2 K, 3 K], and the RMS errors around the circumference (with elevation for
different rods) are within the range 2–4 K.
However, the steady RANS approach could not capture well the corner subchannel
center fluid temperatures at the end of heated length and central rod circumferential
temperature distribution patterns in the far wake probably because of not capturing the
qualitative cross-flow pattern change due to the laterally confined test section, and
showed quite large local maximum rod inner-surface temperature errors (ranging
4–9 K with elevation) probably because of unsteady, large-scale cross-flow fluctuation
effect.
Thus, if the purpose of simulation is to obtain the global (axial and radial) distributions
of the rod surface temperature in the core, appropriate steady RANS calculations
can achieve the purpose quite satisfactorily. However, if the purpose of
simulation is to obtain the accurate circumferential and axial distributions of the
surface temperatures for each rod, as required in the level IV in-core crudding risk
assessment (EPRI, 2014), the limitations mentioned above need to be resolved.
Furthermore, we discussed the limitations of the current experiment methods as
well as the CFD methods and provided the recommendations for the future research
of typical split-type MVG rod bundle. Especially, for the experiment to reflect right
physics and to achieve right CFD validation the effect of test section sidewall (and
related inward-peripheral vanes) should be considered more carefully; and a longer
MVG span without SSG needs to be considered. For CFD methods, in parallel with
higher-level unsteady turbulence models (e.g., hybrid RANS-LES and LES) relating
to vane-upstream structure effects, large-scale unsteady fluctuations of the cross-flow
across the rod bundle, and possibly qualitative cross-flow change, more systematic

<!-- page 775 (PDF 47) -->
RANS turbulence models (e.g., cubic NLEVMs, EARSMs, and RSMs) relating to the
generated swirl decay and cross-flow interaction, were recommended.
Finally, it is worth noting that the round robin benchmark was suitable for identifying
the overall characteristics and effects of CFD methodological factors, but not for
accurate individual effect; thus, the detailed sensitivity study should be performed.

### 12.8.2 Example of nontraditional approach: LBM and IBM applications

Immersed boundary methods (IBM) and lattice Boltzmann methods (LBM) may be
seen as nontraditional approaches in CFD applications (although the tradition of
CFD application is not “so long”).
In particular, in recent years, the lattice Boltzmann method has been widely applied
to numerous fluid dynamics and heat transfer problems as an alternative to conventional
CFD methods based on the Navier-Stokes equation. This is because the LBM has advantages
over the conventional methods, such as simplicity in implementation due to its
simple algorithm and effective parallelization (with the domain decomposition) due
to its locality. Following this trend, the LBM has started to be applied to various nuclear
thermal hydraulics problems. In their work, see e.g., Fig. 12.13, Li et al. (2016), present
some basic LBM applications to nuclear-related problems and provide some insights
and notes.
Key items for LBM (and IBM) applications can be summarized as follows:
l
Complex geometry problems.Turbulentflowsinnuclearreactor geometriescanbeconsidered
for LBM (and IBM) application as an alternative or a support to Large Eddy simulation (LES).
l
Moving boundary problems. Fluid-structure interaction problems and particle-fluid interaction
problems are within the principle capabilities of Immersed Boundary Method (IBM).
The same can be repeated for two-phase flow with phase-field flow regimes.
l
Future. Various potential applications of the Lattice Boltzmann Method to nuclear thermal
fluids problems can be envisaged.

### 12.8.3 Overall data evaluation

An overall view of experiments and CFD applications to experiments brings the
following synthesis.
l
Synergy of efforts. The progress in the development and the capabilities of CFD methods can
be largely enhanced if an “open system” is adopted: this implies cooperation among
developers of CFD methods and models as well as cooperation between experimentalists,
developers, and analysts (i.e., those who apply the code), as well as experts in NRS and
licensing of NPP. The cooperation should be solid, i.e., not only in format but also in content.
Namely accessibility to valued codes, models, and data should be guaranteed to the overall
community of experts and an alive system should be created and operated.
l
Trade-offs in CFD NTF applications. The following aspects are relevant in CFD applications
to experiments: (1) Accuracy vs. Efficiency: acceptable calculation accuracy and efficiency
(i.e., computational resources) are needed; this implies the definition of target accuracy; (2)
Experiment vs. Numerical analysis: qualified CFD tools may substitute experiments in some

<!-- page 776 (PDF 48) -->
cases; however, experiments are indispensable for progressing the knowledge; (3) CFD code
vs. System code: synergic use of CFD and SYS TH codes appears the best choice consistent
with the current state of the art; (4) Partial application vs. Entire application: this is related to
CFD simulation of NPP; present CFD capabilities do not allow an “Entire” application; (5)
Using results vs. Using methods: using results without knowing the method should be
discouraged; method capabilities and limitations must be associated with the use of result;
Fig. 12.13 Applications of lattice Boltzmann method: (A) flow in a rod bundle (with LES),
(B) flow across a tube bundle (with LES), (C) flow in a pebble bed (with LES), (D) flow-induced
vibration (with IBM), (E) particle sedimentation (with IBM), (F) bubble rising (with phase-field
model), and (G) particulated flows (with IBM) (Li et al., 2016).
