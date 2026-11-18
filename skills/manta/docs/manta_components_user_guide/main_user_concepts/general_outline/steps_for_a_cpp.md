<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/main_user_concepts/general_outline/steps_for_a_cpp.html -->

# Steps for a c++ computation with MANTA

The goal of this section is to give an overview of the different steps of
creating a MANTA script at the lower level C++ layer, as well as
give a taste of some of the available functionalities.

This commented example is centered around the previously presented
scalar laplacian problem. Similarly commented MANTA c++ scripts
can be found in [commented examples](../../../demos/demos.md#demos).

All ingredients mentioned in this section are detailed further in the
user guide and developer guide.
Links to the relevant part of the documentation are provided in each mini-chapters.

As in the previous page, here is the reference file for this section:

file pipeline-outline.cpp

```c++
//tag::includes
// need to give an absolute path to the .h
#include "manta/components-system/decl/exit_status.h"
#include "manta/components-system/init.h"
#include "manta/components-system/context.h"
#include "manta/components-system/decl/error_backtrace.h"
#include "manta/components-core/decl/dof_var.h"
#include "manta/components-core/linear_system/linear_system.h"
#include "manta/components-core/field/node_field.h"
#include "manta/components-core/field/function_set_value.h"
#include "manta/components-core/post_formulation.h"
// problem specific includes:e.g., here to solve a scalar laplacian problem
#include "manta/components-modeling/finite_elements/scalar_laplacian.h"
#include "manta/components-fem_tools/constraints/dirichlet_constraint_set.h"
// post processings
#include "manta/components-io_vtk/writer.h"
//end::includes

using namespace manta;

int main(int argc, char **argv)
{
  init(argc, argv);    // init manta
  {
    // Create the "model"
    // tag::defrm[]
    ResourcesManager rm(3);
    // end::defrm[]

    // Create a `Context` instance that is passed to some function to handle error messages or other things
    Context ctx;

    // Create a cubic mesh and get 2 MeshSets: the cube itself and its front (x=0.) face
    // tag::mesh[]
    auto &mesh               = rm.getMesh();
    auto meshSetList         = mesh.generateGrid<3>("cube", {.5, .5, .5}, {1., 1., 1.}, {16, 16, 16});
    const MeshSet &cube      = meshSetList[0];
    const MeshSet &frontFace = meshSetList[1];
    // end::mesh[]

    // Create a field to store the solution of the problem, and the dof variable used to attach it to dofs
    // tag::ufield[]
    auto &u = rm.make<NodeField<>>(cube, "solution", 1, 1);
    DofVar uVar(1, "solution");
    // end::ufield[]

    // Create the "main" linear system
    // tag::linsys-create[]
    auto &scalarLaplacianLinearSystem = rm.make<LinearSystem>("main linear system", mesh);
    // end::linsys-create[]

    // Create a formulation for scalar laplacian attached to the "cube" MeshSet, and passing it to the linear system
    // tag::form0[]
    auto &scalarLaplacianFormulation = rm.make<ScalarLaplacianFormulation<ShapeId::hex8>>(cube, QuadId::hex8, uVar);
    rm.assignFormulationToLinearSystem(scalarLaplacianFormulation, scalarLaplacianLinearSystem);
    // end::form0[]

    // Create a field storing the imposed function on the front face of the cube
    //tag::gfield[]
    auto &g = rm.make<NodeField<>>(frontFace, "imposed value", 1, 1);
    //end::gfield[]

    // Create a constraint set attached to the main linear system
    // tag::cset-create[]
    auto &dirichletBCConstraintSet = rm.make<ConstraintSet>(scalarLaplacianLinearSystem, "Constraints set");
    // end::cset-create[]

    // Create a formulation for the boundary condition related to the imposed field g, and passing it to the constraint set
    // tag::form1[]
    auto &dirichletBCFormulation = rm.make<DirichletConstraintFormulation<1, true>>(uVar, g);
    rm.assignFormulationToLinearSystem(dirichletBCFormulation, dirichletBCConstraintSet);
    // end::form1[]

    // For post treatment
    const Vector<FieldBase *> postFields = {&u};
    rm.make<PostFormulation>(postFields);

    // Initialize the model
    AdvancedExitStatus s = rm.init(ctx);
    if (s != ExitStatus::success) {
      Message::error(ctx.getErrorMessage());
    }

    //tag::gfield-setvalue[]
    g.setValue([](const RowVector<3> &x) {
      Matrix<1, 1> M;
      M(0) = std::sin(2. * M_PI * x(1)) * std::sin(M_PI * x(2));    // g = sin(\pi y) * sin(\pi z)
      return M;
    });
    //end::gfield-setvalue[]

    // Solve the problem
    // tag::calculation[]
    AdvancedExitStatus s1 = scalarLaplacianLinearSystem.assemble(ctx);

    AdvancedExitStatus s2 = scalarLaplacianLinearSystem.solve(ctx);

    AdvancedExitStatus s3 = scalarLaplacianLinearSystem.updateField(ctx, u, uVar);
    // end::calculation[]

    if (s1 != ExitStatus::success) {
      Message::error(ctx.getErrorMessage());
    }
    if (s2 != ExitStatus::success) {
      Message::error(ctx.getErrorMessage());
    }
    if (s3.shallStop()) {
      Message::error(ctx.getErrorMessage());
    }

    // tag::post_proc[]

    // Write the solution to the disk
    VtkWriter writer("scalar_laplacian", rm);
    writer.write(0., {"solution"});
    // end::post_proc[]
  }
  finalize();

  return 0;
}
```

## Outline of a MANTA lower level API C++ script

The steps of a MANTA C++ file can be listed as:

1. Defining the appropriate `include` for all the ingredients used in the file
and enter the manta namespace. Call to main.

2. Set the constant and parameters (*e.g.,* directly or by reading a
json file with a DataReader). Call to init.

3. Create a `Context` for error management, and a
`ResourcesManager`, from which all other instances will derive.

4. The declaration of the `ResourcesManager` instanciates a mesh,
that can be filled with an imported mesh, or by a MANTA generated grid.

5. Get/Create/Name some useful `MeshSets`.

6. Create the fields needed in the simulation (Fields at the nodes,
per elements, or at the integration points).

7. Create the `LinearSystem` and `Formulation`
representative of the different terms of the physics that is being solve.
This amounts to declaring the boundary conditions, the models along with
their coupling each linked to a specific part of the domain.

8. Declare the `TimeIntegrator`, or non linear solver `Algorithm` if needed.
9. Customizing the post-processing details for vtk output. (*e.g.,* which field, with which name).
10. Allocate the memory with the `ResourcesManager::init`.
11. Initialize fields, loadings, and other boundary conditions.

12. Solve the problem (*e.g.,* with a `TimeIntegrator`,
an `Algorithm.solve`, by assembling and solving).

13. Post-processings.
14. Finalize and return

Steps 1. to 9. are all declarative and *must* be performed
before the call to `ResourcesManager::init`.
In this document, we put forward a brief overview of some of those steps.

## Includes and parameter definition

Steps 1. and 2. can be mimicked from [commented examples](../../../demos/demos.md#demos),
and most main.cpp in the test base. Here is one example for includes:

```c++
// need to give an absolute path to the .h
#include "manta/components-system/decl/exit_status.h"
#include "manta/components-system/init.h"
#include "manta/components-system/context.h"
#include "manta/components-system/decl/error_backtrace.h"
#include "manta/components-core/decl/dof_var.h"
#include "manta/components-core/linear_system/linear_system.h"
#include "manta/components-core/field/node_field.h"
#include "manta/components-core/field/function_set_value.h"
#include "manta/components-core/post_formulation.h"
// problem specific includes:e.g., here to solve a scalar laplacian problem
#include "manta/components-modeling/finite_elements/scalar_laplacian.h"
#include "manta/components-fem_tools/constraints/dirichlet_constraint_set.h"
// post processings
#include "manta/components-io_vtk/writer.h"
```

And one example for the reading of parameters

```c++
  XMLDataReader inputData("input_data.xml");
  auto E   = inputData.get<Real>("YoungModulus");
  auto nu  = inputData.get<Real>("PoissonRatio");
  auto rho = inputData.get<Real>("rho");
  auto g   = inputData.get<Real>("g");
```

## The `ResourcesManager` class

The mesh is created along with the `ResourcesManager`. One has to specify the dimension of the
mesh at the declaration. For a 3D mesh, one can instanciate
a `ResourcesManager` and a `Mesh` with:

```c++
    ResourcesManager rm(3);
    auto &mesh = rm.getMesh();
```

## Filling the `Mesh`

Most of the time, the mesh is expected to be generated through an external software
and then read in MANTA. Three mesh format are supported, MED, GMSH, and Cast3M.
In the considered example, the mesh is a regular grid generated by MANTA.

The following lines from the considered example aim at:

1. Creating am empty `Mesh` instance within the
   `ResourcesManager` instance.
2. Generating a 16x16x16 cube in that mesh.
3. Getting `MeshSet` instances, one for the volumic elements of
   the cube mesh, one for the surfacic elements of the \(x=0\) face

```c++
    auto &mesh               = rm.getMesh();
    auto meshSetList         = mesh.generateGrid<3>("cube", {.5, .5, .5}, {1., 1., 1.}, {16, 16, 16});
    const MeshSet &cube      = meshSetList[0];
    const MeshSet &frontFace = meshSetList[1];
```

More details about the `Mesh`, and its manipulation
are given in the [pre-processing catalog](../../../catalogs/components/pre_proc_catalog_theme.md#pre-proc-catalog-theme) and
the developer guide's [services section](../../../developer_guide/services/services.md#services).

## Setting the `Meshsets`

`Meshsets` are simply defined as a collection of mesh entities.
They offer the support to manipulate specific parts of the mesh.
This could be to apply different physics on different domains,
applying boundary conditions or setting different material properties.

`Meshsets` can be extracted from the generated grid, or imported mesh.

Above was an example of the instanciation of `Meshsets` from a grid. Here
is an example of the instanciation of `Meshsets` read from an external file:

```c++
MeshSet &meshSet = mesh.getSet("nameOfMeshSet");
```

The string `nameOfMeshSet` must be consistent with the name of mesh entities
created by the external software.

`Meshsets` can also be created from other parts of the mesh,
or by selecting some specific mesh entities within the mesh.

More details about the definition of `MeshSet` can be
found in the [pre-processing catalog](../../../catalogs/components/pre_proc_catalog_theme.md#pre-proc-catalog-theme),
and in-depth details about the `MeshSet` classes
are given in the developer guide's [services section](../../../developer_guide/services/services.md#services).

## Declaring the `Fields`

The `Fields` are data structures used to link values to mesh entities,
and thus define the state and internal variables of the physical problem. There are three
types of `Field`:

- A `NodeField` associates values to each node of its support.
- An `ElementField` associates values to each entity of its support.
- An `IPField` derives from an `ElementField`
  but is associated with a quadrature so that values are associated
  with the integration points of an element.

In the example we construct two `NodeField`:

```c++
    auto &u = rm.make<NodeField<>>(cube, "solution", 1, 1);
    DofVar uVar(1, "solution");
```

It is defined on the whole domain (`cube`), and is a scalar quantity
(a `Field` carrying 1X1 matrices). Alongside the field, a `DofVar`
is also created: it names the family of degrees of freedom to which the
field's values will be related once it is linked to a `LinearSystem`
(see [DofVar: Dof variables](../../../developer_guide/pipeline/dof_var.md#dof-var) for details). Below is another example where we
define a `NodeField` on a given `MeshSet`.

```c++
    auto &g = rm.make<NodeField<>>(frontFace, "imposed value", 1, 1);
```

More details can be found on the definition and manipulation
of fields in the [preprocessing catalog](../../../catalogs/components/pre_proc_catalog_theme.md#pre-proc-catalog-theme) and
[the developer guide](../../../developer_guide/services/details_fields.md#details-fields).

## Declaring `Formulations` or the terms of the equation

As explained in the previous [page](user_outline.md#user-outline), to set up the equation
we define a `LinearSystem`, whose terms are computed by `Formulation` objects.

First we create a `LinearSystem`:

```c++
    auto &scalarLaplacianLinearSystem = rm.make<LinearSystem>("main linear system", mesh);
```

And then we create a `Formulation`, which we assign to the `LinearSystem`:

```c++
    auto &scalarLaplacianFormulation = rm.make<ScalarLaplacianFormulation<ShapeId::hex8>>(cube, QuadId::hex8, uVar);
    rm.assignFormulationToLinearSystem(scalarLaplacianFormulation, scalarLaplacianLinearSystem);
```

The boundary conditions are set-up through another formulation, with which we follow the same logic:

```c++
    auto &dirichletBCConstraintSet = rm.make<ConstraintSet>(scalarLaplacianLinearSystem, "Constraints set");
```

```c++
    auto &dirichletBCFormulation = rm.make<DirichletConstraintFormulation<1, true>>(uVar, g);
    rm.assignFormulationToLinearSystem(dirichletBCFormulation, dirichletBCConstraintSet);
```

The specific construction of available `Formulation` objects can be found in
this [catalog](../../../catalogs/components/physics_catalog_theme.md#physics-catalog-theme).

The way that the linear systems are assembled from attached formulations
is described with more details in [this section of the documentation](../../../developer_guide/pipeline/assembling.md#assembling).
Furthermore, the developer documentation details the linear system class and its implementation,
*e.g*, see the [blueprint section](../../../developer_guide/blueprints/linear_system_blueprint.md#blueprint-linear-system).

## The `TimeIntegrators` and `Algorithms`

In order to solve time dependant problems, users may use a `TimeIntegrator`,
that provides the support for a specific time discretization scheme.

In order to solve non linear problem, users may use an `Algorithm`,
that provides the support to use a non-linear solver. For the moment, only the Newton
algorithm is available.

Documentation for both these MANTA classes can be found in the [catalog section](../../../catalogs/components/physics_catalog_theme.md#physics-catalog-theme).

## Post-processings declaration for `vtk` output

Before initializing the MANTA datastructures, we can declare a `PostFormulation`,
where we specify the fields that are kept for post-processing,
and specify their name for the writer. Here is an example:

```c++
Vector<FieldBase *> postFields = {&U};
rm.make<PostFormulation>(postFields);
Vector<std::string> postFieldNames = {"U"};
```

## Initializing fields before resolution

After the declaration of every relevant instance to solve our problem,
it is mandatory to call for the `ResourcesManager::init` method.
The call is wrapped to improve error report:

```c++
if (rm.init(ctx).shallStop()) {
 Message::error(ctx.getErrorMessage());
}
```

Then fields can be filled with values (always **after** `rm.init()`)

```c++
    g.setValue([](const RowVector<3> &x) {
      Matrix<1, 1> M;
      M(0) = std::sin(2. * M_PI * x(1)) * std::sin(M_PI * x(2));    // g = sin(\pi y) * sin(\pi z)
      return M;
    });
```

## Solving the given problem

As presented in the previous page the following lines carry out the
steps of the assembly and resolution of the considered system
to solve a scalar Laplacian problem.

```c++
    AdvancedExitStatus s1 = scalarLaplacianLinearSystem.assemble(ctx);

    AdvancedExitStatus s2 = scalarLaplacianLinearSystem.solve(ctx);

    AdvancedExitStatus s3 = scalarLaplacianLinearSystem.updateField(ctx, u, uVar);
```

When using a `TimeIntegrator` or a `NewtonAlgorithm`, these steps are
wrapped in those class's respective methods:

```c++
AdvancedExitStatus s = timeIntegrator.advanceOneStep(ctx, timeIncrement);
```

```c++
auto s = newtonAlgorithm.solve(ctx);
```

Note here that those methods return a so-called `ExitStatus` or `AdvancedExitStatus`,
which are designed to assist MANTA developers with error management (more details can be found in
[the developer guide](../../../developer_guide/dev_guidelines/error_handling.md#error-handling)).

More information about algorithms at this layer are available in
the [the catalog of functionalities](../../../catalogs/components/physics_catalog_theme.md#physics-catalog-theme).

## Post-processings

### FieldReduction

For post-processings, one can use the available `FieldReduction` tools, described in depth
in the [following section about fields](../user_guide_objects/user_fields.md#reduction). It can, for instance,
yield the max/min value over a `MeshSet`, of a given `Field`.

### Vtk Output

There is a possibility to output fields in a `vtk` format

```c++
    // Write the solution to the disk
    VtkWriter writer("scalar_laplacian", rm);
    writer.write(0., {"solution"});
```

Note that here, `solution` is the name given to the primal nodal field.
Indeed, in the declaration part, we set:

```c++
    auto &u = rm.make<NodeField<>>(cube, "solution", 1, 1);
    DofVar uVar(1, "solution");
```

Furthermore, a time wise vtk output can be set up: the first parameter
being a "time-step": here we write the nodal field on the whole mesh and
save it at step 0.

## Further Examples

Additional sources of inspiration can be found in the [verification tests](../../../verification_tests/manta_components_verification_tests/manta_components_verification_tests.md#manta-components-verification-tests)
and [commented examples](../../../demos/demos.md#demos). For instance consider those cases:

- [2D linear elastic thin plate with a hole in tension](../../../demos/components_examples/elasticity/2D_elastic_thin_plate_with_hole_cpp.md#example-2d-elastic-thin-plate-with-hole-components) (FEM mechanics, implicit linear problem)
- [3D notched beam subjected to a Charpy impact test](../../../demos/components_examples/contact_and_impact/charpy.md#example-3d-charpy) (FEM damage mechanics, explicit)
- [Water-hammer in a pipe connected to a tank](../../../verification_tests/manta_components_verification_tests/compressible_fluid_mechanics/compressible_fluid_mechanics.md#manta-verification-tests-compressible-fluid-mechanics) (FV fluid mechanics) with sources in the components verification tests (compressible_fluid_mechanics/tank).
