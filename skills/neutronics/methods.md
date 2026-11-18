# Methods branch: how it is computed

Source key: **M** = `sources/cea-methodes-neutronique/` (*Les méthodes de la neutronique*, CEA 2013). Pages are printed page numbers; the file is given as its two-digit prefix. Equations: see `equations.md` (§M…).

## Calculation schemes (the neutronicist's approach)

| Topic | Where | Notes |
|---|---|---|
| Why we need schemes: 7 variables, about 10¹² unknowns for a fine description, coupling, time scales | M `02`, p. 51 | |
| **Two-step scheme**: lattice/assembly calculation (2D transport, infinite lattice), then homogenization/condensation, equivalence, then core calculation (3D diffusion or simplified transport) | M `02`, pp. 51–54 | The only qualified operational scheme for 3D cores with depletion and feedback |
| Direct 3D transport: deterministic (out of reach for large cores) vs Monte Carlo coupled to a depletion code (statistical uncertainty propagation problem) | M `02`, p. 52 | |
| Separating statics / slow evolution / fast transients | M `02`, p. 52 | |

## Deterministic solution of the stationary Boltzmann equation (chapter `04`)

| Topic | Where | Notes |
|---|---|---|
| Discretizing phase space: orders of magnitude of unknowns | M `04`, pp. 62–63 | |
| **Energy: multigroup** equations; flux-weighted multigroup cross sections; lethargy | M `04`, pp. 64–65 | §M1 |
| **Self-shielding formalism** (APOLLO2): self-shielded vs infinite-dilution cross sections; equivalence with an infinite homogeneous medium; **subgroup** methods; mixtures of resonant isotopes; BWR assembly validation | M `04`, pp. 65–72 | Livolant–Jeanpierre method also cited in `02`, p. 53 |
| **Angle: SN** (discrete ordinates, quadratures) | M `04`, pp. 72–74 | |
| **PN**, **SPN** (simplified transport, available in the MINOS and MINARET solvers) | M `04`, pp. 74–75 | §M2 |
| **Diffusion approximation** (P1 truncation, Fick's law, diffusion coefficient) | M `04`, pp. 75–76 | §M2 |
| **Space**: finite differences, **nodal methods**, finite elements (primal and mixed formulations) | M `04`, pp. 76–79 | |
| **Angle + space**: finite elements (even-parity formulation, discontinuous Galerkin) | M `04`, p. 81 | |
| **Method of characteristics (MOC)**: tracking, transmission and balance equations, transverse integration, boundary conditions, use with self-shielding and finite elements | M `04`, pp. 82–86 | §M3. APOLLO3 |

## Monte Carlo solution (chapter `05`)

| Topic | Where | Notes |
|---|---|---|
| General principles; **Neumann series** of the integral equation | M `05`, pp. 89–90 | |
| Transport by Monte Carlo: analog vs non-analog (biased) simulation | M `05`, pp. 91–92 | |
| **Sampling laws**: source, path length, collision kernel (nuclide, reaction, outgoing E and Ω) | M `05`, pp. 92–94 | §M4 |
| Neutron **weight** | M `05`, p. 95 | |
| Simulation strategies: fine PWR power distribution, flux attenuation in structures (shielding) | M `05`, p. 97 | |
| **Convergence, figure of merit / quality factor**, estimators and variance | M `05`, pp. 97–98 | |
| **Criticality**: power iteration (deterministic vs Monte Carlo batches), dominance ratio, source convergence, stationarity diagnostics (entropy) | M `05`, pp. 99–100 | §M5 |
| **Variance of k_eff and flux**: inter-cycle correlation leads to underestimated variance in large cores; independent replicas | M `05`, p. 101 | |
| **Acceleration / variance reduction**: deterministic initial source for criticality; biasing in propagation (importance, splitting / Russian roulette, exponential transform) | M `05`, pp. 101–104 | |
| Perspectives | M `05`, p. 104 | |

## Depletion solvers (chapter `06`)

| Topic | Where | Notes |
|---|---|---|
| Principles; decay/reaction chains | M `06`, p. 107 | |
| **Analytic solution** of the Bateman equations | M `06`, p. 108 | |
| **Numerical solution** (time steps, Runge–Kutta) | M `06`, p. 109 | |
| Examples: heavy nuclides, Xe/Sm poisoning; DARWIN | M `06`, pp. 110–113 | |

## Kinetics solvers (chapter `07`)

| Topic | Where | Notes |
|---|---|---|
| Principles of time-dependent solution | M `07`, pp. 116–117 | |
| Point kinetics: solution via the Nordheim equation | M `07`, pp. 118–119 | Equations in physics §P6 |
| **3D kinetics**: simplification models, **quasi-static (QS)**, **improved quasi-static (IQS)**, local quasi-static, **multi-scale**, **modal synthesis**, direct 3D kinetics (CRONOS, APOLLO3/MINARET) | M `07`, pp. 120–124 | |

## Codes named in the source

APOLLO2 / APOLLO3 (deterministic lattice and core), MINOS, MINARET (core solvers), CRONOS (core), ERANOS (fast reactors), TRIPOLI-4 (Monte Carlo → `tripoli4` skill), DARWIN (depletion).
