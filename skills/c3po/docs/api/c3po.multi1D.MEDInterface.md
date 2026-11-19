<!-- source: c3po/multi1D/MEDInterface.py -->

# `c3po.multi1D.MEDInterface`

Contain the class `MEDInterface`.

### `class c3po.multi1D.MEDInterface.MEDInterface(multi1DAPI, baseGrid, objectGrids=None)`

MEDInterface links a set of 1D objects with 3D MEDCoupling meshes.

#### `MEDInterface.getBaseMEDMesh(self)`

Return the 3D MEDCouling first level mesh (whose 2D base is `baseGrid`).

## Returns

> The 3D MEDCouling first level mesh.

#### `MEDInterface.getObjectMEDMesh(self)`

Return the 3D MEDCouling second level mesh (built using `objectGrids[i][j]` at each cell of the `BaseMEDMesh`).

## Returns

> The 3D MEDCouling second level mesh (and None if not defined).

#### `MEDInterface.getPartOfObjectMEDMesh(self, objectNames)`

Return the part of the 3D MEDCouling second level mesh associated with the provided object names.

## Parameters

objectNames : list  
List of object names for which the mesh is required.

## Returns

> The part of the 3D MEDCouling second level mesh, associated with the provided object names.

#### `MEDInterface.getField(self, fieldName)`

Return the 3D MEDCoupling field associated with fieldName.

<div class="note">

<div class="title">

Note

</div>

The field underlying mesh is either the same than `getBaseMEDMesh`, or the same than `getObjectMEDMesh`, depending on fieldName.

</div>

## Parameters

fieldName  
name of the required field.

## Returns

> The required 3D MEDCoupling field.

#### `MEDInterface.setField(self, fieldName, field)`

Set a 3D MEDCoupling field.

<div class="note">

<div class="title">

Note

</div>

The field underlying mesh must be the base one (`getBaseMEDMesh`) or the object one (`getObjectMEDMesh`), depending on `fieldName`. No projection is made.

</div>

## Parameters

fieldName  
Name of the field to set.

field  
MEDCoupling field with data to be set.
