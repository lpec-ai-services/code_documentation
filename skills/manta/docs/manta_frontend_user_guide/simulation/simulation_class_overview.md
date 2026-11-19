<!-- source: https://manta-project.gitlab.io/manta/manta_frontend_user_guide/simulation/simulation_class_overview.html -->

# Overview of the simulation `class`

A simulation tries to compute the evolution of a physical system over
several temporal sequences. Temporal sequences are defined by the user.

An example of definition of temporal sequences would typically be:

```python
temporal_sequences = [0, 2.5, 4]
```

which defines a first temporal sequence `[0, 2.5]` and a second one
`[2.5, 4]`. By defining such sequences, the user impose to MANTA a
start and an end simulation time, but also impose that the intermediate
times (`2.5` in the example above) will be among the simulation time
steps.

Temporal sequences are necessarily contiguous.

The management of time steps inside temporal sequences is handled by MANTA.

The main role of a simulation is to manage the time steps in the
temporal sequences. To do so, it relies on the coupling scheme and:

- A time increment computer, whose role is to compute the time increment
  at the beginning of the next time step. The default time increment
  computer returns the difference between the end of the temporal
  sequence and the current time step.
- A time step validator, whose role is to validate a time step after the
  convergence of the coupling scheme. If the time step is invalidated,
  the time step validator shall provide a new time step. The default
  time step validator only relies on user-defined functions.
- A convergence failure handler, whose role is to propose a default time
  step in case of divergence of the coupling scheme. The default
  convergence handler just takes the current time step and divides it by
  two.

A simulation also:

- intializes the physical system if it not initialized at the beginning
  of the simulation.
- calls user-defined initialization tasks
- calls the post-processings defined by the physical system or some
  user-defined post-processing tasks.

## Main parameters

- `times`: list of times defining the temporal sequences.
- `allowSubStepping`: boolean stating if sub stepping in case of
  convergence failure is allowed. The default value of this parameter is
  true.
- `independentTemporalSequences`: boolean stating if the temporal
  sequences are independent. Currently, this boolean only choose if the
  last time increment of the previous temporal sequence is taken into
  account to bound the first time increment of the current temporal
  sequence (bounding occurs if this boolean is false. The default value
  of this parameter is true.
- `minimalTimeIncrement`: minimal time increment. If the time
  increment decreases below this value, the simulation is stopped.
- `maximalTimeIncrement`: maximal time increment. The time step
  can't be greater than this value: the time is set to this value if its
  computation leads to a greater value.
- `criticalTimeStepSafetyCoefficient`: scaling factor that multiplies
  the computed critical time steps. Must be between \(0\) (excluded)
  and \(1\) (included). Defaults to \(1\).
- `maximumNumberOfFailuresPerTemporalSequence`: maximum number of
  failures or time step rejections allowed within each temporal sequence.
- `timeIncrementComputer`: strategy used to determine the next time step.
- `timeStepValidator`: strategy used to determine the next time step.
- `convergenceFailureHandler`: strategy used to determine how a
  divergence of the resolution shall be handled.
- `limitTimeIncrementIncrease`: boolean stating if the current
  estimate of the next time step can be greater than the previous time
  increment multiplied by the
  `maximalTimeIncrementRelativeIncrease` parameter.
- `maximalTimeIncrementRelativeIncrease`: coefficient used to
  determined the maximum ratio between the next time step and the
  previous one. The default value of this parameter is 1.1, allowing a
  \(10\%\) increase of the time step compared to the previous one.
- `limitTimeIncrementDecrease`: boolean stating if the current
  estimate of the next time step can be lower than the previous time
  increment multiplied by the
  :param`:maximalTimeIncrementRelativeDecrease parameter.
- `maximalTimeIncrementRelativeDecrease`: coefficient used to
  determined the minimum ratio between the next time step and the
  previous one. The default value of this parameter is 0.2, allowing
  the next time step to be 5 times smaller than the previous one.
- `balanceTimeIncrement`: boolean stating if time increments
  shall be balanced to avoid small time increments at the end of the
  temporal sequence.
- `timeIncrementBalancer`: strategy used to balance the time
  increments to avoid small time increments at the end of the temporal
  sequence.
- `maximumNumberOfTimeSteps`: maximum number of time steps
  allowed per call to the run method.

  See Section [How simulation is stopped](#simulation-ending) for details.
- `numberOfTimeStepsBetweenPostProcessings`: the number of time
  steps between two post-processing times marked as *explicitly
  requested by the user*.

  Note that the parameter `numberOfTimeStepsBetweenPostProcessings`
  has no effect if it is greater than the
  `maximumNumberOfTimeSteps` parameter.

  See Section [Conditions for post-processings to be executed](#simulation-post-processings) for details.
- `timeBetweenPostProcessings`: time between two post-processing
  times marked as *explicitly requested by the user*.

  See Section [Conditions for post-processings to be executed](#simulation-post-processings) for details.
- `monitors`: list of simulation monitors.

  See Section [Monitoring a simulation](../miscellaneous/simulation_monitors.md#user-guide-simulation-monitors) for details.

## Time steps management

### Determining the next time increment at the beginning of a time step

Let \(t\) be the time at the beginning of the current time step and
\(t_{e}\) the end of the current temporal sequence and
\(\Delta\,t^{(p)}\) the previous time step.

The next time increment is defined as follows:

- A first candidate \(\Delta\, t_{1}\) is given by calling the
  method of the getNextTimeIncrement of the coupling scheme. This time
  increment is the minimum increment returned by the
  getNextTimeIncrement of all coupling items.
- A second candidate \(\Delta\, t_{2}\) is given by calling the time
  increment computer.
- \(\Delta\, t_{3}\) is the minimum of \(\Delta\, t_{1}\) and
  \(\Delta\, t_{2}\), \(t_{e}-t\) and \(\Delta\,
  t_{\textrm{max}}\) if the maximal time increment \(\Delta\,
  t_{\textrm{max}}\) has been defined (see the
  `maximalTimeIncrement`).
- if \(\Delta\, t_{3}\) is greater \(\Delta\,t_{(p)}\) and if
  the `limitTimeIncrementIncrease` parameter is true,
  \(\Delta\, t_{3}\) is limited by
  \(\alpha_{\textrm{i}}\,\Delta\,t_{(p)}\) where
  \(\alpha_{\textrm{i}}\) is the value of the
  `maximalTimeIncrementRelativeIncrease` parameter.
- if \(\Delta\, t_{3}\) is lower \(\Delta\,t_{(p)}\) and if the
  `limitTimeIncrementDecrease` parameter is true,
  \(\Delta\, t_{3}\) is limited by
  \(\alpha_{\textrm{d}}\,\Delta\,t_{(p)}\) where
  \(\alpha_{\textrm{i}}\) is the value of the
  `maximalTimeIncrementRelativeDecrease` parameter.
- if \(\Delta\, t_{3}\) is lower than \(\Delta\,
  t_{\textrm{min}}\), the simulation is stopped.

The time increment \(\Delta\, t_{3}\) can be balanced to avoid the
small time steps at the end of the time step (see the
`balanceTimeIncrement` and `timeIncrementBalancer`
parameters).

### Determining the next time increment in case of convergence failure

In case of convergence failure, the convergence failure handler is
called to propose an estimate of a new time increment
\(\Delta\,t_{e}\).

The next time increment is computed as follows:

\[\Delta\,t = \max(\Delta\,t_{e}, \alpha_{\textrm{i}}\, \Delta\,t_{c});\]

where \(\alpha_{\textrm{i}}\) is the value of the
`maximalTimeIncrementRelativeIncrease` parameter and
\(\Delta\,t_{c}\) the current time increment (corresponding to the
time step which lead to a failure).

The default convergence failure handler divides the current time step by
(2).

### Determining the next time increment in case of invalidation of the time step

The time step validator must propose an estimate of a new time increment
\(\Delta\,t_{e}\) when it invalidates the current time step.

The next time increment is computed as follows:

\[\Delta\,t = \max(\Delta\,t_{e}, \alpha_{\textrm{i}}\, \Delta\,t_{c});\]

where \(\alpha_{\textrm{i}}\) is the value of the
`maximalTimeIncrementRelativeIncrease` parameter and
\(\Delta\,t_{c}\) the current time increment (corresponding to the
rejected time step).

The default time step validator just calls user defined validators. If
no user defined validator is defined, the time step is always validated.

### How simulation is stopped

Simulation may fail du to non-convergence of the coupling scheme and
excessive sub-steppings.

Simulation may stop on success for two reasons:

- the last temporal sequence has been completed,
- the maximum number of time steps has been reached.

In the second case, the `run` method can be called again and again,
up to the point where the last temporal sequence has been completed.

To know, if last temporal sequence has been completed, one may check the
output of the `getTimes` methods:

- if the returned array contains only one value (corresponding the the
  value of the time at the end of the last temporal sequence), then the
  last temporal sequence has been completed,
- if the returned array contains more than one value, one may safely call
  the `run` method again.

### Conditions for post-processings to be executed

Every time a post-processing is called, it recieves a boolean stating if
the post-processing time as been *explicitly requested by the user*.

Lightweight post-processings (`Curves` for instance) may ignore
this boolean by default.

This boolean is mostly important for heavy post-processsings in terms of
memory, disk usage or computations, such as the `VTKExport`
post-processing.

By convention, every post-processing shall expose a parameter named
boolean `allTimeSteps` which allows to select if the
post-processing must be executed at the end of each time step or only at
at times
*explicitly requested by the user*.

The difference between lightweight and heavy post-processings is only
the default value of this parameter (`true` for lightweight
post-processings, `false` for heavy post-processings).

#### Post-processings times *explicitly requested by the user*

The end of each temporal sequence is always a post-processing times.

Two parameters allows to select additional post-processing times:

- `numberOfTimeStepsBetweenPostProcessings` the number of time
  steps between two post-processing times marked as *explicitly
  requested by the user*.
- `timeBetweenPostProcessings` between two post-processings
  marked as *explicitly requested by the user*.

The criteria (to mark a post-processing time as *explicitly requested by
the user*) associated with those parameters rely with some internal
counters which are reset at each call to the `run` method.

Note also that those criteria are taken evaluated independently, i.e. if
the criterion associated with
`numberOfTimeStepsBetweenPostProcessings` is satisfied, it does
not reset the internal timer associated with the criterion associated
with the `timeBetweenPostProcessings`.

Note that:

- each end of a temporal sequence is always flaged as *explicitly
  requested by the user*, independently of the
  `numberOfTimeStepsBetweenPostProcessings` parameter,

## Appendix

### Description of the default time increment balancer

Let \(\Delta\, t_{c}\) be the current estimate of the time
increment, \(t\) be the time at the beginning of the current time
step and \(t_{e}\) the end of the current temporal sequence.

Let \(q\) be equal to \(\lfloor (t_{e}-t)/\Delta\, t_{c} \rfloor\)
(where \(\lfloor x \rfloor\) is the integral part of \(x\)) and
\(r\) be equal to \((t_{e}-t)/\Delta\, t_{c}-q\). Note that r
is positive and lower than \(1\).

Assuming that the time increment remains constant, the number of time
steps will be:

1. \(q\) if \(t_{e}-t\) is exactly proportional to
   \(\Delta\, t_{c}\). This case can only be verified approximatly by
   verifying that \(r\) is close enough to \(0\). The default
   time increment balancer compares r to a value
   \(r_{\textrm{min}}\) whose default value is \(5\,10^{-2}\) and
   which can be modified by a parameter named named
   `minimalRelativeRemainder` .
2. \(q+1\) otherwise. However, this may lead to a final time step
   that can be much smaller than the other. To avoid this, \(r\) is
   compared to a parameter named `maximalRelativeRemainder` whose
   default value is \(0.8\).

The default time increment balancer thus selects the time step as follows:

- If \(r<r_{\textrm{min}}\), the time increment is chosen as \((t_{e}-t)/q\).
- If \(r>r_{\textrm{max}}\), the time increment is chosen as \(\Delta\, t_{c}\).
- If \(r_{\textrm{min}} \leq r \leq r_{\textrm{max}}\), the time
  increment is chosen as \((t_{e}-t)/(q+1)\).
