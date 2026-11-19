<!-- source: c3po/mpi/MPIMasterExchanger.py -->

# `c3po.mpi.MPIMasterExchanger`

Contain the class `MPIMasterExchanger`.

### `class c3po.mpi.MPIMasterExchanger.MPIMasterExchanger(workerProcesses, idExchangerWorker, localExchanger=None)  — bases: Exchanger`

`MPIMasterExchanger` is used by the master to control remote `c3po.Exchanger.Exchanger`.

It can, in addition, be in charge of a local one (that allows the master to participate to the calculation).

The `exchange` method of `MPIMasterExchanger` commands workers to exchange data.

#### `MPIMasterExchanger.exchange(self)`

Trigger the exchange of data.

#### `MPIMasterExchanger.clean(self)`

See `c3po.Exchanger.Exchanger.clean`.
