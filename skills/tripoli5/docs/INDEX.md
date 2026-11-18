# Index of pages

Each entry: file — title, then its section headings.


## api

- `api/agora-api.md` — **The AGORA API** (18 kB)
- `api/core-api.md` — **The CORE API** (7 kB)
  - Parameters
- `api/delos-api.md` — **The DELOS API** (44 kB)
- `api/geoplotter-api.md` — **The GeoPlotter API** (13 kB)
  - Parameters · Returns · Examples · Parameters · Returns · Examples · Attributes · Parameters · Returns · Examples
- `api/patmos-api.md` — **The PATMOS API** (61 kB)
  - tripoli5.utils module · tripoli5.geometry module · tripoli5.materials module · tripoli5.score module · tripoli5.source module · tripoli5.simulation module · Parameters · Returns · Parameters · Returns · Parameters · Returns … (+7)
- `api/python-api.md` — **The Python API** (1 kB)

## examples

- `examples/criticality/Jezebel.md` — **Jezebel Plutonium Sphere** (12 kB)
  - Material Definition · Geometry Definition · Physics Configuration · Scores · Configure and Run Criticality Calculation
- `examples/criticality/bigten-agora.md` — **Big Ten with AGORA Geometry** (17 kB)
  - Material Definition · Geometry Definition · Physics Configuration · Scores · Configure and Run Criticality Calculation
- `examples/criticality/pin_cell.md` — **A pin cell from the Mosteller suite** (25 kB)
  - Imports · Geometry · Nuclear Data and Material Compositions · Score · Simulation setup · Launching the code · Inspecting results · keff · Delta-Tracking
- `examples/criticality/sphere_u235.md` — **A single isotope bare sphere** (15 kB)
  - Imports · User inputs · Geometry · Nuclear Data and Material Compositions · Score · Simulation setup · Launching the code · Printing out results into files · keff results
- `examples/features/agora_geometry.md` — **Defining a Geometry Model with AGORA** (27 kB)
  - Defining Surfaces · Example: Sphere · Defining Shapes · Defining half-spaces · Combining half-spaces using Boolean Operators · Defining a Shape from half-spaces · Defining an infinite Shape · Shape examples · Defining Volumes · Build a Volume · Defining Universes · Defining Composite Volumes … (+8)
- `examples/features/materials_compositions.md` — **Overview of Material compositions and physics** (10 kB)
  - Imports · Catalog · Defining Mixtures · Using concentrations · Using mass fractions · Using atom fractions and use of natural abundances · Configure and Build a NeutronMedia
- `examples/features/mixtures.md` — **Mixtures** (24 kB)
  - Imports · Mixture Builder · Example: Create a fuel mixture · Input methods for nuclides amounts · Natural Abundances · Specifying Temperature and Density fields
- `examples/features/neutron_media.md` — **Neutron Media** (77 kB)
  - Prerequisites: imports, Catalog and Mixtures · Imports · Catalog · Mixtures · Neutron Media with all default options · Lower energy threshold · Unresolved Resonance Range treatment · Doppler Broadening of freegas cross section · GPU processing of the SIGMA1 algorithm · Epithermal broadening of the elastic scattering kernel · Default options · Turning off the Epithermal broadening treatment … (+6)
- `examples/features/new_scores.md` — **Scores** (28 kB)
  - Types of Scores · Setting up a Configuration · Score Declaration · Building the elements required to build a Detector or a DistributionDetector · Building the detectors · Configure and Run Simulation · Score Results
- `examples/features/physical_quantities.md` — **Physical quantities in TRIPOLI-5** (2 kB)
  - TRIPOLI-5 literals in the Python API
- `examples/features/plotter.md` — **Visualising a geometry** (13 kB)
  - Prerequisites: Imports and geometry definition · Creating the plotter engine · Defining a frame · Plotting the geometry: TL;DR · Plotting the geometry: full options · Saving to a file · Changing the resolution · Passing a matplotlib Axes · Changing colors · Interrogating the geometry
- `examples/features/score.md` — **Scores** (28 kB)
  - Types of Scores · Setting up a Configuration · Score Declaration · Flux Spectrum Scores · Reaction Rate Scores · Kappa Fission Scores · Score Manager · Configure and Run Simulation · Score Results · KStep Results · Volume-based Score Results · MT Reaction Rate Score Results … (+1)
- `examples/features/simulation.md` — **Simulation** (40 kB)
  - The system · Mixtures · Geometry · Media · Scores · Source · Simulation parameters · Advanced Simulation parameters · The simulation builder · Particle tracking · Surface tracking and delta tracking · Collision Sampling Algorithm … (+2)
- `examples/features/source.md` — **Source** (11 kB)
  - Imports · Factorized Source · Spatial distributions · Energy distributions · Angular distributions · Create a Factorized Source · Point Isotropic Source · Create a Point Isotropic Source
- `examples/geometries/candu.md` — **A CANDU assembly** (4 kB)
- `examples/geometries/hexagonal_lattice_example.md` — **A reactor core example with hexagonal lattices:** (15 kB)
  - Cells definition · Tie tube · Fuel element · Reactor hexagonal lattice · Placing the fuel matrix in its reflector
- `examples/geometries/pwr_assembly.md` — **PWR fuel assembly** (4 kB)
- `examples/geometries/superphenix_assembly.md` — **Superphénix assembly** (4 kB)
- `examples/index.md` — **Examples** (1 kB)
  - Features · Geometries · Criticality

## (root)

- `index.md` — **TRIPOLI-5 ® Documentation** (1 kB)
  - Examples · Validation · Theory · Python API · Release notes

## release

- `release/changelog.md` — **Changelog** (3 kB)
  - 0.3.0 · 0.2.0 · Main features · 0.1.0 · Main features
- `release/known_bugs.md` — **Known bugs** (2 kB)
  - 0.3.0 · 0.2.0 · 0.1.0

## theory

- `theory/collision_physics.md` — **Collision physics** (1 kB)
- `theory/collision_physics/svt.md` — **The SVT algorithm** (2 kB)
- `theory/collision_physics/tsl.md` — **Thermal scattering laws** (12 kB)
  - Introduction · Inelastic scattering reaction · Evaluation of the cross section · Sampling of the outgoing energy · Sampling of the outgoing cosine · Incoherent elastic reaction · Evaluation of the cross section · Sampling of the outgoing cosine · Coherent elastic reaction · Evaluation of the cross section · Sampling of the outgoing cosine · Integration of thermal scattering laws in TRIPOLI-5
- `theory/geometry.md` — **Geometry** (1 kB)
- `theory/index.md` — **Theoretical aspects of the TRIPOLI-5 ® Monte Carlo code** (1 kB)
- `theory/introduction.md` — **Introduction** (1 kB)
- `theory/scores.md` — **Scores** (1 kB)
- `theory/scores/computing_moments.md` — **Computing central statistical moments** (4 kB)
  - Definition of central statistical moments · Efficient numerical computation of statistical moments · First raw moment: average · Second central moment: the sample variance · Third central moment · Fourth central moment

## validation

- `validation/criticality/beavrs/beavrs.md` — **The BEAVRS benchmark** (14 kB)
- `validation/criticality/stacy_agora.md` — **The modified STACY facility using AGORA geometry** (22 kB)
  - Materials definition · Geometry definition · Plot geometry · Source definition · Sample Keff at different water heights
- `validation/index.md` — **Validation suite** (1 kB)
  - Criticality
