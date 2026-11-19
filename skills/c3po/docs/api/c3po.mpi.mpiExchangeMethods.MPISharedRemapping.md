<!-- source: c3po/mpi/mpiExchangeMethods/MPISharedRemapping.py -->

# `c3po.mpi.mpiExchangeMethods.MPISharedRemapping`

Contain the class `SharedRemapping`.

### `class c3po.mpi.mpiExchangeMethods.MPISharedRemapping.MPIRemapper(meshAlignment=False, offset=None, rescaling=1.0, rotation=0.0, outsideCellsScreening=False, reverseTransformations=True)  — bases: object`

Allow to share the mesh projection for different `MPISharedRemapping` objects by building them with the same instance of this class.

#### `MPIRemapper.initialize(self, ranksToGet, ranksToSet, mpiComm, field)`

INTERNAL

#### `MPIRemapper.terminate(self)`

Release all allocated resources.

<div class="warning">

<div class="title">

Warning

</div>

This method must be called once the object is no more needed in order to properly release MPI resources.

</div>

#### `MPIRemapper.recvField(self, fieldTemplate)`

INTERNAL

#### `MPIRemapper.sendField(self, field)`

INTERNAL

### `class c3po.mpi.mpiExchangeMethods.MPISharedRemapping.MPISharedRemapping(remapper, reverse=False, defaultValue=0.0, linearTransform=(1.0, 0.0))  — bases: MPIExchangeMethod`

`MPISharedRemapping` is the MPI version of `c3po.exchangeMethods.SharedRemapping.SharedRemapping`.

MPI features of MEDCoupling must be available. It allows to use MEDCoupling projections between codes using domain decomposition methods.

#### `MPISharedRemapping.setRanks(self, ranksToGet, ranksToSet, mpiComm)`

See `MPIExchangeMethod.setRanks`.

#### `MPISharedRemapping.initialize(self, field)`

INTERNAL

#### `MPISharedRemapping.getPatterns(self)`

See `ExchangeMethod.getPatterns`.

#### `MPISharedRemapping.clean(self)`

See `ExchangeMethod.clean`.
