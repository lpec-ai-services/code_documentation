---
title: MFront, a code generation tool dedicated to material knowledge
author: Helfer Thomas, Jean-Michel Proix
date: 15/08/2014
lang: en-EN
---

# Overview

`TFEL` is a collaborative development of
[CEA](http://www.cea.fr/english-portal "Commissariat à l'énergie
atomique") and [EDF](http://www.edf.com/ "Électricité de France").

`MFront` is a code generator which translates a set of closely related
domain specific languages into plain [C++](http://isocpp.org/) on top
of the `TFEL` library. Those languages cover three kinds of material
knowledge:

- [material properties](material-properties.md) (for instance the
  Young's modulus, the thermal conductivity, etc.)
- [mechanical behaviours](behaviours.md). Numerical performance of
  generated mechanical behaviours was given particular
  attention. [Various benchmarks](benchmark.md) show that `MFront`
  implementations are competitive with native implementations
  available in the `Cast3M`, `Code-Aster`, `Abaqus Standard` and
  `Cyrano3` solvers.
- [simple point-wise models](models.md), such as material swelling
  used in fuel performance codes.

A set of interfaces are provided for various solvers:

- the [`Cast3M`](http://www-cast3m.cea.fr) finite element solver. This
  interface is described [here](castem.md).
- the [`Code_Aster`](http://www.code-aster.org) finite element
  solver. This interface is described [here](aster.md)
- the
  [`Abaqus Standard`](http://www.3ds.com/products-services/simulia/products/abaqus/abaqusstandard/)
  finite element solver. This interface is described
  [here](abaqus.md).
- the
  [`Abaqus Explicit`](http://www.3ds.com/products-services/simulia/products/abaqus/abaqusexplicit/)
  finite element solver. This interface is described
  [here](abaqus.md).
- the
  [`CalculiX`](http://www.calculix.de/)
  finite element solver. This interface is described
  [here](calculix.md).
- the [`ANSYS Mechanical APDL`](https://www.ansys.com/) finite element
  solver. This interface is described [here](ansys.md).
- the [`ZeBuLoN`](http://www.zset-software.com/products/zebulon)
  finite element solver. This interface is described [here](zmat.md).
- the `TMFFT` and the
  [`AMITEX_FFTP`](https://amitexfftp.github.io/AMITEX/)
  Fast Fourier Transform solvers developed internally at
  [CEA](http://www.cea.fr/english-portal "Commissariat à l'énergie
  atomique"). Note that
  [`AMITEX_FFTP`](http://www.maisondelasimulation.fr/projects/amitex/html/)
  is distributed under a free license for research and education
  purposes. Those solvers reuse the interface developed for the
  [`Cast3M`](http://www-cast3m.cea.fr) finite element solver.
- the [`ElmerFEM`](https://www.elmerfem.org/blog/) multiphysics
  solver. This interface is described [here](elmerfem.md).

For material properties, various interfaces are also provided and
cover the following languages: `C`, `C++`, `python`, `fortran`, etc.

# Getting Started

New to TFEL/MFront? Start here!

| Resource | Description | Difficulty |
|----------|-------------|------------|
| [Getting Started](getting-started.md) | Step-by-step guide for beginners. | ⭐ |
| [Installation Guide](install.md) | How to install TFEL/MFront on Linux, Windows, macOS, and FreeBSD. | ⭐/⭐⭐ |
| [Documentation](documentations.md) | List of all available documentation. | ⭐/⭐⭐/⭐⭐⭐ |
| [FAQ](faq.md) | Frequently asked questions and troubleshooting. | ⭐ |

- ⭐: Beginner
- ⭐⭐: Intermediate
- ⭐⭐⭐: Advanced

# Development & Contribution

For developers and contributors.

| Resource | Description |
|----------|-------------|
| [Contributing](contributing.md) | How to contribute to TFEL/MFront. |
| [Compiling MFront Shared Libraries](compiling-mfront-shared-libraries.md) | Guide for building shared libraries. |
| [CMake Options](https://github.com/thelfer/tfel/blob/master/CMakeLists.txt) | Advanced CMake configuration. |
| [Coverity Scan](coverity-scan.md) | Static analysis for TFEL. |
| [Running Sanitized Tests](sanitizers.md) | Building and testing TFEL/MFront with sanitizers. |
| [Fuzz Testing The Tokenizer](testing-fuzzing.md) | Running libFuzzer based analyses of the tokenizer of MFront files. |
| [Packages](packages.md) | Creating binary packages for TFEL. |
| [Release How-To](release-howto.md) | Preparing a TFEL/MFront release. |
| [TFEL System](TFELSystem.md) | Overview of TFEL's architecture. |

# Release Notes & History

Stay up-to-date with the latest changes.

| Version | Release Notes |
|---------|----------------|
| **5.x** | [v5.2](release-notes-5.2.md) |
| **5.1** | [v5.1](release-notes-5.1.md) |
| **5.0** | [v5.0](release-notes-5.0.md) |
| **4.x** | [v4.2](release-notes-4.2.md) |
| **3.x** | [v3.4](release-notes-3.4.md) |
| **All Versions** | [Release Notes Archive](./release-notes/) |

> **Note**: For a consolidated changelog, see [CHANGELOG.md](CHANGELOG.md).

# Community & Support

Get help and connect with the TFEL/MFront community.

| Resource | Description |
|----------|-------------|
| [GitHub Discussions](https://github.com/thelfer/tfel/discussions) | Ask questions, share ideas. |
| [GitHub Issues](https://github.com/thelfer/tfel/issues) | Report bugs or request features. |
| [Mailing List](mailto:tfel-contact@cea.fr) | Official contact for support. |
| [Associated Projects](associated-projects.md) | Projects using or extending TFEL/MFront. |
| [Publications](publications.md) | Scientific papers and references. |
| [News](news.md) | Latest news and announcements. |

> **Note**: This documentation is a **work in progress**. Contributions are welcome! See [Contributing](contributing.md) for details.

# Licences

`TFEL` versions prior to 0.1 were released under both the LGPL and the
CECILL-B licences. A copy of those licences is included in the
distributions of TFEL.

`TFEL` versions 1.x were developed by CEA within the PLEIADES
project. Since svn revision 584, TFEL was part of the `PLEIADES`
project.

Starting from versions 2.x, TFEL has been publicly released under either
the GPL or the CECILL-A licence. A copy of those licences is delivered
with the sources of TFEL. CEA or EDF may also distribute this project
under specific licensing conditions. Since 2023, the linking exception
clause was added to the GPL licence.

Copyright (C) 2006-2013 CEA/DEN. All rights reserved. 
Copyright (C) 2014-2025 CEA/DEN, EDF R&D. All rights reserved. 

<!-- Local IspellDict: english -->
