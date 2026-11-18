# Physics branch: what happens and why

Source key: **M** = `sources/cea-methodes-neutronique/` (*Les méthodes de la neutronique*, CEA 2013). Pages are printed page numbers; the file is given as its two-digit prefix. Equations: see `equations.md` (§P…).

## Governing equations

| Topic | Where | Notes |
|---|---|---|
| Why transport theory applies to neutrons (classical particles between point-like collisions, phase space) | M `00`, pp. 43–44 | Introduction "Sur les fondements de l'équation du transport" |
| **Boltzmann equation**, time-dependent integro-differential form: removal, scattering, prompt fission, spontaneous fission, delayed neutrons, external sources; (α,n) and photonuclear sources | M `01`, pp. 45–47 | §P1. Linear in flux because there are no neutron-neutron interactions (p. 45, p. 51) |
| Legendre expansion of the differential scattering cross section | M `01`, p. 46 | Isotropic media: depends only on Ω′·Ω |
| **Generalized Bateman equations** (nuclide evolution: production by reactions and decay, disappearance) | M `01`, p. 49 | §P2. Coupled with Boltzmann through the flux, so the system is closed |
| Stationary forms: integro-differential and **integral** (collision density, transport kernel) | M `03`, pp. 55–56 | §P3. The integral form is the starting point of Monte Carlo |
| Formal analogy between the Boltzmann and Bateman integral equations (box) | M `03`, p. 57 | Transport in space ↔ transmutation in time |

## Criticality and reactivity

| Topic | Where | Notes |
|---|---|---|
| **Critical equation**, k_eff as eigenvalue (fission source divided by k_eff); k_eff as the ratio between neutron generations | M `03`, p. 56 | §P4 |
| Higher harmonics, dominance ratio k₂/k₁ (large, loosely coupled cores such as PWRs) | M `05`, p. 99 | Physical reason for slow source convergence; see methods |
| Reactivity ρ, k_eff = 1/(1−ρ); prompt-critical limit ρ = β | M `07`, pp. 118–119 | §P6 |

## Kinetics and delayed neutrons

| Topic | Where | Notes |
|---|---|---|
| Time scales: µs (Doppler feedback), minutes to hours (Xe/Sm poisoning), years (fuel residence) | M `02`, p. 51 | Justifies separating statics, depletion and kinetics |
| Delayed-neutron precursors (β⁻,n), grouped into families of precursors (6 or 8) | M `03`, pp. 59–60 | §P5 |
| **Point kinetics** equations; neutron lifetime ℓ and ℓ* = ℓ/k_eff | M `07`, p. 118 | §P6 |
| U-235 delayed-neutron data, 8 groups (JEFF-3.1): λᵢ, τᵢ, βᵢ; β ≈ 665 pcm | M `07`, p. 118 (table 17) | §P6 |
| **Nordheim** (inhour) equation; asymptotic period; prompt-critical vs delayed-critical behaviour | M `07`, p. 119 | §P6. τ ≈ 0.0866 s for U-235 |

## Phenomena relevant to modelling

| Topic | Where | Notes |
|---|---|---|
| **Self-shielding as a physical phenomenon** (flux dips in resonances, effect on reaction rates) | M `04`, pp. 66–67 | The models are in methods |
| Doppler effect, temperature feedback, density changes | M `02`, p. 51 | |
| Heterogeneous vs homogeneous media; when homogenization is valid | M `02`, pp. 51–52 | |
| Heavy-nuclide evolution (U/Pu chains) | M `06`, p. 110 | Depletion examples |
| **Fission-product poisoning**: samarium-149, xenon-135 | M `06`, pp. 110–111 | |
| Photon transport and gamma heating, coupled through photonuclear sources | M `01`, pp. 45, 47 | |
