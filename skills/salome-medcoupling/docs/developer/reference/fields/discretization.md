<!-- source: reference/fields/discretization.dox -->

# Spatial and temporal discretizations

When defining a field in MEDCoupling, the notions of spatial and temporal discretizations play
a crucial role.

The spatial discretization details the relationship between the field and its support mesh
and the temporal discretization gives an indication of the time coverage represented
by the field.

## Spatial discretization

A field can be supported by:
- the nodes (vertices) of the mesh: this is built with the
ON_NODES keyword in the
MEDCoupling::MEDCouplingFieldDouble::New(TypeOfField , TypeOfTimeDiscretization) "constructor of a field".

- the cells (or "elements") of the mesh: built with the
ON_CELLS keyword in the
MEDCoupling::MEDCouplingFieldDouble::New(TypeOfField , TypeOfTimeDiscretization) "constructor of a field".
- or more complex items:
    - Gauss points: built with ON_GAUSS_PT
    - Gauss points on nodes per element: built with ON_GAUSS_NE
    - Kriging points:  built with ON_NODES_KR
    - On points using standard FE description :  built with ON_NODES_FE

The spatial discretization is at the center of the [interpolation](reference/interpolation/interpolation.md) mechanisms,
since one of the main interpolation parameter is indeed specifying from which source discretization
to which target discretization one wants to go. For example:
- a P0->P0 interpolation means that a field on cells will be transferred to another cell-based field;
- a P1->P0 interpolation means that a field on nodes this time will be transferred to a cell-based field.
- etc ...

Finally, in the code itself, the class MEDCouplingFieldDiscretization
is the concrete representation of this concept.

## Temporal discretization

Similarly to the spatial discretization, a field object in MEDCoupling has a time discretization
representing the time range that is covered by the data. It is also specified in the
MEDCoupling::MEDCouplingFieldDouble::New(TypeOfField , TypeOfTimeDiscretization) "constructor of a field".

It can be one of:
- NO_TIME, in this case no time is attached to the field, and no
time-related operation is permitted (for example unable to call
getValueOn())
- ONE_TIME, the field data represent a single time step.
- LINEAR_TIME, the field data contains **two** arrays, stamped with two
different time points. A linear interpolation of the field values between those two time steps is then possible.
- CONST_ON_TIME_INTERVAL, the field data contains a single array
of data, but a start- and end-time can be specified, thus declaring that the field represent a constant
set of data during this time interval. All time evaluation function then just check that the given time
fits in the interval.

Finally, in the code itself, the class MEDCouplingTimeDiscretization
is the concrete representation of this concept.
