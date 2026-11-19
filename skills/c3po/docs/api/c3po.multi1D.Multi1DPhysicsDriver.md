<!-- source: c3po/multi1D/Multi1DPhysicsDriver.py -->

# `c3po.multi1D.Multi1DPhysicsDriver`

Contain the classes `Multi1DPhysicsDriver` and `DriversAPI` and the function `shiftList`.

### `class c3po.multi1D.Multi1DPhysicsDriver.Multi1DPhysicsDriver(physics, grid, weights=None)  — bases: PhysicsDriverWrapper`

`Multi1DPhysicsDriver` allows to handle as a unique `PhysicsDriver` that reads and writes 3D fields a list of 1D `PhysicsDriver`.

#### `Multi1DPhysicsDriver.getPhysicsDrivers(self)`

Return the wrapped `PhysicsDriver` list.

## Returns

list\[PhysicsDriver\]  
The wrapped PhysicsDriver list.

#### `Multi1DPhysicsDriver.shiftPhysicsDrivers(self, shiftMap)`

Shift the hold `PhysicsDriver` according to `shiftMap`.

## Parameters

shiftMap : list\[int\]  
A list of integers of same length than `physics`. `shiftMap[i]` is the new position of `physics[i]`. 'wherever' can be used to indicate that this element is no more used. In this case, the associated `PhysicsDriver` is moved to one of the free positions.

## Returns

list\[PhysicsDriver\]  
The list of `PhysicsDriver` that were associated to 'wherever' in the `shiftMap`.

For example, `shiftMap=[3, 'wherever', 1, 2]` indicates that at first call `physics_0` goes to position 3, `physics_1` is discharged, `physics_2` goes to 1 and `physics_3` goes to 2. It returns `[physics_1]` (and `physics_1` goes to position 0). At the second call with the same input, `physics_0` (now at position 3) goes to 2, `physics_1` (at 0) goes to 3, `physics_2` (at 1) is discharged and `physics_3` (at 2) goes to 1. It returns `[physics_2]`. The thrid call returns `[physics_3]`, the fourth call `[physics_0]`, the fifth call `[physics_1]`.

#### `Multi1DPhysicsDriver.getInputFieldsNames(self)`

See `c3po.DataAccessor.DataAccessor.getInputFieldsNames`.

#### `Multi1DPhysicsDriver.getOutputFieldsNames(self)`

See `c3po.DataAccessor.DataAccessor.getOutputFieldsNames`.

#### `Multi1DPhysicsDriver.getFieldType(self, name)`

See `c3po.DataAccessor.DataAccessor.getFieldType`.

#### `Multi1DPhysicsDriver.getMeshUnit(self)`

See `c3po.DataAccessor.DataAccessor.getMeshUnit`.

#### `Multi1DPhysicsDriver.getFieldUnit(self, name)`

See `c3po.DataAccessor.DataAccessor.getFieldUnit`.

#### `Multi1DPhysicsDriver.getInputMEDDoubleFieldTemplate(self, name)`

See `c3po.DataAccessor.DataAccessor.getInputMEDDoubleFieldTemplate`.

#### `Multi1DPhysicsDriver.setInputMEDDoubleField(self, name, field)`

See `c3po.DataAccessor.DataAccessor.setInputMEDDoubleField`.

#### `Multi1DPhysicsDriver.getOutputMEDDoubleField(self, name)`

See `c3po.DataAccessor.DataAccessor.getOutputMEDDoubleField`.

#### `Multi1DPhysicsDriver.updateOutputMEDDoubleField(self, name, field)`

See `c3po.DataAccessor.DataAccessor.updateOutputMEDDoubleField`.

### `class c3po.multi1D.Multi1DPhysicsDriver.DriversAPI(physics, meshes, testIndex, weights=None)  — bases: Multi1DAPI`

`DriversAPI` implements `Multi1DAPI` with 1D `PhysicsDriver`.

#### `DriversAPI.getSize(self)`

See `Multi1DAPI.getSize`.

#### `DriversAPI.getNumberOfCells(self, index)`

See `Multi1DAPI.getNumberOfCells`.

#### `DriversAPI.getCellSizes(self, index)`

See `Multi1DAPI.getCellSizes`.

#### `DriversAPI.getNature(self, fieldName)`

See `Multi1DAPI.getNature`.

#### `DriversAPI.getValues(self, index, fieldName)`

See `Multi1DAPI.getValues`.

#### `DriversAPI.setValues(self, index, fieldName, values)`

See `Multi1DAPI.setValues`.

### `c3po.multi1D.Multi1DPhysicsDriver.shiftList(listToShift, shiftMap)`

Create a new list where elements of `listToShift` are shifted according to `shiftMap`.

<div class="note">

<div class="title">

Note

</div>

Users should not need to call this function directly.

</div>

## Parameters

listToShift : list  
The list to shift.

shiftMap : list\[int\]  
A list of integers of same length than `listToShift`. `shiftMap[i]` is the new position of `listToShift[i]`. 'wherever' can be used to indicate that an element can go to any free position. It is also returned by the function.

## Returns

list  
The list of `listToShift` elements that were associated to 'wherever' in the `shiftMap` and the new list with shifted elements.

For example, `shiftMap=[3, 'wherever', 1, 2]` indicates that at first call `listToShift[0]` goes to position 3, `listToShift[1]` is discharged, `listToShift[2]` goes to 1 and `listToShift[3]` goes to 2. It returns `([listToShift[1]], newlist)`. At the second call with the same input, `listToShift[0]` (now at position 3) goes to 2, `listToShift[1]` (at 0) goes to 3, `listToShift[2]` (at 1) is discharged and `listToShift[3]` (at 2) goes to 1. Its first return is now `[listToShift[2]]`. The thrid call first return is `[listToShift[3]]`, the fourth call first return `[listToShift[0]]`, the fifth call first return `[listToShift[1]]` etc.
