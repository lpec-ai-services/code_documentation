<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/FeaturesPlugin/pipeFeature.html -->

# Pipe

**Pipe** feature makes an extruded Pipe shape.

To create a Pipe in the active part:

1. select in the Main Menu *Features - > Pipe* item or
2. click ![pipe.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/pipe.png) **Pipe** button in the toolbar

Pipe can be created in three different ways:

[![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/pipe_simple_32x32.png)](https://docs.salome-platform.org/latest/gui/SHAPER/_images/pipe_simple_32x32.png)

by object and path

[![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/pipe_binormal_32x32.png)](https://docs.salome-platform.org/latest/gui/SHAPER/_images/pipe_binormal_32x32.png)

by object, path and Bi-normal

[![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/pipe_locations_32x32.png)](https://docs.salome-platform.org/latest/gui/SHAPER/_images/pipe_locations_32x32.png)

by object, path and locations

---

## Pipe by object and path

Base Objects are extruded along the Path Object so that the angle between the normal vector to the base shape and the tangent to the path remain constant at any point of the given path.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Pipe1.png)

Pipe by object and path property panel

Input fields:

- **Base objects** panel contains shapes to be extruded. Several Base Objects generate several pipes. Shapes (edges, faces, shells) are selected in 3D OCC viewer or object browser;
- **Path object** defines the path along which the Base Object will be extruded. **Path object** (edge or wire) is selected in 3D OCC viewer or object browser;

**TUI Command**:

model.addPipe(*Part_doc*, [*shape*, ]*path*)
:   Parameters:
    :   - **part** – The current part object.
        - **list** – A list of shapes in format *model.selection(TYPE, shape)*.
        - **object** – A path in format *model.selection(TYPE, shape)*.

    Returns:
    :   Created object.

### Result

Result of extrusion of an arc along another arc.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/simplePipe.png)

Pipe by object and path

**See Also** a sample TUI Script of ref:tui_simple_pipe operation.

## Pipe by object, path and Bi-normal

The pipe is generated to preserve the constant angle between the normal vector to the base shape and the BiNormal vector at any point of the given path.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Pipe2.png)

Pipe by object, path and Bi-normal property panel

Input fields:

- **Base objects** panel contains shapes to be extruded. Several Base Objects generate several pipes. Shapes (edges, faces, shells) are selected in 3D OCC viewer or object browser;
- **Path object** defines the path along which the Base Object will be extruded. **Path object** (edge or wire) is selected in 3D OCC viewer or object browser;
- **Bi-Normal** defines the BiNormal Vector. **Bi-Normal** (edge or wire) is selected in 3D OCC viewer or object browser.

**TUI Command**:

model.addPipe(*Part_doc*, [*shape*, ]*path*, *binormal*)
:   Parameters:
    :   - **part** – The current part object.
        - **list** – A list of shapes in format *model.selection(TYPE, shape)*.
        - **object** – A path in format *model.selection(TYPE, shape)*.
        - **object** – A binormal in format *model.selection(TYPE, shape)*.

    Returns:
    :   Created object.

### Result

Result of extrusion of a rectangular face along arc.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/binormalPipe.png)

Pipe by object, path and Bi-normal

**See Also** a sample TUI Script of [Pipe by object, path and Bi-normal](TUI_pipebinormalFeature.md#tui-binormal-pipe) operation.

## Pipe by object, path and locations

The pipe is generated to preserve selected profiles at the specified locations along the path.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Pipe3.png)

Pipe by object, path and locations property panel

Input fields:

- **Base objects** panel contains shapes to be extruded. Shapes (edges, faces, shells) are selected in 3D OCC viewer or object browser;
- **Path object** defines the path along which the Base Object will be extruded. **Path object** (edge or wire) is selected in 3D OCC viewer or object browser;
- **Locations** define the list of vertices that specify the locations of extruded Base Objects on the resulting Path Object. The number of Base Objects should be equal to the number of Locations.

**TUI Command**:

model.addPipe(*Part_doc*, [*shape*, ]*path*, *locations*)
:   Parameters:
    :   - **part** – The current part object.
        - **list** – A list of shapes in format *model.selection(TYPE, shape)*.
        - **object** – A path in format *model.selection(TYPE, shape)*.
        - **list** – A list of locations in format *model.selection(TYPE, shape)*.

    Returns:
    :   Created object.

### Result

Result of extrusion of 3 circles along arc with specified locations.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/locationPipe.png)

Pipe by object, path and locations

**See Also** a sample TUI Script of [Pipe by object, path and locations](TUI_pipelocationsFeature.md#tui-locations-pipe) operation.
