---
name: icoco
description: ICoCo (Interface for Code Coupling, version 2) — the C++ norm (abstract class ICoCo::Problem) that simulation codes implement to be coupled; implemented by TRUST and used by C3PO. Use for any question about implementing or calling ICoCo: lifecycle and context rules (setDataFile, setMPIComm, initialize, terminate), time-step control (presentTime, computeTimeStep, initTimeStep, solveTimeStep, validateTimeStep, abortTimeStep, iterateTimeStep, stationary mode), save/restore, field and scalar I/O (MEDDoubleField/MEDIntField via MEDCoupling, getOutputMEDDoubleField, setInputMEDDoubleField, getInputValuesNames…), exceptions (WrongContext, WrongArgument, NotImplemented), SWIG wrapping, ICoCo v1 vs v2, and the official Python implementation (pip package `icoco`, abstract class icoco.Problem, ICoCoMethods/ICoCoMethodContext introspection).
---

# ICoCo v2 (02/2021): C++ norm and Python implementation

The official ICoCo repository (`github.com/cea-trust-platform/icoco-coupling`) has no prose manual. The **documentation is the header comments**, converted here into a Markdown reference. Paths are relative to this file's directory.

| File | Content |
|---|---|
| `docs/README.md` | What ICoCo is, the version, the MEDCoupling dependency (≥ 9.7), how to build the Doxygen docs and the SWIG example |
| `docs/api/ICoCoProblem.md` | **The norm itself**: the `ICoCo::Problem` class and its **56 documented members**, each with its full contract: mandatory/optional, when it may be called, return value, exceptions. The class comment defines the **TIME_STEP_DEFINED context** and the temporal semantics of exchanged fields |
| `docs/api/ICoCoMEDDoubleField.md`, `ICoCoMEDIntField.md`, `ICoCoField.md` | Field wrappers around MEDCoupling fields (`getMCField`, `setMCField`) |
| `docs/api/ICoCoExceptions.md` | `WrongContext`, `WrongArgument`, `NotImplemented` |
| `docs/api/ICoCoTrioField.md` | Legacy TRUST field type |
| `docs/swig/*.i` | SWIG interface example for a dummy code (`ProblemYourCode`), to expose an implementation in Python |
| `docs/api/INDEX.md` | All documented members |
| `docs/python/` | **Python implementation** (`pip install "icoco~=2.0.0"`, package v2.0.7, `github.com/cea-trust-platform/icoco-coupling-python`): introduction and quick start (`index.md`), API reference per module (`src/icoco.problem.md`, `icoco.exception.md`, `icoco.utils.md`, `icoco.version.md`), README |
| `docs/python/tests/` | Python tests. `conftest.py` contains **`MinimalProblem`** (a minimal working implementation) and **`SaveRestoreProblem`** |

## Essentials (from the headers)

- **Each method's comment says "(Mandatory)" (10 of them) or "(Optional)".** The default implementation of every method throws `ICoCo::NotImplemented`, so a code implements what it needs.
- **Call order:** `setDataFile()`/`setMPIComm()` → `initialize()` → time loop → `terminate()`. The time loop is `presentTime()`, `computeTimeStep()`, then `initTimeStep(dt)`, which enters TIME_STEP_DEFINED, then `solveTimeStep()` (or `iterateTimeStep()`), then `validateTimeStep()` or `abortTimeStep()`, which leaves it.
- **Field validity:** fields and values set inside TIME_STEP_DEFINED are only valid until the step is validated or aborted. Set them again at each step. Fields set outside it are permanent.
- **Time semantics:** whether a field refers to the start, middle or end of the step is not fixed by the norm. The coupled codes must agree on it.

## Python implementation (`icoco` package)

- `from icoco import Problem`, then subclass it. The class is an `abc.ABC`, and **9 methods are abstract** and must be implemented: `initialize`, `terminate`, `presentTime`, `computeTimeStep`, `initTimeStep`, `solveTimeStep`, `validateTimeStep`, `setStationaryMode`, `getStationaryMode`. The others raise `NotImplementedMethod` until overridden.
- Method names and contracts are the C++ ones, documented in Python docstrings in `docs/python/src/icoco.problem.md`. The C++ header (`docs/api/ICoCoProblem.md`) stays the reference for the full contract.
- Exceptions are in `icoco.exception`: `WrongContext`, `WrongArgument`, `NotImplementedMethod` (the C++ name is `NotImplemented`).
- `icoco.utils` provides `ICoCoMethods` (all method names) and `ICoCoMethodContext` (context restrictions per method), useful to check an implementation or write generic drivers.
- MEDCoupling and mpi4py are optional: they're only needed for field exchanges and MPI.
- Start from `MinimalProblem` in `docs/python/tests/conftest.py` when writing a new Python implementation.

## How to answer

1. For any method, read its block in `docs/api/ICoCoProblem.md` and quote its contract (context, mandatory/optional, exceptions). Don't infer behaviour the comment doesn't state.
2. **The API must not be modified** (the header says so). Codes derive from `ICoCo::Problem`, and an implementation may be partial.
3. Implementing ICoCo in Python: the `icoco` package (above). Writing coupling scripts between ICoCo codes: the **`c3po`** skill. Its `PhysicsDriver` follows the same API.
4. Cite the file and method.

## Related skills

- **`c3po`:** coupling scripts.
- **`salome-medcoupling`:** MEDCoupling fields.
