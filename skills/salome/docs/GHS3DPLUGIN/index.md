<!-- source: https://docs.salome-platform.org/latest/gui/GHS3DPLUGIN/index.html -->

# Introduction to MG-Tetra plug-in

MG-Tetra plug-in adds two meshing algorithm to the SALOME Mesh:  **MG-Tetra or MG-Tetra HPC** (former GHS3D) and **MG-Tetra Optimization**.

**MG-Tetra or MG-Tetra HPC** meshing algorithm is destined for:

- Meshing 3D geometric entities: solids are split into tetrahedral (pyramidal) elements.
- Generating 3D meshes from 2D meshes (triangles and quadrangles), working without geometrical objects.

**MG-Tetra Optimization** algorithm optimizes linear tetrahedral meshes not based on geometry.

- To be able to optimize a mesh generated on geometry, copy this mesh (menu **Mesh > Copy Mesh**) and assign MG-Tetra Optimization algorithm to the new mesh in **Edit Mesh** dialog.
- To re-optimize a just optimized mesh, invoke **Clear Mesh Data** command and then **Compute** the mesh again.

Note
:   MG-Tetra plug-in uses MG-Tetra commercial mesher and requires a license to be used within the Mesh module. To obtain a license, visit <http://www.meshgems.com/meshgems-products.html>

To manage parameters of the MG-Tetra mesher use [MG-Tetra Parameters hypothesis](ghs3d_hypo_page.md) and [Additional Hypotheses](additional_hypo_page.md). Parameters of MG-Tetra Optimization can be managed via [MG-Tetra Optimization Parameters hypothesis](optimization_page.md).

Also all MG-Tetra functionalities are accessible via [MG-Tetra Python interface](ghs3dplugin_python_interface_page.md).

![image2.gif](https://docs.salome-platform.org/latest/gui/GHS3DPLUGIN/image2.gif)

Example of a tetrahedral 3D mesh
