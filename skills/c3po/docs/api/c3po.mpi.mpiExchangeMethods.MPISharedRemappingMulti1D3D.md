<!-- source: c3po/mpi/mpiExchangeMethods/MPISharedRemappingMulti1D3D.py -->

# `c3po.mpi.mpiExchangeMethods.MPISharedRemappingMulti1D3D`

Contain the class `MPISharedRemappingMulti1D3D`.

### `class c3po.mpi.mpiExchangeMethods.MPISharedRemappingMulti1D3D.MPIMulti1D3DRemapper(xCoordinates, yCoordinates, indexTable, weights, physics, meshAlignment=False, offset=None, rescaling=1.0, rotation=0.0, outsideCellsScreening=False, reverseTransformations=True)  — bases: MPIRemapper`

Allow to share the mesh projection for different `MPISharedRemappingMulti1D3D` objects by building them with the same instance of this class.

#### `MPIMulti1D3DRemapper.buildInnerField(self, meshes1D)`

INTERNAL

#### `MPIMulti1D3DRemapper.getInnerField(self)`

INTERNAL

#### `MPIMulti1D3DRemapper.build3DField(self, fields1D, defaultValue=0.0)`

INTERNAL

#### `MPIMulti1D3DRemapper.build1DFields(self, field3D)`

INTERNAL

#### `MPIMulti1D3DRemapper.getNumberOf1DFields(self)`

INTERNAL

#### `MPIMulti1D3DRemapper.shift1DFields(self, shiftMap)`

See `Multi1D3DRemapper.shift1DFields`

### `class c3po.mpi.mpiExchangeMethods.MPISharedRemappingMulti1D3D.MPISharedRemappingMulti1D3D(remapper, reverse=False, defaultValue=0.0, linearTransform=(1.0, 0.0))  — bases: MPISharedRemapping`

`MPISharedRemappingMulti1D3D` is the MPI version of `c3po.exchangeMethods.SharedRemappingMulti1D3D.SharedRemappingMulti1D3D`.

#### `MPISharedRemappingMulti1D3D.getPatterns(self)`

See `ExchangeMethod.getPatterns`.

#### `MPISharedRemappingMulti1D3D.clean(self)`

See `ExchangeMethod.clean`.
