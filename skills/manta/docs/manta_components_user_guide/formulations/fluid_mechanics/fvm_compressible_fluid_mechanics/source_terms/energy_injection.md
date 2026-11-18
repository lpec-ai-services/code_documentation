<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/formulations/fluid_mechanics/fvm_compressible_fluid_mechanics/source_terms/energy_injection.html -->

# Energy injection source term

For some problems, energy may need to be injected in water to simulate explosions, heating or boiling. In that case, the compressible Euler equations [(241)](../../../../../theory_manual/fluid_mechanics/compressible_fluid_mechanics.md#equation-euler-eq) become:

(25)\[\begin{split}\begin{aligned}
\frac{\partial \rho}{\partial t}
+ \nabla \cdot (\rho \mathbf{u})
&= 0, \\
\frac{\partial (\rho \mathbf{u})}{\partial t}
+ \nabla \cdot
\left(
\rho \mathbf{u} \otimes \mathbf{u} + p\mathbf{I}
\right)
&= \mathbf{0}, \\
\frac{\partial (\rho E)}{\partial t}
+ \nabla \cdot
\left(
(\rho E + p)\mathbf{u}
\right)
&= \frac{\dot{Q}}{V}.
\end{aligned}\end{split}\]

Here:

- \(Q\) is the total injected thermal energy (\(\text{J}\)).
- \(\dot{Q} = \frac{dQ}{dt}\) is the injected thermal power (\(\text{W}\)).
- \(V\) is the volume (\(\text{m}^3\)).
- \(\frac{\dot{Q}}{V}\) is the volumetric rate of energy injection (\(\text{W/m}^3\)).

Because the source term cannot be written in divergence form, the problem is
solved using a splitting method. At each time step, the problem is first solved
without the energy injection term. This corresponds to the classical problem
[(241)](../../../../../theory_manual/fluid_mechanics/compressible_fluid_mechanics.md#equation-euler-eq) and yields an intermediate conservative state
\(\mathbf{U}_{n+1}^{\star}\). Energy injection is then taken into account by
updating the conservative variable associated with the energy equation:

\[(\rho E)_{n+1} = (\rho E)_{n+1}^{\star} + \Delta t \, \frac{\dot{Q}_{n+1}^{\star}}{V_{n+1}}\]

## Computation of the injected thermal power \(\dot{Q}\)

The thermal power \(\dot{Q}\) injected depends on
the propagation delay, the temporal power modulation, and the chosen injection mode.

1. **Spatial propagation delay** (\(t_{\text{delay}}\))

   The energy release starts at a given location in the mesh
   \(\mathbf{x}_{\text{origin}}\) and moves through the domain
   at a prescribed characteristic speed \(c_{\text{propag}}\). For a given location \(\mathbf{x}\), this delay is:

   \[t_{\text{delay}}(\mathbf{x}) = \frac{\lVert \mathbf{x} - \mathbf{x}_{\text{origin}} \rVert}{c_{\text{propag}}}\]

   Before the arrival of the wave at location \(\mathbf{x}\) (\(t \le t_{\text{delay}}\)), no energy is injected (\(\dot{Q} = 0\)).
2. **Time-dependent power modulation** (\(P(t_{\text{rel}})\))

   The injected power is modulated by a (user-supplied) dimensionless function
   \(P(t_{\text{rel}})\), where \(t_{\text{rel}} = t - t_{\text{delay}}(\mathbf{x})\)
   is the local time elapsed since the wave arrival at location \(\mathbf{x}\).
   For \(t \le t_{\text{delay}}(\mathbf{x})\), \(\dot{Q} = 0\).

   Note

   The function is **not** called with the simulation time \(t\), but with
   \(t_{\text{rel}}\). The profile therefore restarts from \(t_{\text{rel}} = 0\)
   in each cell when the wave reaches it. For example, \(P(t_{\text{rel}}) = 100\, t_{\text{rel}}\)
   is zero at the wave arrival in every cell, whatever the value of \(t_{\text{delay}}\).
3. **Injection modes**

   The injected thermal power \(\dot{Q}\) is computed according to the mode defined by the user (`EnergyInjectionMode`):

   - **Mode 1** (`ProportionalToWaterMass`). Power is proportional to the total water mass:

     \[\dot{Q} = q_{\text{inj}} \cdot M \cdot P(t_{\text{rel}})\]

     where \(M = \rho V\) is the mass of water and \(q_{\text{inj}}\) the injected specific power (\(\text{W/kg}\)). An optional density threshold \(\rho_{\text{limit}}\) can be provided. If \(\rho < \rho_{\text{limit}}\), the injection is zero (\(\dot{Q} = 0\)).
   - **Mode 2** (`ProportionalToLiquidMass`). Power is proportional to the liquid water mass:

     \[\dot{Q} = q_{\text{inj}} \cdot (1 - x_{\text{vap}}) \cdot M \cdot P(t_{\text{rel}})\]

     where \(M = \rho V\) is the mass of water, \(x_{\text{vap}}\) the vapor mass fraction, and \(q_{\text{inj}}\) the injected specific power (\(\text{W/kg}\)).
   - **Mode 3** (`ProportionalToLiquidVolume`). Power is proportional to the liquid volume:

     \[\dot{Q} = q_{\text{inj}} \cdot (1 - \alpha) \cdot V \cdot P(t_{\text{rel}})\]

     where \(\alpha\) is the void fraction and \(q_{\text{inj}}\) the injected power density (\(\text{W/m}^3\)).
   - **Mode 4** (`ProportionalToTemperatureGap`). Power is proportional to the temperature difference:

     \[\dot{Q} = q_{\text{inj}} \cdot (T_{\text{imp}} - T) \cdot P(t_{\text{rel}})\]

     where \(T\) is the fluid temperature, \(T_{\text{imp}}\) the imposed fluid temperature, and \(q_{\text{inj}}\) the heat exchange coefficient (\(\text{W/K}\)).

Note

The energy injection source term strictly requires the formulation to use
`EPXTabulatedWaterEOS`.

## Configuration Options

Configuration parameters are gathered into the `EnergyInjectionOptions`
structure as shown in the following declaration:

```c++
/**
 * @enum EnergyInjectionMode
 * @brief Injection modes for energy injection in water
 */
enum class EnergyInjectionMode : Int {
  ProportionalToWaterMass      = 1,    //!< Power proportional to total water mass
  ProportionalToLiquidMass     = 2,    //!< Power proportional to liquid water mass
  ProportionalToLiquidVolume   = 3,    //!< Power proportional to liquid volume
  ProportionalToTemperatureGap = 4     //!< Power proportional to temperature difference (timp - T)
};

/**
 * @struct EnergyInjectionOptions
 * @brief Configuration parameters and options for EnergyInjectionTerm
 */
struct EnergyInjectionOptions {
  Real powerIntensity;                  //!< Nominal injection power intensity (W/kg, W/m^3, or W/K)
  Real propagationSpeed;                //!< Characteristic wave propagation speed (m/s)
  EnergyInjectionMode injectionMode;    //!< Injection mode

  Optional<Real> densityThreshold = std::nullopt;    //!< Density threshold (only for ProportionalToWaterMass mode)
  Optional<Real> imposedTemperature =
      std::nullopt;    //!< Imposed temperature target (only for ProportionalToTemperatureGap mode)
```

## Example of usage:

Here is an example to add an energy injection source term to an Euler formulation:

```c++
    using FluidModel = HEMFluidModel<geoDim, EPXHLLCRiemannSolver<geoDim, EOS>>;
    using Form       = EulerExplicitPipeFormulation<FluidModel>;
    auto &fluxForm   = rm.make<Form>(tube, eos, U, Uvar, W, leftBoundary, areaFunction);
```

```c++
    Real time = 0.;    // time has to be initialized before being given to addEnergyInjection
    fluxForm.addEnergyInjection(ctx, originCell, time, powerInjection, injectionOptions);
```

All parameters and options related to energy injection are summarized in the following table.

Table 8 Key Parameters and options of the energy injection source term

| Provided ... | Symbol / C++ Equivalent | Units | Description |
| --- | --- | --- | --- |
| **Directly by the caller** | \(P(t_{\text{rel}})\)  `powerInjection` | N/A | Dimensionless function of the time elapsed  since the wave arrival, \(t_{\text{rel}} = t - t_{\text{delay}}\) |
|  | \(\mathbf{x}_{\text{origin}}\)  `originCell` | N/A | `MeshSet` containing the single  cell where the wave originates |
| **Through** `EnergyInjectionOptions` | \(q_{\text{inj}}\)  `powerIntensity` | \(\text{W/kg}\) (Modes 1 & 2)  \(\text{W/m}^3\) (Mode 3)  \(\text{W/K}\) (Mode 4) | Base power intensity |
|  | \(c_{\text{propag}}\)  `propagationSpeed` | \(\text{m/s}\) | Characteristic wave propagation speed |
|  | Mode  `injectionMode` | N/A | Selected injection model  (Modes 1 to 4) |
|  | \(\rho_{\text{limit}}\)  `densityThreshold` | \(\text{kg/m}^3\) | Density cutoff threshold  (Mode 1 only, optional) |
|  | \(T_{\text{imp}}\)  `imposedTemperature` | \(\text{K}\) | Imposed fluid temperature  (Mode 4 only, mandatory) |

The method `addEnergyInjection` is compatible with every Euler explicit formulation using `EPXTabulatedWaterEOS`.

Note

Each `addEnergyInjection` has an overload taking an additional
`MeshSet` argument, to restrict the energy injection source term to a
subset of cells instead of applying it to the whole formulation's domain.

Note

Implicit Euler formulations, such as `EulerImplicitPipeFormulation`,
are not yet compatible with `addEnergyInjection`: `EnergyInjectionTerm` does
not currently implement `computeJacobian`, which is required for
implicit time integration.

Warning

The propagation delay calculation relies on the Euclidean straight line distance
\(\|\mathbf{x} - \mathbf{x}_{\text{origin}}\|\). This formulation assumes
a convex domain. For complex non-convex geometries (like curved pipes), the wave path is assumed straight between the origin and the target cell.
