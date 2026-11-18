# The Reoptimizer module
<!-- source PDF pages 148-156 -->

<!-- page 141 (PDF 148) -->
THE REOPTIMIZER MODULE

## 9.1 Introduction

The reoptimizer module provides optimisation features, using the relauncher architecture. It can indeed be considered
as a specialisation of this module for the closed-loop case (optimisation steps usually depends on the previous steps).
This document will present neither an introduction to the optimisation problem characteristics (one simple version can be
found in [Bla17]), nor a description of the different algorithms. It will more discuss the possible combination of runners,
solvers and masters with (if possible) their pros and cons. For a glimpse at the way the implementation of a script can be
done, one can look at the use-cases, provided in Macros Reoptimizer.
Two kinds of solver are proposed: local search ones, starting from an initial guess point and global search ones, starting
from a random population of potential solutions. They differ on many points:
• Problem types: only global solvers offer multi-objective optimisation.
• Constraints: Global solvers deal with inequality but not equality constraints, while local ones deal with both of
them.
• Inputs nature: all solvers deal with continuous problems, and some global solvers can deal with combinatory problems
, with extra works.
• Convergence speed and robustness: local solvers need less evaluations to converge but can be trapped in a local
minimum, while global ones are more robust.
• Unavailable items: only global solvers can deal with it.
• Parallelism: local solvers are intrinsically sequential, and the only way to parallelised them is to run many optimisations
starting from different points. Global solvers are intrinsically parallel.

### 9.1.1 local optimizer

A local solver proposes mono-objective optimisation with or without constraints. It uses the NLopt library [Joh] and
different solvers are proposed. These solvers could be distinguished with:
• Needed information: some solvers need gradient information while others use just the objective value.
• Constraints handling: some solvers handle constraints naturally while the others use the augmented Lagrangian
method.

### 9.1.2 global optimizer

A global solver proposes mono and multiobjective optimisation, potentially with constraints. It uses the Vizir library
[Arn10] and offers different solvers.

<!-- page 142 (PDF 149) -->
### 9.1.3 Number of objectives

The number of objectives to be minimised plays a crucial part in the technique to be used, along with the time needed
for a given code to converge and provide results. The main idea behind this small discussion is to identify the needs when
starting an analysis.
• One objective or more than one but they are not antagonistic: a single objective optimisation can be done. When
dealing with several criteria the idea is then to combine them into an homemade criteria, based on whatever recipe
one wants to apply (weighted/unweighted criteria, L1 or L2 sum, …). From there, the use of TNlopt algorithm is
recommended.
• More than one objective that cannot be combined. In this case, the approach recommended would be to use Vizir
which contains multi and many objectives algorithms. The difference between multi and many is tidious and is
oftenly set between 3 and 4. A discussion between these algorithm is provided in [Bla17].

## 9.2 Problem definition

An optimisation problem is a kind of parametric studies, so, it could make the best of the Relauncher architecture. Having
this in mind, having a look at The Relauncher module is crucial in order to get good understanding of the following,
already-introduced, concepts.
In this module, one will introduce new masters, meaning classes that inherit from TMaster which will handle the distribution
of evaluations, with extra specificities linked to their optimisation purpose. But before using them, the runners
(inheriting from TRun) and assessors (inheriting from TEval) have to be defined as well, respecting the pattern separation
between study and evaluation sides. Only the study side is concerned by optimisation objects (all these notions are defined
in The Relauncher module). The standard steps to solve an optimisation problem are:
• to declare the optimisation input parameters.
• to choose a solver (eventually configure it).
• to create a master (eventually configure it).
• to declare the objective and constraints of the problem.
• to run the optimisation.
• to analyse the results.
The Rosenbrock example script provided in Relauncher abstraction levels gives a simple example of these steps.
There are few TMaster sub-classes depending of the local or global algorithm that is chosen (the underlying library).
The constructor has three arguments: the two TMaster usual arguments (a TDataServer and a TRun), and the solver.
A common method to all masters is setTolerance with a double as only argument. It defines a threshold to stop the
search. However, its interpretation is solver dependant.
As we saw in the TMaster section, item definition parameters are defined in the TDataServer used as first constructor
argument. These attributes generally need to be defined with a domain, whose boundaries are used for the optimisation.
The master and solver declaration will be covered in next section. Running the optimisation is done by the solverLoop
method, and results will be found in the TDataServer.
Lightbulb Tip
Before Uranie version 4.2, only the final results were kept in the dataserver and no option was allowing the user to
keep track of all performed estimation (either to see how the algorithm is driving the parameters evolution, or just
for bookkeeping). From version 4.2, it is possible to create an empty TDataServer and to provide it to the chosen
Master so that every computation will be stored in this specific object. For a single objective optimisation this should
look like this:

<!-- page 143 (PDF 150) -->
```python
# ... Problem definition
runner.startSlave()
                     # Usual Relauncher construction
if runner.onMaster():
    # Create the main TDS
    tds = DataServer.TDataServer("nloptDemo", "Param de l'opt nlopt pour la barre")
    tds.addAttribute(x)
    tds.addAttribute(y)
    # Defining the optimisation condition
    solv = Reoptimizer.TNloptCobyla()
                                       # algorithm
    # Create the single-objective constrained optimizer master
    opt = Reoptimizer.TNlopt(tds, runner, solv)
    # ... + objective, constraint...
    # Create the dataserver in which all computation will be stored
    trc = DataServer.("allevents", "dataserver containing all events")
    opt.setTrace(trc)
                       # pass the dataserver to the master
    opt.solverLoop()
                      # perform the optimisation
```

###  9.2.1 Objectives and Constraints

An optimisation problem is defined by an objective (may be more for multi-objective problems) and eventually some
constraints (objectives can as well be called criteria in various literature). An item evaluation may return many values.
Some of them may be used as objectives or constraints, while the others are left unused by the solver. The master
methods addObjective, addConstraint and addEquality may be used to declare the corresponding values. The
last method is only available in local solver. All these methods have a first argument, the output variable (a pointer to its
corresponding TAttribute object), and a second optional argument (a pointer to a modifier object).
Modifiers are used to overwrite the default solver behaviour: objectives have to be minimised, constraints are satisfied
when their values are lesser than zero, and equality when their value is zero. Once this is settled and when the returned
value does not fit with these defaults, a modifier have to be used. Existing modifier classes are:
• TMaximizeFit objective modifier: value has to be maximised.
• TTargetFit objective modifier: value has to be closed to a target value.
• TLesserFit constraint modifier: value has to be lesser than a threshold value.
• TGreaterFit constraint modifier: value has to be greater than a threshold value.
• TInsideFit constraint modifier: value has to be inside a domain.
The chosen threshold value(s) are passed in the constructor.
Exclamation-Triangle Warning
In the current implementation, it is not allowed to use an input variable as an objective or a constraint.

<!-- page 144 (PDF 151) -->
### 9.2.2 Sizing of a hollow bar example problem

In order to give a more detailed example of the usage of both local and global solvers, the hollow bar problem is introduced.
It consists in finding the lengths of the internal and external sides of a hollow bar with a square section, minimising its
weight (i.e. its section) and its deformation by an external force applied at its centre. The two lengths are normalised so
that they evolved in a 0 to 1 range and the pipe can be sketched as done in Figure 9.1.
Figure 9.1: Hollow Bar
The problem has then three variables:
• 𝑓1(𝑥, 𝑦) = 𝑥−𝑦which is called the thickness.
• 𝑓2(𝑥, 𝑦) = 𝑥2 −𝑦2 which is called the section.
• 𝑓3(𝑥, 𝑦) = (𝑥4 −𝑦4)−1 which is called the distortion
and three natural constraints:
• 0 < 𝑥< 1.
• 0 < 𝑦< 1.
• 𝑥> 𝑦
In the following sections the idea will be to study (if possible) the minimisation of the section of the bar and the distortion,
keeping a minimum thickness of about 0.4. This threshold is chosen so that the bar can sustain its own weight. The
examples will use an external code to compute the three previously-introduced variables once both the internal and external
lengths are provided. The code is written in python as following:

```python
#!/usr/bin/env python
"""
Simple file to mimick the barAllCost function to emulate it as a code
"""
x = .8
y = .3
def barre(out_l, in_l):
    """Compute the constraint and objectives for the hollow bar
```

<!-- page 145 (PDF 152) -->
```python
    Arguments:
    out_l -- outter length of the hollow bar
    in_l -- inner length of the hollow bar
    """
    epais = out_l - in_l
    surf = out_l*out_l - in_l*in_l
    defor = 1 / (1.e-66 + out_l*out_l*out_l*out_l - in_l*in_l*in_l*in_l)
    return [epais, surf, defor]
def echo(out_l, in_l):
    """Print the results of the hollow bar computation
    Arguments:
    out_l -- outter length of the hollow bar
    in_l -- inner length of the hollow bar
    """
    print("#COLUMN_NAMES: c1|o1|o2")
    print("")
    evt = ""
    for i in barre(out_l, in_l):
        # print i,
        evt += "%.25g " % i
    print(evt)
echo(x, y)
```

In both examples, the same tip is used: the bar.py file is used to perform the computation (as the code is defined by
python bar.py > output.dat) but it is also defined as the input file for the TCode. Thanks to this, the file is copied
to every temporary working directory (so no need to change the $PYTHONPATH environment variable) and no extra file is
needed to define the inputs. The output is directly stored as an ASCII file compatible with the usual Salome table format
so that it can easily be read and convert as a TDataServer

## 9.3 Local solver

Local solvers proposed by Uranie come from the NLopt library (Non Linear OPTimization). This library is developed
by Steven G. Johnson, integrating many original algorithms in an uniform interface. The NLopt website provides many
useful information, that enhance the succinct ones provided here. The example used as support for this part is given in
Macro “reoptimizeHollowBarCode.py” with a specification with respect to the way it was described in Sizing of a hollow
bar example problem: since there is no multicriteria solver implemented from NLopt, the criteria on the distortion is
downgraded to a constraint using a randomly defined threshold (set to 14).

### 9.3.1 TNlopt

The TMaster subclass for local optimizer is called TNlopt.
Local optimization starts from an initial guess point. This point has to be defined using the setStartingPoint method
with an integer to precise the dimension, as first argument and a double * as second argument. This has changed in order
to be complient with python but also to be able to check that the provided number of double is matching the dimension of
our problem under consideration. You can call the setStartingPoint method many times. In Python, it could look
like this:

<!-- page 146 (PDF 153) -->
```python
import numpy
...
opt = Reoptimizer.TNlopt(tds, runner, solv)
...
p = numpy.array([0.2, 0.3])
opt.setStartingPoint(len(p), p)
```

In this case, each optimization, starting from a corresponding starting point, may be done in parallel using an appropriate
TRun. If the results of the optimisation is not consistent when changing the starting points, this might be a sign for a
problem with local minimum. In this case a safer (but slower) solution might be to consider using global solvers.
To modify the default configuration, the setMaximumEval method, with an int as only argument, may be used. The
default value is 10 000. For multi starting point, it is interpreted as the accumulation of all evaluations.

### 9.3.2 Solvers

Uranie proposes different Nlopt solvers. For direct solvers, there is:
• TNloptCobyla: Constrained Optimization BY Linear Approximation from M.J.D.Powell works. The only direct
algorithm that supports constraints naturally.
• TNloptBobyqa: Bounded Optimization BY Quadratic Approximation from M.J.D.Powell works. It is usually
quicker than the previous one, but might give nonphysical results if the problem should not be assumed to be
quadratic.
• TNloptPraxis: It uses the PRincipal AXIS method of Richard Brend. This algorithm has a stochastic part.
• TNloptNelderMead: The well known Nelder-Mead Simplex algorithm.
• TNloptSubplexe: a simplex variant, the Tom Rowan’s subplex algorithm.
and for gradient-based solvers:
• TNloptMMA: Method of Moving Asymptotes from Krister Svanberg works. It deals with nonlinear inequality constraints
naturally.
• TNloptSLSQP: Sequential Least-Squares Quadratic Programming from Dieter Kraft. It deals with both inequality
and equality constraints naturally.
• TNloptLBFGS: an implementation of the Limited memory Broyden-Fletcher-Goldfarb-Shanno algorithm written
by Ladislaw lukan.
• TNloptNewtown: A preconditioned inexact truncated Newtown algorithm written by Ladislaw Lukan.
• TNloptVariableMetric: An implementation of shifted limited-memory variable-metric by Ladislaw lukan.
You may notice that actually none of Nlopt global solvers is provided.
Lightbulb Tip
Remarks for the gradient case: oftenly one does not have access to the real gradient. In this case a finite difference
method is used by doing 2𝑛𝑋+ 1 computation around every point, which implies:
• a code that will provide results with a sufficient accuracy so that the gradient is not always assumed to be
null (which can happen when a code returns a value with a very low number of digits). Even with a non-null
estimation, the gradient accuracy needs to be sufficient since gradient-based solver usually estimates the Hessian
matrix.
• a possible parallelisation of the computation.

<!-- page 147 (PDF 154) -->
## 9.4 Global solver

IR𝑝spaces have no ordering relations when 𝑝is greater than 1. As a consequence, finding the minimum of a function the
output of which is defined in such a space has no meaning. Multicriteria optimisation solves this problem by finding the
inputs corresponding to the Pareto frontier in the costs space.
The evolutionary algorithm library Vizir, allows to perform multicriteria optimisation with a global approach, and is
available in Uranie. It is first introduced in a broad picture (even though more details can be found in [Bla17]) before
considering the different solvers available and their possible configuration. We have also illustrate its use in a simple
example that can be found in Macro “reoptimizeHollowBarCodevizir.py”.

### 9.4.1 A step-by-step description of Vizir

Figure 9.2: Schematic description of the requested steps of an optimisation procedure once this one is performed with
Vizir
The global organisation of an analysis performed within Uranie with the Vizir package is as followed: the user request a
certain number 𝑁Cand of elements to describe correctly the Pareto set and front.
1. The first step is to create randomly, only using the research space definition, a population of the requested size. An
evaluation is performed for all candidates, meaning that the criteria and constrains will be tested and the results
will be stored in a vector for all candidates. All the calculation concerning a candidate will count as one evaluation
(this notion will be important later on when considering the number of evaluation 𝑁Eval). This step (the turquoise
blue box in Figure 9.2) is followed by the ranking of all the candidates (red step in Figure 9.2).
2. As already discussed, ranking single criterion results is simple because there is an obvious relation order, but this is
not the case when dealing with multi-criteria. The chosen solution in the Uranie implementation is to affect a rank
to a candidate under study, corresponding to the number of other candidates that dominate it. The best candidates
have then a rank 0 (they are not-dominated), following by rank 1, rank 2… With the ranking step completed the
next step is to test whether the algorithm has converged or not.
3. The test of convergence can reach three possible states:
• all the tested candidates are not-dominated. This means the algorithm have converged and the loop will stop
as the objective of having a description of both Pareto set and front is achieved.
• not all candidates are not-dominated but the maximum number of evaluation has been reached. In this case,
the algorithm stopped as well but this time without having converged. Restart the algorithm with different
configuration might be a possibility.
• not all candidates are not-dominated and the maximum number of evaluation is not reached.
4. In the latter case, a certain fraction of the candidates will be selected and used as a new starting point to recreate a
new population. A fraction 𝜆is indeed kept (this fraction value being set by changing the survival rate in the genetic
case, whose default value is 40%) in order to produce a new generation that will hopefully converge better than
the current one. The evolutionary algorithm uses the selected fraction (𝜆𝑁Cand) to complete the total population

<!-- page 148 (PDF 155) -->
(meaning re-generating 1 −𝜆𝑁Cand). This procedure is explained more deeply, in the case of a genetic algorithm,
in [Bla17].

### 9.4.2 TVizir2 and TVizirIsland

The TVizir2 and TVizirIsland classes are the TMaster subclass for global optimizer, the former being the more
commonly used disregarding the chosen solver and runner. The latter is dedicated to the island principle: instead of growing
a large population, 𝑁Is populations are defined (this parameter can be changed by the dedicated setIsland(int)
method) and are growing independently, exchanging inhabitants from time to time.
The setSize may be used to configure this. The first argument defines the population size (default to 250). The second
optional argument defines the maximum number of evaluations that the solver may use (default to 100 000). The third
optional argument defines the number of items born to create a new generation (default to 50).

### 9.4.3 Solvers

The Vizir solvers, that are interfaced with Uranie, are:
• TVizirGenetic, a genetic algorithm using a diploid representation.
• TVizirSwarm, a particle swarm algorithm.
• TVizirSimplex, a Nelder Mead Simplex variant, adapted to work with a population, and to deal with multiobjective
problem.

#### 9.4.3.1 TVizirGenetic

The TVizirGenetic (whose principle and vocabulary is define in [Bla17]) can be configured using the following methods
:
• setMutationRate, defines the rate of population items that are muted during creation. Default value is 0.01
(1%).
• setHomozygoteRate, defines the rate of population considered as homozygote. Default value is 0.5 (50%).
• setSurvivalRate, obsolete, defines the rate of population items that survive at each generation. use setSize
instead. Default value is 0.4 (40%).

#### 9.4.3.2 TVizirSwarm

The TVizirSwarm behaviour can be configured using the following methods:
• setLocalSize, defines the particle memory size: its size and a generation step size.
The particle number is defines using the third parameter of setSize method (generation item number). It is half of it.
No specific method is actually provided.

#### 9.4.3.3 TVizirSimplex

The TVizirSimplex have not any specific configuration method.

#### 9.4.3.4 Many objectives methods

The global solvers discussed here have dedicated methods to call many-objective algorithms. An example of implementation
can be shown in Macro “reoptimizeHollowBarVizirMoead.py”.
• setMogaDiversity(int val=0)
• setCrowdDiversity(int vois=0)
• setPairDiversity(int vois=0)

<!-- page 149 (PDF 156) -->
• setIbeaDiversity(double k=0)
• setKneeDiversity(int vois=0, double taux=0.0)
• setMoeadDiversity(int cut1, int cut2=0, int vois=0)
• setStoppingCriteria(int stop=0)
