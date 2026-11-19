<!-- source: c3po/physicsDrivers/CATHARE2Driver.py -->

# `c3po.physicsDrivers.CATHARE2Driver`

Contain the class `CATHARE2Driver`.

### `c3po.physicsDrivers.CATHARE2Driver.shortName(name)`

INTERNAL

### `c3po.physicsDrivers.CATHARE2Driver.buildName(keyword, cname, loc, irad=-1)`

INTERNAL

### `class c3po.physicsDrivers.CATHARE2Driver.CATHARE2Driver()  — bases: C2, PhysicsDriver`

This is the implementation of `PhysicsDriver` for CATHARE2.

#### `CATHARE2Driver.getMEDCouplingMajorVersion(self)`

#### `CATHARE2Driver.isMEDCoupling64Bits(self)`

#### `CATHARE2Driver.solveTimeStep(self)`

#### `CATHARE2Driver.computeTimeStep(self)`

#### `CATHARE2Driver.initTimeStep(self, dt)`

#### `CATHARE2Driver.validateTimeStep(self)`

#### `CATHARE2Driver.setStationaryMode(self, stationaryMode)`

#### `CATHARE2Driver.getStationaryMode(self)`

#### `CATHARE2Driver.abortTimeStep(self)`

#### `CATHARE2Driver.initialize(self)`

#### `CATHARE2Driver.terminate(self)`

#### `CATHARE2Driver.presentTime(self)`

#### `CATHARE2Driver.resetTime(self, time_)`

#### `CATHARE2Driver.getOutputMEDFieldDriver(self, name)`

! INTERNAL

#### `CATHARE2Driver.getOutputMEDDoubleField(self, name)`

#### `CATHARE2Driver.setInputMEDDoubleField(self, name, field)`

#### `CATHARE2Driver.getInputMEDDoubleFieldTemplate(self, name)`

#### `CATHARE2Driver.getOutputDoubleValue(self, name)`

#### `CATHARE2Driver.setInputDoubleValue(self, name, value)`

#### `CATHARE2Driver.post(self)`

INTERNAL
