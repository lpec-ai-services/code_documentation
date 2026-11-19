<!-- source: c3po/CollaborativeDataManager.py -->

# `c3po.CollaborativeDataManager`

Contain the class `CollaborativeDataManager`.

### `class c3po.CollaborativeDataManager.CollaborativeDataManager(dataManagers)  — bases: DataManager, CollaborativeObject`

`CollaborativeDataManager` is a `DataManager` that handles a set of `DataManager` as a single one.

#### `CollaborativeDataManager.ignoreForConstOperators(self, indexToIgnore)`

INTERNAL

#### `CollaborativeDataManager.clone(self)`

Return a clone of `self`.

## Returns

CollaborativeDataManager  
A clone of `self`. Data are copied.

#### `CollaborativeDataManager.cloneEmpty(self)`

Return a clone of `self` without copying the data.

## Returns

CollaborativeDataManager  
An empty clone of `self`.

#### `CollaborativeDataManager.copy(self, other)`

Copy data of other in `self`.

## Parameters

other : CollaborativeDataManager  
A `CollaborativeDataManager` with the same list of data than `self`.

## Raises

Exception  
If `self` and `other` are not consistent.

#### `CollaborativeDataManager.normMax(self)`

Return the infinite norm.

## Returns

> The max of the absolute values of the scalars and of the infinite norms of the MED fields.

#### `CollaborativeDataManager.norm2(self)`

Return the norm 2.

## Returns

> `sqrt(sum_i(val[i] * val[i]))` where `val[i]` stands for each scalar and each component of the MED fields.

#### `CollaborativeDataManager.checkBeforeOperator(self, other)`

INTERNAL Make basic checks before the call of an operator.

#### `CollaborativeDataManager.imuladd(self, scalar, other)`

Add in `self` `scalar * other` (in place operation).

In order to do so, `other *= scalar` and `other *= 1./scalar` are done.

For example `a.imuladd(b, c)`.

## Parameters

scalar  
A scalar value.

other : CollaborativeDataManager  
A `CollaborativeDataManager` with the same list of data than `self`.

## Returns

CollaborativeDataManager  
`self`.

## Raises

Exception  
If `self` and `other` are not consistent.

#### `CollaborativeDataManager.dot(self, other)`

Return the scalar product of `self` with `other`.

## Parameters

other : CollaborativeDataManager  
A `CollaborativeDataManager` with the same list of data than `self`.

## Returns

> The scalar product of `self` with `other`.

## Raises

Exception  
If `self` and `other` are not consistent.
