<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/post_processings/vtk_output.html -->

# VTK output

By now exists an historical VTK writer for paraview post-treatment.

Examples of use of this writer can be found in many tests and examples
like the commented one [2D linear elastic thin plate with a hole in tension in c++](../../demos/components_examples/elasticity/2D_elastic_thin_plate_with_hole_cpp.md#example-2d-elastic-thin-plate-with-hole-components).

The major drawback is the need to define a PostFormulation which supports the solution NodeField.

Each formulation results in a VTK block, which has the following consequences:

1. In paraview, the filter ExtractBlock must always be use as a first step of post-treatment.
2. It is not possible to easily mix nodal and cell fields.
   For example, it is not possible to plot the isovalue of stresses
   on a mesh wrapped by a vector equal to n times the displacement (amplification).

Future developments will concern med export which will permit the visualization of results in Salome/Paravis software.
