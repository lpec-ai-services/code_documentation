# Part 2. Insights into computational fluid dynamics for nuclear power plant applications — CFD validation
<!-- source PDF pages 79-88 -->

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
