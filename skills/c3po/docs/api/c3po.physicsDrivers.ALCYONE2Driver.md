<!-- source: c3po/physicsDrivers/ALCYONE2Driver.py -->

# `c3po.physicsDrivers.ALCYONE2Driver`

Contain the class `ALCYONE2Driver`.

### `class c3po.physicsDrivers.ALCYONE2Driver.ALCYONE2Driver()  — bases: PhysicsDriver`

This is the implementation of `PhysicsDriver` for Alcyone2.

A Alcyone2Init method must be available. It has the internal Alcyone2 object as input.

#### `ALCYONE2Driver.getMEDCouplingMajorVersion(self)`

#### `ALCYONE2Driver.isMEDCoupling64Bits(self)`

#### `ALCYONE2Driver.setMPIComm(self, mpicomm)`

#### `ALCYONE2Driver.initialize(self)`

#### `ALCYONE2Driver.terminate(self)`

#### `ALCYONE2Driver.presentTime(self)`

#### `ALCYONE2Driver.computeTimeStep(self)`

#### `ALCYONE2Driver.initTimeStep(self, dt)`

#### `ALCYONE2Driver.solveTimeStep(self)`

#### `ALCYONE2Driver.validateTimeStep(self)`

#### `ALCYONE2Driver.setStationaryMode(self, stationaryMode)`

#### `ALCYONE2Driver.getStationaryMode(self)`

#### `ALCYONE2Driver.abortTimeStep(self)`

#### `ALCYONE2Driver.isStationary(self)`

#### `ALCYONE2Driver.resetTime(self, time_)`

#### `ALCYONE2Driver.iterateTimeStep(self)`

#### `ALCYONE2Driver.save(self, label, method)`

#### `ALCYONE2Driver.restore(self, label, method)`

#### `ALCYONE2Driver.forget(self, label, method)`

#### `ALCYONE2Driver.getInputFieldsNames(self)`

#### `ALCYONE2Driver.getOutputFieldsNames(self)`

#### `ALCYONE2Driver.getInputMEDDoubleFieldTemplate(self, name)`

#### `ALCYONE2Driver.getInputMEDIntFieldTemplate(self, name)`

#### `ALCYONE2Driver.setInputMEDDoubleField(self, name, field)`

#### `ALCYONE2Driver.getOutputMEDDoubleField(self, name)`

#### `ALCYONE2Driver.setInputIntValue(self, name, value)`
