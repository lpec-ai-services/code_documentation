<!-- source: c3po/mpi/MPICoupler.py -->

# `c3po.mpi.MPICoupler`

Contain the class `MPICoupler`.

### `class c3po.mpi.MPICoupler.MPICoupler(physics, exchangers, dataManagers=[], mpiComm=None)  — bases: Coupler`

`MPICoupler` is the MPI collaborative version of `c3po.Coupler.Coupler`.

The MPI functionalities are used for some collective operations.

Can replace, without impact, a `c3po.Coupler.Coupler` for a calculation on a single process, if the MPI environment is available.

#### `MPICoupler.getMEDCouplingMajorVersion(self)`

See `Coupler.getMEDCouplingMajorVersion`.

#### `MPICoupler.isMEDCoupling64Bits(self)`

See `Coupler.isMEDCoupling64Bits`.

#### `MPICoupler.setMPIComm(self, mpicomm)`

#### `MPICoupler.getMPIComm(self)`

#### `MPICoupler.initialize(self)`

See `Coupler.initialize`.

#### `MPICoupler.computeTimeStep(self)`

See `Coupler.computeTimeStep`.

#### `MPICoupler.initTimeStep(self, dt)`

See `Coupler.initTimeStep`.

#### `MPICoupler.getSolveStatus(self)`

See `Coupler.getSolveStatus`.

#### `MPICoupler.getStationaryMode(self)`

See `Coupler.getStationaryMode`.

#### `MPICoupler.isStationary(self)`

See `Coupler.isStationary`.

#### `MPICoupler.getIterateStatus(self)`

See `Coupler.getIterateStatus`.
