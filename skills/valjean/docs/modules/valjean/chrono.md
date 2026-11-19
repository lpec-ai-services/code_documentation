<!-- source: modules/valjean/chrono.rst -->

# `chrono` — A context manager to time code sections

This module provides the `Chrono` context manager.

### `class valjean.chrono.Chrono()`

Time some code and store the elapsed time.

This class is a simple context manager that measures the execution time of a code fragment. The elapsed time is stored as a float in `self.elapsed` and can be accessed as such.

Examples:

\>\>\> with Chrono() as chrono: ... print(42) 42 \>\>\> print(f'printing 42 took {chrono} seconds') printing 42 took ... seconds
