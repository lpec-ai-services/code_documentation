<!-- source: modules/valjean.rst -->

# valjean — VALidation, Journal d'Évolution et ANalyse

Top-level module for the valjean package.

### `valjean.note(self, message, *args, **kwargs)`

New results level function

### `class valjean.ValjeanFormatter(fmt)`

Custom formatter for log messages.

This formatter class uses a different format for the `INFO` message level.

#### `ValjeanFormatter.format(self, record)`

Format the given record.

### `valjean.set_log_level(level)`

Set the verbosity level for the default logger.

### `valjean.get_logger(module)`

Get logger for the given module

### `valjean.set_logger_level(module, level=logging.INFO)`

Set the verbosity level for the required module logger.

param str module  
module name

param int level  
logger level (logging.DEBUG, logging.NOTE, logging.INFO, logging.WARNING, logging.ERROR)

### `valjean.local_logger_level(module, level)`

Set the verbosity level for the required module logger in a context case.

param str module  
module name

param int level  
logger level (logging.DEBUG, logging.NOTE, logging.INFO, logging.WARNING, logging.ERROR) - `valjean/chrono` (`valjean/chrono.md`) - `valjean/config` (`valjean/config.md`) - `valjean/dyn_import` (`valjean/dyn_import.md`) - `valjean/path` (`valjean/path.md`)
