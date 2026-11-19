<!-- source: c3po/LocalExchanger.py -->

# `c3po.LocalExchanger`

Contains the classes `LocalExchanger`, `ShortcutToField` and `ShortcutToValue`. `ShortcutToData` is for internal use only.

### `class c3po.LocalExchanger.ShortcutToField(container, name, type_=None)  — bases: object`

INTERNAL.

#### `ShortcutToField.initialize(self)`

INTERNAL.

#### `ShortcutToField.get(self)`

INTERNAL.

#### `ShortcutToField.getFieldTemplate(self)`

INTERNAL.

#### `ShortcutToField.set(self, field)`

INTERNAL.

#### `ShortcutToField.clean(self)`

INTERNAL.

### `class c3po.LocalExchanger.ShortcutToValue(container, name, type_=None)  — bases: object`

INTERNAL.

#### `ShortcutToValue.initialize(self)`

INTERNAL.

#### `ShortcutToValue.get(self)`

INTERNAL.

#### `ShortcutToValue.set(self, value)`

INTERNAL.

### `class c3po.LocalExchanger.LocalExchanger(method, fieldsToGet, fieldsToSet, valuesToGet=[], valuesToSet=[])  — bases: Exchanger`

`LocalExchanger` is an `Exchanger` for local data exchanges between `DataAccessor` objects (`PhysicsDriver` or `LocalDataManager`).

Once the object has been constructed, a call to `exchange` triggers the exchanges of data.

#### `LocalExchanger.exchange(self)`

Trigger the exchange of data.

#### `LocalExchanger.clean(self)`

See `Exchanger.clean`.
