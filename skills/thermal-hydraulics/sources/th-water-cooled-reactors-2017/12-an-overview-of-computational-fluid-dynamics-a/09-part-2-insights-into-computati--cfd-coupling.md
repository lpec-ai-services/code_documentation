# Part 2. Insights into computational fluid dynamics for nuclear power plant applications — CFD coupling … Conclusions and recommendations
<!-- source PDF pages 78-93 -->

<!-- page 806 (PDF 78) -->
## 12.10 CFD coupling

The following CFD couplings are considered below:
l
Coupling of CFD code with neutron physics codes
l
Coupling of CFD code with structural mechanics codes
l
Coupling CFD with System (SYS TH) codes: porous medium approach
Validation of CFD-type computer codes on separate-effect experiments is discussed
thoroughly in Mahaffy et al. (2007a,b) as already mentioned. The processes of validation
in the context of nuclear reactor simulations are, in majority of cases,
beyond the possibilities of present hardware capabilities if a CFD code is used
alone. Use of a less detailed, less demanding system analysis code to produce initial
and boundary conditions for the CFD code is a practical alternative. Such multiscale
coupling is indispensable in the case of demonstration simulations and, of course,
application of a CFD code to real industrial problems. Moreover, in such problems
it is very frequently necessary to simulate not only thermal hydraulics, but also phenomena
belonging to different fields of physics or even to chemistry. Furthermore,
in this type of multiphysics coupling, problems with different spatial and temporal
scales appear.
General methods of coupling are treated in several books and papers, e.g.,
Zienkiewicz (1984), Hackbush and Wittum (1995), Cadinu et al. (2007), and
Ibrahimbegovic and Markovic (2003). Most generally, couplings are distinguished
between those taking place on the same domain, by changing the differential equations
describing the corresponding physical phenomena (this approach is frequently realized
by means of a single computer code), or coupling on adjacent domains by
matching boundary conditions at their interfaces. In this case, either the models are
combined to produce a comprehensive model for the coupled problem (joint, or simultaneous
solution strategy), or there are modules solving the individual problems, and
Table 12.5 CPU time required by various
SGS models
Model
CPU time
No model
0.93
Smagorinsky
1.00
Dynamic eddy viscosity
1.07
Dynamic mixed
1.11
Lagrangian eddy viscosity
1.21
Lagrangian mixed (one coefficient)
1.28
Lagrangian mixed (two coefficients)
1.31
The CPU time is normalized by that of an LES that used the Smagorinsky
model (Piomelli, 1999).

<!-- page 807 (PDF 79) -->
coupling is effected via an outer iteration (changing of parameters, boundary conditions
, or geometries after each step or selected steps of the outer iteration—partitioned
solution strategy). Whenever an outer iteration is used, the problem of the optimum
level of explicitness of the coupling has to be faced, especially when two-way coupling
is required. Generally, explicit coupling is easy to program compared with
implicit coupling, but is more prone to numerical instabilities.
Independently of the details of the particular coupling strategy, validation and
assessment of the coupled code are required. The individual codes usually solve
problems with different spatial and timescales and, particularly if two-way coupling
is required, it is not enough to validate or assess the codes individually. Design of
corresponding experiments must take into account different requirements concerning
density of instrumentation (when multiscale coupling of codes is tested)
or requirements of different type of instrumentation (in the case of multiphysics
coupling).
There are several examples of coupled CFD or CFD-type codes with system codes,
as can be seen in the Table 12.6, reproduced from Cadinu et al. (2007).

## 12.11 CFD validation

An assessment matrix for a given application should comprise three groups of items
(OECD/NEA/CSNI/R(2014)3, 2014) (Section 6):
l
Verification problems with “highly accurate” CFD solutions;
l
Validation experiments and their CFD simulations;
l
Demonstration simulations, possibly with some suitable supporting experiments.
Table 12.6 Examples of CFD coupled codes (Cadinu et al., 2007)
Authors, source
System code
CFD code
Process
Jeong et al. (1997)
RELAP5
COBRA/TF
LOFT L2-3 LOCA
Experiment
Graf (1998)
ATHLET
FLUBOX
UPTF Experiment, Weiss
et al. (1986)
Kliem et al. (1999)
ATHLET
CFX
MSLB analysis
Aumiller et al.
(2001)
RELAP5
CFDS-FLOW3D
Subcooled boiling
experiments, Christensen
(1961)
Gibeling and
Mahaffy (2002)
Author’ 1D
code
NPHASE
Pipe flow experiments,
Laufer (1953)
Schultz and
Weaver (2003)
RELAP5
FLUENT
Grgic et al. (2003)
RELAP5
GOTHIC
IRIS reactor 4-inch break

<!-- page 808 (PDF 80) -->
Assessment can be performed as (Fig. 12.15):
l
Verification or solving the equation correctly;
l
Validation or solving the correct equations;
l
Demonstration of the capability to solve a given class of problems.

### 12.11.1 Assessment matrix

The assessment matrix can consist of (OECD/NEA/CSNI/R(2014)3, 2014):
l
“Exact” solutions and corresponding CFD calculations;
l
Validation experiments and corresponding CFD calculations;
l
Demonstration CFD simulations, and possibly prototype experiments;
Any assessment matrix should be strictly problem dependent: that is, any particular
matrix must contain at least part of a computational path (numerical algorithm and/
or physical model) considered for the intended application of the code.
As a consequence, a separate assessment matrix should be prepared for every
selected nuclear safety issue where CFD simulation can be beneficial. This is a very
demanding task. Fortunately though, many items (particular matrices) will be the
same in the majority of such groups of matrices associated with different applications,
since the same numerical algorithm and physical models will often be used.
Whereas verification should be performed mainly by code developers, validation
and demonstration are strictly application dependent and must therefore be performed,
or at least overseen, by users. Validation and demonstration are the principal themes of
this document. A review of several available general-purpose databases comprising
experimental data is presented below under appropriate subheadings.
Intended application, planning, requirements gathering, PIRT
Experiments
Code
verification
Validation
Demonstration, including solution verification
Assessment
Fig. 12.15 Applicability demonstration for CFD codes (OECD/NEA/CSNI/R(2014)3, 2014).

<!-- page 809 (PDF 81) -->
Then, specific application areas, namely boron dilution, pressurized thermal
shocks, thermal fatigue, and aerosol transport in containments, are dealt with in more
detail. Some corresponding experiments are presented, together with available calculations
. On the basis of analysis of experimental data and results of CFD simulations, a
statement on the appropriateness of a given CFD code to the intended class of
problems can be stated. This step completes the description of the existing
assessment bases.

#### Examples of established assessment bases for NRS applications

A list of experiments already adopted (i.e., boron dilution, PTS and core) or envisaged
areas needing experiments to demonstrate the applicability and the qualification of
CFD codes to NRS problems is given below (OECD/NEA/CSNI/R(2014)3, 2014)
(Section 5):
l
Boron dilution: University of Maryland experiments and corresponding simulations (ISP-
43); ROCOM experiments (FLOMIX-R); Gidropress Facility (FLOMIX-R); Vattenfall
Experiments (FLOMIX-R);
l
Pressurized Thermal Shock (PTS):
−
Creare 1:5 (Tests 100, 101, 103, 104, 106) and 1:2 (tests May 105, May 106), USA;
−
IVO (FORTUM) 2:5 (Tests T9, T10, T12, T16, T44, T45, T47, T51, T106, T111 to
T116), Finland;
−
Purdue 1:2 (Runs 0-1C, 0-1C-R, 0IV, 0-2C, 0-2C-R, 0-2 V, CE-1C, W-1C,B&W-1C,
CE-2C, W-1C-90, CE-1C-PS, CE-3C-0), USA;
−
HDR 1:1 (Tests T32.11 to T32.15, T32.18 to T32.22, T32.31 to T32.34, T32.36, T32.41,
T32.51, T32.52, T32.57, T32.58, T32.61), Germany
−
UPTF 1:1 (Runs 020, 021, 023, 025, 026), Germany
l
Core benchmark: MATIS-H facility and KAERI facility.
l
Thermal fatigue: T-junctions in Liquid-Metal Reactors and Light Water Reactors; Parallel
jets,
l
Aerosol transport in containments;
l
Sump clogging;

### 12.11.2 Deficiencies in assessment

Validation of CFD codes for NRS application frequently encounters deficiencies,
which includes, but is not restricted to (OECD/NEA/CSNI/R(2014)3, 2014):
l
PIRT for the intended application is not prepared.
l
Quantified estimates of experimental and numerical uncertainties are not provided.
l
Validation metrics, figures of merit, or target values for the intended application are not
clearly defined.
l
Experiments, selected for validation at some of the tiers, do not meet requirements put on
validation experiments. Since validation experiments are very expensive, experiments
intended for other purpose (e.g., for study of physical phenomena or for development of
physical models), or very old experiments performed on already nonexisting facilities
(which excludes feedback between CFD simulations and experiments), are sometimes used.
l
For some physical phenomena identified in the PIRT, suitable experiments are missing so
that new experiments must be proposed.

<!-- page 810 (PDF 82) -->
l
Validation simulations cannot provide information on boundaries of regions of acceptability
of the conceptual model from regions where the model cannot be applied, or where its
application is questionable.

#### Identification of gaps in technology and assessment bases

An assessment matrix for a given application should comprise three groups of items
(OECD/NEA/CSNI/R(2014)3, 2014) (Section 6):
l
Verification problems with “highly accurate” CFD solutions;
l
Validation experiments and their CFD simulations;
l
Demonstration simulations, possibly with some suitable supporting experiments.

#### 12.11.2.1 Additional notes: Validation in computational simulation of nuclear system thermal fluids behavior

The notes below are intended to provide an overview of efforts of and some insights into
the numerical validation (focusing on the CFD method) relating to the nuclear system
thermal fluids behavior. In addition to general CFD validation requirements, we stress
outtheimportanceofconsideringthephysicsinspecificproblemsforthevalidationprocedure
. We provide specific examples to support the respective main points addressed
using the previous CFD validation experiences from our groups and other groups.
For the last few decades, the broad applications of the computational simulation to
predict nuclear system thermal fluids behaviors have been performed. Traditionally,
system codes and subchannel analysis codes have been successful to a degree for the
nuclear safety analysis. However, because their main role is to combine numerous
empirical correlations based on very simple governing equations to evaluate the
synthetic effect, the expected level of accuracy was relatively low. The validation is
performed against global variables (pressure, temperature, void fraction, liquid level,
and so on) in a relatively large control volume (components, subchannels, and so on)
On the other hand, in recent years, as the computing power increases, the CFD code
has become a viable tool to predict the more detailed thermal fluids behavior in the
nuclear system with a higher accuracy than system and subchannel codes.
However, because the nuclear system, in general, involves very complex phenomena
characterized as high turbulence and/or multiphase during not only transient
events and accidents but also normal operating conditions, the models used in the
CFD code for the nuclear system problems still involves empirical closure models,
such as RANS equations with turbulence closure models for turbulence calculations
and two-fluid model equations with closure models for two-phase calculations, rather
than less-empirical models, such as wall-resolved LES/DNS turbulence models and
ITMs, respectively, because of practical feasibility. Once some assumptions and
related modeling are involved in the CFD code, we need to understand more about
the phenomenon of our interest because the assumptions and modeling have to have
capability of reflecting key phenomenon.
The CFD validation is not just comparing the CFD-calculated results with the
measured data for a given problem. For successful CFD validation, we need to
consider several things from experimental point of view, CFD point of view, and both

<!-- page 811 (PDF 83) -->
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
CFD BPG—for mesh sensitivity, mesh quality, turbulence models and near-wall treatment
, numerical schemes, and so on—toreduce the user errors and evaluate the selected
CFD methods in a right way. Beyond this, we need to use an advantage of the CFD—
availabilityofall variablesinthecomputationaldomain—tounderstandtheoverall phenomenon
made in the selected CFD world. This will help both experimental design and
interpretation of discrepancies between the CFD results and measured data.
From both points of view, it should be stressed that the reliable and effective CFD
validation needs closer collaboration between experimentalists and CFD analysts.
Both ways from experiment to CFD and from CFD to experiment can greatly reduce
time and cost at the end. Each party needs to be willing to provide not only results
(data) but also the limitations (errors and uncertainty) and phenomenological insights
to another and try to understand the other party to achieve a common goal effectively.

### 12.11.3 Verification matrix

Code verification activities can be subdivided into Numerical Algorithm Verification
and Software Quality Assurance Practices. Here, only the Numerical Algorithm
Verification will be discussed in which CFD solutions are compared with “correct
answers,” which are highly accurate solutions for a set of well-chosen test problems.
Designing and performing the Numerical Algorithm for verification imposes the
need for highly accurate solutions. Then, there is a hierarchy of confidence in these
“highly accurate solutions,” ranging from high confidence of exact analytical
solutions and/or application of the Method of Manufactured Solutions (MMS),
through semianalytic benchmark solutions (reduction to numerical integration of
ODEs) to highly accurate benchmark numerical solutions to PDEs.

### 12.11.4 Requirements for assessment

#### 12.11.4.1 Validation and demonstration matrices

According to the tiered approach to validation of conceptual models, four progressively
simpler levels of validation experiments can be distinguished:
l
complete system,
l
subsystem cases,
l
benchmark cases,
l
unit problems.

<!-- page 812 (PDF 84) -->
Related experiments should be selected or proposed for each intended application of
the CFD code, with at least one suitable experiment (or a set of experiments in the case
of unit problems and benchmark cases) at each level.

#### 12.11.4.2 Requirements for validation of experimental data

According to the ECORA BPG, experimental data for validation of a CFD code
should be complete (geometry, boundary and initial conditions, well analyzed as to
the physical phenomena involved), high quality (accurate within given error bounds,
repeatable, consistent), and publicly available.

#### 12.11.4.3 Demonstration simulations

Demonstration simulations are frequently similar to subsystem or complete system
cases when there is no or very limited experimental support. Only very approximate
conclusions on applicability of the conceptual model can therefore be formulated.
Nevertheless, demonstration simulations are very important from the viewpoint of
application, since such simulations can support decisions on funding of verification
and validation activities, or even of purchase of a CFD code. Especially at the
complete system levels, multiscale and multiphysics coupling is frequently required,
and balance of resource constraints, including time, level of effort, available expertise
and desired fidelity is very important. In many cases, a demonstration simulation is the
first step in application of a CFD code to an NRS issue; such simulation can provide an
insight into problems very probably encountered in future, more serious, application
of the code. These problems can then be taken into account during planning of the
code validation activity.
When demonstration simulations of the same problem are performed with two or
more CFD codes, some idea on effectiveness of algorithms can be deduced. Since
requirements put on the demonstration simulations are very relaxed in comparison
with the validation simulations, it is not in fact possible to speak about
“deficiencies,” with the exception of formulation of the initial and boundary conditions
(which are either deduced from system code calculations or defined as “the most
unfavorable” from the point of view of the intended application), fineness of the computational
grid, selection of time steps, and selection of physical models. An important
role in the evaluation of demonstration simulations is played by expert judgment,
which should take into account all the mentioned deficiencies.

### 12.11.5 Insights into the assessment process

The overall procedures of CFD analysis for the simulation of heat transfer and fluid
flows in a rod bundle with mixing vane grids is considered in this section.
Overall steps of CFD methodology development and validation for the rod bundle
problem are presented in Fig. 12.16. First, we have to clearly set objectives of CFD
analysis and then set a validation strategy, i.e., choose benchmark problems for the
validation of CFD methods. For each benchmark problem, we must clearly describe

<!-- page 813 (PDF 85) -->
the problem and then set the CFD solution strategy, which includes choice of CFD
methods of turbulence models, computational domain, boundary conditions, numerical
schemes, grid types, and resolution. This choice is initially based on previous CFD
exercises on this and similar problems and general CFD guidelines. Then, we implement
the CFD calculations based on the CFD methods selected and analyze the results
by comparing them with experimental results. Changing a specific choice in CFD
methods, we iterate the application and analysis until we find the optimized CFD
methods in terms of accuracy and efficiency.

#### 12.11.5.1 Setting objectives of CFD analysis (Step 1)

First, we set objectives of CFD analysis clearly, e.g., design of a component,
safety analysis, interpretation of experimental data, validation of numerical grid
structure, validation of a model, demonstration of CFD code-user quality, user
Setting objectives of CFD analysis
Setting validation strategy
(Choice of benchmark problems)
Problem description
Setting CFD solution strategy
(choice of CFD methods)
Application of CFD methods
Analysis and interpretation of the results
Sensitivity study
For each benchmark problem
Other benchmark problems
Fig. 12.16 Overall steps of CFD methodology development and validation.

<!-- page 814 (PDF 86) -->
training (many calculation analyses actually fall in this category), finalizing the
development of a CFD model, development of BPG or demonstration of quality
for BPG, etc.

#### 12.11.5.2 Setting validation strategy (Step 2)

The next step is to set validation strategy. Here, one needs to thoroughly review previous
experiments and CFD analyses relating to the topic to efficiently and specifically
set the strategy. Collecting available experimental tests and identifying
unresolved CFD issues, one must select and organize experiments as benchmark problems
. During the choice process, several problems, not a single problem, are often
considered. This is because one problem cannot be complete in terms of data coverage
and quality and because data provided sometimes need to be cross-checked through
other tests at similar conditions. In addition, attacking one complex problem often
does not clearly reveal the source of discrepancy, if one exists, because the problem
may involve several complex interactions. In this case, we can take the stepwise
approach from simple to complex problems.

#### 12.11.5.3 Problem description (Step 3)

Once experimental tests to be benchmarked are determined, for each problem CFD
methods are applied and validated. Before applying CFD methods, each benchmark
problem should be clearly defined. The following information should be described in
detail:
l
Purposes of the experiment,
l
Geometry, and
l
Boundary conditions
In addition, any uncertainties (incompleteness) relating to the above information must
be clearly stated. This can play an important role in the result analysis procedure.

#### 12.11.5.4 Setting CFD solution strategy (Step 4)

Then, we need to set CFD solution strategy for a given problem, which includes many
choice procedures, such as choice of computational domain, choice of boundary
conditions, choice of turbulence models including near-wall treatment, choice of
numerical schemes, choice of geometrical representation, and choice of computational
grids. It should be pointed out that the choice of any CFD method does not
necessarily coincide with the actual implementation. In other words, in the implementation
of CFD methods, geometry and computational domain are first generated and
the grid is, then, created mainly by using preprocessing tools. Then, the choices of
other CFD methods may follow.
In this step, knowledge about CFD methods previously used for this or similar
problems and general guidelines is very important because it provides for an effective
initial choice of CFD methods, which can reduce uncertainties and thus the number of
methods requiring sensitivity study. Thus, we identify main CFD methodological

<!-- page 815 (PDF 87) -->
issues, which can preliminary affect the results, especially target variables in the
region of interest.

#### 12.11.5.5 Application of CFD methods (Step 5)

In the process of application of CFD methods selected, i.e., implementing the CFD
solution strategy with a particular code, user errors should be minimized and appropriate
convergence criteria must be selected. These issues are not specific to rod
bundle problems, but are general to all CFD simulations.

##### Minimizing user errors

Before running the code, a potential source of user errors should be checked. Such
errors may be minimized by using a formal check list or by letting another CFD
analyst check through the code input data.
For example, the following types of questions can be considered (Gallagher and
Woodburn, 2003):
l
Have boundary conditions not only been properly defined, but also properly applied?
l
Has the appropriate system of units been used?
l
Is the geometry correct?
l
Are the correct physical properties specified?
l
Have the intended physical and mathematical models, such as gravity force, rotation, and
user-defined functions, been used?
l
Have default parameters been changed which may affect the solution?
l
Has the appropriate convergence criterion been defined?

##### Choice of convergence criteria

The choice of convergence criteria also needs to be considered in the application of a
CFD method, i.e., running the CFD code, because most computer programs use
iterative methods to solve the algebraic system of equation (e.g., the equation for
the pressure). Here, convergence indicates the criterion adopted to terminate an
iterative process, not the convergence of discretized equation to differential equation.
The following convergence criteria are typically used (COST, 2007):
l
(Scaled) residuals;
l
Target variables;
l
Integral balance of mass, momentum, and energy.
The termination criterion is usually based on the residuals of the corresponding
equations. These residuals should tend toward zero. Scaling of the residuals is usually
done with the residuals after the first iteration. The scaled residual then shows how
much the initial error has dropped. In industrial applications, typically a termination
criterion of 0.001 is used, which, in general, is too high to have a converged solution.
A reduction of the residuals of at least four orders of magnitude is recommended. For
validation purposes of turbulence or other physical models much lower threshold
criteria should be used.
General guidelines for convergence control are as follows (Gallagher and
Woodburn, 2003):

<!-- page 816 (PDF 88) -->
l
Be aware that different codes have different definitions of residuals.
l
Always check the convergence on global balances (conservation of mass, momentum, and
turbulent kinetic energy) where possible, such as the mass flow balance at inlet and outlet
and at intermediate planes within the flow domain.
l
Check not only the residual itself but also the rate of change of the residual with an increasing
iteration count.
l
Convergence of a simulation should not be assessed purely in terms of the achievement of
a particular level of residual error. Carefully define solution-sensitive target quantities for
the integrated global parameters of interest and select an acceptable level of convergence
based on the rate of change of these (such as mass flow, lift, drag and moment forces on
a body).
l
For each problem class, test the effect of converging to different levels of residual on the
integrated parameter of interest (this may be a single calculation that is stopped and restarted
at different residual levels). This test demonstrates at what level of residual the parameter of
interest can be considered to have converged and identifies the level of residual that should
be aimed at in similar simulations of this problem class.
l
Monitor the solution in at least one point of a sensitive area to see if the region has reached
convergence.
For calculations that are proving difficult to converge, the following advices may be
helpful (Gallagher and Woodburn, 2003):
l
Use more robust numerical schemes during the first (transient) period of convergence and
switch to more accurate numerical schemes as the convergence improves.
l
When using RSM, start with a stable turbulence model like the k-ε model.
l
Reduce parameters controlling convergence, for instance, under-relaxation parameters or the
CFL number.
l
If the solution is heavily under-relaxed, increase relaxation factors at the end to see if the
solution holds.
l
Check whether switching from a steady to a transient calculation has any effect.
l
Consider using a different initial condition for the calculation.
l
Check the numerical and physical suitability of boundary conditions.
l
Check whether the grid quality in areas with large residual has any effect on the
convergence rate.
l
Look at the residual distribution and associated flow field for possible hints, e.g., regions
with large residuals or unrealistic velocity levels.

#### 12.11.5.6 Analysis and interpretation of the results (Step 6)

Most commercial CFD codes have useful postprocessing tools, which allow various
flow and heat transfer phenomena to be visualized or plotted in graphical form. The
step of results analysis covers:
l
Checking credibility of results,
l
Checking needs of sensitivity studies, and
l
Using various variables which help understand the phenomena.
Checking the credibility of the results in the validation process can be directly
implemented because the main target variables are usually given in the experiment.

<!-- page 817 (PDF 89) -->
However,ifthe objectiveofthesimulationistoprovidedetaileddatainanewspacergrid
design, checking credibility may involve several steps, such as checks on conserved
variables, visual confirmation that velocities and pressure are smoothly distributed,
and comparison with other similar problem results (Gallagher and Woodburn, 2003).
As discussed in the step of setting the CFD solution strategy, a sensitivity study is
not confined to only computational grid resolution, but is also applied to all computational
methods selected in the CFD solution strategy step, such as turbulence modeling
, near-wall treatment, numerical schemes, grid types, boundary conditions, and
geometrical representation. In practicality, performing a sensitivity study about all
procedures is impossible, since an interpretation of the results must focus on finding
the CFD method most regarded as affecting the target variables.
Analysis using multiple variables helps understand the phenomena more clearly.

## 12.12 CFD scaling

### 12.12.1 The scaling issue

The word scaling can be used in a number of contexts: two of these are reported here.
(1) Scaling of an experiment is the process of demonstrating how and to what extent the
simulation of a physical process (e.g., a reactor transient) by an experiment at a reduced
scale (or at different values of some flow parameters, such as pressure and fluid properties)
can be sufficiently a representative of the real process in the reactor.
(2) Scaling applied to a numerical simulation tool is the process of demonstrating how and to
what extent the numerical simulation tool validated on one or several reduced scale experiments
(or at different values of some flow parameters, such as pressure and fluid properties
) can be applied with sufficient confidence to the real process.
One should emphasize that scaling is meant here in terms of the prediction of a result
for the reactor from a scaled experiment, as defined by Oberkampf and Roy in their
book on V&V (Oberkampf and Roy, 2010).
When solving a reactor thermal-hydraulic problem, the answer to the scaling issue
may be:
1. Purely experimental: the experiments can tell what would occur in the reactor with sufficient
accuracy and reliability;
2. Purely numerical: only numerical simulations are used to solve the problem (usually this is
not acceptable);
3. Both experiments and simulation tools are used to solve the issue (this is the best practice).
The first case is not common and is not considered here since CFD simulation tools are
not involved. The second case is also not common, due to the limited reliability and
accuracy of thermal-hydraulic simulation tools. So we will focus here on the third
case, in which both experiments and simulation tools are used to try to resolve the
issue. This means that the simulation tool is used to extrapolate from experiments
to the reactor situation, and that the degree of confidence in this extrapolation is itself
part of the scaling issue.

<!-- page 818 (PDF 90) -->
The extrapolation to a reactor situation made by a single-phase CFD tool introduces
several new aspects and raises several questions:
l
How to guarantee that a CFD code can extrapolate from a reduced-scale validation experiment
to the full-scale application?
l
How to extrapolate nodalization from a reduced-scale validation experiment to the full-scale
application?
l
How to extrapolate:
–
from one fluid to another?
–
to a different value of the Re number and/or to a different value of any other
nondimensional number important in the physical processes taking place?
l
In any case, numerical simulation of scaled experiments has a given accuracy defined by the
error on some target parameters, and one should determine how the code error changes when
extrapolating to the reactor situation.
Therefore, scaling associated with a CFD application is part of the CFD code uncertainty
evaluation, and is a necessary preliminary step in this uncertainty evaluation.
Both scaling and uncertainty are closely related to the process of Validation and Verification
. The definition of a metric for the validation is also part of the issue.

## 12.13 Conclusions and recommendations

12.13.1
Conclusions of OECD/NEA/CSNI report (OECD/NEA/CSNI/
R(2014)3, 2014)
Hereafter conclusions are reported that have been agreed within a wide scientific
community (OECD/NEA/CSNI) in relation to the CFD technology. The reported
conclusions are (obviously) consistent with the text of the chapter. Minor editorial
changes are introduced, namely to adapt the original text to the content of this chapter.
The use of computational methods for performing safety analyses of reactor
systems has been established for nearly 40 years. Reliable codes have been developed
for analyzing the primary system in particular, and results from these analyses are
often used to support the safety assessment of nuclear power systems undertaken
by the regulatory authorities. Similarly, but to a lesser extent, programs have also been
written for containment and severe accident analyses. Such codes are based on
networks of 1D or even 0D cells. However, the flow in many reactor primary
components is essentially 3D in nature, as is natural circulation, mixing, and stratification
in containments. CFD has the potential to treat flows of this type and to handle
geometries of almost arbitrary complexity. Already, CFD has been successfully
applied to such flows, and to a limited extent has made up for a lack of applicable test
data in better quantifying safety margins. Consequently, CFD is expected to feature
more prominently in reactor safety analyses in the future.
The traditional approaches to nuclear reactor safety analysis, using system codes
for example, take advantage of the very large database of mass, momentum, and
energy exchange correlations that have been built into them. The correlations have

<!-- page 819 (PDF 91) -->
been formulated from essentially 1D special-effects experiments, and their range of
validity is well known, and (as far as possible) controlled internally within the numerical
algorithms. Herein lays the trustworthiness of the numerical predictions of such
codes. Analogous databases for 3D flows are very sparse by comparison, and the issue
of the trust and reliability of CFD codes for use in NRS applications has therefore to be
addressed before the use of CFD can be considered as trustworthy.
A list of NRS problems for which it is considered CFD analysis is required or its
application is expected to result in positive benefits in terms of better understanding
and improved safety margins is provided in OECD/NEA/CSNI (2014) and also
discussed in this chapter. The list contains safety issues of relevance to fluid flows
in the core, primary circuit and containment, both under normal and off-normal operating
conditions including accident sequences. The list contains both single-phase and
two-phase safety items, though in the latter case reference is made to the document
dealing with the Extension of CFD Codes to Two-Phase Flow Nuclear Reactor Safety
Problems, Mahaffy et al. (2007a,b) and OECD/NEA/CSNI (2014) (see also Bestion
et al., 2016).
Recognizing that CFD is already an established technology outside of the nuclear
community, a list of the existing assessment bases from other application areas has
also been included in OECD/NEA/CSNI (2014) and their relevance to NRS issues
discussed in the same report. It is shown that these databases are principally of two
types: those concerned with aspects of trustworthiness of CFD code predictions in
general industrial applications (ERCOFTAC, QNET-CFD, FLOWNET), and those
focused on specialized topics (MARNET, NPARC, AIAA). The usefulness and
relevance of these databases to NRS have been assessed. In addition, most CFD codes
currently being used for NRS analysis have their own, custom-built assessment bases,
the data being provided from both within and external to the nuclear community.
Application of CFD to NRS problems can benefit indirectly from these databases.
The continuing efforts to extend them can lead to a well-maintained NRS-specific
database, a valuable addition.
Descriptions of the existing CFD assessment bases have been established specifically
within the nuclear domain and their usefulness discussed. Typical examples
are experiments devoted to the boron dilution and in-vessel mixing issues (ISP-43,
ROCOM, Vattenfall 1/5th Scale Benchmark, UPTF TRAM C3), pressurized thermal
shock (UPTF TRAM C2), and thermal fatigue in pipes (THERFAT, Forsmarks), all of
which have already been the subject of benchmarking activities. The EU Framework
Programs, such as ASTAR, ECORA, EUBORA, FLOWMIX-R and ASCHLIM, have
also provided direct NRS-specific data and/or have each focused on relevant aspects
of the CFD modeling.
The technology gaps which need to be closed to make CFD a more trustworthy
analytical tool have also been identified in OECD/NEA/CSNI (2014). These include,
for example, lack of a proper uncertainty methodology; limitations in the range of
application of turbulence models, for example in stratified and buoyant flows;
coupling of CFD with neutronics and system codes, needed to keep simulations to
a manageable size; and generally computer power limitations in simulating long
transients. Particular application areas for which CFD simulations need to be

<!-- page 820 (PDF 92) -->
improved are in stratified flows, containment modeling, aerosol transport and deposition
, and liquid-metal heat transfer. In other areas, such as in-vessel mixing, the
models may be adequate but grid resolution is inadequate due to the current lack
of machine power, a situation that will certainly improve with time.
The computational overhead of performing CFD simulations in comparison with
system code transient computations may still be regarded as a definite limitation of
the potential for directly using CFD in licensing procedures, even for single-phase
applications for which the underlying models are well established. The uncertainty
quantification methodology for system codes generally requires 50–100 computations
to be carried out, and the statistical method of Latin Hypercube Sampling (LHS) is
becoming widespread in order to optimize the efficiency of the random parameter
sampling. This cannot, at the present time, be mirrored with CFD, and until it can,
a different methodology needs to be established. However, in the spirit of BPGs, at
least mesh independency must be demonstrated, and some limited study of sensitivity
to input parameters should be attempted. The issue of access to the source code of CFD
software, particularly in regard to the commercial codes, will also have to be
addressed before CFD is accepted as an analysis tool by the regulatory bodies.
There is a distinct lack of quality validation data for aerosol transport, even though
the phenomenon was identified as a key process in containment modeling, and one
that can only be treated mechanistically by the use of CFD. The experiments carried
out at the PHEBUS facility as part of the EU 5th Framework Programme PHEBEN
produced only data of an integral nature, and as such very limited in regard to
validating CFD models. Comprehensive, local aerosol deposition data appear only
to be available for pipes (straight and elbowed), and for some nonnuclear applications,
such as atmospheric pollution. This is one key area where future CFD assessment
needs to be focused.
Important new information has been provided by the material presented at the
CFD4NRS series of Workshops (here listed in the Foreword), in which numerical
simulations with a strong emphasis on validation were particularly encouraged, and
the reporting of experiments which provided high-quality data suitable for CFD
validation. Participation in the workshops has enabled a list of existing databases
to be assembled of possible candidates for future benchmarking activities for:
(1) primary circuits,
(2) core-flow regions,
(3) containments,
in relation to which data of the type needed for CFD benchmarking already exists or
are likely to be available in the near future.
This updated document represents a continuing process in establishing an assessment
database for the application of CFD to NRS problems, but in many places
reflects the time and manpower restriction for issuing the concerned OECD/NEA/
CSNI report (this also applies to this chapter), and considerable further work still
needs to be done in terms of both presentation and technical content. Sections of
the OECD/NEA/CSNI report, as well as of this chapter, remain unbalanced in terms
of detail, reflecting not only the subjective inputs of the authors but also whether the

<!-- page 821 (PDF 93) -->
safety issue being addressed is of a country-specific nature or of more common
concern. Part of the recommended obligation to regularly update the provided information
shall include an attempt to equilibrate the information level. In addition,
similar information appears in different sections of the report and of the chapter. This
was done to avoid excessive page turning or scrolling, but gives the OECD/NEA/
CSNI document (and this chapter) an appearance of disjointedness if read in a
continuous manner.
CFD remains a very dynamic technology, and with its increasing use within the
nuclear domain there will be ever greater demands to document current capabilities
and prove their trustworthiness by means of validation exercises. It is therefore
expected that any existing list of specific assessment databases will soon require
further updating. In order to prevent the important information assembled in the
OECD/NEA/CSNI document and in this chapter from becoming obsolete, the following
recommendations are made:
l
Extend the process of consolidating the information contained here through continuous
updating. This process is necessary to ensure that the NRS assessment database is readily
accessible to all, and as dynamic and mobile as the CFD technology itself.
l
Set up a forum for numerical analysts and experimentalists to exchange information in the
field of NRS-related activities relevant to CFD validation, e.g., like the one provided by the
series of CFD4NRS workshops (see e.g., Foreword to this chapter).
l
New blind CFD benchmarking exercises should be defined, both to encourage the release of
previously restricted CFD-grade data from experiments, to test the skills of the CFD
practitioners, and perhaps persuade the software developers to improve their models, where
these have proved lacking. To this end, it is encouraging to note that representatives of the
large commercial software houses actively participate in the benchmarks.
Finally, it seems worthwhile to extend the alarm given in the following statement of
OECD/NEA/CSNI (2014) report to this chapter. The Special CFD Group, which was
first set up in 2007 and initially comprised of the chairmen of the original three Writing
Groups (WG) together with the NEA secretariat, can continue to act as the central
organizing bodies for the above activities provided new members are appointed to
replace the “old guard.” The timescale for this process is (i) overdue for the WG1
chairman (J. H. Mahaffy reached pensionable age in 2009); (ii) imminent for the
WG2 chairman (B. L. Smith reached pensionable age in 2012); and within sight
for the WG3 chairman (D. Bestion will reach pensionable age in 2017). It is important
to ensure a smooth transition to a new group membership before the existing expertise
is lost.

### 12.13.2 Final-summary remarks

The complex CFD subject is discussed in this, work-in-progress type (see the
Chapter foreword), chapter: question marks and identification of critical issues are
part of the text; however, an attempt is made to clarify some important topics in
relation to nuclear thermal hydraulics. Any reader who has completed the reading
of the chapter should not believe he has acquired the understanding of the CFD
