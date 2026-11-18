---
title: The `MFront` gallery
author: Thomas Helfer
date: 1/12/2016
lang: en-EN
---

# Mechanical behaviours

## Hyperelasticity

- [SaintVenantKirchhoffElasticity](./gallery/hyperelasticity/SaintVenantKirchhoffElasticity.mfront)
- [Signorini](signorini.md)
- [Ogden](ogden.md)

## Hyperviscoelasticity

We provide a general framework to build hyperviscoelastic
behaviour. This framework is described
[here](hyperviscoelasticity.md).

## Viscoelasticity

- [GeneralizedMaxwell](./gallery/viscoelasticity/GeneralizedMaxwell.mfront)
- [This page](sovs.md) describes how to implement the
  Skorohold-Olevsky Viscous Sintering (SOVS) model.
- [This page](LoadInducedThermalStrainBehaviourTorelli2018.md)
  describes how to implement Torelli's behaviour describing the load
  induced thermal strain in concrete.
- [This page](Burger_EDF_CIWAP_2021.md) describes the implementation
  of the `̀Burger_EDF_CIWAP_2021` which aims at modelling the following
  phenomena in concrete:
    - Elasticity
    - Drying shrinkage
    - Basic creep
    - Drying creep

## Non-linear elasticity

- [A non-linear elastic behaviour that mimics the Ramberg-Osgood plastic
  behaviour on monotonic
  loadings](RambergOsgoodNonLinearElasticity.md) (useful in fracture
  analysis)

## Damage

- [Marigo](gallery/damage/Marigo.mfront)
- [Mazars](gallery/damage/Mazars.mfront)
- The implementation of the Fichant-La Borderie damage behaviour is
  described [here](FichantLaBorderieDamageBehaviour.md)

## Plasticity

- [IsotropicLinearHardeningPlasticity](IsotropicLinearHardeningPlasticity.md)
- [IsotropicLinearKinematicHardeningPlasticity](gallery/plasticity/IsotropicLinearKinematicHardeningPlasticity.mfront)
- The implementation of an orthotropic plastic behaviour with
  isotropic linear hardening is described
  [here](orthotropiclinearhardeningplasticity.md).
- The implementation of a multi-surface plastic behaviour (the Iwan
  behaviour) is described [here](iwan.md).
- The implementation of a perfect plastic behaviour based on the
  Hosford equivalent stress is described [here](hosford.md).
- The implementation of the Barlat Yld2004-18p behaviour is described
  [here](barlat-yld2004.md).
- The implementation of a perfect plastic behaviour based on the
  Green yield criterion is described [here](greenplasticity.md).
- The implementation of a multi-surface, compressible and perfect
  plastic behaviour using the Drucker-Prager yield criterion and a cap
  is described [here](drucker-prager-cap.md)
- An invariant-based implementation of the Mohr-Coulomb elasto-plastic
  model is described [here](MohrCoulomb.md)

## Viscoplasticity

- [Hayhurst](gallery/viscoplasticity/Hayhurst.mfront)
- [ChabocheViscoplasticity](gallery/viscoplasticity/ChabocheViscoplasticity.mfront)
- The implementation of an isotropic plastic behaviour with several
  kinematic variables following the Amstrong-Frederic evolution law is
  described
  [here](isotropicplasticityamstrongfrederickinematichardening.md)
- [ImplicitNorton](gallery/viscoplasticity/ImplicitNorton.mfront)
- The implementation of the Méric-Cailletaud single crystal behaviour
  under the small and finite strain assumptions are described
  [here](MericCailletaudSingleCrystalPlasticity.md)

## Homogenization

- The implementation of linear homogenization schemes in 3d elasticity
  for biphasic media is described [here](BiphasicLinearHomogenization.md).
- The implementation of [Sachs scheme](Sachs.md) and [Taylor scheme](Taylor.md)
  show how to implement basic homogenized bounds with any behaviour laws on the
  phases using `@BehaviourVariable`.
- The implementation of Idiart's scheme [@idiart_thermodynamic_2025] for a
  maxwellian viscoelastic composite with oriented ellipsoid is available [here](https://github.com/thelfer/MFrontGallery/blob/master/generic-behaviours/homogenization/Idiart_viscoelastic.mfront)
- The description of the implementation of a polycrystal behaviour
  based on the Berveiller-Zaoui homogenisation scheme using an
  explicit scheme is available
  [here](ExplicitBerveillerZaouiPolyCrystals.md).
- [\(\beta\)-rule](BetaRule.md) can also be implemented with
  `@BehaviourVariable` and hence any behaviour law on each phase.
- A tutorial on implementation of Ponte-Castaneda bound [@castaneda_new_1992]
  for a non-linear elastic composite is detailed [here](PonteCastaneda1992.md).
- A tutorial on implementation of the [affine formulation](MassonAffineFormulation.md)
  from Masson et al. [@masson_affine_2000] for a viscoplastic polycrystal.

 
# References

<!-- Local IspellDict: english -->
