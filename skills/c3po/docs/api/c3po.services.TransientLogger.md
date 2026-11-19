<!-- source: c3po/services/TransientLogger.py -->

# `c3po.services.TransientLogger`

Contains the class `TransientLogger` and its daughters `Timekeeper` and `FortuneTeller`.

### `class c3po.services.TransientLogger.TransientLogger  — bases: object`

`TransientLogger` is the base class for the production of transient logging strings.

#### `TransientLogger.initTransient(self, driver, tmax, finishAtTmax, stopIfStationary, presentTime)`

Method called before transient starts.

## Parameters

driver : c3po.PhysicsDriver.PhysicsDriver  
The caller of solveTransient().

tmax : float  
`tmax` argument given to solveTransient().

finishAtTmax : bool  
`finishAtTmax` argument given to solveTransient().

stopIfStationary : bool  
`stopIfStationary` argument given to solveTransient().

presentTime : float  
Present time when calling solveTransient().

#### `TransientLogger.logAbort(self, dt, presentTime)`

Method called when time step is aborted.

## Parameters

dt : float  
Size of the failed time step.

presentTime : float  
Present time after calling abortTimeStep().

#### `TransientLogger.logValidate(self, dt, presentTime)`

Method called when time step is validated.

## Parameters

dt : float  
Size of the validated time step.

presentTime : float  
Present time after calling validateTimeStep().

#### `TransientLogger.terminateTransient(self, presentTime, stop, isStationary)`

Method called after the transient ends.

## Parameters

presentTime : float  
Present time after the transient.

stop : bool  
Indicate if the transient ends because of a stopping criteria.

isStationary : bool  
Indicate if the stopping criteria is due to isStationary().

### `class c3po.services.TransientLogger.Timekeeper()  — bases: TransientLogger`

`TransientLogger` which provides information about transient progress.

#### `Timekeeper.initTransient(self, driver, tmax, finishAtTmax, stopIfStationary, presentTime)`

See `TransientLogger.initTransient`

#### `Timekeeper.logAbort(self, dt, presentTime)`

See `TransientLogger.logAbort`

#### `Timekeeper.logValidate(self, dt, presentTime)`

See `TransientLogger.logValidate`

#### `Timekeeper.terminateTransient(self, presentTime, stop, isStationary)`

See `TransientLogger.terminateTransient`

### `class c3po.services.TransientLogger.FortuneTeller(relaxation=0.3)  — bases: Timekeeper`

`Timekeeper` which estimates in addition the duration of the transient with Exponential Moving Average.

#### `FortuneTeller.initTransient(self, driver, tmax, finishAtTmax, stopIfStationary, presentTime)`

See `TransientLogger.initTransient`

#### `FortuneTeller.logValidate(self, dt, presentTime)`

See `TransientLogger.logValidate`

### `class c3po.services.TransientLogger.TransientPrinter(transientLogger)  — bases: object`

INTERNAL.

`TransientPrinter` writes information about transient in the standard output.

#### `TransientPrinter.initTransient(self, driver, tmax, finishAtTmax, stopIfStationary, presentTime)`

See `TransientLogger.initTransient`.

#### `TransientPrinter.logAbort(self, dt, presentTime)`

See `TransientLogger.logAbort`.

#### `TransientPrinter.logValidate(self, dt, presentTime)`

See `TransientLogger.logValidate`.

#### `TransientPrinter.terminateTransient(self, presentTime, stop, isStationary)`

See `TransientLogger.terminateTransient`.

#### `TransientPrinter.getPrinter(self)`

Return the `Printer` object used.

## Returns

c3po.services.Printer.Printer  
the `Printer` object used.

#### `TransientPrinter.setLogger(self, transientLogger)`

Set a new `TransientLogger` object.

## Parameters

transientLogger : c3po.services.TransientLogger.TransientLogger  
The `TransientLogger` object to use.

#### `TransientPrinter.getLogger(self)`

Return the `TransientLogger` object used.

## Returns

c3po.services.TransientLogger.TransientLogger  
The used `TransientLogger` object.
