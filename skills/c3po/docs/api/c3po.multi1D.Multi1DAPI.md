<!-- source: c3po/multi1D/Multi1DAPI.py -->

# `c3po.multi1D.Multi1DAPI`

Contain the classes `Multi1DAPI` and `Multi1DWithObjectsAPI`.

### `class c3po.multi1D.Multi1DAPI.Multi1DAPI  — bases: ABC`

`Multi1DAPI` is an abstract class handling a set of 1D object.

#### `Multi1DAPI.getSize(self)`

Return the number of 1D objects handled by self.

## Returns

> The number of 1D objects.

#### `Multi1DAPI.getNumberOfCells(self, index)`

Return the number of cells of the 1D object with the required index.

## Parameters

index  
Index of the queried 1D object .

## Returns

> The number of cells in the required 1D object.

#### `Multi1DAPI.getCellSizes(self, index)`

Return the list of the sizes of the cells of the 1D object with the required index.

<div class="note">

<div class="title">

Note

</div>

The length of the returned list should be equal to `getNumberOfCells`.

</div>

## Parameters

index  
Index of the queried 1D object.

## Returns

list  
List with the sizes of the cells of the required 1D object.

#### `Multi1DAPI.getNature(self, fieldName)`

Return the nature of the field `fieldName`, which mush be available for `getValues`, using MEDCoupling enum.

## Parameters

fieldName  
Name of the field.

## Returns

> Nature of the field.

#### `Multi1DAPI.getValues(self, index, fieldName)`

Return the values of the field `fieldName` for the 1D object with the required index.

<div class="note">

<div class="title">

Note

</div>

The length of the returned list should be equal to `getNumberOfCells`.

</div>

## Parameters

index  
Index of the queried 1D object.

fieldName  
Name of the field.

## Returns

list  
List of values.

#### `Multi1DAPI.setValues(self, index, fieldName, values)`

Set the values of the field `fieldName` to the 1D object with the required index.

<div class="note">

<div class="title">

Note

</div>

The length of `values` should be equal to `getNumberOfCells`.

</div>

## Parameters

index  
Index of the queried 1D object.

fieldName  
Name of the field.

values : list  
List of values to set.

### `class c3po.multi1D.Multi1DAPI.Multi1DWithObjectsAPI  — bases: Multi1DAPI`

`Multi1DWithObjectsAPI` is an abstract class that extends `Multi1DAPI` with the possibility for each 1D object to hold internal objects.

These internal objects are named. They can differ from one 1D object to another. Values may be written and read from (or on) these internal objects. They may not be all involved in every set or get.

#### `Multi1DWithObjectsAPI.getObjectNames(self, index)`

Return the list of list of the names of the internal objects hold by the 1D object with the required index at each cell.

<div class="note">

<div class="title">

Note

</div>

The length of the returned list should be equal to `getNumberOfCells`.

</div>

## Parameters

index  
Index of the queried 1D object.

## Returns

list  
List (for each cell) of list of internal object names.

#### `Multi1DWithObjectsAPI.getObjectNamesInField(self, fieldName)`

Return the list of the names of the internal objects that are involved in get / set methods for the field `fieldName`.

<div class="note">

<div class="title">

Note

</div>

The names of all involved internal object should be listed, even if they appear in only one cell of one 1D object.

The ordering of the names must be coherent with `getObjectValues` and `setObjectValues` behavior.

</div>

<div class="note">

<div class="title">

Note

</div>

This method returns an empty list if the field is known but does not involve any internal object. It means that the field should be handled using Multi1DAPI methods. If the field is totally unknown, an exception is raised.

</div>

## Parameters

fieldName  
Name of the field.

## Returns

list  
List of internal object names involved in the required field.

#### `Multi1DWithObjectsAPI.getObjectValues(self, index, fieldName)`

Return the list of list of the values for the field `fieldName` for the 1D object with the required index (for each object and for each cell).

<div class="note">

<div class="title">

Note

</div>

The length of the returned list should be equal to the lenght of the list returned by `getObjectNamesInField(fieldName)`.

For every `i`, the length of the `i`-th components of the return list should be equal to `getNumberOfCells(index)`.

</div>

## Parameters

index  
Index of the queried 1D object.

fieldName  
Name of the field.

## Returns

list  
List of list of values.

#### `Multi1DWithObjectsAPI.setObjectValues(self, index, fieldName, values)`

Set the values for the field `fieldName` to the 1D object with the required index (for each object and for each cell).

<div class="note">

<div class="title">

Note

</div>

The length of values should be equal to the lenght of the list returned by `getObjectNamesInField(fieldName)`.

For every `i`, the length of `values[i]` should be equal to `getNumberOfCells(index)`.

</div>

## Parameters

index  
Index of the queried 1D object.

fieldName  
Name of the field.

values : list  
List of list of values to set.
