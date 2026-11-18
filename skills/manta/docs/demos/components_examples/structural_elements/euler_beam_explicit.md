<!-- source: https://manta-project.gitlab.io/manta/demos/components_examples/structural_elements/euler_beam_explicit.html -->

# Euler beam in explicit mechanics

Note

The following files are required to run the tutorial:

- [`main.cpp`](../../../_downloads/95044b6a1132cdb48f608828f4887d58/main.cpp):
- [`input_data.json`](../../../_downloads/bdfdd3319955bdadf203b9532603fcd0/input_data.json):
- [`CMakeLists.txt`](../../../_downloads/d61badd37c0091e8fd6dc90f90d75b18/CMakeLists.txt):

## Description

A cantilever beam is loaded with a distributed bending load, and the beam
vibrations are studied (no initial displacement / velocity).
Its behavior is supposed linear elastic and the small perturbation hypothesis holds.

To model this problem, Euler beam hypotheses are assumed, and an explicit
integration scheme is chosen.

![figure](https://manta-project.gitlab.io/manta/_images/clamped_free_2d_bending_explicit.svg)

Fig. 6 Clamped beam under bending load

**Keywords:** elastic, linear, structure, dynamic, Euler beam, explicit integration scheme.

**References:**

- Analytical solution: Test SDLL135 of **code_aster** [[Ast](../../../references/references.md#id49)], and
  [MANTA verifications tests](../../../verification_tests/manta_components_verification_tests/solid_mechanics/fem_explicit_linear/beams/clamped_free.md#cantilever-endforce-beam-verification-tests-explicit).
- Numerical solution: [MANTA verifications tests](../../../verification_tests/manta_components_verification_tests/solid_mechanics/fem_explicit_linear/beams/clamped_free.md#cantilever-endforce-beam-verification-tests-explicit).

The full test-file of this example is given just hereafter
but each significant step of this simple example
is explained in the next subsections.

Full test-file

```c++
#include <cmath>
#include "manta/components-parameters/json_data_reader.h"
#include "manta/components-core/linear_system/linear_system.h"
#include "manta/components-modeling/mechanics/beams/euler_beam_explicit_formulation.h"
#include "manta/components-modeling/mechanics/beams/euler_beam_distributed_load_formulation.h"
#include "manta/components-fem_tools/constraints/blocking_formulation.h"
#include "manta/components-executable_utilities/fatal_error.h"
#include "manta/components-modeling/time_integrators/central_difference.h"
#include "manta/components-modeling/physical_constants.h"
#include "manta/components-core/post_formulation.h"
#include "manta/components-io_vtk/writer.h"

using namespace manta;

/**
 * Main function that runs all the specific parametric studies
 */
int main(int argc, char **argv)
{
  // [manta fatal error]
  // Macro to disable warnings and error coming from the ignoring of functions
  // marked as nodiscard
  MANTA_FATAL_ERROR;
  // [manta fatal error]

  // [context creation]
  // Creation of the context
  Context ctx;
  // [context creation]

  // [json reading]
  // > Read the data from the JSON file
  const auto parameters = readJSONDataFile(ctx, "input_data.json");

  const Real E                           = get<Real>(*parameters, "YoungModulus");
  const Real nu                          = get<Real>(*parameters, "PoissonRatio");
  const Real h                           = get<Real>(*parameters, "thickness");
  const Real length                      = get<Real>(*parameters, "length");
  const Real rho                         = get<Real>(*parameters, "massDensity");
  const Vector<Real> principalAxisVector = get<Vector<Real>>(*parameters, "oyVector");

  // > Deduced geometric values
  Real b  = h;        // Dimension along the other axis. For this example, we choose a square cross section
  Real S  = b * h;    // Cross-section area
  Real Iy = (h / 12.) * (std::pow(b, 3));    // Second moment of area aroung principal axis
  Real Iz = (b / 12.) * (std::pow(h, 3));    // Second moment of area aroung secondary axis
  Real Jx = Iy + Iz;                         // Polar moment

  ColVector<3> oy_vector(principalAxisVector.data());    // Orientation vector
  // [json reading]

  init(argc, argv);
  {
    // [geometrical hypothesis]
    // > Geometrical hypothesis
    constexpr StructuralHypothesis hypothesis = StructuralHypothesis::tridimensional;
    constexpr Int dim                         = StructuralHypothesisTraits<hypothesis>::geoDim;
    constexpr Int numDofsTranslation          = 3;
    constexpr Int numDofsRotation             = 3;
    // [geometrical hypothesis]

    // [kinematic description]
    // > Lagrangian kinematic description
    constexpr KinematicDescription kinematicDescription = KinematicDescription::lagrangian;
    // [kinematic description]

    // [ressource manager creation]
    // > Define the Ressource Manager
    ResourcesManager rm(dim);
    // [ressource manager creation]

    // [mesh creation]
    // > Create a uniform mesh
    auto &mesh = rm.getMesh();
    mesh.generateGrid<1>("beam", {0.5 * length}, {length}, {20});

    // > Build meshSets
    MeshSet &beam  = mesh.getSet("beam");
    MeshSet &right = mesh.getSet("beam_x1");
    // [mesh creation]

    // [fields creation]
    // > Node field
    // displacement (translation and rotation)
    auto &Ut = rm.make<NodeField<>>(beam, "Ut", numDofsTranslation, 1);
    auto &Ur = rm.make<NodeField<>>(beam, "Ur", numDofsRotation, 1);
    // velocity (translation and rotation)
    auto &Vt = rm.make<NodeField<>>(beam, "Vt", numDofsTranslation, 1);
    auto &Vr = rm.make<NodeField<>>(beam, "Vr", numDofsRotation, 1);
    // acceleration (translation and rotation)
    auto &At = rm.make<NodeField<>>(beam, "At", numDofsTranslation, 1);
    auto &Ar = rm.make<NodeField<>>(beam, "Ar", numDofsRotation, 1);
    DofVar Atvar(numDofsTranslation, "At");
    DofVar Arvar(numDofsRotation, "Ar");
    // [fields creation]

    // [linear system]
    // > global linear system
    auto &feSystem = rm.make<DiagonalLinearSystem>("FESystem", mesh);
    // [linear system]

    // [euler beam formulation]
    // Euler Explicit Formulation
    auto &eulerForm = rm.make<EulerBeamExplicitFormulation<hypothesis, Real, Real, Real, kinematicDescription>>(
        beam,
        QuadId::seg4,
        QuadId::seg2,
        Atvar,
        Arvar,
        Ut,
        Ur,
        E,
        nu,
        rho,
        BeamProperties<hypothesis>{S, Iy, Iz, Jx, oy_vector},
        LumpingTranslationStrategy::bending,
        LumpingRotationStrategy<hypothesis>{0., 420. / 24., 0., 0., 0., 0., 5.});

    rm.assignFormulationToLinearSystem(eulerForm, feSystem);
    // [euler beam formulation]

    // [boundary condition]
    // Boundary conditions (clamped at the right node)
    auto &clampFormTran = rm.make<BlockingFormulation<true>>(Atvar, right, std::set{0, 1, 2});
    auto &clampFormRot  = rm.make<BlockingFormulation<true>>(Arvar, right, std::set{0, 1, 2});
    auto &clampCst      = rm.make<ConstraintSet>(feSystem, "clamp");

    rm.assignFormulationToLinearSystem(clampFormTran, clampCst);
    rm.assignFormulationToLinearSystem(clampFormRot, clampCst);
    // [boundary condition]

    // [distributed loads]
    // Imposing the distributed load force
    auto &eulerLoadForm = rm.make<EulerBeamDistributedLoadFormulation<hypothesis, Real>>(
        beam,
        QuadId::seg2,
        Atvar,
        Arvar,
        BeamProperties<hypothesis>{S, Iy, Iz, Jx, oy_vector},
        BeamDistributedLoads<hypothesis, Real>{0., -PhysicalConstants<UnitSystem::SI>::g * rho * S, 0., 0., 0., 0.},
        false);

    rm.assignFormulationToLinearSystem(eulerLoadForm, feSystem);
    // [distributed loads]

    // [time integrator]
    // Explicit time integrator
    CentralDifferenceTimeIntegrator timeIntegrator(feSystem, {{Atvar, {Ut, Vt, At}}, {Arvar, {Ur, Vr, Ar}}});
    // [time integrator]

    // [post formulations]
    // Declare post formulations to allow post-processing
    Vector<FieldBase *> postFields = {&Ut, &Vt, &At, &Ur, &Vr, &Ar};
    rm.make<PostFormulation>(postFields);
    // [post formulations]

    // [memory allocation]
    // > Manta initialisation
    rm.init(ctx);
    // [memory allocation]

    // -------------------------------------------------------------------------

    // [initial conditions]
    // > Initial value of the Node Field for all the nodes
    // Zero velocity such as we place ourselves at an extremum of displacement
    Vt.setValue(0.);
    Vr.setValue(0.);

    // Zero displacement -> Will be the value of an extremum
    Ut.setValue(0.);
    Ur.setValue(0.);
    // [initial conditions]

    // [declaration post-processing]
    // > set post-proc writer
    VtkWriter writer("euler_beam_explicit", rm);
    writer.write(0., {"Ut", "Vt", "At", "Ur", "Vr", "Ar"});    // write initial values
    // [declaration post-processing]

    // [simulation time]
    // -- Physical computational time
    // Anlytical period of first bending
    Real analyticalPeriod = 2. * M_PI / std::pow(1.875, 2) * std::pow(rho * S * std::pow(length, 4) / (E * Iz), 0.5);

    // Number of periods on which the computation should be done
    constexpr Real nbPeriods = 4.0;

    // N x First bending period
    Real calculationTime = analyticalPeriod * nbPeriods;

    // Get the critical time step of the formulation
    Real dt = eulerForm.getCriticalTimeStep();

    // number of iterations given th time stepping
    Int nbIterations = calculationTime / dt;
    // [simulation time]

    // [resolution]
    // --- Solving : time integration
    Real time = 0.;    // Incremental time of the simulation
    for (Int i = 1; i <= nbIterations; ++i) {
      // Compute next time step
      timeIntegrator.advanceOneStep(ctx, dt);
      time += dt;
      // Write to the VTK result file - 100 total points to not clog up the file
      if (i % (nbIterations / 500) == 0) {
        writer.write(time, {"Ut", "Vt", "At", "Ur", "Vr", "Ar"});
      }
    }
    // [resolution]
  }
  finalize();
}
```

## Call to the `MANTA_FATAL_ERROR` macro

The call to the `MANTA_FATAL_ERROR` allows the user to disable and safely
ignore all warnings and errors that could be raised by C++ functions marked as
`nodiscard`, i.e. the value returned by functions is expected to be stored and
post-processed by the script calling the function.
Additionally, this marks all encountered error as fatal as soon as possible,
rather than expecting the user to handle the error themself.

The call to this macro is **optional**.

```c++
  // Macro to disable warnings and error coming from the ignoring of functions
  // marked as nodiscard
  MANTA_FATAL_ERROR;
```

## Creation of `Context`

This object is mandatory for any MANTA computation.

The `Context` enables the handling of errors in MANTA (more details in
[Error handling in MANTA](../../../developer_guide/dev_guidelines/error_handling.md#error-handling)).

```c++
  // Creation of the context
  Context ctx;
```

## Reading a json input file

The example comes with a json file containing all independant parameters that can
be controlled.

The `readJSONDataFile` function reads the whole file, whereas each call to
the `get` function reads the value of a parameter, and specifies to which
type the parameter should be casted.

In this example, the deduced geometric values of a beam are deduced by hand and
will be used later on.

```c++
  // > Read the data from the JSON file
  const auto parameters = readJSONDataFile(ctx, "input_data.json");

  const Real E                           = get<Real>(*parameters, "YoungModulus");
  const Real nu                          = get<Real>(*parameters, "PoissonRatio");
  const Real h                           = get<Real>(*parameters, "thickness");
  const Real length                      = get<Real>(*parameters, "length");
  const Real rho                         = get<Real>(*parameters, "massDensity");
  const Vector<Real> principalAxisVector = get<Vector<Real>>(*parameters, "oyVector");

  // > Deduced geometric values
  Real b  = h;        // Dimension along the other axis. For this example, we choose a square cross section
  Real S  = b * h;    // Cross-section area
  Real Iy = (h / 12.) * (std::pow(b, 3));    // Second moment of area aroung principal axis
  Real Iz = (b / 12.) * (std::pow(h, 3));    // Second moment of area aroung secondary axis
  Real Jx = Iy + Iz;                         // Polar moment

  ColVector<3> oy_vector(principalAxisVector.data());    // Orientation vector
```

## Definition of the geometrical hypothesis

Before creating the mesh inside MANTA, the geometrical hypothesis must first be
set. In this example, we choose to conduct the calculation in **3D**, so the
appropriate `StructuralHypothesis` must be chosen (see [General parameters of solid mechanics formulations](../../../manta_components_user_guide/formulations/solid_mechanics/general_parameters.md#general-formulation-parameters-doc) for available `StructuralHypothesis`).

Then, the number of geometrical dimensions `geoDim` is deduced through the
helper structure `StructuralHypothesisTraits`, but could also have been
directly written (it is simply equal to **3** in **3D**).

The number of degrees of freedom (separated into translation DOFs and rotation
DOFs) are also stored in variables for later use, namely for the definition of
the node fields for displacement, velocity and acceleration. For a **3D** beam,
there are **6** DOFs per node, **3** of which are translation DOFs, and the **3**
other being rotation DOFs (see [Beam theory - Euler-Bernoulli and Timoshenko](../../../theory_manual/solid_mechanics/beams/beam_theory.md#theory-beam) for more details).

```c++
    // > Geometrical hypothesis
    constexpr StructuralHypothesis hypothesis = StructuralHypothesis::tridimensional;
    constexpr Int dim                         = StructuralHypothesisTraits<hypothesis>::geoDim;
    constexpr Int numDofsTranslation          = 3;
    constexpr Int numDofsRotation             = 3;
```

## Definition of the kinematic description

The total Lagrangian description is used in this example. Kinematics formulations available for beam models are described in the theory manual in the [Kinematics description formulation](../../../theory_manual/solid_mechanics/beams/beam_theory.md#theory-beam-kinematic-description-formulation) section. See also [General parameters of solid mechanics formulations](../../../manta_components_user_guide/formulations/solid_mechanics/general_parameters.md#general-formulation-parameters-doc) for available `KinematicDescription` options.

```c++
    // > Lagrangian kinematic description
    constexpr KinematicDescription kinematicDescription = KinematicDescription::lagrangian;
```

## Creation of `ResourcesManager`

This object is mandatory for any MANTA computation.

The `ResourcesManager` is the top-level structure in which global information
like the mesh support are defined (more details in [ResourcesManager](../../../developer_guide/services/resources_manager.md#resources-manager)).

The instanciation of most of the MANTA objects must transit thourgh the
`ResourcesManager.make` function (see following sections).

```c++
    // > Define the Ressource Manager
    ResourcesManager rm(dim);
```

## Import the mesh

In this example, the mesh is a simple beam, thus a simple meshed line will suffice.

The call to the `generateGrid` function allows the creation of a simple
**1D grid**, which corresponds to the desired meshed line. The origin, the dimension
and the number of elements are given as a parameter.

The `generateGrid` function also automatically creates groups of elements and
nodes, called `MeshSet`. These groups are named using the name given as
parameter to the `generateGrid` method (for more information, see
[Generating a grid and its MeshSet](../../../manta_components_user_guide/main_user_concepts/user_guide_objects/user_mesh.md#gridgenerator)).

Here, two `MeshSet` are also created to help with the definition of the
formulations, loads and boundary conditions.

- The `beam` mesh set contains all the generated elements (no suffix) ;
- The `right` mesh set contains the rightmost node (`_x1` suffix).

```c++
    // > Create a uniform mesh
    auto &mesh = rm.getMesh();
    mesh.generateGrid<1>("beam", {0.5 * length}, {length}, {20});

    // > Build meshSets
    MeshSet &beam  = mesh.getSet("beam");
    MeshSet &right = mesh.getSet("beam_x1");
```

## Define the node fields

The fields of unknown are declared as a vector (of size `numDofsTranslation`
or `numDofRotation`) field defined at the nodes.

Six fields of unknown are created to contain the **displacement**, the
**velocity** and the **acceleration**.
All these fields are needed because of the explicit integration scheme approach.
Translation and rotation DOFs are separated.

Notice that the fields are created through the `ResourcesManager.make`
method.

```c++
    // > Node field
    // displacement (translation and rotation)
    auto &Ut = rm.make<NodeField<>>(beam, "Ut", numDofsTranslation, 1);
    auto &Ur = rm.make<NodeField<>>(beam, "Ur", numDofsRotation, 1);
    // velocity (translation and rotation)
    auto &Vt = rm.make<NodeField<>>(beam, "Vt", numDofsTranslation, 1);
    auto &Vr = rm.make<NodeField<>>(beam, "Vr", numDofsRotation, 1);
    // acceleration (translation and rotation)
    auto &At = rm.make<NodeField<>>(beam, "At", numDofsTranslation, 1);
    auto &Ar = rm.make<NodeField<>>(beam, "Ar", numDofsRotation, 1);
    DofVar Atvar(numDofsTranslation, "At");
    DofVar Arvar(numDofsRotation, "Ar");
```

## Linear system and formulations

The linear system is then created, as well as the formulations. This constitutes
the declarative part of the example, where all physics related information
is created.

We go through each of the step of the problem definition in the following
sections.

### Linear system definition

A `LinearSystem` is declared in order to host all equation terms
relative to the problem that will be modeled and solved. As we deal with an
explicit integration scheme, the global mass matrix will be lumped, i.e. diagonal.
This justifies the usage of a `DiagonalLinearSystem`, which is suited for
diagonal / lumped matrices both memory-wise and speed-wise

```c++
    // > global linear system
    auto &feSystem = rm.make<DiagonalLinearSystem>("FESystem", mesh);
```

### Euler beam formulation

The `EulerBeamExplicitFormulation` is defined in order to model the beam.
This formulation encapsulates all needed equation terms to solve the problem,
namely the lumped mass matrix and the internal forces vector (corresponds to
the beam stiffness behaviour).

A **lumping strategy** for the mass matrix must be chosen. As
[Beam theory - Euler-Bernoulli and Timoshenko](../../../theory_manual/solid_mechanics/beams/beam_theory.md#theory-beam) states, the translation term has no impact as long as the
geometrical and material properties are constant along a single element. However,
for rotation terms, a choice must be made. In this example, we choose the
**Belytschko** lumping method, which corresponds to the term
\(\rho S L (\frac{L^2}{24} + \frac{1}{2}\frac{\max{I_y, I_z}}{S})\).

Finally, the formulation is assigned to the linear system.

For more details on this formulation implementation, see
[EulerBeamExplicitFormulation](../../../manta_components_user_guide/formulations/solid_mechanics/beams_and_shells/euler_beams/euler_beam_explicit_formulation.md#formulation-euler-beam-explicit).

```c++
    // Euler Explicit Formulation
    auto &eulerForm = rm.make<EulerBeamExplicitFormulation<hypothesis, Real, Real, Real, kinematicDescription>>(
        beam,
        QuadId::seg4,
        QuadId::seg2,
        Atvar,
        Arvar,
        Ut,
        Ur,
        E,
        nu,
        rho,
        BeamProperties<hypothesis>{S, Iy, Iz, Jx, oy_vector},
        LumpingTranslationStrategy::bending,
        LumpingRotationStrategy<hypothesis>{0., 420. / 24., 0., 0., 0., 0., 5.});

    rm.assignFormulationToLinearSystem(eulerForm, feSystem);
```

### Boundary Condition

The `BlockingFormulation` allows to define a boundary condition on the beam.
Here, all degrees of freedom are blocked at the `right` node.

For more details, see [BlockingFormulation](../../../manta_components_user_guide/formulations/constraints_and_bcs/blockingFormulation.md#formulation-blocking-fem).

```c++
    // Boundary conditions (clamped at the right node)
    auto &clampFormTran = rm.make<BlockingFormulation<true>>(Atvar, right, std::set{0, 1, 2});
    auto &clampFormRot  = rm.make<BlockingFormulation<true>>(Arvar, right, std::set{0, 1, 2});
    auto &clampCst      = rm.make<ConstraintSet>(feSystem, "clamp");

    rm.assignFormulationToLinearSystem(clampFormTran, clampCst);
    rm.assignFormulationToLinearSystem(clampFormRot, clampCst);
```

### Distributed loads

The `EulerBeamDistributedLoadFormulation` defines the distributed loads
that are to be applied on the beam. A uniform load equivalent to the effect of
gravity is imposed along the \(y\) axis.

For more details, see [EulerBeamDistributedLoadFormulation](../../../manta_components_user_guide/formulations/solid_mechanics/beams_and_shells/euler_beams/euler_beam_distributed_load_formulation.md#formulation-euler-distributed-load-formulation).

```c++
    // Imposing the distributed load force
    auto &eulerLoadForm = rm.make<EulerBeamDistributedLoadFormulation<hypothesis, Real>>(
        beam,
        QuadId::seg2,
        Atvar,
        Arvar,
        BeamProperties<hypothesis>{S, Iy, Iz, Jx, oy_vector},
        BeamDistributedLoads<hypothesis, Real>{0., -PhysicalConstants<UnitSystem::SI>::g * rho * S, 0., 0., 0., 0.},
        false);

    rm.assignFormulationToLinearSystem(eulerLoadForm, feSystem);
```

## Time integration scheme

A time integration scheme must be chosen. In this example, the chosen scheme
is the `CentralDifferenceTimeIntegrator`.

The dix previously declared **node fields** are given here to the integrator,
as well as the linear system to solve. The node fields must be given to the
integrator such as those correspoding to the translation DOFs are separated
from those corresponding to the rotation DOFs.

```c++
    // Explicit time integrator
    CentralDifferenceTimeIntegrator timeIntegrator(feSystem, {{Atvar, {Ut, Vt, At}}, {Arvar, {Ur, Vr, Ar}}});
```

## Post formulations

A `PostFormulation` is declared to allow the declared fields to be
post-processed and written to a VTK file.

```c++
    // Declare post formulations to allow post-processing
    Vector<FieldBase *> postFields = {&Ut, &Vt, &At, &Ur, &Vr, &Ar};
    rm.make<PostFormulation>(postFields);
```

## Memory allocation

This step is important to enable the effective computation. All previous steps
were purely **declarative**. From this point, no other declaration (e.g.
formulations) can be added, however the actual computation can now be conducted.

```c++
    // > Manta initialisation
    rm.init(ctx);
```

## Initial conditions

Now that memory allocation is effective, initial conditions can be defined.
Initial null displacement and velocity are assumed. Numerically, this will mean
that the initial time step will consist of an extremum of the displacement, and
that that extremum value will be \(0\).

```c++
    // > Initial value of the Node Field for all the nodes
    // Zero velocity such as we place ourselves at an extremum of displacement
    Vt.setValue(0.);
    Vr.setValue(0.);

    // Zero displacement -> Will be the value of an extremum
    Ut.setValue(0.);
    Ur.setValue(0.);
```

## VTK writer

To post-process the results, a writer must first be declared. All node fields
names are indicated here to write all of those fields in the result file.

```c++
    // > set post-proc writer
    VtkWriter writer("euler_beam_explicit", rm);
    writer.write(0., {"Ut", "Vt", "At", "Ur", "Vr", "Ar"});    // write initial values
```

## Simulation time and critical time step

The total number of time step must first be determined before solving
the problem iteratively.

An arbitrary calculation time is chosen (\(4.0\) periods). The total time
is then determined by multiplying the number of wanted periods and the time
corresponding to a period (the analytical expression of the period is given
in the analytical reference).

As the time integration scheme is **explicit**, the scheme is **conditionally stable**.
The maximal value of the time step, also known as the critical time step, is
directly given by the formulation via the `getCriticalTimeStep` method
(it could have been manually computed, the formula is given in [Beam theory - Euler-Bernoulli and Timoshenko](../../../theory_manual/solid_mechanics/beams/beam_theory.md#theory-beam)).

Finally, the total number of iterations is simply equal to the ratio between
the total calculation time and the critical time step.

```c++
    // -- Physical computational time
    // Anlytical period of first bending
    Real analyticalPeriod = 2. * M_PI / std::pow(1.875, 2) * std::pow(rho * S * std::pow(length, 4) / (E * Iz), 0.5);

    // Number of periods on which the computation should be done
    constexpr Real nbPeriods = 4.0;

    // N x First bending period
    Real calculationTime = analyticalPeriod * nbPeriods;

    // Get the critical time step of the formulation
    Real dt = eulerForm.getCriticalTimeStep();

    // number of iterations given th time stepping
    Int nbIterations = calculationTime / dt;
```

## Resolution

The resolution is conducted iteratively by calling the `advanceOneStep`
in a loop, and giving the wanted time step.

The results are also written into the VTK file.

```c++
    // --- Solving : time integration
    Real time = 0.;    // Incremental time of the simulation
    for (Int i = 1; i <= nbIterations; ++i) {
      // Compute next time step
      timeIntegrator.advanceOneStep(ctx, dt);
      time += dt;
      // Write to the VTK result file - 100 total points to not clog up the file
      if (i % (nbIterations / 500) == 0) {
        writer.write(time, {"Ut", "Vt", "At", "Ur", "Vr", "Ar"});
      }
    }
```

## Visualizing the results

Here are the results, shown on **ParaViS**.

[![figure](https://manta-project.gitlab.io/manta/_images/beam_results.gif)](../../../_images/beam_results.gif)

Fig. 7 Results of the example, exported in *ParaVis*
