<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/formulations/fluid_mechanics/equations_of_state/isothermal_fluid.html -->

# Isothermal fluid equation of state

An equation of state (EOS) is a relation linking thermodynamic variables, and is
necessary to close the equations system. It characterizes each fluid and usually
comes with many assumptions and a domain of validity. EOS parameters are to be
provided by the user. For some fluids, an analytical relation cannot be provided
and the EOS is then tabulated (e.g. the steam/water EOS).

Every analytical EOS implemented in MANTA is linking the following
three variables :

- density \(\rho\),
- pressure \(p\),
- specific internal energy \(e\).

Equations of state can sometimes be found in literature using temperature
\(T\) instead of \(e\) or specific volume \(v = \frac{1}{\rho}\).

## `IsothermalFluidEOS`

This equation of state characterizes an isothermal fluid, with a liquid
behavior. The sound speed is considered constant.

It writes:

\[p = p_{ini} + (\rho - \rho_{ini}) * c^2\]

with :

- [Mandatory] \(c\) the isothermal speed of sound, a constant.
- [Mandatory] \(p_{ini}\), the initial pressure.
- [Mandatory] \(\rho_{ini}\), the corresponding initial density.
- [Optional] \(p_{min}\), the minimum pressure.

  - Default value: \(p_{min} = 0\)

## Example of usage

- Include:

```c++
#include "manta/components-fvm_compressible_fluid_mechanics/eos.h"
```

- Constructor:

```c++
    IsothermalFluidEOS eos(c, p0, rho0);
```
