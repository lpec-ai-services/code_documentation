<!-- source: https://docs.salome-platform.org/latest/gui/GUI/using_pluginsmanager.html -->

# Extend SALOME gui functions using python plugins

1. [Objectives](#s1-salomeplugins)
2. [Principles](#s2-salomeplugins)
3. [A complete example](#s3-salomeplugins)
4. [How to select an object of the object browser](#s4-salomeplugins)
5. [Other examples](#s5-salomeplugins)

## Objectives

The SALOME python plugin manager allows the end user to extend the
graphic interface of SALOME with custom functions written as python
modules. The screenshots below show the example of a tool that creates
a mesh from a set of geometrical parameters with the support of
simple graphical interface:

The default menu for plugins is “Tool->Extensions”:

![figure](https://docs.salome-platform.org/latest/gui/GUI/_images/SALOME_pythonplugins_menu.png)

In this example, the plugin provides a small interface to input the
parameters (not provided by the plugin manager):

![figure](https://docs.salome-platform.org/latest/gui/GUI/_images/SALOME_pythonplugins_dialog.png)

Then creates the mesh model:

![figure](https://docs.salome-platform.org/latest/gui/GUI/_images/SALOME_pythonplugins_result.png)

In this example, the end user has to write:

1. the python script that creates the mesh from the parameters, using the GEOM and SMESH python interface, as in a classic use case,
2. the dialog box in PyQt to input the parameters,
3. the file salome_plugins.py that declares the plugins.

This page explains only the last point.

## Principles

The general form of the file salome_plugins.py is:

```python
     import salome_pluginsmanager

     # Creation of the plugin
     def myplugin1(context):
        ...
        # Here is the code of the plugin myplugin1
        ...

     def myplugin2(context):
        ...
        # Here is the code of the plugin myplugin2
        ...

     # Declaration of the plugins to the pluginsmanager
     salome_pluginsmanager.AddFunction('My plugin n°1', 'This action runs the plugin n°1', myplugin1)
     salome_pluginsmanager.AddFunction('My plugin n°2', 'This action runs the plugin n°2', myplugin2)
     ...
```

The procedure is to define a function that implements the plugin, and
to declare this function to the plugins manager. The implementation
can be very variable. It is advisable to consider this function as a
proxy to your code that you can manage in a python package
installed in the standard SALOME python directories.

In this code, the variable “context” is automatically transmitted by
the pluginmanager when you request the plugin. This context provides
you with at least the following attributes:

```python
     activeStudy = context.study
     salomegui = context.sg
```

Once written, this script salome_plugin.py has to be moved to a
specific place on your filesystem where SALOME is programmed to search
for plugins. The possible directories are (in search order):

1. The directory <*_ROOT_DIR>/share/salome/plugins/<module_name>, when this plugin is developped in the framework of a SALOME module (<*_ROOT_DIR> is the root installation directory of the module, and <module_name> is the name of the module in low letters).
2. The directory ~/.config/salome/Plugins for personnal end user plugins.
3. Any path in the shell variable SALOME_PLUGINS_PATH (each path must be separated by a comma “:” for unix and “;” for windows). This variable should be set and exported before running the SALOME application.

## A complete example

Suppose that you write a SALOME script that creates a trihedron for each of
your studies (a simple and standard SALOME script, that every end user
is capable to write if he reads the documentation and follows the
training course):

```python
     # Intialize the geompy factory with the active study
     import salome
     import GEOM
     from salome.geom import geomBuilder
     geompy = geomBuilder.New(salome.myStudy)

     # Create the objects
     Vx = geompy.MakeVectorDXDYDZ(10, 0, 0)
     Vy = geompy.MakeVectorDXDYDZ(0, 10, 0)
     Vz = geompy.MakeVectorDXDYDZ(0, 0, 10)
     origin = geompy.MakeVertex(0, 0, 0)

     # Register the objects in the active study
     geompy.addToStudy( Vx, "Vx" )
     geompy.addToStudy( Vy, "Vy" )
     geompy.addToStudy( Vz, "Vz" )
     geompy.addToStudy( origin, "origin" )
```

The job consists in creating the file salome_plugins.py as follows:

```python
     import salome_pluginsmanager
     def trihedron(context):
         import GEOM
         from salome.geom import geomBuilder
         geompy = geomBuilder.New(salome.myStudy)
         # Intialize the geompy factory with the active study
         activeStudy = context.study
         geompy.init_geom(activeStudy)
         # Create the objects
         Vx = geompy.MakeVectorDXDYDZ(10, 0, 0)
         Vy = geompy.MakeVectorDXDYDZ(0, 10, 0)
         Vz = geompy.MakeVectorDXDYDZ(0, 0, 10)
         origin = geompy.MakeVertex(0, 0, 0)
         # Register the objects in the active study
         geompy.addToStudy( Vx, "Vx" )
         geompy.addToStudy( Vy, "Vy" )
         geompy.addToStudy( Vz, "Vz" )
        geompy.addToStudy( origin, "origin" )

     # Register the function in the plugin manager
     salome_pluginsmanager.AddFunction('O,Vx,Vy,Vz',
                                       'Creates the trihedron',
                                       trihedron)
```

Move this script in the directory ~/.config/salome/Plugins, run SALOME and enjoy your new function.

## How to select an object of the object browser

Sometimes it can be useful to retrieve an object of the object browser to perform
an action on it, for example, to select a mesh and display some information related to it.

Some important methods and objects to use are as follows:

1. context.sg.getObjectBrowser(): to connect the signal event selectionChanged() to a custom slot
2. context.salome.sg.getAllSelected(): to get the list of selected object in the object browser
3. objId = context.salome.sg.getSelected(0): to get the first selected object in the object browser
4. salomeObj = context.salome.study.FindObjectID(objId).GetObject(): to retrieve the salome object from selection. It can be a GEOM, SMESH, or any other module object.

> If it is a mesh, then it is possible to call methods of the SMESH::SMESH_Mesh interface
> on the object, for example GetShapeToMesh().
> If it is not a mesh, this call will raise an exception.
> So it is possible to write the code retrieving the shape a mesh is built on in the following way:

```python
     mesh = None
     try:
       shape = salomeObj.GetShapeToMesh()
     except:
       print "The selection is not a mesh"
```

An example of those methods is available with the demo examples.
See the next chapter [Other examples](#s5-salomeplugins).

## Other examples

The GUI module provides you with some basic demo examples located in
the directory src/SalomeApp/pluginsdemo of the source space and
installed in the directory $GUI_ROOT_DIR/share/salome/plugins/gui/demo.

Note

These examples are automatically installed when you install the GUI but are not activated. To activate the plugins, edit the file $GUI_ROOT_DIR/share/salome/plugins/gui/demo/salome_plugins.py and turn the variable DEMO_IS_ACTIVATED to True.

The demo examples are:

1. **trihedron:** create a trihedron and display it with fit on the size
2. **tube_shapewithgui:** create a geom object from parameters given by a dialog box.
3. **tube_meshwithgui:** create a mesh object from parameters given by a dialog box. This illustrates that a plugin can work with more than one SALOME module.
4. **tube_shapewithguiAndPreview:** same than tube_shapewithgui but with an additionnal preview function (button apply in the dialog box).
5. **runSalomeShellSession:** run a SALOME prepared shell session in a xterm.
6. **minmax:** computes the min and max values of a control on a selected mesh.
   :   Note

       This plugin is available in the SMESH module only. To activate it, edit the file $GUI_ROOT_DIR/share/salome/plugins/gui/demo/smesh_plugins.py and turn the variable DEMO_IS_ACTIVATED to True.
