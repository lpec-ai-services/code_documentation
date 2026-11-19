# `ICoCoMEDDoubleField.hxx`


## class `MEDDoubleField`

```cpp
class ICOCO_EXPORT MEDDoubleField : public ICoCo::Field
```

Field data stored internally as a MEDCoupling object.

This class is a wrapper around a MEDCoupling::MEDCouplingFieldDouble object, which holds the field data.
In version 2 of ICoCo, MEDCoupling::MEDCouplingFieldDouble objects are not anymore exposed directly into the API
of ICoCo::Problem. The rationale is to make the interface ICoCo::Problem free of external dependencies
(MEDCoupling particularly).


**Sa:** the MEDCoupling documentation, notably the reference counter mechanism used to manage the lifecycle of
MEDCoupling objects.


### `MEDDoubleField`

```cpp
MEDDoubleField();
```

Builds an empty field (internal MEDCoupling object not set).


### `MEDDoubleField`

```cpp
MEDDoubleField(MEDCoupling::MEDCouplingFieldDouble* field);
```

Builds a field and assign its internal MEDCouplingField object.

The name of 'this' is also automatically set the name of the MEDCouplingField object. If 'field' is null
the name is set to the empty string.


- **field**: MEDCoupling field instance to use for field data. The field reference counter is incremented.


### `MEDDoubleField`

```cpp
MEDDoubleField(const MEDDoubleField& field);
```

Copy construcotr.


### `MEDDoubleField& operator=(const MEDDoubleField& field)`

```cpp
MEDDoubleField& operator=(const MEDDoubleField& field);
```

Assignement operator.

- **field**: another MEDDoubleField instance. The previous internal MEDCoupling field reference (if any) has
its counter decremented.


### `~MEDDoubleField`

```cpp
virtual ~MEDDoubleField();
```

Destructor.


### `getMCField`

```cpp
MEDCoupling::MEDCouplingFieldDouble *getMCField() const;
```

Get the internal MEDCoupling field object.

**Returns:** a pointer to the MEDCouplingField object detained by this instance. Note that the corresponding
object should not be deleted, or its reference counter should not be decreased! Doing so will result in an
invalid instance of the current MEDField.


### `setMCField`

```cpp
void setMCField(MEDCoupling::MEDCouplingFieldDouble * field);
```

Set the internal MEDCoupling field object.

Any previously set field is discarded (its reference counter is decreased) and the reference counter of the
field being set is increased.

The name of 'this' is also automatically set the name of the MEDCouplingField object. If 'field' is nullptr
the name is reset to the empty string.


- **field**: MEDCouplingFieldDouble object to be used.
