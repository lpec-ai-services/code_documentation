<!-- source: https://tripoli5.asnr.dev/documentation/latest-release/api/patmos-api.html -->

# The PATMOS API

The description of PATMOS

## tripoli5.utils module

utils is a submodule of `tripoli5`.

*class* tripoli5.utils.DataBufferStrategyName
:   Members:

    Lru

    Fifo

    Fifo *= <DataBufferStrategyName.Fifo: 1>*

    Lru *= <DataBufferStrategyName.Lru: 0>*

    __init__(*value: SupportsInt*) → None

    *property* name

    *property* value

*class* tripoli5.utils.DataDecompositionParameters
:   __init__(**args*, ***kwargs*)
    :   Overloaded function.

        1. __init__(self: tripoli5.utils.DataDecompositionParameters, global_data_size: typing.SupportsInt, remote_read_only: bool = True) -> None
        2. __init__(self: tripoli5.utils.DataDecompositionParameters, global_data_size: typing.SupportsInt, strategy: str | None, overload_buffer_size_rate: typing.SupportsFloat | None = 0.5) -> None

*exception* tripoli5.utils.PATMOSException

*exception* tripoli5.utils.PATMOSFileNotFoundError

*exception* tripoli5.utils.PATMOSLostInitError

*exception* tripoli5.utils.PATMOSLostTrackingError

*exception* tripoli5.utils.PATMOSNotImplemented

*exception* tripoli5.utils.PATMOSOutOfRange

*exception* tripoli5.utils.PATMOSRuntimeError

*exception* tripoli5.utils.PATMOSValueError

## tripoli5.geometry module

`geometry` contains TRIPOLI-5 objects common to all geometry engines (AGORA, ROOT…).

*class* tripoli5.geometry.IGeoNavigator
:   __init__(**args*, ***kwargs*)

    *property* nb_volumes

*class* tripoli5.geometry.IGeometry
:   __init__(**args*, ***kwargs*)

    *property* materials

    *property* nb_volumes

*class* tripoli5.geometry.Index
:   Members:

    OUTSIDE_WORLD

    BOUNDARY

    WIREFRAME_ONLY_BACKGROUND

    LOST_PARTICLE

    BOUNDARY *= <Index.BOUNDARY: -2>*

    LOST_PARTICLE *= <Index.LOST_PARTICLE: -4>*

    OUTSIDE_WORLD *= <Index.OUTSIDE_WORLD: -1>*

    WIREFRAME_ONLY_BACKGROUND *= <Index.WIREFRAME_ONLY_BACKGROUND: -3>*

    __init__(*value: SupportsInt*) → None

    *property* name

    *property* value

*class* tripoli5.geometry.Plotter
:   A Plotter for geometry.

    __init__(*geometry: tripoli5.geometry.IGeometry*) → None
    :   Constructor for Plotter

    query(*plane_cut: str*, *altitude: typing.SupportsFloat*, *u_min: typing.SupportsFloat*, *u_max: typing.SupportsFloat*, *v_min: typing.SupportsFloat*, *v_max: typing.SupportsFloat*, *coloring: str = 'material'*, *resolution: typing.SupportsInt = 20*, *mode: str = 'track'*, *nb_threads: typing.SupportsInt*, *ignore_bc: bool*) → tuple[list[int], int, int]
    :   Query the material or volume over a frame defined by plane, altitude, mins and maxs

*class* tripoli5.geometry.PushAcrossBoundaryResult
:   __init__(**args*, ***kwargs*)

    *property* albedo

    *property* distance

`agora` is a submodule of [`tripoli5.geometry`](#module-tripoli5.geometry). It is the main entry point for using the AGORA geometry engine in TRIPOLI-5 simulations.

*class* tripoli5.geometry.agora.AGORAGeoNavigator
:   __init__(*geometry: tripoli5.agora.Geometry*, *ignore_bc: bool = False*) → None
    :   Constructor for AGORAGeoNavigator

    computeDistanceToNextBoundary(*distance: SupportsFloat*) → bool
    :   Check whether a trial distance is smaller than the distance to the next boundary

        > distance : float
        > :   the trial distance (to be compared to the distance to the next boundary), i.e. the distance to the next collision for instance
        >
        > bool
        > :   True if a particle virtually pushed by the given distance has not left the volume,
        >     False otherwise
        >
        > In the case of a non convex volume, if the particle that is pushed with the trial distance is still in the volume but if the corresponding flight does not entirely lie in the volume, then the method must return False.

    *property* current_direction
    :   Current direction (Direction)

    *property* current_material
    :   Current material (str)

    *property* current_point
    :   Current point (Point)

    *property* current_volume_rank
    :   Rank of the current volume (int)

    initializeNavigation(*point: tripoli5.core.euclide.Point*, *direction: tripoli5.core.euclide.Direction*, *flush_surfaces: bool = True*) → None
    :   Locate a point with a given direction in the geometry

        > Updates the internal state of the navigator (namely the current point, current direction, current volume and current material)
        >
        > point : Point
        > :   the queried point
        >
        > direction : Direction
        > :   the queried direction
        >
        > flush_surfaces : bool
        > :   a boolean indicating whether we flush the internal surfaces (True by default)
        >
        > The direction is useful for edge cases (particle on a boundary, etc.).

    isInsideGeometry() → bool
    :   Check whether the current point is still inside the geometry

        > bool
        > :   True if the navigator is in the geometry,
        >     False otherwise

    isLost() → bool
    :   Check whether the navigator is a lost state (unsafe to use later)

        > bool
        > :   True if the navigator is in a lost state (after the initialization or tracking),
        >     False otherwise

    locate(*point: tripoli5.core.euclide.Point*, *flush_surfaces: bool = True*) → None
    :   Locate a point with the current direction (assumed to be set) in the geometry

        > Updates the internal state of the navigator (namely the current point, current direction, current volume and current material)
        >
        > point : Point
        > :   the queried point
        >
        > flush_surfaces : bool
        > :   a boolean indicating whether we flush the internal surfaces (True by default)

    *property* number_volumes
    :   Number of AGORA leaf volumes in the whole geometry (including “outside” leaves) (int)

    pushAcrossBoundary() → tripoli5.geometry.PushAcrossBoundaryResult
    :   Push the current point to the next boundary and finds the next volume

        > Updates the internal state of the navigator
        >
        > PushAcrossBoundaryResult
        > :   a struct containing the distance to the next boundary and an optional float corresponding to the albedo if a boundary condition has been crossed

    pushCurrentPoint(*distance: SupportsFloat*) → None
    :   Push the current point with a given distance (assumed to be shorter than the distance to the next boundary!)

        > Updates the internal state of the navigator
        >
        > distance : float
        > :   the distance to push the current point with

    updateDirection(*direction: tripoli5.core.euclide.Direction*) → None
    :   Update the current direction

        > Updates the internal state of the navigator
        >
        > direction : Direction
        > :   the new direction

*class* tripoli5.geometry.agora.AGORAGeometry
:   __init__(**args*, ***kwargs*)
    :   Overloaded function.

        1. __init__(self: tripoli5.geometry.agora.AGORAGeometry, filename: str) -> None

        Constructor of AGORAGeometry object

        2. __init__(self: tripoli5.geometry.agora.AGORAGeometry, geom: tripoli5.agora.Geometry) -> None

        Constructor of AGORAGeometry object

`root` is a submodule of [`tripoli5.geometry`](#module-tripoli5.geometry). It is the main entry point for using the ROOT geometry engine in TRIPOLI-5 simulations.

*class* tripoli5.geometry.root.ROOTGeoNavigator
:   __init__(*root_geometry: tripoli5.geometry.root.ROOTGeometry*) → None
    :   Constructor for ROOTGeoNavigator

    computeDistanceToNextBoundary(*distance: SupportsFloat*) → bool
    :   Check whether a trial distance is smaller than the distance to the next boundary

        > distance : float
        > :   the trial distance (to be compared to the distance to the next boundary), i.e. the distance to the next collision for instance
        >
        > bool
        > :   True if a particle virtually pushed by the given distance has not left the volume,
        >     False otherwise
        >
        > In the case of a non convex volume, if the particle that is pushed with the trial distance is still in the volume but if the corresponding flight does not entirely lie in the volume, then the method must return False.

    *property* current_direction
    :   Current direction (Direction)

    *property* current_material
    :   Current material (str)

    *property* current_point
    :   Current point (Point)

    *property* current_volume_rank
    :   Rank of the current volume (int)

    initializeNavigation(*point: tripoli5.core.euclide.Point*, *direction: tripoli5.core.euclide.Direction*, *flush_surfaces: bool = True*) → None
    :   Locate a point with a given direction in the geometry

        > Updates the internal state of the navigator (namely the current point, current direction, current volume and current material)
        >
        > point : Point
        > :   the queried point
        >
        > direction : Direction
        > :   the queried direction
        >
        > flush_surfaces : bool
        > :   a boolean indicating whether we flush the internal surfaces (True by default)
        >
        > The direction is useful for edge cases (particle on a boundary, etc.).

    isInsideGeometry() → bool
    :   Check whether the current point is still inside the geometry

        > bool
        > :   True if the navigator is in the geometry,
        >     False otherwise

    isLost() → bool
    :   Check whether the navigator is a lost state (unsafe to use later)

        > bool
        > :   True if the navigator is in a lost state (after the initialization or tracking),
        >     False otherwise

    locate(*point: tripoli5.core.euclide.Point*, *flush_surfaces: bool = True*) → None
    :   Locate a point with the current direction (assumed to be set) in the geometry

        > Updates the internal state of the navigator (namely the current point, current direction, current volume and current material)
        >
        > point : Point
        > :   the queried point
        >
        > flush_surfaces : bool
        > :   a boolean indicating whether we flush the internal surfaces (True by default)

    *property* number_volumes
    :   Number of ROOT volumes in the whole geometry (int)

    pushAcrossBoundary() → tripoli5.geometry.PushAcrossBoundaryResult
    :   Push the current point to the next boundary and finds the next volume

        > Updates the internal state of the navigator
        >
        > PushAcrossBoundaryResult
        > :   a struct containing the distance to the next boundary and an optional float corresponding to the albedo if a boundary condition has been crossed

    pushCurrentPoint(*distance: SupportsFloat*) → None
    :   Push the current point with a given distance (assumed to be shorter than the distance to the next boundary!)

        > Updates the internal state of the navigator
        >
        > distance : float
        > :   the distance to push the current point with

    updateDirection(*direction: tripoli5.core.euclide.Direction*) → None
    :   Update the current direction

        > Updates the internal state of the navigator
        >
        > direction : Direction
        > :   the new direction

*class* tripoli5.geometry.root.ROOTGeometry
:   __init__(*filename: str*) → None
    :   Constructor of ROOTGeometry objects

    get_material_in_volume(*volume_rank: SupportsInt*) → str
    :   Return the name of the material in the given volume

    get_volume_path(*volume_rank: SupportsInt*) → str
    :   Return the ROOT path for the volume with the given rank

    get_volume_rank(*volume_path: str*) → int
    :   Return the rank of the volume with the given path

## tripoli5.materials module

materials is a submodule of `tripoli5`. It is the main entry point for materials description in Tripoli-5.

*class* tripoli5.materials.ACEURRDataLibraryArchiveSource
:   Archive source for [`ACEURRDataLibrary`](delos-api.md#tripoli5.delos.ACEURRDataLibrary)

    __init__(*catalog: tripoli5.delos.Catalog*) → None
    :   Library Constructor from a catalog

    has(*nuclide_name: str*, *temperature: SupportsFloat*) → bool
    :   Check if library contains nuclide at given temperature (expressed in K)

    printSummary() → None

*class* tripoli5.materials.ACEURRDataLibraryDirectorySource
:   Directory source for [`ACEURRDataLibrary`](delos-api.md#tripoli5.delos.ACEURRDataLibrary)

    __init__(*catalog: tripoli5.delos.Catalog*) → None
    :   Library Constructor from a catalog

    getAvailableTemperatures(*object_name: str*) → list[tripoli5.core.physics.Temperature]
    :   Return the list of available temperatures for a given object (e.g. “U235”)

    has(*nuclide_name: str*, *temperature: SupportsFloat*) → bool
    :   Check if library contains nuclide at given temperature (expressed in K)

    hasData(*object_name: str*) → bool
    :   Check if library contains a given object (e.g. “U235”) at any temperature

    printSummary() → None

    setReactionFilter(*filter: tripoli5.delos.IReactionFilter*) → None
    :   Filter given reactions (available reaction filters are available through the `delos` module)

*class* tripoli5.materials.CALENDFURRDataLibraryArchiveSource
:   Archive source for [`CALENDFURRDataLibrary`](delos-api.md#tripoli5.delos.CALENDFURRDataLibrary)

    __init__(*catalog: tripoli5.delos.Catalog*) → None
    :   Library Constructor from a catalog

    has(*nuclide_name: str*, *temperature: SupportsFloat*) → bool
    :   Check if library contains nuclide at given temperature (expressed in K)

    printSummary() → None

*class* tripoli5.materials.CALENDFURRDataLibraryDirectorySource
:   Directory source for [`CALENDFURRDataLibrary`](delos-api.md#tripoli5.delos.CALENDFURRDataLibrary)

    __init__(*catalog: tripoli5.delos.Catalog*) → None
    :   Library Constructor from a catalog

    getAvailableTemperatures(*object_name: str*) → list[tripoli5.core.physics.Temperature]
    :   Return the list of available temperatures for a given object (e.g. “U235”)

    has(*nuclide_name: str*, *temperature: SupportsFloat*) → bool
    :   Check if library contains nuclide at given temperature (expressed in K)

    hasData(*object_name: str*) → bool
    :   Check if library contains a given object (e.g. “U235”) at any temperature

    printSummary() → None

    setReactionFilter(*filter: tripoli5.delos.IReactionFilter*) → None
    :   Filter given reactions (available reaction filters are available through the `delos` module)

*class* tripoli5.materials.DopplerBroadeningMethod
:   Members:

    PreTabulated

    Sigma1

    Multipole

    Multipole *= <DopplerBroadeningMethod.Multipole: 2>*

    PreTabulated *= <DopplerBroadeningMethod.PreTabulated: 0>*

    Sigma1 *= <DopplerBroadeningMethod.Sigma1: 1>*

    __init__(*value: SupportsInt*) → None

    *property* name

    *property* value

*class* tripoli5.materials.EnergyRange
:   __init__(*arg0: tripoli5.materials.Threshold | None*, *arg1: tripoli5.materials.Threshold | None*) → None
    :   Constructor for class EnergyRange

    contains(*energy: tripoli5.core.physics.Energy*, *temperature: tripoli5.core.physics.Temperature*) → bool

    getLowerThreshold() → tripoli5.materials.Threshold | None

    getUpperThreshold() → tripoli5.materials.Threshold | None

*class* tripoli5.materials.EpithermalBroadeningParameters
:   __init__(**args*, ***kwargs*)

    add(*method: str*, *nuclide_selector: tripoli5.materials.NuclideSelector*) → tripoli5.materials.EpithermalBroadeningParameters
    :   Add a Method/NuclideSelector pair

    *static* defaultParams() → tripoli5.materials.EpithermalBroadeningParameters

    *static* empty() → tripoli5.materials.EpithermalBroadeningParameters

*class* tripoli5.materials.IACEURRDataLibrarySource
:   __init__(**args*, ***kwargs*)

*class* tripoli5.materials.ICALENDFURRDataLibrarySource
:   __init__(**args*, ***kwargs*)

*class* tripoli5.materials.IFieldConcentration
:   __init__(**args*, ***kwargs*)

*class* tripoli5.materials.IFieldDensity
:   __init__(**args*, ***kwargs*)

*class* tripoli5.materials.IFieldTemperature
:   __init__(**args*, ***kwargs*)

*class* tripoli5.materials.IMassDataLibrarySource
:   __init__(**args*, ***kwargs*)

*class* tripoli5.materials.IMedia
:   __init__(**args*, ***kwargs*)

*class* tripoli5.materials.INeutronDataLibrarySource
:   __init__(**args*, ***kwargs*)

*class* tripoli5.materials.IThermalDataLibrarySource
:   __init__(**args*, ***kwargs*)

*class* tripoli5.materials.MassDataLibraryArchiveSource
:   Archive source for [`MassDataLibrary`](delos-api.md#tripoli5.delos.MassDataLibrary)

    __init__(*catalog: tripoli5.delos.Catalog*) → None
    :   Library Constructor from a catalog

    has(*nuclide_name: str*, *temperature: SupportsFloat*) → bool
    :   Check if library contains nuclide at given temperature (expressed in K)

    printSummary() → None

*class* tripoli5.materials.MedCouplingFieldDensity
:   __init__(*a_field: object*, *unit: tripoli5.core.physics.Density.Units*) → None
    :   Constructor

*class* tripoli5.materials.MedCouplingFieldTemperature
:   __init__(*a_field: object*, *unit: tripoli5.core.physics.Temperature.Units*) → None
    :   Constructor

*class* tripoli5.materials.Mesh3DFieldLinear
:   __init__(*grid: tripoli5.core.grid.Mesh3DDoubleLinear*, *values: Annotated[numpy.typing.ArrayLike, numpy.int32]*) → None
    :   Create a Mesh3DField from a grid (tripoli5.core.grid.mesh3d) and a 3D numpy array.

    getValue(*arg0: tripoli5.core.euclide.Point*) → int
    :   Returns the value of the field given a position. Returns throws if the position is invalid.

    *property* maximum
    :   Maximum value stored in the field.

    *property* minimum
    :   Minimum value stored in the field.

    printSummary() → None
    :   Prints useful informations about the field and the mesh.

    *property* size
    :   Number of values stored in the field (and number of cells in the grid).

*class* tripoli5.materials.Mixture
:   __init__(**args*, ***kwargs*)

    get_concentrations(*id_: SupportsInt*) → list[float]

    modifyConcentration(**args*, ***kwargs*)
    :   Overloaded function.

        1. modifyConcentration(self: tripoli5.materials.Mixture, mass_data: tripoli5.materials.IMassDataLibrarySource, nuclide_name: str, value: typing.SupportsFloat) -> None

        Modify the concentration of a nuclide in the mixture in presence of a density field. Requires a Mass data source, the name of the nuclide, and a value. The resulting mixture may have the total density modified.

        2. modifyConcentration(self: tripoli5.materials.Mixture, mass_data: tripoli5.materials.IMassDataLibrarySource, id: typing.SupportsInt, nuclide_name: str, value: typing.SupportsFloat) -> None

        Modify the concentration of a nuclide in the mixture in presence of a concentration field. Requires the id of the concentration field to be modified, the name of the nuclide, and a value.

    *property* name

    *property* nuclides

    *property* number_of_nuclides

    printSummary() → None

*class* tripoli5.materials.MixtureBuilder
:   A helper to generate mixtures.

    __init__(**args*, ***kwargs*)
    :   Overloaded function.

        1. __init__(self: tripoli5.materials.MixtureBuilder) -> None
        2. __init__(self: tripoli5.materials.MixtureBuilder, [type_](#id9): str) -> None

        Constructor with the builder type choice. Possible types are: ‘concentrations’, ‘mass_fractions’, ‘atom_fractions’

    add(**args*, ***kwargs*)
    :   Overloaded function.

        1. add(self: tripoli5.materials.MixtureBuilder, nuclide_name: str, amount: typing.SupportsFloat) -> tripoli5.materials.MixtureBuilder

        Add a nuclide to the mixture. The amount is defined by the `type` that was selected at `MixtureBuilder`
        :   construction (concentration in at/barn-cm, atom fraction or mass fraction)

        2. add(self: tripoli5.materials.MixtureBuilder, nuclides_name: collections.abc.Sequence[str], amounts: collections.abc.Sequence[typing.SupportsFloat]) -> tripoli5.materials.MixtureBuilder

        Add several nuclides to the mixture

        3. add(self: tripoli5.materials.MixtureBuilder, id: typing.SupportsInt, nuclide_name: str, amount: typing.SupportsFloat) -> tripoli5.materials.MixtureBuilder

        Add a single nuclide and its amount to a specific ID in the mixture.
        :   Requires a concentration field defined with ‘withConcentrationField(field)’.
            If the ID is not already present, it is added with its nuclide concentration.
            If the nuclide is not already present in the mixture, it is added,
            and it is assigned a null concentration in all the other IDs.

        4. add(self: tripoli5.materials.MixtureBuilder, id: typing.SupportsInt, nuclide_names: collections.abc.Sequence[str], amounts: collections.abc.Sequence[typing.SupportsFloat]) -> tripoli5.materials.MixtureBuilder

        Add a set of nuclides and their amounts for a specific ID in the mixture.
        :   Requires a concentration field defined with ‘withConcentrationField(field)’.
            If the ID is not already present, it is added along with its corresponding nuclide concentrations.
            If any nuclide is not already present in the mixture, it is added,
            and it is assigned a null concentration in all the other IDs.

        5. add(self: tripoli5.materials.MixtureBuilder, ids: collections.abc.Sequence[typing.SupportsInt], nuclide_names: collections.abc.Sequence[str], amounts: collections.abc.Sequence[collections.abc.Sequence[typing.SupportsFloat]]) -> tripoli5.materials.MixtureBuilder

        Add multiple IDs, each with a set of nuclides and corresponding amounts.
        :   Requires a concentration field defined with ‘withConcentrationField(field)’.
            Each ID represents a unique mixture component, associated with a set of nuclides and their corresponding amounts.
            If any ID is not already present, it is added to the mixture along with its nuclide data.
            If any nuclide is not already present in the mixture, it is added,
            and it is assigned a null concentration in all the other IDs.

    build() → tripoli5.materials.Mixture
    :   Build the mixture using provided characteristics

    *property* summary
    :   The description of the current state of the builder.

    withCatalog(*catalog: tripoli5.delos.Catalog*) → tripoli5.materials.MixtureBuilder
    :   Specify the Nuclear Data library from which the atomic weight ratios will be read

    withConcentrationField(*concentration_field: tripoli5.materials.IFieldConcentration*) → tripoli5.materials.MixtureBuilder
    :   Set the concentration field
        When a concentration field is defined, you must use .add(id, nuclide, amount) instead of the global .add(nuclide, amount).
        The id refers to the composition ID stored in the field.

    withDensity(*density: tripoli5.core.physics.Density*) → tripoli5.materials.MixtureBuilder
    :   Set the density of the mixture

    withDensityField(*density_field: tripoli5.materials.IFieldDensity*) → tripoli5.materials.MixtureBuilder
    :   Set the density field

    withName(*name: str*) → tripoli5.materials.MixtureBuilder
    :   Set the name of the mixture

    withNaturalAbundances(*natural_abundances: tripoli5.materials.NaturalAbundances*) → tripoli5.materials.MixtureBuilder

    withTemperature(*temperature: tripoli5.core.physics.Temperature*) → tripoli5.materials.MixtureBuilder
    :   Set the temperature (if the mixture has a constant temperature, see [`withTemperatureField()`](#tripoli5.materials.MixtureBuilder.withTemperatureField) otherwise)

    withTemperatureField(*temperature_field: tripoli5.materials.IFieldTemperature*) → tripoli5.materials.MixtureBuilder
    :   Set the temperature field

*class* tripoli5.materials.MixtureBuilderAtomFractions
:   __init__() → None

*class* tripoli5.materials.MixtureBuilderConcentrations
:   __init__() → None

*class* tripoli5.materials.MixtureBuilderMassFractions
:   __init__() → None

*class* tripoli5.materials.NaturalAbundances
:   Reflects the nuclides natural abundances of an element.It is used by MixtureBuilder to replace missing natural elements with their corresponding nuclides.Amounts are expressed as atomic fractions.

    __init__(*origin: str*, *abundances: collections.abc.Mapping[str, collections.abc.Sequence[tuple[str, SupportsFloat]]]*, *error_tolerance: SupportsFloat = 0.01*, *warn_tolerance: SupportsFloat = 0.005*) → None
    :   Constructor for user-defined natural abundances. Ex: NaturalAbundances(‘mynat’, {‘H’: [(‘H1’, 0.3), (‘H2’, 0.7)]}). Sum of each natural element abundances must be equal to 1.0 within tolerances ‘error_tolerance’ and ‘warn_tolerance’.

    filterWithNuclidesIn(*neutron_data_library_source: tripoli5.materials.INeutronDataLibrarySource*, *temperature: tripoli5.core.physics.Temperature*) → None
    :   Filter the natural abundances with the nuclides present in the neutron data library at temperature T.

    *static* fromMORET6() → tripoli5.materials.NaturalAbundances
    :   Return the natural abundances table used by MORET6. Note that the nuclide names are given in uppercase, e.g. “CR” and “CR52”.

    *static* fromNUBASE2020() → tripoli5.materials.NaturalAbundances
    :   Return the natural abundances table recommended by the NUBASE 2020 evaluation. Note that the nuclide names are given in uppercase, e.g. “CR” and “CR52”.

    *static* fromOpenMC() → tripoli5.materials.NaturalAbundances
    :   Return the natural abundances table used by OpenMC. Note that the nuclide names are given in uppercase, e.g. “CR” and “CR52”.

    getElementNames() → list[str]

    getNuclideAbundance(*element_name: str*, *nuclide_name: str*) → float
    :   Returns 0.0 if the element or nuclide is not in the list of abundances

    hasElement(*element_name: str*) → bool

    *property* origin

*class* tripoli5.materials.NeutronDataLibraryArchiveSource
:   Archive source for [`NeutronDataLibrary`](delos-api.md#tripoli5.delos.NeutronDataLibrary)

    __init__(*catalog: tripoli5.delos.Catalog*) → None
    :   Library Constructor from a catalog

    has(*nuclide_name: str*, *temperature: SupportsFloat*) → bool
    :   Check if library contains nuclide at given temperature (expressed in K)

    printSummary() → None

*class* tripoli5.materials.NeutronDataLibraryDirectorySource
:   Directory source for [`NeutronDataLibrary`](delos-api.md#tripoli5.delos.NeutronDataLibrary)

    __init__(*catalog: tripoli5.delos.Catalog*) → None
    :   Library Constructor from a catalog

    getAvailableTemperatures(*object_name: str*) → list[tripoli5.core.physics.Temperature]
    :   Return the list of available temperatures for a given object (e.g. “U235”)

    has(*nuclide_name: str*, *temperature: SupportsFloat*) → bool
    :   Check if library contains nuclide at given temperature (expressed in K)

    hasData(*object_name: str*) → bool
    :   Check if library contains a given object (e.g. “U235”) at any temperature

    printSummary() → None

    setReactionFilter(*filter: tripoli5.delos.IReactionFilter*) → None
    :   Filter given reactions (available reaction filters are available through the `delos` module)

*class* tripoli5.materials.NeutronMedia
:   __init__(***, *ndl: tripoli5.materials.INeutronDataLibrarySource = None*, *tdl: tripoli5.materials.IThermalDataLibrarySource = None*, *audl: tripoli5.materials.IACEURRDataLibrarySource = None*, *cudl: tripoli5.materials.ICALENDFURRDataLibrarySource = None*, *opts: tripoli5.materials.Sigma1SchedulerOptions = SchedulerOptions(target=None, nb_threads=0, gpu_rate=0, offload_size=0, policy=Static)*) → None
    :   NeutronMedia Constructor

    getParticleType() → tripoli5.core.physics.ParticleType

    *property* number_of_media

    *property* number_of_nuclides

*class* tripoli5.materials.NeutronMediumBuilder
:   A builder for constructing media.

    __init__() → None
    :   Constructor for class NeutronMediumBuilder

    build() → tripoli5.materials.NeutronMedia
    :   Build the media to pass to the simulation

    withCatalog(*catalog: tripoli5.delos.Catalog*) → tripoli5.materials.NeutronMediumBuilder
    :   Specify the data catalog

    withCollisionSampler(*sampling_method: str*) → tripoli5.materials.NeutronMediumBuilder

    withDopplerBroadening(*doppler_broadening_method: str*, *base_temperature: tripoli5.core.physics.Temperature = Temperature(0.0, Temperature.Units.K)*, *max_energy: tripoli5.core.physics.Energy = Energy(1.0, Energy.Units.MeV)*) → tripoli5.materials.NeutronMediumBuilder
    :   Set the Doppler Broadening options. Possible methods are: “PreTabulated”, “Sigma1”

    withEnergyGridParameters(*search_type: str*, *n_hash_bins: SupportsInt = 1*) → tripoli5.materials.NeutronMediumBuilder
    :   Specify Energy grid parameters. Possible search types are: “BinarySearch”, “HashMap”

    withEpithermalBroadening(*parameter: tripoli5.materials.EpithermalBroadeningParameters*) → tripoli5.materials.NeutronMediumBuilder
    :   Set the Epithermal Broadnening options

    withLowerEnergyCut(*lower_bound: tripoli5.core.physics.Energy*) → tripoli5.materials.NeutronMediumBuilder
    :   Set the simulation lower bound

    withMixtures(*mixtures: collections.abc.Sequence[tripoli5.materials.Mixture]*) → tripoli5.materials.NeutronMediumBuilder
    :   A list of mixtures (material compositions)

    withOrigin(*source: str*) → tripoli5.materials.NeutronMediumBuilder
    :   Source of the nuclear data. Possible sources are: “Directory”, “Archive”

    withReactionFilter(*filter: tripoli5.delos.IReactionFilter*) → tripoli5.materials.NeutronMediumBuilder

    withSigma1Scheduler(*parameter: tripoli5.materials.Sigma1SchedulerOptions*) → tripoli5.materials.NeutronMediumBuilder
    :   Select the Sigma1 scheduler options

    withTSLThreshold(*energy: tripoli5.core.physics.Energy | None*) → tripoli5.materials.NeutronMediumBuilder

    withTemperatureInterpolationMethod(*temperature_interpolation_method: str*) → tripoli5.materials.NeutronMediumBuilder

    withURR(*parameter: str*) → tripoli5.materials.NeutronMediumBuilder
    :   Select the Unresolved Resonance Range options. Possible options are: “none”, “ace”, “calendf”

*class* tripoli5.materials.NuclideSelector
:   __init__(**args*, ***kwargs*)

    *static* all(*energy_range: tripoli5.materials.EnergyRange*) → tripoli5.materials.NuclideSelector
    :   Create a NuclideSelector for all nuclides in the system on a given energy range.

    *static* from_list(*list: collections.abc.Set[str]*, *energy_range: tripoli5.materials.EnergyRange*) → tripoli5.materials.NuclideSelector
    :   Create a NuclideSelector for a given list of nuclides in the system on a given energy range.

    *static* from_list_all_bounds(*list: collections.abc.Set[str]*, *energy_range: tripoli5.materials.EnergyRange*) → tripoli5.materials.NuclideSelector
    :   Create a NuclideSelector for all bound versions of a list of nuclides in the system on a given energy range.The name of the nuclides appearing in the list must correspond to the free (unbound) version (for instance H1, C12).

*class* tripoli5.materials.Particle
:   __init__(*type_: tripoli5.core.physics.ParticleType*, *point: tripoli5.core.euclide.Point*, *direction: tripoli5.core.euclide.Direction*, *energy: tripoli5.core.physics.Energy*, *time: SupportsFloat*, *weight: SupportsFloat*, *normalization: SupportsFloat*) → None
    :   Constructor for class Particle

    *property* direction

    *property* energy

    *property* historyId

    *property* normalization

    *property* position

    *property* speed

    *property* time

    *property* type_

    *property* weight

*class* tripoli5.materials.Sigma1SchedulerOptions
:   __init__(*target: str*, *nb_threads: SupportsInt*, *gpu_rate: SupportsFloat*, *offload_size: SupportsInt*, *policy: str*) → None
    :   Constructor. Possible targets are: none, host, cuda, openacc. Possible policies are: static, dynamic

    *property* gpu_rate

    *property* nb_threads

    *property* offload_size

    *property* policy

    *property* target

*class* tripoli5.materials.Sigma1SchedulerPolicy
:   Members:

    Static

    Dynamic

    Dynamic *= Sigma1SchedulerPolicy.Dynamic*

    Static *= Sigma1SchedulerPolicy.Static*

    __init__(*value: SupportsInt*) → None

    *property* name

    *property* value

*class* tripoli5.materials.Sigma1SchedulerTarget
:   Members:

    None

    Host

    Cuda

    OpenACC

    Cuda *= Sigma1SchedulerTarget.Cuda*

    Host *= Sigma1SchedulerTarget.Host*

    None *= Sigma1SchedulerTarget.None*

    OpenACC *= Sigma1SchedulerTarget.OpenACC*

    __init__(*value: SupportsInt*) → None

    *property* name

    *property* value

*class* tripoli5.materials.ThermalDataLibraryArchiveSource
:   Archive source for [`TSLDataLibrary`](delos-api.md#tripoli5.delos.TSLDataLibrary)

    __init__(*catalog: tripoli5.delos.Catalog*) → None
    :   Library Constructor from a catalog

    has(*nuclide_name: str*, *temperature: SupportsFloat*) → bool
    :   Check if library contains nuclide at given temperature (expressed in K)

    printSummary() → None

*class* tripoli5.materials.ThermalDataLibraryDirectorySource
:   Directory source for [`TSLDataLibrary`](delos-api.md#tripoli5.delos.TSLDataLibrary)

    __init__(*catalog: tripoli5.delos.Catalog*) → None
    :   Library Constructor from a catalog

    getAvailableTemperatures(*object_name: str*) → list[tripoli5.core.physics.Temperature]
    :   Return the list of available temperatures for a given object (e.g. “U235”)

    has(*nuclide_name: str*, *temperature: SupportsFloat*) → bool
    :   Check if library contains nuclide at given temperature (expressed in K)

    hasData(*object_name: str*) → bool
    :   Check if library contains a given object (e.g. “U235”) at any temperature

    printSummary() → None

    setReactionFilter(*filter: tripoli5.delos.IReactionFilter*) → None
    :   Filter given reactions (available reaction filters are available through the `delos` module)

*class* tripoli5.materials.Threshold
:   __init__(**args*, ***kwargs*)

    *static* energy(*energy: tripoli5.core.physics.Energy*) → tripoli5.materials.Threshold

    has_same_type(*rhs: tripoli5.materials.Threshold*) → bool

    *static* temperature_dependent(*value: SupportsFloat*) → tripoli5.materials.Threshold

    value() → float

*class* tripoli5.materials.URRParameters
:   __init__(***, *type_: str | None*) → None
    :   Constructor for class URRParameters

## tripoli5.score module

score is a submodule of `tripoli5`. It is the main entry point for scores description in Tripoli-5.

*class* tripoli5.score.BScore
:   __init__(**args*, ***kwargs*)

*class* tripoli5.score.FilterMEDMesh
:   __init__(*mesh: object*, *neutron_media: tripoli5.materials.NeutronMedia*, *material_name: str*, *nuclide_name: str*, *reaction: tripoli5.delos.ReactionId = ReactionId(18)*, *energy_min: SupportsFloat = 1e-11*, *energy_max: SupportsFloat = 20.0*, *nb_groups: SupportsInt = 100*, *name: str = 'FilterMEDMesh'*) → None
    :   Constructor

    writeFieldToVTKFile(*: tripoli5.score.MEDMeshScore*, *file_path: str*, *field: str*) → None

    writeToFile(*file_path: str*) → None

    writeToMEDFile(*file_path: str*) → None

*class* tripoli5.score.FluxSpectrumAllVolumes
:   __init__(**args*, ***kwargs*)
    :   Overloaded function.

        1. __init__(self: tripoli5.score.FluxSpectrumAllVolumes, nb_volumes: typing.SupportsInt, energy_min: typing.SupportsFloat = 1e-11, energy_max: typing.SupportsFloat = 20.0, nb_groups: typing.SupportsInt = 100, name: str = ‘FluxSpectrumAllVolumes’) -> None

        Constructor

        2. __init__(self: tripoli5.score.FluxSpectrumAllVolumes, decomposition_options: tripoli5.utils.DataDecompositionParameters, nb_volumes: typing.SupportsInt, energy_min: typing.SupportsFloat = 1e-11, energy_max: typing.SupportsFloat = 20.0, nb_groups: typing.SupportsInt = 100, name: str = ‘FluxSpectrumAllVolumes’) -> None

        Constructor

    writeToFile(*file_path: str*) → None

*class* tripoli5.score.FluxSpectrumAllVolumesGeneral
:   __init__(*nb_volumes: SupportsInt*, *energy_bounds: collections.abc.Sequence[SupportsFloat]*, *name: str*) → None
    :   Constructor

    writeToFile(*arg0: str*) → None

*class* tripoli5.score.FluxSpectrumCollAllVolumes
:   __init__(*nb_volumes: SupportsInt*, *energy_min: SupportsFloat = 1e-11*, *energy_max: SupportsFloat = 20.0*, *nb_groups: SupportsInt = 100*, *name: str = 'FluxSpectrumCollAllVolumes'*) → None
    :   Constructor

    writeToFile(*file_path: str*) → None

*class* tripoli5.score.FluxSpectrumCollAllVolumesGeneral
:   __init__(*nb_volumes: SupportsInt*, *energy_bounds: collections.abc.Sequence[SupportsFloat]*, *name: str*) → None
    :   Constructor

    writeToFile(*arg0: str*) → None

*class* tripoli5.score.FluxSpectrumCollGeneral
:   __init__(*arg0: collections.abc.Sequence[SupportsFloat]*, *arg1: str*) → None
    :   Constructor

    *property* energy_bounds

    writeToFile(*arg0: str*) → None

*class* tripoli5.score.FluxSpectrumCollMEDMesh
:   __init__(*mesh: object*, *energy_min: SupportsFloat = 1e-11*, *energy_max: SupportsFloat = 20.0*, *nb_groups: SupportsInt = 100*, *name: str = 'FluxSpectrumCollMEDMesh'*) → None
    :   Constructor

    writeFieldToVTKFile(*: tripoli5.score.MEDMeshScore*, *file_path: str*, *field: str*) → None

    writeToFile(*file_path: str*) → None

    writeToMEDFile(*file_path: str*) → None

*class* tripoli5.score.FluxSpectrumTrackGeneral
:   __init__(*arg0: collections.abc.Sequence[SupportsFloat]*, *arg1: str*) → None
    :   Constructor

    *property* energy_bounds

    writeToFile(*arg0: str*) → None

*class* tripoli5.score.GenScore
:   __init__(**args*, ***kwargs*)

    *property* mean
    :   The score mean

    *property* shape
    :   Retrieves number of bins for each dimension

    *property* var
    :   The score variance

*class* tripoli5.score.IMeshScore
:   __init__(**args*, ***kwargs*)

*class* tripoli5.score.IScore
:   __init__(**args*, ***kwargs*)

*class* tripoli5.score.KStep
:   __init__() → None

    reset() → None

    writeToFile(*arg0: str*) → None

*class* tripoli5.score.KappaFissionAllVolumes
:   The KappaFissionAllVolumes is used to compute the energy deposited by fission in each volume of the geometry. The energy deposition is retrieved from the Q value of the fission. Its unit is [MeV per source particle].

    __init__(*media: tripoli5.materials.NeutronMedia*, *nb_volumes: SupportsInt*, *energy_min: SupportsFloat = 1e-11*, *energy_max: SupportsFloat = 20.0*, *nb_groups: SupportsInt = 100*, *name: str = 'KappaFissionAllVolumes'*) → None
    :   Constructor

    writeToFile(*file_path: str*) → None

*class* tripoli5.score.KappaFissionMEDMesh
:   The KappaFissionMEDMesh is used to compute the energy deposited by fission in a mesh. The energy deposition is retrieved from the Q value of the fission. Its unit is [MeV per source particle].

    __init__(*mesh: object*, *neutron_media: tripoli5.materials.NeutronMedia*, *energy_min: SupportsFloat = 1e-11*, *energy_max: SupportsFloat = 20.0*, *nb_groups: SupportsInt = 100*, *name: str = 'KappaFissionMEDMesh'*) → None
    :   Constructor

    writeFieldToVTKFile(*: tripoli5.score.MEDMeshScore*, *file_path: str*, *field: str*) → None

    writeToFile(*file_path: str*) → None

    writeToMEDFile(*file_path: str*) → None

*class* tripoli5.score.MEDMeshScore
:   __init__(**args*, ***kwargs*)

*class* tripoli5.score.MTReactionRate
:   Class used to compute MT reaction rate scores

    __init__(*media: tripoli5.materials.NeutronMedia*, *mt_numbers: collections.abc.Sequence[tripoli5.delos.ReactionId]*, *nb_volumes: SupportsInt*, *energy_bounds: collections.abc.Sequence[tripoli5.core.physics.Energy]*, *name: str*) → None
    :   Constructor

    *property* energy_bounds

    writeToFile(*arg0: str*) → None
    :   Writes results into a tabulated separated values file

*class* tripoli5.score.ScoreManager
:   __init__(*name: str*) → None
    :   Constructor

    addScore(*score: tripoli5.score.IScore*) → None

    getScore(*index: SupportsInt*) → tripoli5.score.IScore

    initialize(*simulation_name: str*) → None

    reset() → None

## tripoli5.source module

source is a submodule of `tripoli5`. It is the main entry point for describing particle sources in Tripoli-5.

*class* tripoli5.source.FactorizedSource
:   __init__(*spatial: tripoli5.distributions.spatial.ISpaceDistribution*, *energy: tripoli5.distributions.energy.IEnergyDistribution*, *angle: tripoli5.distributions.angular.IAngularDistribution*, *norm: SupportsFloat = 1.0*) → None
    :   Constructor a factorized source

*class* tripoli5.source.ISource
:   __init__(**args*, ***kwargs*)

*class* tripoli5.source.PointIsotropicSource
:   __init__(*type_: tripoli5.core.physics.ParticleType*, *energy_dist: tripoli5.distributions.energy.IEnergyDistribution*, *point: tripoli5.core.euclide.Point*, *norm: SupportsFloat = 1.0*, *time: SupportsFloat = 0.0*) → None
    :   Constructor of a Point Isotropic Source of particles from a point located at position (x,y,z)

## tripoli5.simulation module

simulation is a submodule of `tripoli5`. It is the main entry point for launching simulations in Tripoli-5.

*class* tripoli5.simulation.CriticalityMono
:   A criticality simulation object contaning all necessary objects to actually run the simulation.

    __init__(**args*, ***kwargs*)

    *property* cycles_count
    :   Number of cycles already run

    getDetector(*i: SupportsInt*) → tripoli5.future_score.Detector | tripoli5.future_score.DistributionDetector
    :   Get detector by index.

        ### Parameters

        i : int
        :   Index of the detector to retrieve (0-based indexing).

        ### Returns

        Detector | DistributionDetector
        :   The requested detector object at index i in the list given to the SimulationBuilder with method withNewScores.

    getKStep() → tripoli5.score.KStep
    :   Retrieve the kstep score

    getMedia(*particle_type: tripoli5.core.physics.ParticleType*) → tripoli5.materials.IMedia
    :   Retrieve the media of a particle type

    *property* getNbDetectors
    :   The number of detectors defined in the simulation

    getNbScores() → int
    :   The number of scores

    getScore(*score_index: SupportsInt*) → tripoli5.score.IScore
    :   Retrieve a score

    getSource() → tripoli5.source.ISource
    :   Get the source

    initializeDefaultScores() → None
    :   Turn on some defaults scores

    printSimulationStatistics() → None

    resetNewScores() → None
    :   Reset scores to zero (can be called multiple times)

    resetScores() → None
    :   Reset scores to zero (can be called multiple times)

    run() → None
    :   Run the complete simulation (all cycles)

    runCycle(*cycle_index: SupportsInt*) → None
    :   run one cycle

    setMedia(*particle_type: tripoli5.core.physics.ParticleType*, *media: tripoli5.materials.IMedia*) → None
    :   Define the media used

    setParticleTracking(*particle_type: tripoli5.core.physics.ParticleType*, *factory: tripoli5.simulation.IParticleTrackingFactory*) → None
    :   Set the particle tracking by type

    setSource(*source: tripoli5.source.ISource*) → None
    :   Set the source

    setUserScores(*user_scores: tripoli5.score.IScore*) → None
    :   Add user’s scores to compute

*class* tripoli5.simulation.CriticalityOpenMP
:   A criticality simulation object contaning all necessary objects to actually run the simulation.

    __init__(**args*, ***kwargs*)

    *property* cycles_count
    :   Number of cycles already run

    getDetector(*i: SupportsInt*) → tripoli5.future_score.Detector | tripoli5.future_score.DistributionDetector
    :   Get detector by index.

        ### Parameters

        i : int
        :   Index of the detector to retrieve (0-based indexing).

        ### Returns

        Detector | DistributionDetector
        :   The requested detector object at index i in the list given to the SimulationBuilder with method withNewScores.

    getKStep() → tripoli5.score.KStep
    :   Retrieve the kstep score

    getMedia(*particle_type: tripoli5.core.physics.ParticleType*) → tripoli5.materials.IMedia
    :   Retrieve the media of a particle type

    *property* getNbDetectors
    :   The number of detectors defined in the simulation

    getNbScores() → int
    :   The number of scores

    getScore(*score_index: SupportsInt*) → tripoli5.score.IScore
    :   Retrieve a score

    getSource() → tripoli5.source.ISource
    :   Get the source

    initializeDefaultScores() → None
    :   Turn on some defaults scores

    printSimulationStatistics() → None

    resetNewScores() → None
    :   Reset scores to zero (can be called multiple times)

    resetScores() → None
    :   Reset scores to zero (can be called multiple times)

    run() → None
    :   Run the complete simulation (all cycles)

    runCycle(*cycle_index: SupportsInt*) → None
    :   run one cycle

    setMedia(*particle_type: tripoli5.core.physics.ParticleType*, *media: tripoli5.materials.IMedia*) → None
    :   Define the media used

    setParticleTracking(*particle_type: tripoli5.core.physics.ParticleType*, *factory: tripoli5.simulation.IParticleTrackingFactory*) → None
    :   Set the particle tracking by type

    setSource(*source: tripoli5.source.ISource*) → None
    :   Set the source

    setUserScores(*user_scores: tripoli5.score.IScore*) → None
    :   Add user’s scores to compute

*class* tripoli5.simulation.FixedSourceMono
:   __init__(**args*, ***kwargs*)

    *property* cycles_count
    :   Number of cycles already run

    getDetector(*i: SupportsInt*) → tripoli5.future_score.Detector | tripoli5.future_score.DistributionDetector
    :   Get detector by index.

        ### Parameters

        i : int
        :   Index of the detector to retrieve (0-based indexing).

        ### Returns

        Detector | DistributionDetector
        :   The requested detector object at index i in the list given to the SimulationBuilder with method withNewScores.

    *property* getNbDetectors
    :   The number of detectors defined in the simulation

    getSource() → tripoli5.source.ISource

    initializeDefaultScores() → None

    printSimulationStatistics() → None

    run() → None

    runCycle(*arg0: SupportsInt*) → None

    setMedia(*arg0: tripoli5.core.physics.ParticleType*, *arg1: tripoli5.materials.IMedia*) → None

    setParticleTracking(*arg0: tripoli5.core.physics.ParticleType*, *arg1: IParticleTrackingFactory*) → None

    setSource(*arg0: tripoli5.source.ISource*) → None

    setUserScores(*arg0: tripoli5.score.IScore*) → None

*class* tripoli5.simulation.FixedSourceOpenMP
:   __init__(**args*, ***kwargs*)

    *property* cycles_count
    :   Number of cycles already run

    getDetector(*i: SupportsInt*) → tripoli5.future_score.Detector | tripoli5.future_score.DistributionDetector
    :   Get detector by index.

        ### Parameters

        i : int
        :   Index of the detector to retrieve (0-based indexing).

        ### Returns

        Detector | DistributionDetector
        :   The requested detector object at index i in the list given to the SimulationBuilder with method withNewScores.

    *property* getNbDetectors
    :   The number of detectors defined in the simulation

    getSource() → tripoli5.source.ISource

    initializeDefaultScores() → None

    printSimulationStatistics() → None

    run() → None

    runCycle(*arg0: SupportsInt*) → None

    setMedia(*arg0: tripoli5.core.physics.ParticleType*, *arg1: tripoli5.materials.IMedia*) → None

    setParticleTracking(*arg0: tripoli5.core.physics.ParticleType*, *arg1: IParticleTrackingFactory*) → None

    setSource(*arg0: tripoli5.source.ISource*) → None

    setUserScores(*arg0: tripoli5.score.IScore*) → None

*class* tripoli5.simulation.IParticleTrackingFactory
:   __init__(**args*, ***kwargs*)

*class* tripoli5.simulation.ISimulation
:   __init__(**args*, ***kwargs*)

*class* tripoli5.simulation.IdSyncEngineConfig
:   A container that holds IdSyncEngine strategy parameters

    __init__(**args*, ***kwargs*)

    *static* select(*strategy_name: str*, *imbalance_ratio_threshold: SupportsFloat = 1.0*, *particles_nb_threshold: SupportsInt = 400*) → tripoli5.simulation.IdSyncEngineConfig
    :   Selects the IdSync Strategy Config according to the parameters.

        ### Parameters

        strategy_name : str
        :   The name of the load balancing strategy. Possible values: “light”, “collective”.

        imbalance_ratio_threshold : float
        :   The maximum accepted imbalance ratio. This is basically the ratio between
            the number of particles of the most loaded process and the mean number of
            particles. Load balancing using the collective strategy is not performed
            if the imbalance ratio is lower than this value.

        particles_nb_threshold : int
        :   The total number of particles above which the collective load balancing
            algorithm is triggered.

*class* tripoli5.simulation.MajorantExecutor
:   Members:

    Mono

    OpenMP

    Mono *= <MajorantExecutor.Mono: 0>*

    OpenMP *= <MajorantExecutor.OpenMP: 1>*

    __init__(*value: SupportsInt*) → None

    *property* name

    *property* value

*class* tripoli5.simulation.MajorantType
:   Members:

    Global

    OnTheFly

    EnergyDependent

    EnergyDependent *= <MajorantType.EnergyDependent: 1>*

    Global *= <MajorantType.Global: 0>*

    OnTheFly *= <MajorantType.OnTheFly: 2>*

    __init__(*value: SupportsInt*) → None

    *property* name

    *property* value

*class* tripoli5.simulation.SimulationBuilder
:   A helper to generate simulation.

    __init__(**args*, ***kwargs*)
    :   Overloaded function.

        1. __init__(self: tripoli5.simulation.SimulationBuilder) -> None
        2. __init__(self: tripoli5.simulation.SimulationBuilder, simulation_mode: str, parallelism_type: str) -> None

        Constructor with the simulation mode and the parallel type.Possible simulation modes are: ‘fixed_source’, ‘criticality’.
        Possible parallelism types are: ‘mono’, ‘openmp’

    build() → tripoli5.simulation.ISimulation
    :   Build the simulation using provided characteristics

    withGeometry(*geom: IGeometry | Geometry*) → SimulationBuilder
    :   Specify the geometry

    withMedia(*particle_type: str*, *media: tripoli5.materials.IMedia*) → tripoli5.simulation.SimulationBuilder
    :   Associate a particle type to a the media. Possible particle types are neutron, photon, electron, positron

    withNewScores(*detectors: collections.abc.Sequence[tripoli5.future_score.Detector | tripoli5.future_score.DistributionDetector]*) → tripoli5.simulation.SimulationBuilder
    :   Specify the new scores

    withParameters(*params: tripoli5.simulation.SimulationParameters*) → tripoli5.simulation.SimulationBuilder
    :   Specify the simulation parameters

    withParticleTracking(*particle_type: str*, *tracking_factory: tripoli5.simulation.IParticleTrackingFactory*) → tripoli5.simulation.SimulationBuilder
    :   Associate a particle type to a the tracking method. Possible particle types are neutron, photon, electron, positron

    withScores(*scores: tripoli5.score.IScore*) → tripoli5.simulation.SimulationBuilder
    :   Specify the scores

    withSource(*source: tripoli5.source.ISource*) → tripoli5.simulation.SimulationBuilder
    :   Specify the source

*class* tripoli5.simulation.SimulationBuilderCriticalityMono
:   See [`SimulationBuilder`](#tripoli5.simulation.SimulationBuilder)

    __init__() → None

    withBatchStrategy(*: tripoli5.simulation.SimulationBuilder*, *strategy_type: str*, *nb_generations: typing.SupportsInt*) → tripoli5.simulation.SimulationBuilder
    :   Select the strategy for simulating particles in a given cycle. Possible strategies are: single_fission_generation, super_history

*class* tripoli5.simulation.SimulationBuilderCriticalityOpenMP
:   See [`SimulationBuilder`](#tripoli5.simulation.SimulationBuilder)

    __init__() → None

    withBatchStrategy(*: tripoli5.simulation.SimulationBuilder*, *strategy_type: str*, *nb_generations: typing.SupportsInt*) → tripoli5.simulation.SimulationBuilder
    :   Select the strategy for simulating particles in a given cycle. Possible strategies are: single_fission_generation, super_history

*class* tripoli5.simulation.SimulationBuilderFixedSourceMono
:   See [`SimulationBuilder`](#tripoli5.simulation.SimulationBuilder)

    __init__() → None

    withBatchStrategy(*: tripoli5.simulation.SimulationBuilder*, *strategy_type: str*, *nb_generations: typing.SupportsInt = 0*) → tripoli5.simulation.SimulationBuilder
    :   Select the strategy for simulating particles in a given cycle. Possible strategies are: whole_progeny, single_fission_generation, super_history

*class* tripoli5.simulation.SimulationBuilderFixedSourceOpenMP
:   See [`SimulationBuilder`](#tripoli5.simulation.SimulationBuilder)

    __init__() → None

    withBatchStrategy(*: tripoli5.simulation.SimulationBuilder*, *strategy_type: str*, *nb_generations: typing.SupportsInt = 0*) → tripoli5.simulation.SimulationBuilder
    :   Select the strategy for simulating particles in a given cycle. Possible strategies are: whole_progeny, single_fission_generation, super_history

*class* tripoli5.simulation.SimulationParameters
:   A container that holds the simulation parameters

    __init__(*nb_cycles: SupportsInt = 100*, *nb_events: SupportsInt = 100*, *name: str = ''*, *nb_threads: SupportsInt = 1*, *schedule_size: SupportsInt = 1*, *random_seed: SupportsInt | None = None*, *discard: SupportsInt | None = None*, *idconf: tripoli5.simulation.IdSyncEngineConfig | None = None*, *bundle_size: SupportsInt = 100*) → None
    :   Default constructor

    *property* bundle_size
    :   Number of simulated particles before tallying

    *property* discard
    :   Number of discarded cycles

    *property* idsync_config
    :   IdSyncEngine configuration

    *property* name
    :   Name of the simulation

    *property* nb_cycles
    :   Number of cycles

    *property* nb_events
    :   Number of ‘events’ (particles) per cycle

    *property* nb_threads
    :   Number of threads (e.g. OpenMP threads)

    *property* random_seed
    :   Random seed

    *property* schedule_size
    :   Number of particles to follow in an event based manner; 1 means history based and self.nb_events means that all particles in the batch are followed using an event-based scheme

*class* tripoli5.simulation.TrackingBuilder
:   __init__(**args*, ***kwargs*)
    :   Overloaded function.

        1. __init__(self: tripoli5.simulation.TrackingBuilder) -> None

        Constructor using Surface tracking option

        2. __init__(self: tripoli5.simulation.TrackingBuilder, majorant_type: tripoli5.simulation.MajorantType) -> None

        Constructor using Delta Tracking option

    build() → tripoli5.simulation.IParticleTrackingFactory
    :   Build the Tracking Factory

    catchExceptions(*catch_exc: bool*) → tripoli5.simulation.TrackingBuilder
    :   Decide if exceptions raised during particle transport should be caught. If true, any exceptions thrown by particle tracking will be caught and will not interrupt the whole simulation. Otherwise, the simulation will stop (default behaviour).

    withMajorantFudgeFactors(*bounds: collections.abc.Sequence[SupportsFloat]*, *factors: collections.abc.Sequence[SupportsFloat]*) → tripoli5.simulation.TrackingBuilder
    :   Pass the fudge factors (factor that are applied to the majorant) to the builder

    withMajorantParameters(*media: tripoli5.materials.NeutronMedia*, *majorant_executor: tripoli5.simulation.MajorantExecutor*) → tripoli5.simulation.TrackingBuilder
    :   Pass the parameters for constructing the majorant to the builder

    withMaxSteps(*min_dist: SupportsFloat*, *max_steps: SupportsInt*) → tripoli5.simulation.TrackingBuilder
    :   Set a limit on how many steps across a surface will be attempted

        If tracking attempts more than max_steps steps of length shorter than
        min_dist across a surface, an exception will be thrown. This is used to
        prevent particles from getting stuck in corners of the geometry and
        bringing down the whole simulation.

        These parameters are only used in surface tracking, because there are no
        surfaces in delta tracking.

        ### Parameters

        min_dist : int
        :   the minimum step distance

        max_steps : int
        :   the maximum number of steps

    withPopulationControl(*roulette_threshold: SupportsFloat = 0.25*, *roulette_survival_weight: SupportsFloat = 1.0*, *splitting_threshold: SupportsFloat = 4.0*, *splitting_target_weight: SupportsFloat = 1.0*) → tripoli5.simulation.TrackingBuilder

## tripoli5.distributions module

*class* tripoli5.distributions.energy.IEnergyDistribution
:   __init__(**args*, ***kwargs*)

*class* tripoli5.distributions.energy.MaxwellSpectrum
:   Energy spectrum following a Maxwell-Boltzmann distribution

    > Parameters:
    > :   kb_T (tripoli5::core::physics::Energy): Thermal energy of the medium

    __init__(*kb_T: tripoli5.core.physics.Energy*) → None
    :   Maxwell spectrum distribution constructor

*class* tripoli5.distributions.energy.MonoKinetic
:   __init__(*energy: tripoli5.core.physics.Energy*) → None
    :   MonoKinetic distribution constructor

*class* tripoli5.distributions.energy.WattSpectrum
:   Energy spectrum following a Watt distribution

    > Parameters:
    > :   a (tripoli5::core::physics::Energy): first parameter of the distribution
    >     c (tripoli5::core::physics::Energy): second parameter of the distribution

    The probability density function is given by:
    .. math:

    ```
    p(E)dE = \frac{2\exp(\frac{-a}{4c})}{\sqrt{\frac{\pi a^{3}}{c}}}\exp(\frac{-E}{a})\sinh(\sqrt(\frac{E}{c}))dE
    ```

    __init__(*a: tripoli5.core.physics.Energy*, *c: tripoli5.core.physics.Energy*) → None
    :   Watt distribution constructor

*class* tripoli5.distributions.spatial.BoxDistribution
:   __init__(*lower_left: tripoli5.core.euclide.Point*, *upper_right: tripoli5.core.euclide.Point*) → None
    :   Box distribution constructor

*class* tripoli5.distributions.spatial.CylinderCosineDistribution
:   __init__(*center: tripoli5.core.euclide.Point*, *radius: SupportsFloat*, *half_height: SupportsFloat*) → None
    :   Cylinder Cosine distribution constructor

*class* tripoli5.distributions.spatial.CylinderDistribution
:   __init__(*center: tripoli5.core.euclide.Point*, *radius: SupportsFloat*, *half_height: SupportsFloat*) → None
    :   Cylinder uniform distribution constructor

*class* tripoli5.distributions.spatial.ISpaceDistribution
:   __init__(**args*, ***kwargs*)

*class* tripoli5.distributions.spatial.LineDistribution
:   __init__(*p0: tripoli5.core.euclide.Point*, *p1: tripoli5.core.euclide.Point*) → None
    :   Line distribution constructor

*class* tripoli5.distributions.spatial.PointDistribution
:   __init__(*point: tripoli5.core.euclide.Point*) → None
    :   Point distribution constructor

*class* tripoli5.distributions.spatial.SphereDistribution
:   __init__(*center: tripoli5.core.euclide.Point*, *radius: SupportsFloat*) → None
    :   Sphere distribution constructor

*class* tripoli5.distributions.angular.IAngularDistribution
:   __init__(**args*, ***kwargs*)

*class* tripoli5.distributions.angular.IsotropicAngularDistribution
:   __init__() → None
    :   Isotropic distribution constructor

*class* tripoli5.distributions.angular.MarsagliaIsotropicAngularDistribution
:   __init__() → None
    :   Marsaglia isotropic distribution constructor

## tripoli5.mpi module

mpi is the submodule of `tripoli5` that handles MPI communications.

tripoli5.mpi.finalize() → None

tripoli5.mpi.getGlobalRank() → int

tripoli5.mpi.getGlobalSize() → int

tripoli5.mpi.getSimuIndex() → int

tripoli5.mpi.getSimuRank() → int

tripoli5.mpi.getSimuSize() → int

tripoli5.mpi.init(**args*, ***kwargs*)
:   Overloaded function.

    1. init(communicator: object) -> None

    Initialize the MPI handler with the given mpi4py communicator.

    2. init(argv: collections.abc.Sequence[str]) -> None

    Initialize the MPI handler from the command line (call MPI_Init).

## tripoli5.icoco module

*class* tripoli5.icoco.Problem
:   GetICoCoMajorVersion() → int

    __init__(*name: str*, *raise_sigfpe: bool = False*) → None
    :   constructor

    abortTimeStep() → None

    computeTimeStep() → tuple

    getFieldType(*name: str*) → str

    getFieldUnit(*name: str*) → str

    getInputFieldsNames() → list[str]

    getInputMEDDoubleFieldTemplate(*name: str*) → object

    getInputValuesNames() → list[str]

    getMEDCouplingMajorVersion() → int

    getMeshUnit() → str

    getOutputDoubleValue(*name: str*) → float

    getOutputFieldsNames() → list[str]

    getOutputMEDDoubleField(*arg0: str*) → object
    :   name_a

    getOutputValuesNames() → list[str]

    getScoreManager() → tripoli5.score.ScoreManager

    getStationaryMode() → bool

    getValueType(*name: str*) → str

    getValueUnit(*name: str*) → str

    initTimeStep(*dt: SupportsFloat*) → bool

    initialize() → bool

    isMEDCoupling64Bits() → bool

    isStationary() → bool

    presentTime() → float

    resetTime(*time: SupportsFloat*) → None

    setCatalog(*arg0: tripoli5.delos.Catalog*) → None

    setInputDoubleValue(*name: str*, *val: SupportsFloat*) → None

    setInputMEDDoubleField(*name: str*, *afield: object*) → None

    setMPIComm(*communicator: object*) → None

    setStationaryMode(*stationaryMode: bool*) → None

    solveTimeStep() → bool

    terminate() → None

    updateOutputMEDDoubleField(*name: str*, *field: ICoCo::MEDDoubleField*) → None

    validateTimeStep() → None
