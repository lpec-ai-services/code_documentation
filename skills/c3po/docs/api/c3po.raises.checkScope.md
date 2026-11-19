<!-- source: c3po/raises/checkScope.py -->

# `c3po.raises.checkScope`

Contain the meta-class `CheckScopeMeta` and class wrapper `checkScope`.

### `class c3po.raises.checkScope.CheckScopeMeta  — bases: type`

Metaclass related to the use of `checkScope`.

### `c3po.raises.checkScope.checkScope(baseclass)`

Add a verification of the calling context of ICoCo methods.

`checkScope` is to be applied on a class (not an object) and return a new class that inherits from the provided one.

`checkScope` has the following effects:

- It raises `icoco.exception.WrongContext` errors when an ICoCo method is called in a wrong context (see ICoCo documentation).
- It adds an object attribute 'problemName' used in the message of these `icoco.exception.WrongContext` errors. Default: `f"{self.__class__.__module__}.{self.__class__.__name__}`"
- It also adds the object attribute 'iCoCoEnsureScope' that can be used to activate / desactivate these checks. Default: `iCoCoEnsureScope=True` which means activated.

Two additional object attributes are added for internal use: `_iCoCoInitialized` and `_iCoCoTimeStepDefined`.

`checkScope` can be used either as a python decorator (where the class is defined) in order to modify the class definition everywhere:

``` python
@c3po.raises.checkScope
class MyClass(...):
    ...
```

or it can be used in order to redefined only locally the class like that:

``` python
MyNewClass = c3po.raises.checkScope(MyClass)
```

<div class="note">

<div class="title">

Note

</div>

`checkScope` looks for ICoCo methods definitions in base classes in order to overload them.

`checkScope` relies on a metaclass (`c3po.raises.checkScope.CheckScopeMeta`). That means that daughter classes will also be modified by `checkScope`.

</div>

<div class="warning">

<div class="title">

Warning

</div>

It is recommended not to overload a class: use "`MyNewClass = c3po.raises.checkScope(MyClass)`" and not "`MyClass = c3po.raises.checkScope(MyClass)`". Overloading a class may lead to `TypeError`, in particular in case of inheritance, if the mother class is not accessible any more.

</div>

## Parameters

baseclass  
The class to modify.

## Returns

> A new class, with modified methods.
