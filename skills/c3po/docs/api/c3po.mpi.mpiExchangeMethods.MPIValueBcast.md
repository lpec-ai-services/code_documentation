<!-- source: c3po/mpi/mpiExchangeMethods/MPIValueBcast.py -->

# `c3po.mpi.mpiExchangeMethods.MPIValueBcast`

Contain the class `MPIValueBcast`.

### `class c3po.mpi.mpiExchangeMethods.MPIValueBcast.MPIValueBcast(reduceOp=None)  — bases: MPIExchangeMethod`

`MPIValueBcast` can be used to exchange values between two sets of processes.

A reduce is first made on the source processes, then the result is broacasted on the target processes.

#### `MPIValueBcast.setRanks(self, ranksToGet, ranksToSet, mpiComm)`

See `MPIExchangeMethod.setRanks`.

#### `MPIValueBcast.getPatterns(self)`

See `ExchangeMethod.getPatterns`.

#### `MPIValueBcast.clean(self)`

See `ExchangeMethod.clean`.
