<!-- source: modules/cosette/run.rst -->

# `run` — Task for generic command execution

This module defines a few useful functions and classes to embed generic command execution in a `depgraph`.

## Spawning external processes

code

\>\>\> from valjean.config import Config \>\>\> config = Config()

The `RunTask` class is the basic building block to run tasks that consist in spawning external processes and waiting for their completion. It makes it possible to execute arbitrary commands. Consider:

> \>\>\> from valjean.cosette.run import RunTask \>\>\> task = RunTask.from_cli(name='say', cli=\['echo', 'ni!'\]) \>\>\> env_update, status = task.do(env=dict(), config=config) \# prints 'ni!' \>\>\> print(status) TaskStatus.DONE

The task succeeded, but where is the output of our command?! Note that `RunTask` captures standard output and standard error and redirects them to files. If you want to see what was printed, you have to look there:

> \>\>\> def print_stdout(env_up, name): ... """A small function to print the stdout of a task.""" ... stdout = env_up\[name\]\['stdout'\] ... with open(stdout) as stdout_f: ... print(stdout_f.read(), end='') \>\>\> print_stdout(env_update, 'say') ni!

Note that `command` is not parsed by a shell. So the following may not do what you expect:

> \>\>\> task = RunTask.from_cli(name='want', ... cli=\['echo', 'We want... ', '&&', ... 'echo', 'a shrubbery!'\]) \>\>\> env_update, status = task.do(env=dict(), config=config) \>\>\> print_stdout(env_update, 'want') We want... && echo a shrubbery!

Indeed, `RunTask` ran `echo` only once. If you need to execute several commands, you can wrap them in a shell script and execute it. Alternatively, you can directly invoke the `RunTask.from_clis` class method:

> \>\>\> task = RunTask.from_clis(name='want', ... clis=\[\['echo', '-n', 'We want... '\], ... \['echo', 'a shrubbery!'\]\]) \>\>\> env_update, status = task.do(env=dict(), config=config) \>\>\> print_stdout(env_update, 'want') We want... a shrubbery!

## Creating tasks using a factory

When you want to create multiple `RunTask` objects using the same executable, it can be convenient to use `RunTaskFactory`. This class can be parametrized to create tasks by specifying the path to the executable once and for all, for instance, and providing the missing arguments later.

RunTaskFactory

\>\>\> import os \>\>\> from valjean.config import Config \>\>\> config = Config() \>\>\> def print_stdout(env_up, name): ... """A small function to print the stdout of a task.""" ... stdout = env_up\[name\]\['stdout'\] ... with open(stdout) as stdout_f: ... print(stdout_f.read(), end='')

The simplest way to create a `RunTaskFactory` is to use one of the `RunTaskFactory.from_executable` or `RunTaskFactory.from_task` class methods. For example, this will create a factory instance that generates `RunTask` objects for the `echo` executable:

> \>\>\> factory = RunTaskFactory.from_executable('echo', name='echo')

You can use it to generate tasks by invoking the `RunTaskFactory.make` method:

> \>\>\> task = factory.make(name='task', extra_args=\['spam'\])

This creates an `task.echo` object (of type `RunTask`) that executes `echo spam` when run:

> \>\>\> env_up, status = task.do(env={}, config=config) \>\>\> print_stdout(env_up, 'task.echo') spam

You can also leave the `name` parameter out. If you do so, `RunTaskFactory` will generate a name for you:

> \>\>\> task_sausage = factory.make(extra_args=\['sausage'\]) \>\>\> task_sausage.name '....echo'

Of course you can generate multiple tasks using the same factory (this is the whole point of `RunTaskFactory`, really):

> \>\>\> task_spam = factory.make(name='task_spam', extra_args=\['spam'\]) \>\>\> task_eggs = factory.make(name='task_eggs', extra_args=\['eggs'\]) \>\>\> task_bacon = factory.make(name='task_bacon', extra_args=\['bacon'\])

You can also specify a few arguments beforehand and provide the rest later:

> \>\>\> factory = RunTaskFactory.from_executable('echo', name='echo', ... default_args=\['spam'\]) \>\>\> task = factory.make(name='task', extra_args=\['eggs'\]) \>\>\> env_up, status = task.do(env={}, config=config) \>\>\> print_stdout(env_up, 'task.echo') spam eggs

Finally, you can parametrize your arguments on arbitrary keywords that will be provided when the task is created:

> \>\>\> args = \['{food}', 'with', '{side}'\] \>\>\> factory = RunTaskFactory.from_executable('echo', name='echo', ... default_args=args) \>\>\> task = factory.make(name='task', food='lobster', side='spam') \>\>\> env_up, status = task.do(env={}, config=config) \>\>\> print_stdout(env_up, 'task.echo') lobster with spam

Default values for the parameters may be specified when creating the factory and can be overridden when the task is created:

> \>\>\> args = \['{food}', 'with', '{side}'\] \>\>\> factory = RunTaskFactory.from_executable('echo', default_args=args, ... side='spam', name='echo') \>\>\> beans = factory.make(name='baked beans', food='baked beans') \>\>\> eggs = factory.make(name='eggs', food='eggs', ... side='bacon and spam') \>\>\> env_up, status = beans.do(env={}, config=config) \>\>\> print_stdout(env_up, 'baked beans.echo') baked beans with spam \>\>\> env_up, status = eggs.do(env={}, config=config) \>\>\> print_stdout(env_up, 'eggs.echo') eggs with bacon and spam

Note also that you can refer to the environment or the configuration in your command-line arguments:

> \>\>\> args = \['{env\[side\]}'\] \>\>\> factory = RunTaskFactory.from_executable('echo', name='echo', ... default_args=args) \>\>\> task = factory.make(name='task') \>\>\> env_up, status = task.do(env={'side': 'spam'}, config=config) \>\>\> print_stdout(env_up, 'task.echo') spam

### Caching

The `RunTaskFactory` class caches generated tasks under the hood. Repeated calls to `RunTaskFactory.make` from the same factory with the same arguments will result in the same task:

> \>\>\> factory = RunTaskFactory.from_executable('echo', name='echo') \>\>\> task_sausage = factory.make(extra_args=\['sausage'\]) \>\>\> task_sausage_again = factory.make(extra_args=\['sausage'\]) \>\>\> task_sausage is task_sausage_again True

If you instantiate another factory, the caching mechanism is defeated:

> \>\>\> other_factory = RunTaskFactory.from_executable('echo', name='echo') \>\>\> task_sausage_other = other_factory.make(extra_args=\['sausage'\]) \>\>\> task_sausage is task_sausage_other False

## Module API

### `valjean.cosette.run.run(clis, stdout, stderr, **subprocess_args)`

Run the given command lines and capture their stdout/stderr.

Execution stops at the first failure (result value != 0).

param list clis  
The list of commands to execute.

param stdout  
File handle to capture the stdout stream.

type stdout  
`file object`

param stderr  
File handle to capture the stderr stream.

type stderr  
`file object`

param dict subprocess_args  
Parameters to be passed to `subprocess.call`.

### `valjean.cosette.run.make_cap_paths(base_path)`

Construct filenames to capture stdout and stderr.

### `class valjean.cosette.run.RunTask(name, clis_closure, *, deps=None, soft_deps=None, **subprocess_args)  — bases: PythonTask`

Task that executes the specified shell commands and waits for their completion.

#### `RunTask.from_cli(cls, name, cli, **kwargs)`

Create a `RunTask` from a single command line.

Use the `RunTask.from_clis` method if you want to run several commands in a row.

param str name  
The name of this task.

param list cli  
The command line to be executed, as a list of strings. The first element of the list is the command and the following ones are its arguments.

param kwargs  
Any other keyword arguments will be passed on to the constructor (see `RunTask.__init__`).

#### `RunTask.from_clis(cls, name, clis, **kwargs)`

Create a `RunTask` from a list of command lines.

param str name  
The name of this task.

param list clis  
The command lines to be executed, as a list of lists of strings. The first element of each sub-list is the command and the following ones are its arguments.

param kwargs  
Any other keyword arguments will be passed on to the constructor (see `RunTask.__init__`).

#### `RunTask.run_task(self, clis_closure, name, **subprocess_args)`

Execute the specified command and wait for its completion.

On completion, this method proposes the following updates to the environment:

    env[task.name]['clis'] = clis
    env[task.name]['return_codes'] = return_codes
    env[task.name]['elapsed_time'] = wallclock_time
    env[task.name]['stdout'] = stdout
    env[task.name]['stderr'] = stderr

Here `clis` is the list of command lines that were executed, `return_codes` is the list of return codes of the executed commands, and `elapsed_time` is the time the whole list took. The keys `stdout` and `stderr` hold the paths to the files containing respectively the captured standard output and standard error streams.

param Env env  
The task environment.

param config  
The configuration object.

type config  
Config or None

returns  
The proposed environment update.

### `class valjean.cosette.run.RunTaskFactory(make_closure, *, deps=None, soft_deps=None, name, **kwargs)`

Create multiple tasks from the same executable without even breaking a sweat.

#### `RunTaskFactory.from_task(cls, task, *, relative_path, name=None, default_args=None, **kwargs)`

This class method creates a `RunTaskFactory` from a `Task`. The command to be executed must appear in the `output_dir` directory of the given task; its relative location must be specified with the `relative_path` argument.

This method can be used, among other things, to create a `RunTaskFactory` from a `CheckoutTask` or a `BuildTask`.

param task  
The `Task` object.

type task  
`Task`

param str relative_path  
The path to the executable, relative to the the output directory (`output_dir`) of the task.

param name  
a unique identifier for this factory. The factory name is used to produce unique names for the generated tasks. If `None` is given, the factory name will be constructed by hashing the other arguments.

type name  
str or None

param default_args  
see `RunTaskFactory.from_executable`.

param kwargs  
Any remaining arguments will be passed to the `__init__`.

#### `RunTaskFactory.from_executable(cls, path, name=None, default_args=None, **kwargs)`

This class method creates a `RunTaskFactory` from the path to an existing executable.

param str path  
the path to the executable.

param name  
a unique identifier for this factory. If `None` is given, the factory will use a hash of the other arguments.

type name  
str or None

param default_args  
The list of arguments that will be passed to the executed command by `RunTask`. It may contain expressions understood by Python's format mini-language, such as `{foo}`. These expressions can be filled when the task is generated by passing appropriate keyword arguments to the `make` method.

type default_args  
list(str) or None

param kwargs  
Any remaining arguments will be passed to the `__init__`.

#### `RunTaskFactory.make(self, *, name=None, extra_args=None, subprocess_args=None, deps=None, soft_deps=None, **kwargs)`

Create a `RunTask` object.

param name  
the name of the task to be generated, as a string. If `None` is passed, `RunTaskFactory` will generate a name by hashing the contents of all the other arguments.

type name  
str or None

param extra_args  
A list of additional arguments that will be appended at the end of the command line.

type extra_args  
list or None

param subprocess_args  
A dictionary of arguments for the call to the `.subprocess.Popen` constructor.

type subprocess_args  
dict or None

param deps  
A list of dependencies for the generated task. Note that factories built with `from_task` automatically inject dependencies on the given task.

type deps  
list(Task) or None

param soft_deps  
A list of soft dependencies for the generated task.

type soft_deps  
list(Task) or None

param kwargs  
Any remaining keyword arguments will be used to format the command line before execution. The environment and the configuration are available at formatting time as `env` and `config`, respectively.

#### `RunTaskFactory.copy(self)`

Return a copy of this object.
