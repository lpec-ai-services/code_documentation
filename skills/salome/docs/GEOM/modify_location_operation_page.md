<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/modify_location_operation_page.html -->

# Modify the Location

To **Modify the Location** in the **Main Menu** select **Operations - > Transformation - > Modify the Location**.

This operation modifies the **Location** of **Objects**.

The first algorithm places the **Object(s)** so that its center coincides with the origin of the **Local Coordinate System**.   
**Create a copy** checkbox allows to keep the initial objects, otherwise they will be removed.   
**Arguments:** Name + one or several objects + End Coordinate System.   
[Advanced options](restore_presentation_parameters_page.md).

![transformation5.png](https://docs.salome-platform.org/latest/gui/GEOM/transformation5.png)

In the picture the initial cube with the global coordinate system is to the right and the modified cube with the Local Coordinate System in the center of it is to the left .

![image30.png](https://docs.salome-platform.org/latest/gui/GEOM/image30.png)

The second algorithm modifies the location of the **Object(s)** using **Start** and **End** **LCS**, although the final position of the object will not coincide with the center of either of the two systems. In this method the object is shifted from its initial position by the value of the remainder after subtraction of the coordinates of the **Start LCS** from the coordinates of the **End LCS**.   
**Create a copy** checkbox allows to keep the initial object, otherwise it will be removed.   
**Arguments:** Name + one or several objects + Start Coordinate System + End Coordinate System.   
[Advanced options](restore_presentation_parameters_page.md).

![transformation6.png](https://docs.salome-platform.org/latest/gui/GEOM/transformation6.png)

In this picture we see the initial cube with the global coordinate system and two LCS: LocalCS1 (GCS+100 along x-axis) and LocalCS2 (GCS+200 along x-axis)

![image1.png](https://docs.salome-platform.org/latest/gui/GEOM/image1.png)

Selecting Start LCS = LCS1 and End LCS = LCS2, we obtain the translated cube at the position (100;0;0)

![image21.png](https://docs.salome-platform.org/latest/gui/GEOM/image21.png)

Selecting Start LCS = LCS2 and End LCS = LCS1, we obtain the translated cube at the position (-100;0;0)

![image4.png](https://docs.salome-platform.org/latest/gui/GEOM/image4.png)

The third algorithm modifies the location of the **Object(s)** using the **Path object** (Wire or Edge) and the **Distance** parameter (ranging from 0 to 1) defining how far the object will move along the path.   
**Create a copy** checkbox allows to keep the initial object, otherwise it will be removed.   
**Select Unpublished edges** checkbox allows to select sub-shape edges on the other objects.   
**Reverse Direction** checkbox allows to REVERSE the direction of the object movement along its path.

**Arguments:** Name + one or several objects + Translation path.   
[Advanced options](restore_presentation_parameters_page.md).

![transformation13.png](https://docs.salome-platform.org/latest/gui/GEOM/transformation13.png)

![transformation12.png](https://docs.salome-platform.org/latest/gui/GEOM/transformation12.png)

![transformation14.png](https://docs.salome-platform.org/latest/gui/GEOM/transformation14.png)

**TUI Command:** *geompy.MakePosition(theObject, theStartLCS, theEndLCS),* where *theObject* is a shape, location of which is modified, *theStartLCS* is a location to move the shape from, *theEndLCS* is a location to move the shape to.

Our **TUI Scripts** provide you with useful examples of the use of [Transformation Operations](tui_transformation_operations_page.md#tui_modify_location).
