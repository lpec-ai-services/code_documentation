<!-- source: https://manta-project.gitlab.io/manta/manta_frontend_user_guide/miscellaneous/simulation_monitors.html -->

# Monitoring a simulation

Simulation monitors are called at the end of each time step to report
information about how the execution of a simulation such as memory
usage.

See also

Further help about available monitors can be found in the
`Simulation Monitors` section of the online help which is
accessible in `python` through the `manta.info` function or
through the `manta-info` utility (see Section
[The manta-info utility](tools.md#manta-info-utility)).

PYTHON

```python
manta.info('Simulation monitors')
```

SH

```sh
manta-info "Simulation monitors"
```

There are mostly three ways to add a new monitor to a simuluation:

1. Use the `monitors` parameter when initializing the simulation:

   PYTHON

   ```python
   s = manta.Simulation(ps, times = [i * dt for i in range(0, nsteps + 1)],
                        monitors = [{'MemoryUsage': {}}])
   ```
2. Monitors can be added to a simulation using a first
   version of the `addMonitor` method. This version takes the name
   of the monitor and the parameters passed to the initialize the
   monitor.
3. Monitor can be generated using `create` method of the
   `SimulationMonitorFactory` class. The resulting monitor can then
   be added to the simulation using the `addMonitor` method. Direct
   usage of the `SimulationMonitorFactory` class is discouraged.

## [Available monitors](#id1)

### [`MemoryUsage`](#id2)

The `MemoryUsage` monitor displays the maximum amount of memory
used by manta since it was started.

### [`Convergence`](#id3)

The `Convergence` monitor displays various
information about the convergence of the coupling schemes and models
involved in the simulation.

#### [Example of usage](#id4)

```python
s = manta.Simulation(ps, times = times,
                     keepOutputs = True,
                     monitors = [{'Convergence': {'file': 'convergence-report.txt'}}])
```

#### [Parameters](#id5)

The `Convergence` monitor has only one parameter named
`file` which allows to specify an output file. This parameter is
optional. If not defined, the information are displayed in the
default output stream.

#### [Notes](#id6)

- Setting the `keepOutputs` parameter to `true` when creating the
  simulation is required for the Convergence monitor to work as expected.
- For the monitor to report the evolution of the residuals of solvers used
  by models, the solvers must report them. In the case of the `Newton`
  algorithm, this must be explicitly stated as follows:

  ```python
  mechanics = manta.Model('ImplicitMechanics', ps,
                          nonlinearSolver = {'Newton': {'switchFromRelativeToAbsoluteCriterion': True,
                                                        'thresholdOnTheFirstResidualNorm': 1e-100,
                                                        'convergenceTolerances': {'relativeConvergenceTolerance': reps},
                                                        'reportResidualNorms': True}})
  ```

#### [Typical output](#id7)

```text
Convergence reports for time step from '0.6' to '0.8'

- coupling scheme: main coupling scheme
  - number of iterations: 8
  - iteration 1
    - coupling item: ImplicitMechanicsModel(ImplicitMechanicsModel on [matrix])
      - number of iterations: 1
      - residuals evolutions (iteration number, absolute residual, relative residual):
        - 0 54.9893 1
    - coupling item: ImplicitMicromorphicDamageModel(ImplicitMicromorphicDamageModel on [matrix])
      - number of iterations: 2
      - residuals evolutions (iteration number, absolute residual, relative residual):
        - 0 0.00638389 1
        - 1 1.44291e-07 2.26023e-05
  - iteration 2
    - coupling item: ImplicitMechanicsModel(ImplicitMechanicsModel on [matrix])
      - number of iterations: 1
      - residuals evolutions (iteration number, absolute residual, relative residual):
        - 0 0.0777925 1
    - coupling item: ImplicitMicromorphicDamageModel(ImplicitMicromorphicDamageModel on [matrix])
      - number of iterations: 1
      - residuals evolutions (iteration number, absolute residual, relative residual):
        - 0 0.000513415 1
```
