<!-- source: https://manta-project.gitlab.io/manta/demos/components_examples/contact_and_impact/charpy.html -->

# 3D notched beam subjected to a Charpy impact test

## Description

A notched beam with a square cross-section is simply supported and subjected to an impact with a cylinder.
Its behavior is assumed elastoplastic.

[![figure](https://manta-project.gitlab.io/manta/_images/simply_supported_notched_beam.svg)](https://manta-project.gitlab.io/manta/_images/simply_supported_notched_beam.svg)

Fig. 5 Description of the notched beam, its support and impacting cylinder

**Keywords:** structure, impact, elastoplastic, 3D, hex8.

## Files for computation

The following files are needed in the working directory:

- CMakeLists.txt: a file used by cmake which specifies the build targets (here main) and their dependencies (here input_data.xml and charpy.geo).
- input_data.xml: stores the simulation parameters like the material constants, the loading value, etc.
- main.cpp: contains the simulation steps, from importing the mesh to performing the time integration.

The full test-file of this example is given just hereafter
but each significant step of this simple example
is explained in next subsections.

Full test-file

```c++
// [manta includes]

#include "manta/components-core/core.h"
#include "manta/components-io_vtk/writer.h"
#include "manta/components-xml_data_reader/xml_data_reader.h"
#include "manta/components-core/linear_system/linear_system.h"
#include "manta/components-core/linear_system/constraint_set.h"
#include "manta/components-modeling/mechanics/solid_finite_element_formulation.h"
#include "manta/components-behavior/mfront_behavior_component.h"
#include "manta/components-modeling/finite_elements/analytical_contact.h"
#include "manta/components-modeling/time_integrators/central_difference_with_contact.h"
#include "manta/components-core/post_formulation.h"

// system includes
#include <iostream>

// using the manta namespace

using namespace manta;

// [manta includes]

int main(int argc, char **argv)
{
  std::string casename = "./charpy";

  // [manta parameter reading]

  // Build a `XMLDataReader` from the xml input file...
  XMLDataReader inputData("input_data.xml");
  // ...then use the `DataReader` to get the parameters

  // Behaviors
  auto behaviorCharpyName  = inputData.get<std::string>("behaviorCharpy");
  auto behaviorStrikerName = inputData.get<std::string>("behaviorStriker");
  auto behaviorSupportName = inputData.get<std::string>("behaviorSupport");

  // Physical parameters
  auto rhoCharpy          = inputData.get<Real>("rhoCharpy");
  auto YoungModulusCharpy = inputData.get<Real>("YoungModulusCharpy");
  auto PoissonRatioCharpy = inputData.get<Real>("PoissonRatioCharpy");
  auto HCharpy            = inputData.get<Real>("HardeningSlopeCharpy");
  auto sy0Charpy          = inputData.get<Real>("YieldStrengthCharpy");

  // Final instant and output frequency
  auto tEnd        = inputData.get<Real>("tEnd");
  auto outputTFreq = inputData.get<Real>("outputTFreq");

  // What are those?
  auto v0 = inputData.get<Real>("v0");
  auto v1 = inputData.get<Real>("v1");

  // [manta parameter reading]

  // [ctx and rm creation]

  // init manta
  init(argc, argv);
  {
    Context ctx;
    ResourcesManager rm(3);

    // [ctx and rm creation]

    // [mesh decl and filling]

    // > read the mesh and get the meshSet
    // mesh is the global mesh viewed by the ResourcesManager
    auto &mesh = rm.getMesh();

    // It is necessary to define regions and their dimension
    Vector<std::string> regions = {
        "charpyContactUp=1",
        "charpyContactDown=1",
        "charpy=2",
    };

    if (!readAndPartition(ctx, mesh, {casename + ".msh", "GMSH"}, regions, "RIB")) {
      Message::error(ctx.getErrorMessage());
    }

    // The regions are identified as `MeshSet` objects which can have different attributes
    MeshSet &charpyContactUp   = mesh.getSet("charpyContactUp");
    MeshSet &charpyContactDown = mesh.getSet("charpyContactDown");
    MeshSet &charpy            = mesh.getSet("charpy");

    // [mesh decl and filling]

// [linearSystem decl]
    // create the "main" linear system
    auto &feSystem = rm.make<DiagonalLinearSystem>("FESystem", mesh);

    // > create the fields and other variables
    Real dt = 0.0;
    auto &U = rm.make<NodeField<>>(charpy, "U", 3, 1);
    auto &V = rm.make<NodeField<>>(charpy, "V", 3, 1);
    auto &G = rm.make<NodeField<>>(charpy, "G", 3, 1);
    DofVar Gvar(3, "G");
    // <
// [linearSystem decl]

// [behavior_def]
    // > create the behavior
    OMap<std::string, Vector<Real>> matp;

    matp["YoungModulus"]   = {YoungModulusCharpy};
    matp["PoissonRatio"]   = {PoissonRatioCharpy};
    matp["HardeningSlope"] = {HCharpy};
    matp["YieldStrength"]  = {sy0Charpy};
    matp["H"]              = {HCharpy};
    matp["sy0"]            = {sy0Charpy};
    MFrontBehaviorComponent behaviorCharpy(
        charpy, GeoType::hex8, QuadId::hex8, "./libCharpyBehaviours-generic.so", behaviorCharpyName, "Tridimensional", matp);
    // <

  // [behavior_def]

  // [formulation_def]

    // > formulations which compute the mass matrix and the internal forces
    auto &charpyInternalForcesForm =
        rm.make<SolidFiniteElementFormulation<tridimensional, MFrontBehaviorComponent, ShapeId::hex8, true>>(
            charpy, QuadId::hex8, Gvar, U, behaviorCharpy);
    auto &charpyMassForm = rm.make<HRZMassMatrixFormulation<tridimensional, ShapeId::hex8>>(charpy, Gvar, rhoCharpy);
    CriticalTimeStepComputer criticalTimeStepComputer(charpy, rhoCharpy, matp["YoungModulus"][0]);

    // > assign the formulations to the defined linearSystem
    rm.assignFormulationToRHSOfLinearSystem(charpyInternalForcesForm, feSystem);
    rm.assignFormulationToLinearSystem(charpyMassForm, feSystem);
    // <

  // [formulation_def]

  // [constraints_def]

    // > create the contact constraints

    // Use of lambda functions to define the variation of the contact constraints in space

    RowVector<2> oStriker;
    auto analyticalContactFuncStriker =
        [&](ConstRowVectorRef<3> xs, RowVectorRef<3> xm, RowVectorRef<3> nm, RowVectorRef<3> vm) {
          const Real R = .002;

          RowVector<2> D = head<2>(xs) - oStriker;
          Real d         = norm(D);

          if (d < R) {
            head<2>(xm) = oStriker + D / d * R;
            xm(2)        = xs(2);
            head<2>(nm) = D / d;
            nm(2)        = 0.;
            vm.setZero();
            vm(1) = v0;
            return true;
          }
          else {
            return false;
          }
        };

    auto analyticalContactFuncSupport =
        [&](ConstRowVectorRef<3> xs, RowVectorRef<3> xm, RowVectorRef<3> nm, RowVectorRef<3> vm) {
          if (xs(0) < 8.5e-3 && xs(1) < -1.e-5) {
            if (xs(0) < 7.5e-3) {
              xm    = xs;
              xm(1) = -1.e-5;
              nm << 0., 1., 0.;
              vm.setZero();
              return true;
            }
            else {
              Real R = .001;
              RowVector<2> oSupport;
              oSupport << 7.5e-3, -1.01e-3;
              RowVector<2> D = head<2>(xs) - oSupport;
              Real d         = norm(D);

              if (d < R) {
                head<2>(xm) = oSupport + D / d * R;
                xm(2)        = xs(2);
                head<2>(nm) = D / d;
                nm(2)        = 0.;
                vm.setZero();
                return true;
              }
              else {
                return false;
              }
            }
          }
          else if (xs(0) > 46.5e-3 && xs(1) < -1.e-5) {
            if (xs(0) > 47.5e-3) {
              xm    = xs;
              xm(1) = -1.e-5;
              nm << 0., 1., 0.;
              vm.setZero();
              return true;
            }
            else {
              Real R = .001;
              RowVector<2> oSupport;
              oSupport << 47.5e-3, -1.01e-3;
              RowVector<2> D = head<2>(xs) - oSupport;
              Real d         = norm(D);

              if (d < R) {
                head<2>(xm) = oSupport + D / d * R;
                xm(2)        = xs(2);
                head<2>(nm) = D / d;
                nm(2)        = 0.;
                vm.setZero();
                return true;
              }
              else {
                return false;
              }
            }
          }
          else {
            return false;
          }
        };

    // Definition of the contact constraints based on the previously defined lambdas
    auto &contactFormStriker =
        rm.make<AnalyticalContactFormulation>(Gvar, analyticalContactFuncStriker, charpyContactUp, V);
    auto &contactCSetStriker = rm.make<ConstraintSet>(feSystem, "contactCharpyStriker");
    contactCSetStriker.asPrimitive(V, Gvar, dt);
    rm.assignFormulationToLinearSystem(contactFormStriker, contactCSetStriker);

    auto &contactFormSupport =
        rm.make<AnalyticalContactFormulation>(Gvar, analyticalContactFuncSupport, charpyContactDown, V);
    auto &contactCSetSupport = rm.make<ConstraintSet>(feSystem, "contactCharpySupport");
    contactCSetSupport.asPrimitive(V, Gvar, dt);
    rm.assignFormulationToLinearSystem(contactFormSupport, contactCSetSupport);
    // <
  // [constraints_def]

// [post-processing definitions]
    // > output fields defined in this main
    Vector<FieldBase *> postFields = {&U, &V, &G};
    rm.make<PostFormulation>(postFields);
// [post-processing definitions]

    // <

//[timeintegrator definition]
    // > time integrator
    CentralDifferenceWContactTimeIntegrator timeIntegrator(
        feSystem, {U, V, G}, Gvar, {contactCSetStriker, contactCSetSupport});
    // <
//[timeintegrator definition]

//[memory allocation]
    // init the model
    if (rm.init(ctx).shallStop()) {
      Message::error(ctx.getErrorMessage());
    }
//[memory allocation]

//[initializations]
    // > set initial values
    //tag::getTS[]
    Real dtCrit = criticalTimeStepComputer.getCriticalTimeStep();
    //end::getTS[]
    Real cfl    = 0.9;
    dt          = dtCrit * cfl;
    G.setValue(0.);
    V.setValue(0.);
    U.setValue(0.);
    Matrix<3, 1> V0;
    Matrix<3, 1> V1;
    V0 << 0., v0, 0.;
    V1 << 0., v1, 0.;
    // V.setValue(V0, striker);
    V.setValue(V1, charpy);
    // V.setValue(V1, support);
    // <

    // > create writer and output initial mesh
    VtkWriter writer(casename, rm);
    writer.write(0., {"U", "V", "Gc"});
    // <
//[initializations]

//[resolution]

    // > time integration
    Real time           = 0.;
    Index tStep         = 0;
    Real lastOutputTime = 0.;
    while (time < tEnd) {
      oStriker << 0.0275, 0.01201;
      oStriker(1) += v0 * time;

      if (timeIntegrator.advanceOneStep(ctx, dt).shallStop()) {
        Message::error(ctx.getErrorMessage());
      }
      charpyInternalForcesForm.update();

      // update time
      time += dt;

      // > output if required
      if (time - lastOutputTime > outputTFreq) {
        Message::info(">> Compute time step " + std::to_string(tStep) + " at time " + std::to_string(time));
        lastOutputTime = time;
        writer.write(time, {"U", "V", "Gc"});
      }
      // <
      ++tStep;
    }
    // <

  //[resolution]

  //[finalize]

  }
  finalize();
  return 0;
}
  //[finalize]
```

## The main.cpp step-by-step

Includes and namespace

Includes are classes/librairies the program will need.

[Namespaces](https://en.cppreference.com/w/cpp/language/namespace) are a way to prevent name conflicts in large projects. They also enable direct
access to functions and objects instead of having to use fully qualified names.
For instance, if `std::cout` is used a lot throughout a file, it may be convenient to
add `using namespace std;` at the beginning of the file, and then call
`cout << hello` instead of `std::cout << hello`.

```c++
#include "manta/components-core/core.h"
#include "manta/components-io_vtk/writer.h"
#include "manta/components-xml_data_reader/xml_data_reader.h"
#include "manta/components-core/linear_system/linear_system.h"
#include "manta/components-core/linear_system/constraint_set.h"
#include "manta/components-modeling/mechanics/solid_finite_element_formulation.h"
#include "manta/components-behavior/mfront_behavior_component.h"
#include "manta/components-modeling/finite_elements/analytical_contact.h"
#include "manta/components-modeling/time_integrators/central_difference_with_contact.h"
#include "manta/components-core/post_formulation.h"

// system includes
#include <iostream>

// using the manta namespace

using namespace manta;
```

### Reading parameters from external xml file

Parameters are stored in an external xml file format. A `XMLDataReader` is first created in order to extract those parameters.
Note that parameters can also be set directly in the main.cpp file.

> ```c++
>   // Build a `XMLDataReader` from the xml input file...
>   XMLDataReader inputData("input_data.xml");
>   // ...then use the `DataReader` to get the parameters
>
>   // Behaviors
>   auto behaviorCharpyName  = inputData.get<std::string>("behaviorCharpy");
>   auto behaviorStrikerName = inputData.get<std::string>("behaviorStriker");
>   auto behaviorSupportName = inputData.get<std::string>("behaviorSupport");
>
>   // Physical parameters
>   auto rhoCharpy          = inputData.get<Real>("rhoCharpy");
>   auto YoungModulusCharpy = inputData.get<Real>("YoungModulusCharpy");
>   auto PoissonRatioCharpy = inputData.get<Real>("PoissonRatioCharpy");
>   auto HCharpy            = inputData.get<Real>("HardeningSlopeCharpy");
>   auto sy0Charpy          = inputData.get<Real>("YieldStrengthCharpy");
>
>   // Final instant and output frequency
>   auto tEnd        = inputData.get<Real>("tEnd");
>   auto outputTFreq = inputData.get<Real>("outputTFreq");
>
>   // What are those?
>   auto v0 = inputData.get<Real>("v0");
>   auto v1 = inputData.get<Real>("v1");
> ```

### Creation of `Context` and `ResourcesManager`

Both objects are always necessary for MANTA computation.

- The `Context` enables to handle error in MANTA
  (more details in [Error handling in MANTA](../../../developer_guide/dev_guidelines/error_handling.md#error-handling)).
- The `ResourcesManager` is the top-level structure in which global information
  like the mesh support are defined
  (more details in [ResourcesManager](../../../developer_guide/services/resources_manager.md#resources-manager)). Its initialization requires to input the dimension of the treated problem.

  > ```c++
  >   // init manta
  >   init(argc, argv);
  >   {
  >     Context ctx;
  >     ResourcesManager rm(3);
  > ```

### Import the mesh

A mesh support is extracted from the `ResourcesManager`.
Then mesh is imported from a GMSH saving and important regions are defined as `MeshSet`.

> ```c++
>     // > read the mesh and get the meshSet
>     // mesh is the global mesh viewed by the ResourcesManager
>     auto &mesh = rm.getMesh();
>
>     // It is necessary to define regions and their dimension
>     Vector<std::string> regions = {
>         "charpyContactUp=1",
>         "charpyContactDown=1",
>         "charpy=2",
>     };
>
>     if (!readAndPartition(ctx, mesh, {casename + ".msh", "GMSH"}, regions, "RIB")) {
>       Message::error(ctx.getErrorMessage());
>     }
>
>     // The regions are identified as `MeshSet` objects which can have different attributes
>     MeshSet &charpyContactUp   = mesh.getSet("charpyContactUp");
>     MeshSet &charpyContactDown = mesh.getSet("charpyContactDown");
>     MeshSet &charpy            = mesh.getSet("charpy");
> ```

### Define the `Fields` and associated `LinearSystem`

The field of unknown is declared as a vector (of size `dim x 1`) field defined at the nodes.
Here, the dynamic mechanical model imposes the declaration of three fields, representative of the
three order of displacement unknowns when acceleration is considered (`U` the displacement,
`V`, its rate, and `G` its acceleration).
Only one `DofVar` (`Gvar`) is created, for the acceleration: since
`G` is the actual unknown of the explicit dynamics system, `U` and
`V` are later related to the same dofs by being paired with `Gvar`
wherever they are needed (see [DofVar: Dof variables](../../../developer_guide/pipeline/dof_var.md#dof-var) and, in particular,
[Several fields for the same DofVar](../../../developer_guide/pipeline/dof_var.md#dof-var-several-fields) for details).

> ```c++
>     // create the "main" linear system
>     auto &feSystem = rm.make<DiagonalLinearSystem>("FESystem", mesh);
>
>     // > create the fields and other variables
>     Real dt = 0.0;
>     auto &U = rm.make<NodeField<>>(charpy, "U", 3, 1);
>     auto &V = rm.make<NodeField<>>(charpy, "V", 3, 1);
>     auto &G = rm.make<NodeField<>>(charpy, "G", 3, 1);
>     DofVar Gvar(3, "G");
>     // <
> ```

### Define the `MFrontBehaviorComponent` or mechanical model

> ```c++
>     // > create the behavior
>     OMap<std::string, Vector<Real>> matp;
>
>     matp["YoungModulus"]   = {YoungModulusCharpy};
>     matp["PoissonRatio"]   = {PoissonRatioCharpy};
>     matp["HardeningSlope"] = {HCharpy};
>     matp["YieldStrength"]  = {sy0Charpy};
>     matp["H"]              = {HCharpy};
>     matp["sy0"]            = {sy0Charpy};
>     MFrontBehaviorComponent behaviorCharpy(
>         charpy, GeoType::hex8, QuadId::hex8, "./libCharpyBehaviours-generic.so", behaviorCharpyName, "Tridimensional", matp);
>     // <
> ```

### Define the `Formulation`

The `Formulation` shall compute all elementary terms that will fill the terms of the `LinearSystem`
:   ```c++
        // > formulations which compute the mass matrix and the internal forces
        auto &charpyInternalForcesForm =
            rm.make<SolidFiniteElementFormulation<tridimensional, MFrontBehaviorComponent, ShapeId::hex8, true>>(
                charpy, QuadId::hex8, Gvar, U, behaviorCharpy);
        auto &charpyMassForm = rm.make<HRZMassMatrixFormulation<tridimensional, ShapeId::hex8>>(charpy, Gvar, rhoCharpy);
        CriticalTimeStepComputer criticalTimeStepComputer(charpy, rhoCharpy, matp["YoungModulus"][0]);

        // > assign the formulations to the defined linearSystem
        rm.assignFormulationToRHSOfLinearSystem(charpyInternalForcesForm, feSystem);
        rm.assignFormulationToLinearSystem(charpyMassForm, feSystem);
        // <
    ```

### Define contact `Constraints`

The boundary conditions in this example are based on contacts.
Definition of these contact are performed in two steps, first defining the coordinates of
slave and master components of the contact (`xs`, `xm`), and speed and normal
of the master components (`nm`, `vm`).
Then those contact informations for the indenter and supports
are inputted in an `AnalyticalContactFormulation` defining the constraintSet for this problem.

> ```c++
>     // > create the contact constraints
>
>     // Use of lambda functions to define the variation of the contact constraints in space
>
>     RowVector<2> oStriker;
>     auto analyticalContactFuncStriker =
>         [&](ConstRowVectorRef<3> xs, RowVectorRef<3> xm, RowVectorRef<3> nm, RowVectorRef<3> vm) {
>           const Real R = .002;
>
>           RowVector<2> D = head<2>(xs) - oStriker;
>           Real d         = norm(D);
>
>           if (d < R) {
>             head<2>(xm) = oStriker + D / d * R;
>             xm(2)        = xs(2);
>             head<2>(nm) = D / d;
>             nm(2)        = 0.;
>             vm.setZero();
>             vm(1) = v0;
>             return true;
>           }
>           else {
>             return false;
>           }
>         };
>
>     auto analyticalContactFuncSupport =
>         [&](ConstRowVectorRef<3> xs, RowVectorRef<3> xm, RowVectorRef<3> nm, RowVectorRef<3> vm) {
>           if (xs(0) < 8.5e-3 && xs(1) < -1.e-5) {
>             if (xs(0) < 7.5e-3) {
>               xm    = xs;
>               xm(1) = -1.e-5;
>               nm << 0., 1., 0.;
>               vm.setZero();
>               return true;
>             }
>             else {
>               Real R = .001;
>               RowVector<2> oSupport;
>               oSupport << 7.5e-3, -1.01e-3;
>               RowVector<2> D = head<2>(xs) - oSupport;
>               Real d         = norm(D);
>
>               if (d < R) {
>                 head<2>(xm) = oSupport + D / d * R;
>                 xm(2)        = xs(2);
>                 head<2>(nm) = D / d;
>                 nm(2)        = 0.;
>                 vm.setZero();
>                 return true;
>               }
>               else {
>                 return false;
>               }
>             }
>           }
>           else if (xs(0) > 46.5e-3 && xs(1) < -1.e-5) {
>             if (xs(0) > 47.5e-3) {
>               xm    = xs;
>               xm(1) = -1.e-5;
>               nm << 0., 1., 0.;
>               vm.setZero();
>               return true;
>             }
>             else {
>               Real R = .001;
>               RowVector<2> oSupport;
>               oSupport << 47.5e-3, -1.01e-3;
>               RowVector<2> D = head<2>(xs) - oSupport;
>               Real d         = norm(D);
>
>               if (d < R) {
>                 head<2>(xm) = oSupport + D / d * R;
>                 xm(2)        = xs(2);
>                 head<2>(nm) = D / d;
>                 nm(2)        = 0.;
>                 vm.setZero();
>                 return true;
>               }
>               else {
>                 return false;
>               }
>             }
>           }
>           else {
>             return false;
>           }
>         };
>
>     // Definition of the contact constraints based on the previously defined lambdas
>     auto &contactFormStriker =
>         rm.make<AnalyticalContactFormulation>(Gvar, analyticalContactFuncStriker, charpyContactUp, V);
>     auto &contactCSetStriker = rm.make<ConstraintSet>(feSystem, "contactCharpyStriker");
>     contactCSetStriker.asPrimitive(V, Gvar, dt);
>     rm.assignFormulationToLinearSystem(contactFormStriker, contactCSetStriker);
>
>     auto &contactFormSupport =
>         rm.make<AnalyticalContactFormulation>(Gvar, analyticalContactFuncSupport, charpyContactDown, V);
>     auto &contactCSetSupport = rm.make<ConstraintSet>(feSystem, "contactCharpySupport");
>     contactCSetSupport.asPrimitive(V, Gvar, dt);
>     rm.assignFormulationToLinearSystem(contactFormSupport, contactCSetSupport);
>     // <
> ```

### Defining output `Fields`

`Fields` that has to be analysed by end-users have to be defined in a `PostFormulation`

> ```c++
>     // > output fields defined in this main
>     Vector<FieldBase *> postFields = {&U, &V, &G};
>     rm.make<PostFormulation>(postFields);
> ```

### Definition of a `TimeIntegrator`

In an explicit context, time integration is required to treat the second order time equation
of dynamical mechanics. Pre-made structure are available in `MANTA` for time integration,
such as the `CentralDifferenceTimeIntegrator`, or here the specific
`CentralDifferenceWContactTimeIntegrator`

> ```c++
>     // > time integrator
>     CentralDifferenceWContactTimeIntegrator timeIntegrator(
>         feSystem, {U, V, G}, Gvar, {contactCSetStriker, contactCSetSupport});
>     // <
> ```

### Memory allocation

This step is important to enable the effective computation.

> ```c++
>     // init the model
>     if (rm.init(ctx).shallStop()) {
>       Message::error(ctx.getErrorMessage());
>     }
> ```

### Field initialization

Before the first computing step, all fields must be initialized with a given value.
Furthermore, a `VTKWriter` can be initialized and used to write the value of
some specific fields in a `VTK` format just before the first computing step.

> ```c++
>     // > set initial values
>     //tag::getTS[]
>     Real dtCrit = criticalTimeStepComputer.getCriticalTimeStep();
>     //end::getTS[]
>     Real cfl    = 0.9;
>     dt          = dtCrit * cfl;
>     G.setValue(0.);
>     V.setValue(0.);
>     U.setValue(0.);
>     Matrix<3, 1> V0;
>     Matrix<3, 1> V1;
>     V0 << 0., v0, 0.;
>     V1 << 0., v1, 0.;
>     // V.setValue(V0, striker);
>     V.setValue(V1, charpy);
>     // V.setValue(V1, support);
>     // <
>
>     // > create writer and output initial mesh
>     VtkWriter writer(casename, rm);
>     writer.write(0., {"U", "V", "Gc"});
>     // <
> ```

### Resolution and post-processing

At each time-step, boundary conditions are updated (to induce a load by contacts),
and the `advanceOneStep` method of the `TimeIntegrator` is used to
assemble, solve and update the displacement (and rate and acceleration) field.

The defined `VTKWriter` is used to write the value of `Fields` of interest in a `VTK` format
at each time-step (here only at a specific `outputTFreq`)

> ```c++
>     // > time integration
>     Real time           = 0.;
>     Index tStep         = 0;
>     Real lastOutputTime = 0.;
>     while (time < tEnd) {
>       oStriker << 0.0275, 0.01201;
>       oStriker(1) += v0 * time;
>
>       if (timeIntegrator.advanceOneStep(ctx, dt).shallStop()) {
>         Message::error(ctx.getErrorMessage());
>       }
>       charpyInternalForcesForm.update();
>
>       // update time
>       time += dt;
>
>       // > output if required
>       if (time - lastOutputTime > outputTFreq) {
>         Message::info(">> Compute time step " + std::to_string(tStep) + " at time " + std::to_string(time));
>         lastOutputTime = time;
>         writer.write(time, {"U", "V", "Gc"});
>       }
>       // <
>       ++tStep;
>     }
>     // <
> ```

### Finalize a main.cpp

Closing the `init` bracket (not the rm.init() !), and return from the `main`.

> ```c++
>   }
>   finalize();
>   return 0;
> }
> ```
