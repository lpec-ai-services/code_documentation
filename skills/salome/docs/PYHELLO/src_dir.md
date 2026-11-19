<!-- source: https://docs.salome-platform.org/latest/gui/PYHELLO/src_dir.html -->

# The src directory

The src contains all source files required to build and install CORBA engine and (optionally) GUI of the module. Each of these entities usually has (but this is not actually obligatory) its own directory.

The `CMakeLists.txt` file triggers the path of sub-directories described by the *ADD_SUBDIRECTORY()* command.

- The src/PYHELLO directory

This directory contains the Python files that implement the engine of the module. The `CMakeLists.txt` defines the rules used to install these files to the destination folder. The name of the module engine Python file is predefined and should be set as <MODULE>.py where <MODULE> is a name of the module. In the case of the PYHELLO module, the name of the engine Python script should be PYHELLO.so.

The `PYHELLO.py` Python script implements PYHELLO class that is derived from the PYHELLO_Gen interface of the PYHELLO_ORB__POA CORBA module, the SALOME_ComponentPy_i class (base implementation of SALOME Python module engine exported by the KERNEL module) and SALOME_DriverPy_i class that provides base implementation of persistence mechanism.

In particular, *PYHELLO* class implements makeBanner() function that is defined in the IDL interface PYHELLO_ORB::PYHELLO_Gen.

```python
def makeBanner( self, name ):
    banner = "Hello %s!" % name
    return banner
```

Other services defined in PYHELLO_Gen CORBA interface also should be implemented by this class.

- The src/PYHELLOGUI directory

This directory contains the Python files that implement the GUI of PYHELLO module. The name of the module GUI Python script is predefined and should be set as <MODULE>GUI.py where <MODULE> is a name of the module. In the case of the PYHELLO module, the name of the GUI Python script should be PYHELLOGUI.py.

The implementation of GUI of the PYHELLO module should be done according to the architecture and rules specified by the SALOME GUI module. The PYHELLO.py script should implement a set of the functions which define the module behavior in GUI, for example, create menus, toolbars, define context popup menus, objects selection behavior, implement dialog boxes etc.

Here below is a short description of these methods. For more details please refer to the SALOME GUI module documentation.

- initialize() - module first initialization; usually used to create GUI actions, menus, toolbars and so on;
- activate() - module activation; perform actions which should be done when the module is activated by the user;
- deactivate() - module deactivation; perform actions which should be done when the module is deactivated by the user;
- windows() - get a list and a position of the windows to be associated with the module; these windows will be automatically opened and positioned according to the setting defined by the value returned by this function;
- views() - get a list of the compatible viewers; these viewers will be automatically opened/raised on the module activation;
- createPopupMenu() - create and return context popup menu according to the current selection;
- createPreferences() - initialize module's preferences;
- preferenceChanged() - callback function that is called when some module's preference is changed by the user; allows to perform the corresponding actions;
- engineIOR() - to get the reference to the module CORBA engine

Note, that some of these methods are optional and need not be obligatory implemented because SalomePyQtGUI_Module class provides a base implementation of these functions. It's sometimes enough to implement only some of them, depending on the module needs.

In the case of PYHELLO module, some of these functions are implemented to provide a sample for the development:

- engineIOR() that initializes PYHELLO module's eggine:

```python
def engineIOR():
    IOR = ""
    if getORB() and getEngine():
        IOR = getORB().object_to_string( getEngine() )
        pass
    return IOR
```

- initialize() that sets default module preferences

```python
def initialize():
    if not sgPyQt.hasSetting( "PYHELLO", "def_obj_name"):
        sgPyQt.addSetting( "PYHELLO", "def_obj_name", GUIcontext.DEFAULT_NAME )
    if not sgPyQt.hasSetting( "PYHELLO", "creation_mode"):
        sgPyQt.addSetting( "PYHELLO", "creation_mode", 0 )
```

- createPreferences() that initializes module preferences for the application's Preferences dialog box

```python
def createPreferences():
    if verbose():
        print("PYHELLOGUI.createPreferences()")
    gid = sgPyQt.addPreference("General")
    gid = sgPyQt.addPreference("Object creation", gid)
    sgPyQt.addPreference("Default name", gid, SalomePyQt.PT_String, "PYHELLO", "def_obj_name")
    pid = sgPyQt.addPreference("Default creation mode", gid, SalomePyQt.PT_Selector, "PYHELLO", "creation_mode")
    strings = ["Default name", "Generate name", "Ask name"]
    indexes = [0, 1, 2]
    sgPyQt.setPreferenceProperty(pid, "strings", strings)
    sgPyQt.setPreferenceProperty(pid, "indexes", indexes)
    pid = sgPyQt.addPreference("Password", gid, SalomePyQt.PT_String, "PYHELLO", "Password")
    sgPyQt.setPreferenceProperty(pid, "echo", 2)
    pass
```

- windows() that defines dockable windows layout

```python
def windows():
    if verbose() : print("PYHELLOGUI.windows()")
    wm = {}
    wm[SalomePyQt.WT_ObjectBrowser] = Qt.LeftDockWidgetArea
    wm[SalomePyQt.WT_PyConsole]     = Qt.BottomDockWidgetArea
 return wm
```

Please refer to PYHELLOGUI.py script for more details about implementation of other callback functions.

An implemention of the ShowHello() function is quite simple. It shows the small dialog box allowing user to enter the name, and then uses reference to the module CORBA engine to invoke its makeBanner() service.

Note, that GUI elements of the Python module are implemented with help of PyQt toolkit which provides a Python wrappings of the Qt library.

[<< Previous](idl_dir.md)  
[>> Next](bin_dir.md)
