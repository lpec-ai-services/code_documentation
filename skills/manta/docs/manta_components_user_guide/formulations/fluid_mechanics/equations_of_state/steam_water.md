<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/formulations/fluid_mechanics/equations_of_state/steam_water.html -->

# Steam / Water equation of state

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

## `EPXTabulatedWater` equation of state

This equation of state characterizes liquid water and its vapor as an
homogeneous mixture in thermodynamic equilibrium (same pressure / temperature).
Hence the mixture is treated as a single-component fluid.

The relations between thermodynamic variables are stored within tables. The
implementation was extracted from [EUROPLEXUS](http://www-epx.cea.fr/) and
steam/water tables originated from a joint publication of the US National Bureau
of Standards and the Canadian National Research Council, referenced in
[[HGK84](../../../../references/references.md#id72)]. These tables work by computing the evolution of pressure and
temperature by providing increments of specific volume and enthalpy.

The tabulated nature of the EOS implies that there is no analytical relationship
between thermodynamic variables. Setting the EOS implies initializing the
tables, and thus giving the pressure and temperature ranges as well as the
number of intervals to decompose pressure and temperature.

Water tables are initialized by giving a `Parameters` structure called
`WaterTablesSettings`, that can be constructed on the fly in the main cpp
file or in the input_data.json file:

```JSON
{
  "WaterTablesSettings" :
 {
  "extended"       : false,
  "temp_min"       : 3,
  "temp_max"       : 800,
  "press_min"      : 0.01e5,
  "press_max"      : 250e5,
  "l_coeff"        : 1,
  "m_coeff"        : 1,
  "n_split_low_t"  : 50,
  "n_split_high_t" : 50,
  "n_split_psat"   : 200,
  "n_split_phyper" : 50
 },

}
```

And in the main cpp file:

```c++
  const auto parameters          = readJSONDataFile(ctx, "input_data_hem.json");
  const auto waterTablesSettings = get<Parameters>(*parameters, "WaterTablesSettings");

  const auto extended       = get<Bool>(waterTablesSettings, "extended");
  const auto temp_min       = get<Real>(waterTablesSettings, "temp_min");
  const auto temp_max       = get<Real>(waterTablesSettings, "temp_max");
  const auto press_min      = get<Real>(waterTablesSettings, "press_min");
  const auto press_max      = get<Real>(waterTablesSettings, "press_max");
  const auto l_coeff        = get<Real>(waterTablesSettings, "l_coeff");
  const auto m_coeff        = get<Real>(waterTablesSettings, "m_coeff");
  const auto n_split_low_t  = get<Int>(waterTablesSettings, "n_split_low_t");
  const auto n_split_high_t = get<Int>(waterTablesSettings, "n_split_high_t");
  const auto n_split_psat   = get<Int>(waterTablesSettings, "n_split_psat");
  const auto n_split_phyper = get<Int>(waterTablesSettings, "n_split_phyper");

  EPXTabulatedWaterEOS eos_eau(extended,
                               temp_min,
                               temp_max,
                               press_min,
                               press_max,
                               l_coeff,
                               m_coeff,
                               n_split_low_t,
                               n_split_high_t,
                               n_split_psat,
                               n_split_phyper);
```

Parameters are:

- [optional] `extended` is a boolean to use the base version (\(T \in [0°C,
  800°C] ; P \in [0.0062 bar, 1000 bar]\)) or the extended version (\(T \in
  [0°C, 2000°C] ; P \in [0.0062 bar, 30000 bar]\)), default = false;
- [mandatory] `temp_min` (in °C), `temp_max` (in °C), `press_min`
  (in Pa), `press_max` (in Pa) the pressure and temperature ranges;
- [optional] `n_split_low_t`: number of intervals in low temperature area, default = 50;
- [optional] `n_split_high_t`: number of intervals in high temperature area, default = 50;
- [optional] `n_split_psat`: number of intervals in saturation pressure curve, default = 50;
- [optional] `n_split_phyper`: number of intervals in hypercritical pressure area, default = 50;
- [optional] `l_coeff` (length coefficient) and `m_coeff` (mass coefficient) are
  parameters in the water tables implementation to change units for length
  (meter by default) or mass (kg by default). This is unavailable for now in
  MANTA and changing these parameters will not have any effect. They should be
  ignored or left equal to 1.

Note

Temperatures to set the tables must be given in degrees Celsius, and pressures in Pascal.

Setting initial values for the model is trickier than other EOS. A
`waterstate` field is needed to store additional thermodynamic variables.
This field is then available for post-processing. It has 11 components, some
being redundant with classical conservative or primitive variables:

- pressure (\(Pa\)): 0
- density (\(kg/m^3\)): 1
- soundSpeed (\(m/s\)): 2
- vapor mass fraction: 3
- temperature (\(°C\)): 4
- specific enthalpy (\(J/kg\)): 5
- void fraction: 6
- specific volume remaining (\(kg^{-1}\)): 7
- specific enthalpy remaining (\(J/kg\)): 8
- \(\frac{p}{\rho}\) remaining (\(J/kg\)): 9
- specific internal energy (\(J/kg\)): 10

At each time step, obtaining actualized pressure and temperature is an iterative
process. Inputs are increments of specific volume and enthalpy, and the
algorithm tries to determine the pressure and temperature evolution that consume
a maximum of these increments. The remaining (small) fraction is kept and
reinjected for next time step.

In order to set an initial state in a domain, the user need to provide the
initial pressure, temperature and vapor mass fraction. Here is an example for
properly setting the fields in a 2D shocktube:

```c++
  Matrix<nVar, 1> leftState;
  Matrix<nVar, 1> rightState;
  ColVector<EOS::nInternalVariables> leftWaterState;
  ColVector<EOS::nInternalVariables> rightWaterState;

  Real rhoL(0), rhoR(0), rhoeL(0), rhoeR(0);
  auto s = eos.setInitialState(ctx, leftWaterState, rhoL, rhoeL, pL, tL, xvapL);
  s.update(eos.setInitialState(ctx, rightWaterState, rhoR, rhoeR, pR, tR, xvapR));
  if (!s) {
    Message::error(ctx.getErrorMessage());
  }

  // state initialisation
  leftState(0)  = rhoL;
  leftState(1)  = rhoL * vxL;
  rightState(0) = rhoR;
  rightState(1) = rhoR * vxR;

  if constexpr (geoDim == 2) {
    const auto vyL = get<Real>(inputs, "vyL");
    const auto vyR = get<Real>(inputs, "vyR");
    leftState(2)   = rhoL * vyL;
    leftState(3)   = rhoeL + rhoL * (vxL * vxL + vyL * vyL);
    rightState(2)  = rhoR * vyR;
    rightState(3)  = rhoeR + rhoR * (vxR * vxR + vyR * vyR);
  }
  else if constexpr (geoDim == 3) {
    const auto vyL = get<Real>(inputs, "vyL");
    const auto vzL = get<Real>(inputs, "vzL");
    const auto vyR = get<Real>(inputs, "vyR");
    const auto vzR = get<Real>(inputs, "vzR");
    leftState(2)   = rhoL * vyL;
    leftState(3)   = rhoL * vzL;
    leftState(4)   = rhoeL + rhoL * (vxL * vxL + vyL * vyL + vzL * vzL);
    rightState(2)  = rhoR * vyR;
    rightState(3)  = rhoR * vzR;
    rightState(4)  = rhoeR + rhoR * (vxR * vxR + vyR * vyR + vzR * vzR);
  }
  else {
    return ctx.registerErrorMessage("wrong dimension");
  }
  U.setValue(leftState, mesh.getSet("hp"));
  U.setValue(rightState, mesh.getSet("lp"));
  waterState.setValue(leftWaterState, mesh.getSet("hp"));
  waterState.setValue(rightWaterState, mesh.getSet("lp"));
```
