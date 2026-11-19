<!-- source: c3po/couplers/JFNKCoupler.py -->

# `c3po.couplers.JFNKCoupler`

Contain the class `JFNKCoupler`.

### `c3po.couplers.JFNKCoupler.solveTriang(matrixA, vectorB)`

INTERNAL.

Solves a triangular linear system.

### `class c3po.couplers.JFNKCoupler.JFNKCoupler(physics, exchangers, dataManagers)  — bases: Coupler`

`JFNKCoupler` inherits from `Coupler` and proposes a Jacobian-Free Newton Krylov coupling algorithm.

This is a Newton algorithm using a Krylov (GMRES) method for the linear system solving.

The Jacobian matrix is not computed, but the product of the jacobian matrix with a vector $v$ is approximated by a Taylor formula ($J_u$ is the jacobian of $F$ at the point $u$):

$$J_u v \approx (F(u + \varepsilon v) - F(u))/\varepsilon$$

$\varepsilon$ is a parameter of the algorithm. Its default value is 1E-4. Call `setEpsilon` to change it

JFNKCoupler is a Coupler working with :

- A single `PhysicsDriver` (possibly a Coupler) defining the calculations to be made each time $F$ is called.
- A list of `DataManager` allowing to manipulate the data in the coupling.
- Two `Exchanger` allowing to go from the `PhysicsDriver` to the `DataManager` and vice versa.

Each `DataManager` is normalized with its own norm got after the first iteration. They are then used as a single `DataManager| using :class:`.CollaborativeDataManager\`.

As the Newton algorithm solves for $F(X) = 0$, in order to be coherent with the fixed point coupling algorithms, $F(x)$ is defined as $F(X) = f(X) - X$, where $f$ is the output of the physicsDriver.

The convergence criteria is : $||f(X^{n}) - X^{n}|| / ||f(X^{n})|| < \rm{tolerance}$. The default norm used is the infinite norm. `Coupler.setNormChoice` allows to choose another one.

The default Newton tolerance is 1.E-6. Call `setConvergenceParameters` to change it.

The default maximum Newton number of iterations is 10. Call `setConvergenceParameters` to change it.

The default Krylov tolerance is 1.E-4. Call `setKrylovConvergenceParameters` to change it.

The default maximum Krylov iteration is 100. Call `setKrylovConvergenceParameters` to change it.

#### `JFNKCoupler.setConvergenceParameters(self, tolerance, maxiter)`

Set the convergence parameters (tolerance and maximum number of iterations).

## Parameters

tolerance  
The convergence threshold in $||f(X^{n}) - X^{n}|| / ||f(X^{n})|| < \rm{tolerance}$.

maxiter  
The maximal number of iterations.

#### `JFNKCoupler.setKrylovConvergenceParameters(self, tolerance, maxiter)`

Set the convergence parameters (tolerance and maximum number of iterations) of the Krylov method.

## Parameters

tolerance  
The convergence threshold of the Krylov method.

maxiter  
The maximal number of iterations of the Krylov method.

#### `JFNKCoupler.setEpsilon(self, epsilon)`

Set the `epsilon` value of the method.

## Parameters

epsilon  
The `epsilon` value in the formula $J_u v \approx (F(u + \varepsilon v) -
F(u))/\varepsilon$.

#### `JFNKCoupler.setPrintLevel(self, level)`

Set the print level during iterations (0=None, 1 keeps last iteration, 2 prints every iteration).

## Parameters

level : int  
Integer in range \[0;2\]. Default: 2.

#### `JFNKCoupler.setFailureManagement(self, leaveIfSolvingFailed)`

Set if iterations should continue or not in case of solver failure (`solveTimeStep` returns False).

## Parameters

leaveIfSolvingFailed : bool  
Set False to continue the iterations, True to stop. Default: False.

#### `JFNKCoupler.solveTimeStep(self)`

Solve a time step using Jacobian-Free Newton Krylov algorithm.

See also `c3po.PhysicsDriver.PhysicsDriver.solveTimeStep`.

#### `JFNKCoupler.getSolveStatus(self)`

See `PhysicsDriver.getSolveStatus`.
