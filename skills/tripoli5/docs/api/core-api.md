<!-- source: https://tripoli5.asnr.dev/documentation/latest-release/api/core-api.html -->

# The CORE API

The description of CORE

*exception* tripoli5.core.CoreNotImplemented

*exception* tripoli5.core.CoreRuntimeError

*exception* tripoli5.core.CoreValueError

*class* tripoli5.core.Identifier
:   __init__(**args*, ***kwargs*)

*class* tripoli5.core.Version
:   __init__(*version: str*) → None
    :   Custom constructor from a string

    *property* build_metadata

    hasSameMajor(*version: tripoli5.core.Version*) → bool

    hasSameMajorMinor(*version: tripoli5.core.Version*) → bool

    *property* major

    *property* minor

    *property* patch

    *property* pre_release

tripoli5.core.set_output_file(*fname: str*) → None
:   Opens a new file to which all logged TRIPOLI-5 output will be written, in addition to the terminal/notebook output.

    ## Parameters

    fname : str
    :   Name of the output file.

*class* tripoli5.core.euclide.AffineTransformation
:   __init__(*translation: tripoli5.core.euclide.Translation | None*, *rotation: tripoli5.core.euclide.Rotation | None*) → None
    :   Custom constructor

    apply(**args*, ***kwargs*)
    :   Overloaded function.

        1. apply(self: tripoli5.core.euclide.AffineTransformation, arg0: tripoli5.core.euclide.Point, arg1: tripoli5.core.euclide.Direction) -> tuple[tripoli5.core.euclide.Point, tripoli5.core.euclide.Direction]
        2. apply(self: tripoli5.core.euclide.AffineTransformation, arg0: tripoli5.core.euclide.Direction) -> tripoli5.core.euclide.Direction

*class* tripoli5.core.euclide.Angle
:   __init__(*mu: SupportsFloat*, *phi: SupportsFloat*) → None
    :   Custom constructor from 2 double: mu, phi

    *property* mu

    *property* phi

*class* tripoli5.core.euclide.Direction
:   __init__(**args*, ***kwargs*)
    :   Overloaded function.

        1. __init__(self: tripoli5.core.euclide.Direction, x: typing.SupportsFloat, y: typing.SupportsFloat, z: typing.SupportsFloat) -> None

        Custom constructor from 3 double: x, y, z

        2. __init__(self: tripoli5.core.euclide.Direction, angle: tripoli5.core.euclide.Angle) -> None

        Custom constructor from an Angle:

        3. __init__(self: tripoli5.core.euclide.Direction, v: tripoli5.core.euclide.Vector) -> None

        Custom constructor from a vector

    dot(**args*, ***kwargs*)
    :   Overloaded function.

        1. dot(self: tripoli5.core.euclide.Direction, direction: tripoli5.core.euclide.Direction) -> float
        2. dot(self: tripoli5.core.euclide.Direction, vector: tripoli5.core.euclide.Vector) -> float

    getX() → float

    getY() → float

    getZ() → float

    scale(*a: SupportsFloat*) → tripoli5.core.euclide.Vector
    :   Return self multiplied by a

*class* tripoli5.core.euclide.Point
:   __init__(*x: SupportsFloat*, *y: SupportsFloat*, *z: SupportsFloat*) → None
    :   Custom constructor from 3 double: x, y, z

    *static* affineCombi(*a: SupportsFloat*, *p1: tripoli5.core.euclide.Point*, *b: SupportsFloat*, *p2: tripoli5.core.euclide.Point*) → tripoli5.core.euclide.Point

    displace(*distance: SupportsFloat*, *d: tripoli5.core.euclide.Direction*) → tripoli5.core.euclide.Point
    :   displace the current point of the distance distance in d direction

    distance(*p: tripoli5.core.euclide.Point*) → float
    :   compute the distance to another point p

    getX() → float

    getY() → float

    getZ() → float

*class* tripoli5.core.euclide.Rotation
:   __init__(*v: tripoli5.core.euclide.Vector*) → None
    :   Custom constructor from a Vector

    apply(**args*, ***kwargs*)
    :   Overloaded function.

        1. apply(self: tripoli5.core.euclide.Rotation, d: tripoli5.core.euclide.Direction) -> tripoli5.core.euclide.Direction
        2. apply(self: tripoli5.core.euclide.Rotation, p: tripoli5.core.euclide.Point) -> tripoli5.core.euclide.Point
        3. apply(self: tripoli5.core.euclide.Rotation, v: tripoli5.core.euclide.Vector) -> tripoli5.core.euclide.Vector
        4. apply(self: tripoli5.core.euclide.Rotation, arg0: tripoli5.core.euclide.Point, arg1: tripoli5.core.euclide.Direction) -> tuple[tripoli5.core.euclide.Point, tripoli5.core.euclide.Direction]

*class* tripoli5.core.euclide.Translation
:   __init__(*v: tripoli5.core.euclide.Vector*) → None
    :   Custom constructor from a Vector

    apply(*p: tripoli5.core.euclide.Point*) → tripoli5.core.euclide.Point
    :   apply the translation to a Point

*class* tripoli5.core.euclide.Vector
:   __init__(*x: SupportsFloat*, *y: SupportsFloat*, *z: SupportsFloat*) → None
    :   Custom constructor from 3 double: x, y, z

    dot(*arg0: tripoli5.core.euclide.Vector*) → float

    getNorm() → float

    getX() → float

    getY() → float

    getZ() → float

    reflect(*normal: tripoli5.core.euclide.Vector*) → tripoli5.core.euclide.Vector
    :   Return the vector reflected with respect to a normal vector

    renormalize(*norm: SupportsFloat = 1.0*) → None
    :   Renormalize the vector with norm

    rescale(*a: SupportsFloat*) → None
    :   Multiply self by a

    scale(*a: SupportsFloat*) → tripoli5.core.euclide.Vector
    :   Return self multiplied by a

physics is a submodule of [`tripoli5.core`](#module-tripoli5.core). It is the main entry point for physical quantities description in Tripoli-5.

*class* tripoli5.core.physics.Density
:   *class* Units
    :   Members:

        gPerCm3

        __init__(*value: SupportsInt*) → None

        gPerCm3 *= Density.Units.gPerCm3*

        *property* name

        *property* value

    __init__(*value: SupportsFloat*, *unit: tripoli5.core.physics.Density.Units*) → None
    :   Custom constructor from a double and units

    *property* gPerCm3

*class* tripoli5.core.physics.Energy
:   *property* MeV

    *class* Units
    :   Members:

        MeV

        keV

        eV

        MeV *= Energy.Units.MeV*

        __init__(*value: SupportsInt*) → None

        eV *= Energy.Units.eV*

        keV *= Energy.Units.keV*

        *property* name

        *property* value

    __init__(*value: SupportsFloat*, *unit: tripoli5.core.physics.Energy.Units*) → None
    :   Custom constructor from a double and units

    *property* eV

    *property* keV

*class* tripoli5.core.physics.Mass
:   *class* Units
    :   Members:

        g

        NeutronMass

        MeV

        MeV *= Mass.Units.MeV*

        NeutronMass *= Mass.Units.NeutronMass*

        __init__(*value: SupportsInt*) → None

        g *= Mass.Units.g*

        *property* name

        *property* value

    __init__(*value: SupportsFloat*, *unit: tripoli5.core.physics.Mass.Units*) → None
    :   Custom constructor from a double and units

    *property* energy

    *property* g

    *property* neutronMass

*class* tripoli5.core.physics.ParticleType
:   *property* Mass

    __init__(*type_: str*) → None

*class* tripoli5.core.physics.Temperature
:   *property* C

    *property* K

    *property* MeV

    *class* Units
    :   Members:

        K

        C

        MeV

        C *= Temperature.Units.C*

        K *= Temperature.Units.K*

        MeV *= Temperature.Units.MeV*

        __init__(*value: SupportsInt*) → None

        *property* name

        *property* value

    __init__(*value: SupportsFloat*, *unit: tripoli5.core.physics.Temperature.Units*) → None
    :   Custom constructor from a double and units
