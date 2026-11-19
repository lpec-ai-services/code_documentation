<!-- source: c3po/mpi/MPIWorker.py -->

# `c3po.mpi.MPIWorker`

Contain the class `MPIWorker`.

### `class c3po.mpi.MPIWorker.MPIWorker(physicsDrivers, exchangers, dataManagers, masterProcess, isCollective=False)  — bases: object`

`MPIWorker` defines the behavior of workers in a master/workers MPI paradimg.

#### `MPIWorker.answer(self, data, collectiveOperator=MPI.MIN)`

INTERNAL

#### `MPIWorker.getIdNewData(self)`

INTERNAL

#### `MPIWorker.checkDataID(self, idList)`

INTERNAL

#### `MPIWorker.listen(self)`

Make the worker waits for instructions from the master.

The worker gets out of this waiting mode when the master call the terminate method of the related `c3po.mpi.MPIMasterPhysicsDriver.MPIMasterPhysicsDriver`.
