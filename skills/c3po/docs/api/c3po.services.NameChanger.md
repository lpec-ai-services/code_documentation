<!-- source: c3po/services/NameChanger.py -->

# `c3po.services.NameChanger`

Contain the class wrapper `NameChanger`.

### `class c3po.services.NameChanger.NameChanger(physics, nameMappingValue={}, nameMappingField={}, wildcard=None, exclusive=False)  — bases: PhysicsDriverWrapper`

`NameChanger` wraps a `PhysicsDriver` object and changes the names of the values and fields quantities that can be get/set through ICoCo methods.

This allows to improve the genericity of coupling scripts by using generic variable names without modifying the `PhysicsDriver` "by hand".

#### `NameChanger.updateNameMappingValue(self, nameMappingValue, variableTypes=(0, 1))`

Update (with the `update()` method of `dict`) the dictionary `nameMappingValue` previously provided.

## Parameters

nameMappingValue : dict  
The Python dictionary used for the update.

variableTypes : list  
List which values are 0 (for output) and/or 1 for input.

#### `NameChanger.updateNameMappingField(self, nameMappingField, variableTypes=(0, 1))`

Update (with the `update()` method of `dict`) the dictionary `nameMappingField` previously provided.

## Parameters

nameMappingField : dict  
The Python dictionary used for the update.

variableTypes : list  
List which values are 0 (for output) and/or 1 for input.

#### `NameChanger.getInputFieldsNames(self)`

See `c3po.DataAccessor.DataAccessor.getInputFieldsNames`.

#### `NameChanger.getOutputFieldsNames(self)`

See `c3po.DataAccessor.DataAccessor.getOutputFieldsNames`.

#### `NameChanger.getFieldType(self, name)`

See `c3po.DataAccessor.DataAccessor.getFieldType`.

#### `NameChanger.getFieldUnit(self, name)`

See `c3po.DataAccessor.DataAccessor.getFieldUnit`.

#### `NameChanger.getInputMEDDoubleFieldTemplate(self, name)`

See `c3po.DataAccessor.DataAccessor.getInputMEDDoubleFieldTemplate`.

#### `NameChanger.setInputMEDDoubleField(self, name, field)`

See `c3po.DataAccessor.DataAccessor.setInputMEDDoubleField`.

#### `NameChanger.getOutputMEDDoubleField(self, name)`

See `c3po.DataAccessor.DataAccessor.getOutputMEDDoubleField`.

#### `NameChanger.updateOutputMEDDoubleField(self, name, field)`

See `c3po.DataAccessor.DataAccessor.updateOutputMEDDoubleField`.

#### `NameChanger.getInputMEDIntFieldTemplate(self, name)`

See `c3po.DataAccessor.DataAccessor.getInputMEDIntFieldTemplate`.

#### `NameChanger.setInputMEDIntField(self, name, field)`

See `c3po.DataAccessor.DataAccessor.setInputMEDIntField`.

#### `NameChanger.getOutputMEDIntField(self, name)`

See `c3po.DataAccessor.DataAccessor.getOutputMEDIntField`.

#### `NameChanger.updateOutputMEDIntField(self, name, field)`

See `c3po.DataAccessor.DataAccessor.updateOutputMEDIntField`.

#### `NameChanger.getInputValuesNames(self)`

See `c3po.DataAccessor.DataAccessor.getInputValuesNames`.

#### `NameChanger.getOutputValuesNames(self)`

See `c3po.DataAccessor.DataAccessor.getOutputValuesNames`.

#### `NameChanger.getValueType(self, name)`

See `c3po.DataAccessor.DataAccessor.getValueType`.

#### `NameChanger.getValueUnit(self, name)`

See `c3po.DataAccessor.DataAccessor.getValueUnit`.

#### `NameChanger.setInputDoubleValue(self, name, value)`

See `c3po.DataAccessor.DataAccessor.setInputDoubleValue`.

#### `NameChanger.getOutputDoubleValue(self, name)`

See `c3po.DataAccessor.DataAccessor.getOutputDoubleValue`.

#### `NameChanger.setInputIntValue(self, name, value)`

See `c3po.DataAccessor.DataAccessor.setInputIntValue`.

#### `NameChanger.getOutputIntValue(self, name)`

See `c3po.DataAccessor.DataAccessor.getOutputIntValue`.

#### `NameChanger.setInputStringValue(self, name, value)`

See `c3po.DataAccessor.DataAccessor.setInputStringValue`.

#### `NameChanger.getOutputStringValue(self, name)`

See `c3po.DataAccessor.DataAccessor.getOutputStringValue`.

### `class c3po.services.NameChanger.NameChangerMeta(cls, clsname, superclasses, attributedict)  — bases: type`

Metaclass related to the use of `nameChanger`.

### `c3po.services.NameChanger.nameChanger(nameMapping, wildcard=None)`

`nameChanger` is a class wrapper that allows to change the names of the variables used by the base class (usually a `PhysicsDriver`).

This allows to improve the genericity of coupling scripts by using generic variable names without modifying the `PhysicsDriver` "by hand".

When a method of the base class is called there is two possibilities :

1.  The call uses a named argument "name" (for example `myObject.setInputDoubleValue(name="myName", value=0.)`). In this case, the value passed to the argument "name" is modified (if this is a key of `nameMapping`).
2.  There is no named argument "name" (for example `myObject.setInputDoubleValue("myName", 0.)`). In this case, the value of all arguments of type "str" is modified (if the value used is a key of `nameMapping`).

In both cases, nothing is done (no error) if the initial value is not in the keys of `nameMapping`.

The parameters of `nameChanger` are added to the class ("static" attributes) with the names `static_nameMapping` and `static_wildcard`. A new method is also added for internal use: `_getChangedName(self, name)`.

`nameChanger` can be used either as a python decorator (where the class is defined) in order to modify the class definition everywhere. For example:

``` python
@c3po.nameChanger({"newName" : "oldName", "newName2*" : "oldName2*"}, "*")
class MyClass(...):
    ...
```

or it can be used in order to redefined only locally the class like that:

``` python
MyNewClass = c3po.nameChanger({"newName" : "oldName", "newName2*" : "oldName2*"}, "*")(MyClass)
```

afterward "newName" can be used in place of "oldName" everywhere with `MyNewClass`. "oldName" is still working.

<div class="note">

<div class="title">

Note

</div>

`nameMapping` is copied.

</div>

<div class="warning">

<div class="title">

Warning

</div>

`nameChanger` looks for ICoCo methods (the methods to implement in order to define a `PhysicsDriver`) in base classes and redefine them. Other inherited methods are invisible to `nameChanger`.

A class that inherits from a class wrapped by nameChanger will be wrapped as well, with the same parameters. It may be a workaround for the previous warning. The definition of the daughter class ("`class Daughter(Mother): ...`") must be done after the application of `nameChanger` on Mother. Otherwise it will result in `TypeError` when the daughter class will try to call mother methods (since its mother class does not exist anymore!). As a consequence, if `nameChanger` is to be applied to C3PO classes, it is recommended to change their name "(`MyNewClass = c3po.nameChanger(...)(MyClass)`").

</div>

## Parameters

nameMapping : dict  
A Python dictionary with the mapping from the new names (the generic ones) to the old ones (the names used by the code).

wildcard : str  
A Python string. If both new and old names terminate by this wildcard (a wildcard in the middle of the names is not taken into account), `nameChanger` will substitute only the preceding part. For example : `c3po.nameChanger({"newName*" : "oldName*"}, "*")` will substitute `newNameA05` in `oldNameA05` and `newNameB9` in `oldNameB9`.

## Raises

Exception  
If applied to a class already modified by `nameChanger`, because it could result in an unexpected behavior.
