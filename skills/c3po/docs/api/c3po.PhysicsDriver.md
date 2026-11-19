<!-- source: c3po/PhysicsDriver.py -->

# `c3po.PhysicsDriver`

Contain the class `PhysicsDriver`.

### `class c3po.PhysicsDriver.PhysicsDriver()  — bases: DataAccessor`

`PhysicsDriver` is an abstract class which standardizes the functionalities expected by computer codes.

It follows the ICoCo (Interface for Code Coupling) V2 standard. The ICoCo V2 I/O (in/out) methods are defined in the mother class `DataAccessor`.

ICoCo V2 is originally defined for C++ here: <https://github.com/cea-trust-platform/icoco-coupling>. `PhysicsDriver` (together with `DataAccessor`) can be seen as the translation in Python of ICoCo V2.

In order to use a code with C3PO it is necessary to define a class that inherits from `PhysicsDriver` and to overload needed methods (including the ones of `DataAccessor`). Note that not all the methods need to be implemented! Mandatory methods are marked as such.

Some of the methods may not be called when some conditions are not met (i.e. when not in the correct context). Thus in this documentation we define the "`TIME_STEP_DEFINED` context" as the context that the code finds itself, when the method `initTimeStep` has been called, and the method `validateTimeStep` (or `abortTimeStep`) has not yet been called. This is the status in which the current computation time step is well defined.

Within the computation of a time step (so within `TIME_STEP_DEFINED`), the temporal semantic of the fields (and scalar values) is not imposed by the norm. Said differently, it does not require the fields to be defined at the start/middle/end of the current time step, this semantic must be agreed on between the codes being coupled. Fields and scalar values that are set within the `TIME_STEP_DEFINED` context are invalidated (undefined behavior) after a call to `validateTimeStep` (or `abortTimeStep`). They need to be set at each time step. However, fields and scalar values that are set outside of this context (before the first time step for example, or after the resolution of the last time step) are permanent (unless modified afterward within the `TIME_STEP_DEFINED` context).

#### `PhysicsDriver.GetICoCoMajorVersion()`

(Mandatory) Return ICoCo interface major version number.

## Returns

int  
ICoCo interface major version number (2 at present)

#### `PhysicsDriver.getMEDCouplingMajorVersion(self)`

(Optional) Get MEDCoupling major version, if the code was built with MEDCoupling support.

Mandatory if the code is built with MEDCoupling support. This can be used to assess compatibility between codes when coupling them.

## Returns

int  
The MEDCoupling major version number (typically 7, 8, 9, ...).

#### `PhysicsDriver.isMEDCoupling64Bits(self)`

(Optional) Indicate whether the code was built with a 64-bits version of MEDCoupling.

Mandatory if the code is built with MEDCoupling support. This can be used to assess compatibility between codes when coupling them.

## Returns

bool  
True if the code was built with a 64-bits version of MEDCoupling.

#### `PhysicsDriver.setDataFile(self, datafile)`

(Optional) Provide the relative path of a data file to be used by the code.

This method must be called before `initialize`.

## Parameters

datafile : str  
Relative path to the data file.

## Raises

AssertionError  
If called multiple times or after `initialize`.

ValueError  
If an invalid path is provided.

#### `PhysicsDriver.setMPIComm(self, mpicomm)`

(Optional) Provide the MPI communicator to be used by the code for parallel computations.

This method must be called before `initialize`. The communicator should include all the processes to be used by the code. For a sequential code, the call to `setMPIComm` is optional or `mpicomm` should be None.

## Parameters

mpicomm : mpi4py.MPI.Comm  
mpi4py communicator.

## Raises

AssertionError  
If called multiple times or after `initialize`.

#### `PhysicsDriver.init(self)`

This is a recommanded wrapper for `initialize`.

It works with `term` in order to guarantee that `initialize` and `terminate` are called only once:  
- `initialize` is called at the first call of .
- `terminate` is called when the number of calls to `term` is equal to the number of calls to .

also stores the return value of `initialize` instead of returning it. The output is accessible with .

<div class="warning">

<div class="title">

Warning

</div>

This method, in association with , should always be used inside C3PO instead of `initialize` which is not adapted to MPI Master-Workers paradigm.

</div>

<div class="warning">

<div class="title">

Warning

</div>

This method should never be redefined: define `initialize` instead!

</div>

#### `PhysicsDriver.getInitStatus(self)`

Return the output status of the last call to `initialize` made through .

<div class="warning">

<div class="title">

Warning

</div>

This method, in association with , should always be used inside C3PO instead of `initialize` which is not adapted to MPI Master-Workers paradigm.

This method should never be redefined: define `initialize` instead!

</div>

## Returns

bool  
True if all OK, otherwise False.

#### `PhysicsDriver.initialize(self)`

(Mandatory) Initialize the current problem instance.

In this method the code should allocate all its internal structures and be ready to execute. File reads, memory allocations, and other operations likely to fail should be performed here, and not in the constructor (and not in the or in the methods either). This method must be called only once (after a potential call to and/or ) and cannot be called again before `terminate` has been performed.

<div class="warning">

<div class="title">

Warning

</div>

This method is not adapted to MPI Master-Workers paradigm. and methods should be used in C3PO instead.

</div>

## Returns

bool  
True if all OK, otherwise False.

## Raises

AssertionError  
If called multiple times.

#### `PhysicsDriver.term(self)`

This is a recommanded wrapper for `terminate`.

It works with in order to guarantee that `initialize` and `terminate` are called only once:  
- `initialize` is called at the first call of .

- `terminate` is called when the number of calls to `term`  
  is equal to the number of calls to .

<div class="warning">

<div class="title">

Warning

</div>

This method should be used inside C3PO instead of `terminate`.

This method should never be redefined: define `terminate` instead!

</div>

#### `PhysicsDriver.terminate(self)`

(Mandatory) Terminate the current problem instance and release all allocated resources.

Terminate the computation, free the memory and save whatever needs to be saved. This method is called once at the end of the computation or after a non-recoverable error. No other ICoCo method except , and `initialize` may be called after this.

## Raises

AssertionError  
If called before `initialize` or after `terminate`.

AssertionError  
If called inside the `TIME_STEP_DEFINED` context (see `PhysicsDriver` documentation).

#### `PhysicsDriver.getInitNb(self)`

Return the number of times has been called but not `term`.

This method is made to work with the wrappers and `term`. It indicates the number of `term` that are still needed to trigger `terminate`.

## Returns

int  
The number of times has been called but not `term`.

#### `PhysicsDriver.presentTime(self)`

(Mandatory) Return the current time of the simulation.

Can be called any time between `initialize` and `terminate`. The current time can only change during a call to `validateTimeStep` or to `resetTime`.

## Returns

float  
The current (physical) time of the simulation.

## Raises

AssertionError  
If called before `initialize` or after `terminate`.

#### `PhysicsDriver.computeTimeStep(self)`

(Mandatory) Return the next preferred time step (time increment) for this code, and whether the code wants to stop.

Both data are only indicative, the supervisor is not required to take them into account. This method is however marked as mandatory, since most of the coupling schemes expect the code to provide this information (those schemes then typically compute the minimum of the time steps of all the codes being coupled). Hence a possible implementation is to return a huge value, if a precise figure can not be computed.

Can be called whenever the code is outside the `TIME_STEP_DEFINED` context (see `PhysicsDriver` documentation).

## Returns

tuple(float, bool)  
A tuple `(dt, stop)`. `dt` is the preferred time step for this code (only valid if `stop` is False). `stop` is True if the code wants to stop. It can be used for example to indicate that, according to a certain criterion, the end of the transient computation is reached from the code point of view.

## Raises

AssertionError  
If called inside the `TIME_STEP_DEFINED` context (see `PhysicsDriver` documentation).

AssertionError  
If called before `initialize` or after `terminate`.

#### `PhysicsDriver.initTimeStep(self, dt)`

(Mandatory) Provide the next time step (time increment) to be used by the code.

After this call (if successful), the computation time step is defined to `]t, t + dt]` where `t` is the value returned by `presentTime`. The code enters the `TIME_STEP_DEFINED` context. A time `step = 0`. may be used when the stationaryMode is set to True for codes solving directly for the steady-state.

## Parameters

dt : float  
The time step to be used by the code.

## Returns

bool  
False means that the given time step is not compatible with the code time scheme.

## Raises

AssertionError  
If called inside the `TIME_STEP_DEFINED` context (see `PhysicsDriver` documentation).

AssertionError  
If called before `initialize` or after `terminate`.

ValueError  
If `dt` is invalid (`dt < 0.0`).

#### `PhysicsDriver.solve(self)`

Call `solveTimeStep` but store its return value instead of returning it.

The output is accessible with .

<div class="warning">

<div class="title">

Warning

</div>

This method, in association with , should always be used inside C3PO instead of `solveTimeStep`. They fit better with MPI use.

This method should never be redefined: define `solveTimeStep` instead!

</div>

#### `PhysicsDriver.getSolveStatus(self)`

Return the output of the last call to `solveTimeStep` made through .

<div class="warning">

<div class="title">

Warning

</div>

This method, in association with , should always be used inside C3PO instead of `solveTimeStep`. They fit better with MPI use.

This method should never be redefined: define `solveTimeStep` instead!

</div>

## Returns

bool  
True if computation was successful, False otherwise.

#### `PhysicsDriver.solveTimeStep(self)`

(Mandatory) Perform the computation on the current time interval.

Can be called whenever the code is inside the `TIME_STEP_DEFINED` context (see `PhysicsDriver` documentation).

<div class="warning">

<div class="title">

Warning

</div>

This method is not adapted to MPI Master-Workers paradigm. and methods should be used with C3PO instead.

</div>

## Returns

bool  
True if computation was successful, False otherwise.

## Raises

AssertionError  
If called outside the `TIME_STEP_DEFINED` context (see `PhysicsDriver` documentation).

AssertionError  
If called several times without a call to `validateTimeStep` or to `abortTimeStep`.

#### `PhysicsDriver.validateTimeStep(self)`

(Mandatory) Validate the computation performed by `solveTimeStep`.

Can be called whenever the code is inside the `TIME_STEP_DEFINED` context (see `PhysicsDriver` documentation). After this call:

- the present time has been advanced to the end of the computation time step
- the computation time step is undefined (the code leaves the `TIME_STEP_DEFINED` context).

## Raises

AssertionError  
If called outside the `TIME_STEP_DEFINED` context (see `PhysicsDriver` documentation).

AssertionError  
If called before the `solveTimeStep` method.

#### `PhysicsDriver.setStationaryMode(self, stationaryMode)`

(Mandatory) Set whether the code should compute a stationary solution or a transient one.

New in version 2 of ICoCo. By default the code is assumed to be in stationary mode False (i.e. set up for a transient computation). If set to True, `solveTimeStep` can be used either to solve a time step in view of an asymptotic solution, or to solve directly for the steady-state. In this last case, a time step = 0. can be used with `initTimeStep` (whose call is always needed). The stationary mode status of the code can only be modified by this method (or by a call to `terminate` followed by `initialize`).

Can be called whenever the code is outside the `TIME_STEP_DEFINED` context (see `PhysicsDriver` documentation).

## Parameters

stationaryMode : bool  
True if the code should compute a stationary solution.

## Raises

AssertionError  
If called outside the `TIME_STEP_DEFINED` context (see `PhysicsDriver` documentation).

AssertionError  
If called before `initialize` or after `terminate`.

#### `PhysicsDriver.getStationaryMode(self)`

(Mandatory) Indicate whether the code should compute a stationary solution or a transient one.

See also `setStationaryMode`.

Can be called whenever the code is outside the `TIME_STEP_DEFINED` context (see `PhysicsDriver` documentation).

## Returns

bool  
True if the code has been set to compute a stationary solution.

## Raises

AssertionError  
If called inside the `TIME_STEP_DEFINED` context (see `PhysicsDriver` documentation).

AssertionError  
If called before `initialize` or after `terminate`.

#### `PhysicsDriver.isStationary(self)`

(Optional) Return whether the solution is constant on the computation time step.

Used to know if the steady-state has been reached. This method can be called whenever the computation time step is not defined.

## Returns

bool  
True if the solution is constant on the computation time step.

## Raises

AssertionError  
If called inside the `TIME_STEP_DEFINED` context (see `PhysicsDriver` documentation), meaning we shouldn't request this information while the computation of a new time step is in progress.

AssertionError  
If called before `initialize` or after `terminate`.

#### `PhysicsDriver.abortTimeStep(self)`

(Optional) Abort the computation on the current time step.

Can be called whenever the computation time step is defined, instead of `validateTimeStep`. After this call, the present time is left unchanged, and the computation time step is undefined (the code leaves the `TIME_STEP_DEFINED` context).

## Raises

AssertionError  
If called outside the `TIME_STEP_DEFINED` context (see `PhysicsDriver` documentation).

#### `PhysicsDriver.resetTime(self, time_)`

(Optional) Reset the current time of the `PhysicsDriver` to a given value.

New in version 2 of ICoCo. Particularly useful for the initialization of complex transients: the starting point of the transient of interest is computed first, the time is reset to 0, and then the actual transient of interest starts with proper initial conditions, and global time 0.

Can be called outside the `TIME_STEP_DEFINED` context (see `PhysicsDriver` documentation).

## Parameters

time\_ : float  
The new current time.

## Raises

AssertionError  
If called inside the `TIME_STEP_DEFINED` context (see `PhysicsDriver` documentation).

AssertionError  
If called before `initialize` or after `terminate`.

#### `PhysicsDriver.iterate(self)`

Call `iterateTimeStep` but store its return value instead of returning it.

The output is accessible with .

<div class="warning">

<div class="title">

Warning

</div>

This method, in association with , should always be used inside C3PO instead of `iterateTimeStep`. They fit better with MPI use.

This method should never be redefined: define `iterateTimeStep` instead!

</div>

#### `PhysicsDriver.getIterateStatus(self)`

Return the output of the last call to `iterateTimeStep` made through .

<div class="warning">

<div class="title">

Warning

</div>

This method, in association with , should always be used inside C3PO instead of `iterateTimeStep`. They fit better with MPI use.

This method should never be redefined: define `iterateTimeStep` instead!

</div>

## Returns

tuple(bool,bool)  
A tuple `(succeed, converged)`. `succeed = False` if the computation fails. `converged = True` if the solution is not evolving any more.

#### `PhysicsDriver.iterateTimeStep(self)`

(Optional) Perform a single iteration of computation inside the time step.

This method is relevant for codes having inner iterations for the computation of a single time step. Calling `iterateTimeStep` until `converged` is True is equivalent to calling `solveTimeStep`, within the code's convergence threshold. Can be called (potentially several times) inside the `TIME_STEP_DEFINED` context (see `PhysicsDriver` documentation).

<div class="warning">

<div class="title">

Warning

</div>

This method is not adapted to MPI Master-Workers paradigm. and methods should be used with C3PO instead.

</div>

## Returns

tuple(bool, bool)  
A tuple `(succeed, converged)`. `succeed = False` if the computation fails. `converged = True` if the solution is not evolving any more.

## Raises

AssertionError  
If called outside the `TIME_STEP_DEFINED` context (see `PhysicsDriver` documentation).

#### `PhysicsDriver.save(self, label, method)`

(Optional) Save the state of the code.

The saved state is identified by the combination of `label` and `method` arguments. If `save` has already been called with the same two arguments, the saved state is overwritten.

## Parameters

label : int  
A user- (or code-) defined value identifying the state.

method : str  
A string specifying which method is used to save the state of the code. A code can provide different methods (for example in memory, on disk, etc.).

## Raises

AssertionError  
If called inside the `TIME_STEP_DEFINED` context (see `PhysicsDriver` documentation), meaning we shouldn't save a previous time step while the computation of a new time step is in progress.

AssertionError  
If called before `initialize` or after `terminate`.

ValueError  
If the `method` or `label` argument is invalid.

#### `PhysicsDriver.restore(self, label, method)`

(Optional) Restore the state of the code.

After restore, the code should behave exactly like after the corresponding call to save (except of course for save/restore methods, since the list of saved states may have changed). The state to be restored is identified by the combination of `label` and `method` arguments. The `save` method must have been called at some point or in some previous run with this combination.

## Parameters

label : int  
A user- (or code-) defined value identifying the state.

method : str  
A string specifying which method was used to save the state of the code. A code can provide different methods (for example in memory, on disk, etc.).

## Raises

AssertionError  
If called inside the `TIME_STEP_DEFINED` context (see `PhysicsDriver` documentation), meaning we shouldn't restore a previous time step while the computation of a new time step is in progress.

AssertionError  
If called before `initialize` or after `terminate`.

ValueError  
If the `method` or `label` argument is invalid.

#### `PhysicsDriver.forget(self, label, method)`

(Optional) Discard a previously saved state of the code.

After this call, the save-point cannot be restored anymore. This method can be used to free the space occupied by unused saved states.

## Parameters

label : int  
A user- (or code-) defined value identifying the state.

method : str  
A string specifying which method was used to save the state of the code. A code can provide different methods (for example in memory, on disk, etc.).

## Raises

AssertionError  
If called before `initialize` or after `terminate`.

ValueError  
If the `method` or `label` argument is invalid.

#### `PhysicsDriver.setTransientLogger(self, transientLogger)`

Defines the logger for `solveTransient` method.

## Parameters

transientLogger : c3po.services.TransientLogger.TransientLogger  
Logger instance.

#### `PhysicsDriver.setTransientPrintLevel(self, level)`

Set the print level for `solveTransient` method (0=None, 1 keeps only the first and last lines, 2 keeps everything).

## Parameters

level : int  
Integer in range \[0;2\]. Default = 0.

#### `PhysicsDriver.solveTransient(self, tmax, finishAtTmax=False, stopIfStationary=False)`

Make the `PhysicsDriver` to advance in time until it reaches the time `tmax` or it asks to stop.

The `PhysicsDriver` can ask to stop either with `computeTimeStep` (always checked) or with `isStationary` (only if `stopIfStationary` is set to True).

## Parameters

tmax : float  
Maximum time to be reached (compared with `presentTime`).

finishAtTmax : bool  
If set to True, the method ends with `time = tmax` (instead of `time >= tmax`).

stopIfStationary : bool  
If set to True, the method stops also if `isStationary` returns True.

#### `PhysicsDriver.getMPIComm(self)`
