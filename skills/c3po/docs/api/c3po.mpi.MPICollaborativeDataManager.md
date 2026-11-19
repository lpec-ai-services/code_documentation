<!-- source: c3po/mpi/MPICollaborativeDataManager.py -->

# `c3po.mpi.MPICollaborativeDataManager`

Contain the class `MPICollaborativeDataManager`.

### `class c3po.mpi.MPICollaborativeDataManager.MPICollaborativeDataManager(dataManagers, mpiComm=None)  — bases: CollaborativeDataManager`

`MPICollaborativeDataManager` is the MPI collaborative version of `c3po.CollaborativeDataManager.CollaborativeDataManager` (for collaborative MPI paradigm).

It allows to handle a set of `c3po.DataManager.DataManager` (some of then being remote) as a single one. Thanks to this class, data can be distributed on different MPI processes but still used in the same way.

When at least one `MPIRemote` is present, `MPICollaborativeDataManager` uses collective MPI communications: the object must be built and used in the same way for all the involved processes. They must all share the same communicator, and all the processes of that communicator must be involved.

#### `MPICollaborativeDataManager.cloneEmpty(self)`

Return a clone of `self` without copying the data.

## Returns

MPICollaborativeDataManager  
An empty clone of `self`.

#### `MPICollaborativeDataManager.normMax(self)`

Return the infinite norm.

## Returns

The max of the absolute values of the scalars and of the infinite norms of the MED fields.

#### `MPICollaborativeDataManager.norm2(self)`

Return the norm 2.

## Returns

`sqrt(sum_i(val[i] * val[i]))` where `val[i]` stands for each scalar and each component of the MED fields.

#### `MPICollaborativeDataManager.dot(self, other)`

Return the scalar product of `self` with `other`.

## Parameters

other : MPICollaborativeDataManager  
A `MPICollaborativeDataManager` consistent with `self`.

## Returns

> The scalar product of `self` with `other`.

## Raises

Exception  
If `self` and `other` are not consistent.
