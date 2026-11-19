---
name: c3po
description: C3PO (Collaborative Code Coupling PlatfOrm, CEA) — Python library for writing multiphysics coupling scripts between codes wrapped with the ICoCo API, exchanging MEDCoupling fields, sequentially or with MPI (SPMD, master/workers, collaborative). Use for any question about C3PO: PhysicsDriver, DataManager, Exchanger, Coupler, coupling algorithms (fixed point/Picard with damping, Anderson acceleration, JFNK, crossed secant, adaptive and dynamic residual balance), exchange methods (direct matching, shared remapping, multi-1D/3D), TimeAccumulator, transient and steady-state coupling, multi1D, MPI classes, services (listings, tracer, name changer, wrappers), and the ready-made drivers (APOLLO3, CATHARE2/3, CRONOS2, FLICA4, THEDI, TRUST, ALCYONE2, generic ICoCo).
---

# C3PO documentation (v2.4.2)

The docs come from the C3PO repository (`github.com/cea-code-coupling/c3po`, master branch). Paths are relative to this file's directory.

| Part | Content |
|---|---|
| `docs/mainpage.md` | **Overview**: framework (Python, MEDCoupling, MPI, ICoCo), and the **source overview**, a guided tour of every directory: couplers, exchange methods, services, raises, multi1D, MPI (common base, collaborative mode, master/workers mode). **Start here** |
| `docs/code_integration.md` | **How to make a code usable by C3PO**: Python wrapping (SWIG, F2PY…), MEDCoupling exchanges, MPI, the ICoCo API |
| `docs/api/c3po.*.md` | **API reference**, one page per module: class signature, bases, docstring (with LaTeX formulas) and methods, read from the source |
| `examples/` | **Working coupling scripts** (the repo's tests). See `examples/README.md` for what each one does |

## Examples by need

| Need | Example |
|---|---|
| Minimal coupling of two scalar models | `examples/scalar_linear/` |
| Fixed point vs Anderson vs JFNK on the same problem | `examples/matrix/` |
| Two meshes, MEDCoupling fields, sequential and MPI (SPMD, double-level SPMD, master/workers) | `examples/med_Dussaix/` |
| Steady state, then transient with exchanges every n steps | `examples/transient/` |
| 3D model coupled to several 1D models (multi1D), hybrid MPI | `examples/med_1D3D/`, `examples/med_multi1D3D/`, `examples/multi1D/` |
| Interface coupling of 2D thermal models, **every coupling algorithm** compared | `examples/plaques_coupling/` |
| Listings, renaming variables | `examples/listings/` |

## Key ideas

- A code is wrapped as a **`PhysicsDriver`**, C3PO's Python form of the ICoCo `Problem` API. Lifecycle and time stepping (`initialize`, `computeTimeStep`, `initTimeStep`, `solveTimeStep`, `validateTimeStep`, `solveTransient`…) are on `docs/api/c3po.PhysicsDriver.md`. Field and value I/O (`getOutputMEDDoubleField`, `setInputMEDDoubleField`, `getInputValuesNames`…) are **inherited from `DataAccessor`**, documented on `docs/api/c3po.DataAccessor.md`. Inherited methods are only listed on the base class's page, so follow the `bases:` shown after each class name. For an ICoCo-compliant code, `physicsDrivers/ICOCODriver` or a code-specific driver may already exist.
- **`DataManager`** holds the coupled data (fields, scalars). **`Exchanger`** moves data between drivers and data managers, through an **exchange method** (direct matching, shared remapping via MEDCoupling).
- A **`Coupler`** is itself a `PhysicsDriver`, so couplers can be nested. The algorithms are in `c3po.couplers`.
- MPI variants (`c3po.mpi`) mirror the sequential classes: collaborative mode (each process runs its share) and master/workers mode.

## How to answer

1. Start from the closest example, then check every class and method in `docs/api/`. Grep (`grep -rn "setDampingFactor" docs/api`). Don't invent methods or argument orders.
2. To choose an algorithm, read the coupler docstrings (convergence criterion, default tolerance, maximum iterations and damping are stated there), then the comparison in `examples/plaques_coupling/`.
3. To integrate a new code, read `docs/code_integration.md`, then the ICoCo method semantics in the **`icoco`** skill.
4. Cite the page or example path.

## Related skills

- **`icoco`:** the ICoCo norm.
- **`salome-medcoupling`:** fields and remapping.
- **`scivianna`:** live visualization of coupled results.
- **`tripoli5`, `thermal-hydraulics`, `neutronics`:** coupled physics.
