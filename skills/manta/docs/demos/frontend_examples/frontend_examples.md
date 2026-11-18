<!-- source: https://manta-project.gitlab.io/manta/demos/frontend_examples/frontend_examples.html -->

# Commented examples in pyManta

This section contains commented examples of the frontend layer of MANTA,
the PyManta layer to be used with python.

Here is a list of all available commented example to this date:

commented Manta examples with python

- [2D linear elastic thin plate with a hole in tension in python](elasticity/2D_elastic_thin_plate_with_hole_python.md)
- [Heat transfer in solid material](solid_heat_transfer/solid_heat_transfer.md)
- [Non linear behaviour](non_linear_behaviour/non_linear_behaviour.md)
- [Damage and fracture mechanics modelling](damage_and_fracture/damage_and_fracture.md)
- [Numerical analysis](numerical_analysis/numerical_analysis.md)

## General remarks about the test-files contents

In a python test-file, using manta implies (see Section [Main concepts](../../manta_frontend_user_guide/main_concepts.md#main-concepts)):

> - `import manta`
> - Declaring the physical system.
> - Creating the models and attach bricks definining the materials and the boundary conditions
> - Declaring the material properties
> - Declaring the loadings and loadings evolutions
> - Declaring and running the simulation
