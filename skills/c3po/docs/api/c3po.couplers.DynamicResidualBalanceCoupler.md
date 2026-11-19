<!-- source: c3po/couplers/DynamicResidualBalanceCoupler.py -->

# `c3po.couplers.DynamicResidualBalanceCoupler`

Contains the class `DynamicResidualBalanceCoupler`.

### `class c3po.couplers.DynamicResidualBalanceCoupler.DynamicResidualBalanceCoupler(physics, exchangers, dataManagers)  — bases: Coupler`

`DynamicResidualBalanceCoupler` inherits from `Coupler` and proposes a dynamic residual balance algorithm. This is a variant of the adaptive residual balance implemented by `c3po.couplers.AdaptiveResidualBalanceCoupler.AdaptiveResidualBalanceCoupler`.

This algorithm is designed to couple two solvers using an iterative procedure. It controls the accuracy required to each solver in order to limit over-solving and make them converge together.

See R. Delvaux, "Algorithmes de couplage entre neutronique, thermohydraulique et thermique", PhD Thesis, Institut Polytechnique de Paris, 2022.

`DynamicResidualBalanceCoupler` works with :

- Two `PhysicsDriver`, one for each solver. They must implement the `iterateTimeStep` method, together with the possibilities to get residual and set target accuracy.
- Four `Exchanger`: two for exchanges between the `PhysicsDriver`, and two to get residuals.
- One `LocalDataManager` (not just a `DataManager`) which contains the residuals got with the last two exchangers.

<div class="note">

<div class="title">

Note

</div>

Two `Exchanger` and a `DataManager` are used to access the residuals in order to support all possible MPI schemes.

</div>

The default target accuracies are 1e-4 and the default maximum number of iterations is 100. Use `setConvergenceParameters` to change these values.

It may be interesting to use a `FixedPointCoupler` to add a damping factor and to control the coupling error.

In this case :

- The option `setUseIterate(True)` of `FixedPointCoupler` must be used.
- The maximal number of iterations provided to `DynamicResidualBalanceCoupler.setConvergenceParameters` is ignored.
- The exchanger '2to1' is also probably redondant with the `FixedPointCoupler` exchangers and, in this case, can be set to do nothing.

#### `DynamicResidualBalanceCoupler.setConvergenceParameters(self, targetResidualSolver1, targetResidualSolver2, maxiter)`

Set the convergence parameters (target residuals for each solver and maximum number of iterations).

## Parameters

targetResidualSolver1  
Target residual for solver 1. Default value: 1.E-4.

targetResidualSolver2  
Target residual for solver 2. Default value: 1.E-4.

maxiter  
The maximal number of iterations. Default value: 100.

#### `DynamicResidualBalanceCoupler.setPrintLevel(self, level)`

Set the print level during iterations (0=None, 1 keeps last iteration, 2 prints every iteration).

## Parameters

level : int  
Integer in range \[0;2\]. Default: 2.

#### `DynamicResidualBalanceCoupler.setFailureManagement(self, leaveIfSolvingFailed)`

Set if iterations should continue or not in case of solver failure (`solveTimeStep` returns False).

## Parameters

leaveIfSolvingFailed : bool  
Set False to continue the iterations, True to stop. Default: False.

#### `DynamicResidualBalanceCoupler.solveTimeStep(self)`

See `c3po.PhysicsDriver.PhysicsDriver.solveTimeStep`.

#### `DynamicResidualBalanceCoupler.iterateTimeStep(self)`

See `c3po.PhysicsDriver.PhysicsDriver.iterateTimeStep`.

#### `DynamicResidualBalanceCoupler.getIterateStatus(self)`

See `c3po.PhysicsDriver.PhysicsDriver.getSolveStatus`.

#### `DynamicResidualBalanceCoupler.getSolveStatus(self)`

See `c3po.PhysicsDriver.PhysicsDriver.getSolveStatus`.

#### `DynamicResidualBalanceCoupler.initTimeStep(self, dt)`

See `c3po.PhysicsDriver.PhysicsDriver.initTimeStep`.
