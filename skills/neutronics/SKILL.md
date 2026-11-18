---
name: neutronics
description: Neutronics / reactor physics knowledge base (neutronique), split into PHYSICS (neutron transport/Boltzmann equation, Bateman depletion equations, criticality and k_eff, reactivity, delayed neutrons and kinetics, self-shielding, fission-product poisoning Xe/Sm) and SIMULATION METHODS (deterministic solvers — multigroup, self-shielding models, SN, PN/SPN, diffusion, finite differences, nodal, finite elements, method of characteristics —, Monte Carlo transport, power iteration and convergence, variance reduction, depletion solvers, kinetics solvers, two-step calculation schemes). Use for conceptual, theoretical or methodological questions independent of a specific code. For a code's input syntax use the code's own skill (tripoli4, tripoli5, valjean).
---

# Neutronics: physics and simulation methods

This skill has two branches. First decide which one the question belongs to:

| The question is about… | Branch | Open |
|---|---|---|
| **What happens and why.** Phenomena, governing equations, physical quantities: flux, reaction rates, k_eff, reactivity, delayed neutrons, depletion, poisoning, self-shielding as a phenomenon | **Physics** | `physics.md` |
| **How it is computed.** Discretizations, solvers, Monte Carlo algorithms, convergence and statistics, calculation schemes, codes and their approximations | **Methods** | `methods.md` |

Many questions need both, e.g. "why does a Monte Carlo k_eff converge slowly in a large PWR?". Start with the physics (dominance ratio, decoupled core), then go to the method (power iteration, inter-cycle correlation).

## Files

- `physics.md` / `methods.md`: topic → source file → printed page, plus a summary of what each source says.
- `equations.md`: the key equations in LaTeX, transcribed from the source pages and tagged physics or methods. **Use this for equations.** The extracted source text garbles mathematical symbols.
- `sources/<document>/`: full text of each source, one Markdown file per chapter. Each has a `TOC.md` (sections → file → page) and `_meta.json`.

## Sources

| Folder | Document | Language |
|---|---|---|
| `sources/cea-methodes-neutronique/` | *La neutronique — Les méthodes de la neutronique*, CEA DEN monograph (2013), pp. 43–124 | French |

## How to answer

1. Pick the branch, then find the topic in its map. Grep `sources/` for French terms (e.g. `autoprotection`, `léthargie`, `itération de la puissance`, `neutrons retardés`).
2. Read the source passage. In the source text, inline symbols are unreliable: ")" may stand for r, "/" for E′, "?" for φ, and "□" marks a symbol that could not be decoded. Take any formula from `equations.md`, or say it is not transcribed and cite the page.
3. Cite the document and its **printed page** (`<!-- page N (PDF M) -->` markers give both), e.g. "(CEA, *Les méthodes de la neutronique*, p. 83)".
4. Answer in the user's language, keeping standard notation (ψ angular flux, φ scalar flux, Σ macroscopic and σ microscopic cross sections, N_k concentrations).
5. Point to code skills when relevant. Monte Carlo practice is in `tripoli4` / `tripoli5`. Comparing calculations and statistical tests is in `valjean`.

## Adding a document

Convert it into `sources/<short-name>/` with `tools/pdf2md.py` (see `sync.sh`, `sync_neutronics`). Add it to the Sources table. Add its topics to `physics.md` and/or `methods.md`, and its key equations to `equations.md`.
