# Part 1. Computational fluid dynamics for nuclear thermal hydraulics: The current overview
<!-- source PDF pages 6-13 -->

<!-- page 734 (PDF 6) -->
Definitely, a work-in-progress chapter seems to reflect the CFD technology status
better than a synthesis of (nonexisting) consolidated achievements.
A hint for the reader: a look to the list of acronyms gives an idea of the multitarget
nature and complexity of CFD area.
Part 1. Computational fluid dynamics for nuclear
thermal hydraulics: The current overview

## 12.1 Introduction

In the nuclear field, views on the CFD are poles apart. Some think that the CFD is
promising and can play a key role in nuclear thermal fluid problems now and in
the near future, while others think that the CFD is not reliable compared to the experiment
and it will take a very long time until it plays a key role in this field. Anyway, it
is true that in recent years numerous applications of CFD have been actively
performed in the nuclear field. In this chapter, leaning to the first view, we address
what we have to keep in mind for the CFD to be a promising tool and to play an important
role in the nuclear thermal hydraulics.
There are numerous issues and questions relating to the use of CFD in the nuclear
thermal hydraulics. These can be categorized into application-related and validationrelated
ones, each of which can be classified into CFD and physics viewpoints.
In addition, the stance, i.e., CFD users, experimentalists, system code users, vendors,
utilities, regulators, etc., changes the emphasis on the questions/issues.
Traditionally, system codes (SYS TH codes, see e.g., Chapter 11) and subchannel
analysis codes have been successful to a degree for the nuclear safety analysis. However
, because their main role is to combine numerous empirical correlations based on
very simple governing equations to evaluate the synthetic effect, the expected level of
accuracy was relatively low. The validation is performed against global variables
(pressure, temperature, void fraction, liquid level, and so on; see Chapter 13) in a
relatively large control volume (components, subchannels, and so on). On the other
hand, in recent years, as the computing power increases, the CFD code has become
a viable tool to predict the more detailed thermal fluids behavior in the nuclear system
with a higher accuracy than system and subchannel codes.
However, because the nuclear system, in general, involves very complex phenomena
characterized as high turbulence and/or multiphase not only during transient
events and accidents but also in normal operating conditions, the models used in
the CFD code for the nuclear system problems still involve empirical closure models,
such as RANS equations with turbulence closure models for turbulence calculations
and two-fluid model equations with closure models for two-phase calculations, rather
than less-empirical models, such as wall-resolved LES/DNS turbulence models and
interfacial tracking models (ITMs), respectively, because of practical feasibility. Once
some assumptions and related modeling are involved in the CFD code, we need to

<!-- page 735 (PDF 7) -->
understand more about the phenomenon of our interest because the assumptions and
modeling have to have the capability of reflecting key phenomenon.
In this chapter, we provide a critical (as far as possible) overview for the CFD applications
in the nuclear thermal-hydraulic fields and some recommendations for
better use.

## 12.2 CFD analysis procedure

Now, we address a CFD analysis procedure, which can be generally applied to
validation and application (prediction). This is important to CFD analysts. Selected
steps are (Faragher, 2004):
l
Understand the problem and set the simulation strategy;
l
Generate the geometry and the mesh;
l
Set the boundary and the initial conditions;
l
Run the CFD solver;
l
Postprocess and interpret the results;
l
Refine the mesh;
l
Perform the sensitivity studies;
l
Document the analysis.

### 12.2.1 Understand the problem (phenomena) and set the simulation strategy

When applying the CFD to nuclear thermal-hydraulic problems, it is important to
understand the characteristics of the phenomenon. These may include physical
conditions, turbulence, flow separation, swirling, secondary flows, multiphase flows,
etc. Based on these, we set the simulation strategy by considering objectives of the
analysis, required level of accuracy (qualitative information/incremental quantities/
absolute quantities), geometry (simplification and/or omission) flow domain and
boundary
conditions,
turbulence
models
(steady/unsteady,
RANS/hybrid
RANS-LES, LES, closure models), solvers, heat transfer, heat conduction (conjugate
heat transfer/heat flux), memory and CPU resources, etc.

### 12.2.2 Generate the geometry and the mesh

In many nuclear thermal-hydraulic problems, we need to consider the geometrical
simplification. Unlike the system code where geometry-related information must
be supplied by code user in an averaged manner (see e.g., the local pressure drop coefficient
at any geometric discontinuity), the geometry is very important because it plays
a role in boundary condition in the CFD calculation.

<!-- page 736 (PDF 8) -->
The mesh is a key factor affecting the accuracy of the calculation results. However,
it has infinite degrees of freedom, thus representing quantitatively the geometry and
hard to directly compare with other mesh configurations.

### 12.2.3 Set the boundary and the initial conditions

Flow and thermal variables (and turbulent variables) should be specified on the boundaries
of the flow domain. Material properties should be specified for all solids and
fluids in the simulation.
If the CFD-level boundary and initial conditions are not given in validation
problem or if we have to impose the boundary and initial conditions in application
problems, it should be reasonable and its sensitivity should be examined afterward.

### 12.2.4 Postprocess and interpret the results

Because CFD has all the information in the computational domain, it is difficult to
determine what results should be extracted and visualized. If the calculation purpose
is validation, i.e., comparison with measured data, it may be clear. Otherwise, we need
to consider various ways to get more insights.

### 12.2.5 Refine the mesh (rerun) and perform a sensitivity analysis (rerun)

Refining mesh is usually prior to other sensitivity study. Depending on the mesh type,
this process may be easy or impossible. However, demonstrating the convergence of
results when mesh size is decreased must be considered an implicit requirement for
CFD code application in nuclear thermal hydraulics (e.g., something that cannot be
achieved by SYS TH codes). An important thing is what variable in what region needs
to be used to evaluate the mesh sensitivity.
The sensitivity of the computed results may be examined with respect to variables
such as flow conditions, initial and boundary conditions, mesh type, configuration and
density, turbulence models, and computer system. Practically, all of these cannot be
performed. The round robin benchmark exercise can support some of these; however,
it cannot cover this individual sensitivity studies.

### 12.2.6 Document the analysis

Documentation is very important because it is a tool to communicate with others. The
document should include not only the findings from the analysis but also each process
in detail so that other analysts can repeat it. To go further toward the problem-specific
best practice, this individual document is very important. Qualified analyses should
include results of sensitivity studies, possible demonstration of convergence of results
(when the mesh size is decreased), and quantification of expected uncertainty (UQ).

<!-- page 737 (PDF 9) -->
## 12.3 Methodological aspects—Physical models

In this section, we briefly explain CFD methodologies that can be used or considered
in the nuclear field. In fact, it is impossible to describe all aspects of CFD in this
chapter because there are numerous CFD methodologies depending on problems that
we want to deal with.

### 12.3.1 Single-phase modeling

In most problems in nuclear field flows are turbulent. To accurately simulate the
turbulent flows, the broad range of time and space scales should be suitably captured
or modeled. Considering the geometrical complexity (broad range of scales) and high
Re in typical nuclear thermal fluid problems, it is a key to adopt methodology with
efficiency (even practicality or possibility) as well as accuracy. The basic starting
point is steady RANS modeling, which solves the time-averaged Navier-Stokes equations
and the closure models for the turbulence stress resulting from the averaging
procedure. Numerous studies on the turbulence closure models have been performed
in various industrial problems for the last fifty years. What we need to have in mind
when applying the steady RANS turbulence models are:
(i) no unique turbulence closure model to be appropriate for different problems;
(ii) the steady RANS turbulence model is a steady model; thus, when large unsteady effect is
involved as a key phenomenon in a given problem, it is not expected to be successful to this
problem.
Once the problem involves locally, in critical regions, or globally unstable unsteady
turbulent phenomena, we need to consider unsteady turbulence models. However, it is
sometimes challenging to characterize any unsteady phenomenon. There are numerous
unsteady turbulence models, which can, however, be classified into unsteady
RANS, hybrid RANS-LES, LES, and DNS. These should be selected carefully
considering the main physics and efficiency.
Another important factor in the CFD turbulence simulation is near-wall treatment.
The wall function method is typically used because of its efficiency and reasonable
accuracy. Since each solver has slightly different enhanced near-wall treatment
method, users need to understand how it works before using it. In the near-wall treatment
, it is important to generate the near-wall mesh, so that the assumptions (basic
requirements) of the near-wall treatment adopted are satisfied, and then to evaluate
whether the assumptions are applicable to this problem.

### 12.3.2 Two-phase modeling

Once multiphase phenomena are involved in the problem of our interest, change of
governing equations may be needed. Depending on how to deal with interface, there
are various methodological changes. In multiphase modeling, there are large differences
depending on whether the interface is treated statistically or deterministically.
The statistical approach requires numerous modeling, while the deterministic

<!-- page 738 (PDF 10) -->
approach requires enormous CPU resources. We do not get into the details of respective
methods within the multiphase CFD in this chapter. Please refer to Chapters 5, 9,
and 11 for further details.

## 12.4 Characteristics of the CFD analysis

To successfully apply the CFD to nuclear thermal-hydraulic problems, we need to
understand the characteristics of the CFD analysis different from other numerical
and experimental analyses and then use the advantages fully.

### 12.4.1 Applications

The validated CFD-based numerical experiment can give us various insights because
we can use all variables overthe entireregion, which is different fromthe physicalexperiments
. Thus, we may need to spend more time on the development of how to use the
numerical experimental results fully using the benefit of the numerical experiment.
An ideal image of the CFD use may be that like a system code, the CFD simulates
flow and heat transfer phenomena (covering all transient and accident scenarios) in the
entire reactor coolant system of the reactor. However, this may not be attainable at least
within a few decades (50 years is a guess). In this sense, the CFD may not play a key
role in the applied nuclear thermal hydraulics field. However, CFD can do what
lumped codes cannot do and can do more specifically and efficiently what experiments
can do. In fact, various different aspects of CFD use in this field have been considered.
First, we can directly use the CFD-calculated data for the target analysis, for example
, production of the thermal-hydraulic data (pressure, temperature fluctuations) for
the structural analysis, production of rod surface temperature (heat transfer coefficient
) for the crud analysis tool. Next, we can use the data to determine the input
parameters for lumped volume codes (subchannel and system codes). For example,
we can use the CFD-calculated pressure drop data for the new design of the mixing
vane grids to impose the resistance coefficient in the subchannel or system codes. For
another example, we can adjust the loss coefficient based on the CFD-calculated
three-dimensional flow distribution. Also, we can use the CFD calculation results
to develop physical models needed in lumped volume codes. Some (CFD) research
groups started development or application of ITM to produce the correlations needed
in the lumped volume code. Also, CFD can provide insight for the new design of
components or new experimental designs. So, it can help people reduce the trial
and error in making the experimental apparatus. In addition, CFD can increase the
physical understandings of or help identify complex phenomena that cannot be imagined
by people’s insight. Also, CFD can be used to check the system code results especially
for the 3D flow distributions. For example, NRC adopted CFD to check the flow
distribution obtained by system codes for refueling storage tank problem (Boyd,
2016). Depending on the purpose, the level of accuracy can change.

<!-- page 739 (PDF 11) -->
### 12.4.2 Validations

The capabilities and the advantages of CFD over SYS TH codes addressed in the
previous section are only valid when the CFD method is validated for the test appropriately
mimicking a given problem. The validation process for the CFD is basically
similar to that of the system code (see e.g., Chapter 13); however, there are many more
difficulties in CFD validation (Smith et al., 2015). In the CFD-level benchmark experiment
, problem specification needs to be much more elaborate than the system code.
Initial and boundary conditions and geometrical information should be accurately
provided. For the data measurement, the data should cover not only target regions
and target variables but also supplementary variables and regions. However, in the
previous experience, it is not easy to identify the target regions and the target
variables. Also, physically important phenomena for nuclear thermal hydraulics are
not necessarily part of the capabilities of the CFD codes and methods. Thus, benchmark
experiments, which are supposed to address physically important phenomena
and the CFD calculations, should give rise to a feedback process, not to a serial
process. If any experiment is for the CFD benchmark the CFD needs to be involved
in its design process. Furthermore, phenomena identification and ranking table (PIRT,
e.g., see Chapter 13) for the system code is not suitable for the CFD code in most cases.
Although numerous experiments have been performed for the validation of the system
code (models), most of them are not suitable for the CFD validation. Thus, in many
cases, new experiment should be performed. CFD validation experiments and other
experiments (developing physical models, for the study of physical phenomena, for
the validation of system codes) are needed.
The CFD validation is not just comparing the CFD-calculated results with the
measured data for a given problem. For successful CFD validation, we need to
consider several things from experimental point of view, CFD point of view, and both
points of view. Here, we address some (selected) important things for each point of
view. From the experimental point of view, a general requirement for data accuracy
(with errors) should be satisfied. Beyond this, the specific problem-related issues
should be reflected well. Among these, at first, the benchmark experiment should
be representative of the prototype. This becomes problematic when the main discrepancies
between the CFD calculations and the experiment are due to the difference
between the experimental and the prototypic conditions (geometry and thermal fluid
conditions). Next, the measured variables in the experiment should reflect key
phenomenon and target variables at target range.
From the CFD calculation point of view, it is very important to follow the general
CFD best practice guidelines (BPG)—for mesh sensitivity, mesh quality, turbulence
models and near-wall treatment, numerical schemes, and so on—to reduce the user
errors and evaluate the selected CFD methods in a right way. Beyond this, we need
to use an advantage of the CFD—availability of all variables in the computational
domain—to understand the overall phenomenon made in the selected CFD world.
This will help both experimental design and interpretation of discrepancies between
the CFD results and measured data.

<!-- page 740 (PDF 12) -->
From both points of view, it should be stressed that the reliable and effective CFD
validation needs closer collaboration between experimentalists and CFD analysts.
Both ways from experiment to CFD and from CFD to experiment can greatly reduce
time and cost at the end. Each party needs to be willing to provide not only results
(data) but also the limitations (errors and uncertainty) and phenomenological insights
to another and try to understand the other party to achieve a common goal effectively.
On the other hand, several round robin benchmark exercises have been performed,
as discussed in Part 2 of this chapter. The round robin exercise has a great advantage
because various numerical methods (especially, various turbulence models, codes,
and mesh configurations) can be considered and compared for the same problem.
In fact, through the previous round robin benchmark exercise, some meaningful
conclusions could be derived (see Part 2 of this chapter). In several benchmark applications
where different CFD codes or procedures are involved, the ranking method
was adopted to evaluate and compare the results. It seems very objective; however,
it also has limitations. We need to consider qualitative analysis along with such
quantitative measures.
Some findings relevant to the application of CFD methods, models, and codes,
which are discussed in Part 2 of this chapter, are summarized below.

#### 12.4.2.1 Capabilities of steady RANS

The main insight from Phase 2 of EPRI round robin benchmark (EPRI, 2014, 2015)
was that appropriate steady RANS approaches with wall function could reasonably
predict two key variables in the PWR fuel rod bundle with split-type mixing vane
grids: the grid span pressure loss and rod surface temperature distributions. Here,
the appropriate steady RANS approach indicates that:
(i) fluid and solid region meshes are suitable for the complex geometry of the grid and
wall-function requirement;
(ii) conjugate heat transfer is considered;
(iii) the “reasonable” prediction specifically means that:
−
the pressure loss errors for SSG and MVG spans are within about 5% and about 10%,
respectively;
−
the circumferentially averaged rod inner-surface temperature errors with elevation for
different rods are within ·2 to 3 K and the RMS errors around the circumference (with
elevation for different rods) are within the range 2–4 K.
Overall, the CFD calculations under the trim mesh with extrusion layers consistently
showed good result. In addition, the effect of turbulence-anisotropy was relatively
reduced in the MVG wake region.

#### 12.4.2.2 Limitations of steady RANS

On the other hand, the steady RANS approaches showed limitations:
(i) they could not capture well central rod circumferential temperature distribution patterns in
the far wake probably because of the cross-flow reorientation (and dumping) due to the
interaction between asymmetric, cross-flows with test section wall;

<!-- page 741 (PDF 13) -->
(ii) they showed quite large local maximum rod inner-surface temperature error (ranging 4–9 K
with elevation, see Section 12.8.1 in the Part 2 of this chapter), probably because of
unsteady, large-scale cross-flow fluctuation effect. In addition, it should be pointed out
again that in the actual applications to PWR fuel rod bundles where the test section wall
is not present except near the core barrel, the unsteady, large-scale cross-flow fluctuation
effect on the circumferential temperature variation magnitude may be of greater importance
than the test section wall effect on the flow pattern changes.

#### 12.4.2.3 Final remarks from EPRI round robin

The steady RANS approaches showed reasonable capabilities in predicting the
circumferentially averaged rod surface temperature and the grid span pressure loss.
However, if the purpose of the simulation is to predict the local surface temperature
distribution in the far downstream (e.g., crud-induced localized corrosion), we may
need to adopt higher level unsteady turbulence models. Concurrently, we may need
to perform experiments with a larger lateral domain to see the test section wall effect
and with a longer axial domain (comparable to typical PWR span) to see decaying
patterns of the rod temperature distribution in the real target region.

## 12.5 Summary remarks

The CFD cannot play a system code-like role in the nuclear thermal-hydraulic analysis
in the near future. However, the CFD can contribute to the nuclear thermal-hydraulic
analysis in different ways from other numerical and experimental analyses. In this
context, the nuclear CFD analysts have tried to find the problems (physics) that
CFD models can simulate and have applied those models to various problems in
various aspects (e.g., Smith et al., 2015). In some problems, they successfully used
and have established some level of best practices.
Finally, to increase the contribution of the CFD to the nuclear thermal hydraulics
field, we need to keep in mind the following points:
l
We need to set timely goals–near-term, mid-term, and long-term goals. Depending on the
time-based goals, we can have totally different strategies.
l
We do not need to confine ourselves to accustomed methodologies just because new methodologies
need new strict validations.
l
We need more specific application examples and need to develop problem-specific BPG as
many as possible. As the number of BPG increases, the applications will accelerate.
l
We need to construct open systems where the communications, accumulations, and collaborations
can be actively performed. Their best form (web-based or hypertext) and contents
should be identified.
l
The CFD analyst need to fully understand the problem (physics), physical models, as well as
the numerical factors.
l
We need to develop efficient CFD assessment methods.
These cannot be done by one person or one group. Collaborations between CFD
analysts, with experimentalists, with system or subchannel code analysts are essential.
