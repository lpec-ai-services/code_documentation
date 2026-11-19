<!-- source: c3po/services/tracer.py -->

# `c3po.services.tracer`

Contain the class wrapper tracer.

### `c3po.services.tracer.getRegularName(name)`

INTERNAL

### `c3po.services.tracer.getNameFieldInput(name, field)`

INTERNAL

### `c3po.services.tracer.getNameInput(name)`

INTERNAL

### `c3po.services.tracer.getDtInput(dt)`

INTERNAL

### `c3po.services.tracer.getStationaryModeInput(stationaryMode)`

INTERNAL

### `c3po.services.tracer.getTimeInput(time_)`

INTERNAL

### `c3po.services.tracer.getSaveInput(label, method)`

INTERNAL

### `c3po.services.tracer.getArgsString(*args, **kwargs)`

INTERNAL

### `c3po.services.tracer.buildTypeArgs(name, bases, dct)`

INTERNAL

### `c3po.services.tracer.tracer(pythonFile=None, saveInputMED=False, saveOutputMED=False, stdoutFile=None, stderrFile=None, listingWriter=None, workingDir=None)`

`tracer` is a class wrapper allowing to trace the calls of the methods of the base class.

`tracer` is to be applied on a class (not an object) and return a new class that inherits from the provided one.

It has different functions:

1.  It can write all calls of the methods of the base class in a text file in python format in order to allow to replay what happened from the code point of view outside of the coupling.
2.  It can save in .med files input or output MEDFields.
3.  It can redirect code standard and error outputs in text files.
4.  It can contribute (with `ListingWriter`) to the writing of a global coupling listing file with calculation time measurement.

The parameters of tracer are added to the returned class ("static" attributes) with the names `static_pythonFile`, `static_saveInputMED`, `static_saveOutputMED`, `static_stdout`, `static_stderr`, `static_lWriter` and `static_wDir`.

One additional static attribute is added for internal use: `static_Objectcounter`.

Two additional attributes (not static!) are added for internal use: `tracerObjectName` and `tracerRecurrenceDepth`.

`tracer` can be used either as a python decorator (where the class is defined) in order to modify the class definition everywhere:

``` python
@c3po.tracer(...)
class MyClass(...):
    ...
```

or it can be used in order to redefined only locally the class like that:

``` python
MyNewClass = c3po.tracer(...)(MyClass)
```

<div class="note">

<div class="title">

Note

</div>

In case a method calls another method of self, tracer modifies only to the first method call.

</div>

<div class="warning">

<div class="title">

Warning

</div>

`tracer` can be applied to any class, but it is design for standard C3PO objects: `PhysicsDriver`, `DataManager` and `Exchanger`. It may be hazardous to use on "similar but not identical" classes (typically with the same methods but different inputs and/or outputs).

`tracer` looks for ICoCo methods (the methods to implement in order to define a `PhysicsDriver`) (plus `__init__`) in base classes and redefine them. Other inherited methods are invisible to `tracer`.

It is recommended not to overload a class: use "`MyNewClass = c3po.tracer(...)(MyClass)`" and not "`MyClass = c3po.tracer(...)(MyClass)`". Overloading a class may lead to `TypeError`, in particular in case of inheritance, if the mother class is not accessible any more.

</div>

## Parameters

pythonFile  
A file object which has to be already open in written mode (`file = open("file.txt", "w")`). The python script is written there. It has to be closed (`file.close()`) by caller. The script can be run only if `saveInputMED` is set to True: otherwise, input MED fields are not stored.

saveInputMED : bool  
If set to True, every time `setInputMED(Double/Int/String)Field` is called, the input MED field is stored in a `.med` file. If `pythonFile` is activated, a MEDLoader reading instruction is also written in the Python file.

saveOutputMED : bool  
If set to True, every time `getOutputMED(Double/Int/String)Field` is called, the output MED field is stored in a `.med` file.

stdoutFile  
A file object which has to be already open in written mode (`file = open("file.txt", "w")`). The standard output is redirected there. It has to be closed (`file.close()`) by caller.

stderrFile  
A file object which has to be already open in written mode (`file = open("file.txt", "w")`). The error output is redirected there. It has to be closed (`file.close()`) by caller.

listingWriter : ListingWriter  
A `ListingWriter` object which will manage the writing of the coupling listing file. Refer to the documentation of `ListingWriter`.

workingDir  
Path to an existing directory which is used as working directory when calling the methods of the traced object.

## Raises

Exception  
If applied to a class already modified by `tracer`, because it could result in an unexpected behavior.
