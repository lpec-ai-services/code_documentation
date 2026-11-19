<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/SketchPlugin/SketchPlugin.html -->

# Sketch plug-in

Sketch plug-in includes features for creation of 2D shapes.

The sketch creation takes the following steps:

- definition of sketch plane;
- creation of sketch objects from scratch;
- generation of sketch objects via operations on the existing operations;
- definition of constraints.

Sketch can be created in the active part or in a partset (if there is no active part).

To create a Sketch:

1. select in the Main Menu *Sketch - > Sketch* item or
2. click ![SketchButton.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/SketchButton.png) **Sketch** button in Sketch toolbar:

First define a plane for the sketch:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/PlaneDefinition.png)

- specify plane size (equal to 25 in the example above);
- select the appropriate plane in the viewer.

Note that coordinate planes will be suggested for selection if no convenient objects for plane selection are displayed in the viewer:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/CoordinatePlanes.png)

After the plane for sketch is selected, the following property panel will be opened:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/SketchPanel.png)

Sketch general panel

- **Reversed** check box - allows reversing the sketch plane normal;
- **Set plane view** button - switches the viewer to the top view for the sketch plane;
- **Show geometrical constraints** check box - displays/hides geometrical constraints:
- **Show dimensional constraints** check box - displays/hides dimensional constraints;
- **Show existing expressions** check box - displays/hides expressions.
- **Show free points** check box - highlights free points in the current sketch if it is checked.
- **Automatic constraints** - automatically create horizontal or vertical constraints if angle between created line and horizontal or vertical less then angular tolerance (defined in preferences).
- **Change sketch plane** button - allows to change working plane of the current sketch.
- **Show remaining DoFs** button - highlights all sketch edges which are not fully constrained.

A window containing the specified constraints will also appear:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/ConstraintsBrowser.png)

Sketch constraints browser

**See** [Sketch Constraints Browser](sketchConstraintsBrowser.md#sketchconstraintsbrowsers)

Now it is possible to:

- create [sketch objects](#sketch-objects)
- create [constraints](#sketch-constraints)
- perform [sketch operations](#sketch-operations)

To apply or cancel sketch creation use Apply and Cancel buttons from the
Sketch panel as well as equivalent buttons from Sketch toolbar.

The Result of operation will be a COMPOUND. In the object tree, Result node is located in
**Constructions** folder.

The Name is assigned automatically: **Sketch_1**, **Sketch_2**, … both for Feature and Result.

**TUI Command**:

model.addSketch(*PartOrPartSet*, *plane*)
:   Parameters:
    :   - **part** – The current part object.
        - **object** – A plane.

    Returns:
    :   Result object.

## Sketch objects

The plug-in includes the following features for creation of 2D objects:

- [Point](pointFeature.md)
- [Line](lineFeature.md)
- [Rectangle](rectangleFeature.md)
- [Circle](circleFeature.md)
- [Arc](arcFeature.md)
- [Ellipse](ellipseFeature.md)
- [Elliptic Arc](arcEllipseFeature.md)
- [B-spline and periodic B-spline](bsplineFeature.md)
- [Curve Fitting](curveFittingFeature.md)

## Constraints

Constraints are available and viewable during sketch creation or editing.

The goal of constraints creation is to fix sketch geometry, i.e. set degrees of freedom to zero.

If all degrees of freedom are eliminated, the sketch is fixed and displayed with green color.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Sketch_fixed.png)

Fixed Sketch

If any degrees of freedom remain unsolved, the sketch is under-constrained and displayed with red color.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Sketch_underconstrained.png)

Underconstrained Sketch

The plug-in includes the following constraints:

- [Distance constraint](distanceFeature.md)
- [Horizontal distance constraint](horizontalDistFeature.md)
- [Vertical distance constraint](verticalDistFeature.md)
- [Length constraint](lengthFeature.md)
- [Angle constraint](angleFeature.md)
- [Radius constraint](radiusFeature.md)
- [Horizontal constraint](horizontalFeature.md)
- [Vertical constraint](verticalFeature.md)
- [Fixed constraint](fixedFeature.md)
- [Parallel constraint](parallelFeature.md)
- [Perpendicular constraint](perpendicularFeature.md)
- [Tangent constraint](tangentFeature.md)
- [Coincident constraint](coincedentFeature.md)
- [Middle point constraint](middleFeature.md)
- [Equal constraint](equalFeature.md)
- [Collinear constraint](collinearFeature.md)

## Overconstraned state

Sketcher comes into overconstrained state when an extra constraint was defined. The following picture shows an example of the overconstrained state:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Overconstrained.png)

Overconstrained Sketch

When Sketcher gets this state then:

- buttons Apply and Cancel for the whole Sketcher are blocked;
- a constraint which causes the overconstraint state is highlightid by red color;
- a warning message in sketcher Property Panel is shown with recomendation what to do in this case;
- an additional Undo button is shown under the warning messages;

After undoing the last operation or deletion of a conflicting constraint Sketcher will be reverted into a normal state.

## Operations

Operations modify existing features of the sketch or create new ones by copying them.

The plug-in includes the following operations:

- [Fillet](filletFeature.md)
- [Split](splitFeature.md)
- [Trim](trimFeature.md)
- [Projection](projectionFeature.md)
- [Intersection](intersectionFeature.md)
- [Mirror copy](mirrorFeature.md)
- [Linear copy](translationFeature.md)
- [Angular copy](rotationFeature.md)
- [Offset](offsetFeature.md)
- [Sketch Drawer](sketchDrawer.md)
- [Sketch Copy](sketchCopy.md)
