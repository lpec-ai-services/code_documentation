<!-- source: c3po/Coupler.py -->

# `c3po.Coupler`

Contain the class `Coupler`.

### `class c3po.Coupler.NormChoice  — bases: object`

Enum definition of norm choice.

Values :  
- `normMax`
- `norm2`

### `class c3po.Coupler.Coupler(physics, exchangers, dataManagers=[])  — bases: PhysicsDriver`

`Coupler` is the base class for the definition of a coupling.

A coupling is defined using `PhysicsDriver`, `DataManager` and `Exchanger` objects. A user needs to define his own class inheriting from `Coupler` and to define its `solveTimeStep()` method. It may also be necessary to overload the I/O methods (for fields and/or of scalars) inherited from `PhysicsDriver`.

<div class="note">

<div class="title">

Note

</div>

`Coupler` inherits from `PhysicsDriver`, it is therefore possible to couple of `Coupler` objects!

</div>

#### `Coupler.getMEDCouplingMajorVersion(self)`

See `PhysicsDriver.getMEDCouplingMajorVersion`.

#### `Coupler.isMEDCoupling64Bits(self)`

See `PhysicsDriver.isMEDCoupling64Bits`.

#### `Coupler.initialize(self)`

See `PhysicsDriver.initialize`.

#### `Coupler.terminate(self)`

See `PhysicsDriver.terminate`.

#### `Coupler.presentTime(self)`

See `PhysicsDriver.presentTime`.

#### `Coupler.computeTimeStep(self)`

See `PhysicsDriver.computeTimeStep`.

#### `Coupler.initTimeStep(self, dt)`

See `PhysicsDriver.initTimeStep`.

#### `Coupler.getSolveStatus(self)`

See `PhysicsDriver.getSolveStatus`.

#### `Coupler.validateTimeStep(self)`

See `PhysicsDriver.validateTimeStep`.

#### `Coupler.setStationaryMode(self, stationaryMode)`

See `PhysicsDriver.setStationaryMode`.

#### `Coupler.getStationaryMode(self)`

See `PhysicsDriver.getStationaryMode`.

#### `Coupler.abortTimeStep(self)`

See `PhysicsDriver.abortTimeStep`.

#### `Coupler.isStationary(self)`

See `PhysicsDriver.isStationary`.

#### `Coupler.resetTime(self, time_)`

See `PhysicsDriver.resetTime`.

#### `Coupler.getIterateStatus(self)`

See `PhysicsDriver.getSolveStatus`.

#### `Coupler.setNormChoice(self, choice)`

Choose a norm for future use.

## Parameters

choice : `NormChoice.normMax`, `NormChoice.norm2`  
To be choosen between :

- `NormChoice.normMax` : infinite norm. This is the default choice.
- `NormChoice.norm2` : norm 2 ( `sqrt(sum_i(val[i] * val[i]))` ).

#### `Coupler.getNorm(self, data)`

Return the norm choosen by `setNormChoice` of `data` (a `DataManager`).

## Parameters

data : DataManager  
A `DataManager` object.

## Returns

> The asked norm of data.

#### `Coupler.readNormData(self)`

Return a list of the norms of the `DataManager` objects hold by `self`.

## Returns

list  
List of the norm of the `DataManager` objects.

#### `Coupler.normalizeData(self, norms)`

Divide the `DataManager` objects by the scalar values provided.

## Parameters

norms : list  
List of scalar values. The `DataManager` are divided by these scalars.

#### `Coupler.denormalizeData(self, norms)`

Multiply the `DataManager` objects by the scalar values provided.

## Parameters

norms : list  
List of scalar values. The `DataManager` are multiplied by these scalars.
