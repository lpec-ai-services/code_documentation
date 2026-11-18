<!-- source: https://manta-project.gitlab.io/manta/demos/components_examples/components_examples.html -->

# Commented examples in the components

This section contains commented examples of the components c++ layer of MANTA.

Here is a list of all available commented example to this date:

c++ Commented manta examples

- [2D linear elastic thin plate with a hole in tension in c++](elasticity/2D_elastic_thin_plate_with_hole_cpp.md)
- [Contact and impact](contact_and_impact/contact_and_impact.md)
- [Euler beam in explicit mechanics](structural_elements/euler_beam_explicit.md)
- [Linear elastic fracture mechanics on a 2D plate with an inclined crack](fracture_mechanics/gtheta_example.md)

## General remarks about the test-files contents

In a C++ test-file (often named `main.cpp`),

> - Define the needed `include` and use the `namespace` manta before the `main`.
> - Set the constants and parameters (directly or by reading a json file with a `DataReader`).
> - Call to `init`.
> - Create a `Context` object
>   to manage error and other information messages.
> - Create a `ResourcesManager` object:
>   kind of "hub" to supervise the different objects needed for the computation (mesh, fields, formulations, ...).
> - Import (with `readAndPartition`) or generates a mesh.
> - Get some useful `MeshSet` with `getSet`.
> - Create objects needed for the simulation:
>   `NodeField`, `LinearSystem`, `Formulation`, `ConstraintSet` and loading.
> - Allocate the memory with the ResourcesManager `init` command (**obligatory step**).
> - Solve the problem with the appropriate method.
> - Make some post-treatment as writing the solution.
> - `finalize` and `return`
