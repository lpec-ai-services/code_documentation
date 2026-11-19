<!-- source: c3po/services/ListingWriter.py -->

# `c3po.services.ListingWriter`

Contain the class `ListingWriter`.

### `c3po.services.ListingWriter.getFormattedTime(timeValue)`

INTERNAL

### `class c3po.services.ListingWriter.ListingWriter(listingFile)  — bases: object`

`ListingWriter` allows, in association with `c3po.services.tracer.tracer`, to write a global coupling listing file with calculation time measurement.

`ListingWriter` is completed by the funtions `mergeListing`, `getTotalTimePhysicsDriver` and `getTimesExchanger`.

#### `ListingWriter.initialize(self, physics, exchangers, force=False)`

Clear and initialize the object.

Can be replace by a call to `terminate` (optional for the first call) followed by calls to `setPhysicsDriverName` and `setExchangerName`.

`setPhysicsDriverName` and `setExchangerName` can also be used after `initialize`, but not before (what is set before is forgotten).

## Parameters

physics : list\[tuple\]\]  
A list of tuples `(object, name)`. `object` should be a `PhysicsDriver`, modified with `c3po.services.tracer.tracer` to point on this `ListingWriter` object. An object that does not meet these conditions is ignored. A column (entitled with `name`) is created in the listing file for each of them.

exchangers : list\[tuple\]\]  
A list of tuples `(object, name)`. `object` should be an `Exchanger` object, modified with `c3po.services.tracer.tracer` to point on this `ListingWriter` object. An object that does not meet these conditions is ignored. `name` allows to identify them in the final listing file.

force : bool  
If set to True, `physics` and `exchangers` are added even if they do not meet the previously defined conditions.

#### `ListingWriter.terminate(self)`

Get ready to write a new listing.

What was previously set by `initialize`, `setPhysicsDriverName` and `setExchangerName` is forgotten.

#### `ListingWriter.setPhysicsDriverName(self, physics, name, force=False)`

Get ready to write a listing with the provided `PhysicsDriver`.

## Parameters

physics : PhysicsDriver  
A `PhysicsDriver` object, modified with `c3po.services.tracer.tracer` to point on this `ListingWriter` object. If `physics` does not meet these conditions, it is ignored. Otherwise, a column (entitled with `name`) will be created in the listing file for it.

name : str  
The name to use for `physics` in the listing.

force : bool  
If set to True, `physics` is added even if it does not meet the previously defined conditions.

#### `ListingWriter.setExchangerName(self, exchanger, name, force=False)`

Get ready to write a listing with the provided `Exchanger`.

## Parameters

exchanger : Exchanger  
A `Exchanger` object, modified with `c3po.services.tracer.tracer` to point on this `ListingWriter` object. If `exchanger` does not meet these conditions, it is ignored. Otherwise, a lign will be written in the listing for each call of exchanger's `exchange` method .

name : str  
The name to use for `exchanger` in the listing.

force : bool  
If set to True, `exchanger` is added even if it does not meet the previously defined conditions.

#### `ListingWriter.prepare(self)`

INTERNAL

#### `ListingWriter.writeInitialize(self, presentTime)`

INTERNAL

#### `ListingWriter.writeValidate(self, timeValid)`

INTERNAL

#### `ListingWriter.writeTerminate(self)`

INTERNAL

#### `ListingWriter.writeAfter(self, sourceObject, inputVar, outputTuple, methodName, presentTime, calculationTime)`

INTERNAL

### `class c3po.services.ListingWriter.MergedListingWriter(listingFile)  — bases: ListingWriter`

INTERNAL

#### `MergedListingWriter.prepare(self)`

INTERNAL

#### `MergedListingWriter.readLastLine(self)`

INTERNAL

#### `MergedListingWriter.writeBefore(self, sourceObject, toWrite, methodName, runningPhysics, presentTime, calculationTime)`

INTERNAL

#### `MergedListingWriter.writeBeforeExchange(self, sourceObject, toWrite, methodName, involvedPhysics, runningPhysics, presentTime, calculationTime)`

INTERNAL

#### `MergedListingWriter.writeAfterNew(self, sourceObject, toWrite, methodName, runningPhysics, presentTime)`

INTERNAL

#### `MergedListingWriter.writeAfterExchange(self, sourceObject, toWrite, methodName, involvedPhysics, runningPhysics, presentTime)`

INTERNAL

### `c3po.services.ListingWriter.goToLastBox(listingFile)`

INTERNAL

### `c3po.services.ListingWriter.mergeListing(listingsName, newListingName)`

`mergeListing` allows to merge listing files produced by ListingWriter (or by previous call to `mergeListing`).

It is designed to produce a comprehensive view of a MPI calculation. Only the last listing box of the provided files are considered.

<div class="warning">

<div class="title">

Warning

</div>

Each of the provided files must contain one and only one listing (one table).

</div>

## Parameters

listingsName : list  
List of the name of the listing files to merge.

newListingName  
Name of the file to write.

### `c3po.services.ListingWriter.getTotalTimePhysicsDriver(listingName, physicsDriverName, methodNames=['initialize', 'computeTimeStep', 'initTimeStep', 'solveTimeStep', 'iterateTimeStep', 'validateTimeStep', 'setStationaryMode', 'abortTimeStep', 'resetTime', 'terminate', 'save', 'restore'])`

`getTotalTimePhysicsDriver` reads a listing file produced by `ListingWriter` or mergeListing and returns the total time spent by one `PhysicsDriver` in indicated methods (in the last calculation).

## Parameters

listingName  
Name of the listing file to read.

physicsDriverName  
Name (given in the listing file) of the `PhysicsDriver` for which the total time is requested.

methodNames : list  
List of the names of the methods to take into account. By defaut: everything but `"exchange": ["initialize", "computeTimeStep", "initTimeStep", "solveTimeStep", "iterateTimeStep", "validateTimeStep",  "setStationaryMode", "abortTimeStep", "resetTime", "terminate", "save", "restore"]`.

## Returns

> The total time spent by the `PhysicsDriver` in the indicated methods.

### `c3po.services.ListingWriter.getTimesExchanger(listingName, exchangerName, physicsDriverNames)`

`getTimesExchanger` reads a listing file produced by `ListingWriter` or mergeListing and returns time information about a chosen exchanger (during the last calculation).

For each `PhysicsDriver` involved in the exchange, the function distinguishes between exchange time and waiting time. The exchange is assumed to really begin when all involved `PhysicsDriver` enter the exchange. For each of them, the waiting time is the time spent in the exchange before they all enter it. The exchange time is the time from this "real beginning" to the end of the exchange (from the point of view of each `PhysicsDriver`).

## Parameters

listingName  
Name of the listing file to read.

exchangerName  
Name (given in the listing file) of the `Exchanger` for which time information is requested.

physicsDriverNames : list  
List of the names of the `PhysicsDriver` (given in the listing file) involved in the `Exchanger`. They must be really involved!

## Returns

list  
A list of `len(physicsDriverNames)` elements, in the same order than `physicsDriverNames`. Each element is a list of two values: first the total exchange time spent by this `PhysicsDriver` in the `Exchanger`, then its total waiting time in the `Exchanger`.
