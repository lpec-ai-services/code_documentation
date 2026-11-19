# `ICoCoField.hxx`


## class `Field`

```cpp
class ICOCO_EXPORT Field
```

Top abstract class defining field objects that can be exchanged via the ICoCo interface.

The Field class holds the name of the field.


### `setName`

```cpp
void setName(const std::string& name);
```

Set the name of the field.

- **name**: name of the field


### `getName`

```cpp
const std::string& getName() const;
```

Retrieves the name of the field.

**Returns:** name of the field.


### `getCharName`

```cpp
const char* getCharName() const;
```

Retrieves the name of the field as a char *

**Returns:** name of the field.
