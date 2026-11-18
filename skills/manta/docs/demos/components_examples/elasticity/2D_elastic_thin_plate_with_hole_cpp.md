<!-- source: https://manta-project.gitlab.io/manta/demos/components_examples/elasticity/2D_elastic_thin_plate_with_hole_cpp.html -->

# 2D linear elastic thin plate with a hole in tension in c++

This example exists in two flavours. In this file we focus on the one used with the `C++` components.
The second one relies on the Python bindings of the MANTA frontend, available [here](../../frontend_examples/elasticity/2D_elastic_thin_plate_with_hole_python.md#example-2d-elastic-thin-plate-with-hole-frontend-doc)

Note

The following files are required to run the tutorial:

- [`plate_with_hole.dgibi`](../../../_downloads/cfd42353b6e736b6d97f8ac484664bce/plate_with_hole.dgibi):
- [`main.cpp`](../../../_downloads/6c9cfa2f4d4ce0f6306375278771b743/main.cpp):
- [`CMakeLists.txt`](../../../_downloads/fefe3acdb7381e03d9a02fbb0def20fa/CMakeLists.txt):

Cast3M is required to run as a mesher to get the mesh file required to run this example.
You can find the current version of cast3M on this website: <https://www-cast3m.cea.fr> .

## Description

A thin plate with a hole is loaded in tension.
Its behavior is supposed linear elastic and small perturbation hypothesis hold.

Due to symmetry, only a quarter is meshed with the appropriate boundary conditions.

[![figure](https://manta-project.gitlab.io/manta/_images/plate_with_hole.svg)](../../../_images/plate_with_hole.svg)

Fig. 4 Description of the 2D plate with a hole in tension

**Keywords:** structure, static, elastic, linear, 2D, qua4.

**References:**

- Analytical solution: Test SSLP 01/89 of [[SocieteFdMecaniciens90](../../../references/references.md#id35)].
- Numerical solution: Cast3M, 2022.

The full test-file of this example is given just hereafter
but each significant step of this simple example
is explained in next subsections.

Full test-file

```c++
// clang-format off

// INCLUDE ------------------------------------------------------------
#include <iostream>         // standard includes
#include <string>
#include "manta/components-core/core.h"
#include "manta/components-xml_data_reader/xml_data_reader.h"
#include "manta/components-core/linear_system/linear_system.h"
#include "manta/components-core/linear_system/constraint_set.h"
#include "manta/components-modeling/mechanics/linearized_elasticity_formulation.h"
#include "manta/components-fem_tools/constraints/blocking_formulation.h"
#include "manta/components-modeling/mechanics/imposed_pressure_formulation.h"
#include "manta/components-core/post_formulation.h"
#include "manta/components-io_vtk/writer.h"

// NAMESPACE ----------------------------------------------------------
using namespace manta;
  
// MAIN ---------------------------------------------------------------
int main(int argc, char **argv)
{ 

  // PARAMETERS (set here or read from a xml file) --------------------

  // dim is a contant integer representing the modelling dimension (=2 for X,Y)
  constexpr Int dim = 2;
  constexpr StructuralHypothesis h = StructuralHypothesis::planeStress;
  // set in a .xml file to read
  XMLDataReader inputData("input_data.xml");
  // There are 2 ways to  declare, read and affect:
  // - 2-lines code:
  //   Int n1;
  //   inputData.get("NbElements", n1);
  // - 1-line code:
  auto n1   = inputData.get<Int>("NbElements");
  //not needed here  auto rho1 = inputData.get<Real>("rho");
  auto Ey1  = inputData.get<Real>("YoungModulus");
  auto nu1  = inputData.get<Real>("PoissonRatio");
  auto pext1 =inputData.get<Real>("Syy_inf");

  // Some output message
  std::string casename = "plate_with_hole-QUA4-" + std::to_string(n1);
  std::cout << casename << ": applied surface force =" << pext1 << std::endl;

  // INITIALISATION ---------------------------------------------------
  init(argc, argv);
  {
    // [ctx and rm creation]
    Context ctx;
    ResourcesManager rm(dim);
    // [ctx and rm creation]

    // [mesh creation]
    // mesh1 is the global mesh viewed by the ResourcesManager
    auto &mesh1=rm.getMesh();
    // It is necessary to define regions and their dimension
    Vector<std::string> regions = {"stot=2", "d13=1", "d25=1", "d36=1", "d67=1"};
    // read and partition
    if(!readAndPartition(ctx, mesh1, {casename + "-MESH.sauvgibi", "CASTEM_SAUV"}, regions, "RIB")) {
      Message::error(ctx.getErrorMessage());
    }

    // The regions are identified as MeshSet object to attribute specific modelling
    MeshSet &stot = mesh1.getSet("stot");
    MeshSet &d13  = mesh1.getSet("d13");
    MeshSet &d25  = mesh1.getSet("d25");
    MeshSet &d36  = mesh1.getSet("d36");
    MeshSet &d67  = mesh1.getSet("d67");
    // [mesh creation]

    // [displacement field]
    auto &U1 = rm.make<NodeField<dim, 1>>(stot, "U");
    DofVar U1var(dim, "U");
    // [displacement field]

    // [linear system]
    auto &feSystem1 = rm.make<LinearSystem>("FESystem", mesh1);

    // ELASTIC FORMULATION -------------------------------------------- // ①
    // of type LinearizedElasticityFiniteElementFormulation
    // based on the MeshSet stot, the dof var U1var and the field U1, with elastic constants Ey1 and nu1
    auto &myForm1 =
        rm.make<LinearizedElasticityFiniteElementFormulation<h, ShapeId::qua4, Real, Real>>(
          stot, QuadId::qua4, U1var, Ey1, nu1);
    rm.assignFormulationToLinearSystem(myForm1, feSystem1);

    // BOUNDARY CONDITIONS -------------------------------------------- // ②
    // --- LEFT BOUNDARY CONDITIONS : on d25, UX=0  ---
    // ConstraintSet is added to feSystem1
    auto &leftBC1   = rm.make<ConstraintSet>(feSystem1, "leftBC");
    // No value other than 0 imposed to the blocked dof --> BlockingFormulation is adapted
    // - true: to eliminate dof
    // - Vector<Int>{0}: first component is blocked (set to 0)
    auto &leftBCForm1 = rm.make<BlockingFormulation<true>>(U1var, d25, Vector<Int>{0});
    // BlockingFormulation is added to ConstraintSet
    rm.assignFormulationToLinearSystem(leftBCForm1, leftBC1);    
    // --- BOTTOM BOUNDARY CONDITIONS : on d13 and d36, UY=0 ---
    auto &bottom1       = rm.make<MeshSet>(UnionOf({&d13, &d36}), "bottom");
    auto &bottomBCForm1 = rm.make<BlockingFormulation<true>>(U1var, bottom1, Vector<Int>{1});
    auto &bottomBC1     = rm.make<ConstraintSet>(feSystem1, "bottomBC");
    rm.assignFormulationToLinearSystem(bottomBCForm1, bottomBC1);

    // LOADING -------------------------------------------------------- // ③
    // ImposedPressureFormulation is added to the linear system 
    // with a negative value to be in tension
    constexpr auto h2     = GeometricHypothesis::defaultGeometricHypothesis;
    auto &extForce1 = rm.make<ImposedPressureFormulation<h2, ShapeId::seg2, const Real>>(
        d67, QuadId::seg2, U1var, -1.*pext1);
    rm.assignFormulationToLinearSystem(extForce1, feSystem1);

    // TEMPORARY TRICK FOR THE OUPUT  --------------------------------- // ④
    Vector<FieldBase *> postFields = {&U1};
    rm.make<PostFormulation>(postFields);
    // [linear system]

    // [memory allocation]
    // MEMORY ALLOCATION AND INITIALISATIONS --------------------------
    if(rm.init(ctx).shallStop()){
      Message::error(ctx.getErrorMessage());
    }
    // [memory allocation]

    // [resolution and output]
    // VTK OUTPUT (time=0.) -------------------------------------------
    VtkWriter writer(casename, rm);
    writer.write(0., {"U", "CauchyStress"});

    // RESOLUTION -----------------------------------------------------
    if(feSystem1.assemble(ctx).shallStop()){
      Message::error(ctx.getErrorMessage());
    }
    //feSystem1.handleEliminatedConstraints();
    std::cout << "solving..." << std::endl;     
    if (feSystem1.solve(ctx).shallStop()){ // <1 
      Message::error(ctx.getErrorMessage());
    }

    // update displacement
    if (feSystem1.updateField(ctx, U1, U1var).shallStop())  { // ②
      Message::error(ctx.getErrorMessage());
    }
    // update CauchyStress
    // myForm1.afterConvergence(); --> doesn't work
    // ok, but suboptimal
    if(feSystem1.assemble(ctx).shallStop()){
      Message::error(ctx.getErrorMessage());
    }

    // VTK OUTPUT (time=1.) -------------------------------------------
    writer.write(1., {"U", "CauchyStress"}); // ③
    // [resolution and output]

// 1st { was opened by the main function
  // 2nd { was opened by the init function
    std::cout << "That's all folks !" << std::endl;  
  }
  finalize();
  return 0;
}
```

## Creation of `Context` and `ResourcesManager`

Both objects are always necessary for MANTA computation.

- The `Context` enables to handle error in MANTA
  (more details in [Error handling in MANTA](../../../developer_guide/dev_guidelines/error_handling.md#error-handling)).
- The `ResourcesManager` is the top-level structure in which global information
  like the mesh support are defined
  (more details in [ResourcesManager](../../../developer_guide/services/resources_manager.md#resources-manager)).

  > ```c++
  >     Context ctx;
  >     ResourcesManager rm(dim);
  > ```

## Import the mesh

The mesh is imported from a Cast3M saving and then important regions are defined as `MeshSet`.

> ```c++
>     // mesh1 is the global mesh viewed by the ResourcesManager
>     auto &mesh1=rm.getMesh();
>     // It is necessary to define regions and their dimension
>     Vector<std::string> regions = {"stot=2", "d13=1", "d25=1", "d36=1", "d67=1"};
>     // read and partition
>     if(!readAndPartition(ctx, mesh1, {casename + "-MESH.sauvgibi", "CASTEM_SAUV"}, regions, "RIB")) {
>       Message::error(ctx.getErrorMessage());
>     }
>
>     // The regions are identified as MeshSet object to attribute specific modelling
>     MeshSet &stot = mesh1.getSet("stot");
>     MeshSet &d13  = mesh1.getSet("d13");
>     MeshSet &d25  = mesh1.getSet("d25");
>     MeshSet &d36  = mesh1.getSet("d36");
>     MeshSet &d67  = mesh1.getSet("d67");
> ```

## Define the displacement field

The field of unknown is declared as a vector (of size `dim x 1`) field defined at the nodes.
A `DofVar` is also created alongside it: it names the degrees of freedom to
which the field will be related once attached to a `LinearSystem`
(see [DofVar: Dof variables](../../../developer_guide/pipeline/dof_var.md#dof-var) for details).

> ```c++
>     auto &U1 = rm.make<NodeField<dim, 1>>(stot, "U");
>     DofVar U1var(dim, "U");
> ```

## Linear system and formulation

The linear system is then created, as well as the formulations.

> ```c++
>     auto &feSystem1 = rm.make<LinearSystem>("FESystem", mesh1);
>
>     // ELASTIC FORMULATION -------------------------------------------- // ①
>     // of type LinearizedElasticityFiniteElementFormulation
>     // based on the MeshSet stot, the dof var U1var and the field U1, with elastic constants Ey1 and nu1
>     auto &myForm1 =
>         rm.make<LinearizedElasticityFiniteElementFormulation<h, ShapeId::qua4, Real, Real>>(
>           stot, QuadId::qua4, U1var, Ey1, nu1);
>     rm.assignFormulationToLinearSystem(myForm1, feSystem1);
>
>     // BOUNDARY CONDITIONS -------------------------------------------- // ②
>     // --- LEFT BOUNDARY CONDITIONS : on d25, UX=0  ---
>     // ConstraintSet is added to feSystem1
>     auto &leftBC1   = rm.make<ConstraintSet>(feSystem1, "leftBC");
>     // No value other than 0 imposed to the blocked dof --> BlockingFormulation is adapted
>     // - true: to eliminate dof
>     // - Vector<Int>{0}: first component is blocked (set to 0)
>     auto &leftBCForm1 = rm.make<BlockingFormulation<true>>(U1var, d25, Vector<Int>{0});
>     // BlockingFormulation is added to ConstraintSet
>     rm.assignFormulationToLinearSystem(leftBCForm1, leftBC1);    
>     // --- BOTTOM BOUNDARY CONDITIONS : on d13 and d36, UY=0 ---
>     auto &bottom1       = rm.make<MeshSet>(UnionOf({&d13, &d36}), "bottom");
>     auto &bottomBCForm1 = rm.make<BlockingFormulation<true>>(U1var, bottom1, Vector<Int>{1});
>     auto &bottomBC1     = rm.make<ConstraintSet>(feSystem1, "bottomBC");
>     rm.assignFormulationToLinearSystem(bottomBCForm1, bottomBC1);
>
>     // LOADING -------------------------------------------------------- // ③
>     // ImposedPressureFormulation is added to the linear system 
>     // with a negative value to be in tension
>     constexpr auto h2     = GeometricHypothesis::defaultGeometricHypothesis;
>     auto &extForce1 = rm.make<ImposedPressureFormulation<h2, ShapeId::seg2, const Real>>(
>         d67, QuadId::seg2, U1var, -1.*pext1);
>     rm.assignFormulationToLinearSystem(extForce1, feSystem1);
>
>     // TEMPORARY TRICK FOR THE OUPUT  --------------------------------- // ④
>     Vector<FieldBase *> postFields = {&U1};
>     rm.make<PostFormulation>(postFields);
> ```
>
> Elasticity of the material ①,
> as well as boundary conditions ② and loadings ③
> participate to the linear system, and must be assign to it.
>
> The use of a PostFormulation ④ is a temporary trick
> for output which will be removed very soon.

## Memory allocation

This step is important to enable the effective computation.

> ```c++
>     // MEMORY ALLOCATION AND INITIALISATIONS --------------------------
>     if(rm.init(ctx).shallStop()){
>       Message::error(ctx.getErrorMessage());
>     }
> ```

## Resolution and post-processing

> ```c++
>     // VTK OUTPUT (time=0.) -------------------------------------------
>     VtkWriter writer(casename, rm);
>     writer.write(0., {"U", "CauchyStress"});
>
>     // RESOLUTION -----------------------------------------------------
>     if(feSystem1.assemble(ctx).shallStop()){
>       Message::error(ctx.getErrorMessage());
>     }
>     //feSystem1.handleEliminatedConstraints();
>     std::cout << "solving..." << std::endl;     
>     if (feSystem1.solve(ctx).shallStop()){ // <1 
>       Message::error(ctx.getErrorMessage());
>     }
>
>     // update displacement
>     if (feSystem1.updateField(ctx, U1, U1var).shallStop())  { // <2>
>       Message::error(ctx.getErrorMessage());
>     }
>     // update CauchyStress
>     // myForm1.afterConvergence(); --> doesn't work
>     // ok, but suboptimal
>     if(feSystem1.assemble(ctx).shallStop()){
>       Message::error(ctx.getErrorMessage());
>     }
>
>     // VTK OUTPUT (time=1.) -------------------------------------------
>     writer.write(1., {"U", "CauchyStress"}); // <3>
> ```
>
> ① Solve the linear system
>
> ② Update the displacement field
>
> ③ Write the result to a file
