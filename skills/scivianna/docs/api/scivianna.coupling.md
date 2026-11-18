<!-- source: api/scivianna.coupling.rst -->

# scivianna.coupling package

# Scivianna Coupling Module

The `coupling` module provides integration with the C3PO coupling platform and implements the ICOCO interface for code-to-code coupling in simulation workflows.

## Files

| File | Description |
|------|-------------|
| `__init__.py` | Package initialization file |
| `icoco.py` | ICOCO-compatible interface implementation for coupling with C3PO |
| `problem_server.py` | Server-side problem definition for coupled simulations |
| `visualizer.py` | Visualizer-specific coupling utilities and helpers |

## Purpose

This module enables Scivianna to participate in multi-physics coupling scenarios where multiple simulation codes exchange data during runtime. It implements the ICOCO standard interface used by the C3PO coupling tool.

## Key Classes

### LayoutProblem
Main class implementing the ICOCO `Problem` interface:
- Manages visualization panels during coupling
- Handles time stepping synchronization
- Transfers field data between codes
- Supports stationary and transient modes

### ICoCo Interface Methods
| Method | Purpose |
|--------|---------|
| `initialize()` | Initialize the visualizer server |
| `terminate()` | Clean up resources and save state |
| `presentTime()` | Return current simulation time |
| `computeTimeStep()` | Suggest next time step |
| `initTimeStep(dt)` | Set time step for computation |
| `solveTimeStep()` | Perform visualization update |
| `validateTimeStep()` | Confirm time step completion |
| `setInputMEDDoubleField()` | Receive field data from coupling |

## Usage Example

An example of working coupling is available in the scivianna_example module, c3po_coupling

## Field Naming Convention

Fields are identified using the format: `panel_name@field_name`

Example: `"main_view@temperature"`

## Update Policies

Supported update policies for coupled fields:
- `UPDATE_DATA`: Update and replaces field values on existing mesh
- `UPDATE_MESH`: Update and replaces both mesh and field values
- `APPEND_DATA`: Add new time-step data
- `APPEND_MESH`: Add new time-step with new mesh

## Dependencies

- ICOCO library (~=2.0.0)
- MEDCoupling (for MED field handling)
- C3PO coupling platform (runtime)

## References

- ICOCO API: https://github.com/cea-trust-platform/icoco-coupling
- C3PO: https://github.com/code-coupling/c3po Submodules ----------

## scivianna.coupling.icoco module

ICoCo compatible interface to couple the visualizer to other codes using the coupling tool C3PO

ICOCO interface API: <https://github.com/cea-trust-platform/icoco-coupling>

C3PO coupling tool: <https://github.com/code-coupling/c3po>

The process threads structure of a coupling with the visualiser works as follow:

            C3PO used process \| Slave 1 process \|  
  C3PO Thread - Visualizer thread \| Slave 1 thread \|

> - C3PO objects, and drivers creation
>
> - ---------------------------------------\> \* For each Visualization panel, a new process is created with a slave that will provide the data to the visualizer (1 in this example)
>
> - LayoutDriver initialisation
>
> - -------------------\> \* pn.serve() -\> creation of the visualizer thread \* -----------\> \* \* \<----------- \* At each update of a panel (requested by the visualizer thread, on a button clic for example), an exchange of request is done between the visualizer thread and its associated thread. \* The visualizer thread can then request itself to update the visualizer at the end of the tick based on the data received from the slave.
>
> - ---------------------------------------\> \* At each setInputMedFieldDouble call, the C3PO thread provides the slave associated to the field the new version of the field.
>
> - If the C3PO Thread requests an update to the Visualizer, in the end, the C3PO Thread requests a plot update, two cases: - The C3PO Thread doesn't have the hand on the plots, throwing an exception; - The C3PO Thread adds a task, it is not read by the Visualizer thread, therefore not updating.
>
>   > \* The visualizer update has to come from the Visualizer thread to be able to work:
>   > - A play button was added, if clicked, a periodic task is added (from the Visualizer thread which handles the GUI) every second to refresh the visualization;
>   > - The C3PO Thread will set a boolean to mark the need for an update;
>   > - At each periodic task, if the boolean is at True, the Visualizer thread refreshes the geometry

### `class scivianna.coupling.icoco.Value`

Container for ICoCo value name constants used in the coupling system.

## Attributes

UPDATE_RATE : str  
Key for the update rate parameter. Defines how frequently updates are performed (1 update per UPDATE_RATE calls to solveTimeStep).

NOTIFICATION_SUCCESS : str  
Key for success notifications displayed in the layout.

NOTIFICATION_INFO : str  
Key for informational notifications displayed in the layout.

NOTIFICATION_ERROR : str  
Key for error notifications displayed in the layout.

### `class scivianna.coupling.icoco.LayoutProblem(layout: GenericLayout, title='C3PO Coupling visualizer', show_server: bool=True, start: bool=True)  — bases: Problem`

ICoCo Problem implementation for the C3PO coupling visualizer.

This class extends the ICoCo Problem interface to provide visualization capabilities through Panel. It manages the simulation time stepping, field data exchange, and connection monitoring for client sessions.

#### `LayoutProblem.setDataFile(self, datafile: str) -> None`

(Optional) Provide the relative path of a data file to be used by the code.

This method must be called before initialize().

## Parameters

datafile : str  
relative path to the data file.

## Raises

WrongContext  
exception if called multiple times or after initialize().

WrongArgument  
exception if an invalid path is provided.

#### `LayoutProblem.initialize(self) -> bool`

Initialize the current problem instance.

In this method the code should allocate all its internal structures and be ready to execute.

File reads, memory allocations, and other operations likely to fail should be performed here, and not in the constructor (and not in the setDataFile() or in the setMPIComm() methods either).

This method must be called only once (after a potential call to setMPIComm() and/or setDataFile()) and cannot be called again before terminate() has been performed.

## Returns

bool  
True if all OK, otherwise False.

## Raises

WrongContext  
Raised if called multiple times or after initialize().

#### `LayoutProblem.wait_for_disconnect(self, poll_interval: float=0.5) -> None`

Wait until all client connections have been disconnected.

This method blocks the calling thread until no active connections remain. It polls at the specified interval to check for remaining connections.

## Parameters

poll_interval : float, optional  
Time in seconds between connection checks (default: 0.5).

#### `LayoutProblem.terminate(self) -> None`

Terminate the current problem instance and release all allocated resources.

Terminate the computation, free the memory and save whatever needs to be saved.

This method is called once at the end of the computation or after a non-recoverable error. No other ICoCo method except setDataFile(), setMPIComm() and initialize() may be called after this.

## Raises

WrongContext  
Raised if called before initialize() or after terminate().

WrongContext  
Raised if called inside the TIME_STEP_DEFINED context (see Problem documentation).

#### `LayoutProblem.presentTime(self) -> float`

Return the current time of the simulation.

This method can be called any time between initialize() and terminate(). The current time can only change during a call to validateTimeStep() or to reset_time().

## Returns

float  
The current (physical) time of the simulation.

## Raises

WrongContext  
Raised if called before initialize() or after terminate().

#### `LayoutProblem.computeTimeStep(self) -> Tuple[float, bool]`

Return the next preferred time step and whether to stop.

Both values are only indicative; the supervisor is not required to take them into account. This method is marked as mandatory since most of the coupling schemes expect the code to provide this information (those schemes then typically compute the minimum of the time steps of all the codes being coupled).

This method can be called whenever the code is outside the TIME_STEP_DEFINED context (see Problem documentation).

## Returns

Tuple\[float, bool\]  
A tuple containing:

- The preferred time step for this code (only valid if stop is False).
- Stop flag set to True if the code wants to stop. It can be used to indicate that, according to a certain criterion, the end of the transient computation is reached from the code point of view.

## Raises

WrongContext  
Raised if called before initialize() or after terminate().

WrongContext  
Raised if called inside the TIME_STEP_DEFINED context (see Problem documentation).

#### `LayoutProblem.initTimeStep(self, dt: float) -> bool`

Provide the next time step (time increment) to be used by the code.

After this call (if successful), the computation time step is defined to \]t, t + dt\] where t is the value returned by presentTime(). The code enters the TIME_STEP_DEFINED context.

A time step of 0.0 may be used when the stationaryMode is set to True for codes solving directly for the steady-state.

## Parameters

dt : float  
The time step to be used by the code.

## Returns

bool  
False means the given time step is not compatible with the code time scheme.

## Raises

WrongContext  
Raised if called before initialize() or after terminate().

WrongContext  
Raised if called inside the TIME_STEP_DEFINED context (see Problem documentation).

WrongContext  
Raised if called several times without resolution.

WrongArgument  
Raised if dt is invalid (dt \< 0.0).

#### `LayoutProblem.solveTimeStep(self) -> bool`

Perform the computation on the current time interval.

This method can be called whenever the code is inside the TIME_STEP_DEFINED context (see Problem documentation).

If the update rate has been reached, it marks panels for recomputation and triggers a visual update.

## Returns

bool  
True if computation was successful, False otherwise.

## Raises

WrongContext  
Raised if called before initialize() or after terminate().

WrongContext  
Raised if called outside the TIME_STEP_DEFINED context (see Problem documentation).

WrongContext  
Raised if called several times without a call to validateTimeStep() or abortTimeStep().

#### `LayoutProblem.validateTimeStep(self) -> None`

Validate the computation performed by solveTimeStep.

This method can be called whenever the code is inside the TIME_STEP_DEFINED context (see Problem documentation).

After this call:

- The present time has been advanced to the end of the computation time step.
- The computation time step is undefined (the code leaves the TIME_STEP_DEFINED context).

## Raises

WrongContext  
Raised if called before initialize() or after terminate().

WrongContext  
Raised if called outside the TIME_STEP_DEFINED context (see Problem documentation).

WrongContext  
Raised if called before the solveTimeStep() method.

#### `LayoutProblem.abortTimeStep(self)`

Abort the current time step computation.

Resets the time step to None without validating the computation.

#### `LayoutProblem.setStationaryMode(self, stationaryMode: bool) -> None`

Set whether the code should compute a stationary or transient solution.

New in version 2 of ICoCo. By default the code is assumed to be in stationary mode False (i.e., set up for a transient computation).

If set to True, solveTimeStep() can be used either to solve a time step in view of an asymptotic solution, or to solve directly for the steady-state. In this last case, a time step of 0. can be used with initTimeStep() (whose call is always needed).

The stationary mode status of the code can only be modified by this method (or by a call to terminate() followed by initialize()).

## Parameters

stationaryMode : bool  
True if the code should compute a stationary solution.

## Raises

WrongContext  
Raised if called inside the TIME_STEP_DEFINED context (see Problem documentation).

WrongContext  
Raised if called before initialize() or after terminate().

#### `LayoutProblem.getStationaryMode(self) -> bool`

Indicate whether the code should compute a stationary or transient solution.

See also setStationaryMode().

This method can be called whenever the code is outside the TIME_STEP_DEFINED context (see Problem documentation).

## Returns

bool  
True if the code has been set to compute a stationary solution.

## Raises

WrongContext  
Raised if called before initialize() or after terminate().

WrongContext  
Raised if called inside the TIME_STEP_DEFINED context (see Problem documentation).

#### `LayoutProblem.getValueType(self, name: str) -> ValueType`

Get the value type for a given parameter name.

## Parameters

name : str  
The name of the parameter to query.

## Returns

ValueType  
The ICoCo value type corresponding to the name.

## Raises

NotImplemetedError  
Raised if the name is not recognized.

#### `LayoutProblem.getInputValuesNames(self)`

Get the list of input value names.

## Returns

list of str  
List of input value parameter names.

#### `LayoutProblem.setInputIntValue(self, name: str, val: float)`

Set an integer input value by name.

## Parameters

name : str  
Name of the scalar value to set.

val : float  
Value passed to the code.

## Raises

WrongArgument  
Raised if the scalar name is invalid.

#### `LayoutProblem.setInputStringValue(self, name: str, val: str)`

Set an string input value by name.

## Parameters

name : str  
Name of the scalar value to set.

val : float  
Value passed to the code.

## Raises

WrongArgument  
Raised if the scalar name is invalid.

#### `LayoutProblem.getInputMEDDoubleFieldTemplate(self, name: str) -> medcoupling.MEDCouplingFieldDouble`

Retrieve an empty shell for an input field.

This shell can be filled by the caller and then given to the code via setInputField(). The field has the MEDDoubleField format.

The code uses this method to populate 'afield' with all the data that represents the context of the field (i.e., its support mesh, its discretization -- on nodes, on elements, ...). The remaining job for the caller is to fill the actual values of the field itself. When this is done, the field can be sent back to the code through setInputField().

This method is not mandatory but is useful to know the mesh, discretization, etc. on which an input field is expected.

See Problem documentation for more details on the time semantic of a field.

## Parameters

name : str  
Name of the field for which we would like the empty shell. The format should be "<visualization_panel@field>\_name".

## Returns

medcoupling.MEDCouplingFieldDouble  
Field object (in MEDDoubleField format) that will be populated with all the contextual information. Any previous information in this object will be discarded.

## Raises

WrongContext  
Raised if called before initialize() or after terminate().

WrongArgument  
Raised if the field name is invalid.

#### `LayoutProblem.setInputMEDDoubleField(self, name: str, afield: medcoupling.MEDCouplingFieldDouble) -> None`

Provide the code with input data in the form of a MEDDoubleField.

The method getInputFieldTemplate(), if implemented, may be used first to prepare an empty shell of the field to pass to the code.

See Problem documentation for more details on the time semantic of a field.

## Parameters

name : str  
Name of the field that is given to the code. The format should be "<visualization_panel@field>\_name".

afield : medcoupling.MEDCouplingFieldDouble  
Field object (in MEDDoubleField format) containing the input data to be read by the code. The name of the field set on this instance (with the Field::setName() method) should not be checked. However its time value should ensure it is within the proper time interval \]t, t+dt\].

## Returns

None

## Raises

WrongContext  
Raised if called before initialize() or after terminate().

WrongArgument  
Raised if the field name ('name' parameter) is invalid.

WrongArgument  
Raised if the time property of 'afield' does not belong to the currently computed time step \]t, t + dt\].

#### `LayoutProblem.setInputDoubleValue(self, name: str, val: float) -> None`

Provide the code with a scalar double data.

See Problem documentation for more details on the time semantic of a scalar value.

## Parameters

name : str  
Name of the scalar value that is given to the code. The format should be "<visualization_panel@field>\_name".

val : float  
Value passed to the code.

## Returns

None

## Raises

WrongArgument  
Raised if the scalar name ('name' parameter) is invalid.

WrongContext  
Raised if called before initialize() or after terminate(). scivianna.coupling.problem_server module -----------------------------------------

This module contains a functional client-server implementation of ICoCo `Problem`. It helps moving scivianna on another process to prevent it to slow down the ongoing simulation.

## Warning

> This is an experimental module.

### `class scivianna.coupling.problem_server.ServerManager  — bases: BaseManager`

Manager class to register remote ICoCo `Problem` implementations.

This class extends Python's BaseManager to allow registration of Problem classes that will be executed on a remote server process, enabling distributed visualization.

## See Also

ProblemClient : Client-side proxy for remote problems.

#### `ServerManager.register(cls, class_type: Type, *args, **kwargs) -> str`

Register a remote class for distributed execution.

## Parameters

class_type : Type  
The Problem class to use on the server side.

*args : tuple Additional positional arguments passed to the server class constructor.*\*kwargs : dict  
Additional keyword arguments passed to the server class constructor.

## Returns

str  
The typeid string to use as the `ProblemClient` argument.

## Raises

ValueError  
Raised if the class typeid is already registered.

### `class scivianna.coupling.problem_server.RemoteException  — bases: Exception`

Exception raised when a remote process fails.

This exception wraps the traceback and error details from the remote server process to help diagnose failures in distributed execution.

## See Also

ProblemClient : Uses this exception to communicate remote errors.

### `scivianna.coupling.problem_server.redirect_icoco_to_server(cls)`

Decorator that redirects ICoCo methods to the remote server.

This decorator dynamically assigns all ICoCo protocol methods to the decorated class, routing each call through the `_method` helper to the underlying remote problem instance. It also removes any abstract method restrictions from the class.

## Parameters

cls : type  
The class to decorate. Must have an `__abstractmethods__` attribute.

## Returns

type  
The decorated class with ICoCo methods redirected to server.

## Raises

AttributeError  
Raised if the class does not have an `__abstractmethods__` attribute.

## See Also

\_method : The helper function that performs the actual method redirection.

### `class scivianna.coupling.problem_server.ProblemClient(typeid: str, *args, **kwargs) -> None  — bases: Problem`

Server-Client implementation of ICoCo Problem for distributed execution.

This class acts as a proxy that delegates all ICoCo method calls to a remote server process running the actual Problem implementation. It enables visualization without slowing down the main simulation.

## Examples

\>\>\> typeid = ServerManager.register(MyProblem) \>\>\> client = ProblemClient(typeid=typeid, arg1=val1) \>\>\> client.initialize()

## See Also

ServerManager : Registers and starts the remote problem server. scivianna.coupling.visualizer module ------------------------------------

Coupling visualizer for Scivianna.

This module provides visualization capabilities for code coupling using ICoCo/C3PO.

### `class scivianna.coupling.visualizer.CouplingPanel  — bases: BaseModel`

Base model for coupling visualization panels.

This class defines the common properties shared by all coupling panel types, including name, update policy, interface configuration, and field templates.

## Attributes

name : str  
Plot panel name.

update_policy : UpdatePolicy  
Code interface management definition.

interface : Type\[GenericInterface\]  
Code interface type.

## Example

\>\>\> panel = CouplingPanel( ... name="temperature", ... update_policy=UpdatePolicy.UPDATE_DATA, ... interface=MyInterface ... )

#### `CouplingPanel.resolve_interface(cls, v)`

Validate and resolve the interface attribute.

Converts string interface identifiers to their corresponding interface classes using the global INTERFACES registry.

## Parameters

v : any  
The interface value to validate (type or string).

## Returns

Type\[GenericInterface\]  
The resolved interface class.

## Raises

ValueError  
Raised if the string identifier is not found in scivianna INTERFACES.

TypeError  
Raised if the value is neither a type nor a string.

### `class scivianna.coupling.visualizer.FieldPanel  — bases: CouplingPanel`

Panel configuration for 2D field visualization.

Extends CouplingPanel with 2D geometry-specific properties including coordinate system vectors, axis bounds, and display settings.

## Attributes

interface : Type\[Geometry2D\]  
2D Geometry code interface type.

u : tuple\[float, float, float\] \| None  
Horizontal axis vector.

v : tuple\[float, float, float\] \| None  
Vertical axis vector.

origin : tuple\[float, float, float\] \| None  
Physical 3D position of the slice center

size_u : float \| None  
Size of the slice along the u axis.

size_v : float \| None  
Size of the slice along the v axis.

color_map : str \| None  
Plot color map name.

displayed_fields : str  
Displayed field when the GUI is opened.

## Example

\>\>\> panel = FieldPanel( ... name="temperature_field", ... interface=SomeInterface, ... u=(1.0, 0.0, 0.0), ... v=(0.0, 1.0, 0.0), ... origin=(0.5, 0.5, 0.0), ... size_u=1.0, ... size_v=1.0, ... color_map="viridis", ... displayed_field="power" ... )

### `class scivianna.coupling.visualizer.ValuePanel  — bases: CouplingPanel`

Panel configuration for 1D value visualization.

Extends CouplingPanel with 1D plot-specific properties including axis bounds and data interface type.

## Attributes

min_time : Optional\[NonNegativeFloat\]  
1D plot minimum horizontal axis value.

max_time : Optional\[PositiveFloat\]  
1D plot maximum horizontal axis value.

min_value : Optional\[NonNegativeFloat\]  
1D plot minimum vertical axis value.

max_value : Optional\[PositiveFloat\]  
1D plot maximum vertical axis value.

interface : Union\[Type\[Value1DAtLocation\], Type\[ValueAtLocation\]\]  
1D data code interface type.

displayed_fields : List\[str\]  
List of displayed fields when the GUI is opened.

## Example

\>\>\> panel = ValuePanel( ... name="pressure_at_point", ... interface=ValueAtLocation, ... min_time=0.0, ... max_time=10.0, ... displayed_fields=\["min", "max"\] ... )

### `class scivianna.coupling.visualizer.GridLayoutData  — bases: BaseModel`

Grid layout configuration for visualization panels.

Defines a 2D grid structure where each cell contains either a FieldPanel, ValuePanel, or None (for empty cells). Includes automatic validation to ensure panel names are unique.

## Attributes

grid : List\[List\[Optional\[Union\[FieldPanel, ValuePanel\]\]\]\]  
2D grid of visualization panels.

title : str  
Title for the layout.

## Example

\>\>\> layout = GridLayoutData( ... title="Temperature Distribution", ... grid=\[ ... \[field_panel_1, field_panel_2\], ... \[None, value_panel\] ... \] ... )

#### `GridLayoutData.check(self)`

Validates that all panel names in the grid are unique.

### `class scivianna.coupling.visualizer.SplitLayoutData  — bases: BaseModel`

Recursive split layout configuration for visualization panels.

Defines a hierarchical tree structure where panels can be split vertically or horizontally. Supports nested layouts for complex visual arrangements. Includes automatic validation to ensure panel names are unique.

## Attributes

split : List\[Union\[FieldPanel, ValuePanel, "SplitLayoutData"\]\]  
List of child elements (panels or nested split layouts).

vertical_cut : bool  
Direction of the cut between panels: True for vertical separator, False for horizontal separator.

name : str  
Name identifier for the layout section.

## Example

\>\>\> layout = SplitLayoutData( ... name="analysis_view", ... vertical_cut=True, ... split=\[field_panel, value_panel\] ... )

#### `SplitLayoutData.check(self)`

Validates that all panel names in the split layout are unique.

#### `SplitLayoutData.get_panels(self) -> List[Union[FieldPanel, ValuePanel]]`

Get all FieldPanel and ValuePanel objects in this layout and children.

Recursively traverses the split layout tree to collect all leaf panel objects (FieldPanel and ValuePanel).

## Returns

List\[Union\[FieldPanel, ValuePanel\]\]  
List of all actual panels contained in the layout hierarchy.

## Raises

TypeError  
Raised if one of the contained objects is not implemented (i.e., not a FieldPanel, ValuePanel, or SplitLayoutData).

#### `SplitLayoutData.get_serializable(self) -> 'SplitLayoutData'`

Get a serializable version of this layout.

Replaces interface type objects with their string keys so the layout can be serialized to JSON. Recursively processes all nested SplitLayoutData objects.

## Returns

SplitLayoutData  
A new SplitLayoutData instance with serializable interface references.

## Raises

TypeError  
Raised if self contains a not implemented type.

#### `SplitLayoutData.build_item(self, panels: Dict[str, VisualizationPanel]) -> SplitLayout`

Build a SplitLayout widget from the panel configuration.

Recursively constructs Panel widgets from the layout data using the provided visualization panel dictionary.

## Parameters

panels : Dict\[str, VisualizationPanel\]  
Dictionary mapping panel names to VisualizationPanel instances.

## Returns

SplitLayout  
The constructed SplitLayout widget.

## Raises

ValueError  
Raised if the split list is empty.

TypeError  
Raised if contained objects are not implemented types.

### `scivianna.coupling.visualizer.get_serializable_data(visualiser_data: Union[GridLayoutData, SplitLayoutData]) -> Union[GridLayoutData, SplitLayoutData]`

Get a serializable version of the visualization layout data.

Converts interface type objects to their string keys for JSON serialization. Handles both GridLayoutData and SplitLayoutData input types.

## Parameters

visualiser_data : Union\[GridLayoutData, SplitLayoutData\]  
The visualization layout data to serialize.

## Returns

Union\[GridLayoutData, SplitLayoutData\]  
A new layout instance with serializable interface references.

## Raises

AssertionError  
Raised if an interface is not registered in scivianna interfaces.

### `class scivianna.coupling.visualizer.GridStackProblem(working_directory: Path, show_server: bool=True, start: bool=True)  — bases: LayoutProblem`

ICoCo Problem for grid-stack visualization layouts.

Extends LayoutProblem to support GridStackLayout-based visualizations where panels are arranged in a fixed grid structure.

#### `GridStackProblem.setDataFile(self, datafile)`

Set the data file path for the layout configuration.

## Parameters

datafile : Path or str  
Path to the layout configuration file.

## Returns

Result of parent setDataFile call.

## Raises

TypeError  
Raised if datafile is not a Path or string.

#### `GridStackProblem.initialize(self)`

Initialize the GridStackProblem visualization.

Reads the layout configuration from the data file path and creates the GridStackLayout with appropriate visualization panels.

### `class scivianna.coupling.visualizer.SplitLayoutProblem(working_directory: Path, show_server: bool=True, start: bool=True)  — bases: LayoutProblem`

ICoCo Problem for split-tree visualization layouts.

Extends LayoutProblem to support SplitLayout-based visualizations where panels are arranged in a recursive tree structure with horizontal or vertical splits.

#### `SplitLayoutProblem.setDataFile(self, datafile)`

Set the data file path for the layout configuration.

## Parameters

datafile : Path or str  
Path to the layout configuration file.

## Returns

Result of parent setDataFile call.

## Raises

TypeError  
Raised if datafile is not a Path or string.

#### `SplitLayoutProblem.initialize(self)`

Initialize the SplitLayoutProblem visualization.

Reads the layout configuration from the data file path and creates the SplitLayout with appropriate visualization panels.

### `scivianna.coupling.visualizer.get_problem(working_directory: Path, data_to_view: Union[GridLayoutData, SplitLayoutData], use_server: bool=True, show: bool=True, start: bool=True) -> Tuple[Union[GridStackProblem, SplitLayoutProblem], str]`

Create visualization objects from a working directory and layout data.

This function creates the appropriate ICoCo problem (GridStackProblem or SplitLayoutProblem) based on the input data type, optionally running it in a separate server process for better performance.

## Parameters

working_directory : Path  
Directory where the MED files and visualization config are stored.

data_to_view : Union\[GridLayoutData, SplitLayoutData\]  
Layout data defining what to display.

use_server : bool, optional  
Whether to use a separate server process for the visualizer (default: True). Running in a server prevents the visualizer from slowing down the main simulation.

show : bool, optional  
Whether to display the server window on start (default: True).

start : bool, optional  
Whether to start a server to access the layout (default: True).

## Returns

Tuple\[Union\[GridStackProblem, SplitLayoutProblem\], str\]  
A tuple containing:

- The ICoCo problem instance for the visualizer.
- The path to the serialized visualization data file (visu.json).

## Examples

\>\>\> layout = GridLayoutData(title="Test", grid=\[\[field_panel\]\]) \>\>\> problem, data_file = get_problem(Path("."), layout) Module contents ---------------

ICoCo/C3PO coupling support for scivianna visualization.
