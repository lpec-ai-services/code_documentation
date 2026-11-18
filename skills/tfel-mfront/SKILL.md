---
name: tfel-mfront
description: TFEL/MFront (CEA/EDF) — code generator for material knowledge (material properties, mechanical behaviours, point-wise models) and its tools MTest, mfront-query, mfm, Python bindings, TFEL/Math and TFEL/Material. Use for any question about writing .mfront files (DSLs Implicit, Default, RungeKutta, IsotropicMisesCreep…, keywords, bricks such as StandardElastoViscoPlasticity), implicit integration and consistent tangent operators, finite strain, single crystals, homogenization, testing with MTest/.mtest, or using MFront behaviours in Cast3M, code_aster, Abaqus, ANSYS, CalculiX, ZeBuLoN, Cyrano, AMITEX or via MGIS. Also covers the constitutive-law theory behind them (plasticity, viscoplasticity, damage, hyperelasticity).
---

# TFEL/MFront documentation (v5.2.0)

The official documentation is in `docs/`: 266 pages, kept as Markdown in the TFEL repository, with the **equations in exact LaTeX**. Paths are relative to this file's directory.

- `docs/INDEX.md` lists every page with its title and headings. **Start here.**
- `docs/documentations.md` is the official guided tour, with recommended reading by topic and difficulty.
- `docs/*-keywords.md` is the **reference for each DSL's keywords** (`Implicit-keywords.md`, `Default-keywords.md`, `RungeKutta-keywords.md`, `MaterialProperty-keywords.md`, `Model-keywords.md`, `MTest-keywords.md`…).
- `docs/release-notes/` has what changed in each version. Check it when a keyword or feature seems missing.
- `examples/behaviours/<family>/*.mfront` (and `*.mtest`) holds the **gallery implementations**, kept up to date with the latest MFront. The docs link to them as `gallery/<family>/X.mfront`.
- `docs/_meta.json` records the source commit and version.

Pages start with a block of `\newcommand` LaTeX macros (`\tenseur`, `\tsigma`, `\tepsilonel`, `\bts`/`\mts`/`\ets` for values at $t$, $t+\theta\Delta t$ and $t+\Delta t$, …). Read them before interpreting the equations.

## Physics or methods?

| The question is about… | Open |
|---|---|
| **The material model.** Elasticity, yield criteria, hardening, viscoplastic flow, damage, hyperelasticity, finite-strain kinematics, crystal plasticity, homogenization schemes | `physics.md` |
| **Implementing, integrating, testing or using it.** DSLs and keywords, implicit scheme, Jacobian, tangent operator, bricks, solver interfaces, MTest, Python, compilation | `methods.md` |

Most gallery pages cover both: the behaviour's equations first, then its implicit discretization and the `.mfront` code.

## How to answer

1. **To write a new behaviour**, find the closest gallery case (`docs/gallery.md`, `examples/behaviours/`). Check whether a brick does the job (`StandardElastoViscoPlasticityBrick.md` often avoids hand-writing the implicit system). Then check every keyword in the DSL's `*-keywords.md`.
2. **Never invent keywords, options or method names.** Grep for them: `grep -rn "@IntegrationVariable" docs/`. If a keyword is absent, say so and check `release-notes/`.
3. **For a solver integration**, read that solver's interface page (`castem.md`, `aster.md`, `abaqus.md`, `ansys.md`, `calculix.md`, `zmat.md`, `cyrano.md`, `amitex.md`, `generic-behaviours-interface.md` for MGIS). Hypotheses, finite-strain strategies and tangent conventions differ between solvers.
4. **To test a behaviour**, write an `.mtest` file (`mtest.md`, `MTest-keywords.md`) or use the Python API (`mtest-python.md`).
5. Cite the page (file name) and, for gallery code, the `.mfront` path.

## Related skills

- **`thermal-hydraulics`, `neutronics`:** coupled problems.
- **`valjean`:** statistical comparison of results.
- **Fuel performance** (Cyrano, PLEIADES): see `cyrano.md` and `benchmark.md` here.
