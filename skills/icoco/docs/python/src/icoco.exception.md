<!-- source: src/icoco.exception.rst -->

# icoco.exception module

ICoCo file common to several codes Version 2 -- 02/2021

WARNING: this file is part of the official ICoCo API and should not be modified. The official version can be found at the following URL:

<https://github.com/cea-trust-platform/icoco-coupling>

This module contains the exceptions for ICoCo specifications.

### `class icoco.exception.WrongContext(prob: str, method: str, precondition: str) -> None  — bases: Exception`

Exception raised when an ICoCo method is called at the wrong place.

This exception is raised whenver an ICoCo method is called when it shouldn't. This is for example the case if the icoco.Problem.initTimeStep() method is called when icoco.Problem.initialize() hasn't been called yet.

### `class icoco.exception.WrongArgument(prob: str, method: str, arg: str, condition: str) -> None  — bases: Exception`

Exception raised when an ICoCo method is called with an invalid argument.

This exception is raised whenver an ICoCo method is called with inappropriate arguments. This is for example the case if the Problem::getOutputField() is called with a non-existing field name.

### `class icoco.exception.NotImplementedMethod(prob: str, method: str) -> None  — bases: NotImplementedError`

Exception raised when one tries to call an ICoCo method which is not implemented.

By default all ICoCo methods raise this exception. The code implementing the norm should derive the Problem class and override (at least partially) this default implementation.
