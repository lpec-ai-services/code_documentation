<!-- source: c3po/mpi/MPICollectiveDataManager.py -->

# `c3po.mpi.MPICollectiveDataManager`

Contain the class `MPICollectiveDataManager`.

### `class c3po.mpi.MPICollectiveDataManager.MPICollectiveDataManager(mpiComm)  — bases: LocalDataManager, MPICollectiveProcess`

`MPICollectiveDataManager` is the MPI collaborative version of the `c3po.DataManager.DataManager` in which all processes have locally all data.

Can replace, without impact, a `c3po.LocalDataManager.LocalDataManager` for a calculation on a single process, if the MPI environment is available.

#### `MPICollectiveDataManager.cloneEmpty(self)`

Return a clone of `self` without copying the data.

## Returns

MPICollectiveDataManager  
An empty clone of `self`.
