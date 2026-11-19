<!-- source: c3po/mpi/mpiExchangeMethods/MPIExchangeMethod.py -->

# `c3po.mpi.mpiExchangeMethods.MPIExchangeMethod`

Contain the class `MPIExchangeMethod`.

### `class c3po.mpi.mpiExchangeMethods.MPIExchangeMethod.MPIExchangeMethod  — bases: ExchangeMethod`

`MPIExchangeMethod` is a class interface (to be implemented) which standardizes MPI exchange methods (they also deal with MPI exchanges).

#### `MPIExchangeMethod.setRanks(self, ranksToGet, ranksToSet, mpiComm)`

Set the MPI communicator and the related ranks to use for the exchanges.

## Parameters

ranksToGet  
List of the ranks of the processes on the get side.

ranksToSet  
List of the ranks of the processes on the set side.

mpiComm  
MPI communicator related to the previous ranks.
