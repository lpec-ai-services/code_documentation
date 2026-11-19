# Physics branch: what happens and why

Sources (pages are printed pages; files are listed in each source's `TOC.md`):
- **M** = `sources/cea-methodes-neutronique/`: *Les méthodes de la neutronique*, CEA monograph (2013), in French. File = two-digit prefix.
- **S** = `sources/stacey-reactor-physics-3e/`: W. M. Stacey, *Nuclear Reactor Physics*, 3rd ed. (Wiley, 2018), in English. Cite as "S §x.y, p. N".

Equations: `equations.md` (§P…).

## Nuclear data and neutron interactions

| Topic | Where | Notes |
|---|---|---|
| Fission (binding energy, threshold, cross sections, products, prompt and delayed neutrons, energy release) | S §1.1, pp. 3–12 | |
| Capture, resonances (Breit–Wigner, Doppler broadening) | S §1.2, pp. 12–19 | |
| Elastic scattering, kinematics, energy loss, lethargy, moderating ratio | S §1.3, §1.6, pp. 19–30 | Table 1.4: collisions to thermalize |
| Cross-section summary; evaluated data files (ENDF…) | S §1.4–1.5, pp. 23–25 | |
| Physical constants and nuclear data tables | S App. A, p. 695 | |

## Governing equations

| Topic | Where | Notes |
|---|---|---|
| Why transport theory applies to neutrons | M `00`, pp. 43–44 | |
| **Boltzmann equation**, time-dependent: all source terms | M `01`, pp. 45–47; S §9.1, p. 307 | §P1 |
| **Generalized Bateman equations** | M `01`, p. 49; S §6.1, p. 197 | §P2 |
| Stationary and **integral** forms | M `03`, pp. 55–56; S §9.2, p. 312 | §P3 |
| Boltzmann ↔ Bateman analogy | M `03`, p. 57 | |
| **One-speed diffusion theory**: derivation (Fick's law), diffusion and migration lengths, albedo | S §3.1–3.5, pp. 43–57 | §P8 |

## Criticality and chain reaction

| Topic | Where | Notes |
|---|---|---|
| **Six-factor formula**: η, f, ε, p, non-leakage; k∞ and k; effect of fuel lumping | S §2.1–2.2, pp. 33–38 | §P7 |
| Critical equation, k_eff as eigenvalue | M `03`, p. 56 | §P4 |
| **Bare homogeneous reactor**: geometric buckling, slab, sphere, cylinder; reflected reactor, reflector savings | S §3.6–3.7, pp. 57–65 | §P8 |
| Heterogeneous fuel–moderator cells; control rods | S §3.8–3.9, pp. 65–76 | |
| Higher harmonics, dominance ratio | M `05`, p. 99 | |
| Reactor types and their physics characteristics (PWR, BWR, CANDU, RBMK, gas, LMFR, Gen III/IV, subcritical) | S ch. 7, pp. 247–284 | Engineering of PWRs: `technology.md` |

## Neutron energy spectrum

| Topic | Where | Notes |
|---|---|---|
| Fission, slowing-down and thermal ranges: analytical solutions | S §4.1, p. 101 | |
| **Resonance absorption** (narrow/wide resonance, resonance integral, Doppler) | S §4.3, p. 118; S ch. 11, pp. 429–468 | Physical basis of self-shielding |
| Elastic scattering transfer function; slowing-down theory (P1/B1, continuous slowing down: Fermi age, Goertzel approximation) | S ch. 10, pp. 395–423 | |
| **Thermalization**: scattering from Maxwellian gas and bound nuclei, thermal spectra in homogeneous media and lattices | S ch. 12, pp. 469–500 | Tie-in with TSL data |
| Self-shielding as a phenomenon | M `04`, pp. 66–67 | |

## Kinetics, dynamics and feedback

| Topic | Where | Notes |
|---|---|---|
| Delayed neutrons and precursor families | M `03`, pp. 59–60; S §5.1, p. 141 | §P5 |
| **Point kinetics**, period–reactivity (inhour), prompt jump | M `07`, pp. 118–119; S §5.2–5.4, pp. 145–153 | §P6 |
| Delayed-neutron kernel, transfer function, measuring kinetics parameters | S §5.5–5.6, §5.10, pp. 153–160, 179 | |
| **Reactivity feedback**: fuel temperature (Doppler), moderator temperature and void coefficients, perturbation estimates of coefficients | S §5.7–5.8, pp. 160–171 | |
| Reactor stability; transients with feedback; **fast excursions** (step reactivity with energy feedback) | S §5.9, §5.11–5.12, pp. 171–192 | §P10 |
| Flux tilts, delayed-neutron holdback, spatial stability, **xenon spatial oscillations**, stochastic kinetics | S ch. 16, pp. 623–694 | |
| Time scales (Doppler µs, Xe/Sm h, burnup years) | M `02`, p. 51 | |

## Burnup and fuel cycle

| Topic | Where | Notes |
|---|---|---|
| Changes in fuel composition, transmutation chains, fission products | S §6.1, p. 197 | |
| **Samarium and xenon poisoning**: equilibrium, after shutdown (xenon peak), reactivity worth | S §6.2, pp. 211–217; M `06`, pp. 110–111 | §P9 |
| Conversion and breeding; simple depletion model | S §6.3–6.4, pp. 217–221 | |
| Reprocessing and recycling (MOX), radioactive waste, weapons material, uranium utilization, transmutation, closing the cycle | S §6.5–6.10, pp. 221–246 | |

## Safety

| Topic | Where | Notes |
|---|---|---|
| Elements of reactor safety, safety analysis, **probabilistic risk assessment** | S §8.1–8.3, pp. 285–294 | |
| Reactor accidents (TMI, Chernobyl, Fukushima), passive safety | S §8.4–8.5, pp. 294–306 | Thermal-hydraulic side: `thermal-hydraulics` skill |
