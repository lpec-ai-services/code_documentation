<!-- source: https://tripoli5.asnr.dev/documentation/latest-release/api/agora-api.html -->

# The AGORA API

The description of AGORA

*exception* tripoli5.agora.AGORALostError

*exception* tripoli5.agora.AGORAMissingNeighborsError

*exception* tripoli5.agora.AGORANotImplemented

*exception* tripoli5.agora.AGORAOutOfRange

*exception* tripoli5.agora.AGORAParseError

*exception* tripoli5.agora.AGORARuntimeError

*exception* tripoli5.agora.AGORAValueError

*class* tripoli5.agora.AlbedoBoundaryCondition
:   This class represents an albedo boundary condition

    __init__(*value: SupportsFloat*) → None
    :   Construct an albedo boundary condition with the given value: it acts as the reflective boundary condition but the weight of the outgoing particle is multiplied by the value of the albedo.

*class* tripoli5.agora.BSurface
:   __init__(**args*, ***kwargs*)

    isOnPositiveSide(*point: tripoli5.core.euclide.Point*, *direction: tripoli5.core.euclide.Direction*, *tolerance: SupportsFloat*) → bool

    *property* label

*class* tripoli5.agora.BoundaryConditions
:   __init__() → None
    :   Constructor

    add(*surface: tripoli5.agora.ISurface*, *boundary_condition: tripoli5.agora.IBoundaryCondition*) → None
    :   Add a boundary condition

*class* tripoli5.agora.CompositeVolume
:   __init__(*shape: tripoli5.agora.Shape*, *filler: tripoli5.agora.IFiller*, *affinetransformation: tripoli5.core.euclide.AffineTransformation | None = None*, ***, *label: str = ''*) → None
    :   Custom constructor from one Shape and one string:

    isOutsideVolume() → bool

*class* tripoli5.agora.DistancePackage
:   __init__(**args*, ***kwargs*)

    *property* boundary_condition

    *property* crossed_surface

    *property* crossing_coord_level

    *property* distance

    *property* lattice_translation

*class* tripoli5.agora.Geometry
:   __init__(*root_universe: tripoli5.agora.Universe*, *boundary_conditions: tripoli5.agora.BoundaryConditions = None*, *description: str = ''*) → None
    :   Constructor from the root universe:

    *property* description
    :   a string describing the geometry

    *static* deserialize(*filename: str*) → tripoli5.agora.Geometry
    :   read a geometry from a file

    getMaterial(*rank: SupportsInt*) → str
    :   get the material associated to the given rank; valid values range from 0 to nb_materials

    getMaterialRank(*material: str*) → int
    :   get the rank associated to the given material

    *property* materials
    :   the list of materials

    *property* nb_materials
    :   number of materials

    *property* nb_volumes
    :   number of geometry volumes

    serialize(*filename: str*) → None
    :   write the geometry to a file

*class* tripoli5.agora.GeometryChecker
:   __init__(*geometry: tripoli5.agora.Geometry*) → None
    :   Constructor from the geometry:

    check(*list: collections.abc.Sequence[tuple[tripoli5.core.euclide.Point, tripoli5.core.euclide.Direction]]*) → tuple[list[tripoli5.agora.Location], list[tripoli5.agora.Location]]
    :   Check holes and overlaps for each element (pair point/direction) of a list

    find(*list: collections.abc.Sequence[tuple[tripoli5.core.euclide.Point, tripoli5.core.euclide.Direction]]*) → list[tripoli5.agora.Location]
    :   Find locations for each element (pair point/direction) of a list

*class* tripoli5.agora.HexLattice
:   This class represents a hexagonal lattice with given indices in the x-alpha base (e.g., for 3 rings):

    ```
                  (0, 2)
           (-1, 2)      (1, 1)
    (-2, 2)       (0, 1)       (2, 0)
           (-1, 1)      (1, 0)
    (-2, 1)       (0, 0)       (2,-1)
           (-1,0)       (1, -1)
    (-2, 0)       (0,-1)       (2,-2)
           (-1,-1)      (1, -2)
                  (0,-2)
    ```

    __init__(*point: tripoli5.core.euclide.Point*, *hex_pitch: SupportsFloat*, *axial_pitch: SupportsFloat*, *nb_rings: SupportsInt*, *n_axial: SupportsInt*, *universe: tripoli5.agora.Universe*, *outer_universe: tripoli5.agora.Universe | None = None*, ***, *label: str = ''*) → None
    :   Custom constructor:

*class* tripoli5.agora.IBoundaryCondition
:   __init__(**args*, ***kwargs*)

*class* tripoli5.agora.IFiller
:   __init__(**args*, ***kwargs*)

    *property* label

*class* tripoli5.agora.ILattice
:   __init__(**args*, ***kwargs*)

*class* tripoli5.agora.ISurface
:   __init__(**args*, ***kwargs*)

    *property* label

*class* tripoli5.agora.IVolume
:   __init__(**args*, ***kwargs*)

    *property* label

*class* tripoli5.agora.IntersectionPolicy
:   Members:

    IgnoreFirstIntersection

    ReturnFirstIntersection

    IgnoreFirstIntersection *= <IntersectionPolicy.IgnoreFirstIntersection: 0>*

    ReturnFirstIntersection *= <IntersectionPolicy.ReturnFirstIntersection: 1>*

    __init__(*value: SupportsInt*) → None

    *property* name

    *property* value

*class* tripoli5.agora.LatticeIndices
:   __init__(*i: SupportsInt*, *j: SupportsInt*, *k: SupportsInt*) → None
    :   Custom constructor three int32_t:

    *property* i

    *property* j

    *property* k

*class* tripoli5.agora.LatticePackage
:   __init__(**args*, ***kwargs*)

    *property* indices

*class* tripoli5.agora.LatticeTranslation
:   __init__(*i: SupportsInt*, *j: SupportsInt*, *k: SupportsInt*) → None
    :   Custom constructor three int32_t:

    *property* i

    *property* j

    *property* k

*class* tripoli5.agora.LeakageBoundaryCondition
:   This class represents a leakage boundary condition: it absorbs any particle reaching the surface it is applied to.

    __init__() → None
    :   Constructor

*exception* tripoli5.agora.LexError

*class* tripoli5.agora.LocalCoord
:   __init__(**args*, ***kwargs*)

    *property* direction

    *property* lattice_package

    *property* position

    *property* universe

    *property* volume

*class* tripoli5.agora.Location
:   __init__(**args*, ***kwargs*)

    *property* direction
    :   Direction

    *property* locations
    :   Locations

    *property* point
    :   Position

*class* tripoli5.agora.MultiLevelCoords
:   __init__(**args*, ***kwargs*)

    *property* coords

    *property* innest_direction

    *property* innest_level

    *property* innest_position

    *property* leaf

    *property* nb_levels

    *property* root_direction

    *property* root_position

*class* tripoli5.agora.Navigator
:   __init__(*geometry: tripoli5.agora.Geometry*, *ignore_bc: bool = False*) → None
    :   Constructor from the geometry:

    computeDistanceToNextBoundary(*distance: SupportsFloat*) → bool

    *property* coords

    *property* current_direction

    *property* current_material

    *property* current_point

    *property* current_volume_rank

    getDistanceToBoundary() → tripoli5.agora.DistancePackage

    getDistanceToBoundaryCondition() → tripoli5.agora.DistancePackage

    initializeNavigation(*point: tripoli5.core.euclide.Point*, *direction: tripoli5.core.euclide.Direction*, *flush_surfaces: bool = True*) → None

    isInsideGeometry() → bool

    isLost() → bool

    locate(*point: tripoli5.core.euclide.Point*, *flush_surfaces: bool = True*) → None

    *property* nb_volumes

    pushAcrossBoundary() → tripoli5.agora.PushAcrossBoundaryResult

    pushAcrossNextBoundaryCondition() → tripoli5.agora.PushAcrossBoundaryResult

    pushCurrentPoint(*distance: SupportsFloat*) → None

    updateDirection(*direction: tripoli5.core.euclide.Direction*) → None

*class* tripoli5.agora.OrientedSurface
:   __init__(**args*, ***kwargs*)

    *property* surface

    *property* surface_crossing

*class* tripoli5.agora.Plane
:   __init__(*a: SupportsFloat*, *b: SupportsFloat*, *c: SupportsFloat*, *d: SupportsFloat*, ***, *label: str = ''*) → None
    :   Custom constructor from 4 double(s): a, b, c, d and label

    evaluate(*point: tripoli5.core.euclide.Point*) → float

    getA() → float

    getB() → float

    getC() → float

    getD() → float

    getDistance(*point: tripoli5.core.euclide.Point*, *direction: tripoli5.core.euclide.Direction*, *distpolicy: tripoli5.agora.IntersectionPolicy*) → float

    getNormal(*point: tripoli5.core.euclide.Point*) → tripoli5.core.euclide.Vector

*class* tripoli5.agora.PushAcrossBoundaryResult
:   __init__(**args*, ***kwargs*)

    *property* albedo

    *property* distance

*class* tripoli5.agora.Quadric
:   __init__(*a: SupportsFloat*, *b: SupportsFloat*, *c: SupportsFloat*, *d: SupportsFloat*, *e: SupportsFloat*, *f: SupportsFloat*, *g: SupportsFloat*, *h: SupportsFloat*, *i: SupportsFloat*, *j: SupportsFloat*, ***, *label: str = ''*) → None
    :   Custom constructor from 10 double(s): a, b, c, d, e, f, g, h, i and j

    evaluate(*point: tripoli5.core.euclide.Point*) → float

    getA() → float

    getB() → float

    getC() → float

    getD() → float

    getDistance(*point: tripoli5.core.euclide.Point*, *direction: tripoli5.core.euclide.Direction*, *distpolicy: tripoli5.agora.IntersectionPolicy*) → float

    getE() → float

    getF() → float

    getG() → float

    getH() → float

    getI() → float

    getJ() → float

    getNormal(*point: tripoli5.core.euclide.Point*) → tripoli5.core.euclide.Vector

*class* tripoli5.agora.RectLattice
:   __init__(*point: tripoli5.core.euclide.Point*, *pitch: tripoli5.core.euclide.Vector*, *nx: SupportsInt*, *ny: SupportsInt*, *nz: SupportsInt*, *universe: tripoli5.agora.Universe*, *outer_universe: tripoli5.agora.Universe | None = None*, ***, *label: str = ''*) → None
    :   Custom constructor:

*class* tripoli5.agora.ReflectionBoundaryCondition
:   This class represents a reflective boundary condition: it reflects an incoming particle with respect to the normal of the surface it is applied to.

    __init__() → None
    :   Constructor

*class* tripoli5.agora.Region
:   __init__(*surface: tripoli5.agora.ISurface*) → None
    :   Constructor from a surface

    *static* infinite() → tripoli5.agora.Region
    :   Create a infinite region (whole space)

    simplify() → tripoli5.agora.Region
    :   Return an equivalent region without duplicated surfaces

*class* tripoli5.agora.Shape
:   __init__(**args*, ***kwargs*)
    :   Overloaded function.

        1. __init__(self: tripoli5.agora.Shape, surfaces: collections.abc.Sequence[tripoli5.agora.ISurface], signature: str) -> None

        Constructor from a list of surfaces and a string signature

        2. __init__(self: tripoli5.agora.Shape, region: tripoli5.agora.Region) -> None

        Constructor from a a Region, built from surfaces and operators (i.e. -s1 & +s2)

        3. __init__(self: tripoli5.agora.Shape, surface: tripoli5.agora.ISurface) -> None

        Constructor from a surface

    getDistanceToBoundary(*point: tripoli5.core.euclide.Point*, *direction: tripoli5.core.euclide.Direction*, *last_oriented_surface: collections.abc.Sequence[tripoli5.agora.OrientedSurface]*) → tuple[float, tripoli5.agora.OrientedSurface | None]

    *static* infinite() → tripoli5.agora.Shape
    :   Create a infinite shape (whole space)

    isPointInside(*point: tripoli5.core.euclide.Point*, *direction: tripoli5.core.euclide.Direction*, *last_oriented_surface: tripoli5.agora.OrientedSurface | None*) → bool

*class* tripoli5.agora.Sphere
:   __init__(*p: tripoli5.core.euclide.Point*, *r: SupportsFloat*, ***, *label: str = ''*) → None
    :   Custom constructor from 1 point p, 1 double r and 1 string label:

    evaluate(*point: tripoli5.core.euclide.Point*) → float

    getDistance(*point: tripoli5.core.euclide.Point*, *direction: tripoli5.core.euclide.Direction*, *distpolicy: tripoli5.agora.IntersectionPolicy*) → float

    getNormal(*point: tripoli5.core.euclide.Point*) → tripoli5.core.euclide.Vector

    getP() → tripoli5.core.euclide.Point

    getR() → float

    getX0() → float

    getY0() → float

    getZ0() → float

*class* tripoli5.agora.SurfaceCrossing
:   Members:

    ToPositive

    ToNegative

    ToNegative *= <SurfaceCrossing.ToNegative: -1>*

    ToPositive *= <SurfaceCrossing.ToPositive: 1>*

    __init__(*value: SupportsInt*) → None

    *property* name

    *property* value

*class* tripoli5.agora.Universe
:   __init__(*volumes: collections.abc.Sequence[tripoli5.agora.IVolume]*, ***, *label: str = ''*) → None
    :   Custom constructor:

    *property* volumes

*class* tripoli5.agora.Volume
:   __init__(*shape: tripoli5.agora.Shape*, *material: str*, ***, *label: str = ''*) → None
    :   Custom constructor from one Shape and one string:

    isOutsideVolume() → bool

    *property* material

    *static* outside(*shape: tripoli5.agora.Shape*, ***, *label: str = ''*) → tripoli5.agora.Volume
    :   Create a volume representing part of the space outside the geometry

*class* tripoli5.agora.XCone
:   __init__(*p: tripoli5.core.euclide.Point*, *tan_alpha: SupportsFloat*, ***, *label: str = ''*) → None
    :   Custom constructor from 1 point p, 1 double tan_alpha and 1 string label:

    evaluate(*point: tripoli5.core.euclide.Point*) → float

    getDistance(*point: tripoli5.core.euclide.Point*, *direction: tripoli5.core.euclide.Direction*, *distpolicy: tripoli5.agora.IntersectionPolicy*) → float

    getNormal(*point: tripoli5.core.euclide.Point*) → tripoli5.core.euclide.Vector

    getP() → tripoli5.core.euclide.Point

    getTanAlpha() → float

    getX0() → float

    getY0() → float

    getZ0() → float

*class* tripoli5.agora.XCylinder
:   __init__(*y0: SupportsFloat*, *z0: SupportsFloat*, *r: SupportsFloat*, ***, *label: str = ''*) → None
    :   Custom constructor from 3 doubles y0, z0, r and label:

    evaluate(*point: tripoli5.core.euclide.Point*) → float

    getDistance(*point: tripoli5.core.euclide.Point*, *direction: tripoli5.core.euclide.Direction*, *distpolicy: tripoli5.agora.IntersectionPolicy*) → float

    getNormal(*point: tripoli5.core.euclide.Point*) → tripoli5.core.euclide.Vector

    getR() → float

    getY0() → float

    getZ0() → float

*class* tripoli5.agora.XPlane
:   __init__(*x0: SupportsFloat*, ***, *label: str = ''*) → None
    :   Custom constructor from 1 double and 1 string: x0

    evaluate(*point: tripoli5.core.euclide.Point*) → float

    getDistance(*point: tripoli5.core.euclide.Point*, *direction: tripoli5.core.euclide.Direction*, *distpolicy: tripoli5.agora.IntersectionPolicy*) → float

    getNormal(*point: tripoli5.core.euclide.Point*) → tripoli5.core.euclide.Vector

    getX0() → float

*class* tripoli5.agora.YCone
:   __init__(*p: tripoli5.core.euclide.Point*, *tan_alpha: SupportsFloat*, ***, *label: str = ''*) → None
    :   Custom constructor from 1 point p, 1 double tan_alpha and 1 string label:

    evaluate(*point: tripoli5.core.euclide.Point*) → float

    getDistance(*point: tripoli5.core.euclide.Point*, *direction: tripoli5.core.euclide.Direction*, *distpolicy: tripoli5.agora.IntersectionPolicy*) → float

    getNormal(*point: tripoli5.core.euclide.Point*) → tripoli5.core.euclide.Vector

    getP() → tripoli5.core.euclide.Point

    getTanAlpha() → float

    getX0() → float

    getY0() → float

    getZ0() → float

*class* tripoli5.agora.YCylinder
:   __init__(*x0: SupportsFloat*, *z0: SupportsFloat*, *r: SupportsFloat*, ***, *label: str = ''*) → None
    :   Custom constructor from 3 doubles x0, z0, r and label:

    evaluate(*point: tripoli5.core.euclide.Point*) → float

    getDistance(*point: tripoli5.core.euclide.Point*, *direction: tripoli5.core.euclide.Direction*, *distpolicy: tripoli5.agora.IntersectionPolicy*) → float

    getNormal(*point: tripoli5.core.euclide.Point*) → tripoli5.core.euclide.Vector

    getR() → float

    getX0() → float

    getZ0() → float

*class* tripoli5.agora.YPlane
:   __init__(*y0: SupportsFloat*, ***, *label: str = ''*) → None
    :   Custom constructor from 1 double and 1 string: y0

    evaluate(*point: tripoli5.core.euclide.Point*) → float

    getDistance(*point: tripoli5.core.euclide.Point*, *direction: tripoli5.core.euclide.Direction*, *distpolicy: tripoli5.agora.IntersectionPolicy*) → float

    getNormal(*point: tripoli5.core.euclide.Point*) → tripoli5.core.euclide.Vector

    getY0() → float

*class* tripoli5.agora.ZCone
:   __init__(*p: tripoli5.core.euclide.Point*, *tan_alpha: SupportsFloat*, ***, *label: str = ''*) → None
    :   Custom constructor from 1 point p, 1 double tan_alpha and 1 string label:

    evaluate(*point: tripoli5.core.euclide.Point*) → float

    getDistance(*point: tripoli5.core.euclide.Point*, *direction: tripoli5.core.euclide.Direction*, *distpolicy: tripoli5.agora.IntersectionPolicy*) → float

    getNormal(*point: tripoli5.core.euclide.Point*) → tripoli5.core.euclide.Vector

    getP() → tripoli5.core.euclide.Point

    getTanAlpha() → float

    getX0() → float

    getY0() → float

    getZ0() → float

*class* tripoli5.agora.ZCylinder
:   __init__(*x0: SupportsFloat*, *y0: SupportsFloat*, *r: SupportsFloat*, ***, *label: str = ''*) → None
    :   Custom constructor from 3 doubles x0, y0, r and label:

    evaluate(*point: tripoli5.core.euclide.Point*) → float

    getDistance(*point: tripoli5.core.euclide.Point*, *direction: tripoli5.core.euclide.Direction*, *distpolicy: tripoli5.agora.IntersectionPolicy*) → float

    getNormal(*point: tripoli5.core.euclide.Point*) → tripoli5.core.euclide.Vector

    getR() → float

    getX0() → float

    getY0() → float

*class* tripoli5.agora.ZPlane
:   __init__(*z0: SupportsFloat*, ***, *label: str = ''*) → None
    :   Custom constructor from 1 double and 1 string: z0

    evaluate(*point: tripoli5.core.euclide.Point*) → float

    getDistance(*point: tripoli5.core.euclide.Point*, *direction: tripoli5.core.euclide.Direction*, *distpolicy: tripoli5.agora.IntersectionPolicy*) → float

    getNormal(*point: tripoli5.core.euclide.Point*) → tripoli5.core.euclide.Vector

    getZ0() → float

tripoli5.agora.createInfinite(*material: str*) → tripoli5.agora.Universe

tripoli5.agora.createSlab(*limits: collections.abc.Sequence[SupportsFloat]*, *materials: collections.abc.Sequence[str]*, *orientation: str*) → tuple[tripoli5.agora.Universe, tuple[tripoli5.agora.ISurface, tripoli5.agora.ISurface]]

tripoli5.agora.retrieveFillerGeneratedByCASTOR(*geometry: tripoli5.agora.Geometry*) → tripoli5.agora.IFiller
