<!-- source: c3po/couplers/CrossedSecantCoupler.py -->

# `c3po.couplers.CrossedSecantCoupler`

Contain the class `CrossedSecantCoupler`.

### `class c3po.couplers.CrossedSecantCoupler.CrossedSecantCoupler(physics, exchangers, dataManagers)  — bases: Coupler`

`CrossedSecantCoupler` inherits from `Coupler` and proposes a fixed point algorithm with crossed secant acceleration.

The class proposes an algorithm for the resolution of $F(X) = X$. Thus `CrossedSecantCoupler` is a `Coupler` working with :

- A single `PhysicsDriver` (possibly a `Coupler`) defining the calculations to be made each time $F$ is called.
- A list of `DataManager` allowing to manipulate the data in the coupling (the $X$).
- Two `Exchanger` allowing to go from the `PhysicsDriver` to the `DataManager` and vice versa.

Each `DataManager` is normalized with its own norm got after the first iteration. They are then used as a single `DataManager` using `CollaborativeDataManager`.

At each iteration we do (with $n$ the iteration number):

$$X^{n+1} = F(X^{n}) - (F(X^{n}) - X^{n}).[(F(X^{n}) - F(X^{n-1})).(F(X^{n}) - X^{n} -$$$$(F(X^{n-1}) - X^{n-1}))]/(||F(X^{n}) - X^{n} - (F(X^{n-1}) - X^{n-1})||^2)$$

The convergence criteria is : $||F(X^{n}) - X^{n}|| / ||F(X^{n})|| < \rm{tolerance}$. The default norm used is the infinite norm. `setNormChoice()` allows to choose another one.

The default value of tolerance is 1.E-6. Call `setConvergenceParameters` to change it.

The default maximum number of iterations is 100. Call `setConvergenceParameters` to change it.

#### `CrossedSecantCoupler.setConvergenceParameters(self, tolerance, maxiter)`

Set the convergence parameters (`tolerance` and maximum number of iterations).

## Parameters

tolerance  
The convergence threshold in $||F(X^{n}) - X^{n}|| / ||X^{n+1}|| < \rm{tolerance}$.

maxiter  
The maximal number of iterations.

#### `CrossedSecantCoupler.setPrintLevel(self, level)`

Set the print level during iterations (0=None, 1 keeps last iteration, 2 prints every iteration).

## Parameters

level : int  
Integer in range \[0;2\]. Default: 2.

#### `CrossedSecantCoupler.solveTimeStep(self)`

Solve a time step using the damped fixed-point algorithm.

See also `c3po.PhysicsDriver.PhysicsDriver.solveTimeStep`.

#### `CrossedSecantCoupler.getSolveStatus(self)`

See `PhysicsDriver.getSolveStatus`.
