<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/formulations/fluid_mechanics/fvm_compressible_fluid_mechanics/boundary_conditions/prescribed_outflow.html -->

# `PrescribedPressureOutflow` boundary condition

The `PrescribedPressureOutflow` boundary condition imposes a given
pressure. The outside state is copied from the inside state, except for the
pressure, which is the given pressure.

## Example of usage

Include:

```c++
#include "manta/components-fvm_compressible_fluid_mechanics/euler_boundary_conditions.h"
```

The boundary condition is added to the Euler formulation through the
`addBc` method. It takes the Boundary condition type as template parameter
and takes as arguments the BC parameters.

This boundary condition is valid for `PerfectGasEOS`,
`IsothermalFluidEOS` and `EPXTabulatedWaterEOS`. The influence of the
EOS is only relevant for Euler implicit formulations.

```c++
    fluxForm.addBc<PrescribedPressureOutflowBoundaryCondition<geoDim, nVar, EOSType>>(ctx, l_top, eos, p_imp);
```

## Input parameters

- **Template parameters** :

  > - `geoDim`: space dimension of the cells
  > - `nVar`: number of state variables
  > - `EOSType`: type of the `eos` parameter (for instance `IsothermalFluidEOS`)
- **Constructor parameters**

  > - `l_top`: the support `meshSet` of the boundary condition
  > - `eos`: the equation of state
  > - `p_imp`: the prescribed pressure

Note

If a constant value is given for the `p_imp` parameter, i.e. if the
parameter is not a variable that has been declared outside of the
`rm.make` function, then the prescribed pressure will not be able to
be altered after the boundary condition declaration.

However, if a previously declared variable is given, then the prescribed
pressure in the boundary condition will exactly follow the value of that
variable.
