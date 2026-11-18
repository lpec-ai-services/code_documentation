---
title: General documentation
author: Thomas Helfer, Jean-Michel Proix
date: 17/08/2021
lang: en-EN
---

Welcome to the **official documentation** for TFEL and MFront. This
section provides a **structured overview** of all available resources,
organized by topic and difficulty level.

This page provides several links to available documentations regarding
`TFEL` and `MFront`, which are fairly detailed. Unfortunately, most of
these materials are written in French. They also mostly refer to
versions `2.0.x`, and thus do not describe the latest available version.

For a new (English speaking) user, we would highly recommend:

- Read the **reference paper** @helfer_introducing_2015. Although this
  paper covers versions `2.0.x`, it gives a good general overview of
  `TFEL` and `MFront`'s abilities.
- Read the [`getting-started` page](getting-started.md).
- Read the page dedicated to second and fourth order tensors,
  [here](tensors.md).
- Have a look at the [**gallery**](gallery.md) which details the
  implementations of various classical mechanical behaviours. Those
  implementations are kept up-to-date to use the latest developments
  and techniques introduced in `TFEL` and `MFront`.
- If none of the implementations described in the gallery match the user
  need, one may have a look at the implementations provided in the
  `mfront/tests/behaviours` directory in the sources. Beware that those
  implementations are not updated on purpose to ensure backward
  compatibility. Most of them can be simplified by using
  [bricks](BehaviourBricks.md).
- Finally, you may want to have a look at the documentation of the
  interface of the solver that you plan to use (see below for links).

For Spanish users, Jordi Alberich has written "A Spanish introduction
to `MFront` and `Salome-MECA`", which is available
[here](tutorial-spanish.md).

# MFront documentation

## Tutorials & Examples

Learn by doing with hands-on examples.

| Resource | Description | Language | Difficulty |
|----------|-------------|----------|------------|
| [MFront Gallery](gallery.md) | Step-by-step implementations of classical behaviours. | English | ⭐⭐ |
| [Tutorial (French)](tutorial.md) | Complete tutorial for beginners (Norton law example). | French | ⭐⭐ |
| [Spanish Tutorial](tutorial-spanish.md) | Introduction to MFront and Salome-MECA. | Spanish | ⭐⭐ |
| [Behaviour Examples](https://github.com/thelfer/tfel/tree/master/mfront/tests/behaviours) | Official test cases (GitHub). | Code | ⭐⭐⭐ |

## Courses

- General introduction: [mfront-presentation.pdf](documents/mfront-presentation/mfront-presentation.pdf)
- Writing mechanical behaviours [mfront-behaviours.pdf](documents/mfront-behaviours/mfront-behaviours.pdf)
- General introduction [mfront-formation.pdf](documents/mfront-formation/mfront-formation.pdf)
    - [tp.pdf](documents/tp/tp.pdf)

## Talks

- Finite strain: [mfront-finitestrain.pdf](documents/mfront-finitestrain/mfront-finitestrain.pdf)
- [Writing portable behaviours](documents/portable-behaviour/portability.md)

A `github` repository has been set up to store various documents
describing TFEL and MFront usage. The talks of the first and second
MFront Users are available there:

<https://github.com/thelfer/tfel-doc>

## Material Knowledge Types

| Resource | Description |
|----------|-------------|
| [Material Properties](material-properties.md) | How to define material properties (e.g., Young's modulus, thermal conductivity). |
| [Mechanical Behaviours](behaviours.md) | In-depth guide to implementing mechanical behaviours. |
| [Models](models.md) | Simple point-wise models (e.g., swelling for fuel performance codes). |

## Domain specific languages

| Resource | Description |
|----------|-------------|
| [Implicit](implicit-dsl.md) | Implicit integration for strain-based behaviours. |

## Bricks and Extensions

| Resource | Description |
|----------|-------------|
| [Behaviour Bricks](BehaviourBricks.md)          | Pre-defined bricks to simplify behaviour implementation. |
| [`StandardElastoViscoplasticity` brick](StandardElastoViscoPlasticityBrick.md) | Brick allowing to implement a vast class of plastic and viscoplastic behaviours |
| [`StandardElasticity`](HookeStressPotential.md) | Brick used by behaviours based on an elastic part described by Hooke's law|
| [`FiniteStrainSingleCrystal`](finitestrainsinglecrystal.md) | Brick dedicated to finite strain behaviour describing single crystals |
| [`DDIF2` brick](DDIF2Brick.md)                  | Brick based the `DDIF2` damage law used in various fuel performance code developed at CEA |

## Homogenization

| Resource | Description |
|----------|-------------|
| [Sachs Scheme](Sachs.md) | Lower bound for polycrystals. |
| [Taylor Scheme](Taylor.md) | Upper bound for polycrystals. |
| [Ponte Castaneda](PonteCastaneda1992.md) | Non-linear elastic composites. |
| [Masson Affine Formulation](MassonAffineFormulation.md) | Affine formulation for viscoplastic polycrystals. |
| [Biphasic Linear Homogenization](BiphasicLinearHomogenization.md) | Homogenization for biphasic media. |
| [β-Rule](BetaRule.md) | Implementation of the β-rule for homogenization. |

## Post-Processing & Outputs

| Resource | Description |
|----------|-------------|
| [Post-Processings](post-processings.md) | How to extract and analyze results. |
| [Parameters](parameters.md) | Material parameters and their usage. |

## Interfaces

### Interfaces dedicated to material properties

| Interface| Description | Documentation |
|--------|-------------|----------------|
| **Generic interface** | For use with the [MGIS project](https://thelfer.github.io/mgis/web/index.html). | [Generic Interface]( generic-material-property-interface.md) |
| **Generic parallel interface** | For use with the [MGIS project](https://thelfer.github.io/mgis/web/index.html). | [Generic Interface](generic-parallel-material-property-interface.md) |

### Mechanical behaviours

TFEL/MFront supports multiple finite element solvers. Each interface has its own documentation.

| Interface | Description | Documentation |
|--------|-------------|----------------|
| **Abaqus** | Commercial FEA solver (Standard/Explicit). | [Abaqus Interface](abaqus.md) |
| **Code_Aster** | Open-source FEA solver developped by EDF. | [Aster Interface](aster.md) |
| **Cast3M** | CEA's finite element solver. | [Cast3M Interface](castem.md) |
| **CalculiX** | Open-source FEA solver. | [CalculiX Interface](calculix.md) |
| **ANSYS** | Commercial FEA solver (APDL). | [ANSYS Interface](ansys.md) |
| **ZeBuLoN (Zmat)** | Zset's finite element solver. | [Zmat Interface](zmat.md) |
| **Cyrano** | Fuel performance code (CEA). | [Cyrano Interface](cyrano.md) |
| **ElmerFEM** | Open-source multiphysics solver. | [ElmerFEM Interface](elmerfem.md) |
| **AMITEX_FFTP** | FFT-based solver. | [AMITEX Interface](amitex.md) |
| **Generic interface** | For use with the [MGIS project](https://thelfer.github.io/mgis/web/index.html). | [Generic Interface](generic-behaviours-interface.md) |

## Advanced topics ⭐⭐/⭐⭐⭐

| Resource | Description |
|----------|-------------|
| [Theory](theory.md) | Theoretical background for material behaviours. |
| [mfront types](mfront-types.md) | Predefined aliases in `MFront` |
| [The `@BehaviourVariable` keyword](behaviour-variable.md) | Calling behaviours inside behaviours |
| [Unicode](unicode.md) | Unicode support in `MFront` |
| [Glossary](glossary.md) | Definitions of all TFEL/MFront terms. |
| [madnex](madnex.md) | Support of `madnex` files in `MFront` |
| [mfront-query](mfront-query.md) | Command line queries about MFront files |
| [mfront-doc](mfront-doc.md) | A documentation generator from MFront files |
| [The `mfm` tool](mfm.md) | A tool for querying entry points in `MFront` generated libraries |
| [Compilation process](compiling-mfront-shared-libraries.md) | Compilation process used by `MFront`|
| [Fisher-Burmeister complementary function](FischerBurmeister.md) | On the Fisher-Burmeister complementary function and its applications to multi-surface plasticity |
| [Extending StandardElastoViscoPlasticity](ExtendingStandardElastoViscoPlasticityBrick-StressCriterion.md) | How to extend standard bricks with custom criteria. |

## Keywords associated with Domain-Specific Languages (DSL)

Note the those pages may be outdated or can not apply to your particular
installation of `TFEL/MFront`. We highly recommend using the command
line to retrieve the list of keywords associated with a `DSL` or the
documentation associated with a keyword.

| DSL | Description | Keywords Reference |
|-----|-------------|---------------------|
| Implicit | Implicit integration for strain-based behaviours. | [Implicit Keywords](Implicit-keywords.md) |
| Default | Generic DSL for custom integration algorithms. | [Default Keywords](Default-keywords.md) |
| Runge-Kutta | Explicit integration for ODE-based behaviours. | [Runge-Kutta Keywords](RungeKutta-keywords.md) |
| IsotropicPlasticMisesFlow | DSL for isotropic J₂ plasticity. | [Keywords](IsotropicPlasticMisesFlow-keywords.md) |

# Testing & Validation ⭐⭐

Tools and guides for testing your implementations.

| Resource | Description |
|----------|-------------|
| [MTest](mtest.md) | TFEL's testing tool for material point simulations. |
| [Simulation of pipes](ptest.md) | Simulation of pipes in MTest. |
| [MTest Nonlinear Constraints](mtest-nonlinear-constraints.md) | Advanced constraints in MTest. |
| [TFEL-Check](tfel-check.md) | Validation suite for TFEL. |
| [MTest Keywords](MTest-keywords.md) | Keywords reference for MTest. |
| [mfm-test-generator](mfm-test-generator.md) | Generation of integration tests for various solvers. |

# Python modules ⭐⭐

| Resource | Description |
|----------|-------------|
| [TFEL Python](tfel-python.md) | bindings for TFEL libraries. |
| [MFront Python](mfront-python.md) | Python bindings for MFront. |
| [MTest Python](mtest-python.md) | Python bindings for MTest. |

# Advanced Topics ⭐⭐/⭐⭐⭐

For experienced users.

## TFEL libraries

| Library | Description |
|----------|-------------|
| [TFEL/Math](tfel-math.md) | Overview of the TFEL/Math library. |
| [TFEL/Material](tfel-material.md) | Overview of the TFEL/Material library. |
| [TFEL/PhysicalConstants](physical-constants.md) | Pre-defined physical constants in TFEL. |
| [TFEL/MFrontDataBase](tfel-mfront-database.md) | Utilities to handle MFront generated libraries. |
| [TFEL/System](TFELSystem.md) | Overview of the TFEL/System library. |
| [TFEL/Config](tfel-config.md) | Overview of the TFEL/Config library. |

Usage of the TFEL libraries in `C++` is described in [this page](libraries_usage.md).

## Mathematical Foundations

| Resource | Description |
|----------|-------------|
| [Tensors](tensors.md) | Operations on 2nd and 4th order tensors (TFEL/Math). |
| [Numerical Integration](tfel-math-numerical-integration.md) | Numerical integration methods in TFEL. |
| [Data Interpolation](tfel-math-data-interpolation.md) | Interpolation techniques. |

## Doxygen documentation

The `Doxygen` documentation is available [here](https://thelfer.github.io/tfel/doxygen/index.html).

# Legend

- ⭐: Beginner
- ⭐⭐: Intermediate
- ⭐⭐⭐: Advanced

# External Resources

Additional materials (mostly outdated) and references.

| Resource | Description |
|----------|-------------|
| [TFEL/MFront Reference Manual (PDF)](documents/mfront/mfront.pdf) | Complete reference manual (French). |
| [Behaviours Manual (PDF)](documents/mfront/behaviours.pdf) | Guide to writing mechanical behaviours (French). |
| [planestress.pdf](documents/mfront/planestress.pdf) | How to handle plane stress in implicit schemes. |
| [finitestrain.pdf](documents/mfront/finitestrain.pdf) |  Finite strain behaviours. |
| [MTest User Guide (PDF)](documents/mtest/mtest.pdf) | MTest documentation. |
| [TFEL Doc Repository](https://github.com/thelfer/tfel-doc) | Additional talks, tutorials, and documents. |

# Bibliography

<!-- Local IspellDict: english -->
