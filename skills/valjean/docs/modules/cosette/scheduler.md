<!-- source: modules/cosette/scheduler.rst -->

# `scheduler` — Task scheduling and dependency handling

This module provides classes to schedule the execution of several tasks, possibly dependent on each other.

Example usage:

> \>\>\> from valjean.cosette.task import DelayTask \>\>\> spam = DelayTask('spam', 0.1) \>\>\> eggs = DelayTask('eggs', 0.2) \>\>\> bacon = DelayTask('bacon', 0.2)
>
> \>\>\> from valjean.cosette.depgraph import DepGraph \>\>\> g = DepGraph.from_dependency_dictionary({ ... spam: \[\], ... bacon: \[spam\], ... eggs: \[\] ... })
>
> \>\>\> from valjean.cosette.scheduler import Scheduler \>\>\> s = Scheduler(hard_graph=g) \>\>\> env = s.schedule() \# executes the tasks in the correct order

### `class valjean.cosette.scheduler.SchedulerError  — bases: Exception`

An error that may be raised by the `Scheduler` class.

### `class valjean.cosette.scheduler.Scheduler(*, hard_graph, soft_graph=None, backend=None)`

Schedule a number of tasks.

The Scheduler class has the responsibility of scheduling and executing a number of tasks. Here `hard_graph` is a `DepGraph` describing the *hard* dependencies among the tasks to be executed (see `task` for details about *hard* vs. *soft* dependencies); `soft_graph` is a `DepGraph` describing the *soft* dependencies alone; finally, `backend` should be an instance of a `*Scheduling` class such as `.QueueScheduling`, or at any rate a class that exhibits an `execute_tasks()` method with the correct signature (see `.QueueScheduling.execute_tasks()`). If `backend` is `None`, the default backend will be used.

param DepGraph hard_graph  
The dependency graph for hard dependencies.

param soft_graph  
The dependency graph for soft dependencies.

type soft_graph  
DepGraph or None

param backend  
The scheduling backend.

type backend  
None or QueueScheduling

raises ValueError  
if `depgraph` is not an instance of `DepGraph`.

raises SchedulerError  
if the tasks do not have any `do()` method.

#### `Scheduler.schedule(self, *, config=None, env=None)`

Schedule the tasks!

param Env env  
An initial environment for the scheduled tasks. This allows completed tasks to inform other, dependent tasks of e.g. the location of interesting files.

param Config config  
the configuration object.

returns  
The modified environment. Scheduling backends -------------------

## `queue` — Producer-consumer-queue backend

This module contains an implementation of a scheduling backend that leverages Python "threads" (`threading` module) and producer-consumer queues (`queue` module).

### `class valjean.cosette.backends.queue.QueueScheduling(n_workers=10)`

The default scheduling backend.

Uses `threading` and `queue` to handle concurrent execution of tasks.

#### `QueueScheduling.decide_new_state(cls, task, deps, hard_deps, env)`

Look at the dependencies of the current task and make a decision about what we should do with this task.

This function returns a `TaskStatus` that represents the suggested new state for this task, or `None` in case the task should be ignored and removed from the queue.

param Task task  
the task

param list(Task) deps  
the dependencies of `task`

param list(Task) hard_deps  
the hard dependencies of `task`

param Env env  
the environment.

rtype  
TaskStatus or None

#### `QueueScheduling.last_end_time(cls, tasks, env)`

Return the latest `end_clock` time of the given tasks, or `None` if some of the tasks do not have an `end_clock`.

#### `QueueScheduling.decide_new_state_waiting(cls, task, deps, hard_deps, env)`

Decide what to do with a task that is in `WAITING` state.

#### `QueueScheduling.execute_tasks(self, *, full_graph, hard_graph, env, config)`

Execute the tasks.

param DepGraph full_graph  
Full dependency graph for the tasks, i.e. including both hard and soft dependencies.

param DepGraph hard_graph  
Hard-dependency graph for the tasks.

param env  
An initial environment for the scheduled tasks.

type env  
Env

param env  
The configuration object (for things like paths, etc.).

type env  
Config
