<!-- source: c3po/exchangeMethods/SharedRemappingMulti1D3D.py -->

# `c3po.exchangeMethods.SharedRemappingMulti1D3D`

Contain the class `SharedRemappingMulti1D3D`.

### `c3po.exchangeMethods.SharedRemappingMulti1D3D.shift1DFields(shiftMap, shiftedFieldPositions, indexTable)`

INTERNAL

### `class c3po.exchangeMethods.SharedRemappingMulti1D3D.Multi1D3DRemapper(xCoordinates, yCoordinates, indexTable, weights, meshAlignment=False, offset=None, rescaling=1.0, rotation=0.0, outsideCellsScreening=False, reverseTransformations=True)  — bases: Remapper`

Allow to share the mesh projection for different `SharedRemappingMulti1D3D` objects by building them with the same instance of this class.

#### `Multi1D3DRemapper.buildInnerField(self, meshes1D)`

INTERNAL

#### `Multi1D3DRemapper.getInnerField(self)`

INTERNAL

#### `Multi1D3DRemapper.build3DField(self, fields1D, defaultValue=0.0)`

INTERNAL

#### `Multi1D3DRemapper.build1DFields(self, field3D)`

INTERNAL

#### `Multi1D3DRemapper.getNumberOf1DFields(self)`

INTERNAL

#### `Multi1D3DRemapper.shift1DFields(self, shiftMap)`

This method allows to shift the index of the 1D fields provided through the indexTable parameter of constructor.

For example, `shiftMap=[3, -1, 1, 2]` indicates that at first call `field_0` goes to position 3, `field_1` is discharged, `field_2` goes to 1 and `field_3` goes to 2. It returns `[1]`. At the second call with the same input, `field_0` (now at position 3) goes to 2, `field_1` (at 0) goes to 3, `field_2` (at 1) is discharged and `field_3` (at 2) goes to 1. It returns `[2]`. The third call returns `[3]`, the fourth call `[0]`.

## Parameters

shiftMap : list  
A list providing for each 1D fields the index (in indexTable) of its new position (-1 can be used to indicate that the field is no more used).

## Returns

list  
The list of the indexes no more used.

#### `Multi1D3DRemapper.setShiftedIndex(self, shiftedFieldPositions, indexTable)`

INTERNAL

### `class c3po.exchangeMethods.SharedRemappingMulti1D3D.SharedRemappingMulti1D3D(remapper, reverse=False, defaultValue=0.0, linearTransform=(1.0, 0.0))  — bases: SharedRemapping`

`SharedRemappingMulti1D3D` is an ExchangeMethod which projects the input fields one by one before returning them as outputs, in the same order.

See `c3po.Exchanger.Exchanger.__init__`.

1D fields are processed in packets using the intermediate mesh defined by the `Multi1D3DRemapper` object.

The method assumes that all input fields (or packets) have the same mesh, and produces output fields on identical meshes.

This output mesh is the one of the first field (or packet) passed to the method (obtained by `getInputMEDFieldTemplate`).

The input scalars are returned in the same order, without modification.

The initialization of the projection method (long operation) is done only once, and can be shared with other instances of `SharedRemappingMulti1D3D`.

#### `SharedRemappingMulti1D3D.getPatterns(self)`

See `ExchangeMethod.getPatterns`.

#### `SharedRemappingMulti1D3D.clean(self)`

See `ExchangeMethod.clean`.
