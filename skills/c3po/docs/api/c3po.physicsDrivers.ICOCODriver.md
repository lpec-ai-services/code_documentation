<!-- source: c3po/physicsDrivers/ICOCODriver.py -->

# `c3po.physicsDrivers.ICOCODriver`

Contain the class `ICOCODriver`.

### `class c3po.physicsDrivers.ICOCODriver.ICOCODriver(problem)  — bases: PhysicsDriver`

This is the implementation of `PhysicsDriver` for any ICoCo Problem implementation.

#### `ICOCODriver.getMEDCouplingMajorVersion(self)`

#### `ICOCODriver.isMEDCoupling64Bits(self)`

#### `ICOCODriver.setDataFile(self, datafile)`

#### `ICOCODriver.setMPIComm(self, mpicomm)`

#### `ICOCODriver.getMPIComm(self)`

#### `ICOCODriver.initialize(self)`

#### `ICOCODriver.terminate(self)`

#### `ICOCODriver.presentTime(self)`

#### `ICOCODriver.computeTimeStep(self)`

#### `ICOCODriver.initTimeStep(self, dt)`

#### `ICOCODriver.solveTimeStep(self)`

#### `ICOCODriver.validateTimeStep(self)`

#### `ICOCODriver.setStationaryMode(self, stationaryMode)`

#### `ICOCODriver.getStationaryMode(self)`

#### `ICOCODriver.isStationary(self)`

#### `ICOCODriver.abortTimeStep(self)`

#### `ICOCODriver.resetTime(self, time_)`

#### `ICOCODriver.iterateTimeStep(self)`

#### `ICOCODriver.save(self, label, method)`

#### `ICOCODriver.restore(self, label, method)`

#### `ICOCODriver.forget(self, label, method)`

#### `ICOCODriver.getInputFieldsNames(self)`

#### `ICOCODriver.getOutputFieldsNames(self)`

#### `ICOCODriver.getFieldType(self, name)`

#### `ICOCODriver.getMeshUnit(self)`

#### `ICOCODriver.getFieldUnit(self, name)`

#### `ICOCODriver.getInputMEDDoubleFieldTemplate(self, name)`

#### `ICOCODriver.setInputMEDDoubleField(self, name, field)`

#### `ICOCODriver.getOutputMEDDoubleField(self, name)`

#### `ICOCODriver.updateOutputMEDDoubleField(self, name, field)`

#### `ICOCODriver.getInputValuesNames(self)`

#### `ICOCODriver.getOutputValuesNames(self)`

#### `ICOCODriver.getValueType(self, name)`

#### `ICOCODriver.getValueUnit(self, name)`

#### `ICOCODriver.setInputDoubleValue(self, name, value)`

#### `ICOCODriver.getOutputDoubleValue(self, name)`

#### `ICOCODriver.setInputIntValue(self, name, value)`

#### `ICOCODriver.getOutputIntValue(self, name)`

#### `ICOCODriver.setInputStringValue(self, name, value)`

#### `ICOCODriver.getOutputStringValue(self, name)`
