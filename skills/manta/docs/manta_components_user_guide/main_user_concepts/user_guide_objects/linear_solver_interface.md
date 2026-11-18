<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/main_user_concepts/user_guide_objects/linear_solver_interface.html -->

# Linear solver interface

Users of MANTA can interact with the Linear Solver backend
(currently only [PETSc](https://petsc.org/)) through the interface presented
in this page.

## [Parameters that can be set in scripts (.py, .cpp)](#id3)

MANTA words cover the usual choices only. Anything else can be given as a raw
[PETSc](https://petsc.org/) keyword (e.g. `fgmres` for the method, `gamg` or `hypre` for the
preconditioner), which is then used as is.

### [`method`](#id4)

| MANTA word | meaning | PETSc keyword |
| --- | --- | --- |
| `direct` | a single, exact solve (default) | `KSPPREONLY` with `PCLU` |
| `gmres` | GMRES, a general-purpose method for non-symmetric systems | `KSPGMRES` |
| `cg` | the conjugate gradient method, for symmetric positive-definite systems | `KSPCG` |

PETSc's own raw keyword for `direct` (`preonly`) is recognized just the same: it behaves
identically to MANTA's `direct` word in every respect (including the defaults it gets).

### [`preconditioner`](#id5)

A preconditioner is used by iterative methods. `direct` is a single factorization, and has no use for one.

| MANTA word | meaning | PETSc keyword |
| --- | --- | --- |
| `none` | no preconditioning | `PCNONE` |
| `jacobi` | diagonal scaling | `PCJACOBI` |
| `ilu` | incomplete LU factorization. **Sequential only**: it raises an error when the computation runs on several processes (PETSc's `PCILU` has no parallel implementation). In parallel, use the PETSc keyword `bjacobi`. | `PCILU` |
| `amg` | algebraic multigrid. | `PCGAMG` |

Left unset, an iterative method uses PETSc's own default preconditioner: an ILU in serial,
a block-Jacobi (an ILU on each process's block) in parallel.

### [`factorizationBackend`](#id6)

This parameter sets the library
performing the factorization, e.g. `"mumps"` or
`"superlu_dist"` (currently available through PETSc). Left unset, MANTA
keeps its own default backend for that solve.
It is meaningful for `direct`, for `ilu`, and for any preconditioner that is a factorization.

### [`methodForConstraint`](#id7)

**If** your system still contain non-eliminated constraints,
two mode of resolution can be chosen.

| word | meaning |
| --- | --- |
| `monolithic` | the whole augmented system is solved at once. |
| `schurComplement` | (**default**) solves the nested system with a schur's complement. The resolution of the Schur complement is not configurable through this interface. (use petscrc) |

## [Using a petscrc file to set more options](#id8)

PETSc generic commands can be called through command line arguments or in
a petscrc file in the working repository
to setup further options. User options written in a script override
the command line and petscrc options.
More precisions about this mode of usage are available
in .:ref:this <choosing_a_linear_solver_and_preconditioner> page.

## [Example of usage in pyManta](#id9)

Using MANTA's generic words:

```python
linear_solver_options = {'direct': {'factorizationBackend': 'mumps'},
                         'methodForConstraint': 'monolithic'}
```

Falling back to a raw PETSc keyword (here for `method`, since MANTA has no
generic word for `fgmres`), with the declaration of a specific preconditioner:

```python
linear_solver_options = {'fgmres': {'preconditioner': 'ilu'}}
```

Resolving the constraints with a Schur complement, with a direct
solver for the block of the main unknowns:

```python
linear_solver_options = {'direct': {},
                         'methodForConstraint': 'schurComplement'}
```

## [Example of usage in components](#id10)

In the components, users have to instantiate a `LinearSystem::UserOptions` struct.
It contains the parameters of the method cited above (`methodForConstraint`
is set through `LinearSystem::methodForConstraint()`):

```c++
  struct UserOptions {
    std::string method;
    std::string preconditioner;
    std::string factorizationBackend;
  };
```

A field of `UserOptions` left default-constructed (`{}`) keeps
whatever MANTA would have picked on its own for that field.

Here are examples of usage of this struct and the call to `setLinearSolverOptions()`.

Setting an iterative method, with one of MANTA's own preconditioner words:

```c++
    LinearSystem::UserOptions options{"cg", "jacobi", ""};
```

Falling back to a raw PETSc keyword (here for `method`: `preonly` is PETSc's
own name for what MANTA calls `direct`):

```c++
    // "preonly" is PETSc's own raw name for what manta calls 'direct'.
    // Preconditioner is left unset
    LinearSystem::UserOptions options{"preonly", "", MATSOLVERMUMPS};
```

Either way, the resulting `UserOptions` is applied with:

```c++
    if (!feSystem.setLinearSolverOptions(ctx, *mainKSPOptions)) {
      std::cerr << ctx.getErrorMessage() << std::endl;
      return ExitStatus::failure;
    }
```

Setting the main options and the method for constraints, on
a case resolved through the schur path (gathered constraints, not eliminated):

```c++
  LinearSystem::UserOptions mainOptions{"direct", "", "mumps"};    // solver of the main unknowns (block A)
  if (!feSystem.setLinearSolverOptions(ctx, mainOptions)) {
    Message::error(ctx.getErrorMessage());
  }
  if (!feSystem.methodForConstraint(ctx, "schurComplement")) {
    Message::error(ctx.getErrorMessage());
  }
```

`setLinearSolverOptions()` overrides the method/preconditioner solving the main system of
equations, and takes effect on the next solve. Defaults value for every case are detailed in the
[LinearSystem blueprint](../../../developer_guide/blueprints/linear_system_blueprint.md#blueprint-linear-system-solving).

## [List of examples and tests](#id11)

- `src/components/modeling/tests/e2e/nr/implicit/cantilever_plasticity`
- `src/components/modeling/tests/e2e/nr/implicit/plasticube2`
- `examples/elasticity/2D_plate_with_hole/frontend/plate_with_hole.py`
- `examples/non_linear_behaviour/plasticity/rate_dependent_plasticity/test3D.py`
- `examples/numerical_analysis/norms_calculation/test1.py`
