<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/FeaturesPlugin/smashFeature.html -->

# Smash

Smash feature implements a boolean operation for smashing a set of main objects by a set of tool objects.

To create a Smash in the active part:

1. select in the Main Menu *Features - > Smash* item or
2. click [![bool_smash.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/bool_smash.png)](https://docs.salome-platform.org/latest/gui/SHAPER/_images/bool_smash.png) **Smash** button in the toolbar

The following property panel will be opened:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Smash.png)

**Smash operation**

- **Main Objects** contains a list of objects selected in the Object Browser or in the Viewer, which will be smashed by tool objects.
  If a subshape that belongs to a compsolid/compound was selected, other shapes of this compsolid/compound will be cut from
  other objects (to avoid self intersection) and added to the result.
- **Tool Objects** contains a list of objects selected in the Object Browser or in the Viewer, which will be smashed into main objects.
  If a subshape that belongs to a compsolid/compound was selected, other shapes of this compsolid/compound will be ignored.
- **Fuzzy Parameter** defines the additional tolerance value used to eliminate tiny results.
- **See preview** button shows a result of the operation.

Main objects and Tools objects should have the same dimension. There are supported 2-dimensional (face) or 3-dimensional (solid, compsolid) arguments.

**TUI Command**:

model.addSmash(*Part_doc*, *mainObjects*, *toolObjects*, *fuzzy*)
:   Parameters:
    :   - **part** – The current part object.
        - **list** – A list of main objects.
        - **list** – A list of tool objects.
        - **real** – Additional tolerance used to eliminate tiny results (optional).

    Returns:
    :   Rotated object.

## Result

The Result of the operation will be a shape which is a smash of tool objects from main objects:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/CreatedSmash.png)

**Smash created**

**See Also** a sample TUI Script of [Create Smash](TUI_smashFeature.md#tui-create-smash) operation.
