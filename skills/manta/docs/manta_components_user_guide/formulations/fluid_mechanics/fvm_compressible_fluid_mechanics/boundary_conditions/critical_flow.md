<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/formulations/fluid_mechanics/fvm_compressible_fluid_mechanics/boundary_conditions/critical_flow.html -->

# `CriticalFlow` boundary condition

The `CriticalFlow` boundary condition characterizes a critical flow boundary
condition. It corresponds to imposing the properties of a fluid that goes through
an opening at the end of pipe line into what is assumed to be a large volume.
Depending on the upstream and downstream conditions, the fluid can be in different
states at the opening. The current `CriticalFlow` boundary condition
is only valid for `PerfectGasEOS` and `IsothermalFluidEOS`.

Theoretical considerations are detailed [here](../../../../../theory_manual/fluid_mechanics/critical_flow.md#critical-flow-theory).

The critical flow boundary conditon in MANTA is only valid for wireframe
models where the Finite Volumes framework is used to solve the Compressible
Euler equations (MANTA's corresponding formulation is
`EulerExplicitPipeFormulation`). It is called
`CriticalFlowBoundaryConditionPerfectGas` or
`CriticalFlowBoundaryConditionIsothermalFluid` (depending on the equation
of state) and is implemented in `euler_boundary_conditions.h`. It must be
added to a previously defined Euler explicit formulation via `addBc`.

## Transient regime

In the [theory](../../../../../theory_manual/fluid_mechanics/critical_flow.md#critical-flow-theory), we always considered the case of an
established steady-state flow. It is therefore necessary to add a new assumption
to treat the transient regime. We will assume that the pressure at the break is
the same in both the transient and the steady-state regimes. The fluid will be
progessively accelerated until its velocity reaches the one corresponding the
steady-state mass flow rate.

## Break ratio

The break ratio \(r\) is still defined as :

\[r = \frac{A_0}{A_1}\]

with \(A_0\) the break area and \(A_1\) the upstream pipe cross section
area. \(r\) can lie between \(0\) and \(1\) (included). If the user
specifies a zero break ratio, a minimum ratio of \(r=10^{-6}\) is used in MANTA.

## Examples of usage

Include:

```c++
#include "manta/components-fvm_compressible_fluid_mechanics/euler_boundary_conditions.h"
```

The boundary condition is added to the Euler formulation through the
`addBc` method. It takes the Boundary condition type as template parameter
and takes as arguments the BC parameters.

```c++
    fluxForm.addBc<CriticalFlowBoundaryCondition<geoDim, nVar, EOSType>>(ctx, facets, eos, breakRatio, pRef, pExt, opts);
```

## Input parameters

- **Template parameters**:

  > - `geoDim`: space dimension of the cells
  > - `nVar`: number of state variables
  > - `EOSType`: type of the `eos` parameter
- **Constructor parameters**:

  - `facets` : Boundary condition element
  - `eos` : Equation of state
  - `breakRatio` : Ratio between the break area and the pipe section area
  - `pRef` : Reference pressure
  - `pExt` : External pressure
  - `Options` : set of options (depend on the equation state)

    > - `verbosityLevel` : Verbosity level (similar to
    >   :   `VerbosityLevel::verboseDebug`), prints debug information if its
    >       value is set \(\geq 4\))
    > - `ksi` : User-defined head loss coefficient that overrides the default
    >   :   value taken from [[Idelcik69](../../../../../references/references.md#id56)] (\(\left(1 + 0.707 \sqrt{1 - \mathrm{breakRatio}}\right)^2\))
    > - `lowPressureEpsilon` (`PerfectGasEOS` only): Small value \(\varepsilon_{LP}\) that
    >   :   controls the transition between Bernouilli regime (low pressures
    >       differences) and subsonic/critical regimes (default 0.001). In practice,
    >       if \(P_2 > P_1 + \varepsilon_{LP} \rho_1 C_1^2\), the pressure
    >       difference is considered small enough to apply Bernouilli's law. If not,
    >       the critical flow algorithm is called.
    > - `criticalRegimeEpsilon` (`PerfectGasEOS` only): Small value \(\varepsilon_{CR}\) that
    >   :   controls the imposed pressure in the critical regime (default 0.01). In
    >       practice, if \(P_c > P_1 + \varepsilon_{CR} P_1\), the computed
    >       critical pressure is superior to the upstream pressure and cannot be
    >       imposed. Bernouilli's law is applied instead.

Note

If a constant value is given for the `breakRatio` or `pExt` parameter,
i.e. if the parameter is not a variable that has been declared outside of the
`rm.make` function, then that parameter will not be able to
be altered after the boundary condition declaration.

However, if a previously declared variable is given, then that parameter
in the boundary condition will exactly follow the value of that
variable. This feature makes it possible to model the time-dependent evolution
of the breach opening (for `breakRatio`) or of the external pressure (for `pExt`).
