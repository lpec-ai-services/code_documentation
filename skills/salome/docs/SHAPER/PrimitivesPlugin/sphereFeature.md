<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/PrimitivesPlugin/sphereFeature.html -->

# Sphere

Sphere feature creates a sphere solid or a part of a sphere solid.

To create a Sphere in the active part:

1. select in the Main Menu *Primitives - > Sphere* item or
2. click ![Sphere_button.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Sphere_button.png) **Sphere** button in the toolbar

There are 2 algorithms for creation of a Sphere

[![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/sphere_32x32.png)](https://docs.salome-platform.org/latest/gui/SHAPER/_images/sphere_32x32.png)

**By a center and a radius**

[![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/sphere_part_32x32.png)](https://docs.salome-platform.org/latest/gui/SHAPER/_images/sphere_part_32x32.png)

**By radii (inner and outer) and angle limits (theta and phi)**

---

## By a center and a radius

Sphere is created by a center (origin by default) and a radius.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Sphere_full.png)

Input fields:

- **Point** defines the center of the sphere selected in 3D OCC viewer or object browser;
- **Radius** defines the radius.

**TUI Command**:

model.addSphere(*Part_doc*, *Point*, *Radius*)
:   Parameters:
    :   - **part** – The current part object.
        - **object** – Vertex.
        - **real** – Radius.

    Returns:
    :   Result object.

### Result

A solid sphere based on the origin and a radius.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Sphere1.png)

**See Also** a sample TUI Script of a [Create Sphere](TUI_sphereFeature.md#tui-create-sphere) operation.

## By radii (inner and outer) and angle limits (theta and phi)

Part of sphere is created by radii (inner and outer) and angle limits (phi and theta).

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Sphere_part.png)

Input fields:

- **RMin** defines the inner radius;
- **RMax** defines the outer radius;
- **PhiMin** defines the lower phi limit;
- **PhiMax** defines the higher phi limit;
- **ThetaMin** defines the lower theta limit;
- **ThetaMax** defines the higher theta limit.

**TUI Command**:

model.addSphere(*Part_doc*, *RMin*, *RMax*, *PhiMin*, *PhiMax*, *ThetaMin*, *ThetaMax*)
:   Parameters:
    :   - **part** – The current part object.
        - **real** – Inner radius.
        - **real** – Outer radius.
        - **real** – Lower phi.
        - **real** – Hiher phi.
        - **real** – Lower theta.
        - **real** – Hiher theta.

    Returns:
    :   Result object.

### Result

A solid sphere based on the origin with radii (inner and outer) and angles (phi and theta).

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Sphere2.png)

**See Also** a sample TUI Script of a [Create Part of sphere](TUI_spherePart.md#tui-create-part-sphere) operation.
