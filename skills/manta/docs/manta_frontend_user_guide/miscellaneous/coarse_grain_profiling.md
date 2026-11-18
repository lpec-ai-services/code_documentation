<!-- source: https://manta-project.gitlab.io/manta/manta_frontend_user_guide/miscellaneous/coarse_grain_profiling.html -->

# Coarse grain profilings

Coarse grain profilings allows to have an overview of the resources
usage by manta in terms of CPU time and memory usage.

## Displaying resources usage

If the level of verbosity is set to `verboseDebug`, information
about resources usage is displayed at the end of each iteration of a
coupling scheme.

This behaviour can also be triggered by setting the
`printResourcesUsage` boolean parameter to true when constructing
the coupling scheme.

The displayed resources are described below and depends on the available profilers

### Example of usage

PYTHON

```python
cs = manta.CouplingScheme('IterativeCouplingScheme', ps,
                          maximumNumberOfIterations = 500,
                          printResourcesUsage = True)
```

### Example of output

The following code shows the information displayed at the end of an
iteration of the coupling scheme used for a simple uniaxial tensile test
by the two profilers enabled by default (getrusage and PETSc):

```
- resources usage of 'LoopCouplingScheme::computeNextState':
  - initial resources:
    - getrusage: total system CPU time used (s) (for all MPI processes): 2.050563
    - getrusage: system CPU time used (s) per MPI process:  2.050563
    - getrusage: system CPU time used (s): 2.050563
    - getrusage: total user CPU time used (s) (for all MPI processes): 5.270943
    - getrusage: user CPU time used (s) per MPI process:  5.270943
    - getrusage: user CPU time used (s): 5.270943
    - getrusage: total maximum resident set size (Mb) (for all MPI processes): 84.968000
    - getrusage: maximum resident set size (Mb): 84.968000
    - getrusage: maximum resident set size (Mb) per MPI process:  84.968000
    - PETSc: maximum resident set size (Mb): 0.000000
    - PETSc: current resident set size (Mb): 77.570048
  - final resources:
    - getrusage: total system CPU time used (s) (for all MPI processes): 2.064403
    - getrusage: system CPU time used (s) per MPI process:  2.064403
    - getrusage: system CPU time used (s): 2.064403
    - getrusage: total user CPU time used (s) (for all MPI processes): 5.322976
    - getrusage: user CPU time used (s) per MPI process:  5.322976
    - getrusage: user CPU time used (s): 5.322976
    - getrusage: total maximum resident set size (Mb) (for all MPI processes): 84.968000
    - getrusage: maximum resident set size (Mb): 84.968000
    - getrusage: maximum resident set size (Mb) per MPI process:  84.968000
    - PETSc: maximum resident set size (Mb): 86.745088
    - PETSc: current resident set size (Mb): 86.745088
```

The *initial resources* and *final resources* sections shows the
resources usage at the beginning of the iteration and at the end of the
iteration respectively.

The information whose labels start with *getrusage* are obtained by the
`getrusage` system call. The user may refer to the documentation of
this system call for further details.

The information whose labels start with *PETSc* are obtained by calling
the following functions: `PetscMemoryGetCurrentUsage` and
`PetscMemoryGetMaximumUsage`. The user may refer to the [PETSc
documentation](https://petsc.org) for further details.
