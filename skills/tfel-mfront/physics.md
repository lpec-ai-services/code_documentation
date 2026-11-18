# Physics branch: constitutive laws and material behaviour

Pages are in `docs/`; implementations are in `examples/behaviours/<family>/`.

## Foundations

| Topic | Pages |
|---|---|
| Nonlinear mechanical behaviours: theory, thermodynamic framework, small/finite strain | `theory.md` |
| Role of a mechanical behaviour; generic overview; isotropic J₂ plasticity and viscoplasticity | `behaviours.md` |
| Tensors (2nd and 4th order), invariants, eigen-decomposition | `tensors.md` |
| Material properties (temperature-dependent laws: Young's modulus, conductivity…) | `material-properties.md` |
| Point-wise models (swelling, densification… for fuel codes) | `models.md` |
| Glossary of standard variable names | `glossary.md` |

## Elasticity

| Topic | Pages | Gallery |
|---|---|---|
| Hooke's law: isotropic, orthotropic, plane stress, thermal expansion | `HookeStressPotential.md` | |
| Non-linear elasticity (Ramberg–Osgood) | `RambergOsgoodNonLinearElasticity.md` | `nonlinearelasticity/` |
| **Hyperelasticity** (generic, Ogden, Signorini) | `hyperelasticity.md`, `ogden.md`, `signorini.md` | `hyperelasticity/` |
| Hyperviscoelasticity; viscoelasticity | `hyperviscoelasticity.md` | `hyperviscoelasticity/`, `viscoelasticity/` |

## Plasticity and viscoplasticity

| Topic | Pages | Gallery |
|---|---|---|
| Isotropic linear hardening (von Mises) | `IsotropicLinearHardeningPlasticity.md` | `plasticity/` |
| Orthotropic plasticity (Hill) | `orthotropiclinearhardeningplasticity.md` | `plasticity/` |
| Combined isotropic and Armstrong–Frederick kinematic hardening (viscoplastic) | `isotropicplasticityamstrongfrederickinematichardening.md` | `viscoplasticity/` |
| Norton creep | `Norton-full.md`, `Norton-web.md`, `tutorial.md` (French) | `viscoplasticity/` |
| Other yield criteria: **Drucker–Prager** (with cap), Drucker, Hosford, Green (elliptic), **Barlat Yld2004-18p**, **Mohr–Coulomb** | `drucker-prager-cap.md`, `drucker.md`, `hosford.md`, `greenplasticity.md`, `barlat-yld2004.md`, `MohrCoulomb.md` | `plasticity/` |
| Porous plasticity (Gurson-type, Rousselier…) | `StandardElastoViscoPlasticityBrick-PorousPlasticity.md`, `ExtendingStandardElastoViscoPlasticityBrick-PorousStressCriterion.md` | |
| Multi-surface plasticity (Fischer–Burmeister formulation) | `FischerBurmeister.md` | |
| Iwan model | `iwan.md` | |

## Damage, fracture, concrete, sintering

| Topic | Pages | Gallery |
|---|---|---|
| **Fichant–La Borderie damage** (concrete); coupled with Torelli load-induced thermal strain | `FichantLaBorderieDamageBehaviour.md`, `FichantLaBorderieDamageAndTorelliLoadInducedStrainBehaviour.md`, `LoadInducedThermalStrainBehaviourTorelli2018.md` | `damage/` |
| DDIF2 damage law (CEA fuel performance codes) | `DDIF2Brick.md`, `DDIF2StressPotential.md` | |
| Concrete creep and shrinkage (`Burger_EDF_CIWAP_2021`) | `Burger_EDF_CIWAP_2021.md` | |
| Damage + viscoplasticity | | `damage_viscoplasticity/` |
| **Phase-field** brittle fracture (with Cast3M) | `phasefield.md` | |
| Viscous sintering (Skorohod–Olevsky, SOVS) | `sovs.md` | |
| Cohesive zone models | `DefaultCZM-keywords.md`, `ImplicitCZM-keywords.md` | |

## Finite strain and crystal plasticity

| Topic | Pages | Gallery |
|---|---|---|
| Multiplicative decomposition $F = F_e F_p$, implicit plasticity | `FeFpImplicitPlasticity.md` | |
| **Single crystals**: slip systems, orientation tensors, interaction matrices | `singlecrystal.md` | |
| Méric–Cailletaud single-crystal plasticity | `MericCailletaudSingleCrystalPlasticity.md` | |
| Finite-strain single-crystal framework; comparison with Huang | `finitestrainsinglecrystal.md`, `finitestrainsinglecrystal-huang.md` | `finitestrainsinglecrystal/` |

## Homogenization (mean-field)

| Topic | Pages |
|---|---|
| TFEL/Material homogenization overview | `tfel-material-homogenization.md` |
| Bounds and schemes: **Sachs/Reuss**, **Taylor/Voigt**, biphasic linear schemes (dilute, Mori–Tanaka, Hashin–Shtrikman bounds), Ponte-Castañeda non-linear bound | `Sachs.md`, `Taylor.md`, `BiphasicLinearHomogenization.md`, `PonteCastaneda1992.md` |
| Polycrystals: Berveiller–Zaoui (explicit and implicit), Cailletaud–Pilvin β-rule, Masson affine formulation | `ExplicitBerveillerZaouiPolyCrystals.md`, `ImplicitBerveillerZaouiPolyCrystals.md`, `BetaRule.md`, `MassonAffineFormulation.md` |
