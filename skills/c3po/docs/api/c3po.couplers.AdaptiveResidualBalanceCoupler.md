<!-- source: c3po/couplers/AdaptiveResidualBalanceCoupler.py -->

# `c3po.couplers.AdaptiveResidualBalanceCoupler`

Contains the class `AdaptiveResidualBalanceCoupler`.

### `class c3po.couplers.AdaptiveResidualBalanceCoupler.AdaptiveResidualBalanceCoupler(physics, exchangers, dataManagers)  — bases: Coupler`

`AdaptiveResidualBalanceCoupler` inherits from `Coupler` and proposes a adaptive residual balance algorithm.

This algorithm is designed to coupled two solvers using an iterative procedure. It controls the accuracy required to each solver in order to limit over-solving and make them converge together.

See Senecal J. "Development of an efficient tightly coupled method for multiphysics reactor transient analysis" for details (for instance: <https://www.sciencedirect.com/science/article/pii/S0149197017302676>).

`AdaptiveResidualBalanceCoupler` works with :

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

The algorithm takes one parameter per solver, called initial convergence rate. They are set to 0.1 by default. Use `setConvRateInit` to change them.

It may be interesting to use a `FixedPointCoupler` to add a damping factor and to control the coupling error.

In this case :

- The option `setUseIterate(True)` of `FixedPointCoupler` must be used.
- The maximal number of iterations provided to `AdaptiveResidualBalanceCoupler.setTargetResiduals` is ignored.
- The exchanger '2to1' is also probably redondant with the `FixedPointCoupler` exchangers and, in this case, can be set to do nothing.

#### `AdaptiveResidualBalanceCoupler.setConvergenceParameters(self, targetResidualSolver1, targetResidualSolver2, maxiter)`

Set the convergence parameters (target residuals for each solver and maximum number of iterations).

## Parameters

targetResidualSolver1  
Target residual for solver 1. Default value: 1.E-4.

targetResidualSolver2  
Target residual for solver 2. Default value: 1.E-4.

maxiter  
The maximal number of iterations. Default value: 100.

#### `AdaptiveResidualBalanceCoupler.setConvRateInit(self, convRateSolver1Initial, convRateSolver2Initial)`

Set the initial convergence rates.

## Parameters

convRateSolver1Initial  
Initial convergence rate for solver 1. Default value: 0.1

convRateSolver2Initial  
Initial convergence rate for solver 2. Default value: 0.1

#### `AdaptiveResidualBalanceCoupler.setPrintLevel(self, level)`

Set the print level during iterations (`0=None`, 1 keeps last iteration, 2 prints every iteration).

## Parameters

level : int  
Integer in range \[0;2\]. Default: 2.

#### `AdaptiveResidualBalanceCoupler.setFailureManagement(self, leaveIfSolvingFailed)`

Set if iterations should continue or not in case of solver failure (`solveTimeStep` returns False).

## Parameters

leaveIfSolvingFailed : bool  
Set False to continue the iterations, True to stop. Default: False.

#### `AdaptiveResidualBalanceCoupler.solveTimeStep(self)`

See `c3po.PhysicsDriver.PhysicsDriver.solveTimeStep`.

#### `AdaptiveResidualBalanceCoupler.iterateTimeStep(self)`

See `c3po.PhysicsDriver.PhysicsDriver.iterateTimeStep`.

#### `AdaptiveResidualBalanceCoupler.getIterateStatus(self)`

See `c3po.PhysicsDriver.PhysicsDriver.getSolveStatus`.

#### `AdaptiveResidualBalanceCoupler.getSolveStatus(self)`

See `c3po.PhysicsDriver.PhysicsDriver.getSolveStatus`.

#### `AdaptiveResidualBalanceCoupler.initTimeStep(self, dt)`

See `c3po.PhysicsDriver.PhysicsDriver.initTimeStep`.
