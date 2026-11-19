<!-- source: c3po/physicsDrivers/CRONOS2Driver.py -->

# `c3po.physicsDrivers.CRONOS2Driver`

Contain the class `CRONOS2Driver`.

### `class c3po.physicsDrivers.CRONOS2Driver.ParamKey`

Keys for the dictionary of the names of CRONOS2 parameters in PARAM-type structures

### `class c3po.physicsDrivers.CRONOS2Driver.CRONOS2Driver()  — bases: PhysicsDriver`

This is the implementation of `PhysicsDriver` for CRONOS2.

#### `CRONOS2Driver.setParamDict(self, paramDict)`

Set a new dictionary of names of CRONOS2 parameters in PARAM structures.

This function is reserved for advanced use only ; do not use it unless you know exactly what you are doing.

#### `CRONOS2Driver.getMEDCouplingMajorVersion(self)`

#### `CRONOS2Driver.isMEDCoupling64Bits(self)`

#### `CRONOS2Driver.setDataFile(self, datafile)`

See `PhysicsDriver.setDataFile`.

#### `CRONOS2Driver.initialize(self)`

See `PhysicsDriver.initialize`.

#### `CRONOS2Driver.terminate(self)`

See `PhysicsDriver.terminate`.

#### `CRONOS2Driver.initTimeStep(self, dt)`

See `PhysicsDriver.initTimeStep`.

#### `CRONOS2Driver.presentTime(self)`

See `PhysicsDriver.presentTime`.

#### `CRONOS2Driver.computeTimeStep(self)`

See `PhysicsDriver.computeTimeStep`.

Description of the expected outputs for the `ICOCO_COMPUTE_TIME_STEP` gibiane subroutine:

- The time step (floating-point number) must be output in the variable `T_C3PO.'DT'`
- The stop flag (boolean) must be output in the variable `T_C3PO.'STOP'`

#### `CRONOS2Driver.solveTimeStep(self)`

See `PhysicsDriver.solveTimeStep`.

#### `CRONOS2Driver.validateTimeStep(self)`

See `PhysicsDriver.validateTimeStep`.

#### `CRONOS2Driver.setStationaryMode(self, stationaryMode)`

#### `CRONOS2Driver.getStationaryMode(self)`

#### `CRONOS2Driver.abortTimeStep(self)`

See `PhysicsDriver.abortTimeStep`.

#### `CRONOS2Driver.resetTime(self, time_)`

#### `CRONOS2Driver.getOutputMEDDoubleField(self, name)`

See `PhysicsDriver.getOutputMEDDoubleField()`.

The gibiane subroutine `ICOCO_GET_OUTPUT_MEDFIELD` :

- takes as input the name of the MED field in the string `T_C3PO.'name'` ;
- returns the required MED field in the variable `T_C3PO.'field_out'` of type MEDFIELD.

#### `CRONOS2Driver.getInputMEDDoubleFieldTemplate(self, name)`

See `PhysicsDriver.getInputMEDDoubleFieldTemplate()`.

The gibiane subroutine `ICOCO_GET_INPUT_MEDFIELD_TEMPLATE` :

- takes as input the name of the MED field template in the string `T_C3PO.'name'` ;
- returns the required MED field template in the variable `T_C3PO.'field_out'` of type MEDFIELD.

#### `CRONOS2Driver.setInputMEDDoubleField(self, name, field)`

See `PhysicsDriver.setInputMEDDoubleField()`.

The gibiane subroutine `ICOCO_SET_INPUT_MEDFIELD` :

- takes as input the name of the MED field in the string `T_C3PO.'name'` ;
- takes as input the name of the gibiane variable holding the MED field in the string `T_C3PO.'FSaph'` ;
- sorts away the MED field in the appropriate PARAM structures of CRONOS2.

#### `CRONOS2Driver.setInputDoubleValue(self, name, value)`

See `PhysicsDriver.setInputDoubleValue()`.

The gibiane subroutine `ICOCO_SET_VALUE` :

- takes as input the name of the value in the string `T_C3PO.'name'` ;
- takes as input the value stored in the table `T_C3PO.'value'` with the index name ;
- sorts away the value in the appropriate data structures of CRONOS2.

#### `CRONOS2Driver.getOutputDoubleValue(self, name)`

See `PhysicsDriver.getOutputDoubleValue()`.

The gibiane subroutine `ICOCO_GET_VALUE` :

- takes as input the name of the value in the string `T_C3PO.'name'` ;
- returns the required floating number value in the table `T_C3PO.'value'` at the index name.
