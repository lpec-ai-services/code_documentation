<!-- source: c3po/TimeAccumulator.py -->

# `c3po.TimeAccumulator`

Contain the class `TimeAccumulator`.

### `class c3po.TimeAccumulator.SaveAtInitTimeStep  — bases: object`

Enum defining `TimeAccumulator` saving mode.

Values:  
- `never`:  
  `TimeAccumulator` never calls the `save()` / `restore()` methods. `abortTimeStep()` is not available if not in StationaryMode.

- `always`:  
  `TimeAccumulator` saves at every `initTimeStep()` call and restores at every `abortTimeStep`, even in StationaryMode.

- `transient`:  
  `TimeAccumulator` saves at every `initTimeStep()` call and restores at every `abortTimeStep()`, if not in StationaryMode.

- `transientExceptAfterAbort`:  
  If not in StationaryMode:  
  - `TimeAccumulator` saves at every `initTimeStep()` call that does not follow an `abortTimeStep()` (the first attempt to compute a time-step).
  - It restores at every `abortTimeStep()`, if not in StationaryMode.

### `class c3po.TimeAccumulator.TimeAccumulator(physics, saveParameters=None, stabilizedTransient=(False, 100.0))  — bases: PhysicsDriverWrapper`

`TimeAccumulator` wraps a `PhysicsDriver` into a macro time step procedure (for transients or stationaries (through stabilized transients)).

In transient calculations, the `TimeAccumulator` object is driven like any `PhysicsDriver`, but it will use macro time steps (chosen with `initTimeStep`) whereas the wraped `PhysicsDriver` may use smaller internal time steps (given by its own `computeTimeStep` method).

In stationary calculations, if the stabilizedTransient mode is activated, when a steady-state is asked to the `TimeAccumulator` object (`initTimeStep(0)` in stationaryMode), a time loop over the wraped `PhysicsDriver` object is run until steady-state is reached (`isStationary()` return True). If the stabilizedTransient mode is not activated, steady-state calculations (`initTimeStep(0)` in stationaryMode) are directly asked to the wraped `PhysicsDriver`.

#### `TimeAccumulator.setSavingMode(self, savingMode)`

Set a saving mode.

## Parameters

savingMode  
See `SaveAtInitTimeStep` documentation for available options. Default value is `SaveAtInitTimeStep.transient`.

#### `TimeAccumulator.setStabilizedTransient(self, stabilizedTransient)`

Set stabilized transient data.

## Parameters

stabilizedTransient  
See parameter `stabilizedTransient` of the `__init__` method.

#### `TimeAccumulator.setComputedTimeStep(self, dt)`

Set time-step size returned by `computeTimeStep`.

## Parameters

dt : float  
Time-step size returned by `computeTimeStep`. None can be set to use the time step recommended by the hold `PhysicsDriver`. Default: None.

#### `TimeAccumulator.initialize(self)`

See `PhysicsDriver.initialize`.

#### `TimeAccumulator.terminate(self)`

See `PhysicsDriver.terminate`.

#### `TimeAccumulator.presentTime(self)`

See `PhysicsDriver.presentTime`.

#### `TimeAccumulator.computeTimeStep(self)`

See `PhysicsDriver.computeTimeStep`.

Return the asked macro time step if set (by `setValue("macrodt", dt)`), the preferred time step of the `PhysicsDriver` otherwise.

#### `TimeAccumulator.initTimeStep(self, dt)`

See `PhysicsDriver.initTimeStep`.

#### `TimeAccumulator.solveTimeStep(self)`

Make the `PhysicsDriver` to reach the end of the macro time step asked to `TimeAccumulator` using its own time advance procedure.

#### `TimeAccumulator.validateTimeStep(self)`

See `PhysicsDriver.validateTimeStep`.

#### `TimeAccumulator.abortTimeStep(self)`

See `PhysicsDriver.abortTimeStep`.

#### `TimeAccumulator.getInputValuesNames(self)`

See `c3po.DataAccessor.DataAccessor.getInputValuesNames`.

#### `TimeAccumulator.getValueType(self, name)`

See `c3po.DataAccessor.DataAccessor.getValueType`.

#### `TimeAccumulator.getValueUnit(self, name)`

See `c3po.DataAccessor.DataAccessor.getValueUnit`.

#### `TimeAccumulator.setInputDoubleValue(self, name, value)`

See `c3po.DataAccessor.DataAccessor.setInputDoubleValue`.

The value associated with the name "macrodt" can be used to set the time-step size returned by `computeTimeStep`.
