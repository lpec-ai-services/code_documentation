<!-- source: c3po/couplers/FixedPointCoupler.py -->

# `c3po.couplers.FixedPointCoupler`

Contain the class `FixedPointCoupler`.

### `class c3po.couplers.FixedPointCoupler.FixedPointCoupler(physics, exchangers, dataManagers)  — bases: Coupler`

`FixedPointCoupler` inherits from `Coupler` and proposes a damped fixed point algorithm.

The class proposes an algorithm for the resolution of $F(X) = X$. Thus `FixedPointCoupler` is a `Coupler` working with :

- A single `PhysicsDriver` (possibly a `Coupler`) defining the calculations to be made each time $F$ is called.
- A list of `DataManager` allowing to manipulate the data in the coupling (the $X$).
- Two `Exchanger` allowing to go from the `PhysicsDriver` to the `DataManager` and vice versa.

Each `DataManager` is normalized with its own norm got after the first iteration. They are then used as a single `DataManager` using `CollaborativeDataManager`.

At each iteration we do (with $n$ the iteration number and alpha the damping factor):

$$X^{n+1} = \alpha . F(X^{n}) + (1 - \alpha).X^{n}$$

The convergence criteria is : $||F(X^{n}) - X^{n}|| / ||F(X^{n})|| < \rm{tolerance}$. The default norm used is the infinite norm. `setNormChoice()` allows to choose another one.

The default value of tolerance is 1.E-6. Call `setConvergenceParameters` to change it.

The default maximum number of iterations is 100. Call `setConvergenceParameters` to change it.

The default damping factor is 1 (no damping). Call `setDampingFactor` to change it.

#### `FixedPointCoupler.setConvergenceParameters(self, tolerance, maxiter)`

Set the convergence parameters (tolerance and maximum number of iterations).

## Parameters

tolerance  
The convergence threshold in $||F(X^{n}) - X^{n}|| / ||F(X^{n})|| < \rm{tolerance}$.

maxiter  
The maximal number of iterations.

#### `FixedPointCoupler.setDampingFactor(self, dampingFactor)`

Set the damping factor of the method.

## Parameters

dampingFactor  
The damping factor alpha in the formula $X^{n+1} = \alpha . F(X^{n}) + (1 - \alpha).X^{n}$.

#### `FixedPointCoupler.setPrintLevel(self, level)`

Set the print level during iterations (0=None, 1 keeps last iteration, 2 prints every iteration).

## Parameters

level : int  
Integer in range \[0;2\]. Default: 2.

#### `FixedPointCoupler.setFailureManagement(self, leaveIfSolvingFailed)`

Set if iterations should continue or not in case of solver failure (`solveTimeStep` returns False).

## Parameters

leaveIfSolvingFailed : bool  
Set False to continue the iterations, True to stop. Default: False.

#### `FixedPointCoupler.setUseIterate(self, useIterate)`

If True is given, the `iterate()` method on the given `PhysicsDriver` is called instead of the `solve()` method.

## Parameters

useIterate : bool  
Set True to use `iterate()`, False to use `solve()`. Default: False.

#### `FixedPointCoupler.iterateTimeStep(self)`

Make on iteration of a damped fixed-point algorithm.

See also `c3po.PhysicsDriver.PhysicsDriver.iterateTimeStep`.

#### `FixedPointCoupler.solveTimeStep(self)`

Solve a time step using the damped fixed-point algorithm.

See also `c3po.PhysicsDriver.PhysicsDriver.solveTimeStep`.

#### `FixedPointCoupler.getIterateStatus(self)`

See `PhysicsDriver.getSolveStatus`.

#### `FixedPointCoupler.getSolveStatus(self)`

See `PhysicsDriver.getSolveStatus`.

#### `FixedPointCoupler.initTimeStep(self, dt)`

See `c3po.PhysicsDriver.PhysicsDriver.initTimeStep`.
