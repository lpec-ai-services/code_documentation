<!-- source: c3po/Exchanger.py -->

# `c3po.Exchanger`

Contains the classes `Exchanger`.

### `class c3po.Exchanger.Exchanger  — bases: object`

`Exchanger` is a class interface (to be implemented) which standardizes data exchanges between `DataAccessor` objects (`PhysicsDriver` or `LocalDataManager`).

Once the object has been constructed, a call to `exchange` triggers the exchanges of data.

#### `Exchanger.exchange(self)`

Trigger the exchange of data.

#### `Exchanger.clean(self)`

Clean up internal variables used to speed up data exchange under the assumption that meshes do not vary.

<div class="note">

<div class="title">

Note

</div>

It is mandatory to call this method each time the mesh of one of the `DataAccessor` involved in the exchange is modified.

</div>
