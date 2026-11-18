<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/formulations/fluid_mechanics/equations_of_state/perfect_gas.html -->

# Perfect gas equation of state

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

## `PerfectGasEOS`

The `PerfectGas` EOS describes an ideal gas (that is neglecting electrostatic
interactions between molecules) with heat capacities (\(c_v\) at constant
volume and \(c_p\) at constant pressure) independant of temperature. This
law provides an excellent approximation for the behavior of actual gases at low
pressure.

It writes:

\[p = (\gamma - 1)\rho e\]

with:

- [Mandatory] \(\gamma\) the heat capacity ratio: \(\gamma = \frac{c_p}{c_v}\).

## Example of usage

- Include:

```c++
#include "manta/components-fvm_compressible_fluid_mechanics/eos.h"
```

- Constructor:

```c++
    PerfectGasEOS eos(gamma);
```
