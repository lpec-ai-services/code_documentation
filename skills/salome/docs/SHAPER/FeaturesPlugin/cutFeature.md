<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/FeaturesPlugin/cutFeature.html -->

# Cut

Cut feature implements a Boolean operation to cut tool objects from main objects.

To perform a Cut operationin the active part:

1. select in the Main Menu *Features - > Cut* item or
2. click [![bool_cut.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/bool_cut.png)](https://docs.salome-platform.org/latest/gui/SHAPER/_images/bool_cut.png) **Cut** button in the toolbar

The following property panel will be opened:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/boolean_cut_property_panel.png)

**Cut operation**

- **Main Objects** contains a list of objects selected in the Object Browser or in the Viewer, which will be cut by tool objects.
  Any kind of shape can be selected, including subshapes of compsolids/compounds.
  In this case only selected subshapes will be cut, others will stay untouched (as much as possible).
- **Tool Objects** contains a list of objects selected in the Object Browser or in the Viewer, which will cut main objects.
  Any kind of shape can be selected, including subshapes of compsolids/compounds.
  Non-selected subshapes from compsolids/compounds will be ignored.
- **Fuzzy Parameter** defines the additional tolerance value used to eliminate tiny results.
- **See preview** button shows a result of the operation.

The minimal dimension of Tool Objects should be not less than the maximal dimension of Main Objects.

**TUI Command**:

model.addCut(*Part_doc*, *mainObjects*, *toolObjects*, *fuzzy*)
:   Parameters:
    :   - **part** – The current part object
        - **list** – A list of main objects.
        - **list** – A list of tool objects.
        - **real** – Additional tolerance used to eliminate tiny results (optional).

    Returns:
    :   Created object

## Result

A result shape which is a cut by tool objects from main object, will be produced for each selected object:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/CreatedCut.png)

**Created cut**

If a subsolid (yellow wireframe) of a compsolid was selected:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/boolean_cut_subsolids_arguments.png)

**Cut arguments**

it will be cut in the result and not selected subsolids will be added to it:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/boolean_cut_subsolids_result.png)

**Cut subsolid result**

**See Also** a sample TUI Script of [Create Cut](TUI_cutFeature.md#tui-create-cut) operation.
