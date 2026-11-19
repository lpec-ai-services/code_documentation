<!-- source: c3po/services/PhysicsDriverWrapper.py -->

# `c3po.services.PhysicsDriverWrapper`

Contain the wrapper class `PhysicsDriverWrapper`.

### `class c3po.services.PhysicsDriverWrapper.PhysicsDriverWrapper(physics)  — bases: PhysicsDriver`

`PhysicsDriverWrapper` wraps a `PhysicsDriver` object without modifying its behavior.

This class is a skeleton, intended to be overloaded, for modifying the behavior of a `PhysicsDriver` by composition.

#### `PhysicsDriverWrapper.getPhysicsDriver(self)`

Return the wrapped `PhysicsDriver`.

## Returns

PhysicsDriver  
the wrapped PhysicsDriver.

#### `PhysicsDriverWrapper.getMEDCouplingMajorVersion(self)`

See `PhysicsDriver.getMEDCouplingMajorVersion`.

#### `PhysicsDriverWrapper.isMEDCoupling64Bits(self)`

See `PhysicsDriver.isMEDCoupling64Bits`.

#### `PhysicsDriverWrapper.setDataFile(self, datafile)`

See `PhysicsDriver.setDataFile`.

#### `PhysicsDriverWrapper.setMPIComm(self, mpicomm)`

See `PhysicsDriver.setMPIComm`.

#### `PhysicsDriverWrapper.getMPIComm(self)`

See `c3po.DataAccessor.DataAccessor.getMPIComm`.

#### `PhysicsDriverWrapper.initialize(self)`

See `PhysicsDriver.initialize`.

#### `PhysicsDriverWrapper.terminate(self)`

See `PhysicsDriver.terminate`.

#### `PhysicsDriverWrapper.presentTime(self)`

See `PhysicsDriver.presentTime`.

#### `PhysicsDriverWrapper.computeTimeStep(self)`

See `PhysicsDriver.computeTimeStep`.

#### `PhysicsDriverWrapper.initTimeStep(self, dt)`

See `PhysicsDriver.initTimeStep`.

#### `PhysicsDriverWrapper.solveTimeStep(self)`

See `PhysicsDriver.solveTimeStep`.

#### `PhysicsDriverWrapper.iterateTimeStep(self)`

See `PhysicsDriver.iterateTimeStep`.

#### `PhysicsDriverWrapper.validateTimeStep(self)`

See `PhysicsDriver.validateTimeStep`.

#### `PhysicsDriverWrapper.setStationaryMode(self, stationaryMode)`

See `PhysicsDriver.setStationaryMode`.

#### `PhysicsDriverWrapper.getStationaryMode(self)`

See `PhysicsDriver.getStationaryMode`.

#### `PhysicsDriverWrapper.abortTimeStep(self)`

See `PhysicsDriver.abortTimeStep`.

#### `PhysicsDriverWrapper.isStationary(self)`

See `PhysicsDriver.isStationary`.

#### `PhysicsDriverWrapper.resetTime(self, time_)`

See `PhysicsDriver.resetTime`.

#### `PhysicsDriverWrapper.save(self, label, method)`

See `PhysicsDriver.save`.

#### `PhysicsDriverWrapper.restore(self, label, method)`

See `PhysicsDriver.restore`.

#### `PhysicsDriverWrapper.forget(self, label, method)`

See `PhysicsDriver.forget`.

#### `PhysicsDriverWrapper.getInputFieldsNames(self)`

See `c3po.DataAccessor.DataAccessor.getInputFieldsNames`.

#### `PhysicsDriverWrapper.getOutputFieldsNames(self)`

See `c3po.DataAccessor.DataAccessor.getOutputFieldsNames`.

#### `PhysicsDriverWrapper.getFieldType(self, name)`

See `c3po.DataAccessor.DataAccessor.getFieldType`.

#### `PhysicsDriverWrapper.getMeshUnit(self)`

See `c3po.DataAccessor.DataAccessor.getMeshUnit`.

#### `PhysicsDriverWrapper.getFieldUnit(self, name)`

See `c3po.DataAccessor.DataAccessor.getFieldUnit`.

#### `PhysicsDriverWrapper.getInputMEDDoubleFieldTemplate(self, name)`

See `c3po.DataAccessor.DataAccessor.getInputMEDDoubleFieldTemplate`.

#### `PhysicsDriverWrapper.setInputMEDDoubleField(self, name, field)`

See `c3po.DataAccessor.DataAccessor.setInputMEDDoubleField`.

#### `PhysicsDriverWrapper.getOutputMEDDoubleField(self, name)`

See `c3po.DataAccessor.DataAccessor.getOutputMEDDoubleField`.

#### `PhysicsDriverWrapper.updateOutputMEDDoubleField(self, name, field)`

See `c3po.DataAccessor.DataAccessor.updateOutputMEDDoubleField`.

#### `PhysicsDriverWrapper.getInputMEDIntFieldTemplate(self, name)`

See `c3po.DataAccessor.DataAccessor.getInputMEDIntFieldTemplate`.

#### `PhysicsDriverWrapper.setInputMEDIntField(self, name, field)`

See `c3po.DataAccessor.DataAccessor.setInputMEDIntField`.

#### `PhysicsDriverWrapper.getOutputMEDIntField(self, name)`

See `c3po.DataAccessor.DataAccessor.getOutputMEDIntField`.

#### `PhysicsDriverWrapper.updateOutputMEDIntField(self, name, field)`

See `c3po.DataAccessor.DataAccessor.updateOutputMEDIntField`.

#### `PhysicsDriverWrapper.getInputMEDStringFieldTemplate(self, name)`

See `c3po.DataAccessor.DataAccessor.getInputMEDStringFieldTemplate`.

#### `PhysicsDriverWrapper.setInputMEDStringField(self, name, field)`

See `c3po.DataAccessor.DataAccessor.setInputMEDStringField`.

#### `PhysicsDriverWrapper.getOutputMEDStringField(self, name)`

See `c3po.DataAccessor.DataAccessor.getOutputMEDStringField`.

#### `PhysicsDriverWrapper.updateOutputMEDStringField(self, name, field)`

See `c3po.DataAccessor.DataAccessor.updateOutputMEDStringField`.

#### `PhysicsDriverWrapper.getInputValuesNames(self)`

See `c3po.DataAccessor.DataAccessor.getInputValuesNames`.

#### `PhysicsDriverWrapper.getOutputValuesNames(self)`

See `c3po.DataAccessor.DataAccessor.getOutputValuesNames`.

#### `PhysicsDriverWrapper.getValueType(self, name)`

See `c3po.DataAccessor.DataAccessor.getValueType`.

#### `PhysicsDriverWrapper.getValueUnit(self, name)`

See `c3po.DataAccessor.DataAccessor.getValueUnit`.

#### `PhysicsDriverWrapper.setInputDoubleValue(self, name, value)`

See `c3po.DataAccessor.DataAccessor.setInputDoubleValue`.

#### `PhysicsDriverWrapper.getOutputDoubleValue(self, name)`

See `c3po.DataAccessor.DataAccessor.getOutputDoubleValue`.

#### `PhysicsDriverWrapper.setInputIntValue(self, name, value)`

See `c3po.DataAccessor.DataAccessor.setInputIntValue`.

#### `PhysicsDriverWrapper.getOutputIntValue(self, name)`

See `c3po.DataAccessor.DataAccessor.getOutputIntValue`.

#### `PhysicsDriverWrapper.setInputStringValue(self, name, value)`

See `c3po.DataAccessor.DataAccessor.setInputStringValue`.

#### `PhysicsDriverWrapper.getOutputStringValue(self, name)`

See `c3po.DataAccessor.DataAccessor.getOutputStringValue`.
