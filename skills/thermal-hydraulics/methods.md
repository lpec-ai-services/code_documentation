# Methods branch: how it is computed

**B** = `sources/th-water-cooled-reactors-2017/` (folder `NN-…` = chapter NN; each folder has a `TOC.md`). **F** = `sources/iaea-trs-498-fast-reactors/`. Pages are printed pages. Equations: `equations.md` (§M…).

## Equation systems and averaging (chapter B 05)

| Topic | Where | Notes |
|---|---|---|
| Local instantaneous balance equations (mass, momentum, energy, entropy) | B 05, pp. 174–180 | §M1 |
| Single-phase modelling approaches: RANS, LES / scale-resolving, DNS; locality and universality | B 05, pp. 180–184 | |
| Time-averaged single-phase equations and their closure | B 05, pp. 184–188 | |
| 1-D single-phase equations; predictive capabilities | B 05, pp. 188–196 | |
| Two-phase modelling approaches: time/space/phase averaging; **CMFD** | B 05, pp. 196–203 | |
| Time-averaged (3-D) two-fluid equations | B 05, pp. 203–208 | |
| Space-phase averaging; **1-D two-fluid 6-equation model** | B 05, pp. 208–222 | §M2 |
| How system codes (CATHARE, RELAP5, TRACE) write the 1-D two-fluid equations | B 05, pp. 222–223 | §M2 |
| **Model hierarchy**: 3-equation HEM, drift flux (3/4/5 equations), 6-equation | B 05, pp. 223–231 (table 5.6, p. 225) | §M3, §M4 |
| Characteristic velocities and **hyperbolicity** (well-posedness) | B 05, pp. 231 ff. | |

## Closure laws (constitutive equations, chapter B 09)

| Topic | Where | Notes |
|---|---|---|
| Two-fluid equations and what needs closing | B 09, pp. 551–554 | |
| **Flow-regime maps**: vertical, horizontal, CATHARE 2 and TRACE maps, limits | B 09, pp. 554–564 | |
| **Interfacial heat and mass transfer** (RELAP5 IHTC table) | B 09, pp. 564–570 | |
| **Interfacial drag**: drift-flux method, drag-coefficient method | B 09, pp. 570–577 | |
| **Wall heat transfer**: convection, boiling, condensing regions | B 09, pp. 577–581 | |
| **Wall friction**: single and two-phase | B 09, pp. 581–585 | |
| Validation of constitutive equations | B 09, pp. 585–587 | |

## Special models and components in codes (chapter B 10)

| Topic | Where | Notes |
|---|---|---|
| Critical-flow models in system codes | B 10, p. 601 | Physics: §P5 |
| CCFL, entrainment, reflood, break-flow models | B 10, pp. 602–618 | |
| Component models: pumps, separators/dryers, accumulators, valves | B 10, pp. 619–634 | |

## System thermal-hydraulic codes (chapter B 11)

| Topic | Where | Notes |
|---|---|---|
| Requirements and simulation domain; best-estimate vs safety vs industrial codes; first BE codes | B 11, pp. 641–649 | |
| **Nodalization**: 1-D modules, Tee junctions, 0-D modules, critical flow, singular losses, CCFL, separators, pumps, turbines, ECC, accumulators, valves, breaks, spray; importance of nodalization | B 11, pp. 649–660 | |
| **Numerical solution methods** | B 11, pp. 659–666 | |
| Coupling with containment codes; with component and subchannel codes | B 11, pp. 666–671 | |
| Predicting break flow and choked flow; horizontal two-phase flow and stratification | B 11, pp. 671–698 | |
| Using flow-regime maps; developing and validating closure relations; predicting CCFL | B 11, pp. 698–704 | |
| Upscaling; **predictive capabilities of system codes** | B 11, pp. 704–714 | |
| Drift flux vs two-fluid vs TIA in system codes; **three-field models** | B 11, pp. 714–723 | |
| History and perspectives of system codes; user effect; K-factors; precision targets | B 02, pp. 47–78 | |

## CFD (chapter B 12)

| Topic | Where | Notes |
|---|---|---|
| CFD for nuclear TH: analysis procedure, physical models, characteristics | B 12, pp. 734–741 | |
| CFD definitions, **methods** (turbulence models, two-phase CFD) | B 12, pp. 742–763 | |
| Applications and examples (mixing, PTS, boron dilution, thermal fatigue…) | B 12, pp. 764–805 | |
| CFD coupling, **validation**, scaling, recommendations | B 12, pp. 806–818 | |

## V&V, scaling, uncertainty, BEPU (chapters B 13, B 14)

| Topic | Where | Notes |
|---|---|---|
| Verification and validation of system codes | B 13, pp. 834–848 | |
| **Scaling**: concepts, integral tests, separate-effect tests | B 13, pp. 848–863 | |
| **Uncertainty methods**: common methods (input propagation with Wilks, output accuracy extrapolation…), international comparisons (BEMUSE etc.), licensing use | B 13, pp. 864–898 | |
| **BEPU**: licensing framework, history, requirements, elements, roadmap | B 14, pp. 908–931+ | |
| Analysis-tool adequacy, analysis envelope | B 04, pp. 144–167 | |

## Safety-analysis applications (chapter B 15)

| Topic | Where | Notes |
|---|---|---|
| Cross-link between accident scenarios and phenomena (procedure) | B 15, pp. 975–979 | |
| Application of system codes by scenario class | B 15, pp. 979–1035 | |

## Fast reactors (F)

| Topic | Where | Notes |
|---|---|---|
| Reactor modelling scales: **system TH**, **subchannel codes**, engineering CFD (core, pool), **high-resolution CFD** (LES, DNS), use in safety review | F §5, pp. 24–34 | |
| **Multiscale and multiphysics**: domain decomposition vs overlap, internal vs external coupling, explicit vs implicit temporal coupling, V&V of coupled codes, code platforms under development | F §7, pp. 40–47 | |
| **VVUQ**: verification and validation, uncertainty and sensitivity analysis, lessons from international benchmarks | F §8, pp. 48–55 | |
| Experimental methods and instrumentation for liquid metals (temperature, velocity, particles) | F §4.1, §4.4, pp. 15–24 | |
| Modern TH tools in licensing | F §10, pp. 64–68 | |
