<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/FeaturesPlugin/filletFeature.html -->

# Fillet

**Fillet** feature creates fillets on the edges of a shape.

To create a Fillet in the active part:

1. select in the Main Menu *Feature - > Fillet* item or
2. click ![fillet.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/fillet.png) **Fillet** button in the toolbar

There are 2 types of fillet:

[![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/fillet_fixed_radius.png)](https://docs.salome-platform.org/latest/gui/SHAPER/_images/fillet_fixed_radius.png)

fillet by fixed radius

[![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/fillet_var_radius.png)](https://docs.salome-platform.org/latest/gui/SHAPER/_images/fillet_var_radius.png)

fillet by variable radius

---

## Fillet by fixed radius

The property panel is shown below.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/FilletFixed.png)

Fillet by fixed radius property panel

Input fields:

- **Faces or/and edges** panel contains filleted faces and edges. All edges of a face are subject to fillet operation. Faces and edges are selected in 3D OCC viewer;
- **Radius** defines fillet radius.

**TUI Command**:

model.addFillet(*Part_doc*, [*face*, *edge*, ]*radius*)
:   Parameters:
    :   - **part** – The current part object.
        - **list** – A list of faces and edges subject to fillet operation in format *model.selection(TYPE, shape)*.
        - **number** – Radius value.

    Returns:
    :   Created object.

### Result

Result of **Fillet by fixed radius** is shown below.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/fillet_fix_rad.png)

Fillet by fixed radius

**See Also** a sample TUI Script of [Create Fillet by fixed radius](TUI_filletfixedFeature.md#tui-create-fillet1) operation.

## Fillet by variable radius

Alternatively, there is a possibility to create a fillet with a variable radius.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/FilletVarious.png)

Fillet by variable radius

Input fields:

- **Faces or/and edges** panel contains filleted faces and edges. All edges of a face are subject to fillet operation. Faces and edges are selected in 3D OCC viewer;
- **Start radius** defines the fillet radius at the start of the selected edge(s);
- **End radius** defines the fillet radius at the end of the selected edge(s).

**TUI Command**:

model.addFillet(*Part_doc*, *shapes*, *R1*, *R2*)
:   Parameters:
    :   - **Part_doc** (*document*) – The current part object.
        - **shapes** (*list*) – A list of faces and edges subject to fillet operation in format *model.selection(TYPE, shape)*.
        - **R1** (*double*) – Start radius value.
        - **R2** (*double*) – End radius value.

    Returns:
    :   Created object.

### Result

Result of **Fillet by variable radius** is shown below.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/fillet_var_rad.png)

Fillet by variable radius

**See Also** a sample TUI Script of [Create Fillet by variable radius](TUI_filletvariableFeature.md#tui-create-fillet2) operation.
