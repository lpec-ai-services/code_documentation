<!-- source: modules/cambronne/common.rst -->

# `common` — Common tools for the `valjean` executable

Common utilities for `valjean` commands.

### `class valjean.cambronne.common.Command`

Base class for all `valjean` subcommands.

### `class valjean.cambronne.common.DictKwargAction  — bases: argparse.Action`

An `argparse.Action` subclass that parses arguments as `key=value` pairs and stores the resulting associations in a dictionary.

### `class valjean.cambronne.common.JobCommand  — bases: Command`

Base class for all `valjean` subcommands that take a job file and job arguments.

#### `JobCommand.register(self, parser)`

Add the `job_file` and `job_args` positional arguments to the parser.

### `valjean.cambronne.common.run_job(job_file, job_args, job_kwargs)`

Run the `job()` function from the specified job file and return its result.

param str job_file  
the name of the file containing the `job()` function.

param list(str) job_args  
the list of arguments to be passed to the `job()` function.

param dict job_kwargs  
a dictionary of keyword arguments for `job()`

returns  
whatever `job()` returns; expected to be a list of `Task` objects.

rtype  
list(Task)

### `valjean.cambronne.common.check_unique_task_names(tasks)`

Check that the tasks have unique names.

param list tasks  
A list of tasks.

raises ValueError  
if two or more tasks have the same name.

### `valjean.cambronne.common.collect_tasks(job_file, job_args, job_kwargs)`

Collect tasks from a job file, along with all their dependencies.

param str job_file  
the name of the file containing the `job()` function.

param list(str) job_args  
the list of arguments to be passed to the `job()` function.

param dict job_kwargs  
a dictionary of keyword arguments for `job()`

returns  
the collected tasks.

rtype  
list(Task)

### `valjean.cambronne.common.build_graphs(args)`

Build the dependency graphs according to the CLI parameters.

### `valjean.cambronne.common.read_env(*, root, names, filename, fmt)`

Create an initial environment for the given task names, possibly merging a set of serialized environments.

The environment will be created from the partial environments that were serialized for the given task names. Missing partial environments will be silently ignored.

If `filename` is `None`, no de-serialization will take place and an empty environment will be returned.

param str root  
path to the root directory containing all the environment files.

param list(str) names  
the list of task names that will be deserialized.

param filename  
Name of the file containing the serialized environment. If `None`, no de-serialzation will take place.

type filename  
str or None

param str fmt  
Environment serialization format (only `'pickle'` is supported at the moment).

returns  
an environment.

rtype  
Env

### `valjean.cambronne.common.write_env(env, *, filename, fmt)`

Serialize the environment to files.

The environment will be written to one file per task (i.e. one per environment key). The name of the environment file is given by the `filename` parameter, and the directory is the output directory (`'output_dir'` key) of the task. If the task does not have an `'output_dir'` key, serialization for that task will be skipped.

If `filename` is `None`, no serialization will take place at all.

param filename  
Name of the file containing the serialized environment. If `None`, no serialzation will take place.

type filename  
str or None

param str fmt  
Environment serialization format (only `'pickle'` is supported at the moment).
