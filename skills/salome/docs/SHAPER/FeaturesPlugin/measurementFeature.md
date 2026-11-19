<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/FeaturesPlugin/measurementFeature.html -->

# Measurement

The feature **Measurement** calculates dimensions of sub-elements of a geometrical object (shape).

The measured dimension is displayed in the property panel and shown in 3D OCC viewer.

The properties of dimension text and line, such as font, color, arrow size, etc. can be defined in the Preferences [Visualization tab](../General/Introduction.md#visualization-preferences).

**Apply** button does not generate any result and has the same effect as **Cancel** for this feature.

To start Measurement in the active part:

1. select in the Main Menu *Part - > Measurement* item or
2. click ![measurement.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/measurement.png) **Measurement** button in the toolbar

The following dimensions can be calculated:

[![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/meas_length_32x32.png)](https://docs.salome-platform.org/latest/gui/SHAPER/_images/meas_length_32x32.png)

edge length

[![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/meas_distance_32x32.png)](https://docs.salome-platform.org/latest/gui/SHAPER/_images/meas_distance_32x32.png)

distance between objects

[![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/meas_radius_32x32.png)](https://docs.salome-platform.org/latest/gui/SHAPER/_images/meas_radius_32x32.png)

radius

[![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/meas_angle_32x32.png)](https://docs.salome-platform.org/latest/gui/SHAPER/_images/meas_angle_32x32.png)

angle between edges

[![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/meas_angle3p_32x32.png)](https://docs.salome-platform.org/latest/gui/SHAPER/_images/meas_angle3p_32x32.png)

angle by 3 points

---

## Edge length

The length can be measured for straight or curved edge built on two points.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Measurement1.png)

Edge length

Input fields:

- **Edge** contains edge to be measured selected in 3D OCC viewer or object browser.

Note, that for curved edges length is displayed only in the property panel.

**TUI Command**:

model.measureLength(*Part_doc*, *edge*)
:   Parameters:
    :   - **part** – The current part object.
        - **object** – An edge in format *model.selection(“EDGE”, edge)*.

    Returns:
    :   Calculated value.

## Distance between objects

**Distance between objects** calculates minimal distance for any pair of shapes: vertex, edge, face, solid.

> ![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Measurement2.png)
>
>
> Distance between objects

Input fields:

- **From**, **To** contain shapes between which distance is measured. Shapes are selected in 3D OCC viewer or object browser.

**TUI Command**:

model.measureDistance(*Part_doc*, *shape1*, *shape2*)
:   Parameters:
    :   - **part** – The current part object.
        - **object** – A first edge in format *model.selection(“EDGE”, edge)*.
        - **object** – A second edge in format *model.selection(“EDGE”, edge)*.

    Returns:
    :   Calculated value.

## Radius

**Radius** calculates radius for circular edge or cylindrical face.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Measurement3.png)

Radius

Input fields:

- **Object** contains shape to be measured selected in 3D OCC viewer or object browser.

**TUI Command**:

model.measureRadius(*Part_doc*, *shape*)
:   Parameters:
    :   - **part** – The current part object.
        - **object** – An edge in format *model.selection(“TYPE”, shape)*.

    Returns:
    :   Calculated value.

## Angle between edges

**Angle between edges** calculates angle between the selected pair of edges in the point of intersection. If there are several points of intersection, then angles are calculated in all points.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Measurement4.png)

Angle between edges

Input fields:

- **First Edge**, **Second edge** contain edges between which angle is measured. Edges are selected in 3D OCC viewer or object browser.

**TUI Command**:

model.measureAngle(*Part_doc*, *edge1*, *edge2*)
:   Parameters:
    :   - **part** – The current part object.
        - **object** – A first edge in format *model.selection(“TYPE”, shape)*.
        - **object** – A second edge in format *model.selection(“TYPE”, shape)*.

    Returns:
    :   Calculated value.

## Angle by 3 points

**Angle by 3 points** calculates angle between the selected three points. The second point is in the corner of the angle.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Measurement5.png)

Angle by 3 points

Input fields:

- **First point**, **Second point**, **Third point** contain point between which angle is measured. Points are selected in 3D OCC viewer or object browser.

**TUI Command**:

model.measureAngle(*Part_doc*, *vertex1*, *vertex2*, *vertex3*)
:   Parameters:
    :   - **part** – The current part object.
        - **object** – A first vertex in format *model.selection(“TYPE”, shape)*.
        - **object** – A second vertex in format *model.selection(“TYPE”, shape)*.
        - **object** – A third vertex in format *model.selection(“TYPE”, shape)*.

    Returns:
    :   Calculated value.
