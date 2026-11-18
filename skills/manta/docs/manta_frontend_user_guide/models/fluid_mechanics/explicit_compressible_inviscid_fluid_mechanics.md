<!-- source: https://manta-project.gitlab.io/manta/manta_frontend_user_guide/models/fluid_mechanics/explicit_compressible_inviscid_fluid_mechanics.html -->

# Explicit compressible inviscid fluid mechanics

## Introduction

In this section, we'll consider transient inviscid compressible flows. Such
models are especially used to handle shock waves and explosions. Fluid mechanic
applications in MANTA mainly cover compressible flows, as Europlexus does.
MANTA is able to simulate both fast transient computations for accidental
conditions using explicit time schemes, and nominal quasi-steady states with
implicit time schemes. In this section, we'll consider explicit schemes. The
spatial discretization of the Euler equations is presently implemented within
the Finite Volumes Method.

Details on the Euler equations and the numerical scheme can be found in the
[theory manual](../../../theory_manual/fluid_mechanics/compressible_fluid_mechanics.md#compressible-fluid-mechanics).

## Available solvers

Table 1 Available solvers for compressible inviscid fluid mechanics

| Equation  of state | Riemann  solver | Spatiotemporal  order | Time  integrator | Reconstruction  operator | Limiting  operator |
| --- | --- | --- | --- | --- | --- |
| Perfect gas | HLLC | 2 | MusclHancock | Linear | Dubois |
| Perfect gas | HLLC | 2 | MusclHancock | Linear | BarthJespersen |
| Perfect gas | HLLC | 1 | ForwardEuler | PieceWiseConstant |  |
| Perfect gas | Exact | 2 | MusclHancock | Linear | Dubois |
| Perfect gas | Exact | 2 | MusclHancock | Linear | BarthJespersen |
| Perfect gas | Exact | 1 | ForwardEuler | PieceWiseConstant |  |
| Stiffened gas | HLLC | 2 | MusclHancock | Linear | Dubois |
| Stiffened gas | HLLC | 2 | MusclHancock | Linear | BarthJespersen |
| Stiffened gas | HLLC | 1 | ForwardEuler | PieceWiseConstant |  |

An explicit solver for compressible inviscid fluid mechanics consists in the
combinaison of an **equation of state**, a [Riemann solver](../../../theory_manual/fluid_mechanics/compressible_fluid_mechanics.md#euler-riemann-solvers), a [time_integrator](../../../theory_manual/fluid_mechanics/compressible_fluid_mechanics.md#euler-explicit-time-integrators), a [reconstruction operator](../../../theory_manual/fluid_mechanics/compressible_fluid_mechanics.md#euler-reconstruction-and-limiters) and a [limiting operator](../../../theory_manual/fluid_mechanics/compressible_fluid_mechanics.md#euler-limiters):

- The time integrator fixes the order of approximation in time.
- The reconstruction operator fixes the order of approximation in space.

Two equations of state are available: `PerfectGas` and
`StiffenedGas`. Two Riemann solvers are available `HLLC` and
`Exact`.

This combination can not be arbitrary and the following restrictions
holds:

1. The `Exact` Riemann solver only works with the `PerfectGas`
   equation of state.
2. The order of approximation in space and time must be equal for the
   numerical scheme to be stable:

   - A first order spatiotemporal scheme associates the `ForwardEuler`
     time integrator and the `PieceWiseConstant` reconstruction
     operator.
   - A second order spatiotemporal scheme associates the
     `MusclHancock` time integrator and the
     `Linear` reconstruction operator.
3. Two limiting operators are available for second order reconstruction
   operators: `Dubois` and `BarthJespersen`.

The available solvers are summarized on
Table [Available solvers for compressible inviscid fluid mechanics](#available-explicit-compressible-inviscid-fluid-mechanics-solvers).

### Example of usage

C++

```c++
// get the solver factory
const auto &f         = CompressibleInviscidFluidSolversFactory::get();
// define the parameters
const auto parameters = Parameters{{"domains", Vector<std::string>{"load", "air"}},
                                   {"solverOptions",
                                    Parameters{{"RiemannSolver", "HLLC"},
                                               {"spatiotemporalOrder", 2},
                                               {"limitingOperator", "Dubois"},
                                               {"CFLSafetyFactor", inputData.get<Real>("cfl")}}},
                                   {"equationOfState",
                                    Parameters{
                                       {"name", "PerfectGas"},
                                       {"parameters", Parameters{{"HeatCapacityRatio",
                                                                  inputData.get<Real>("gamma")}}},
                                   }}};
// create the solver defined by the parameters
auto solver = f.generate(ctx, *ps, parameters);
// add the boundary conditions
const auto ib = solver->addBoundaryCondition(ctx, "Wall", Parameters{{"boundary", "allCells_boundary"}});
```

PYTHON

```python
# get the solver factory
sf = manta.fluid_mechanics.fvm.CompressibleInviscidFluidSolverFactory.get()
# create the solver defined by the parameters
solver = sf.create(ps,
                   domains= ["load", "air"],
                   solverOptions = {"RiemannSolver": "HLLC",
                                    "spatiotemporalOrder": 2,
                                    "limitingOperator": "Dubois",
                                    "CFLSafetyFactor": cfl},
                   equationOfState = {"PerfectGas" : {"HeatCapacityRatio": gamma}})
# add the boundary conditions
solver.addBoundaryCondition("Wall",
                            boundary = "allCells_boundary")
```

### User-defined extensions

Users can register variants of the previous built-in solvers by registring new
generators to the `CompressibleInviscidFluidSolversFactory` class.

The following sections give details on the various parameters of this solver.

## Equations of state

Every EOS described in this section is written linking the three following
variables : density \(\rho\), pressure \(p\), and internal energy
\(e\).
Available EOS and their input parameters in MANTA frontend API are :

- `PerfectGas` equation of state, for ideal gases

  Input parameters:

  - [Mandatory] "HeatCapacityRatio" \(\gamma\)
- `StiffenedGas` equation of state

  Input parameters:

  - [Mandatory] "HeatCapacityRatio" \(\gamma\)
  - [Mandatory] "InfinitePressure" \(P_{\infty}\), usually around \(10^8 - 10^9 Pa\)
  - [Optional] "HeatBond" \(q\)
- `IsothermalFluid` equation of state

  Input parameters:

  - [Mandatory] "SoundSpeed" \(c\) the isothermal speed of sound, a constant.
  - [Mandatory] "InitialPressure" \(p_{ini}\), the initial pressure.
  - [Mandatory] "InitialDensity" \(\rho_{ini}\), the corresponding initial density.

## Riemann solvers

The `RiemannSolver` parameter specifies how the flux on each facet is
computed from data in adjacent cells.
Only two solvers are currently available in MANTA frontend.

- `Exact` Riemann solver
- `HLLC` Riemann solver

Documentation about Riemann solvers can be found [here](../../../theory_manual/fluid_mechanics/compressible_fluid_mechanics.md#euler-riemann-solvers).

## Reconstruction operators and limiters

The `spatiotemporalOrder` parameter characterizes the order of the
numerical scheme in both space and time (see [here](#time-integration-frontend)
for time integration). The order in space defines how the state variables are
spatially discretized on the cell volume, and is then associated with a
`ReconstructionOperator`. It provides how the values at facets are
reconstructed from field values at cell centers. At higher order, limiters are
needed to ensure the scheme still verifies the Total Variation Diminishing (TVD)
property, i.e. it preserves monotonicity in space.

Two options are available:

- `spatiotemporalOrder` = 1 => `PieceWiseConstant` reconstruction
  operator, state variables are constant over the volume.
- `spatiotemporalOrder` = 2 => `Linear` reconstruction operator, state
  variables are linear over the volume.

In the `Linear` case, two limiters are available:

- `BarthJespersen` limiter
- `Dubois` limiter. This limiter uses an additional parameter \(K\),
  usually taken between \(0.5\) and \(1\).

Documentation about reconstruction and limiters can be found
[here](../../../theory_manual/fluid_mechanics/compressible_fluid_mechanics.md#euler-reconstruction-and-limiters).

## Time integration

Time integration is managed through the `spatiotemporalOrder` parameter,
since it is strongly recommended to be in first order or second order in both
space and time.

Explicit time integration schemes used are:

- `spatiotemporalOrder` = 1 => `ForwardEuler` time integrator, first
  order scheme, associated with the `PieceWiseConstant` reconstruction
  operator.
- `spatiotemporalOrder` = 2 => `MusclHancock` time integrator, second
  order scheme, associated with the `Linear` reconstruction operator.

Details are available [here](../../../theory_manual/fluid_mechanics/compressible_fluid_mechanics.md#euler-explicit-time-integrators).

### The `CFLStabilityfactorEstimate` parameter

This paragraph describes the role of the
`CFLStabilityfactorEstimate` parameter, denoted \(C_e\) in the
following. Details about the CFL condition can be found here : [The CFLStabilityfactorEstimate parameter](../../../theory_manual/fluid_mechanics/cfl_stability_factor_estimate.md#cfl-stability-factor-estimate)

\(C_e\) is a user-defined parameter used to compute each time step
increment \(\Delta t\) of an explicit FVM *time integrator*,
in such way:

\[\begin{equation}
\Delta t = \Delta t_c \, C_e
\end{equation}\]

where \(\Delta t_c\) is a critical time step, computed internally.

\(C_e\) is usually chosen less than or equal to `1` for
first-order FVM schemes, and less than or equal to `0.5` for
second-order FVM schemes.

## Boundary conditions

Boundary conditions in FVM schemes provide how to compute the outside state on
boundary facets, needed to compute the flux on these. FVM boundary conditions are
then parametrized by a type, an application area (that is a boundary), and input
parameters depending on the type. Additional boundary conditions will be
progressively available in MANTA. Users can also develop their own boundary
condition and add it to the MANTA API.

### The `Wall` boundary condition

The `Wall` boundary condition characterizes a rigid wall. Waves are
reflected along the normal direction of the facet. Scalar variables in the
outside state are copied from the inside state, whereas the velocity is
(\(\mathbf{n}\) is the facet normal):

\[\mathbf{u}_{out} = \mathbf{u}_{in} - 2 ( \mathbf{u}_{in} \cdot \mathbf{n} ) \mathbf{n}\]

With \(\mathbf{u}_{in}\) the velocity in the inside cell and
\(\mathbf{u}_{out}\) the one in the outside ghost cell.

### The `Copied` boundary condition

The `Copied` boundary condition characterizes a supersonic outflow. All
waves are supposed to propagate outside the domain. The outside state is then
copied from the inside state. This boundary condition can be applied for other
boundaries like inflows, but it is assumed that all waves are absorbed.
