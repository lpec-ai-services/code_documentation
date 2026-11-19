<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/multi_translation_operation_page.html -->

# Multi Translation

To produce a **Multi Translation** in the **Main Menu** select **Operations - > Transformation - > Multi Translation**

This operation makes several translations of a shape in **one** or **two** directions.   
The **Result** will be one **GEOM_Object** (compound). The total number of shape copies in the resulting compound will be equal to:

- in case of [Simple multi translation](multi_translation_operation_page.md#single_multi_translation): *NbTimes* (if *NbTimes* parameter is equal to 1, the result will contain only the initial non-translated shape).
- in case of [Double multi translation](multi_translation_operation_page.md#double_multi_translation): *NbTimes1* x *NbTimes2* (if *NbTimes1* and *NbTimes2* parameters are both equal to 1, the result will contain a single non-translated initial shape).

In case of **Simple Multi Translation** the object is translated in one direction.

![mtrans1.png](https://docs.salome-platform.org/latest/gui/GEOM/mtrans1.png)

The following parameters and options can be defined in this dialog:

- **Result Name**;
- **Main Object**  to be translated;
- **Vector** of translation (DX by default). If a curve has been selected instead of the Vector, only its first and last vertices will be used to get the vector direction and the dialog preview will display the vector along which the object will be translated;
- **Step** is the distance between the shape copies;
- **Nb. Times** is the number of shape copies;
- **Reverse Direction**  checkbox allows changing the direction of translation;
- [Advanced options](restore_presentation_parameters_page.md).

![multi_translation_initialsn.png](https://docs.salome-platform.org/latest/gui/GEOM/multi_translation_initialsn.png)

The initial object

![multi_translation1dsn.png](https://docs.salome-platform.org/latest/gui/GEOM/multi_translation1dsn.png)

The result of a simple multi-translation

**TUI Command:** *geompy.MakeMultiTranslation1D(Shape, Dir, Step, NbTimes)*   
**Arguments:** Name + 1 shape + 1 vector (for direction) + 1 step value + 1 value (repetition).

In case of **Double Multi Translation** the object is translated in two directions.

![mtrans2.png](https://docs.salome-platform.org/latest/gui/GEOM/mtrans2.png)

The following parameters and options can be defined in this dialog:

- **Result Name**;
- **Main Object**  to be translated;
- **Vector U/V** of translation (DX and DY by default). If a curve has been selected instead of the Vector, only its first and last vertices will be used to get the vector direction and the dialog preview will display the vector along which the object will be translated;
- **Step U/V** is the distance between the shape copies;
- **Nb. Times U/V** is the number of shape copies;
- **Reverse U/V**  checkbox allows changing the direction of translation;
- [Advanced options](restore_presentation_parameters_page.md).

![multi_translation_initialsn.png](https://docs.salome-platform.org/latest/gui/GEOM/multi_translation_initialsn.png)

The initial object

![multi_translation2dsn.png](https://docs.salome-platform.org/latest/gui/GEOM/multi_translation2dsn.png)

The result of a double multi-translation

**TUI Command:** *geompy.MakeMultiTranslation2D(Shape, Dir1, Step1, NbTimes1, Dir2, Step2, NbTimes2),* where *Shape* is a shape to be translated, *Dir1* is the first direction of translation, *Step1* of the first translation, *NbTimes1* is a number of translations to be done along *Dir1*, *Dir2* is the second direction of translation, *Step2* of the second translation, *NbTimes2* is a number of translations to be done along *Dir2*.   
**Arguments:** Name + 1 shape + 2 vectors defining the direction

- 2 step values + 2 values (repetitions).

Our **TUI Scripts** provide you with useful examples of the use of [Transformation Operations](tui_transformation_operations_page.md#tui_multi_translation).
