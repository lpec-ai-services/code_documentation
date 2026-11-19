# `ICoCoTrioField.hxx`


## class `TrioField`

```cpp
class TrioField : public Field
```

Field data stored internally as a TrioField object.

 This structure contains all the necessary information
 for constructing MEDCouplingFieldDouble (with the addition of the MPI
 communicator).
 This structure can either own or not _field values (_has_field_ownership)
 For _coords, _connectivity and _field, a null pointer means no data allocated.
 _coords and _connectivity tables, when allocated, are always owned by the TrioField.

 Copy constructor and assignment operator raise an exception as they are not implemented.


### `TrioField`

```cpp
TrioField();
```

Builds an empty field.


### `TrioField`

```cpp
TrioField(const TrioField& OtherField);
```

Copy constructor - FORBIDDEN.

**Throws** `ICoCo::NotImplemented`:


### `~TrioField`

```cpp
~TrioField();
```

Destructor.


### `clear`

```cpp
void clear();
```

Clear and reset all internal data structures.

After the call to clear(), all pointers are null and field ownership is false.
Arrays are deleted if necessary


### `set_standalone`

```cpp
void set_standalone();
```

Acquire field ownership.

After a call to set_standalone(), field ownership is true and field is allocated
to the size _nb_field_components*nb_values().
The values of the field have been copied if necessary.


### `dummy_geom`

```cpp
void dummy_geom();
```

Used to simulate a 0D geometry (Cathare/Trio for example).


### `TrioField& operator=(const TrioField& NewField)`

```cpp
TrioField& operator=(const TrioField& NewField);
```

Assignment operator - FORBIDDEN.

**Throws** `ICoCo::NotImplemented`:


### `save`

```cpp
void save(std::ostream& os) const;
```

Save field to a .field file


### `restore`

```cpp
void restore(std::istream& in);
```

Restore field from a .field file


### `nb_values`

```cpp
int nb_values() const;
```

The size of field is nb_values()*_nb_field_components
