<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/formulations/fluid_mechanics/fvm_compressible_fluid_mechanics/boundary_conditions/tank.html -->

# `Tank` boundary condition

The `tank` boundary condition models the behavior of a tank for 1D flow
problems. It can only be used using the `EulerExplicitPipeFormulation`. A
tank is a particular boundary condition as it can rather be considered as a cell
itself. The tank has its own state \(\mathbf{U}_{tank}\), i.e. its own
density, pressure, and velocity. The tank is defined by a volume
\(V_{tank}\) that must be provided by the user, as well as the initial
pressure \(\rho_{tank}\) of the fluid of the tank. The user must also
provide the initial pressure of the tank \(p_{tank}\). As the `tank`
boundary condition is a non-dimensional cell modeling a 3D tank, the velocity
of its state has no physical meaning. The outside state is defined from the
inner state and the tank state as follows:

\[\begin{split}\left\{
\begin{array}{l}
\rho_{out} = \rho_{tank} \\
u_{out} = u_{in} \\
p_{out} = p_{tank}
\end{array}
\right.\end{split}\]

Knowing the outside state, and the inner state (the state of the adjacent cell,
in the pipe), the flux can be computed. The state of the tank is updated at each
time step after the computation of the numerical fluxes. As a tank can be
connected to multiple pipes, the contibution of each facet \(f\) is taken
into account to update the state of the tank at the next time step, using the
[time integrator](../../../../../theory_manual/fluid_mechanics/compressible_fluid_mechanics.md#euler-explicit-time-integrators). For instance, using a
forward Euler time integrator, the conservative state \(\mathbf{U}_{tank}\)
of the tank at the time step \(n+1\) is:

\[\mathbf{U}_{tank}^{n+1} = \mathbf{U}_{tank}^n - \frac{V_{tank} \Delta t}{S_f} F_f(\mathbf{U}_{in},\mathbf{U}_{out})^n\]

where \(S_f\) is the cross section of the pipe of the facet \(f\).

The `TankBoundaryCondition` is only relevant for wireframe models, i.e. it
should be used with `EulerExplicitPipeFormulation`. It is compatible with
any analytical Equation of State.

## Example of usage

Include:

```c++
#include "manta/components-fvm_compressible_fluid_mechanics/euler_boundary_conditions.h"
```

The boundary condition is added to the Euler formulation through the
`addBc` method. It takes the Boundary condition type as template parameter
and takes as arguments the BC parameters.

```c++
    fluxForm.addBc<TankBoundaryCondition<geoDim, nVar, EOSType>>(ctx, tank_boundary, eos_tank, VTank, rhoTank, pTank);
```

## Input parameters

- **Template parameters**:

  > - `geoDim`: space dimension of the cells
  > - `nVar`: number of state variables
  > - `EOSType`: type of the `eos` parameter
- **Constructor parameters**:

  - `tank_boundary`: the support meshSet of the boundary condition
  - `eos_tank`: an equation of state for the fluid in the tank, typically to define the relationship between pressure and density in the tank.
  - `VTank`: Volume of the tank
  - `rhoTank`: density of the fluid in the tank
  - `pTank`: pressure of the fluid in the tank
