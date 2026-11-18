<!-- source: modules/cosette/pythontask.rst -->

# `pythontask` — Wrap Python code in a task

This module implements a task class called `PythonTask`, which is able to execute arbitrary Python code (in the form of a function call) when requested to do so. This is extra useful because functions wrapped in `PythonTask` can receive the scheduling environment as an additional parameter, which makes it possible to write code that depends on the results of previous tasks.

## `PythonTask` objects

Creating a `PythonTask` is very simple. Let us define a function that returns a constant value:

> \>\>\> def func(): ... return 42

We can wrap the function in a `PythonTask` as follows:

> \>\>\> task = PythonTask('answer', func) \# 'answer' is the task name

We can then execute the task by passing an empty environment (dictionary) and an empty `Config` to the `PythonTask.do` method:

> \>\>\> task.do(env={}, config=None) 42

Note that `PythonTask.do` simply returns the result of the wrapped function. For the sake of illustration, our function returns an integer; however, if you want to use `PythonTask` in a `DepGraph`, your wrapped function will need to return an `(env_up, status)` pair, like the other tasks.

Note

Exceptions raised by the wrapped function are not caught by the task (they should be caught by the scheduler, though).

Calling a function without any arguments is not very restrictive per se. Say you want to call a function of two arguments:

> \>\>\> def add(x, y): ... return x + y

If you have your arguments lying around at the time you construct your task, then you may do something like

> \>\>\> x, y = 5, 3 \>\>\> task_add = PythonTask('add', lambda: add(x, y)) \>\>\> task_add.do(env={}, config=None) 8

Essentially, you construct a trampoline: the lambda takes no arguments, but it captures `x` and `y` from the surrounding scope and passes them to the `add` function. This works, but due to the way Python handles captured variables, it may bring a few surprises:

> \>\>\> x, y = 5, 3 \>\>\> task_add = PythonTask('add', lambda: add(x, y)) \>\>\> x, y = 1, 2 \>\>\> task_add.do(env={}, config=None) \# this still returns 8, right? 3 \>\>\> \# WAT

So, unless you know what you are doing, it is better to avoid this surprising behaviour and use the `args` argument to `PythonTask`:

> \>\>\> x, y = 5, 3 \>\>\> task_add = PythonTask('add', add, args=(x, y)) \>\>\> task_add.do(env={}, config=None) 8

There is also a `kwargs` argument that can be used to pass keyword arguments:

> \>\>\> task_add = PythonTask('add', add, kwargs={'x': x, 'y': y}) \>\>\> task_add.do(env={}, config=None) 8

## Passing arguments via the environment

Sometimes your function requires some arguments, but the arguments themselves are not available (e.g. they haven't been computed yet) by the time you create your `PythonTask`. For this purpose, `PythonTask` provides an additional feature that allows the called function to query the task environment and retrieve any additional information from there.

The mechanism is simple: the environment is passed to the wrapped function as a keyword argument. The keyword can be specified by the user using the `env_kwarg` argument to the `PythonTask` constructor.

As a simple example, consider the following function:

> \>\>\> def goodnight(*, some_dict): ... number = some_dict\['number'\] ... return 'Goodnight, ' + ('ding'*number)

You can wrap it in a `PythonTask` as follows:

> \>\>\> task_gnight = PythonTask('goodnight', goodnight, env_kwarg='some_dict')

and this is how it works:

> \>\>\> env = {'number': 8} \>\>\> task_gnight.do(env, config=None) 'Goodnight, dingdingdingdingdingdingdingding'

## Passing arguments via the environment: a more complex example

As an illustration of a more complex scenario, we will now implement a set of `PythonTask` objects to calculate the Pascal's triangle. In plain Python, the code to print all the rows up to the n-th would look something like this:

> \>\>\> import numpy as np \>\>\> def pascal(n): ... res = np.zeros((n, n), dtype=int) ... res\[:, 0\] = 1 ... res\[0, :\] = 1 ... for i in range(2, n): ... for j in range(1, i): ... res\[i-j, j\] = res\[i-j-1, j\] + res\[i-j, j-1\] ... return res \>\>\> direct_pascal = pascal(8) \>\>\> print(direct_pascal) \[\[ 1 1 1 1 1 1 1 1\] \[ 1 2 3 4 5 6 7 0\] \[ 1 3 6 10 15 21 0 0\] \[ 1 4 10 20 35 0 0 0\] \[ 1 5 15 35 0 0 0 0\] \[ 1 6 21 0 0 0 0 0\] \[ 1 7 0 0 0 0 0 0\] \[ 1 0 0 0 0 0 0 0\]\]

The logic is that each matrix element (except for those in the first row/column) is the sum of the element above and the element on the left.

In order to compute Pascal's triangle using `PythonTask` objects, we first need to decide on a strategy. We decide to use a `PythonTask` per matrix element. We also have to choose a strategy for naming the tasks, because the content of the environment is indexed by the task name. So we decide to call `'(i, j)'` the task that computes element `(i, j)`.

Armed with these conventions, we can write the function that computes element `(i, j)`:

> \>\>\> from valjean.cosette.task import TaskStatus \>\>\> def compute(name, i, j, \*, env): ... if i == 0 or j == 0: ... env_up = {name: {'result': 1}} ... return env_up, TaskStatus.DONE ... left = str((i-1, j)) ... above = str((i, j-1)) ... left_result = env\[left\]\['result'\] ... above_result = env\[above\]\['result'\] ... result = left_result + above_result ... env_up = {name: {'result': result}} ... return env_up, TaskStatus.DONE

Note that we have to return an environment update and a status. Now we construct the tasks and assemble them into a dependency dictionary:

> \>\>\> deps = {} \>\>\> name_to_task = {} \>\>\> n = 8 \>\>\> for k in range(n): ... \# k is the index of the row in the triange ... \# i and j index the matrix element, so k = i + j ... for i in range(k+1): ... j = k - i ... task_name = str((i, j)) ... task = PythonTask(task_name, compute, args=(task_name, i, j), ... env_kwarg='env') ... name_to_task\[task_name\] = task ... deps\[task\] = set() ... if i \> 0: ... index_left = str((i-1, j)) ... deps\[task\].add(name_to_task\[index_left\]) ... if j \> 0: ... index_above = str((i, j-1)) ... deps\[task\].add(name_to_task\[index_above\])

We can then import `DepGraph` and `Scheduler` and execute the dependency graph:

> \>\>\> from valjean.cosette.depgraph import DepGraph \>\>\> graph = DepGraph.from_dependency_dictionary(deps) \>\>\> from valjean.cosette.scheduler import Scheduler \>\>\> scheduler = Scheduler(hard_graph=graph) \>\>\> final_env = scheduler.schedule()

And now we can extract the results from the final environment:

> \>\>\> pythontask_pascal = np.zeros_like(direct_pascal) \>\>\> for k in range(n): ... for i in range(k+1): ... j = k - i ... task_name = str((i, j)) ... pythontask_pascal\[i, j\] = final_env\[task_name\]\['result'\] \>\>\> print(pythontask_pascal) \[\[ 1 1 1 1 1 1 1 1\] \[ 1 2 3 4 5 6 7 0\] \[ 1 3 6 10 15 21 0 0\] \[ 1 4 10 20 35 0 0 0\] \[ 1 5 15 35 0 0 0 0\] \[ 1 6 21 0 0 0 0 0\] \[ 1 7 0 0 0 0 0 0\] \[ 1 0 0 0 0 0 0 0\]\] \>\>\> np.all(pythontask_pascal == direct_pascal) True

## Passing arguments via the configuration

The function wrapped in a `PythonTask` can also inspect the global `valjean` configuration object. This may be useful to retrieve global settings for paths, for instance. Like the environment, you can specify that the configuration should be passed to the wrapped function as a keyword argument. The keyword is specified by the `config_kwarg` parameter to the `PythonTask` constructor. For example:

> \>\>\> from valjean.config import Config \>\>\> def print_output_dir(\*, config): ... print(config.query('path', 'output-root')) \>\>\> task = PythonTask('output-dir', print_output_dir, ... config_kwarg='config') \>\>\> config = Config() \>\>\> task.do(env={}, config=config) /.../output

## Module API

### `class valjean.cosette.pythontask.TaskException(reason='unknown')  — bases: Exception`

An exception that can be raised by any functions wrapped in `PythonTask`. It causes the task to fail. A reason can be specified in the constructor.

### `class valjean.cosette.pythontask.PythonTask(name, func, *, args=None, kwargs=None, env_kwarg=None, config_kwarg=None, deps=None, soft_deps=None)  — bases: Task`

Task that executes specified Python code.

#### `PythonTask.do(self, env, config)`

Execute the function.

param env  
The environment. It will be passed to the executed function as the `env_kwarg` keyword, if specified.

param config  
The config. It will be passed to the executed function as the `config_kwarg` keyword, if specified.
