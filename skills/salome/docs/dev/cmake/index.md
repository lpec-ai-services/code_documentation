<!-- source: https://docs.salome-platform.org/latest/dev/cmake/html/index.html -->

# SALOME - CMake build procedure

The section marked as ADVANCED need not be read by someone only trying to compile SALOME. Those
sections are intented to the core SALOME developers, to help them understand/fix/improve
the process.

Contents:

- [Introduction](intro.md)
- [Motivations and overview](intro.md#motivations-and-overview)
  - [CMake must be user-friendly](intro.md#cmake-must-be-user-friendly)
  - [Basic usage](intro.md#basic-usage)
  - [Variable reference](intro.md#variable-reference)
  - [Overview of the logic (advanced)](intro.md#overview-of-the-logic-advanced)
- [Anatomy of a CMakeLists.txt file](skeleton.md)
  - [Root CMakeLists.txt](skeleton.md#root-cmakelists-txt)
  - [CMakeLists.txt dedicated to the build of a target](skeleton.md#cmakelists-txt-dedicated-to-the-build-of-a-target)
- [Package detection mechanism](pkg.md)
  - [Philosophy](pkg.md#philosophy)
  - [Root dir variables and priority order](pkg.md#root-dir-variables-and-priority-order)
  - [Writing the detection macro of a new SALOME prerequisite](pkg.md#writing-the-detection-macro-of-a-new-salome-prerequisite)
  - [Writing a new generic detection macro (advanced)](pkg.md#writing-a-new-generic-detection-macro-advanced)
  - [Implementation details (advanced)](pkg.md#implementation-details-advanced)
- [Exposing a module’s configuration (advanced)](config.md)
  - [Principle](config.md#principle)
  - [Guidelines](config.md#guidelines)
  - [Configuration file](config.md#configuration-file)
- [Various guidelines and conventions (advanced)](various.md)
  - [Debugging CMake](various.md#debugging-cmake)
  - [General conventions](various.md#general-conventions)
  - [Naming conventions](various.md#naming-conventions)
  - [Parallel compilation - Correct dependencies](various.md#parallel-compilation-correct-dependencies)
  - [Command specific conventions](various.md#command-specific-conventions)

# Indices and tables

- [Index](genindex.md)
- [Module Index](py-modindex.md)
- [Search Page](search.md)
