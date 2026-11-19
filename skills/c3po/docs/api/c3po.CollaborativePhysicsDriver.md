<!-- source: c3po/CollaborativePhysicsDriver.py -->

# `c3po.CollaborativePhysicsDriver`

Contain the class `CollaborativePhysicsDriver`.

### `class c3po.CollaborativePhysicsDriver.CollaborativePhysicsDriver(physics)  — bases: Coupler, CollaborativeObject`

`CollaborativePhysicsDriver` is a `PhysicsDriver` (a `Coupler` in fact) that handles a set of `PhysicsDriver` as a single one.

The solving methods of the `CollaborativePhysicsDriver` call the ones of the held `PhysicsDriver` in a row.

#### `CollaborativePhysicsDriver.solveTimeStep(self)`

See `PhysicsDriver.solveTimeStep`.

#### `CollaborativePhysicsDriver.iterateTimeStep(self)`

See `PhysicsDriver.iterateTimeStep`.

#### `CollaborativePhysicsDriver.save(self, label, method)`

See `PhysicsDriver.save`.

#### `CollaborativePhysicsDriver.restore(self, label, method)`

See `PhysicsDriver.restore`.

#### `CollaborativePhysicsDriver.forget(self, label, method)`

See `PhysicsDriver.forget`.

#### `CollaborativePhysicsDriver.setInputDoubleValue(self, name, value)`

See `c3po.DataAccessor.DataAccessor.setInputDoubleValue`.

#### `CollaborativePhysicsDriver.setInputIntValue(self, name, value)`

See `c3po.DataAccessor.DataAccessor.setInputIntValue`.

#### `CollaborativePhysicsDriver.setInputStringValue(self, name, value)`

See `c3po.DataAccessor.DataAccessor.setInputStringValue`.
