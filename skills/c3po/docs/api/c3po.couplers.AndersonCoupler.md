<!-- source: c3po/couplers/AndersonCoupler.py -->

# `c3po.couplers.AndersonCoupler`

Contain the class `AndersonCoupler`.

### `c3po.couplers.AndersonCoupler.deleteQRColumn(matrixQ, matrixR, dataTemp)`

INTERNAL

## Returns

> A new QR decomposition after deletion of one column.

### `class c3po.couplers.AndersonCoupler.AndersonCoupler(physics, exchangers, dataManagers)  — bases: Coupler`

`AndersonCoupler` inherits from `Coupler` and proposes a fixed point algorithm with Anderson acceleration.

A QR decomposition is used for the optimization problem.

The class proposes an algorithm for the resolution of $F(X) = X$. Thus `AndersonCoupler` is a `Coupler` working with :

- A single `PhysicsDriver` (possibly a `Coupler`) defining the calculations to be made each time $F$ is called.
- A list of `DataManager` allowing to manipulate the data in the coupling (the $X$).
- Two `Exchanger` allowing to go from the `PhysicsDriver` to the `DataManager` and vice versa.

Each `DataManager` is normalized with its own norm got after the first iteration. They are then used as a single `DataManager` using `CollaborativeDataManager`.

The first two iterations just do (with $n$ the iteration number):

$$X^{n+1} = F(X^{n})$$

Then the Anderson acceleration starts and computes $X^{n+1}$ as a linear combination of $[\alpha.F(X^{n-i}) + (1. - \alpha).X^{n-i}]$.

$\alpha$, the relative fraction of $F(X^{n-i})$ and $X^{n-i}$ can be set with `setAndersonDampingFactor`. Default value is 1 (only $F(X^{n-i})$).

The default order (number of previous states considered) is 2. Call `setOrder` to change it.

The convergence criteria is : $||F(X^{n}) - X^{n}|| / ||F(X^{n})|| < \rm{tolerance}$. The default norm used is the infinite norm. `Coupler.setNormChoice` allows to choose another one.

The default value of tolerance is 1.E-6. Call `setConvergenceParameters` to change it.

The default maximum number of iterations is 100. Call `setConvergenceParameters` to change it.

#### `AndersonCoupler.setConvergenceParameters(self, tolerance, maxiter)`

Set the convergence parameters (`tolerance` and maximum number of iterations).

## Parameters

tolerance  
The convergence threshold in $||F(X^{n}) - X^{n}|| / ||X^{n+1}|| < \rm{tolerance}$.

maxiter  
The maximal number of iterations.

#### `AndersonCoupler.setAndersonDampingFactor(self, andersonDampingFactor)`

Set the damping factor of the method, the relative contribution of $F(X^{k})$ and $X^{k}$ on the calculation of next step.

## Parameters

andersonDampingFactor  
The damping factor $\alpha$ in the formula $\alpha.F(X^{n-i}) + (1. - \alpha).X^{n-i}$.

#### `AndersonCoupler.setOrder(self, order)`

Set the order of the method.

## Parameters

order  
Order of Anderson method. This is also the number of previous states stored by the algorithm.

#### `AndersonCoupler.setPrintLevel(self, level)`

Set the print level during iterations (0=None, 1 keeps last iteration, 2 prints every iteration).

## Parameters

level : int  
Integer in range `[0;2]`. Default: 2.

#### `AndersonCoupler.setFailureManagement(self, leaveIfSolvingFailed)`

Set if iterations should continue or not in case of solver failure (`solveTimeStep` returns False).

## Parameters

leaveIfSolvingFailed : bool  
Set False to continue the iterations, True to stop. Default: False.

#### `AndersonCoupler.solveTimeStep(self)`

Solve a time step using the fixed point algorithm with Anderson acceleration.

Inspire de Homer Walker (<walker@wpi.edu>), 10/14/2011.

See also `c3po.PhysicsDriver.PhysicsDriver.solveTimeStep`.

#### `AndersonCoupler.getSolveStatus(self)`

See `PhysicsDriver.getSolveStatus`.
