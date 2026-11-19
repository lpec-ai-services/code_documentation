<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/PartSetPlugin/PartSetPlugin.html -->

# Part plug-in

## New Part

To create a New Part:

1. select in the Main Menu *Part - > New part* item or
2. click ![new_part.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/new_part.png) **New part** button in Shaper toolbar:

**TUI Command**:

model.addPart(*partSet*)
:   Parameters:
    :   **part** – The current part object.

    Returns:
    :   Result object.

### Result

Created empty part is activated and appears in the object browser.

**See Also** a sample TUI Script of [Create Part](TUI_new_partFeature.md#tui-create-part) operation.

## Duplicate Part

To duplicate an active Part:

1. select in the Main Menu *Part - > Duplicate part* item or
2. click ![duplicate.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/duplicate.png) **Duplicate part** button in Shaper toolbar:

### Result

Created copied part is activated and appears in the object browser.

Copied part contains all objects existing in the source part.

## Remove Part

To remove an active Part:

1. select in the Main Menu *Part - > Remove part* item or
2. click ![remove.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/remove.png) **Remove part** button in Shaper toolbar:

### Result

Selected part is removed together with all its objects.

## Move Part

The part feature may be moved in the Object Browser by mouse Drag-and-Drop. For this user should
press mouse left button on a Part feature and move it up or down along the PartSet features, then release the mouse button
to put a moved part between other PartSet features.

The following conditions must be met:

- PartSet document must be active.
- No operation is started.
- The moved part(s) do not break order of depended objects.

Only enabled features could participate in the movement. If the history line arrow is located not in the end of the history
of features and the user moves the Part much lower than this arrow, the Part feature will be dropped just after the arrow
(the last active feature).
