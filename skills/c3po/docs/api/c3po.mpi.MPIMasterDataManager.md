<!-- source: c3po/mpi/MPIMasterDataManager.py -->

# `c3po.mpi.MPIMasterDataManager`

Contain the class `MPIMasterDataManager`.

### `class c3po.mpi.MPIMasterDataManager.MPIMasterDataManager(mpiMasterphysicsD, idDataWorker, localDataManager=None)  — bases: DataManager`

`MPIMasterDataManager` is used by the master process to control a (set of) remote `c3po.DataManager.DataManager` as a local one.

It can, in addition, be in charge of a local one (can be usefull to contribute to a collaborative computation).

`MPIMasterDataManager` implements the methods of `c3po.DataManager.DataManager` by instructing the worker to execute them.

#### `MPIMasterDataManager.getMPIComm(self)`

See `PhysicsDriver.getMPIComm`.

#### `MPIMasterDataManager.checkCompatibility(self, other)`

INTERNAL

#### `MPIMasterDataManager.clone(self)`

See `c3po.DataManager.DataManager.clone`.

#### `MPIMasterDataManager.cloneEmpty(self)`

See `c3po.DataManager.DataManager.cloneEmpty`.

#### `MPIMasterDataManager.copy(self, other)`

See `c3po.DataManager.DataManager.copy`.

#### `MPIMasterDataManager.normMax(self)`

See `c3po.DataManager.DataManager.normMax`.

#### `MPIMasterDataManager.norm2(self)`

See `c3po.DataManager.DataManager.norm2`.

#### `MPIMasterDataManager.imuladd(self, scalar, other)`

See `c3po.DataManager.DataManager.imuladd`.

#### `MPIMasterDataManager.dot(self, other)`

See `c3po.DataManager.DataManager.dot`.
