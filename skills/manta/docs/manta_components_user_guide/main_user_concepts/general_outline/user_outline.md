<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/main_user_concepts/general_outline/user_outline.html -->

# General MANTA's c++ outline

To introduce the basics of MANTA's inner layer, let us consider the
case of a scalar Laplacian problem:

\[\begin{split}\begin{aligned}
&\text{Find }u\in H^1(\Omega)\text{ such that:}&&\\
&\begin{aligned}
&\quad&&\int_\Omega \nabla u\cdot\nabla v\d{x} = 0 &&\forall v\in \{H^1(\Omega),v=0\text{ on }\Omega_D\}\\
&\quad&&u=g(y,z)=\sin(2\pi y)\sin(\pi z)&&\text{ on }\partial\Omega_N \\
\end{aligned}\\
&\text{where:}&&\\
&\begin{aligned}
&\quad&&\Omega &&=&&]0,1[^3\\
&\quad&&\partial\Omega_D &&=&& \{x=0\} \\
&\quad&&\partial\Omega_N &&=&& \partial\Omega\backslash\partial\Omega_D\\
\end{aligned}\\
\end{aligned}\end{split}\]

Through finite elements discretization, this problem leads to solve the
following linear system:

\[\begin{split}\begin{bmatrix}
\m{K} & \m{C}^T \\
\m{C} & \m{0}
\end{bmatrix}
\begin{bmatrix}
\v{U} \\
\v{\lambda}
\end{bmatrix}
=
\begin{bmatrix}
\v{0} \\
\v{G}
\end{bmatrix}\end{split}\]

where \(\m{K}\) is related to the \(\int_\Omega \nabla
u\cdot\nabla v\d{x}\) term, and \(\m{C}\) and \(\m{G}\) to the
boundary condition \(u=g\text{ on }\partial\Omega_D\). \(\v{U}\)
is the discrete solution and \(\v{\lambda}\) a discrete Lagrange
multiplier.

Below is the code to treat this simple problem with manta using standard
finite elements on a 16x16x16 elements cube. Without going into
details, some key features of this code are described here.
In the next section, we will go into the details of this file.

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

## The `ResourcesManager` class

An instance of the `ResourcesManager` class aims at gathering and
interconnecting the different features of a given computation. These
features must be created within a resources manager instance using the
`ResourcesManager::make()` function which returns a
reference to the created object. Then **before assembling/solving the
linear system** related to the `ResourcesManager` instance, the model
instance must be initialized with `ResourcesManager::init()`.
In the considered example, all the lines between `ResourcesManager rm;` and
`rm.init();` define the content of the computation.

## The `Mesh` and `MeshSets` classes

The `Mesh` class manages mesh entities (cells, faces, segments,
vertices), and their connections or connectivities.

The mesh of the whole considered domain is fully distributed: each MPI
process only stores the entities related to its subdomain.

The `MeshSet` class manage sets of mesh entities.
They are used to define "physical zones" in the mesh.

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

## The fields

Classes are provided to manage fields of data. The fields are always
defined on a `MeshSet` instance, and in most cases should be
created within a `ResourcesManager` instance. Within its related
`MeshSet` instance, a field can refer to:

- the vertices: then it is a `NodeField`.
- the cells/facets: then it is a `ElementField`.
- the integration points: then it is a `IPField`.

A field manages a matrix of a given size (which could be specified
dynamically at creation, or statically through template parameters) at
each mesh entity it relates to. The matrix size of a given field is the
same for all the entities it relates to.

In the following line from the considered example, a `NodeField`
defined on the "cube" `MeshSet` is created
within a `ResourcesManager` instance. The matrix size at each node of the
"cube" `MeshSet` is 1x1.

```c++
    auto &u = rm.make<NodeField<>>(cube, "solution", 1, 1);
    DofVar uVar(1, "solution");
```

Alongside the field, a `DofVar` is created: it is a lightweight
identifier naming the family of degrees of freedom that will relate the
field's values to the rows/columns of a `LinearSystem` (see
[DofVar: Dof variables](../../../developer_guide/pipeline/dof_var.md#dof-var) for details).

## The `LinearSystem` and `ConstraintSet` classes

Assembling and solving linear systems of the form

\[\begin{split}\begin{bmatrix}
\m{K} & \m{C}^T \\
\m{C} & \m{0}
\end{bmatrix}
\begin{bmatrix}
\v{U} \\
\v{\lambda}
\end{bmatrix}
=
\begin{bmatrix}
\v{0} \\
\v{G}
\end{bmatrix}\end{split}\]

is the outcome of MANTA's pipeline. So the discrete problem
treated must be expressed as such.

The assembling of a `LinearSystem` instance is the computation
of its left hand side matrix (LHS) and its right hand side vector (RHS).
The `ConstraintSet` class derives from the
`LinearSystem` class, so it has to be assembled exactly the
same way as any `LinearSystem`.

The linear systems, as every data structure, are distributed over the
MPI processes: every MPI process only store and manage a portion of a
global linear system whose size is \(\bigo{N/p}\) where \(N\) is
the size of the global linear system and \(p\) is the number of MPI
processes.

In the considered example, there is one `LinearSystem`
instance, `scalarLaplacianLinearSystem`, and one
`ConstraintSet` instance, `dirichletBCFormulation`. The LHS
and RHS of `scalarLaplacianLinearSystem` are \(\m{K}\) and
\(\v{0}\) respectively. The LHS and RHS of
`dirichletBCFormulation` are \(\m{C}\) and \(\v{G}\)
respectively.

At the following line, the `LinearSystem`
`scalarLaplacianLinearSystem` is constructed within a `ResourcesManager`
instance. A `Mesh` instance has to be provided.

```c++
    auto &scalarLaplacianLinearSystem = rm.make<LinearSystem>("main linear system", mesh);
```

At the following line, the `ConstraintSet`
`dirichletBCFormulation` is constructed within a `ResourcesManager`
instance. A `LinearSystem` instance has to be provided (but no
`Mesh` instance, as the `ConstraintSet` instance use
the same mesh as the one of the provided `LinearSystem`
instance). A `ConstraintSet` instance is linked to the
`LinearSystem` instance passed at its construction.

```c++
    auto &dirichletBCConstraintSet = rm.make<ConstraintSet>(scalarLaplacianLinearSystem, "Constraints set");
```

Now let us consider the following lines, which carry out the
calculations of the considered case:

```c++
    AdvancedExitStatus s1 = scalarLaplacianLinearSystem.assemble(ctx);

    AdvancedExitStatus s2 = scalarLaplacianLinearSystem.solve(ctx);

    AdvancedExitStatus s3 = scalarLaplacianLinearSystem.updateField(ctx, u, uVar);
```

The three steps are:

1. The main linear system `scalarLaplacianLinearSystem` is assembled.
   Its attached `ConstraintSet` are automatically assembled
   too. So here \(\m{K}\), \(\m{C}\) and \(\v{G}\) are
   computed, and the LHS
   \(\m{A}=\left [ \m{K}, \m{C}^T; \m{C}, \m{0}\right
   ]\) and RHS \(\v{B}=\left[\v{0};\v{G}\right]\) are 'virtually'
   constructed.
2. The solution \(\v{X}=\left[\v{U};\v{\lambda}\right]\) of the
   system \(\m{A}\v{X}=\v{B}\) is computed. \(\v{U}\) and
   \(\v{\lambda}\) are stored internally by the linear system
   `scalarLaplacianLinearSystem`.
3. The solution \(\v{U}\) is transfered to the field `u`: The
   entities related to the field `u` (the vertices of the
   `MeshSet` `cube`) which bear degrees of freedom in the
   linear system `scalarLaplacianLinearSystem` are attributed the
   value of these degrees of freedom in the solution vector
   \(\v{U}\).

## The `Formulation` classes

Classes that derive from the base class `Formulation` are used
to define how the RHS and LHS of the linear systems are computed.

Internally, every `Formulation` instance is defined over a
`MeshSet` instance.

In the considered example, there are two kind of formulations:

- `ScalarLaplacianFormulation`: this formulation relates to
  the discretization with finite elements of the term
  \(\int_\Omega \nabla u\cdot\nabla v\d{x}\). In the following
  lines, an instance of this formulation is created within the
  `ResourcesManager` instance, and assigned to the 'main' linear system
  `scalarLaplacianLinearSystem`. The created formulation is defined
  over the `cube` `MeshSet`, and uses the `hex8` shape
  functions and the `hex8` quadrature.

  ```c++
      auto &scalarLaplacianFormulation = rm.make<ScalarLaplacianFormulation<ShapeId::hex8>>(cube, QuadId::hex8, uVar);
      rm.assignFormulationToLinearSystem(scalarLaplacianFormulation, scalarLaplacianLinearSystem);
  ```
- `DirichletConstraintFormulation`: this formulation relates
  to the discretization for finite elements of the boundary condition
  \(u=g\text{ on }\partial\Omega_D\). In the following lines, an
  instance of this formulation is created within the `ResourcesManager`
  instance, and assigned to the *constraint* linear system
  `dirichletBCConstraintSet`. The created formulation is defined over
  the `MeshSet` instance related to the input field `g`,
  *i.e.* `frontFace`.

  ```c++
      auto &dirichletBCFormulation = rm.make<DirichletConstraintFormulation<1, true>>(uVar, g);
      rm.assignFormulationToLinearSystem(dirichletBCFormulation, dirichletBCConstraintSet);
  ```

The formulations are the building blocks of the end user to construct its
problem to solve. Their interface and meaning, and at least the numerical
methods they involve, are documented in the [formulation section](../../../catalogs/components/physics_catalog_theme.md#physics-catalog-theme).

In the next [page](steps_for_a_cpp.md#steps-for-a-cpp), the construction of a main.cpp with MANTA is
discussed with more details, along with links to the relevant topics in the doc.
