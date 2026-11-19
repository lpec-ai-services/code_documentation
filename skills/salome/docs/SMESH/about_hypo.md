<!-- source: https://docs.salome-platform.org/latest/gui/SMESH/about_hypo.html -->

# About Hypotheses

**Hypotheses** represent boundary conditions which will be taken into account by meshing algorithms. The hypotheses allow you to manage the level of detail of the resulting mesh: when applying different hypotheses with different parameters you can preset the quantity or size of elements which will compose your mesh. So, it will be possible to generate a coarse or a more refined mesh.

The choice of a hypothesis depends on the selected algorithm.

Hypotheses are created during creation and edition of
[meshes](constructing_meshes.md#constructing-meshes-page) and [sub-meshes](constructing_submeshes.md#constructing-submeshes-page).
Once created a hypotheses can be reused during creation and edition of other meshes and sub-meshes. All created hypotheses and algorithms are present in the Object Browser in *Hypotheses* and *Algorithms* folders correspondingly. It is possible to open a dialog to modify the parameters of a hypothesis from its context menu. This menu also provides **Unassign** command that will unassign the hypothesis from all meshes and sub-meshes using it. Modification of any parameter of a hypothesis and its unassignment leads to automatic removal of elements generated using it.

In **MESH** there are:

- a1d_meshing_hypo_page for meshing of **edges**
- [2D Meshing Hypotheses](2d_meshing_hypo.md#a2d-meshing-hypo-page) for meshing of **faces**
- [3D Meshing Hypotheses](3d_meshing_hypo.md#a3d-meshing-hypo-page) for meshing of **volumes**
- [Additional Hypotheses](additional_hypo.md#additional-hypo-page)

**Table of Contents**

- [1D Meshing Hypotheses](1d_meshing_hypo.md)
  - [Adaptive hypothesis](1d_meshing_hypo.md#adaptive-hypothesis)
  - [Arithmetic Progression hypothesis](1d_meshing_hypo.md#arithmetic-progression-hypothesis)
  - [Geometric Progression hypothesis](1d_meshing_hypo.md#geometric-progression-hypothesis)
  - [Deflection hypothesis](1d_meshing_hypo.md#deflection-hypothesis)
  - [Local Length hypothesis](1d_meshing_hypo.md#local-length-hypothesis)
  - [Max Size](1d_meshing_hypo.md#max-size)
  - [Number of Segments hypothesis](1d_meshing_hypo.md#number-of-segments-hypothesis)
  - [Start and End Length hypothesis](1d_meshing_hypo.md#start-and-end-length-hypothesis)
  - [Automatic Length](1d_meshing_hypo.md#automatic-length)
  - [Fixed Points hypothesis](1d_meshing_hypo.md#fixed-points-hypothesis)
  - [Reversed Edges Helper](1d_meshing_hypo.md#reversed-edges-helper)
- [2D Meshing Hypotheses](2d_meshing_hypo.md)
  - [Max Element Area](2d_meshing_hypo.md#max-element-area)
  - [Length from Edges](2d_meshing_hypo.md#length-from-edges)
  - [Quadrangle parameters](2d_meshing_hypo.md#quadrangle-parameters)
- [3D Meshing Hypotheses](3d_meshing_hypo.md)
  - [Max Element Volume hypothesis](3d_meshing_hypo.md#max-element-volume-hypothesis)
  - [Renumber hypothesis](3d_meshing_hypo.md#renumber-hypothesis)
- [Additional Hypotheses](additional_hypo.md)
  - [Propagation of 1D Hypothesis on opposite edges](additional_hypo.md#propagation-of-1d-hypothesis-on-opposite-edges)
  - [Propagation of Node Distribution on Opposite Edges](additional_hypo.md#propagation-of-node-distribution-on-opposite-edges)
  - [Viscous Layers and Viscous Layers 2D](additional_hypo.md#viscous-layers-and-viscous-layers-2d)
  - [Viscous Layers API](additional_hypo.md#viscous-layers-api)
  - [Quadratic Mesh](additional_hypo.md#quadratic-mesh)
  - [Quadrangle Preference](additional_hypo.md#quadrangle-preference)
