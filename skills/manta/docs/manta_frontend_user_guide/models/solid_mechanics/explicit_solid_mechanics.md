<!-- source: https://manta-project.gitlab.io/manta/manta_frontend_user_guide/models/solid_mechanics/explicit_solid_mechanics.html -->

# The `ExplicitMechanics` model

This page describes the `ExplicitMechanics` model, which corresponds to mechanics
problems which are explicitly integrated in time.

## Example of usage

```python
    model = manta.Model(
        'ExplicitMechanics', 
        ps, 
        kinematicDescription = 'Lagrangian',
    )
```

## Parameters

The model takes in the following parameters:

- (*optional*) `bricks`: Vector of dictionaries describing bricks that
  will be added to the model. Equivalent to an *a posteriori* call to the `add` method.
  Defaults to an empty vector.
- (*optional*) `qsDampingBeta`: reduced damping coefficient \(\beta\) for
  *mass-proportional* quasi-static damping.
- (*optional*) `qsDampingFrequency`: target mode frequency \(f\) (Hz) of the
  structural mode to damp out.
- (*optional*) `kinematicDescription`: Kinematic description (Lagrangian or
  corotational formulation).

  - `Lagrangian` or `lagrangian` (*default*): Total Lagrangian formulation.
    Equations are formulated
    with respect to a fixed reference configuration. Stresses are computed in this
    reference configuration with the total displacement. This formulation should
    be used for small displacements and small rotations.
  - `Corotational` or `corotational`: Corotational formulation. In this
    formulation, stresses are computed
    in a local frame rotating with the element. At each time (or pseudo-time) step,
    the increment of strain is computed from the increment of displacement.
    By applying the constitutive law, the increment of stress is obtained. Stresses
    are then updated by adding the increment of stress to the stress at previous
    time step. This formulation should be used for large displacements and large
    rotations.
- (*optional*) `verbosityLevel`: verbosity level. Possible values are: `quiet`,
  `level0`, `level1`, `level2`, `level3`, `debug` and `full`. The default
  value is the one given via the `manta.setDefaultVerbosityLevel` method.

## Physical description

This model aims at determining the displacement field \(\v{u}\) and its first
and second time derivatives of mechanical problems, using an explicit time integration
scheme. The model solves a (*potentially*) non linear system of the following form:

(1)\[ \mathbb{R}\paren{\ddot{\v{u}}, \dot{\v{u}}, \v{u}} = 0\]

which is is usually written:

(2)\[\mathbb{M} \ddot{\v{u}} = \mathbb{F}_e\paren{\v{u}, \dot{\v{u}}} - \mathbb{F}_i\paren{\v{u}, \dot{\v{u}}}\]

where \(\mathbb{M}\) is a **lumped** mass matrix, \(\mathbb{F}_e\) is the
external forces vector (which includes damping) and \(\mathbb{F}_i\) is the
inner forces vector.

At equilibrium, i.e. when Equation [(2)](#equation-manta-user-guide-explicit-mechanics-system)
is fulfilled, the inertial forces \(\mathbb{M} \ddot{\v{u}}\) are equal to
the difference between the external forces \(\mathbb{F}_{e}\) and the inner forces
\(\mathbb{F}_{i}\).

In MANTA, the residual \(\mathbb{R}\) is computed by summing the
contributions of bricks.

### Time integration

Time integration is done using a central-difference time integrator.

The critical time step that is used for the simulation is equal to the minimal
critical time step that was computed for each of the bricks that were added to
the model. It is then scaled down by a coefficient (usually called CFL) given
during the instantiation of the `Simulation` object (see the `criticalTimeStepSafetyCoefficient`
parameter described [here](../../simulation/simulation_class_overview.md#simulation-class-overview)).

Additionally, a *mass-proportional* quasi-static damping is available to filter out
high-frequency oscillations by specifying the `qsDampingBeta` and `qsDampingFrequency`
parameters. Theoretical aspects are described in [Quasi-Static Damping](../../../manta_components_user_guide/algorithms_and_numerics/time_integrators/time_integrators.md#quasi-static-damping).
