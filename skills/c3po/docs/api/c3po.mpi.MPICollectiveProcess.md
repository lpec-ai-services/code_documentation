<!-- source: c3po/mpi/MPICollectiveProcess.py -->

# `c3po.mpi.MPICollectiveProcess`

Contain the class `MPICollectiveProcess`.

### `class c3po.mpi.MPICollectiveProcess.MPICollectiveProcess(mpiComm)  — bases: object`

`MPICollectiveProcess` defines a collective process.

In particuler, it allows, by inheritance (a new class that inherits from `MPICollectiveProcess` but be defined), to define a collective `c3po.PhysicsDriver.PhysicsDriver`: all processors will locally launch this component.
