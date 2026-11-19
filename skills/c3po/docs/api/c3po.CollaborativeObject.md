<!-- source: c3po/CollaborativeObject.py -->

# `c3po.CollaborativeObject`

Contain the class `CollaborativePhysicsDriver`.

### `class c3po.CollaborativeObject.CollaborativeObject(elements)  — bases: object`

`CollaborativeObject` defines the concept of a collaborative object.

A collaborative object of a certain type is built from a collection of objects of that same type. Collaborative actions are obtained by the realization of these same actions by the objects held.

#### `CollaborativeObject.getElements(self)`

Return the elements held.

## Returns

list  
The list of elements provided to the constructor.

#### `CollaborativeObject.getElementsRecursively(self)`

Similar to `getElements()` but is applied recursively in order to return the full list of elements.

## Returns

list  
The full list of elements.
