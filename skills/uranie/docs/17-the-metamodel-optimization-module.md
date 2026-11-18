# The Metamodel Optimization module
<!-- source PDF pages 157-159 -->

<!-- page 150 (PDF 157) -->
THE METAMODEL OPTIMIZATION MODULE

## 10.1 Introduction

For an optimization problem, when the evaluation function costs in term of resource, chaining the construction of a
surrogate model with the optimization process could be a good solution. Uranie provides modules that can be used directly
to do so. The Metamodel Optimization module gives another way to do similar things by coupling the two process: the
surrogate model construction and the optimization research.
So far, the module provides a parallelized version of the Efficient Global Optimization (EGO) algorithm for mono objective
problems.

## 10.2 Efficient Global Optimization

### 10.2.1 Introduction

EGO [JSW98] makes a global search. As a genetic algorithm, it needs an adequate numbers of initial evaluated items
to initiate its search: in our case, to be able to construct a sufficiently pertinent model. After this first phase, it builds a
surrogate model, and then loops on updating the model with new evaluations, and on searching a new promising solution
to evaluate using this model.
For its surrogate model, EGO uses kriging models which provide, for estimated points, a prediction value and an associated
variance. EGO defines an objective, the expected improvement, which takes both of them into account and provides a
trade-off between a good estimation value and a large uncertainty.
Because of its efficiency in term of evaluation number, this kind of algorithm is well suited when evaluations are expensive
to compute. EGO algorithm is expensive: both construction of the surrogate model and search of the next attractive point
are complex optimization problems, and are done many times, slowing down the problem resolution.
Extensions to constraints and/or to multi objective should come later in Uranie.

#### 10.2.1.1 Parallelism

Uranie’s EGO provides an asynchronous parallelism. With n resources, synchronous parallelism generates n items, evaluates
them and waits for all results and iterates. In asynchronous parallelism, when a result comes, a new item is generated
which takes into account the n-1 evaluations in progress.
Usually a new point generation is not expensive and the resource that finishes its evaluation usually waits for it. It is not
the case for EGO. To avoid wasting computation time, different approaches are implemented:
• the next point is generated before getting the evaluation result back (and so with n ongoing evaluations instead of
n-1)
• after a point generation, if more than one evaluation are available, we get all results back, and if the solver afford
to do so, we generate few points to be evaluated.

<!-- page 151 (PDF 158) -->
• otherwise, if no evaluation is available, the search of next attractive points are extended to try to improve them.

### 10.2.2 Problem definition

This module extends the Reoptimizer module and is kept in a separated module because of its dependency with the
Modeler module. Its use follows the same structure and is also based on the Relauncher architecture. Having that in
mind, it is suggested to have a look at The Relauncher module and at The Reoptimizer module for a better understanding.
As it uses a kriging model, it is also suggested to look at The kriging method.
The principal difference is in the solver definition: we have to define the kriging model and its construction parameters;
and to use an adapted optimization solver.

#### 10.2.2.1 TEGO

The TMaster subclass for EGO is TEGO. Its constructor has two standard arguments, a TDataServer and a TRun
pointer. Three kinds of TDataServer can be passed to the class :
• An empty tds with the input TAttribute declared: initial points are random;
• A tds filled with a sampler where input TAttribute are declared: initial points are defined by user but they need
to be evaluated.
• A tds filled with a launcher or relauncher where both input and output TAttribute are declared: initial filling
phase can be skipped;
The TEGO objects have a method named setSize with two integer arguments: the first one, used in the case of an empty
tds, gives the number of random points needed for the construction of the first surrogate model; the second one gives the
maximum evaluation number of the expensive code.
Two different solvers can be defined, one for the surrogate model construction (using setModeler method) and one for
the next point search (using setSolver method). If they are not defined a default solver is used.
Optimization loop ends when either:
• max number evaluation is reached;
• expected improvement objective is lower than a threshold;
• a Cholesky decomposition problem occurs in the surrogate model construction.
In these version, results are not filtered: all evaluated points are saved in the TDataServer

#### 10.2.2.2 TEgoModeler

There is only one modeler currently available TEgoKBModeler
To deal with solutions that are currently under evaluation by the cpu resources (asynchronous parallelism), this modeler
uses the kriging believe principle (it trusts in the model prediction). Two models are created: a first one, built with all the
evaluated solutions, is used to estimate solutions under evaluation; a second model, built with both evaluated solutions
and estimated ongoing solutions, is used by the solver to find the next solution to evaluate. Predictions is not significantly
affected in the second model but the variances are, especially around ongoing solutions. The EI objective takes it in
account, naturally driving next solutions away from them.
As it is an optimization, advancing in its search, EGO will generate solution near existing ones. It is a difficulty for model
construction that can leads to Cholesky decomposition errors. To get around this problem, users can use the kriging
regulation.
it uses

<!-- page 152 (PDF 159) -->
##### 10.2.2.2.1 TEgoKBModeler

The TEgoKBModeler has a constructor without argument and 2 user methods:
• setModel defines the model that will be used in optimization. It has 3 parameters: a const char* defining the
model to use ("matern7/2" for example); another const char* defining the trend ("const" for example); a
double defining a regularization (1.e-8, use 0.0 for no regularization).
• setSolver define how the model will be constructed. It has 4 parameters: a const char* defining the objective
to minimize ("ML" for maximum likelihood); a const char * defining the NLopt solver to use ("Bobyqa" for
example); an int defining the size of the preliminary screening; an int defining the maximum evaluation number
for optimization.
Take a look at The kriging method for details on possible parameter values.

#### 10.2.2.3 TEgoSolver

There are 4 available solvers combining two distinct features:
• dynamic or static optimization: in static, the search restart with a new random population; in dynamic the search
restart from the previous population which should be rich enough to find a point that was put aside. In dynamic,
the first search is longer than the following one.
• genetic or HJMA algorithm;
This leads to the following classes: TEgoDynSolver, TEgoStdSolver, TEgoHjDynSolver and TEgoHjStdSolver
some methods are provided:
• significantEI with a double parameter is used to define the EI threshold to stop the search loop
• setManyNewItem with an int is used to define the maximum number of new items used to feed the empty
resources (unused with TEgoStdSolver).
• for the class using HJMA, setSize with two int parameters defines the number of global search performed by
the optimization in the preliminary search and in the following ones.
• for the class using Vizir algorithm, setSolver with a pointer on a TVizirSolver defines the solver to use.
• for the TEgoDynSolver, the first and longer search uses the maximum evaluation number defined in the solver.
The following search are shorter and is defined using setStepSize and its int argument.
