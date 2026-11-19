<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/FeaturesPlugin/partitionFeature.html -->

# Partition

Partition feature implements a boolean operation for partitioning of a set of selected objects.

To perform a Partition in the active part:

1. select in the Main Menu *Features - > Partition* item or
2. click ![partition_btn.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/partition_btn.png) **Partition** button in the toolbar

The following property panel will be opened:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Partition.png)

**Partition operation**

**Base Objects** contains a list of objects selected in the Object Browser or in the Viewer,
which will be partitioned. Construction planes are allowed too if at least one non-construction
entity is selected.

**Fuzzy Parameter** defines the additional tolerance value used to eliminate tiny results.

**TUI Command**:

model.addPartition(*Part_doc*, *objects*, *fuzzy*)
:   Parameters:
    :   - **part** – The current part object.
        - **object** – A list of objects.
        - **real** – Additional tolerance used to eliminate tiny results (optional).

    Returns:
    :   Created object.

## Result

The Result of the operation will be a shape which is a partition of selected objects:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/CreatedPartition.png)

**Partition created**

**See Also** a sample TUI Script of [Create Partition](TUI_partitionFeature.md#tui-create-partition) operation.
