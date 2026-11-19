<!-- source: c3po/physicsDrivers/TRUSTDriver.py -->

# `c3po.physicsDrivers.TRUSTDriver`

Contain the class `TRUSTDriver`.

### `class c3po.physicsDrivers.TRUSTDriver.TRUSTDriver()  — bases: ti.ProblemTrio, PhysicsDriver`

This is the implementation of `PhysicsDriver` for TRUST. Since TRUST is ICoCo-compliant, not much to be done!

#### `TRUSTDriver.getMEDCouplingMajorVersion(self)`

#### `TRUSTDriver.isMEDCoupling64Bits(self)`

#### `TRUSTDriver.initialize(self)`

#### `TRUSTDriver.terminate(self)`

#### `TRUSTDriver.presentTime(self)`

#### `TRUSTDriver.computeTimeStep(self)`

#### `TRUSTDriver.initTimeStep(self, dt)`

#### `TRUSTDriver.solveTimeStep(self)`

#### `TRUSTDriver.validateTimeStep(self)`

#### `TRUSTDriver.setStationaryMode(self, stationaryMode)`

#### `TRUSTDriver.getStationaryMode(self)`

#### `TRUSTDriver.abortTimeStep(self)`

#### `TRUSTDriver.resetTime(self, time_)`

#### `TRUSTDriver.setInputMEDDoubleField(self, name, field)`

#### `TRUSTDriver.getInputMEDDoubleFieldTemplate(self, name)`

#### `TRUSTDriver.getOutputMEDDoubleField(self, name)`
