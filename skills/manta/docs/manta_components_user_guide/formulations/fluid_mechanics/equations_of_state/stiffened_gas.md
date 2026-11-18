<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/formulations/fluid_mechanics/equations_of_state/stiffened_gas.html -->

# Stiffened gas equation of state

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

## `StiffenedGasEOS`

The `StiffenedGas` EOS is a simple relation describing condensed matter
(liquid) when compressibility can be assumed (high pressure, shocks, underwater
explosions). It can be viewed as an extension of the `PerfectGas` EOS for
liquids. It takes into account thermal agitation and molecular attraction.
Details about this EOS can be found in [[LMMS04](../../../../references/references.md#id39)].

It writes:

\[p = (\gamma - 1)\rho (e - q) - \gamma p_{\infty}\]

with :

- [Mandatory] \(\gamma\) the heat capacity ratio : \(\gamma = \frac{c_p}{c_v}\).
- [Mandatory] \(p_{\infty}\) characterizing the molecular attraction within the liquid.
- [Optional] \(q\) the heat bond, characterizing the thermal agitation.

  - Default value: \(q = 0\).

## Example of usage

- Include:

```c++
#include "manta/components-fvm_compressible_fluid_mechanics/eos.h"
```

- Constructor:

```c++
    StiffenedGasEOS eos(gamma, pi);
```
