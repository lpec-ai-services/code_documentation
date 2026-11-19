---
name: neutronics
description: Neutronics, reactor physics and PWR technology knowledge base (neutronique, physique des réacteurs), in three branches. PHYSICS: nuclear data and cross sections, Boltzmann/transport and diffusion equations, criticality and k_eff (six-factor formula, buckling, reflectors), neutron spectrum (slowing down, resonances, thermalization), delayed neutrons, point and space–time kinetics, reactivity feedback and coefficients, fast excursions, burnup, Xe/Sm poisoning, fuel cycle, reactor types, safety. SIMULATION METHODS: two-step schemes, homogenization and equivalence, multigroup and self-shielding, collision probabilities, SN, PN/SPN, diffusion, nodal, MOC, synthesis, Monte Carlo, perturbation/adjoint/GPT, depletion and kinetics solvers. TECHNOLOGY: how a PWR is built and operated (French fleet and EPR: primary and secondary circuits, pressurizer, steam generators, vessel and internals, core and fuel, control rods, safety and auxiliary systems RIS/RRA/ASG/EAS, turbine-generator). Use for conceptual, theoretical, methodological or engineering questions independent of a specific code. For a code's input syntax use the code's own skill (tripoli4, tripoli5…).
---

# Neutronics: physics, simulation methods and reactor technology

This skill has three branches. First decide which one the question belongs to:

| The question is about… | Branch | Open |
|---|---|---|
| **What happens and why.** Phenomena, governing equations, physical quantities: cross sections, flux, k_eff, buckling, spectrum, reactivity and feedback, kinetics, depletion, poisoning, safety principles | **Physics** | `physics.md` |
| **How it is computed.** Discretizations, solvers, homogenization, Monte Carlo, perturbation methods, calculation schemes, codes and their approximations | **Methods** | `methods.md` |
| **How a reactor is built and operated.** PWR components, circuits, systems, fuel and core management, French plant series | **Technology** | `technology.md` |

Many questions need two branches. "Why does a Monte Carlo k_eff converge slowly in a large PWR?" needs physics (dominance ratio, loosely coupled core) and then methods (power iteration). "How is boron used to control reactivity?" needs physics (reactivity effect) and then technology (RCV/REA systems, primary chemistry).

## Files

- `physics.md`, `methods.md`, `technology.md`: topic → source → printed page.
- `equations.md`: key equations in LaTeX, transcribed from the source pages (§P physics, §M methods). **Use this for equations.** The extracted text garbles or fragments formulas.
- `sources/<document>/`: full text of each source, one Markdown file per chapter or group of sections. Each has a `TOC.md` (section → file → printed page) and `_meta.json`.

## Sources

| Key | Folder | Document | Language |
|---|---|---|---|
| **M** | `sources/cea-methodes-neutronique/` | *La neutronique — Les méthodes de la neutronique*, CEA DEN monograph (2013), pp. 43–124 | French |
| **S** | `sources/stacey-reactor-physics-3e/` | W. M. Stacey, *Nuclear Reactor Physics*, 3rd revised ed., Wiley-VCH (2018): part 1, basic reactor physics (ch. 1–8); part 2, advanced reactor physics (ch. 9–16); appendices | English |
| **P** | `sources/marguet-technologie-rep-2019/` | S. Marguet, *La technologie des réacteurs à eau pressurisée*, EDF R&D (2019), 1161 pages | French |

**S** is the general reference textbook. **M** gives the CEA view of the methods and of CEA codes. **P** covers engineering and operation.

## How to answer

1. Pick the branch, then find the topic in its map. Otherwise grep `sources/` in the source's language: English for S (`buckling`, `xenon`, `perturbation`), French for M and P (`autoprotection`, `léthargie`, `pressuriseur`, `injection de sécurité`).
2. Read the source passage. In the extracted text, inline symbols may be wrong ("□" marks one that could not be decoded) and display equations are split across lines. Take formulas from `equations.md`, or say they are not transcribed and cite the page.
3. Cite the source and its **printed page** (`<!-- page N (PDF M) -->` markers give both), e.g. "(Stacey 2018, §6.2, p. 213)" or "(CEA, *Les méthodes de la neutronique*, p. 83)".
4. Answer in the user's language, keeping standard notation (ψ angular flux, φ scalar flux, Σ macroscopic and σ microscopic cross sections, N_k concentrations). For French plant systems, keep the French acronym and give the English name.
5. Point to related skills:
   - **`tripoli4` / `tripoli5`:** Monte Carlo practice.
   - **`thermal-hydraulics`:** accident thermal-hydraulics.
   - **`valjean`:** comparing calculations.

## Adding a document

Convert it into `sources/<short-name>/` with `tools/pdf2md.py`. Books without bookmarks use `--chapter-sizes/--section-sizes/--subsection-sizes`, `--header-y` and `--printed-pages`; see `sync_neutronics` in `sync.sh`. Then add it to the Sources table, map its topics in the right branch, and add its key equations to `equations.md`.
