<!-- source: modules/cosette/task.rst -->

# `task` — Task specification

This module collects a few task classes that can be used with the `scheduler` and `depgraph` modules.

This module defines a dummy `Task` class that may be used as a base class and extended.

The `Task.do()` method takes two arguments:

- `env` is an environment for task execution. The idea of the environment is that tasks may use it to store information about their execution. For instance, a task may create a file and store its location in the environment, so that later tasks may be able to retrieve it. The type of `env` is really immaterial, but it is probably natural to use a key-value mapping of some kind. Note, however, that most of the tasks defined in the `task` module hierarchy expect `env` to be an `Env` object.
- `config` is a `Config` object describing the configuration for the current run. Tasks may look up global configuration values here.

The `Task` class models two types of inter-task dependencies. **Hard dependencies** represent dependencies that are crucial for the execution of the task at hand. If task `A` has a hard dependency on task `B`, it means that `A` cannot run unless `B` has successfully completed. If `B` fails, then it makes no sense to run `A`. On the other hand, if task `A` has a **soft dependency** on task `B`, it means that `A` will not start before `B`'s termination, but it makes sense to run `A` even if `B` fails.

### `class valjean.cosette.task.TaskError  — bases: Exception`

An error that may be raised by `Task` classes.

### `class valjean.cosette.task.Task(name, *, deps=None, soft_deps=None)  — bases: ABC`

Base class for other task classes.

#### `Task.do(self, env, config)`

Perform a task.

param env  
The environment for this task.

#### `Task.add_dependency(self, dep)`

Add an item to the list of dependencies of this task.

#### `Task.depends(self, other)`

Return `True` if `self` depends on `other`.

#### `Task.soft_depends(self, other)`

Return `True` if `self` has a soft dependency on `other`.

### `class valjean.cosette.task.DelayTask(name, delay=1.0)  — bases: Task`

Task that waits for the specified number of seconds. This task is useful to test scheduling algorithms under different load conditions.

#### `DelayTask.do(self, env, config)`

Perform the task (i.e. sleep; I wish my life was like that).

param env  
The environment. Ignored.

### `valjean.cosette.task.det_hash(*args)`

Produce a deterministic hash for the collection of objects passed as an argument.

### `valjean.cosette.task.close_dependency_graph(tasks)`

Return the tasks along with all their dependencies.

param list tasks  
A list of tasks.

returns  
The list of tasks, their dependencies, the dependencies of their dependencies and so on.

rtype  
list(Task)
