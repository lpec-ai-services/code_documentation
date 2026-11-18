<!-- source: https://tripoli5.asnr.dev/documentation/latest-release/api/geoplotter-api.html -->

# The GeoPlotter API

GeoPlotter ([`tripoli5.geoplotter`](#module-tripoli5.geoplotter)) can be used to visualize TRIPOLI-5®
geometries.

*class* tripoli5.geoplotter.Any(**args*, ***kwargs*)
:   Special type indicating an unconstrained type.

    - Any is compatible with every type.
    - Any assumed to have all methods.
    - All values assumed to be instances of Any.

    Note that all the above statements are true from the point of view of
    static type checkers. At runtime, Any should not be used with instance
    checks.

*class* tripoli5.geoplotter.Frame(*plane_cut: str*, *altitude: float*, *u_min: float*, *u_max: float*, *v_min: float*, *v_max: float*)
:   A frame description for plotting 2D cuts.

    It represents a plane orientation and the minimum and maximum values of the
    coordinates of the frame window in that plane.

    Consider using [:classmethod:`Frame.fromOrigin`](#id1) and [:classmethod:`Frame.fromMinMax`](#id3)
    to build objects of this class.

    __init__(*plane_cut: str*, *altitude: float*, *u_min: float*, *u_max: float*, *v_min: float*, *v_max: float*) → None

    altitude*: float*

    *static* checkFromOriginArguments(*extent: tuple[float, float]*) → None

    *classmethod* fromMinMax(*plane_cut: str*, *altitude: float*, *u_min: float*, *u_max: float*, *v_min: float*, *v_max: float*) → Self
    :   Build a frame from a plane cut, altitude, and minimum and maximum of the window

        ## Parameters

        plane_cut : str
        :   The plane cut. Accepted values are : “XY”, “XZ”, “YZ”

        altitude : float
        :   The altitude of the cut.

        u_min : float
        :   Minimum value of the first coordinate of the plane cut

        u_max : float
        :   Maximum value of the first coordinate of the plane cut

        v_min : float
        :   Minimum value of the second coordinate of the plane cut

        v_max : float
        :   Maximum value of the second coordinate of the plane cut

        ## Returns

        Frame
        :   The built frame

        ## Examples

        A frame defining a “XY” plane cut at altitude 0.0, i.e. a Z = 0.0 cut.
        The window edge coordinates are xmin=50, xmax=250, ymin=50, and ymax=250.

        ```
        >>> from tripoli5.geoplotter import Frame
        >>> frame = Frame.fromMinMax(plane_cut="XY",
        ...                          altitude=0.0,
        ...                          u_min=50.,
        ...                          u_max=250.,
        ...                          v_min=50.,
        ...                          v_max=250.)
        ```

    *classmethod* fromOrigin(*plane_cut: str*, *point: Point*, *origin: str*, *extent: tuple[float, float]*) → Self
    :   Build a frame from an origin point and the extents of the window

        ## Parameters

        plane_cut : str
        :   The orientation of the plane cut. Accepted values are : `"XY"`, `"XZ"`,
            `"YZ"`

        point : tripoli5.core.euclide.Point
        :   The coordinates of the origin.

        origin : str
        :   Define the origin of the window. Accepted values are: `"center"`,
            `"lower_left"`, `"lower_right"`, `"upper_left"`, `"upper_right"`.

        extent : tuple[float, float]
        :   The extent in each direction of the plane cut. Values must be positive.

        ## Returns

        Frame
        :   The built frame

        ## Examples

        A frame defining a “XY” plane cut at altitude 0.0, i.e. a Z = 0.0 cut.
        The window is centered around the coordinates (150.0, 150.0, 0.0),
        with an extent of 100.0 cm in each direction. In other words,
        xmin=50, xmax=250, ymin=50, and ymax=250.

        ```
        >>> from tripoli5.geoplotter import Frame
        >>> frame = Frame.fromOrigin(plane_cut="XY",
        ...                          point=Point(150.0, 150.0, 0.0),
        ...                          origin="center",
        ...                          extent=[100.0, 100.0])
        ```

    *static* getAltitudeUV(*plane_cut: str*, *point: Point*) → tuple[float, float, float]

    getAxisNames() → tuple[str, str]

    plane_cut*: str*

    u_max*: float*

    u_min*: float*

    v_max*: float*

    v_min*: float*

*class* tripoli5.geoplotter.GeoPlotterEngine(*_geometry: tripoli5.geometry.IGeometry*)
:   __init__(*_geometry: IGeometry*) → None

    query(*frame: Frame*, *coloring: str = 'material'*, *resolution: int = 20*, *mode: str = 'track'*, *nb_threads: int = 1*, *ignore_bc: bool = True*) → tuple[Sequence[float], float, float]

*class* tripoli5.geoplotter.GeoPlotterPyplot(*_geometry_in: IGeometry*)
:   A geometry plotter using matplotlib.pyplot

    ## Attributes

    _geometry: AGORAGeometry | ROOTGeometry | IGeometry
    :   The geometry to query

    __init__(*_geometry_in: IGeometry*) → None

    plot(*frame: Frame*, ***, *ax: Axes | None = None*, *color_map: Colormap | str | None = 'viridis'*, *mapping_colors: Mapping[str, Any] | None = None*, *resolution: int = 20*, *mode: str = 'track'*, *nb_threads: int = 1*, *ignore_bc: bool = True*, *coloring: str = 'material'*, *save_to_file: str | None = None*, *matplotlib_resolution: int = 300*) → tuple[Axes, Sequence[Patch]]
    :   Plot a 2D cut of the geometry

        This function interrogates the geometry over the frame to construct a pixel
        image which is then displayed using matplotlib’s imshow

        ### Parameters

        frame : Frame
        :   The frame for which the figure will be generated

        ax : matplotlib.axes.Axes or None
        :   A pyplot Axes used for drawing the figure

        color_map : matplotlib.colors.Colormap or str or None
        :   A matplotlib colormap (either a string or a colormap object)

        mapping_colors : Mapping[str or int, Any] or None
        :   A dictionary associating user material names or volume ranks to colors.
            Colors may be defined using matplotlib’s named colors:
            <https://matplotlib.org/stable/gallery/color/named_colors.html>
            or any format accepted by matplotlib:
            <https://matplotlib.org/stable/users/explain/colors/colors.html>

        resolution : int
        :   number of pixels per cm for interrogating the geometry

        mode : str
        :   mode for the plotting (must be one of: “point”, “track”, “point-wireframe”, “track-wireframe”, “wireframe”; default: “track”)

        nb_threads : int
        :   number of threads

        ignore_bc : bool
        :   ignore boundary conditions (default: True)

        coloring : str
        :   Select the coloring policy (must be one of “material” or “volume”)

        save_to_file : str or None
        :   A file name (with extension!) to which the figure will be saved

        matplotlib_resolution : int
        :   matplotlib’s dot per inches parameters when saving file

        ### Returns

        axes : matplotlib.axes.Axes
        :   The axes that were used for the plot

        patches : Sequence[matplotlib.patches.Patch]
        :   A list of patches (legend items)

        ### Examples

        plotter.plot(
        :   frame=frame,
            save_to_file=”exemple-1.png”,
            color_map=”Accent”,
            mapping_colors={

            > “COLD_WATER”: “lightblue”,
            > “FUEL”: “darkred”,
            > “VOID”: “grey”,
            > “CLAD”: “lightgrey”,
            > “VESSEL_MAT” : “seagreen”,

            },

        )

*class* tripoli5.geoplotter.IGeometry
:   __init__(**args*, ***kwargs*)

    *property* materials

    *property* nb_volumes

*class* tripoli5.geoplotter.Index
:   Members:

    OUTSIDE_WORLD

    BOUNDARY

    WIREFRAME_ONLY_BACKGROUND

    LOST_PARTICLE

    BOUNDARY *= <Index.BOUNDARY: -2>*

    LOST_PARTICLE *= <Index.LOST_PARTICLE: -4>*

    OUTSIDE_WORLD *= <Index.OUTSIDE_WORLD: -1>*

    WIREFRAME_ONLY_BACKGROUND *= <Index.WIREFRAME_ONLY_BACKGROUND: -3>*

    __init__(*: tripoli5.geometry.Index*, *value: typing.SupportsInt*) → None

    *property* name

    *property* value

*class* tripoli5.geoplotter.Mapping
:   A Mapping is a generic container for associating key/value
    pairs.

    This class provides concrete generic implementations of all
    methods except for __getitem__, __iter__, and __len__.

    get(*k*[, *d*]) → D[k] if k in D, else d.  d defaults to None.

    items() → a set-like object providing a view on D's items

    keys() → a set-like object providing a view on D's keys

    values() → an object providing a view on D's values

*class* tripoli5.geoplotter.MutableSequence
:   All the operations on a read-write sequence.

    Concrete subclasses must provide __new__ or __init__,
    __getitem__, __setitem__, __delitem__, __len__, and insert().

    append(*value*)
    :   S.append(value) – append value to the end of the sequence

    clear() → None -- remove all items from S

    extend(*values*)
    :   S.extend(iterable) – extend sequence by appending elements from the iterable

    *abstract* insert(*index*, *value*)
    :   S.insert(index, value) – insert value before index

    pop([*index*]) → item -- remove and return item at index (default last).
    :   Raise IndexError if list is empty or index is out of range.

    remove(*value*)
    :   S.remove(value) – remove first occurrence of value.
        Raise ValueError if the value is not present.

    reverse()
    :   S.reverse() – reverse *IN PLACE*

*class* tripoli5.geoplotter.Plotter
:   A Plotter for geometry.

    __init__(*: tripoli5.geometry.Plotter*, *geometry: tripoli5.geometry.IGeometry*) → None
    :   Constructor for Plotter

    query(*: tripoli5.geometry.Plotter*, *plane_cut: str*, *altitude: typing.SupportsFloat*, *u_min: typing.SupportsFloat*, *u_max: typing.SupportsFloat*, *v_min: typing.SupportsFloat*, *v_max: typing.SupportsFloat*, *coloring: str = 'material'*, *resolution: typing.SupportsInt = 20*, *mode: str = 'track'*, *nb_threads: typing.SupportsInt*, *ignore_bc: bool*) → tuple[list[int], int, int]
    :   Query the material or volume over a frame defined by plane, altitude, mins and maxs

*class* tripoli5.geoplotter.Point
:   __init__(*: tripoli5.core.euclide.Point*, *x: typing.SupportsFloat*, *y: typing.SupportsFloat*, *z: typing.SupportsFloat*) → None
    :   Custom constructor from 3 double: x, y, z

    *static* affineCombi(*a: SupportsFloat*, *p1: tripoli5.core.euclide.Point*, *b: SupportsFloat*, *p2: tripoli5.core.euclide.Point*) → tripoli5.core.euclide.Point

    displace(*: tripoli5.core.euclide.Point*, *distance: typing.SupportsFloat*, *d: tripoli5.core.euclide.Direction*) → tripoli5.core.euclide.Point
    :   displace the current point of the distance distance in d direction

    distance(*: tripoli5.core.euclide.Point*, *p: tripoli5.core.euclide.Point*) → float
    :   compute the distance to another point p

    getX(*: tripoli5.core.euclide.Point*) → float

    getY(*: tripoli5.core.euclide.Point*) → float

    getZ(*: tripoli5.core.euclide.Point*) → float

*class* tripoli5.geoplotter.Sequence
:   All the operations on a read-only sequence.

    Concrete subclasses must override __new__ or __init__,
    __getitem__, and __len__.

    count(*value*) → integer -- return number of occurrences of value

    index(*value*[, *start*[, *stop*]]) → integer -- return first index of value.
    :   Raises ValueError if the value is not present.

        Supporting start and stop arguments is optional, but
        recommended.

tripoli5.geoplotter.dataclass(*cls=None*, */*, ***, *init=True*, *repr=True*, *eq=True*, *order=False*, *unsafe_hash=False*, *frozen=False*, *match_args=True*, *kw_only=False*, *slots=False*, *weakref_slot=False*)
:   Add dunder methods based on the fields defined in the class.

    Examines PEP 526 __annotations__ to determine fields.

    If init is true, an __init__() method is added to the class. If repr
    is true, a __repr__() method is added. If order is true, rich
    comparison dunder methods are added. If unsafe_hash is true, a
    __hash__() method is added. If frozen is true, fields may not be
    assigned to after instance creation. If match_args is true, the
    __match_args__ tuple is added. If kw_only is true, then by default
    all fields are keyword-only. If slots is true, a new class with a
    __slots__ attribute is returned.

tripoli5.geoplotter.field(***, *default=<dataclasses._MISSING_TYPE object>*, *default_factory=<dataclasses._MISSING_TYPE object>*, *init=True*, *repr=True*, *hash=None*, *compare=True*, *metadata=None*, *kw_only=<dataclasses._MISSING_TYPE object>*)
:   Return an object to identify dataclass fields.

    default is the default value of the field. default_factory is a
    0-argument function called to initialize a field’s value. If init
    is true, the field will be a parameter to the class’s __init__()
    function. If repr is true, the field will be included in the
    object’s repr(). If hash is true, the field will be included in the
    object’s hash(). If compare is true, the field will be used in
    comparison functions. metadata, if specified, must be a mapping
    which is stored but not otherwise examined by dataclass. If kw_only
    is true, the field will become a keyword-only parameter to
    __init__().

    It is an error to specify both default and default_factory.
