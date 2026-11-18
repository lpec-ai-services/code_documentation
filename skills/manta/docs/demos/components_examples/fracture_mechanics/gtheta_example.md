<!-- source: https://manta-project.gitlab.io/manta/demos/components_examples/fracture_mechanics/gtheta_example.html -->

# Linear elastic fracture mechanics on a 2D plate with an inclined crack

This section is a short tutorial on how to write a main.cpp code
that runs a fracture mechanics simulation using the G Theta method
to compute the fracture energy release rate in a linear elastic case.
Below is a representative image of the full model in question.

This case is a reproduction of the rupt9.dgibi verification test available on Cast3M's website.

Note

The following files are required to run the tutorial:
- [`main.cpp`](../../../_downloads/335c5ac86d18f7c5ef336895e0679a6b/mainGtheta.cpp):
- [`RUPT9.dgibi`](../../../_downloads/e194950e5c3fd0db7d55506a5b96bd28/rupt9.dgibi):

Cast3M is required to run as a mesher to get the rupt9.msh file required to run this example.
You can find the current version of cast3M on this website: <https://www-cast3m.cea.fr> .

## Description

This is a model of a 2D plate with a 45° inclined crack,
loaded in traction implying mixed mode crack growth. The assumption of 2D plane strain is adopted,
with an isotropic linear elastic material, in the context of small strain.

[![figure](https://manta-project.gitlab.io/manta/_images/rupt9.png)](../../../_images/rupt9.png)

### Material's properties :

- **Young's Modulus**: \(E = 200\) GPa.
- **Poisson's coefficient**: \(\nu = 0.3\).

The specimen is a 2D rectangle of **length** \(L = 0.25\) m and a **width** \(W = 0.1\) m and a **crack length**
of \(l = 0.05\) m .

### Boundary conditions:

1. The displacements `Ux` and `Uy` are blocked, on the bottom left corner.
2. The displacement `Uy` are blocked, on the bottom right corner.

### Loading :

A 10 MPa pressure is applied to the left and right edges of the model thus sollicitating the sample in mixed modes.

**Keywords** linear elastic fracture mechanics, energy release rate , GTheta

## The mainGtheta.cpp step-by-step

### Libraries to include :

> ```c++
> #include "manta/components-fem_tools/constraints/dirichlet_constraint_set.h"
>
> #include "manta/components-fracture_mechanics/gtheta2D.h"
>
> #include "components/modeling/tests/e2e/nr/solid_finite_element_formulation.h"
>
> #include "manta/components-modeling/mechanics/imposed_pressure_formulation.h"
> ```

### Manta namespace :

> ```c++
> // NAMESPACE ----------------------------------------------------------
> using namespace manta;
> ```

### Declaration of main and init :

> ```c++
> int main(int argc, char **argv)
> {
>   // INITIALISATION ---------------------------------------------------
>
>   init(argc, argv);
>   {
> ```

### Creation of `Context` and `ResourcesManager`

Both objects are always necessary for MANTA computation.

- The `Context` enables to handle error in MANTA
  (more details in [Error handling in MANTA](../../../developer_guide/dev_guidelines/error_handling.md#error-handling)).
- The `ResourcesManager` is the top-level structure in which global information
  like the mesh support are defined
  (more details in [ResourcesManager](../../../developer_guide/services/resources_manager.md#resources-manager)). Its initialization requires to input the dimension of the treated problem.

  > ```c++
  >     Context ctx;
  >     ResourcesManager rm(2);
  > ```

### Import the mesh

A mesh support is extracted from the `ResourcesManager`.
Then mesh is imported from a CAST3M save and important regions are defined as `MeshSet`.
More details can be found on how to handle externally defined meshes in [this section](../../../manta_components_user_guide/main_user_concepts/user_guide_objects/user_mesh.md#reading-an-external-mesh).

> ```c++
>     auto &mesh = rm.getMesh();
>
>     std::string casename = "RUPT9";
>
>     Vector<std::string> regions = {"stot=2", "ctot=1", "lg=1", "ld=1", "p00=0", "p11=0", "lv=1"};
>
>     if (!readAndPartition(ctx, mesh, {casename + ".msh", "CASTEM_SAUV"}, regions, "RIB")) {
>       Message::error(ctx.getErrorMessage());
>     }
>
>     // The regions are identified as MeshSet object
>     MeshSet &cells = mesh.getSet("stot");
>     MeshSet &ld    = mesh.getSet("ld");
>     MeshSet &lg    = mesh.getSet("lg");
>     MeshSet &p00   = mesh.getSet("p00");
>     MeshSet &p11   = mesh.getSet("p11");
> ```

### Define the `Fields` and `LinearSystem`

The field of unknown displacement is declared as a `NodeField`. Furthermore, we declare the stress field
as an `IPField`. A so-called *Theta Field*, is defined as a perturbation field for the GTheta approach.
It is a `NodeField`.
A `LinearSystem` is also declared to solve for the displacement field and
easily obtain the associated stress field.

> ```c++
>     // variables
>     auto &U = rm.make<NodeField<2, 1>>(cells, "U");
>     DofVar Uvar(2, "U");
>     auto &cauchy = rm.make<IPField<>>(cells, "cauchy", 4, 1, QuadId::tri1); /*will be used in computation of G*/
>
>     auto &Theta = rm.make<NodeField<>>(cells, "Theta", 2, 1);
>
>     //Setting up the base linear system for Linearized Elasticity
>
>     // main linear system
>     auto &feSystem = rm.make<LinearSystem>("FESystem", mesh);
> ```

### Define the Behavior of the mechanical model

Here, a `LinearizedElasticityFiniteElementFormulation` class is declared to handle the elastic model used in this example.
This formulation is then assigned to the `LinearSystem` .

> ```c++
>     //Elasticity Formulation
>     auto &elasticityForm = rm.make<LinearizedElasticityFiniteElementFormulation<planeStrain, ShapeId::tri3, Real, Real>>(
>         cells, QuadId::tri1, Uvar, E, nu);
>
>     rm.assignFormulationToLinearSystem(elasticityForm, feSystem);
> ```

### Create the `GTheta2D` object

Instanciate the `GTheta2D` class and pass the required arguments to its constructor.
This class is needed to perform the GTheta method, that will compute the energy release rate.
Usage of this class is described in [GTheta Numerical Method 2D](../../../manta_components_user_guide/algorithms_and_numerics/gtheta_method_2D.md#gthetamethod2d)

> ```c++
>     //Declaring Gtheta procedure
>     GTheta2D GthetaMethod = GTheta2D<ShapeId::qua4, QuadId::qua4>(cells, U, Theta, cauchy);
> ```

### Define the boundary conditions

The `DirichletConstraintFormulation` is used to impose the displacement for some given degrees of freedom .

We can declare Dirichlet boundary conditions and add them to a `ConstraintSet` as follows :

> ```c++
>     // dirichlet BCs
>
>     auto &ends   = rm.make<MeshSet>(UnionOf({&p00, &p11}), "ends");
>     auto &bc     = rm.make<ConstraintSet>(feSystem, "bc");
>     auto &U0     = rm.make<NodeField<>>(ends, "U0", 2, 1);
>     auto &bcForm = rm.make<DirichletConstraintFormulation<2, true>>(Uvar, U0);
>     rm.assignFormulationToLinearSystem(bcForm, bc);
> ```

### Define the `ImposedPressureFormulation`

The `ImposedPressureFormulation` applies a pressure on the cell.
We can declare an applied pressure as follows :

> ```c++
>     // ImposedPressureFormulation is added to the linear system
>     // with a negative value to be in tension
>     constexpr auto h = GeometricHypothesis::defaultGeometricHypothesis;
>     auto &extForce1  = rm.make<ImposedPressureFormulation<h, ShapeId::seg2, const Real>>(lg, QuadId::seg2, Uvar, -1 * pext1);
>     rm.assignFormulationToLinearSystem(extForce1, feSystem);
>     auto &extForce2 = rm.make<ImposedPressureFormulation<h, ShapeId::seg2, const Real>>(ld, QuadId::seg2, Uvar, -1 * pext1);
>     rm.assignFormulationToLinearSystem(extForce2, feSystem);
> ```

More details can be found on this formulation in this section [Imposed pressure](../../../manta_components_user_guide/formulations/constraints_and_bcs/imposed_pressure.md#imposed-pressure-formulation).

### `rm.init`

The `ResourcesManager` is then initialized.

> ```c++
>     if (rm.init(ctx).shallStop()) {
>       Message::error(ctx.getErrorMessage());
>     }
> ```

### Initializing fields

The value of the fields are initialized here.
First, `U0` is initialized to impose the desired boundary conditions.
Then, the `Theta` perturbation field is initialized. It is defined as a circular perturbation field
around the crack tip varying from 0 to 1.

The Theta Field is zero outside the circle and given different value in the inner circle and outter circle.
:   [![figure](https://manta-project.gitlab.io/manta/_images/champsTheta.png)](../../../_images/champsTheta.png)

    ```c++
        //here we define the theta field

        Theta.setValue([](const RowVector<3> &x) {
          Real Value, b, a;

          ColVector<3> x1, rangle, posi;
          Real rayon;
          Real xo = 100 + 50 * sqrt(2) / 2, yo = 50 * sqrt(2) / 2;
          posi(0)   = xo;
          posi(1)   = yo;
          posi(2)   = 0;
          x1(0)     = x(0) - posi(0);
          x1(1)     = x(1) - posi(1);
          x1(2)     = x(2) - posi(2);
          rangle(0) = std::numbers::pi / 4;

          Matrix<2, 1> cteta;
          rayon    = sqrt(x1[0] * x1[0] + x1[1] * x1[1]);
          a        = 30;
          b        = 35;
          Real mag = 1.;
          Value    = (b - rayon) / (b - a);
          if (rayon <= a) {
            cteta(0) = mag * abs(cos(rangle(0)));
            cteta(1) = mag * abs(sin(rangle(0)));
          }
          else if (rayon > a && rayon < b) {
            cteta(0) = mag * Value * abs(cos(rangle(0)));
            cteta(1) = mag * Value * abs(sin(rangle(0)));
          }

          else if (rayon >= b) {
            cteta(0) = 0;
            cteta(1) = 0;
          }

          return cteta;
        });

        //blocking the left bottom corner x and y axis
        U0.setValue(ColVector<2>{0., 0.}, p00);

        //blocking the right bottom corner y axis
        U0.setValue(ColVector<2>{std::nan(""), 0.}, p11);

        cauchy.setValue(0.);
    ```

### Resolution of the `LinearSystem`

To get the displacement field we solve the linear system defined previously :

> ```c++
>     if (feSystem.assemble(ctx).shallStop()) {
>       Message::error(ctx.getErrorMessage());
>     }
>     if (feSystem.solve(ctx).shallStop()) {
>       Message::error(ctx.getErrorMessage());
>     }
>     if (feSystem.updateField(ctx, U, Uvar).shallStop()) {
>       Message::error(ctx.getErrorMessage());
>     }
> ```

### Get the stresses field

To get the stress field needed to compute the J integral we use the auxiliary task linked to the `LinearizedElasticityFiniteElementFormulation` .
An auxiliary task is requested and ran :

> ```c++
>     //we use the auxiliary task to get the cauchy stress that we need to compute the J integral
>     Kwargs auxiliaryTasksRequest = {{"cauchyStress",    //
>                                      Kwargs{{"cauchyField", std::ref(cauchy)}, {"displacementField", std::cref(U)}}}};
>     {
>       ExitStatus success = feSystem.runAuxiliaryTasks(ctx, {{elasticityForm, auxiliaryTasksRequest}});
>       if (!success) {
>         Message::error(ctx.getErrorMessage());
>       }
>     }
> ```

### Calling the function that computes and returns the value of G

To compute the Destuynder Integral for the given problem, the `computeGTheta2D()` method is used.
This method returns a `Real` representative of the computed energy release rate.

> ```c++
>     Real gthetaval = 0;
>
>     gthetaval = GthetaMethod.computeGTheta2D(ctx);
> ```

### End of file

Don't forget to finalize the init we started and close the parenthesis

> ```c++
>   }
>   finalize();
>   return 0;
> }
> ```
