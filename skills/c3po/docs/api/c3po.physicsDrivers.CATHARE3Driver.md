<!-- source: c3po/physicsDrivers/CATHARE3Driver.py -->

# `c3po.physicsDrivers.CATHARE3Driver`

Contain the class `CATHARE3Driver`.

### `c3po.physicsDrivers.CATHARE3Driver.shortName(name)`

INTERNAL

### `c3po.physicsDrivers.CATHARE3Driver.buildName(keyword, cname, loc, irad=-1)`

INTERNAL

### `class c3po.physicsDrivers.CATHARE3Driver.CATHARE3Driver(dtPost=0.0)  — bases: C3, PhysicsDriver`

This is the implementation of `PhysicsDriver` for CATHARE3.

#### `CATHARE3Driver.getMEDCouplingMajorVersion(self)`

#### `CATHARE3Driver.isMEDCoupling64Bits(self)`

#### `CATHARE3Driver.solveTimeStep(self)`

#### `CATHARE3Driver.computeTimeStep(self)`

#### `CATHARE3Driver.initTimeStep(self, dt)`

#### `CATHARE3Driver.validateTimeStep(self)`

#### `CATHARE3Driver.setStationaryMode(self, stationaryMode)`

#### `CATHARE3Driver.getStationaryMode(self)`

#### `CATHARE3Driver.abortTimeStep(self)`

#### `CATHARE3Driver.initialize(self)`

#### `CATHARE3Driver.terminate(self)`

#### `CATHARE3Driver.presentTime(self)`

#### `CATHARE3Driver.resetTime(self, time_)`

#### `CATHARE3Driver.getOutputMEDFieldDriver(self, name)`

INTERNAL

#### `CATHARE3Driver.getRowland(self, cname, loc)`

INTERNAL

#### `CATHARE3Driver.getWeightedVolume(self, cname, loc, irad=-1)`

INTERNAL

#### `CATHARE3Driver.getOutputMEDDoubleField(self, name)`

#### `CATHARE3Driver.setInputMEDDoubleField(self, name, field)`

#### `CATHARE3Driver.getInputMEDDoubleFieldTemplate(self, name)`

#### `CATHARE3Driver.post(self, postMED)`

INTERNAL
