<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/algorithms_and_numerics/time_integrators/time_integrators.html -->

# Notions on time integrators

A time integrator aims at solving an Initial Value Problem numerically by:

1. discretizing the time \(t\) in time intervals \({t_{0}, ... t_{n}, t_{n+1}, ...}\)
bounded by discrete values of times. The value between two consecutive time is called "time-step":
\(\Delta t_{n+1} = t_{n+1} - t_{n}\).
Note that "time-step" sometimes also refer to the state at the end of the interval.

2. proposing some recurrence formulas to advance from a given time-step to the next one
(single step advance are considered here) which may be explicit for some variables (\(X_{n+1} = f(X_{n},Y_{n},...)\))
or implicit.

This page describes how to use the `TimeIntegrator` class.

## General example of usage

For a linear system `feSystem` linked to a formulation:

```c++
auto &feSystem = rm.make<DiagonalLinearSystem>("FESystem", mesh);
CentralDifferenceTimeIntegrator timeIntegrator(feSystem, {Uvar, {U, V, G}});
```

As differential equation are involved, `Fields` representing time-derivative
must be provided by the user prior to the construction of a time integrator.
For instance, a mechanical 3D finite elements model using the explicit
`TimeIntegrator` requires the displacement, velocity and acceleration fields,

In the previous snippet, `Uvar` is the *dof var* associated with the
degrees of freedom that `U`, `V` and `G` all relate to (there is no
automatic way to infer it, it must always be given explicitly).

The arguments expects an array of pairs of a *dof var* and a vector of
fields, for formulations where translations and rotations are separated:

```c++
auto &feSystem = rm.make<DiagonalLinearSystem>("FESystem", mesh);
CentralDifferenceTimeIntegrator timeIntegrator(feSystem, {{Uvar, {U, V, G}}, {Rvar, {R, W, Q}}});
```

Several optional constructor arguments are available:

- `.increments` : to provide and store increment fields.
- `.updateCoordinateField` : to provide the field driving mesh movement
- `.beforeAssemble` : to provide a method called before the assembling stage
- `.qsDampingBeta` : to provide the reduced damping coefficient \(\beta\) for *mass-proportional* quasi-static damping.
- `.qsDampingFrequency` : to provide the target mode frequency \(f\) (Hz) of the structural mode to damp out.

Note

The number of increment fields must be the same as the number of groups of inputted fields,
e.g. in the previously quoted code, one would need to define two increment fields.

Here is another example used with a beam formulation:

```c++
CentralDifferenceTimeIntegrator timeIntegrator(
    feSystem, {{Uvar, {U, V, G}}, {Rvar, {R, W, Q}}}, {.updateCoordinatesField = dU, .increments = {dU, dR}});
```

Other specific time integrators are described further [in this list of available time integrators](#list-time-integrators).

## Usual methods

Users will usually use two methods of `TimeIntegrators` :

- `advanceOneStep` method which shall call the assemble, solve, updateField triad.
- `computeNextTimeStep` method which adaptively compute the time-step

Here is an example of the use of those methods:

```c++
dt = timeIntegrator.computeNextTimeStep(ctx);
ExitStatus oneStep = timeIntegrator.advanceOneStep(ctx, dt);

if(oneStep.shallStop()){
    Message::error(ctx.getErrorMessage());
}
```

## List of available time integrators

Classic time integrators:

- `CentralDifferenceTimeIntegrator` : speed at half time step
- `CentralDifferenceTimeIntegrator2` : no half time steps

Contact/friction time integrators:

- `CentralDifferenceWContactTimeIntegrator` : speed at half time step
- `CentralDifferenceWContactTimeIntegrator2` : no half time steps
- `CentralDifferenceWFrictionTimeIntegrator`

Finite volume time integrators:

- `ForwardEulerFVTimeIntegrator`
- `MusclHancockFVTimeIntegrator`
- `RungeKutta2FVTimeIntegrator`

Phase-field time integrators:

- `PhaseFieldHeunTimeIntegrator`
- `PhaseFieldSubCyclingTimeIntegrator`
- `PhaseFieldRegularizedTimeIntegrator`: for an hyperbolic phase-field model

## Specific example of usage

### Contact and Friction time integrators

For contact and friction specific time integrators,
one shall also provide constraint sets and friction model
(more information can be found [this section](../contact/contact.md#contact-example).)

```c++
CentralDifferenceWContactTimeIntegrator timeIntegrator(feSystem, {U, V, G}, Uvar, {contactCSet});
CentralDifferenceWFrictionTimeIntegrator timeIntegrator(feSystem, {U, V, G}, Uvar, frictionModel);
```

### Finite Volume time integrators

For finite volume time integrators, one needs to provide the [cfl](../../../theory_manual/fluid_mechanics/cfl_stability_factor_estimate.md#cfl-stability-factor-estimate).

```c++
ForwardEulerFVTimeIntegrator timeIntegrator(linearSystem, U, Uvar, cfl);
MusclHancockFVTimeIntegrator timeIntegrator(linearSystem, U, Uvar, cfl);
```

To link formulations to the time integrators, one can use the `addFormulation`
method.

### Phase field time integrators

A more specific page about phase-field time integrators is available in [this page](pf_time_integrators.md#pf-time-integrator).

Phase-field time integrator rely on a staggered phase-field implementation. Therefore one
needs to define a mechanics time integrator, that shall be called in an internal staggered scheme.
Here are the three available phase-field time integrators with their given input arguments:

- A damage explicit formulation
- A linear system linked to this formulation
- The damage field which is updated by the scheme
- A time integrator linked to the time discretization of a mechanical problem.
- `cfl` for the subcycling phase field time integrator
- `tau` for the regularized phase field time integrator (linked to a hyperbolic phase field model)

```c++
PhaseFieldHeunTimeIntegrator timeIntegrator(
    damageExplicitForm, dSystem, D, Dvar, CentralDifferenceTimeIntegrator(uSystem, {Uvar, {U, V, G}}));

PhaseFieldSubCyclingTimeIntegrator timeIntegrator(
    damageExplicitForm, dSystem, D, Dvar, cfl, CentralDifferenceTimeIntegrator(uSystem, {Uvar, {U, V, G}}));

PhaseFieldRegularizedTimeIntegrator timeIntegrator(
    damageExplicitForm, dSystem, D, Dvar, tau, CentralDifferenceTimeIntegrator(uSystem, {Uvar, {U, V, G}}));
```

### Quasi-Static Damping

To filter high-frequency oscillations, mass-proportional quasi-static damping is available.

This damping is exclusively available for:

- `CentralDifferenceTimeIntegrator`
- `CentralDifferenceTimeIntegrator2`

#### Theoretical formulation

The damping force added to the right-hand side (RHS) of the equations of motion is:

(26)\[F_i^{\text{QS}} = -C_d M_i v_i\]

where:

- \(C_d = 4 \pi \beta f\) is the damping coefficient, with \(\beta\) being the reduced damping coefficient and \(f\) the target structural mode frequency.
- \(M_i\) is the lumped (diagonal) mass on DOF \(i\).
- \(v_i\) is the nodal velocity on DOF \(i\).

Thus, the equations of motion read:

(27)\[M_i a_i + C_d M_i v_i = F_i^{\text{ext}} - F_i^{\text{int}}\]

where:

- \(a_i\) is the damped nodal acceleration on DOF \(i\).
- \(F_i^{\text{ext}}\) is the external nodal forces on DOF \(i\).
- \(F_i^{\text{int}}\) is the internal nodal forces on DOF \(i\).

By dividing by the lumped mass \(M_i\), the mass term cancels out completely. The damped acceleration is:

(28)\[a_i = a_i^{\text{undamped}} - C_d v_i\]

where \(a_i^{\text{undamped}} = \frac{F_i^{\text{ext}} - F_i^{\text{int}}}{M_i}\) is the undamped nodal acceleration.

The velocity is updated at the end of each step of size \(\Delta t_{\text{velocity}}\):

(29)\[v_{n+1} = v_{n+1/2} + \Delta t_{\text{velocity}} a_{n+1}\]

where:

- \(v_{n+1/2}\) is the half-step nodal velocity.
- \(v_{n+1}\) is the next step nodal velocity.
- \(a_{n+1}\) is the next step nodal damped acceleration.
- \(\Delta t_{\text{velocity}}\) is the effective time step size used for the velocity update.

Substituting this velocity into equation [(28)](#equation-qsdamping-acceleration) at step \(n+1\) yields:

(30)\[\begin{split}a_{n+1} = a_{n+1}^{\text{undamped}} - C_d (v_{n+1/2} + \Delta t_{\text{velocity}} a_{n+1}) \\
a_{n+1} (1 + C_d \Delta t_{\text{velocity}}) = a_{n+1}^{\text{undamped}} - C_d v_{n+1/2}\end{split}\]

where:

- \(a_{n+1}\) is the next step nodal damped acceleration.
- \(a_{n+1}^{\text{undamped}}\) is the next step nodal undamped acceleration.

This gives the final correction for the acceleration:

(31)\[\boxed{a^{\text{damped}} = \frac{a^{\text{undamped}} - C_d v}{1 + C_d \Delta t_{\text{velocity}}}}\]

Note

Consider [(27)](#equation-qsdamping-motion) without external force (\(F_i^{\text{ext}} = 0\)) and with the internal force written as \(F_i^{\text{int}} = K_i u_i\) (\(K_i\) is the nodal stiffness, \(u_i\) is the nodal displacement on DOF \(i\)). Then, [(27)](#equation-qsdamping-motion) reduces to:

\[M_i a_i + C_d M_i v_i + K_i u_i = 0\]

Dividing by the mass \(M_i\), it leads to:

(32)\[a_i + C_d v_i + \omega_n^2 u_i = 0\]

where \(\omega_n = \sqrt{K_i / M_i} = 2 \pi f\) is the natural angular frequency and \(f\) is the target structural (natural) mode frequency introduced in [(26)](#equation-qsdamping-force).

The characteristic equation of [(32)](#equation-qsdamping-motion2) is \(r^2 + C_d r + \omega_n^2 = 0\). Its roots are complex (oscillations) when \(C_d < 2 \omega_n\) and real (no oscillations) otherwise. The limit case is the critical damping \(C_{\text{crit}} = 2 \omega_n\) and \(C_d\) can be written as follows:

\[C_d = \beta C_{\text{crit}}\]

In consequence, depending on the value of \(\beta\), 3 regimes are obtained:

- \(\beta < 1\): under-damped (return to equilibrium with oscillations)
- \(\beta = 1\): critically damped (fastest return to equilibrium without oscillations)
- \(\beta > 1\): over-damped (return to equilibrium without oscillations)

#### Example of usage

The parameters can be passed to the constructor as follows:

```c++
  CentralDifferenceTimeIntegrator timeIntegrator(feSystem,
                                                 {{Utranvar, {Wtran, Vtran, Utran}}, {Urotvar, {Wrot, Vrot, Urot}}},
                                                 {.qsDampingBeta = qsbeta, .qsDampingFrequency = qsfrequency});
```
