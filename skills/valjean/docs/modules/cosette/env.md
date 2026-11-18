<!-- source: modules/cosette/env.rst -->

# `env` — Environment for task execution

This module defines `Env`, a class that makes it simpler to add information about running tasks. An `Env` object can be created from an existing dictionary as follows:

> \>\>\> from valjean.cosette.env import Env \>\>\> quest = {'name': 'Sir Galahad', 'favourite colour': 'blue'} \>\>\> env_quest = Env(quest) \# a shallow copy of `quest` is performed

You can use an `Env` object as a glorified dicitionary (`Env` inherits from `dict`), but its main purpose is really to store information about concurrently running tasks (see `Task`). By convention, the keys in `Env` are assumed to be task names; the associated values are dictionaries storing whatever information may be useful about the task. The dictionaries are also expected to have a `'status'` key describing the current task status (see `TaskStatus`). An example of `Env` respecting these conventions is the following:

> \>\>\> from valjean.cosette.task import Task, TaskStatus \>\>\> class FindHolyGrail(Task): ... '''We derive a class from Task, which is abstract.''' ... def do(self, env, config): ... \# find the Holy Grail ... pass \>\>\> quest = FindHolyGrail('quest') \# 'quest' is the task name \>\>\> tasks = {quest.name: {'name': 'Sir Galahad', ... 'favourite colour': 'blue', ... 'status': TaskStatus.FAILED}} \>\>\> env = Env(tasks)

The `Env` API integrates well with the `task` module and provides a number of practical methods for dealing with tasks. For instance, there are `is_*` methods for all members of the `TaskStatus` enumeration:

> \>\>\> env.is_failed(quest) True \>\>\> print(env.get_status(quest)) \# equivalently TaskStatus.FAILED

Additionally, you can change the status of a task with

> \>\>\> env.set_status(quest, TaskStatus.DONE) \>\>\> env.set_done(quest) \# equivalent, shorter version

Information about the tasks, incuding their status, is stored with the task name as the key:

> \>\>\> print(env\[quest.name\]\['status'\]) TaskStatus.DONE

The `Env` class tries hard to be thread-safe; that is, all its methods will operate atomically. Internally, thread safety is enforced by locking the object whenever its contents are accessed. This, however, does not help in case of read-and-modify operations, as in the following example:

    >>> if env.is_done(quest):      # WARNING: do not try this at home
    ...     env.set_skipped(quest)  # race condition here!

This snippet is racy in multithreaded mode because another thread may change the status of `quest` after `is_done()` has released the lock but before `set_skipped()` has had the chance to acquire it. For these scenarios, `Env` offers the `atomically()` method, which accepts as an argument the action that should be performed. When called, `atomically()` first acquires the lock on the object, and then passes the `Env` object to the action. A thread-safe implementation of the read-and-modify trip above is implemented as follows:

> \>\>\> def modify_task1(env): ... if env.is_done(quest): ... env.set_skipped(quest) \>\>\> env.atomically(modify_task1) \>\>\> env.is_skipped(quest) True

### `class valjean.cosette.env.EnvError  — bases: Exception`

An error that may be raised by the `Env` class.

### `class valjean.cosette.env.Env(dictionary=None)  — bases: MutableMapping`

The `Env` class can be used to store and dynamically update information about concurrently running tasks, and offers thread-safety guarantees.

#### `Env.from_file(cls, path, *, fmt='pickle')`

Deserialize an `Env` object from a file.

param str path  
Path to the file.

param str fmt  
Serialization format (only `'pickle'` is supported for the moment).

returns  
The deserialized object.

#### `Env.to_file(self, path, *, task_name=None, fmt='pickle')`

Serialize an `Env` object to a file.

param str path  
path to the file.

param task_name  
name of the task to serialize, or `None` to serialize the whole environment.

type task_name  
str or None

param str fmt  
serialization format (only `'pickle'` is supported for the moment).

#### `Env.merge_done_tasks(self, other)`

Merge task status from another environment.

This method takes an additional environment `other` as an argument. If the same key appears in `self` and `other` and `other[key]['status'] == TaskStatus.DONE`, then it sets `self[key] = other[key]`.

The idea is that `self` might contain a pristine environment, while `other` might provide the results of a previous run. We want to mark completed tasks as `DONE`, but we also want to re-run those that failed.

param Env other  
The environment providing the updates.

#### `Env.set_status(self, task, status)`

Set `task`'s status to `status`.

#### `Env.get_status(self, task)`

Return `task`'s status.

#### `Env.atomically(self, action)`

Perform an action atomically on the environment dictionary. The dictionary passes itself as the first argument to `action`, which must be callable.

#### `Env.apply(self, env_update)`

Apply un update to the dictionary.

#### `Env.set_start_end_clock(self, task, *, start, end)`

Set the start and end time for the given task.

#### `Env.get_start_clock(self, task)`

Return the start time for the given task.

#### `Env.get_end_clock(self, task)`

Return the end time for the given task.

#### `Env.copy(self)`

Return a shallow copy of `self`.
