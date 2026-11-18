<!-- source: https://manta-project.gitlab.io/manta/manta_frontend_user_guide/models/solid_mechanics/implicit_solid_mechanics.html -->

# The `ImplicitMechanics` model

This page describes the `ImplicitMechanics` model. The theory
behind this model can be found in various classical textbooks of
computational mechanics, including
[[Bel00](../../../references/references.md#id29), [BCC+09](../../../references/references.md#id28), [dSNPO08](../../../references/references.md#id30)].
The mathematical aspects of the method, with some applications to
mechanics, can be found in the course of Fortin et al.
[[FG20](../../../references/references.md#id27)].

## Example of usage

```python
    model = manta.Model(
        'ImplicitMechanics', 
        ps, 
        linearSolver = {}
    )
```

## Parameters

The model takes in the following parameters:

- (*optional*) Any combination of those three parameters. They should
  contain a vector of dictionaries describing bricks that will be added
  to the model. Equivalent to an *a posteriori* call to the `add` method.
  Defaults to an empty vector.

  - `boundaryConditions`
  - `structures`
  - `bricks`
- (*optional*) At most one of these parameters. Defaults to the default value of
  `nonlinearSolver`.

  - `linearSolver`: Dictionary describing a linear solver (see
    [Solvers for implicit models](../../solvers/implicit_model_solvers.md#manta-user-guide-implicit-model-solver)) ;
  - `solver` or `nonlinearSolver`: Dictionary describing a nonlinear solver,
    (see [Solvers for implicit models](../../solvers/implicit_model_solvers.md#manta-user-guide-implicit-model-solver)) ;
- (*optional*) `verbosityLevel`: verbosity level. Possible values are: `quiet`,
  `level0`, `level1`, `level2`, `level3`, `debug` and `full`. The default
  value is the one given via the `manta.setDefaultVerbosityLevel` method.

## Physical description

This model aims at determining the displacement field \(\ets{\v{u}}\) at the
end of a time step by solving a non linear system of the form:

(3)\[ \mathbb{R}\paren{\ets{\v{u}}} = 0\]

In quasi-statics, the residual \(\mathbb{R}\) is defined by
discretizing the principle of virtual power/work (see below) and can be
decomposed as the substraction of the external forces and the inner
forces:

(4)\[ \mathbb{R}\paren{\ets{\v{u}}} = \mathbb{F}_{e}\paren{\ets{\v{u}}} - \mathbb{F}_{i}\paren{\ets{\v{u}}}\]

At equilibrium, i.e. when Equation
[(3)](#equation-manta-user-guide-implicit-mechanics-residual) is fulfilled, the
external forces \(\mathbb{F}_{e}\) and the inner forces
\(\mathbb{F}_{i}\) are equal.

In MANTA, the residual \(\mathbb{R}\) is computed by summing the
contributions of bricks.

In dynamics, the residual is augmented by inertial contributions.

Warning

Dynamics are not yet implemented in implicit mechanics.
