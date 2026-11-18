<!-- source: https://tripoli5.asnr.dev/documentation/latest-release/index.html -->

# TRIPOLI-5® Documentation

TRIPOLI-5® is a continuous-energy neutron transport Monte Carlo code jointly developed by SERMA [[1]](#serma) at CEA [[2]](#cea) and SNC [[3]](#snc) at ASNR [[4]](#asnr) with the support of EDF [[5]](#edf).
Initially developped for nuclear reactor physics applications, it is capable of simulating fixed source and criticality problems.
Its geometric description relies on a constructive solid geometry or on the ROOT library, the nuclear data rely on binary files that can be generated from ACE formatted files.
The parallel capabilities of TRIPOLI-5® rely on a hybrid MPI, OpenMP and CUDA implementations.

The publication for citing TRIPOLI-5® is

D. Mancusi et al., “Overview of TRIPOLI-5, a Monte Carlo code for HPC”, EPJ N 10
(2024) 26, DOI: [10.1051/epjn/2024028](https://doi.org/10.1051/epjn/2024028)

## Examples

In this section, you will find tutorials and examples for TRIPOLI-5® usage.

- [Examples](examples/index.md)

## Validation

In this section, you will find extended validation tests.

- [Validation suite](validation/index.md)

## Theory

This section contains the documentation concerning theoretical aspects of the
TRIPOLI-5® Monte Carlo code.

- [Theory](theory/index.md)

## Python API

This section will contain a “user manual” in the form of a Python API description.

- [The Python API](api/python-api.md)

## Release notes

- [Changelog](release/changelog.md)
- [Known bugs](release/known_bugs.md)

Footnotes

[[1](#id1)]

Service d’Études des Réacteurs et de Mathématiques Appliquées

[[2](#id2)]

French Alternative Energies and Atomic Energy Commission

[[3](#id3)]

Service de Neutronique et de Criticité

[[4](#id4)]

French Authority for Nuclear Safety and Radiation Protection

[[5](#id5)]

Electricité de France
