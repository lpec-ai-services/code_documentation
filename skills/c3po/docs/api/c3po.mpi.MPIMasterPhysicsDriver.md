<!-- source: c3po/mpi/MPIMasterPhysicsDriver.py -->

# `c3po.mpi.MPIMasterPhysicsDriver`

Contain the class `MPIMasterPhysicsDriver`.

### `class c3po.mpi.MPIMasterPhysicsDriver.MPIMasterPhysicsDriver(workerProcess, localPhysicsDriver=None)  — bases: PhysicsDriver`

`MPIMasterPhysicsDriver` is used by a master process to control a (set of) remote `c3po.PhysicsDriver.PhysicsDriver` as a local one.

It can, in addition, be in charge of a local one (can be usefull for codes using an internal collaborative MPI parallelization).

Inherits from `c3po.PhysicsDriver.PhysicsDriver`. All the methods of `c3po.PhysicsDriver.PhysicsDriver` are implemented and consist in commanding the worker to execute them. Methods inherited from `c3po.DataAccessor.DataAccessor` are NOT implemented (apart from the `setInput(Double/Int/String)Value` methods, for convenience). Use an `c3po.mpi.MPIMasterExchanger.MPIMasterExchanger` to exchange data with the worker.

#### `MPIMasterPhysicsDriver.sendData(self, tag, data=None)`

INTERNAL

#### `MPIMasterPhysicsDriver.recvData(self, data, collectiveOperator=MPI.MIN)`

INTERNAL

#### `MPIMasterPhysicsDriver.setDataManagerToFree(self, idDataManager)`

INTERNAL

#### `MPIMasterPhysicsDriver.setDataFile(self, datafile)`

See `PhysicsDriver.setDataFile`.

#### `MPIMasterPhysicsDriver.getMPIComm(self)`

See `PhysicsDriver.getMPIComm`.

#### `MPIMasterPhysicsDriver.init(self)`

See `PhysicsDriver.init`.

#### `MPIMasterPhysicsDriver.getInitStatus(self)`

See `PhysicsDriver.getInitStatus`.

#### `MPIMasterPhysicsDriver.initialize(self)`

See `PhysicsDriver.initialize`.

#### `MPIMasterPhysicsDriver.terminate(self)`

See `PhysicsDriver.terminate`.

#### `MPIMasterPhysicsDriver.presentTime(self)`

See `PhysicsDriver.presentTime`.

#### `MPIMasterPhysicsDriver.computeTimeStep(self)`

See `PhysicsDriver.computeTimeStep`.

#### `MPIMasterPhysicsDriver.initTimeStep(self, dt)`

See `PhysicsDriver.initTimeStep`.

#### `MPIMasterPhysicsDriver.solve(self)`

See `PhysicsDriver.solve`.

#### `MPIMasterPhysicsDriver.getSolveStatus(self)`

See `PhysicsDriver.getSolveStatus`.

#### `MPIMasterPhysicsDriver.solveTimeStep(self)`

See `PhysicsDriver.solveTimeStep`.

#### `MPIMasterPhysicsDriver.validateTimeStep(self)`

See `PhysicsDriver.validateTimeStep`.

#### `MPIMasterPhysicsDriver.setStationaryMode(self, stationaryMode)`

See `PhysicsDriver.setStationaryMode`.

#### `MPIMasterPhysicsDriver.getStationaryMode(self)`

See `PhysicsDriver.getStationaryMode`.

#### `MPIMasterPhysicsDriver.abortTimeStep(self)`

See `PhysicsDriver.abortTimeStep`.

#### `MPIMasterPhysicsDriver.isStationary(self)`

See `PhysicsDriver.isStationary`.

#### `MPIMasterPhysicsDriver.resetTime(self, time_)`

See `PhysicsDriver.resetTime`.

#### `MPIMasterPhysicsDriver.iterate(self)`

See `PhysicsDriver.iterate`.

#### `MPIMasterPhysicsDriver.getIterateStatus(self)`

See `PhysicsDriver.getIterateStatus`.

#### `MPIMasterPhysicsDriver.iterateTimeStep(self)`

See `PhysicsDriver.iterateTimeStep`.

#### `MPIMasterPhysicsDriver.save(self, label, method)`

See `PhysicsDriver.save`.

#### `MPIMasterPhysicsDriver.restore(self, label, method)`

See `PhysicsDriver.restore`.

#### `MPIMasterPhysicsDriver.forget(self, label, method)`

See `PhysicsDriver.forget`.

#### `MPIMasterPhysicsDriver.setInputDoubleValue(self, name, value)`

See `c3po.DataAccessor.DataAccessor.setInputDoubleValue`.

#### `MPIMasterPhysicsDriver.setInputIntValue(self, name, value)`

See `c3po.DataAccessor.DataAccessor.setInputIntValue`.

#### `MPIMasterPhysicsDriver.setInputStringValue(self, name, value)`

See `c3po.DataAccessor.DataAccessor.setInputStringValue`.

#### `MPIMasterPhysicsDriver.getInputValuesNames(self)`

See `c3po.DataAccessor.DataAccessor.getInputValuesNames`.

#### `MPIMasterPhysicsDriver.getOutputValuesNames(self)`

See `c3po.DataAccessor.DataAccessor.getOutputValuesNames`.

#### `MPIMasterPhysicsDriver.getValueType(self, name)`

See `c3po.DataAccessor.DataAccessor.getValueType`.

#### `MPIMasterPhysicsDriver.getValueUnit(self, name)`

See `c3po.DataAccessor.DataAccessor.getValueUnit`.

#### `MPIMasterPhysicsDriver.getOutputDoubleValue(self, name)`

See `c3po.DataAccessor.DataAccessor.getOutputDoubleValue`.

#### `MPIMasterPhysicsDriver.getOutputIntValue(self, name)`

See `c3po.DataAccessor.DataAccessor.getOutputIntValue`.

#### `MPIMasterPhysicsDriver.getOutputStringValue(self, name)`

See `c3po.DataAccessor.DataAccessor.getOutputStringValue`.
