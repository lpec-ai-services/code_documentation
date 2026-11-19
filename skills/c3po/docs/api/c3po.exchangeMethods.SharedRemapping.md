<!-- source: c3po/exchangeMethods/SharedRemapping.py -->

# `c3po.exchangeMethods.SharedRemapping`

Contain the class `SharedRemapping`.

### `c3po.exchangeMethods.SharedRemapping.computeCellsToScreenOut(mesh1, mesh2)`

INTERNAL

### `class c3po.exchangeMethods.SharedRemapping.Remapper(meshAlignment=False, offset=None, rescaling=1.0, rotation=0.0, outsideCellsScreening=False, reverseTransformations=True)  — bases: object`

Allow to share the mesh projection for different `SharedRemapping` objects by building them with the same instance of this class.

#### `Remapper.initialize(self, sourceMesh, targetMesh)`

INTERNAL

#### `Remapper.directRemap(self, field, defaultValue)`

INTERNAL

#### `Remapper.reverseRemap(self, field, defaultValue)`

INTERNAL

#### `Remapper.getMatrix(self)`

Export remapping matrix.

The matrix can be serialized using pickle, then it can be loaded using `setMatrix` method in order to save initialization time.

<div class="note">

<div class="title">

Note

</div>

This method requires scipy.

</div>

## Returns

> Matrix object.

#### `Remapper.setMatrix(self, matrix)`

Load remapping matrix.

This matrix is usually obtained by `exportMatrix` method.

<div class="note">

<div class="title">

Note

</div>

This method requires scipy.

</div>

## Parameters

matrix  
Matrix object.

#### `Remapper.exportMatrix(self, fileName)`

Export remapping matrix on file.

This file can be loaded using `loadMatrix` method in order to save initialization time.

## Parameters

fileName  
Name of the file to write in.

#### `Remapper.loadMatrix(self, fileName)`

Load remapping matrix from file.

This file is usually written by `exportMatrix` method.

<div class="note">

<div class="title">

Note

</div>

This method requires scipy.

</div>

## Parameters

fileName  
Name of the file to read from.

### `class c3po.exchangeMethods.SharedRemapping.SharedRemapping(remapper, reverse=False, defaultValue=0.0, linearTransform=(1.0, 0.0))  — bases: ExchangeMethod`

`SharedRemapping` is an `ExchangeMethod` which projects the input fields one by one before returning them as outputs, in the same order.

See `c3po.Exchanger.Exchanger.__init__`.

The method assumes that all input fields have the same mesh, and produces output fields on identical meshes.

This output mesh is the one of the first field passed to the method (obtained by `getInputMEDFieldTemplate`).

The input scalars are returned in the same order, without modification.

The initialization of the projection method (long operation) is done only once, and can be shared with other instances of `SharedRemapping` through a `Remapper` object.

#### `SharedRemapping.initialize(self, fieldsToGet, fieldsToSet)`

INTERNAL

#### `SharedRemapping.getPatterns(self)`

See `ExchangeMethod.getPatterns`.

#### `SharedRemapping.clean(self)`

See `ExchangeMethod.clean`.
