<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/formulations/fluid_mechanics/fvm_compressible_fluid_mechanics/boundary_conditions/fvm_boundary_conditions.html -->

# All FVM Boundary conditions and compatibility summaries

Boundary conditions in FVM schemes provide how to compute the outside state on
boundary facets, needed to compute the flux on these. FVM boundary conditions are
then parametrized by a type, an application area (that is a boundary), and input
parameters depending on the type. Users can also develop their own boundary
condition and add it to the MANTA API.

Contents

- [`Copied` boundary condition](copied.md)
- [`Wall` boundary condition](wall.md)
- [`PrescribedPressureOutflow` boundary condition](prescribed_outflow.md)
- [`CriticalFlow` boundary condition](critical_flow.md)
- [`Tank` boundary condition](tank.md)

## Compatibility summary

Compatibilities between boundary conditions and Euler formulations
(implicit/explicit, classical Euler or Euler 1D) and Equations of state are
summarized in the following table:

Table 7 Boundary conditions vs. Euler formulations vs. equations of state

| **Boundary condition** | **Euler Explicit Formulation** | **Euler Implicit Formulation** | **Euler 1D Explicit Formulation** | **Euler 1D Implicit Formulation** |
| --- | --- | --- | --- | --- |
| **Copied** | **Any** | **Any** | **Any** | **Any** |
| **Wall** | **Any** | **Any** | **Any** | **Any** |
| **Prescribed Pressure** | `PerfectGasEOS`  `IsoThermalFluidEOS`  `EPXTabulatedWaterEOS` | `PerfectGasEOS`  `IsoThermalFluidEOS`  `EPXTabulatedWaterEOS` | `PerfectGasEOS`  `IsoThermalFluidEOS`  `EPXTabulatedWaterEOS` | `PerfectGasEOS`  `IsoThermalFluidEOS`  `EPXTabulatedWaterEOS` |
| **Critical Flow** | **No** | **No** | `PerfectGasEOS`  `IsoThermalFluidEOS` | **No** |
| **Tank** | **No** | **No** | `PerfectGasEOS`  `StiffenedGasEOS`  `IsoThermalFluidEOS` | **No** |
