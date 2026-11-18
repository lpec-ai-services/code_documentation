<!-- source: modules/cambronne/commands/run.rst -->

# `run` — The `run` subcommand

Module for the `run` subcommand.

### `class valjean.cambronne.commands.run.RunCommand  — bases: JobCommand`

Command class for the `run` subcommand.

#### `RunCommand.register(self, parser)`

Register options for this command in the parser.

#### `RunCommand.execute(self, args, config)`

Execute the `run` command.

#### `RunCommand.task_diagnostics(cls, *, tasks, env, config)`

Emit diagnostic messages about the status of the tasks. Count how many have succeeded, how many have failed, etc. If any tasks have failed, this method writes their names in a file called 'failed_tasks' in the log directory.

param tasks  
the tasks that have been scheduled.

type tasks  
list(Task)

param Env env  
the environment.

param Config config  
the configuration object.

#### `RunCommand.write_failed_tasks(cls, *, failed, config)`

Write the names of the failed tasks in the `failed_tasks` file.

param list(str) failed  
the names of the failed tasks.

param Config config  
the configuration object.

### `valjean.cambronne.commands.run.schedule(*, hard_graph, soft_graph, env, config=None, workers=1)`

Schedule a graph for execution.
