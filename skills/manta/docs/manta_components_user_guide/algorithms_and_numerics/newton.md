<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/algorithms_and_numerics/newton.html -->

# Newton's algorithm

This page describes how to use the `NewtonAlgorithm` class.

Note that some elements of theory regarding the `NewtonAlgorithm` are available
in this [guide of the frontend](../../manta_frontend_user_guide/solvers/implicit_model_solvers.md#manta-user-guide-implicit-model-solver).
A description of its implementation details can be found in this
[blueprint section](../../developer_guide/blueprints/newton_algorithm_blueprint.md#blueprint-newton-algorithm).

## Example of usage

The `NewtonAlgorithm` solves the non-linear problem described by a `LinearSystem`. First,
one needs to create this `LinearSystem`, from which a `NewtonAlgorithm` can be instantiated:

```c++
    auto &newtonLinearSystem                                   = rm.make<LinearSystem>("NewtonFVSystem", mesh);
    Vector<std::pair<const FieldBase *, DofVar>> unknownFields = {{&U, Uvar}};
    NewtonAlgorithm newtonAlgorithm(newtonLinearSystem, unknownFields, "newtonAlgorithm");
```

This `LinearSystem` is filled with the `EquationTerm` objects of the `Formulation`
objects assigned to it. Any formulation assembling the jacobian of the problem in the left-hand side
and its residual in the right-hand side (see [the blueprint section](../../developer_guide/blueprints/newton_algorithm_blueprint.md#blueprint-newton-algorithm))
can be used with this algorithm. The formulations currently used with a `NewtonAlgorithm` are listed
in [this section](#newton-compatible-formulations).

The relevant `Formulation` is thus instantiated, and assigned to the `LinearSystem`:

```c++
    auto &implicitAdvForm = rm.make<ImplicitAdvectionFormulation<1, 1, FVNewtonBEFeatures>>(tube, U, Uvar, advFunc);
```

```c++
    rm.assignFormulationToLinearSystem(implicitAdvForm, newtonLinearSystem);
```

## Solving

The `NewtonAlgorithm` is then mostly used to solve one time step (or one load increment) with
`solve(ctx)`:

```c++
      auto s = newtonAlgorithm.solve(ctx);
```

`solve()` returns an `Expected<SolveOutput>`: on failure (e.g. maximum number of iterations
exceeded), `shallStop()` is true and the error message is registered in the context. On success,
the `SolveOutput` gives the convergence history of the solve:

- `numberOfIterations`: number of iterations performed;
- `firstIterationResidualNorm`: residual norm at the first iteration, used for normalization;
- `absoluteResidualNormValues`, `relativeResidualNormValues`: residual norms at each iteration.

```c++
const auto output = newtonAlgorithm.solve(ctx);
if (output.shallStop()) {
  std::cerr << ctx.getErrorMessage() << std::endl;
}
nIter += output->numberOfIterations;
```

Note

Once the solve has converged, the internal variables of the formulations shall usually be updated
before the next time step, by calling the dedicated method of the formulation assigned to the
`LinearSystem` (e.g. `update()` for a `SolidFiniteElementFormulation`, or
`afterConvergence()` for an `ImplicitAdvectionFormulation`):

```c++
auto &newtonLinearSystem = rm.make<LinearSystem>("newtonSystem", mesh);
rm.assignFormulationToLinearSystem(userFormulation, newtonLinearSystem);
NewtonAlgorithm newtonAlgorithm(newtonLinearSystem, {{&U, Uvar}}, "");
// ...
if (!newtonAlgorithm.solve(ctx).shallStop()) {
  userFormulation.afterConvergence();
}
```

## Options

All the methods below are defined in `NonLinearSolverBase`, and are thus available for every
specialization (`NewtonAlgorithm`, `CastemLikeNewtonAlgorithm`). The setters returning an
`ExitStatus` register an error message in the context on failure, and shall be checked.

**At construction.** Besides the `LinearSystem` and the `(field, dofVar)` pairs used to update
the unknown fields with the solution (see [this section](#newton-compatible-formulations)), the
tolerances, the maximum number of iterations, the convergence criterion and its norm, the multiphysics
resolution and the parameters of the linear solver can be given as *Parameters*
(*convergenceTolerances*, *maximumNumberOfIterations*, *thresholdOnTheFirstResidualNorm*,
*convergenceCriterion*, *convergenceNorm*, *multiphysicsResolution*, *linearSolver*):

```c++
NewtonAlgorithm newtonAlgo(linearSystem,
                           {{&U, Uvar}},
                           Parameters{{"convergenceTolerances", Parameters{{"relativeConvergenceTolerance", 1e-6}}},
                                      {"maximumNumberOfIterations", 20}});
```

**Convergence tolerances.** `setRelativeConvergenceTolerance()` and `setAbsoluteConvergenceTolerance()`
set the tolerances, `setConvergenceTest()` chooses how they are combined (`relativeTest` by
default, `absoluteTest`, `absoluteOrRelativeTest` or `absoluteAndRelativeTest`), and
`setThresholdOnTheFirstResidualNorm()` sets the norm below which the first residual is considered
null (the solve then converges at once):

```c++
newtonAlgo.setRelativeConvergenceTolerance(ctx, 1e-6);
newtonAlgo.setAbsoluteConvergenceTolerance(ctx, 1e-10);
newtonAlgo.setConvergenceTest(NewtonAlgorithm::absoluteOrRelativeTest);
newtonAlgo.setThresholdOnTheFirstResidualNorm(ctx, 1e-15);
```

**Maximum number of iterations.** `setMaximumNumberOfIterations()` (10 by default): beyond it, the
solve fails.

```c++
newtonAlgo.setMaximumNumberOfIterations(ctx, 20);
```

**Convergence criterion.** `setConvergenceCriterion()` chooses between the norm of the residual
(*residualNorm*, default) and the stationarity of the unknowns (*stationarity*), and
`setConvergenceTestToMultiphysic()` checks the convergence separately on each physics of a
monolithically coupled problem (see [this section](#multiphysicconvergence)).
`setConvergenceNorm()` chooses the norm used by any of these criteria (*INF*, default, or
*L2*), once only: the absolute tolerances shall then be adapted, the L2 norm growing with the number
of degrees of freedom.

```c++
newtonAlgo.setConvergenceCriterion(ctx, "stationarity");
newtonAlgo.setConvergenceNorm(ctx, "L2");
newtonAlgo.setConvergenceTestToMultiphysic(
    ctx, Parameters{{"absoluteConvergenceTolerances", Parameters{{"velocity", 1e-6}, {"pressure", 1e-5}}},
                    {"relativeConvergenceTolerances", Parameters{{"velocity", 1e-4}, {"pressure", 1e-2}}}});
```

**Normalization factors.** `freezeNormalizationFactors()` keeps the residual norm used to compute the
relative residual from one call to `solve()` to the next, and `unfreezeNormalizationFactors()`
lets it be recomputed at the first iteration of each call again (see the section below):

```c++
newtonAlgo.freezeNormalizationFactors();
```

**Quasi-Newton.** `setJacobianUpdateTrigger()` sets when the jacobian is recomputed (at every
iteration by default; see [this section](#jacobianupdatetrigger)):

```c++
// the jacobian is only recomputed at the first iteration of each call to solve()
newtonAlgo.setJacobianUpdateTrigger([](const NewtonAlgorithm::SolveOutput &o) noexcept { return o.numberOfIterations == 0; });
```

**Convergence acceleration.** `setAccelerationMethod()` sets the *act3* or *andersonNStep*
acceleration, only once per solver (see [this section](#setaccelerationmethod)):

```c++
newtonAlgo.setAccelerationMethod(ctx, "andersonNStep", /*andersonDepth=*/3);
```

## Call-backs

User-defined functions can be called at each stage of the Newton loop (`init`, `iterationInit`,
`assemble`, `convergenceCheck`, `linearSolvePreparation`, `linearSolve`,
`reactionComputation`, `solutionUpdate`, `solveEnd`). `addCallBackAfter()` adds such a
call-back after a given stage, i.e. called once the work of this stage succeeded: it takes the
`Context` and a `NewtonState` giving access to the local variables of the loop, and its
failure stops the solve. The stages, and what each call-back can
access and modify, are detailed in the section below and in [the blueprint section](../../developer_guide/blueprints/newton_algorithm_blueprint.md#blueprint-newton-algorithm).
The values returned by the getters of the `NewtonState` at each stage are given in
[this table](../../developer_guide/blueprints/newton_algorithm_blueprint.md#blueprint-newton-getters-table).

```c++
newtonAlgo.addCallBackAfter(NewtonStage::reactionComputation,
                            [&](Context &c, NewtonAlgorithm::NewtonState &) noexcept -> ExitStatus {
                              return linearSystem.updateReactionField(c, R, Uvar);
                            });
```

Shortcuts are available for the most common call-backs, all added at the `solutionUpdate` stage,
i.e. at the end of each iteration:

- `addAfterIterationTask(f)`: calls `f(ctx)`;
- `addAfterIterationTask(fields, f)`: calls `f(ctx, field, correction)` for each given field;
- `addUpdateMeshCoordinateAfterIterationTask(newtonAlgo, U)`: moves the mesh with the correction of
  the displacement field `U` (large displacements).

```c++
newtonAlgo.addAfterIterationTask([](Context &) { std::cout << "end of an iteration" << std::endl; });
newtonAlgo.addAfterIterationTask({&Q}, [](Context &c, const FieldBase &q, const FieldBase &dq) { dq.print(c, true, 2); });
addUpdateMeshCoordinateAfterIterationTask(newtonAlgo, U);
```

## Other useful methods

- `getLinearSystem()`: returns the `LinearSystem` solved by the algorithm, e.g. to be used in a call-back.
- `getInfo(ctx)`: displays the settings of the algorithm on the log stream of the context (verbosity
  level greater than `verboseLevel3`).
- `CastemLikeNewtonAlgorithm`: a `NewtonAlgorithm` preset with the *act3* acceleration
  and a jacobian only recomputed at the first iteration of each call to `solve()` (see the section below).

## Formulations usable with a Newton algorithm

The formulations currently used with a `NewtonAlgorithm`, either in tests or through the Newton
solver of the frontend, are:

- `BlockingFormulation`
- `DirichletConstraintFormulation`
- `GlueConstraintFormulation`
- `HeatSourceFormulation`
- `HHODirichletConstraintFormulation`
- `HHOExternalBodyForceFormulation`
- `ImplicitAdvectionFormulation`
- `ImplicitAnalyticalContactFormulation`
- `ImplicitBurgersFormulation`
- `ImplicitContactFormulation`
- `ImplicitHeatTransferLinearCapacityFormulation`
- `ImplicitHeatTransferLinearConvectionFormulation`
- `ImplicitHeatTransferNonlinearConvectionFormulation`
- `ImplicitHeatTransferSolidMaterialFormulation`
- `ImplicitMicromorphicDamageSolidMaterialFormulation`
- `ImposedHeatFluxFormulation`
- `ImposedNodalForcesFormulation`
- `ImposedPressureFormulation`
- `ImposedResultingForceFormulation`
- `ImposedUniformGravityForceFormulation`
- `InPlaneFormulation`
- `LinearizedElasticityFiniteElementFormulation`
- `MultiplePointsConstraintFormulation`
- `NonlinearHeatSourceFormulation`
- `NSMonolithicTaylorHoodALEFormulation`
- `NSMonolithicTaylorHoodFormulation`
- `NSNestedTaylorHoodIncompressibilityFormulation`
- `NSNestedTaylorHoodVelocityFormulation`
- `NSTaylorHoodVolumicForceFormulation`
- `PhaseFieldDamageImplicitFormulation`
- `SingleComponentDirichletConstraintFormulation`
- `SolidFiniteElementFormulation`
- `SolidHHOFormulation`
- `ThermalDiffusionFormulation`

## Use of `setJacobianUpdateTrigger()` to handle a semi-Newton like resolution

By default the `NewtonAlgorithm` uses a consistent jacobian search operator
that comes from the underlying formulation. However using the `setJacobianUpdateTrigger()`
method, users can set the algorithm to avoid recomputing the operator at each iteration of
the newton loop. An example of this usage is available below:

```c++
  NewtonAlgorithm newtonAlgo(feSystem, {{&U, U__}}, "semiNewtonAlgo");
  newtonAlgo.setJacobianUpdateTrigger(
      [](const NewtonAlgorithm::SolveOutput &solveOutput) noexcept { return solveOutput.numberOfIterations % 3 == 0; });
```

The method expects a function which defines the conditions at which the search operator must be
recomputed. Here, it is recomputed every third iteration, and kept constant otherwise. This kind of
approximation of the jacobian using its consistent value every ith iteration is usually called a
semi-Newton method.

The very first iteration of the first time-step always implies a consistent computation of the tangent
operator. Then, calling `false` in the trigger means that the previously computed operator is kept.

## Use of `setAccelerationMethod()` to accelerate convergence

A convergence acceleration method can be set on the `NewtonAlgorithm` using the
`setAccelerationMethod()` method, either with a keyword or with the
`NewtonAlgorithm::AccelerationMethod` enumeration.
The theory behind these methods is described in [this section](../../theory_manual/nonlinear_resolution/non_linear_resolution_theory.md#theory-convergence-acceleration).
An example of this usage is available below:

```c++
  if (!newtonAlgo.setAccelerationMethod(ctx, accelerationMethod, /*andersonDepth=*/3)) {
    std::cerr << ctx.getErrorMessage() << std::endl;
    return ExitStatus::failure;
  }
```

The available methods are:

- *none* (default): standard Newton algorithm.
- *act3*: Cast3M's `ACT3` acceleration, correcting the residual before the solve, as in
  Cast3M from the fourth iteration on and then every other iteration. Since it assumes a constant
  search operator, the next correction is postponed by 4 iterations whenever the jacobian is rebuilt
  within a call to `solve()`: with a full Newton (jacobian rebuilt at every iteration), *act3*
  thus never corrects anything.
- *andersonNStep*: Anderson acceleration, correcting the increment before the update of the
  solution. Its depth is the optional last argument of `setAccelerationMethod()` (3 by default).
  The depth is the number of secant directions used to build the accelerated iterate, i.e.
  `depth + 1` iterates are kept in history: a depth of 1 is a secant method. A depth of 0 is
  accepted but disables the acceleration (the accelerated iterate is then the plain Newton one).

These methods are mostly useful with a quasi-Newton approach (see `setJacobianUpdateTrigger()` above).

The acceleration method can only be set once per solver: once *act3* or *andersonNStep*
has been set, any further call to `setAccelerationMethod()` fails, whatever its argument
(including *none*). If the returned `ExitStatus` is ignored, the first method silently
stays in use. Setting *none* does nothing, so it does not prevent setting another method later.
To use another method, build a new solver.

## The `CastemLikeNewtonAlgorithm` preset

The `CastemLikeNewtonAlgorithm` is a `NewtonAlgorithm` with presets mimicking Cast3M's
`UNPAS` procedure: the *act3* acceleration, and a jacobian only recomputed at the first
iteration of each call to `solve()`. It is used exactly as a `NewtonAlgorithm`. The jacobian update
setting can be changed afterwards with `setJacobianUpdateTrigger()`, but the acceleration method
can't: since *act3* is already set, any call to `setAccelerationMethod()` fails. Use a plain
`NewtonAlgorithm` for another acceleration method.
More details are available in [this section](../../theory_manual/nonlinear_resolution/castem_like_newton.md#castem-newton).

## Use of `freezeNormalizationFactors()` and `unfreezeNormalizationFactors()`

At the first iteration of the newton loop, the initial estimated residual norm is used
to normalize the next computed residuals norms: this normalization yields the relative residual norm.

This first iteration residual norm is the *normalization factor*. It can be frozen across
multiple time-steps by calling `NewtonAlgorithm::freezeNormalizationFactors()`, and thereafter
recomputed by calling `NewtonAlgorithm::unfreezeNormalizationFactors()`.

## Use of `multiphysicsResolution` to handle a monolithically coupled problem

If the algorithm is used on a `LinearSystem` built by the monolithic coupling of 2 or more
physics, it is possible to evaluate convergency on each physics separately by adding the
`multiphysicsResolution` *Parameter*.

On the contrary, if nothing is specified, the residual is evaluated as the infinity norm of the RHS of the `LinearSystem`.
In the context of a monolithically coupled problem, this RHS may contain several quantities of different order of
magnitude. For example, for a monolithic damage mechanics problem, displacements (of order \(10^{-6}\) m),
coexist with damage (of order \(10^{0}\)) in the solution vector. Their dual, contained in the RHS could then
also be of very different magnitudes.

Users may specify that they wish to perform a `multiphysicsResolution` which means that:

- normalization factors are computed independently for each physics
- absolute and relative residuals are evaluated separately
- convergency is evaluated separately for each physics

Convergence is satisfied if all physics converge.

Users have to specify absolute and relative tolerances for each physics using two *Parameters*
defined as [name of the field - tolerance]. The name of the field is the `std::string`
used to name the *Field* onto which the given physic is defined. For the damage mechanics
example given above, the name of the displacement field, and the name of the damage field could be used.

Here is an example of usage of this feature on a Navier-Stokes model (coupling velocity and pressure),
solved monolithically:

```c++
    //Navier Stokes fields
    auto &Vets = rm.make<NodeField<>>(channel, "velocity", 2, 1);
    auto &P    = rm.make<NodeField<>>(channelp, "pressure", 1, 1);
```

And for the definition of the `NewtonAlgorithm`

```c++
    // definition of the tolerances for each physics
    Parameters absoluteConvergences                     = Parameters{{"velocity", 1e-6}, {"pressure", 1e-5}};
    Parameters relativeConvergences                     = Parameters{{"velocity", 1e-4}, {"pressure", 1e-2}};
    Parameters absoluteAndRelativeConvergenceTolerances = Parameters{{"absoluteConvergenceTolerances", absoluteConvergences},
                                                                     {"relativeConvergenceTolerances", relativeConvergences}};

    Vector<std::pair<const FieldBase *, DofVar>> NS_UnknownFields = {{&Vets, Vvar}, {&P, Pvar}};
    auto newtonAlgo                                               = std::make_shared<NewtonAlgorithm>(
        NSsystem,
        NS_UnknownFields,
        Parameters{{"multiphysicsResolution", absoluteAndRelativeConvergenceTolerances}, {"maximumNumberOfIterations", 50}});
```

Note

when a `multiphysicsResolution` is used, the *stationarity* convergence criterion is used,
rather than the *residualNorm* criterion. Those criteria are described below.

## Choice of the convergence criterion

Multiple convergence criteria are available:

- *residualNorm* (default), evaluating the norm of the residual at the RHS as well as the enforcement of the constraints
- *stationarity*, evaluating if the increment of the unknowns is going toward 0.

As mentionned above this criterion can be chosen with a *Parameter* in the `NewtonAlgorithm` constructor,
or by using the `setConvergenceCriterion` method.

More details on convergence criteria are available in [the blueprint section](../../developer_guide/blueprints/newton_algorithm_blueprint.md#blueprint-newton-algorithm).

## Diverse user-defined call-back functions

Users can define several call-backs functions that can be called at different stages of the loop.
The call-back machinery described below is defined in `NonLinearSolverBase`, and is thus usable
with any of its specializations (`NewtonAlgorithm`, `CastemLikeNewtonAlgorithm`, ...).
Most of them are added at one of the stages of the loop (`NewtonStage`), whose
position in the loop is detailed in [the blueprint section](../../developer_guide/blueprints/newton_algorithm_blueprint.md#blueprint-newton-algorithm):

- `init` : called once, before the first iteration.
- `iterationInit` : called at the start of each iteration, once the maximum number of iterations
  has been checked (it is not called at an iteration where this maximum is exceeded, since the solve
  then stops).
- `assemble` : called after the assembly of the system: the residual (RHS) is always
  reassembled, but the jacobian only when the jacobian update trigger requests it (see
  `setJacobianUpdateTrigger()` above). With a quasi-Newton trigger, which is the setup
  recommended with the acceleration methods, only the RHS is thus reassembled at most iterations.
- `convergenceCheck` : called after the convergence check, may overwrite its decision.
- `linearSolvePreparation` : called when the iteration is not converged, the linear system being ready
  to be solved, may correct the residual.
- `linearSolve` : called after call to solve.
- `reactionComputation` : called after computation of reactions, but before the solution is incremented by the found \(\v{\delta U}\), may correct \(\v{\delta U}\).
- `solutionUpdate` : called after the solution has been incremented, at the end of each iteration.
- `solveEnd` : called once, at the end of a converged solve, may overwrite its status.

These call-back functions can be sent to the algorithm via lambda functions packaged in the following
methods:

- `NonLinearSolverBase::addCallBackAfter(stage, f)`: adds the call-back
  (`NonLinearSolverBase::CallBack`) `f` after the
  given stage, after the ones already added there. All the call-backs have the same signature
  `ExitStatus(Context &, NewtonState &)`, where `NewtonState` gives, through getters, the local
  variables of the loop (convergence history, status of the solve, reactions, iterate \(\v{U}\),
  correction \(\v{\delta U}\) and convergence decision). The four latter don't exist from the start of
  each call to `solve()`: before they are computed, their getters register an error message and
  return a null pointer. Anything else
  (linear system, fields, load factor, ...) shall be captured by the lambda.

  The acceleration methods are implemented with such call-backs too, registered by
  `setAccelerationMethod()` (or by the `CastemLikeNewtonAlgorithm` constructor): at the
  `init` stage for both, and at the `linearSolvePreparation` stage for *act3* or the
  `reactionComputation` stage for *andersonNStep*. Since call-backs added at the same stage
  are called in the order they were added, a user call-back added at one of those stages sees the
  quantities (residual, \(\v{\delta U}\)) before the acceleration if it is added before the call to
  `setAccelerationMethod()`, and after it if it is added afterwards. With a
  `CastemLikeNewtonAlgorithm`, the user call-backs always come after the *act3* ones.
- `NonLinearSolverBase::addAfterIterationTask()`: shorter syntax adding a call-back at the
  `solutionUpdate` stage, i.e. at the end of each iteration.

Note

`AfterIterationTasks` exist in two flavours. One can specify a callback requiring only the `Context`,
or specify a callback based on the fields of the problem at hand. In this latter case, the field must be inputted
with the callback. An example of this is the case of the update of the mesh configuration at the end of an iteration:
one needs to specify which field is the displacement field that is used to distort the mesh. This kind of callback
then contains the field and the associated correction field, as can be seen in the example below.

Below is an example of how to add such callbacks, after the instanciation of a `NewtonAlgorithm`:

```c++
    // testing afterIterationTasks
    newtonAlgorithm.addAfterIterationTask([](Context &) { std::cout << "what's up ?" << std::endl; });

    // testing afterIterationTasks based on a field:
    // > prints the correction field related to the unknown field at hand
    newtonAlgorithm.addAfterIterationTask({&Q},
                                          [](Context &ct, const FieldBase &q, const FieldBase &dq) { dq.print(ct, true, 2); });
```

Like every call-back, they are called in the order they were added.

## Principle of operation

At the moment the resolution of systems of non-linear equations in MANTA is
a simple extension of the [pipeline](../../developer_guide/pipeline/pipeline.md#pipeline). Indeed the Newton's algorithm
simply requires that several linear systems be solved at each time-steps. Therefore,
we can use the tools put in place to solve linear systems in MANTA to implement such
an algorithm.

The current implementation is based on three elements:

- Creation of a `LinearSystem`.
- Filling the *LHS* and *RHS*, done by the `Formulation`.
- Solving the linear system to find the correction field.
- Adding the correction field to the primal field done by `Algorithm`.

To add other non linear behaviours to MANTA, one needs to create `Formulation`
objects that contain the right equation terms (for instance, a residual in the *RHS*
and a tangent matrix in the *LHS*).
