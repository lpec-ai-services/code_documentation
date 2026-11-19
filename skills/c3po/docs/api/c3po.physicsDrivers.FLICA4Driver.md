<!-- source: c3po/physicsDrivers/FLICA4Driver.py -->

# `c3po.physicsDrivers.FLICA4Driver`

Contain the class `FLICA4Driver`.

### `class c3po.physicsDrivers.FLICA4Driver.FLICA4Driver()  — bases: PhysicsDriver`

This is the implementation of `PhysicsDriver` for FLICA4.

#### `FLICA4Driver.getMEDCouplingMajorVersion(self)`

#### `FLICA4Driver.isMEDCoupling64Bits(self)`

#### `FLICA4Driver.setDataFile(self, datafile)`

#### `FLICA4Driver.initialize(self)`

#### `FLICA4Driver.terminate(self)`

#### `FLICA4Driver.presentTime(self)`

#### `FLICA4Driver.computeTimeStep(self)`

#### `FLICA4Driver.initTimeStep(self, dt)`

#### `FLICA4Driver.solveTimeStep(self)`

#### `FLICA4Driver.validateTimeStep(self)`

#### `FLICA4Driver.setStationaryMode(self, stationaryMode)`

#### `FLICA4Driver.getStationaryMode(self)`

#### `FLICA4Driver.abortTimeStep(self)`

#### `FLICA4Driver.resetTime(self, time_)`

#### `FLICA4Driver.getInputFieldsNames(self)`

#### `FLICA4Driver.getOutputFieldsNames(self)`

#### `FLICA4Driver.getInputMEDDoubleFieldTemplate(self, name)`

#### `FLICA4Driver.setInputMEDDoubleField(self, name, field)`

#### `FLICA4Driver.getOutputMEDDoubleField(self, name)`

#### `FLICA4Driver.setInputDoubleValue(self, name, value)`

#### `FLICA4Driver.setInputIntValue(self, name, value)`

#### `FLICA4Driver.getOutputDoubleValue(self, name)`

### `class c3po.physicsDrivers.FLICA4Driver.FLICA4AutoSwitchDriver()  — bases: PhysicsDriver`

This `PhysicsDriver` drives two `FLICA4Driver`, for stationnary and transient, and switches from one to the other automatically.

#### `FLICA4AutoSwitchDriver.getMEDCouplingMajorVersion(self)`

#### `FLICA4AutoSwitchDriver.isMEDCoupling64Bits(self)`

#### `FLICA4AutoSwitchDriver.initialize(self)`

#### `FLICA4AutoSwitchDriver.terminate(self)`

#### `FLICA4AutoSwitchDriver.presentTime(self)`

#### `FLICA4AutoSwitchDriver.computeTimeStep(self)`

#### `FLICA4AutoSwitchDriver.initTimeStep(self, dt)`

#### `FLICA4AutoSwitchDriver.solveTimeStep(self)`

#### `FLICA4AutoSwitchDriver.validateTimeStep(self)`

#### `FLICA4AutoSwitchDriver.setStationaryMode(self, stationaryMode)`

#### `FLICA4AutoSwitchDriver.getStationaryMode(self)`

#### `FLICA4AutoSwitchDriver.abortTimeStep(self)`

#### `FLICA4AutoSwitchDriver.resetTime(self, time_)`

#### `FLICA4AutoSwitchDriver.getInputFieldsNames(self)`

#### `FLICA4AutoSwitchDriver.getOutputFieldsNames(self)`

#### `FLICA4AutoSwitchDriver.getInputMEDDoubleFieldTemplate(self, name)`

#### `FLICA4AutoSwitchDriver.setInputMEDDoubleField(self, name, field)`

#### `FLICA4AutoSwitchDriver.getOutputMEDDoubleField(self, name)`

#### `FLICA4AutoSwitchDriver.setInputDoubleValue(self, name, value)`

#### `FLICA4AutoSwitchDriver.setInputIntValue(self, name, value)`

#### `FLICA4AutoSwitchDriver.getOutputDoubleValue(self, name)`
