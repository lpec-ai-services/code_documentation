# Methods branch: how it is computed

Sources (pages are printed pages):
- **M** = `sources/cea-methodes-neutronique/`: CEA monograph (2013), in French. File = two-digit prefix.
- **S** = `sources/stacey-reactor-physics-3e/`: Stacey, *Nuclear Reactor Physics*, 3rd ed. (2018).

Equations: `equations.md` (§M…).

## Calculation schemes and reactor analysis

| Topic | Where | Notes |
|---|---|---|
| Why schemes (7 variables, ~10¹² unknowns); **two-step scheme** (lattice, then homogenization/condensation and equivalence, then core); direct 3D transport vs Monte Carlo + depletion; separating statics, depletion and transients | M `02`, pp. 51–54 | |
| Nuclear reactor analysis workflow; physics–thermal-hydraulics interaction | S §7.12–7.13, pp. 276–284 | |
| **Homogenization**: equivalent cross sections, ABH collision probability, blackness theory, assembly transport, homogenization theory, **equivalence theory**, multiscale expansion, **flux reconstruction** | S ch. 14, pp. 535–562; S §3.8, p. 65 | |

## Energy treatment

| Topic | Where | Notes |
|---|---|---|
| **Multigroup** equations and flux-weighted cross sections; lethargy | M `04`, pp. 64–65; S §4.2, §4.4, pp. 112, 127 | §M1 |
| **Self-shielding formalism** (APOLLO2): equivalence with a homogeneous medium, **subgroup** methods, resonant mixtures, BWR validation | M `04`, pp. 65–72 | Livolant–Jeanpierre method also cited in M `02`, p. 53 |
| Resonance treatment: first-flight escape probabilities, unresolved resonances, **multiband** spatial self-shielding, resonance representations (SLBW, MLBW, Reich–Moore, Adler–Adler, pole) | S ch. 11, pp. 439–468 | |
| P1 and B1 slowing-down equations; continuous slowing-down; multigroup Sₙ | S ch. 10, pp. 400–428 | |
| Thermal spectra in homogeneous media and lattices (numerical) | S §12.4–12.5, pp. 478–494 | |

## Angle and space (deterministic)

| Topic | Where | Notes |
|---|---|---|
| **Diffusion**: P1 truncation, Fick's law; numerical solution of the diffusion equation | M `04`, pp. 75–76; S §3.10, p. 76 | §M2 |
| **Collision probability** and **interface current** methods (slab and multidimensional) | S §9.3–9.5, pp. 323–343 | |
| **Pₙ** (1D and multidimensional), **SPₙ** (MINOS, MINARET) | M `04`, pp. 74–75; S §9.6–9.7, pp. 344–361 | §M2 |
| **Sₙ** discrete ordinates (slab, sphere, multidimensional) | M `04`, pp. 72–74; S §9.8–9.10, pp. 362–379 | |
| Even-parity transport | M `04`, p. 81; S §9.11, p. 379; S §13.10, p. 524 | |
| **Method of characteristics** (tracking, transmission and balance equations, boundary conditions; APOLLO3) | M `04`, pp. 82–86 | §M3 |
| Space: finite differences, **nodal** (conventional; transverse-integrated diffusion, integral transport and Sₙ), finite elements (primal and mixed), coarse-mesh finite elements | M `04`, pp. 76–79; S §3.11, p. 82; S ch. 15, pp. 563–604 | |
| **Synthesis methods**: single- and multi-channel spatial, spectral | S §15.9–15.11, pp. 608–622 | |
| Variational principle for multigroup diffusion | S §15.8, p. 605 | |

## Monte Carlo

| Topic | Where | Notes |
|---|---|---|
| Principles, Neumann series, analog and non-analog simulation, sampling laws, weights | M `05`, pp. 89–95; S §9.12, p. 380 | §M4 |
| Convergence, figure of merit, estimators, variance | M `05`, pp. 97–98 | |
| Criticality: power iteration, dominance ratio, source convergence, stationarity diagnostics | M `05`, pp. 99–100 | §M5 |
| k_eff variance and inter-cycle correlation; acceleration and variance reduction (importance, splitting / Russian roulette) | M `05`, pp. 101–104 | |

## Perturbation and variational methods

| Topic | Where | Notes |
|---|---|---|
| **Perturbation theory** reactivity estimates; **adjoint operators and importance function** | S §13.1–13.2, pp. 501–508 | |
| Variational / generalized perturbation theory (reactivity, reaction-rate ratios, reaction rates); variational theory; intermediate resonance integral; heterogeneity effects; variational derivation of approximate equations; boundary perturbation | S §13.3–13.11, pp. 508–534 | |
| Perturbation estimates of reactivity temperature coefficients | S §5.8, p. 168 | |

## Depletion

| Topic | Where | Notes |
|---|---|---|
| Bateman principles; analytic and numerical solution | M `06`, pp. 107–109 | |
| Examples: heavy nuclides, Xe/Sm poisoning (DARWIN); simple depletion model | M `06`, pp. 110–113; S §6.4, p. 219 | |

## Kinetics solvers

| Topic | Where | Notes |
|---|---|---|
| Numerical methods for point kinetics | S §5.13, p. 192 | |
| Point kinetics via the Nordheim equation | M `07`, pp. 118–119 | Equations in §P6 |
| **Space–time kinetics**: spatially dependent point kinetics; time integration of the spatial flux; stability | S §16.2–16.4, pp. 626–667 | |
| **3D kinetics models**: quasi-static (QS), improved quasi-static (IQS), local quasi-static, multi-scale, **modal synthesis**, direct 3D kinetics (CRONOS, APOLLO3/MINARET) | M `07`, pp. 120–124 | |

## Codes named in the sources

APOLLO2/3, MINOS, MINARET, CRONOS, ERANOS, TRIPOLI-4 (→ `tripoli4` skill), DARWIN (M).
