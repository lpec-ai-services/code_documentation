---
name: icoco
description: ICoCo (Interface for Code Coupling, version 2) — the C++ norm (abstract class ICoCo::Problem) that simulation codes implement to be coupled; implemented by TRUST and used by C3PO. Use for any question about implementing or calling ICoCo: lifecycle and context rules (setDataFile, setMPIComm, initialize, terminate), time-step control (presentTime, computeTimeStep, initTimeStep, solveTimeStep, validateTimeStep, abortTimeStep, iterateTimeStep, stationary mode), save/restore, field and scalar I/O (MEDDoubleField/MEDIntField via MEDCoupling, getOutputMEDDoubleField, setInputMEDDoubleField, getInputValuesNames…), exceptions (WrongContext, WrongArgument, NotImplemented), SWIG wrapping, and ICoCo v1 vs v2.
---

# ICoCo v2 (02/2021)

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

## Essentials (from the headers)

- **Each method's comment says "(Mandatory)" (10 of them) or "(Optional)".** The default implementation of every method throws `ICoCo::NotImplemented`, so a code implements what it needs.
- **Call order:** `setDataFile()`/`setMPIComm()` → `initialize()` → time loop → `terminate()`. The time loop is `presentTime()`, `computeTimeStep()`, then `initTimeStep(dt)`, which enters TIME_STEP_DEFINED, then `solveTimeStep()` (or `iterateTimeStep()`), then `validateTimeStep()` or `abortTimeStep()`, which leaves it.
- **Field validity:** fields and values set inside TIME_STEP_DEFINED are only valid until the step is validated or aborted. Set them again at each step. Fields set outside it are permanent.
- **Time semantics:** whether a field refers to the start, middle or end of the step is not fixed by the norm. The coupled codes must agree on it.

## How to answer

1. For any method, read its block in `docs/api/ICoCoProblem.md` and quote its contract (context, mandatory/optional, exceptions). Don't infer behaviour the comment doesn't state.
2. **The API must not be modified** (the header says so). Codes derive from `ICoCo::Problem`, and an implementation may be partial.
3. For Python-side coupling scripts, use the **`c3po`** skill (its `PhysicsDriver` is the Python form of this API).
4. Cite the file and method.

## Related skills

- **`c3po`:** coupling scripts.
- **`salome-medcoupling`:** MEDCoupling fields.
