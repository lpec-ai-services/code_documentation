<!-- source: c3po/DataAccessor.py -->

# `c3po.DataAccessor`

Contain the class `DataAccessor`.

### `class c3po.DataAccessor.DataAccessor  — bases: object`

`DataAccessor` is an abstract class which standardizes I/O (in/out) methods.

It follows the ICOCO V2 standard. See also `PhysicsDriver`.

#### `DataAccessor.getMPIComm(self)`

(Optional) Return the MPI communicator used by the code for parallel computations.

## Returns

mpi4py.MPI.Comm  
mpi4py communicator.

#### `DataAccessor.getInputFieldsNames(self)`

(Optional) Get the list of input fields accepted by the code.

## Returns

list  
The list of field names that represent inputs of the code.

## Raises

AssertionError  
If implemented in a `PhysicsDriver` and called before `initialize` or after `terminate`.

#### `DataAccessor.getOutputFieldsNames(self)`

(Optional) Get the list of output fields that can be provided by the code.

## Returns

list  
The list of field names that can be produced by the code.

## Raises

AssertionError  
If implemented in a `PhysicsDriver` and called before `initialize` or after `terminate`.

#### `DataAccessor.getFieldType(self, name)`

(Optional) Get the type of a field managed by the code.

(New in version 2) The three possible types are 'Double', 'Int' and 'String', as defined by `ValueType`.

## Parameters

name : str  
Field name.

## Returns

str  
'Double', 'Int' or 'String', as defined by `ValueType`.

## Raises

AssertionError  
If implemented in a `PhysicsDriver` and called before `initialize` or after `terminate`.

ValueError  
If the field `name` is invalid.

#### `DataAccessor.getMeshUnit(self)`

(Optional) Get the (length) unit used to define the meshes supporting the fields.

(New in version 2)

## Returns

str  
Length unit in which the mesh coordinates should be understood (e.g. 'm', 'cm', ...).

## Raises

AssertionError  
If implemented in a `PhysicsDriver` and called before `initialize` or after `terminate`.

#### `DataAccessor.getFieldUnit(self, name)`

(Optional) Get the physical unit used for a given field.

(New in version 2)

## Parameters

name : str  
Field name.

## Returns

str  
Unit in which the field values should be understood (e.g. 'W', 'J', 'Pa', ...).

## Raises

AssertionError  
If implemented in a `PhysicsDriver` and called before `initialize` or after `terminate`.

ValueError  
If the field `name` is invalid.

#### `DataAccessor.getInputMEDDoubleFieldTemplate(self, name)`

(Optional) Retrieve an empty shell for an input field.

This shell can be filled by the caller and then be given to the code via `setInputMEDDoubleField`.

The code returns a field with all the data that represents the context of the field (i.e. its support mesh, its discretization -- on nodes, on elements, ...). The remaining job for the caller of this method is to fill the actual values of the field itself. When this is done the field can be sent back to the code through the method `setInputMEDDoubleField`. This method is not mandatory but is useful to know the mesh, discretization... on which an input field is expected. Is is required by C3PO remapping functionalities.

See `PhysicsDriver` documentation for more details on the time semantic of a field.

## Parameters

name : str  
Name of the field for which we would like the empty shell.

## Returns

medcoupling.MEDCouplingFieldDouble  
Field with all the contextual information.

## Raises

AssertionError  
If implemented in a `PhysicsDriver` and called before `initialize` or after `terminate`.

ValueError  
If the field `name` is invalid.

#### `DataAccessor.setInputMEDDoubleField(self, name, field)`

(Optional) Provide the code with input data in the form of a `MEDCouplingFieldDouble`.

The method `getInputMEDDoubleFieldTemplate`, if implemented, may be used first to prepare an empty shell of the field to pass to the code.

See `PhysicsDriver` documentation for more details on the time semantic of a field.

## Parameters

name : str  
Name of the field that is given to the code.

field : medcoupling.MEDCouplingFieldDouble  
Field containing the input data to be read by the code. The name of the field set on this instance (with the `Field::setName` method) should not be checked. However its time value should be to ensure it is within the proper time interval `]t, t+dt]`.

## Raises

AssertionError  
If implemented in a `PhysicsDriver` and called before `initialize` or after `terminate`.

ValueError  
If the field `name` ('name' parameter) is invalid.

ValueError  
If the time property of `field` does not belong to the currently computed time step `]t, t + dt]`.

#### `DataAccessor.getOutputMEDDoubleField(self, name)`

(Optional) Return output data from the code in the form of a `MEDCouplingFieldDouble`.

See `PhysicsDriver` documentation for more details on the time semantic of a field.

## Parameters

name : str  
Name of the field that the caller requests from the code.

## Returns

medcoupling.MEDCouplingFieldDouble  
Field with the data read by the code. The name and time properties of the field should be set in accordance with the 'name' parameter and with the current time step being computed.

## Raises

AssertionError  
If implemented in a `PhysicsDriver` and called before `initialize` or after `terminate`.

ValueError  
If the field `name` is invalid.

#### `DataAccessor.updateOutputMEDDoubleField(self, name, field)`

(Optional) Update a previously retrieved output field.

(New in version 2) This method allows the code to implement a more efficient update of a given output field, thus avoiding the caller to invoke `getOutputMEDDoubleField` each time. A previous call to `getOutputMEDDoubleField` with the same name must have been done prior to this call. The code should check the consistency of the field object with the requested data (same support mesh, discretization -- on nodes, on elements, etc.).

See `PhysicsDriver` documentation for more details on the time semantic of a field.

## Parameters

name : str  
Name of the field that the caller requests from the code.

field : medcoupling.MEDCouplingFieldDouble  
Object updated with the data read from the code. Notably the time indicated in the field should be updated to be within the current time step being computed.

## Raises

AssertionError  
If implemented in a `PhysicsDriver` and called before `initialize` or after `terminate`.

ValueError  
If the field name (`name` parameter) is invalid.

ValueError  
If the field object is inconsistent with the field being requested.

#### `DataAccessor.getInputMEDIntFieldTemplate(self, name)`

Similar to `getInputMEDDoubleFieldTemplate` but for `MEDCouplingFieldInt`.

#### `DataAccessor.setInputMEDIntField(self, name, field)`

Similar to `setInputMEDDoubleField` but for `MEDCouplingFieldInt`.

#### `DataAccessor.getOutputMEDIntField(self, name)`

Similar to `getOutputMEDDoubleField` but for `MEDCouplingFieldInt`.

#### `DataAccessor.updateOutputMEDIntField(self, name, field)`

Similar to `updateOutputMEDDoubleField` but for `MEDCouplingFieldInt`.

#### `DataAccessor.getInputMEDStringFieldTemplate(self, name)`

Similar to `getInputMEDDoubleFieldTemplate` but for `MEDCouplingFieldString`.

<div class="warning">

<div class="title">

Warning

</div>

At the time of writing, `MEDCouplingFieldString` are not yet implemented anywhere.

</div>

#### `DataAccessor.setInputMEDStringField(self, name, field)`

Similar to `setInputMEDDoubleField` but for `MEDCouplingFieldString`.

<div class="warning">

<div class="title">

Warning

</div>

At the time of writing, `MEDCouplingFieldString` are not yet implemented anywhere.

</div>

#### `DataAccessor.getOutputMEDStringField(self, name)`

Similar to `getOutputMEDDoubleField` but for `MEDCouplingFieldString`.

<div class="warning">

<div class="title">

Warning

</div>

At the time of writing, `MEDCouplingFieldString` are not yet implemented anywhere.

</div>

#### `DataAccessor.updateOutputMEDStringField(self, name, field)`

Similar to `updateOutputMEDDoubleField` but for `MEDCouplingFieldString`.

<div class="warning">

<div class="title">

Warning

</div>

At the time of writing, `MEDCouplingFieldString` are not yet implemented anywhere.

</div>

#### `DataAccessor.getInputValuesNames(self)`

(Optional) Get the list of input scalars accepted by the code.

## Returns

list  
The list of scalar names that represent inputs of the code.

## Raises

AssertionError  
If implemented in a `PhysicsDriver` and called before `initialize` or after `terminate`.

#### `DataAccessor.getOutputValuesNames(self)`

(Optional) Get the list of output scalars that can be provided by the code.

## Returns

list  
The list of scalar names that can be returned by the code.

## Raises

AssertionError  
If implemented in a `PhysicsDriver` and called before `initialize` or after `terminate`.

#### `DataAccessor.getValueType(self, name)`

(Optional) Get the type of a scalar managed by the code.

(New in version 2) The three possible types are 'Double', 'Int' and 'String', as defined by `ValueType`.

## Parameters

name : str  
Scalar value name.

## Returns

str  
'Double', 'Int' or 'String', as defined by `ValueType`.

## Raises

AssertionError  
If implemented in a `PhysicsDriver` and called before `initialize` or after `terminate`.

ValueError  
If the scalar name is invalid.

#### `DataAccessor.getValueUnit(self, name)`

(Optional) Get the physical unit used for a given value.

(New in version 2)

## Parameters

name : str  
Scalar value name.

## Returns

str  
Unit in which the scalar value should be understood (e.g. 'W', 'J', 'Pa', ...).

## Raises

AssertionError  
If implemented in a `PhysicsDriver` and called before `initialize` or after `terminate`.

ValueError  
If the scalar name is invalid.

#### `DataAccessor.setInputDoubleValue(self, name, value)`

(Optional) Provide the code with a scalar `float` data.

See `PhysicsDriver` documentation for more details on the time semantic of a scalar value.

## Parameters

name : str  
Name of the scalar value that is given to the code.

value : float  
Value passed to the code.

## Raises

AssertionError  
If implemented in a `PhysicsDriver` and called before `initialize` or after `terminate`.

ValueError  
If the scalar name is invalid.

#### `DataAccessor.getOutputDoubleValue(self, name)`

(Optional) Retrieve a scalar `float` value from the code.

See `PhysicsDriver` documentation for more details on the time semantic of a scalar value.

## Parameters

name : str  
Name of the scalar value to be read from the code.

## Returns

float  
The value read from the code.

## Raises

AssertionError  
If implemented in a `PhysicsDriver` and called before `initialize` or after `terminate`.

ValueError  
If the scalar name is invalid.

#### `DataAccessor.setInputIntValue(self, name, value)`

(Optional) Similar to `setInputDoubleValue` but for an `int` value.

#### `DataAccessor.getOutputIntValue(self, name)`

(Optional) Similar to `getOutputDoubleValue` but for an `int` value.

#### `DataAccessor.setInputStringValue(self, name, value)`

(Optional) Similar to `setInputDoubleValue` but for an `str` value.

#### `DataAccessor.getOutputStringValue(self, name)`

(Optional) Similar to `getOutputDoubleValue` but for an `str` value.
