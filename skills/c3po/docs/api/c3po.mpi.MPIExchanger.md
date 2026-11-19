<!-- source: c3po/mpi/MPIExchanger.py -->

# `c3po.mpi.MPIExchanger`

Contain the classes `MPIExchanger` and `MPIShortcutToData`. `MPIShortcutToData` is for internal use only.

### `class c3po.mpi.MPIExchanger.MPIShortcutToData(containerToSet)  — bases: object`

INTERNAL

#### `MPIShortcutToData.store(self, something)`

INTERNAL

#### `MPIShortcutToData.get(self)`

INTERNAL

#### `MPIShortcutToData.getFieldTemplate(self)`

INTERNAL

#### `MPIShortcutToData.set(self, something)`

INTERNAL

#### `MPIShortcutToData.clean(self)`

INTERNAL

### `class c3po.mpi.MPIExchanger.MPIExchanger(method, fieldsToGet, fieldsToSet, valuesToGet=[], valuesToSet=[], exchangeWithFiles=False, mpiComm=None)  — bases: LocalExchanger`

`MPIExchanger` is the MPI version of `c3po.LocalExchanger.LocalExchanger`.

`MPIExchanger` can replace, without impact, a `c3po.LocalExchanger.LocalExchanger` for a calculation on a single process, if the MPI environment is available.

#### `MPIExchanger.exchange(self)`

Trigger the exchange of data.

Must be called at the same time by all processes.

#### `MPIExchanger.clean(self)`

See `c3po.Exchanger.clean`.
