<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/material_page.html -->

# Material

- [General Description](material_page.md#material_general_description_anchor)
- [OpenGL lighting model](material_page.md#material_opengl_model_anchor)
- [Materials library](material_page.md#material_lib_anchor)
- [Material properties](material_page.md#material_anchor)

## General description

Note
:   The functionality related to the material properties is **experimental**, so it might work not as expected. The behavior might be changed in the future versions of SALOME Geometry module.

You can change the material properties of the selected shape(s) in the context menu dialog. The layout of context menu can be customized via "Show predefined materials in popup menu" preferences option. If this option is switched off, only "Material properties" item will be shown in the popup menu. If this option is on (by default), "Material
properties" item in the popup menu will open a sub-menu with a list of predefined materials:

![hide_predef_material.png](https://docs.salome-platform.org/latest/gui/GEOM/hide_predef_material.png)

*"Show predefined materials in popup menu" option is switched off*

![show_predef_material.png](https://docs.salome-platform.org/latest/gui/GEOM/show_predef_material.png)

*"Show predefined materials in popup menu" option is switched on*

The **Custom** item from this list allows defining [Material properties](material_page.md#material_anchor), including the creation of a custom material.

It is also possible to define custom materials in the [Materials library](material_page.md#material_lib_anchor) dialog available from the main menu via **Tools > Materials library** .

Note
:   This functionality works in both OCC and VTK 3D viewers. However, due to the differences between underlying API of OCC and VTK libraries, the behavior of the functionality related to the materials is different:

    - shape presentation in OCC and VTK viewers is not fully identical;
    - some material attributes can affect the presentation in a different way.

## OpenGL lighting model

The material is specified by several attributes of the lighting model. More details can be found in the documentation related to the OpenGL programming, for example, here: <http://www.glprogramming.com/red/chapter05.html>.

In the OpenGL lighting model, the light in a scene comes from several light sources; the light sources have an effect only when there are surfaces that absorb and reflect light. Each surface is assumed to be composed of a material with various properties. A material might emit its own light (like headlights of a vehicle), it might scatter some incoming light in all directions, and it might reflect a portion of the incoming light in a preferential direction like a mirror or other shiny surface.

The OpenGL lighting model considers the lighting to be divided into four independent components: emissive, ambient, diffuse, and specular. All four components are computed independently and then added together.

- The **Ambient** illumination is the light that has been scattered so much by the environment that its direction is impossible to determine - it seems to come from all directions. Backlighting in a room has a large ambient component, since most of the light that reaches your eye has first bounced off many surfaces. A spotlight outdoors has a tiny ambient component; most of the light travels in the same direction, and since you're outdoors, very little of the light reaches your eye after bouncing off other objects. When ambient light strikes a surface, it is scattered equally in all directions.
- The **Diffuse** component is the light that comes from one direction, so it is brighter if it comes squarely down on a surface than if it barely glances off the surface. Once it hits a surface, however, it's scattered equally in all directions, so it appears equally bright, no matter where the eye is located. Any light coming from a particular position or direction probably has a diffuse component.
- The **Specular** light comes from a particular direction, and it tends to bounce off the surface in a preferred direction. A well-collimated laser beam bouncing off a high-quality mirror produces specular reflection by almost 100 percent. Shiny metal or plastic has a high specular component, and chalk or carpet has almost none. You can think of specularity as shininess.
- The **Emissive** color simulates light originating from an object. In the OpenGL lighting model, the emissive color of a surface adds intensity to the object, but is unaffected by any light sources. Also, the emissive color does not introduce any additional light into the overall scene.

Although a light source delivers a single distribution of frequencies, the ambient, diffuse, and specular components might be different. For example, if you have a white light in a room with red walls, the scattered light tends to be red, although the light directly striking objects is white. OpenGL allows you to set the red, green, and blue values for each component of light independently.

## Materials library

![materials_library.png](https://docs.salome-platform.org/latest/gui/GEOM/materials_library.png)

The dialog consists of two parts:

- The list to the left shows all available material models, both predefined and custom.

  - **[Current]** item in the list corresponds to the material model currently assigned to the selected shape(s). This model can be freely modified by the user.
  - **Global** material models are shown in blue color in the list; these are the models predefined by the SALOME Geometry module. The user is not allowed to modify the global models.
  - **User** materials are shown in black color in the list. These models are specified by the user and can be modified at any moment.
- The widgets to the right allow modifying different properties of the material model:

  - **Ambient** color and coefficient (floating point value between 0 and 1)
  - **Diffuse** color and coefficient (floating point value between 0 and 1)
  - **Specular** color and coefficient (floating point value between 0 and 1)
  - **Emissive** color and coefficient (floating point value between 0 and 1). Note: this attribute is applicable only for the OCC viewer; it simulates light originating from an object.
  - **Shininess**
  - **Type** of material model: *physical* or *artificial*.
- The buttons **Add material** and **Remove material** in the lower part of the dialog box can be used to create or remove custom material models. The same commands are also available via the context menu in the materials list. **Rename material** command can be used to change the name of material model.

## Material properties

![material.png](https://docs.salome-platform.org/latest/gui/GEOM/material.png)

In addition to the functionality of **Materials library**, this dialog provides objects selection mechanism and **Color** property.

If the material model is specified as a *physical* (*Gold*, for example), the shape color (more precisely its *ambient* color) cannot be modified. If you assign a physical material model to the shape, the "Color" menu item will not be available in the popup menu.

If the model is non-physical (*artificial*), the color can be changed to any appropriate one, only other attributes will be constant. In the dialog box you will be able to modify the color of the shape via the "Color" button. "Ambient color" button will be disabled to signalize that this attribute of the model is ignored. Also, it will be possible to modify the color of the shape via the [corresponding popup menu command](color_page.md).

**Examples:**

![material_OCC.png](https://docs.salome-platform.org/latest/gui/GEOM/material_OCC.png)

*Various materials in OCC viewer*

![material_VTK.png](https://docs.salome-platform.org/latest/gui/GEOM/material_VTK.png)

*Various materials in VTK viewer*

The default material model is specified via the preferences of Geometry module.
