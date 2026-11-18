<!-- source: https://manta-project.gitlab.io/manta/manta_frontend_user_guide/bricks/solid_mechanics/isotropic_linear_elastic_material.html -->

# The `IsotropicLinearElasticSolidMaterial` brick

## Description

The `IsotropicLinearElasticSolidMaterial` brick describes the following variational operator:

(6)\[\int_{\Omega_{r}}\left(\tepsilonto\paren{\v{u}}-\sum_{i}\tepsilon^{e}_{(i)}\right):\,\tfour{D}\,\colon\,\tepsilonto\paren{\var{\v{u}}} \d\,V\]

where:

- \(\Omega_{r}\) is the domain on which the brick is defined, in the
  reference configuration,
- \(\v{u}\) is the displacement field,
- \(\var{\v{u}}\) is a kinematically admissible virtual variation of
  the displacement field,
- \(\tepsilonto\) is the linearized strain such that:

  \[\tepsilonto\paren{\v{u}} = sym \tGradient{\v{u}} =
  \frac{1}{2}\paren{\tGradient{\v{u}}+\transpose{\tGradient{\v{u}}}},\]

  where \(\tGradient{\v{u}}\) denotes the gradient of \(\v{u}\)
  in the reference configuration.
- \(\tepsilon^{e}_{(i)}\) is a list of strains describing stress
  free expansions.
- \(\tfour{D}\) is the stiffness matrix of an elastic material:

  \[\tfour{D} = \lambda\,\t{I}\otimes\t{I}+2\,\mu\,\tfour{I},\]

  \(\lambda\), \(\mu\) being respectively the first and second
  Lamé's coefficient. The second Lamé's coefficient is generally
  referred to as the shear modulus.

  \(\lambda\) and \(\mu\) are related to Young's modulus \(E\)
  and Poisson's ratio as follow:

  \[\begin{split}\left\{
  \begin{aligned}
  \lambda &= \frac{\nu\,E}{\paren{1+\nu}\,\paren{1-2\,\nu}}\\
  \mu &= \frac{E}{2\,\paren{1+\nu}}\\
  \end{aligned}
  \right.\end{split}\]

## Compatible models

This brick is compatible with the following models:

- [The ImplicitMechanics model](../../models/solid_mechanics/implicit_solid_mechanics.md#implicit-mechanics-model)
