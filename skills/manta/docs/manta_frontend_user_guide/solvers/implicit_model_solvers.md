<!-- source: https://manta-project.gitlab.io/manta/manta_frontend_user_guide/solvers/implicit_model_solvers.html -->

# Solvers for implicit models

Depending on the case, implicit models may have to solve either:

- a linear system of the form:

  (14)\[ \mathbb{K}\paren{\ets{\v{u}}} = \v{F}_{e}\]

  where \(\mathbb{K}\) is the stiffness matrix,
  \(\v{F}_{e}\) is the external forces and
  \(\ets{\v{u}}\) is the value of the unknown
  field at the end of the time step.
- a nonlinear system of equations of the form:

  (15)\[ \mathbb{R}\paren{\ets{\v{u}}} = 0\]

  where \(\mathbb{R}\) is the residual and \(\ets{\v{u}}\)
  is the value of the unknown field at the end of the time step.

Depending on the physics described by the model, the unknown field can
contain the displacement (mechanics), the temperature (heat-transfer),
etc... The unknown field may also contain Lagrange multpliers (See
Section [Imposing constraints on unknowns](../miscellaneous/constraints/constraints.md#imposing-constraints-on-unknowns)).

## Available algorithms

### The `Linear` solver

The `Linear` solver is meant to solve Equation
[(14)](#equation-manta-user-guide-implicit-model-solvers-linear-system).

#### Example of usage

PYTHON

```python
# creating the mechanical model
m = manta.Model('ImplicitMechanics', ps, linearSolver = {})
```

C++

```c++
// solid materials
auto m = mf.create(ctx, "ImplicitMechanics", ps,
                   Parameters{{"linearSolver", Parameters{}}});
```

### The `Newton` solver

The `Newton` solver is meant to solve System
[(15)](#equation-manta-user-guide-implicit-model-solvers-residual) using the
classical Newton algorithm.

#### Example of usage

PYTHON

```python
# creating the mechanical model
m = manta.Model('ImplicitMechanics', ps,
                solver = {'Newton': {'maximumNumberOfIterations', 10}})
```

C++

```c++
// solid materials
auto m = mf.create(ctx, "ImplicitMechanics", ps,
                   Parameters{{"solver",
                               Parameters{{"Newton", Parameters{"maximumNumberOfIterations", 10}}}}});
```

#### The Newton algorithm

System [(15)](#equation-manta-user-guide-implicit-model-solvers-residual) is solved
incrementally by successive approximations \(\v{u}^{(n)}\) (where
\(n\) is the number of the current iteration) of the solution
\(\ets{\v{u}}\) using the following rule:

(16)\[\v{u}^{(n+1)} = \v{u}^{(n)}-\left(\pdfrac{\mathbb{R}}{\v{u}}\right)^{-1}\,\mathbb{R}\paren{\v{u}^{(n)}}\]

#### Convergence criteria

Two convergence criteria can be considered:

- The first criterion is satisfied if the norm
  \(\norm{\mathbb{R}\paren{\v{u}^{(n)}}}\) is lower than a given
  tolerance \(\varepsilon_{a}\).
- The second criterion is satisfied if the relative value
  \(\frac{\norm{\mathbb{R}\paren{\v{u}^{(n)}}}}{\norm{\mathbb{R}\paren{\v{u}^{(0)}}}}\)
  is lower than a given tolerance \(\varepsilon_{r}\).

By default, the test on the relative value
\(\frac{\norm{\mathbb{R}\paren{\v{u}^{(n)}}}}{\norm{\mathbb{R}\paren{\v{u}^{(0)}}}}\)
is used.

#### Parameters

The following parameters can be passed to the Newton solver:

- `convergenceTest`: string allowing to select the convergence
  test used. The following values are currently supported:
  `relative` (default), `absolute`,
  `absoluteOrRelative` or `absoluteAndRelative`.
- `thresholdOnTheFirstResidualNorm`: threshold used to test if
  the first residual is null. Default value is \(1e-15\).
- `maximumNumberOfIterations`: maximum number of iterations of
  the Newton algorithm. Default value is \(10\).
- `convergenceTolerances`: dictionary containing the list of
  convergence tolerances. Two entries are expected:

  - `relativeConvergenceTolerance`: tolerance
    \(\varepsilon_{r}\) used if a test on the relative value of the
    norm of the residual is used. Default value is \(1e-5\).
  - `absoluteConvergenceTolerance`: tolerance
    \(\varepsilon_{a}\) used if a test on the absolute value of the
    norm of the residual is used. Default value is \(1e-15\).
- `linearSolver`: parameters passed to the underlying linear
  solver -- see the [linear solver interface](../../manta_components_user_guide/main_user_concepts/user_guide_objects/linear_solver_interface.md#linear-solver-interface).
- `reportResidualNorms`: boolean stating if the evolution of the
  absolute and relative values of the norm of the residual during the
  Newton iterations must be stored in the output of the solver (see
  [Monitoring a simulation](../miscellaneous/simulation_monitors.md#user-guide-simulation-monitors)).
- `switchFromRelativeToAbsoluteCriterion`: boolean stating if the
  solver switches from a relative criterion to an absolute criterion at
  the second call of the solver for the same time step. If this option
  is enabled, only the relative tolerance must be defined. By default,
  this switch is not enabled. This parameter is only meaningful if the
  `convergenceTest` parameter is set to `relative`.
