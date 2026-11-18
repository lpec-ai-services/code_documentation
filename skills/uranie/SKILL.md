---
name: uranie
description: Uranie (CEA) — ROOT-based platform for uncertainty quantification, sensitivity analysis, surrogate modelling, optimisation and calibration, used from Python (PyROOT / PyURANIE). Use for any question about Uranie or its modules — DataServer (TDataServer, TAttribute, TStochasticAttribute, statistics, quantiles, PCA, uncertainty plots), Sampler (LHS, constrained LHS, QMC, correlations and copulas, random fields, OAT, vector quantification), Launcher and Relauncher (TPythonEval, TCodeEval, TSequentialRun, TThreadedRun, TMpiRun, TLauncher2), Modeler (linear regression, polynomial chaos/Nisp, kriging), Sensitivity (Sobol), Optimizer and Reoptimizer (NLopt, Vizir), Metamodel optimisation (EGO), Calibration (minimisation, linear Bayesian, ABC, MCMC, CIRCE), Uncertainty modeler (EDF tests) — and its Python macros.
---

# Uranie user manual (Python)

The *UserManual Python* of Uranie (CEA DES, Uranie team; build of 13 Feb 2026, 489 pages) is in `docs/`, one Markdown file per chapter or group of sections. Paths are relative to this file's directory.

- `docs/TOC.md` has the full outline, every section → file → printed page. **Start here.**
- **Code blocks are fenced as Python with their indentation rebuilt**, so the macros can be copied and run. Code split across a page break appears as two consecutive blocks.
- Inline mathematics extracts as Unicode (𝑥, 𝜎…), but **sub/superscripts are flattened** ("𝑥2\n1" for $x_1^2$). Read formulas with care, and cite the page.
- `<!-- page N (PDF M) -->` markers give the printed page.

**What this manual is not:** it is the *user* manual (how to use the classes). The theory behind the methods is in Uranie's separate *methodology* manual, which is not included yet. In this edition, the Modeler, Sensitivity and Optimizer chapters are short and partly unfinished (one says "This is a test"). For those modules, rely on the use-case macros.

## Where to look

| Module / topic | Manual chapter | Worked macros (use-cases chapter) |
|---|---|---|
| **Getting started**: ROOT environment, PyROOT, PyURANIE, environment variables, Python FAQ | `01-overview-uranie-in-a-nutshell.md` | `21-use-cases-in-python--introduction.md` (Macros Python HowTo) |
| **DataServer**: TAttribute/TStochasticAttribute (laws), data import/export, merging, selection, normalisation, ranking, statistics, quantiles, correlation; plots (histogram, boxplot, CDF/CCDF, Tufte, pairs, cobweb, QQ/PP); PCA | `02`–`08-dataserver--*.md` | `22`, `23` (DataServer macros) |
| **Sampler**: stochastic methods (SRS, LHS, constrained LHS), correlations and copulas, QMC, random fields, OAT designs, vectorial quantification | `09-sampler--introduction.md`, `10-sampler--oat-design.md` | `24`, `25` |
| **Launcher**: external code, input/output files, remote launching to clusters | `11-the-launcher-module.md` | `26` (Launcher macros) |
| **Sensitivity**: Sobol indices (also Morris, Johnson in macros) | `13-the-sensitivity-module.md` | `26`–`29` |
| **Modeler**: linear regression, polynomial chaos (Nisp), kriging | `12-the-modeler-module.md` | `30`, `31` |
| **Relauncher**: TEval (TPythonEval, TCIntEval/TCJitEval, TCodeEval, composition), TRun (TSequentialRun, TThreadedRun, TMpiRun), TMaster, TLauncher2 | `15-the-relauncher-module.md` | `32`–`34` |
| **Optimizer / Reoptimizer**: problem definition, objectives and constraints, local solvers (NLopt), global solvers (Vizir, TVizir2, TVizirIsland), hollow-bar example | `14-the-optimizer-module.md`, `16-the-reoptimizer-module.md` | `35`, `36` |
| **Metamodel optimisation**: Efficient Global Optimization (EGO) | `17-the-metamodel-optimization-module.md` | `37` |
| **Calibration**: distances and likelihoods, TMinimisation, analytical linear Bayesian, ABC, MCMC, CIRCE | `18-calibration--introduction.md`, `19-calibration--*.md` | `38`–`40` |
| **Uncertainty modeler**: EDF tests | `20-the-uncertainty-modeler-module.md` | `41` |
| References | `42-bibliography.md` | |

## How to answer

1. **For code**, find the closest macro (grep for the class, e.g. `grep -rln "TSobol" docs/`) and adapt it. Uranie classes live under `ROOT.URANIE.<Module>` or `from URANIE import <Module>`, and every call must match the manual: don't invent methods or option strings.
2. Check the module chapter for the options of the class used. Options are keyword strings passed as text, e.g. `generateSample("QmcSobol")` or `computeIndexes("graph")`. Use the exact spelling from the manual.
3. **For theory** (why a method works, assumptions, estimators), use the manual's explanations and cite the page. Say that the full theory is in the Uranie methodology manual.
4. Cite file and printed page.

## Related skills

- **`valjean`:** statistical comparison of code results.
- **`tripoli4`, `tripoli5`, `thermal-hydraulics`:** the codes and physics being studied with Uranie.
