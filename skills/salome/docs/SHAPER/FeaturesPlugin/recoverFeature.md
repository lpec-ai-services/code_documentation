<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/FeaturesPlugin/recoverFeature.html -->

# Recover

**Recover** feature restores some objects used in previous operations.

To recover in the active part:

1. select in the Main Menu *Features - > Recover* item or
2. click ![recover.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/recover.png) **Recover** button in the toolbar or
3. click ![recover.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/recover.png) **Recover** command in the context menu if one feature is selected in the Object Browser

The feature has the following options:

[![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/recover_default_32x32.png)](https://docs.salome-platform.org/latest/gui/SHAPER/_images/recover_default_32x32.png)

restore only the objects used in the operation

[![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/recover_compound_32x32.png)](https://docs.salome-platform.org/latest/gui/SHAPER/_images/recover_compound_32x32.png)

restore full compound/compsolid if the operation used one or more of its sub-shapes

---

## Recover objects

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/recover_mode_default.png)

Recover objects used in operation

- **Feature** field contains one of the previous operations;
- **List of recovered** objects contains all the shapes used in the operation. Need to enable checkbox to restore a shape.

**TUI Command**:

model.addRecover(*Part_doc*, *feature*[, *recovering_results*])
:   Parameters:
    :   - **part** – The current part object.
        - **string** – The name of the feature.
        - **list** – A list of results used in the feature.

    Returns:
    :   Created object.

### Result

Result of restoring the shape used in Split operation in compsolid is a single solid.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/recover_res_default.png)

Recover a solid

**See also** a sample TUI script of ref:tui_recover_default operation.

## Recover top-level objects

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/recover_mode_compound.png)

Recover top-level compounds/compsolids of objects used in operation

- **Feature** field contains one of the previous operations;
- **List of recovered** objects contains all top-level shapes (compounds/compsolids) of the shapes used in the operation. Need to enable checkbox to restore a shape.

**TUI Command**:

model.addRecover(*Part_doc*, *feature*, [*recovering_results*, ]*True*)
:   Parameters:
    :   - **part** – The current part object.
        - **string** – The name of the feature.
        - **list** – A list of results used in the feature.
        - **boolean** – *True* to specify restoring compounds.

    Returns:
    :   Created object.

### Result

Result of restoring the shape used in Split operation in compsolid is a full compsolid.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/recover_res_compound.png)

Recover a compsolid

**See also** a sample TUI script of ref:tui_recover_compound operation.
