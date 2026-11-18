<!-- source: https://manta-project.gitlab.io/manta/manta_frontend_user_guide/miscellaneous/mfront_material_knowledge_management.html -->

# Advices on the management of MFront material knowledge

Many bricks in MANTA require the user to provide material knowledge
(material properties, behaviors or point wise model, see below)
implemented with the [MFront](https://thelfer.github.io/tfel/web/index.html) code generator. Those
bricks are mostly related to numerical simulations of solids.

Note

In the case of fluids, models rely directly on an equation of state,
which is directly implemented in MANTA.

MFront takes one or several source files implementing a given material
knowledge and generates C++ code that is compiled into shared
libraries that can be called from MANTA. This system is very flexible
but requires special care from the user.

This document aims at describing the role of material knowledge in
numerical simulations of solids, exposing specific issues related to
material knowledge management and devising some practical solutions. It
is organized as follows:

- Section [Role of material knowledge in numerical simulations of solids](#role-material-knowledge-in-numerical-simulations-of-solids)
  describes the role of material knowledge in numerical simulations of
  solids to fix the wording.
- MANTA have a large number of use cases and aims at covering both
  research studies and safety-critical studies. Section
  [Requirements related to safety-critical studies](#requirements-related-to-safety-critical-studies) discusses
  specific issues related to material knowledge management in
  safety-critical studies.
- Section [Pratical material knowledge management](#general-advices-for-material-knowledge-management)
  provides some general advices and strategies for proper material
  management, either for team work or individual usage.
- Section [General advices](#general-advices) lists a set of advices to avoid
  common pitfalls.

## Role of material knowledge in numerical simulations of solids

Numerical simulations of solids are based on the description of the
evolution of the thermodynamical state of the materials of interest. In
MANTA, this thermodynamical state is described at each point of space
by a set of internal state variables which can evolve with time due to
various physical phenomena (plasticity, viscoplaticity, damage, phase
change, swelling due to dessication, etc.).

The knowledge that one may have about a given material can be represented
in different forms. Here, the following categorization is employed:

- **Material properties** are defined here as functions of the current
  state of the material.
- **Behaviours** describe how a material evolves and reacts locally due
  to gradients inside the material. Here, the material reaction is
  associated with fluxes (or forces) thermodynamically conjugated with
  the gradients.
- **Point-wise models** describe the evolution of some internal state
  variables with the evolution of other state variables. Point-wise
  models may be seen as behaviours without gradients.

## Requirements related to safety-critical studies

Material knowledge management for safety-critical studies raises several
concerns:

- **Intellectual property**: Frequently, material knowledge reflects
  the know-how of industrials and shall be kept private for various reasons.
  For example, some mechanical behaviours result from years of experimental
  testing in dedicated facilities and are thus highly valuable. In some
  cases, material knowledge can be a competitive advantage.
- **Maintainability over decades**: Some safety-critical studies can be
  used to design buildings, plants, or technological systems for
  operation periods of decades or more. Over such
  periods of time, both the solvers and the material knowledge will
  evolve. The safety-critical studies, however, on which design choices
  or decisions were based, need to remain accessible or reproducible.
- **Progression of the state of the art**: Safety-critical studies need
  to reflect the state of the art. As such, the material knowledge per se,
  numerical methods and software engineering need to evolve. This evolution must
  ensure that the other principles listed here are not violated in order
  to maintain quality assurance of past, present and future analyses.
- **Continuous integration and unit testing**: Each implementation has
  associated unit tests which are used to check non-regression during the
  development of MFront, [MGIS](https://thelfer.github.io/mgis/web/index.html) and MANTA.
- **Documentation**: the project can automatically generate the documentation
  associated with the various implementations.
  Implementations of material knowledge can be associated to essential
  meta data.

## Pratical material knowledge management

### Creating a material management project for enginneering studies and team work

Consider developping a dedicated material management project and
maintaining MFront sources in version control system (such as
`git`). Such material management project can be supported at the
level of a project (sensitive data), of a laboratory, of a service or a
departement (globally public data), depending on the level of
confidentiality required.

The [MFrontGallery project](https://thelfer.github.io/MFrontGallery/web/index.html) typically
provides a `cmake` infrastructure for that purpose and have [dedicated
documentation](https://thelfer.github.io/MFrontGallery/web/creating-derived-project.html)
showing how to create a so-called derived project.

Using proper continuous integration and deployement tools allows to
deploy the generated libraries in shared folders with restricted access
for the member of the project (typically using the Network File System
under Unix-like systems).

Note

The generated libraries are specific to a given version of MFront and,
transitively, specific to a given version of MANTA. If multiple
versions of MANTA are used in parallel, one shall deploy one
version of the shared libraries per version of MANTA.

Note

By default, architecture specific flags are used to optimize
the generated libraries for the computer on which the compilation
of the shared library is performed.

When deploying shared libraries across multiple users, beware of
passing the flag `-Denable-portable-build=ON` to `cmake`
at the configuration stage.

An important point is that every finalized studies shall be associated
with a tag of material management project.

### Personal usage

For personal usage, mileage may vary. Creating a material management
project based on The [MFrontGallery project](https://thelfer.github.io/MFrontGallery/web/index.html) could be a
good solution for people at ease with software development and for files
that are used in many studies.

For other people and non critical studies, manual management of the
MFront files on a per study basis can be a good solution. We however
strongly recommend to place the MFront files in a dedicated
repository, named for instance materials. In this repository, the
following command is generally sufficient to create the shared libraries
from the MFront files:

```sh
$ mfront --obuild --interface=generic *.mfront
```

This command automatically creates two repositories named respectively
`src` and `include`. Those repositories contain C++
sources, files describing the compilation process and the generated
libraries.

For intermediate cases, the following organization of the repository
dedicated to a study has proven to be practical:

```
study_name/
├── common_data
├── materials
│   ├── include
│   └── src
├── test_case_1
├── test_case_2
├── ....
└── test_case_n
```

## General advices

1. Never save the shared libraries. Those shared libraries are specific
   to a given version of MFront and, transitively, specific to a given
   version MANTA. This shall be taken into account if two or more
   versions of MANTA are used in parallel.
2. Avoid transfering shared libraries to another computer. By default,
   architecture specific flags are used to optimize the generated
   libraries for the computer on which the compilation of the shared
   libraries is performed.
3. Strange things may happen when switching between two versions of
   MFront, notably because the compilation process is described in the
   `src` directory. The best way to recompile the MFront files in
   this case is to remove the `include` and
   `src` directories.
4. Prefer use of the `LD_LIBRARY_PATH` environment variable to indicate
   where shared libraries are installed. Avoid absolute paths which are a
   source of nuisance when transfering inputs files to colleages. For
   instance, prefer:

   ```c++
   mechanics_model->add(
     ctx, "ImplicitMechanicsSolidMaterial",
     Parameters{{"domain", "cube"},
                {"library", "libHyperElasticityBehaviours-generic.so"},
                {"behavior", "SaintVenantKirchhoffElasticity"}});
   ```

> , with `libHyperElasticityBehaviours-generic.so` available in a directory of `LD_LIBRARY_PATH`, rather than:
>
> > ```c++
> > mechanics_model->add(
> >   ctx, "ImplicitMechanicsSolidMaterial",
> >   Parameters{{"domain", "cube"},
> >              {"library", "../materials/src/libHyperElasticityBehaviours-generic.so"},
> >              {"behavior", "SaintVenantKirchhoffElasticity"}});
> > ```
>
> or, worse:
>
> > ```c++
> > mechanics_model->add(
> >   ctx, "ImplicitMechanicsSolidMaterial",
> >   Parameters{{"domain", "cube"},
> >              {"library", "/home/user/manta/materials/src/libHyperElasticityBehaviours-generic.so"},
> >              {"behavior", "SaintVenantKirchhoffElasticity"}});
> > ```
