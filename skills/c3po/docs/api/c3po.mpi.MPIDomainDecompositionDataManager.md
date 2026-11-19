<!-- source: c3po/mpi/MPIDomainDecompositionDataManager.py -->

# `c3po.mpi.MPIDomainDecompositionDataManager`

Contain the class `MPIDomainDecompositionDataManager`.

### `class c3po.mpi.MPIDomainDecompositionDataManager.MPIDomainDecompositionDataManager(mpiComm)  — bases: LocalDataManager`

`MPIDomainDecompositionDataManager` is the MPI collaborative version of the `c3po.DataManager.DataManager` in which all processes have locally only a part of the data.

Can replace, without impact, a `c3po.LocalDataManager.LocalDataManager` for a calculation on a single process, if the MPI environment is available.

`MPIDomainDecompositionDataManager` behaves a little bit like a `MPICollaborativeDataManager` built with only one `LocalDataManager` and a `mpiComm`. However, unlike `MPICollaborativeDataManager` which will be expanded by `MPIExchanger`, and therefore seen as a simple `LocalDataManager` in this case, `MPIDomainDecompositionDataManager` will be directly handled by `MPIExchanger`. This is usually preferable when using a `c3po.mpi.mpiExchangeMethods.MPIExchangeMethod.MPIExchangeMethod` as exchange method.

#### `MPIDomainDecompositionDataManager.getMPIComm(self)`

(Optional) Return the MPI communicator used by the code for parallel computations.

## Returns

mpi4py.MPI.Comm  
mpi4py communicator.

#### `MPIDomainDecompositionDataManager.cloneEmpty(self)`

Return a clone of `self` without copying the data.

## Returns

MPIDomainDecompositionDataManager  
An empty clone of `self`.

#### `MPIDomainDecompositionDataManager.normMax(self)`

Return the infinite norm.

## Returns

The max of the absolute values of the scalars and of the infinite norms of the MED fields.

#### `MPIDomainDecompositionDataManager.norm2(self)`

Return the norm 2.

## Returns

`sqrt(sum_i(val[i] * val[i]))` where `val[i]` stands for each scalar and each component of the MED fields.

#### `MPIDomainDecompositionDataManager.dot(self, other)`

Return the scalar product of `self` with `other`.

## Parameters

other : MPICollaborativeDataManager  
A `MPICollaborativeDataManager` consistent with `self`.

## Returns

The scalar product of `self` with `other`.

## Raises

Exception  
If `self` and `other` are not consistent.

#### `MPIDomainDecompositionDataManager.getLocalView(self)`

Return a new `LocalDataManager` that holds the same data than `self`

## Returns

LocalDataManager  
A `LocalDataManager` that holds the same data than `self`
