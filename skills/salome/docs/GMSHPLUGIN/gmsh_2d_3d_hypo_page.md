<!-- source: https://docs.salome-platform.org/latest/gui/GMSHPLUGIN/gmsh_2d_3d_hypo_page.html -->

# Gmsh 2D and 3D hypotheses

**Gmsh Parameters** hypotheses work only with **Gmsh 2D** and **Gmsh 3D** algorithms. **Gmsh 2D** and **Gmsh 3D** algorithms do not require definition of lower-level hypotheses and algorithms (2D and 1D for meshing 3D objects and 1D for meshing 2D objects). **Gmsh 2D** and **Gmsh 3D** algorithms do support sub-meshes.

![Arguments.png](https://docs.salome-platform.org/latest/gui/GMSHPLUGIN/Arguments.png)

Dialog boxes of Gmsh 2D and Gmsh 3D algorithms.

The **Arguments tab** of the dialog boxes is very similar to the original  [**Gmsh**](https://gmsh.info)  GUI general mesh option tab. One familiar with the original interface can refer to the  [**Gmsh documentation**](http://www.geuz.org/gmsh/doc/texinfo/gmsh.html)  for more information. We briefly describe each argument of the **Arguments tab** and give the original corresponding Gmsh keyword (referring to  [**Gmsh Mesh options list**](http://www.geuz.org/gmsh/doc/texinfo/gmsh.html#Mesh-options-list)):

- **Name** - allows to define the name for the algorithm ("Gmsh Parameters" by default).
- **2D algorithm** - allows to choose the Gmsh 2D algorithm for both 2D and 3D meshes. Original corresponding Gmsh keyword is **"Mesh.Algorithm"**.
- **3D algorithm** - allows to choose the Gmsh 3D algorithm for 3D meshes. Original corresponding Gmsh keyword is **"Mesh.Algorithm3D"**.
- **Recombine all triangular meshes** - if this box is checked in, Gmsh will recombine triangles into quadrangles. Original corresponding Gmsh keyword is **"Mesh.RecombineAll"** (set to 1 if the box is checked in, else 0).
- **Subdivision algorithm** - allows to choose the subdivision algorithm. Original corresponding Gmsh keyword is **"Mesh.SubdivisionAlgorithm"**.
- **Remeshing algorithm** - allows to choose the remeshing algorithm. Original corresponding Gmsh keyword is **"Mesh.RemeshAlgorithm"**.
- **Remeshing parametrization** - allows to choose the remeshing parametrization. Original corresponding Gmsh keyword is **"Mesh.RemeshParametrization"**.
- **Smoothing steps** - number of steps to smooth the final mesh. Original corresponding Gmsh keyword is **"Mesh.Smoothing"**.
- **Element size factor** - factor used to linearly increase or decrease the default mesh size. Original corresponding Gmsh keyword is **"Mesh.MeshSizeFactor"**.
- **Elements per 2Pi radians** - number of mesh elements per 2 Pi radians. This helps defining a mesh size with respect to the curvature of the underlying geometry. Original corresponding Gmsh keyword is **"Mesh.MeshSizeFromCurvature"**.
- **Max. Size** - maximum linear dimensions for mesh cells. Original corresponding Gmsh keyword is **"Mesh.MeshSizeMax"**.
- **Min. Size** - minimum linear dimensions for mesh cells. Original corresponding Gmsh keyword is **"Mesh.MeshSizeMin"**.
- **Second Order** - if this box is checked in, the algorithm will create second order nodes on the mesh, which actually will become quadratic. Original corresponding Gmsh keyword is **"Mesh.ElementOrder"** (set to 2 if the box is checked in, else 1).
- **Use incomplete elements** - if this box is checked in (default), quadratic elements will be incomplete. For example a quadrangle will have 8 nodes if incomplete, 9 nodes if complete. See  [**Node ordering**](http://www.geuz.org/gmsh/doc/texinfo/gmsh.html#Node-ordering)  for more information. Be careful with the case of pyramids. Complete pyramids will have 14 nodes but there is no pyra14 available in smesh. The last node created by Gmsh will then be ignored and using complete element can lead to orphelin nodes. Original corresponding Gmsh keyword is **"Mesh.SecondOrderIncomplete"** (set to 1 if the box is checked in, else 0).

![Compounds.png](https://docs.salome-platform.org/latest/gui/GMSHPLUGIN/Compounds.png)

Compounds tab of the dialog boxes.

In the Compounds tab of the dialog boxes, it is possible to choose the following arguments:

- **Add** - allows to add geometrical defined groups of edges or groups of faces as compounds. Each group will be treated as a single entity during meshing. When meshed, the single entity will be reparametrized as a single surface, whose mesh can thus cross internal boundaries.
- **Remove** - deletes selected rows from the table.
