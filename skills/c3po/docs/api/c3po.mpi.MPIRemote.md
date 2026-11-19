<!-- source: c3po/mpi/MPIRemote.py -->

# `c3po.mpi.MPIRemote`

Contain the class `MPIRemote`.

### `class c3po.mpi.MPIRemote.MPIRemote(mpiComm)  — bases: PhysicsDriver, DataManager`

`MPIRemote` replaces a remote `PhysicsDriver` or a remote `DataManager`.

Inherits from `c3po.PhysicsDriver.PhysicsDriver` and `c3po.DataManager.DataManager` but passes most of the methods: it does nothing.

#### `MPIRemote.setMPIComm(self, mpicomm)`

Pass

#### `MPIRemote.setDataFile(self, datafile)`

Pass

#### `MPIRemote.initialize(self)`

`return True`

#### `MPIRemote.terminate(self)`

Pass

#### `MPIRemote.presentTime(self)`

Return the time.

#### `MPIRemote.computeTimeStep(self)`

`return (1.e30, True)`

#### `MPIRemote.initTimeStep(self, dt)`

`self._dt = dt` and `return True`

#### `MPIRemote.solveTimeStep(self)`

`return True`

#### `MPIRemote.validateTimeStep(self)`

`self._time += self._dt`

#### `MPIRemote.setStationaryMode(self, stationaryMode)`

`self._stationaryMode = stationaryMode`

#### `MPIRemote.getStationaryMode(self)`

`return self._stationaryMode`

#### `MPIRemote.abortTimeStep(self)`

`self._dt = 0.`

#### `MPIRemote.isStationary(self)`

`return True`

#### `MPIRemote.resetTime(self, time_)`

Reset time.

#### `MPIRemote.iterateTimeStep(self)`

`return (True, True)`

#### `MPIRemote.save(self, label, method)`

#### `MPIRemote.restore(self, label, method)`

#### `MPIRemote.forget(self, label, method)`

#### `MPIRemote.setInputMEDDoubleField(self, name, field)`

Pass

#### `MPIRemote.setInputMEDIntField(self, name, field)`

Pass

#### `MPIRemote.setInputMEDStringField(self, name, field)`

Pass

#### `MPIRemote.setInputDoubleValue(self, name, value)`

Pass

#### `MPIRemote.setInputIntValue(self, name, value)`

Pass

#### `MPIRemote.setInputStringValue(self, name, value)`

Pass

#### `MPIRemote.cloneEmpty(self)`

Return a clone.
