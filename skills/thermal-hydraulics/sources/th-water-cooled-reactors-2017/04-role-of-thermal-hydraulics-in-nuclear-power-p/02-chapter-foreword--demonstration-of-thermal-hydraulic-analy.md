# Chapter foreword — Demonstration of thermal-hydraulic analysis tool adequacy
<!-- source PDF pages 6-22 -->

<!-- page 148 (PDF 6) -->
exposure criteria for offsite individuals in the event of an arbitrarily-large release of
radioactive material from the reactor coolant system into the reactor containment.
The complete operational and accident domain of a nuclear plant, which makes up
the plant’s design basis, may be represented by the yellow region in the Venn diagram
shown in Fig. 4.2. The owner of a nuclear plant will only qualify for an operating
license if all of the operational conditions, infrequent events/transients, and design
basis events/accidents are shown to result in conditions which do not violate national
standards, laws, and operating requirements—such as, for example, 10 CFR 50 for the
United States.
The design basis includes accident prevention and accident mitigation requirements
for each NPP, for a defined scope of events. The requirements for all events
within the design basis are that the fission process can be shut down, the reactor
remains subcritical, the core can be cooled and its geometry maintained, coolant
makeup can be supplied as needed, and, in the event of an accident involving core
damage, any fission products released from the core can be controlled within a containment
structure that assures limited radioactivity leakage to the environment. Information
contained within the design basis for a particular piece of equipment or
building includes, for example, the specific functions to be performed and the specific
values or ranges of values for conditions that serve as the bounds for its design. These
conditions are derived from engineering analysis or experiments to predict the consequences
of events postulated for design, including those in the preceding list. An
important lesson learned from decades of operating NPPs is that rigorous configuration
control must be applied, throughout a plant’s operating life, to assure that the
design basis is maintained.
A plant designer and a plant operator demonstrate that their nuclear reactor system
does not violate national laws and national nuclear plant operational requirements and
standards by using thermal-hydraulic analysis tools, that is, numeric models, which
have been shown to be adequate for performing trustworthy predictions of the behavior
of the nuclear plant for all the scenarios, conditions, and transients within the
design envelope. The thermal-hydraulic tools themselves must be capable of calculating
trustworthy analyses for a domain which either equals or exceeds the design envelope
. The domain for which the thermal-hydraulic analyses may be used comprises the
“calculational envelope” as shown in Fig. 4.1.

## 4.3 Demonstration of thermal-hydraulic analysis tool adequacy

The process of qualifying software, for example, system analysis codes, such that the
software is considered adequate for calculating the behavior of NPPs, is in concept
relatively straightforward, even though there are many questions to be answered
and the process itself is iterative. From a high-level perspective, the process consists
of five stages (see Fig. 4.2) which must be exercised in their entirety for each NPP
design. The five stages consist of the (1) identification of the scenarios of importance,

<!-- page 149 (PDF 7) -->
Design envelope
Calculational envelope
Calculational envelope
Design envelope
Fig. 4.1 Venn diagram showing relationship between the NPP system envelope and the
thermal-hydraulic analysis calculational envelope (Venn, 1880, 1881).
No
Yes
Yes
5. Adequacy evaluation: The results of the V&V process
are evaluated using key metrics and conclusions formulated
4. Development: If
important phenomena
cannot be calculated
by analysis tools, then
further development is
undertaken
3. Verification & validation: Analysis tools are evaluated to
determine whether important phenomena can be calculated
2. PIRT: Important phenomena are identified for each
scenario (phenomena identification and ranking tables)
1. Scenario identification: Operational and accident
scenarios that require analysis are identified
Fig. 4.2 PIRT informed R&D process.

<!-- page 150 (PDF 8) -->
(2) identification of the key phenomena for the scenarios of importance using a phenomena
identification and ranking table (PIRT) process, (3) verification and validation
(V&V) of the analysis tools/software, that is, determination of whether the tools to
be used to analyze the scenario progressions are capable of calculating the important
phenomena and figures-of-merit for the validation matrix, (4) correction or enhancement
of existing software or possibly development of new software if necessary, and
finally, (5) an adequacy evaluation. The function of the final stage, the adequacy evaluation
, is to bring together all of the data—both experimental and calculational—
obtained in the earlier steps—to enable a thorough review and conclusions to be
formulated regarding whether the software is capable of making trustworthy predictions
of the nuclear system behavior for the scenarios of interest. Therefore, software
deemed adequate to calculate a particular plant scenario is capable of calculating the
dominant phenomena and physics, with an acceptable calculational uncertainty that
governs the behavior of the plant during the scenario in question.
Each of these stages consists of a number of important substages which will be
discussed individually in the subsequent sections. It is important to note: following
a positive outcome during the adequacy evaluation, the stage is set for obtaining
uncertainty quantifications on the figures-of-merit required by the stakeholders—
either for licensing or design purposes.
Online NPPs can only operate within limits defined by the capability of the licensee
to demonstrate that the magnitude of all important figures-of-merit for plant safety
parameters will not exceed acceptable limits. Thus a sufficient margin must be
maintained so these figure-of-merits are not in danger of being violated. A figure-ofmerit
is a key parameter indicative of whether or not a safety limit or an equipment
failure limit is in danger of being violated. For example, important figures-of-merit are
fuel temperature, the quantity of water inventory in a light water reactor pressure vessel
, and/or reactor vessel wall temperature. Although there are a number of figures-ofmerit
crucial to the operation of a power plant, for the sake of demonstrating the role of
thermal-hydraulic tools/software, the fuel cladding temperature is perhaps the most
common, particularly when considering safety limits during loss-of-coolant accidents
(LOCAs) for online light water reactors.
Regardless of the figure-of-merit under consideration, each has the potential to
affect the operational envelope of the plant in some way such that limits may be
imposed resulting in special precautions, operational procedures, or equipment limitations
to ensure the figure-of-merit is not challenged. In some cases, the limits
translate to operating the plant at power levels below the designed power level.
In other cases, the limits may translate to reducing the rate-of-change of an operational
parameter in going from one condition to another, thus increasing the
operational transit time. In any case, limits usually are accompanied with an economic
penalty.

### 4.3.1 Software adequacy: A more detailed look at the process

To ensure that plant designer analyses adequately cover the operational and accident
domain of concern, a number of methodologies have been developed. In the United
States the NRC issued Regulatory Guide 1.203 which describes historically

<!-- page 151 (PDF 9) -->
acceptable processes for the development and assessment of numeric models used to
evaluate transient and accident behaviors that are within the design basis of a NPP.
The process is known as the “Evaluation Model Development and Application
Process” (EMDAP—see Fig. 4.3).
The term “evaluation model (EM)” is commonly used in the licensing arena to
include all the numerical models used to calculate the nuclear system behavior,
including system analysis and CFD software. The NRC EMDAP flow chart consists
of four major elements followed by a final “Adequacy Decision” step.
Establish requirements for evaluation model capability
1. Specify analysis purpose, transient class and power plant class
2. Specify figures of merit
3. Identify systems, components, phases, geometries, fields, and
processes that should be modeled
4. Identify and rank phenomena and processes
Element 1
Develop assessment base
5. Specify objectives for assessment base
6. Perform scaling analysis and identify
similarity criteria
Element 2
7. Identify existing data and/or perform
IETs and SETs to complete data/base
8. Evaluate effects of IET distortions and
SET scaleup capability
9. Determine experimental uncertainties
NO
YES
Adequacy Decision
Return to appropriate
elements, make and
assess corrections
Perform plant
event analyses
Does code meet
adequacy standard?
Develop evaluation model
Element 3
10. Establish EM development plan
11. Establish EM structure
12. Develop or incorporate closure
models
Assess evaluation model adequacy
Closure Relations (Bottom-up)
13. Determine model pedigree and applicability
to simulate physical processes
Element 4
14. Prepare input and perform calculations
to assess model fidelity and/or accuracy
15. Assess scalability of models
Integrated EM (Top-down)
16. Determine capability of field equations and
numeric solutions to represent processes
and phenomena
17. Determine applicability of EM to simulate
system components
18. Prepare input and perform calculations to
assess system interactions and global
capability
19. Assess scalability of integrated calculations
and data for distortions
20. Determine EM bases and uncertainties
Fig. 4.3 Elements of evaluation model development and application process.

<!-- page 152 (PDF 10) -->
#### 4.3.1.1 Element 1

Element 1 establishes the plant scenario types and phenomena ranges that define the
operational and accident envelopes for the plant of interest. It is common practice to
combine these two envelopes to form a single operational/accident envelope for the
system which may be represented by validation matrices specific to each scenario
type. In the subsequent discussions this envelope will be called the design envelope
as shown in Fig. 4.1. The envelope for the system is the domain within which the
numeric models, which will be used to calculate the plant behavior, must be shown
to be applicable and must be shown to be capable of calculating the key phenomena
and figures-of-merit with an acceptable calculational uncertainty. Once the domain
for adequacy evaluation is defined, then each scenario must then be dissected to isolate
the regions where there are different controlling phenomena. Perhaps the most
widely known example of a scenario being divided into regions where there are different
controlling phenomena is the division of the light water reactor double-ended
guillotine break, also known as the large break loss-of-coolant accident (LBLOCA)
scenario, into the blowdown, refill, and reflood regions (USNRC, 1988). For each
of these regions different phenomena dictate the scenario progression—and the dominant
phenomena together with less important phenomena which must still be considered
are identified using a PIRT. The PIRT is an important ingredient to the adequacy
evaluation because the identification of key phenomena points to the physics which
must be adequately represented numerically in each region (Wilson and Boyak, 1998).

#### 4.3.1.2 Element 2

Element 2 is focused on developing the “assessment base” which is equivalent to
developing the validation matrices used as the validation calculation benchmarks.
The validation matrices are comprised of the data from experiments that have a rigorous
, scaled relationship to the prototype as well as known measurement uncertainties
which are sufficiently low to enable high-fidelity validation calculations to
be performed.
The set of experiments designed to generate validation data is based on nuclear
reactor operational and accident envelopes. The envelopes, in turn, are composed
of the various scenarios which may occur. For example, the operational envelope
may be composed of a set of scenarios which include plant operation at various power
levels—such as scenarios A–E shown in Fig. 4.4. The system of equations which
describes the plant operational conditions for any region within a given scenario
(e.g., the blue region within the scenario A domain) will change when a phenomenon
or phenomena, which has negligible influence in the blue region, becomes influential,
for example, the presence of subcooled boiling within the core denoted by the gold
region within the scenario A domain. The boundary between the blue and gold regions
denotes the change in the systems of equations which govern the thermal-hydraulic
behavior in the two regions respectively.
Such boundaries may signify changes to the systems of equations which, although
significant enough to change the trajectory of the scenario progression, will not lead to

<!-- page 153 (PDF 11) -->
a reduction in the plant safety margin. Conversely, some boundaries represent the
crossover to a region where a “cliff-edge” effect may occur, for example, critical heat
flux in the core, which if encountered will lead to significant temperature increases in
the core fuel rods.
This concept is important from several perspectives: (a) an important role of
thermal-hydraulics analysis is to define the boundaries which separate the various
regions within scenarios which reflect important changes in key characteristics of
the governing equations2 and (b) scaled experiments designed to generate validation
data focus on characterizing the fluid/heat transfer behavior within each region as well
as defining the boundaries between regions.
If the validation matrix used to qualify the numeric models is rigorously defined,
the experiments properly scaled such that experimental distortions are both minimized
and quantified, and the data have sufficiently low uncertainties, then the groundwork
for completing the Element 4 numeric model validation and numeric models adequacy
assessment is in place.
The design envelope for any nuclear plant is the domain of conditions and phenomena
which the numeric models must be capable of calculating (see Figs. 4.1 and 4.5).
The definition of the design envelope is addressed in Element 1 of the EMDAP. The
region where the numeric models are valid, as confirmed by performing validation studies
, is the calculational envelope and is the domain where the numeric models are shown
to have the desired calculational fidelity. The numeric models calculational envelope
must encompass the design envelope, as shown in Fig. 4.5, if the numeric models
are to be used to calculate the projected behavior of the system for licensing studies.
Fig. 4.4 Plant operating envelope (irregular curve) overlaid by plant operational scenarios.
Regions within each scenario, denoted by different colors, denote domains a specific system of
equations is applicable.
2Such changes may occur when the fluid behavior moves into the region of applicability of various
correlations.

<!-- page 154 (PDF 12) -->
The range of applicability for a given set of numeric models (the software) is in part
determined by the physics and the numeric models contained within the software
developed in Element 3. Therefore, the assessment or validation process, as
implemented in Element 4, and the decision regarding the adequacy of the numerical
models, must confirm that the software physics models properly calculate the key phenomena
over the entire range of conditions encompassed by the calculation envelope.
Success is only achieved when an adequate, high-fidelity data matrix and/or exact analytical
solution set are available to benchmark the calculation results over the range of
conditions that encompass the entire design envelope.
The data included in the validation matrix are indicated in Fig. 4.5 by − where the +
indicates the data coordinates and the circle around the + indicates the data uncertainty
. An important point to be addressed is the applicability of the individual data
points, and the validations that are performed on the basis of the selected data, to the
region between the data points. The “region of applicability” for a particular data point
within the validation matrix is indicated by the subdomain defined by the dotted line
that surrounds an individual data point (see Fig. 4.5).
The validation matrix is constructed using specially designed experiments which
are linked to the prototype by the scaling laws. Historically experiments such as
LOFT, BETHSY, and ROSA were scaled using power-to-volume scaling with
accommodations to achieve density-gradient scaling important for small break
LOCA-related phenomena by using 1:1 height scaling (Ybarrondo et al., 1974;
Levy, 1999). Over the last 20 years more advanced scaling techniques have been
utilized including hierarchical two-tiered scaling as first proposed by Zuber (1991).
Using the scaling laws in an acceptable fashion, such as outlined in Zuber (1991), is
crucial because when the numerical models are validated using data from correctly
scaled facilities, as noted in Zuber et al. (1990): “Implicit to applications of computer
codes to analyses of postulated accident events in nuclear plants is the premise that
Region of applicability
⊕
⊕
⊕
⊕
⊕
System
envelope
Calculational
envelope
System
envelope
Calculational
envelope
Fig. 4.5 Relationship of validation
data to calculational and system
envelopes.

<!-- page 155 (PDF 13) -->
these codes have the capability to scale-up phenomena and processes from test
facilities to full-scale plant conditions.”
These scaling methods typically include a combination of top-down and bottom-up
scaling analyses. The top-down scaling approach is most applicable to the validation
of system analysis codes and is usually performed for scaled integral experiments
designed to simulate the integral behavior of the complete prototype plant. These
scaled integral experimental facilities include simulation of most of the major components
. On the other hand, the bottom-up scaling approach is useful not only for system
analysis software, but especially the validation of CFD software used to evaluate
localized phenomena. The bottom-up scaling approach typically looks at phenomena
occurring in individual components (local heat transfer, countercurrent flow, etc.) to
confirm that scaling distortion do not occur at the local level or to quantify whatever
distortion is present.
In the top-down scaling approach, the system to be addressed is defined, and the
transient scenarios within the operational and accident domain are divided into several
phases, and subphases if necessary. The system responses of interest in each phase are
represented by the governing conservation equations that determine the behavior of
the systems and/or components. These equations are then nondimensionalized and
the nondimensional groups evaluated to determine the relative importance of each
group. A set of nondimensionalized coefficients characterizing the system response,
are then defined. The nondimensional groups from the calculated response of the prototype
plant can then be compared with the measured data from the experimental facilities
to quantitatively evaluate the scalability of the test facilities to the prototype plant
for the parameters and scenarios of interest.
As indicated earlier, the bottom-up scaling approach is primarily concerned with
localized phenomena, so it is primarily used to assess the applicability of individual
models and correlations implemented into the system analysis and/or CFD software.
This approach addresses the details lost in the averaging at the component level in the
top-down scaling, thereby providing insights into qualitatively different responses
between the test facility and plant. The bottom-up scaling approach is also useful
in understanding apparent distortions between the test facility and plant that are
observed but not easily explained by the nondimensional groups obtained from the
top-down scaling approach. Identification and quantification of the distortions inherent
to the experimental facility design and conditions are a key element of the process.
This activity is identified as item 8 of the EMDAP Element 2 (see Fig. 4.1).
The data need for software validation depends on the particular software being considered
. The system analyses software are used to analyze the overall behavior of the
prototype reactor or experimental facility for selected scenarios in the operational or
accident domain, while the CFD software are used to study more detailed flow behavior
and the potential for hot spots and/or unacceptably large thermal gradients in localized
areas of the reactor system. Depending on the particular application, the system
analysis and CFD software may be used separately or coupled together to perform the
analyses.
When new experimental facilities are required the design of these new facilities
must be rigorous to ensure compliance with NRC requirements for licensing a new

<!-- page 156 (PDF 14) -->
reactor plant, particularly an advanced reactor design with a limited history of regulatory
review. Important features to be considered in the experiment design include:
(1) assurance that the proposed experiment facility captures key phenomena being
investigated; (2) the experiment is scaled to provide a direct link between the scaled
facility and prototype plant; (3) the inherent distortions of the scaled experiments are
identified and quantified; (4) adequate high-quality measurements are available to
ensure that experimental data uncertainties are quantifiable and acceptable low;
and (5) experiment results can be decomposed to the lowest level modeled by the
software to ensure that system behavior at the component level is properly being
calculated by the governing software physics.
All the data from the experimental facilities, taken together, form a data matrix.
The data used in the validation of the numeric models form the validation matrix. Ideally
the validation matrix data are defined in a sufficiently ordered manner—for example
, as depicted in Fig. 4.6—such that the datasets are spaced at intervals sufficiently
small that all of the system envelope domain is covered by either the data points or the
combined subdomains of the individual data points as defined by the regions of
applicability as shown in Fig. 4.5.
In general the data comprising the validation matrix may include NPP, integral
facility, separate effects, and basic (sometimes called fundamental) experimental data.
The relationship between these types of data is shown in a “validation pyramid” as
illustrated in Fig. 4.7. The experiments performed to investigate and characterize
the behavior of individual phenomenon are basic experiments and the data obtained
from these experiments form the foundation of the validation pyramid. Also forming
the foundation of the pyramid are analytical solutions of the phenomena.
Separate-effects experiments are designed to investigate and characterize the behavior
of individual or a limited number of phenomena in a well-defined flow geometry, for
example, turbulent flow in an inlet plenum. The separate-effects data obtained from
such experiments form the next tier. The upper tiers of the validation pyramid are
⊕
⊕
⊕
⊕
⊕
⊕
⊕
⊕
⊕
⊕
⊕
⊕
⊕
⊕
⊕
⊕
⊕
⊕
⊕
⊕
⊕
⊕
⊕
⊕
⊕
⊕
⊕
⊕
⊕
⊕
⊕
⊕
⊕
⊕
⊕
⊕
⊕
⊕
⊕
⊕
⊕
⊕
⊕
⊕
⊕
⊕
System
envelope
Calculational
envelope
Fig. 4.6 Ideal coverage of the
system envelope using an ordered
validation matrix approach.

<!-- page 157 (PDF 15) -->
composed of the data obtained from integral-effects experiments and operational
plants. The overall sum of the data forms the individual elements of the validation
matrices.
In principle, each of the experiments designs is related directly to the system envelope
of the prototype for the key phenomena or figures-of-merit. Thus the ranges of the
data measured in the experiments are quite important. The experimental data range
of interest for the subject phenomena should be comparable to that of the prototype.
An example comparison done for a very high temperature gas-cooled reactor
separate-effects experiment is shown in Fig. 4.8 for Reynolds number (Re) and density
Fig. 4.7 The concept of a validation pyramid.
Fig. 4.8 Comparison of scaled experimental and prototype envelopes for key phenomena in a
design basis scenario.

<!-- page 158 (PDF 16) -->
ratio for density-gradient driven countercurrent stratified air-helium flow where the
system envelope for a gas-turbine modular high temperature reactor (GT-MHR) is
compared to the experimental envelope.
The experimental data quality must satisfy the requirements of Appendix B of Title
10 of the Code of Federal Regulations Part 50.46 and the ASME NQA-1 standard—in
the United States—and comparable quality standards elsewhere internationally. To
achieve this goal, the data should be generated in conformance with the practices
and procedures described in the:
i. International Organization for Standardization (ISO) guide to the expression of uncertainty
in measurement (GUM)
ii. ASME PTC 19.1-2005: Test Uncertainty standard.

#### 4.3.1.3 Element 3

Element 3 activities are centered on the creation of the numeric models that make up
the EM and thus are comprised of the physics and mathematical models, including the
mathematical approximations, for example, finite difference models, finite element
models, correlation approximations, etc. Many widely used numeric models describing
thermal-hydraulics phenomena are already available. Examples of commonly
used system analysis software include RELAP5, RETRAN, CATHARE, and TRACE.
Examples of commonly used CFD software include Fluent, STAR-CCM+, and CFX.
However, the existence of such software does not eliminate the need for both
verification and validation of the software.
Stemming from the presence of readily available software, such as the important
and commonly known examples given in the previous paragraph, verification of the
numeric models and developmental validation of the existing software packages presently
usually focuses on revisions and additions which are specific to advanced
nuclear plant designs which have design features that are not present in online nuclear
plants that were licensed and for which the above software have been found to be adequate
and thus have been used to perform nuclear plant behavioral calculations for
licensing submittals to the applicable regulatory agencies.

#### 4.3.1.4 Element 4

Element 4 encompasses the creation of the input for the numeric models and the initial
and boundary conditions for the numeric models. Subsequently the input models are
verified and finally, the validation calculations are performed as a part of the Element
4 activities. The degree to which the numeric model validation calculations compare
to the benchmark data is a primary ingredient in determining the adequacy of the
numeric models for calculating the behavior of the system within the design envelope.
At the conclusion of the Element 4 activities a decision regarding the adequacy
of the EM to calculate the scenarios, including consideration of the calculational
uncertainty, within the system envelope may be made. To summarize the Element
4 activities, the verification and validation processes are discussed.

<!-- page 159 (PDF 17) -->
##### Verification

Practices and procedures are divided into several categories to indicate the goal and
intent of each. These categories include code verification, code and calculation documentation
, reduction of numerical error, quantification of numerical uncertainty, and
calculation validation. Quantification of numerical uncertainty is discussed in some
detail in Johnson et al. (2006). Validation, including calculation validation, is discussed
in section “Validation.”
Code Verification: Code verification of system analysis codes is generally done via
traditional techniques centered on first performing detailed reviews of the coding by
parties which are independent of the code development group followed by a rigorous
quality assurance protocol designed to track the code results obtained using verification
benchmark problems with respect to known high-fidelity results.
Code verification of CFD codes involves the determination of coding correctness
(Roache, 1998) a process separate from calculation verification (the quantification of
numerical uncertainty). Users demand that the analysis software that will be applied to
reactor safety analyses will already have been subjected to a variety of code verification
tests. What will be required is documentation of these tests.
Only tests that exercise the options used in the particular computations need to be
documented. The tests as a suite must be designed to exercise all the terms in the
governing partial differential equations. For example, it is not adequate to only test
the code on linearly varying solutions such as planar Couette flow, since this solution
does not exercise vertical convection terms and others. The most complete and convincing
type of code verification test uses the method of manufactured solutions or
MMS (Roache, 1998) but this will not be required. If MMS is not used, it will probably
be necessary to use a suite of test problems to demonstrate code correctness. For all of
these problems, the observed rate of discretization error convergence should be documented
and compared to a theoretical value for the discretization algorithms
employed. If it is not, then more stringent requirements will be enforced during calculation
certification (Johnson et al., 2006). The code verification must also include
some data on the effect of iterative convergence criteria on numerical results (see
Chapters 11–13 for details).
Code and Calculation Documentation: Software that is used for nuclear reactor
safety analysis must be described in detail in code documentation. Such documentation
should include describing equations used and their discretization as well as
the basic methods used to obtain a solution. The truncation error and its formal
order or accuracy should be given. The code documentation must include all
details of implementation of the turbulence models used in calculations, for example
, turbulence models for CFD software. The code documentation should be
available for reference to reviewers who must review the associated calculational
results.
For each calculation performed and submitted as a safety analysis, assumptions
must be listed along with the details of the methods and models used. Other details,
including but not limited to boundary and initial conditions, model constants (parameters
), and other relevant information must also be provided. Options not used in the
calculation need not be documented.

<!-- page 160 (PDF 18) -->
Reduction of Numerical Error: The reduction of numerical error is clearly a
desirable objective for numerical calculations. Lessons have been learned about
what not to do when using computational techniques for numerical analysis. These
lessons-learned have been canonized in the requirements for manuscripts submitted
to well-known journals such as the ASME Journal of Fluids Engineering. It therefore
seems prudent to apply them to relevant software to reactor safety analysis.
Examples of such requirements are those given in the ASME Journal of Fluids
Engineering “Statement on Numerical Accuracy.” Details regarding the philosophy
and meaning of the various key points are discussed in Johnson et al. (2006). Examples
of the content include requirements that (a) methods must be at least
second-order accurate in space, (b) grid independence or convergence must be
established, and (c) in transient calculations phase error must be assessed and
minimized.
Grid independence is the process of refining the grid from the starting point until
numerical results stop changing or change by negligible amounts. Theoretically, the
results will continue to change until the grid spacing approaches zero. The precision of
the machine, however, will halt this process at a finite grid spacing. This is sometimes
referred to as achieving machine zero (of the residuals). Not only is the process of
obtaining grid independence important to reducing numerical errors, it is also a good
way to obtain estimates of numerical uncertainty (see “Quantification of Numerical
Uncertainty” in Johnson et al., 2006).
Iterative convergence relates to the number of iterations required to obtain residuals
that are sufficiently close to zero, either for a steady-state problem or for each
time step in an unsteady problem. This error is in addition to the numerical error associated
with the truncation error terms. Because of the well-known and unacceptable
sensitivity of some commercial codes to the iteration tolerance and the too lax default
tolerance, the final calculations must determine this effect. At least two levels of iteration
tolerance must be shown and the sensitivity presented. For example, if results for
a solution functional ƒ are presented using a default iteration tolerance of (say) 10·3
reduction in residual from the initial condition, as required in Freitas et al. (2003), then
another calculation with 10·4 will be required, and the sensitivity f10
0 will be stated as
the normalized % change in ƒ per decade of change in iteration tolerance—as given in
Eq. (4.1).
f 0
10 = Δf f 10·4
□
□
·f 10·3
□
□
□
□
=fnorm □100%
(4.1)
The normalization can be based on ƒnorm=ƒ(10·3) when divides by near zero are not a
problem, otherwise by another appropriate normalization. The final test of sufficient
tightness of the iterative tolerance will be the acceptability of the final results based on
estimation of numerical uncertainty and validation metrics.
For transient calculations, the same convergence criterion should apply as for spatial
convergence (grid independence). The time step should be refined until negligible
change is obtained. Also, though not required by the Journal of Fluids Engineering, it
is recommended that the time-wise discretization scheme should be second-order
accurate or better. While there are other practices to reduce numerical error, the above

<!-- page 161 (PDF 19) -->
will constitute the required practices for rector safety analysis at the present time.
Other practices that reduce numerical error are certainly allowed and even

##### encouraged. Validation

Whether or not software is adequate for performing best-estimate VHTR analyses is
determined using both “top-down” and “bottom-up” evaluations, as summarized in
Fig. 4.9 and described in this section.
“Bottom-Up” Code Adequacy: Bottom-up evaluation of code adequacy entails
examination of four features: the pedigree, applicability, fidelity, and scalability of
the code under consideration.
The pedigree of a systems code consists of its history, its development procedures,
and the basis for each correlation that is used in the code. Any correlations, data
sources, and approximations used in the code must be documented in textbooks, laboratory
reports, papers, etc. The uncertainty data used to bound the correlation(s),
data, and approximations such as instrumentation and data system uncertainties must
be included in the documentation. The basis for the uncertainties should be traceable
and reproducible. The assumptions and limitations of the models must be known and
documented.
The applicability of a systems code depends on the range of use of each of its correlations
, data, and approximations. Those ranges must be documented and
referenced. Finally, the range of applicability claimed in the code manual should
be consistent with the pedigree, or, if a greater range is claimed, the justification
for the increase in range must be reported.
The fidelity of a systems code means the degree to which the code’s predictions
agree with physical reality. High fidelity requires that the mathematical models
and correlations used in the code are not altered in an ad hoc manner from their documented
formulation. A code is validated when it is shown that the code’s predictions
of key parameters agree within allowable tolerances with experimental data. The validation
effort should be complete for all the key phenomena in the events of interest.
Finally, benchmarking studies may either supplement the validation effort or make up
the validation effort if appropriate standards are available, for example, comparisons
of code calculation with a closed form solution.
“Bottom-up” scaling stems from the need to:
l
Build experimental facilities that model the desired full-scale system.
l
Closely match the expected behavior of the most important transient phenomena in the
scenarios of interest.
l
Demonstrate the applicability of data from a scaled facility to a full-scale system and to
defend the use of data from a scaled facility in a code used to calculate the behavior of a
full-scale system.
l
Relate a calculation of a scaled facility to a calculation of a full-scale system.
Scalability studies are usually performed to scale key parameters for a portion of the
system behavior, not to correlate global system behavior. Therefore, scalability analyses
consist of four steps: (1) isolate the “first-order” phenomena, (2) characterize the

<!-- page 162 (PDF 20) -->
Scaling analysis
of collective
experimental data
base
Agreement with data:
-  Excellent
-  Reasonable
-  Minimal
-  Insufficient
Adequacy
decision
What is good
enough?
Are data
applicable?
Knowledge
of physics
What is known?
Phenomena
identification and
ranking tables
(PIRT)
What is
important?
Code validation
Full:
  Partial:
•  Closure relations
(Bottom-up)
- Pedigree
- Applicability
- Fidelity
- Scalability
•  Integrated code
(Top-down)
- Governing Eqs
- Numerics
- Applicability
- Scalability
Assess deficiency correction
Theory manual
Documentation
Developmental
assessment report:
fundamental and
separate effects tests
(SET) validation
Models  and  correlations
applicability
Theory manual
Numerics report
SET validations
Integral effects tests
(IET) validations
Correct
code
inadequacy
Significant
inadequacy?
Perform required
plant analyses
No
How well did code do?
Performance measurement
standards
Fig. 4.9 VHTR system design software—elements of adequacy evaluation and acceptance testing practices.

<!-- page 163 (PDF 21) -->
“first-order” phenomena, (3) convert the defining equations into nondimensional
form, and (4) adjust the experimental facility conditions to give equivalent behavior
with the full-scale system within the limitation of the facility (or nearly equivalent,
based on nondimensional numbers that follow from Step 3).
As implied in the earlier discussion, “bottom-up” code adequacy techniques focus
principally on closure relationships. Thus, the field equations used in the code must be
correctly formulated and programmed. In addition, the field equations must be
reviewed by the scientific community, and its agreement on the correct formulation
and insertion of the governing equations in the code must be obtained.
“Top-Down” Code Adequacy: The “top-down” approach for ensuring code adequacy
focuses on the capabilities and performance of the integrated code. The
top-down approach consists of four parts: numerics, fidelity, applicability, and
scalability.
Numerics. Evaluation of the numerical solution considers convergence, stability, and property
conservation.3 Again, agreement by the scientific community on acceptable convergence
, stability, and property conservation must be obtained.
Fidelity. The fidelity of the code is demonstrated by performing thorough code assessments
based on applicable integral-effects and separate-effects data. The data are part of an
agreed-upon code assessment matrix constructed based on the transients of importance
and the key phenomena for each phase of the transients.
Applicability. The code must be shown to be capable of modeling the key phenomena in the
system components and subsystems by conducting thorough validation studies. The key phenomena
are identified in the PIRT.
The method to determine whether the code is capable of modeling key phenomena is to
compare the calculation produced by the code to data that have known uncertainties. For
example, “excellent” agreement between the code calculation and data is achieved if the calculated
value is at all times within the data uncertainty band.
The degree of agreement between the code calculation and the data is generally divided
into four categories as given in Table 4.1. A more rigorous definition is given by Schultz
(1993). A code is considered adequate in applicability when it shows either excellent or reasonable
agreement with the highly ranked phenomena (sometimes identified as the dominant
phenomena) for a transient of interest. If the code gives minimal or unacceptable agreement,
additional work must be performed, which may range from additional code development to
additional analyses if needed to better understand the phenomena.
Scalability. Experimental scaling distortions are identified and isolated, for example, inappropriate
environmental heat losses that stem from the larger surface-to-volume ratios that
are inherent to scaled facilities. Finally, an effort to isolate all code scaling distortions is
performed through code assessment calculations. Scaling distortions may arise from an inappropriate
use of a correlation developed in a small-scale system when applied to a full-scale
system.
3Property conservation issues arise when two calculations of the same property are performed by a systems
code using two different algorithms or methods. This practice may follow in an effort to enhance the accuracy
of the code result. Because the two methods are likely to calculate slightly different values of the same
property such as pressure, property conservation must be considered.

<!-- page 164 (PDF 22) -->
### 4.3.2 Software tool selection and software development

When confronted with the need to calculate key phenomena for an advanced
nuclear plant, it is inevitable that analysts will be required to choose one software
tool over another. This will be particularly true of system analysis software and
CFD software. To assist the analyst in formally choosing software, a methodology
is given in Fig. 4.10 where a flow chart summarizes key factors and questions
such as:
l
Has the software ever been used to analyze the phenomena or scenario? By answering this
question the analyst may be introduced to references and other experts who have applied the
software to similar phenomena or scenarios. Hence a body of useful information may be
available.
l
Are the phenomena modeled properly? And does the model region of applicability correspond
to the system phenomena or scenario envelope? These questions may be most
easily answered by using the required manuals and documentation identified in Fig. 4.8,
for example, models and correlations, theory manual, scaling relationships and applications
, developmental assessment reports, validations.
l
Have validation studies been completed for the phenomena or scenario? Were the validation
results reasonable or excellent (as defined in Table 4.1)—or were the results minimal
or unacceptable? If a body of validation results are not available, or if the validation
results were not “reasonable” as a minimum, then either the software should not be used
or it should be validated to ensure that the calculated results are reliable rather than
misleading.
Only when acceptable answers are obtained for the questions listed earlier,
can the software under consideration be used for the required analysis with
confidence.
Table 4.1 Code adequacy identifiers
Classifier
Description
Excellent
The calculation lies within or near the data uncertainty band at all times
during phase of interest
Reasonable
The calculation sometimes lies within the data uncertainty band and shows
the same trends as the data. Code deficiencies are minor
Minimal
Significant code deficiencies exist. Some major trends and phenomena are
not predicted. Incorrect conclusions may be drawn based on the
calculation without benefit of data
Unacceptable
A significant difference between the calculation and the data is present—
and the difference is not understood. Such a difference could follow from
errors in either the calculation or the portrayal of the data—or an
inadequate code model of the phenomenon
