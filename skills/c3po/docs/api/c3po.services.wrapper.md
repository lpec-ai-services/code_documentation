<!-- source: c3po/services/wrapper.py -->

# `c3po.services.wrapper`

Contain the functions `buildWrappingClass` and `wrapper`.

### `c3po.services.wrapper.buildWrappingClass(baseclass, objectAttr)`

Return a wrapping class of baseclass.

The `__init__` method of the returned class writes:

``` python
def __init__(self, wrappedObject):
    self._wrappedObject = wrappedObject
```

`_wrappedObject` is the only attribute of instances of the returned class.

All methods of baseclass (inherited methods are also treated) are wrapped this way:

``` python
def methodA(self, *args, **kwargs):
    return self._wrappedObject.methodA(*args, **kwargs)
```

Instance attributes of the wrapped class can be provided using `objectAttr`. They are made available in reading and writing using Python property.

For example:

``` python
ClassAWrapper = c3po.buildWrappingClass(ClassA, ["toto"])
objectA = ClassA(...)
wrapperA = ClassAWrapper(objectA)
```

Now, `wrapperA.toto` gives access to the same variable than `objectA.toto` or `wrapperA._wrappedObject.toto`.

## Parameters

baseclass  
The class we want a wrapper for.

objectAttr : list  
List of the names of `baseclass` instance attributes for which you wish to retain direct access.

## Returns

> A wrapper class for baseclass.

### `c3po.services.wrapper.wrapper(toWrap)`

Return a wrapping object for `toWrap`.

`wrapper` uses `c3po.services.wrapper.buildWrappingClass` in order to build a wrapping class for `toWrap` type, and return an instance of this wrapping class (wrapping `toWrap`).

## Parameters

toWrap  
Object instance (not class) to be wrapped.

## Returns

> A wrapping object.
