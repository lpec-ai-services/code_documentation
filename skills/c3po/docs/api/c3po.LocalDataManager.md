<!-- source: c3po/LocalDataManager.py -->

# `c3po.LocalDataManager`

Contain the class `LocalDataManager`.

### `class c3po.LocalDataManager.LocalDataManager()  — bases: DataManager, DataAccessor`

`LocalDataManager` is the implementation of `DataManager` for local data.

It also implements `DataAccessor`.

Data can be double, int, string, fields of double of fields of int. Only double and fields of double are affected by the methods herited from `DataManager`. Other data are just (shallow) copied in new objects created by these methods.

#### `LocalDataManager.clone(self)`

Return a clone of `self`.

## Returns

LocalDataManager  
A clone of `self`. Data are copied.

#### `LocalDataManager.cloneEmpty(self)`

Return a clone of `self` without copying the data.

## Returns

LocalDataManager  
An empty clone of `self`.

#### `LocalDataManager.copy(self, other)`

Copy data of other in `self`.

## Parameters

other  
A `LocalDataManager` with the same list of data than `self`.

## Raises

Exception  
If `self` and `other` are not consistent.

#### `LocalDataManager.normMax(self)`

Return the infinite norm.

## Returns

> The max of the absolute values of the scalars and of the infinite norms of the MED fields.

#### `LocalDataManager.norm2(self)`

Return the norm 2.

## Returns

> `sqrt(sum_i(val[i] * val[i]))` where `val[i]` stands for each scalar and each component of the MED fields.

#### `LocalDataManager.checkBeforeOperator(self, other)`

INTERNAL Make basic checks before the call of an operator: same data names between `self` and `other`.

#### `LocalDataManager.imuladd(self, scalar, other)`

Add in `self` `scalar * other` (in place operation).

In order to do so, `other *= scalar` and `other *= 1./scalar` are done.

For example `a.imuladd(b, c)`.

## Parameters

scalar  
A scalar value.

other : LocalDataManager  
A `LocalDataManager` with the same list of data then `self`.

## Returns

LocalDataManager  
`self`.

## Raises

Exception  
If `self` and `other` are not consistent.

#### `LocalDataManager.dot(self, other)`

Return the scalar product of `self` with `other`.

## Parameters

other : LocalDataManager  
A `LocalDataManager` with the same list of data then `self`.

## Returns

> The scalar product of `self` with `other`.

## Raises

Exception  
If `self` and `other` are not consistent.

#### `LocalDataManager.setInputMEDDoubleField(self, name, field)`

Store the MED field `field` under the name `name`.

## Parameters

name  
The name given to the field to store.

field  
A field to store.

#### `LocalDataManager.getOutputMEDDoubleField(self, name)`

Return the MED field of name `name` previously stored.

## Parameters

name  
The name of the field to return.

## Returns

> The MED field of name `name` previously stored.

## Raises

Exception  
If there is no stored `name` Double field.

#### `LocalDataManager.setInputMEDIntField(self, name, field)`

Similar to `setInputMEDDoubleField` but for MEDIntField.

#### `LocalDataManager.getOutputMEDIntField(self, name)`

Similar to `getOutputMEDDoubleField` but for MEDIntField.

#### `LocalDataManager.getFieldType(self, name)`

Return the type of a previously stored field.

#### `LocalDataManager.setInputDoubleValue(self, name, value)`

Store the scalar `value` under the name `name`.

## Parameters

name  
The name given to the scalar to store.

value  
A scalar value to store.

#### `LocalDataManager.getOutputDoubleValue(self, name)`

Return the scalar of name `name` previously stored.

## Parameters

name  
The name of the value to return.

## Returns

> The value of name `name` previously stored.

## Raises

Exception  
If there is no stored `name` Double value.

#### `LocalDataManager.setInputIntValue(self, name, value)`

Similar to `setInputDoubleValue` but for Int.

#### `LocalDataManager.getOutputIntValue(self, name)`

Similar to `getOutputDoubleValue` but for Int.

#### `LocalDataManager.setInputStringValue(self, name, value)`

Similar to `setInputDoubleValue` but for String.

#### `LocalDataManager.getOutputStringValue(self, name)`

Similar to `getOutputDoubleValue` but for String.

#### `LocalDataManager.getValueType(self, name)`

Return the type of a previously stored field.

#### `LocalDataManager.setInputMEDDoubleFieldTemplate(self, name, field)`

Store the MED field `field` as a MEDFieldTemplate under the name `name`.

<div class="note">

<div class="title">

Note

</div>

These fields are not be part of data, and will therefore not be taken into account in data manipulations (operators, norms etc.).

</div>

## Parameters

name  
The name given to the field to store.

field  
A field to store.

#### `LocalDataManager.getInputMEDDoubleFieldTemplate(self, name)`

Return the MED field previously stored as a MEDDoubleFieldTemplate under the name `name`. If there is not, returns 0.

## Parameters

name  
The name of the field to return.

## Returns

> The MED field of name `name` previously stored, or 0.
