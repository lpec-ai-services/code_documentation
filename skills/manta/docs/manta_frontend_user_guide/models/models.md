<!-- source: https://manta-project.gitlab.io/manta/manta_frontend_user_guide/models/models.html -->

# Models

The *Models* describe one or several physical phenomena. They are built on
balance equations (heat transfer, diffusion, mechanics, ...) which requires to
solve partial differential for which MANTA provides several numerical methods,
including Finite Element Method (FEM), Finite Volume Method (FVM), Hybrid High
Order method (HHO), ...

The *Models* are linked internally with methods and solvers that are adapted to
the problem they are solving (e.g. time integrators for time dependent phenomena).

*Models* rely on *Bricks*: see [Bricks](../bricks/bricks.md#bricks).

Contents

- [Generalities on models](generalities.md)
- [Solid mechanics models](solid_mechanics/solid_mechanics.md)
- [Solid heat transfer](solid_heat_transfer/solid_heat_transfer.md)
- [Explicit compressible inviscid fluid mechanics](fluid_mechanics/explicit_compressible_inviscid_fluid_mechanics.md)
- [Point-wise models](point_wise_models/point_wise_models.md)
- [Micromorphic damage models](micromorphic_damage/micromorphic_damage.md)
