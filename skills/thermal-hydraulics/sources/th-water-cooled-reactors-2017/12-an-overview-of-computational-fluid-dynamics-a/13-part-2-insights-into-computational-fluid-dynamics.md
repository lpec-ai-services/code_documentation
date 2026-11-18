# Part 2. Insights into computational fluid dynamics for nuclear power plant applications — CFD scaling
<!-- source PDF pages 89-89 -->

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
