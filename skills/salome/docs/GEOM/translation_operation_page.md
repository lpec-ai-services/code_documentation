<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/translation_operation_page.html -->

# Translation

To produce a **Translation** in the **Main Menu** select **Operations - > Transformation - > Translation**

This Operation makes a translation of an **Object**. To translate a shape you need to define the base shape and the coordinates of the vector of translation.   
**Create a copy** checkbox allows to keep the initial object, otherwise it will be removed.   
[Advanced options](restore_presentation_parameters_page.md).   
The **Result** of all operations will be any **GEOM_Object**.

The **Vector** of translation can be defined in three different ways selectable using the radio buttons.

Firstly you can define the **Vector** by coordinates along the axes.   
**TUI Command:** *geompy.MakeTranslation(Shape, DX, DY, DZ),* where Shape is a shape to be translated, DX, DY, DZ are components of translation vector.   
**Arguments:** Name + one or several objects + 3 values (coordinates).

![transformation1.png](https://docs.salome-platform.org/latest/gui/GEOM/transformation1.png)

Secondly you can define the **Vector** by the start and the end points.   
**TUI Command:** *geompy.MakeTranslationTwoPoints(Object, Point1, Point2)*   
**Arguments:** Name + one or several objects + 2 vertices

![transformation2.png](https://docs.salome-platform.org/latest/gui/GEOM/transformation2.png)

Finally you can define the **Vector** explicitly. The **Object** will be translated by the length of the vector. If a curve has been selected instead of the vector, only its first and last vertices will be used to get the vector direction and the dialog preview will display the vector along which the object will be translated.   
**Activate Distance** checkbox and **Distance** field allow defining a custom distance of translation.

**TUI Command:** for translation by vector: *geompy.MakeTranslationVector(Object, Vector)*   
**TUI Command**  for translation by vector and a custom distance: *geompy.MakeTranslationVectorDistance(Object, Vector, Distance)*   
**Arguments:** Name + one or several objects + 1 vector.

![transformation3.png](https://docs.salome-platform.org/latest/gui/GEOM/transformation3.png)

**Example:**

![translationsn1.png](https://docs.salome-platform.org/latest/gui/GEOM/translationsn1.png)

The initial shape (grey)

![translationsn2.png](https://docs.salome-platform.org/latest/gui/GEOM/translationsn2.png)

The resulting shape (yellow)

Our **TUI Scripts** provide you with useful examples of the use of [Transformation Operations](tui_transformation_operations_page.md#tui_translation).
