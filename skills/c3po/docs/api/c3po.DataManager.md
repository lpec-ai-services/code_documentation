<!-- source: c3po/DataManager.py -->

# `c3po.DataManager`

Contain the class `DataManager`.

### `class c3po.DataManager.DataManager  — bases: object`

`DataManager` is a class interface (to be implemented) which standardizes methods to handle data outside of codes.

They are mainly mathematical operators needed for some coupling algorithms.

#### `DataManager.clone(self)`

Return a clone of `self`.

## Returns

DataManager  
A clone of `self`. Data are copied.

#### `DataManager.cloneEmpty(self)`

Return a clone of `self` without copying the data.

## Returns

DataManager  
An empty clone of `self`.

#### `DataManager.copy(self, other)`

Copy data of `other` in `self`.

## Parameters

other : DataManager  
A `DataManager` with the same list of data than `self`.

## Raises

Exception  
If `self` and `other` are not consistent.

#### `DataManager.normMax(self)`

Return the infinite norm.

## Returns

> The infinite norm of all data.

#### `DataManager.norm2(self)`

Return the norm 2.

## Returns

> `sqrt(sum_i(val[i] * val[i]))` where `val[i]` stands for each scalar and each component of stored data.

#### `DataManager.imuladd(self, scalar, other)`

Add in `self` `scalar * other` (in place operation).

In order to do so, `other *= scalar` and `other *= 1./scalar` are done.

For example `a.imuladd(b, c)`.

## Parameters

scalar  
A scalar value.

other : DataManager  
A `DataManager` with the same list of data then `self`.

## Returns

DataManager  
`self`.

## Raises

Exception  
If `self` and `other` are not consistent.

#### `DataManager.dot(self, other)`

Return the scalar product of `self` with `other`.

## Parameters

other : DataManager  
A `DataManager` with the same list of data then `self`.

## Returns

> The scalar product of `self` with `other`.

## Raises

Exception  
If `self` and `other` are not consistent.
