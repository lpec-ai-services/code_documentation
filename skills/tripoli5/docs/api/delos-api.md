<!-- source: https://tripoli5.asnr.dev/documentation/latest-release/api/delos-api.html -->

# The DELOS API

The description of `DELOS` submodule’s API.

*class* tripoli5.delos.ACEPTable
:   __init__(*cdf: collections.abc.Sequence[SupportsFloat]*, *total: collections.abc.Sequence[SupportsFloat]*, *elastic: collections.abc.Sequence[SupportsFloat]*, *fission: collections.abc.Sequence[SupportsFloat]*, *radiative_capture: collections.abc.Sequence[SupportsFloat]*, *heat: collections.abc.Sequence[SupportsFloat]*) → None
    :   Custom constructor from six lists of floats

*class* tripoli5.delos.ACEURR
:   __init__(*infos: tripoli5.delos.Infos*, *egrid: tripoli5.delos.EnergyInterpolatedGrid*, *tables: collections.abc.Sequence[tripoli5.delos.ACEPTable]*, *use_factor: bool*, *flag_inelastic: SupportsInt*, *flag_other_absorption: SupportsInt*) → None
    :   Custom constructor

    *property* egrid

    *property* infos

    *property* ptables

*class* tripoli5.delos.ACEURRDataLibrary
:   Library for neutron data in the unresolved resonance region, in ACE format

    __init__(**args*, ***kwargs*)
    :   Overloaded function.

        1. __init__(self: tripoli5.delos.ACEURRDataLibrary, url: str) -> None

        Constructor from an archive at url

        2. __init__(self: tripoli5.delos.ACEURRDataLibrary) -> None

        Default constructor

    add(*filename: str*) → None

    has(*object_name: str*, *temperature: tripoli5.core.physics.Temperature*) → bool

    load(*object_name: str*, *temperature: tripoli5.core.physics.Temperature*) → tripoli5.delos.ACEURR

    printSummary() → None

*class* tripoli5.delos.AliasDiscreteDistribution
:   __init__()
    :   __init__(self: tripoli5.delos.AliasDiscreteDistribution, Construct from probabilities.

        Parameters:
        :   prob : Vector of normalised probabilities.

        prob: collections.abc.Sequence[typing.SupportsFloat]) -> None

*class* tripoli5.delos.AngularDistribution2D
:   __init__(*egrid: tripoli5.delos.EnergyInterpolatedGrid*, *distributions: collections.abc.Sequence[tripoli5.delos.IDistribution1D]*) → None
    :   Custom constructor from a [`EnergyInterpolatedGrid`](#tripoli5.delos.EnergyInterpolatedGrid) and a list of [`IDistribution1D`](#tripoli5.delos.IDistribution1D)

    *property* distributions

    *property* energy

*class* tripoli5.delos.BraggEdges
:   __init__(*egrid: tripoli5.delos.EnergyInterpolatedGrid*, *values: collections.abc.Sequence[SupportsFloat]*) → None
    :   Custom constructor from an [`EnergyInterpolatedGrid`](#tripoli5.delos.EnergyInterpolatedGrid) and a list of floats

    *property* egrid

    *property* values

*class* tripoli5.delos.BremsstrahlungOutProduct
:   __init__()
    :   __init__(self: tripoli5.delos.BremsstrahlungOutProduct, Build from components.

        Parameters:
        :   photon_distribution : tripoli5.delos.IEnergyAngleDistribution
            :   Distribution describing the emitted photon.

        photon_distribution: tripoli5.delos.IEnergyAngleDistribution) -> None

    *property* photon_distribution

*class* tripoli5.delos.CALENDFPTable
:   __init__(*discrete_prob : collections.abc.Sequence[typing.SupportsFloat], total: collections.abc.Sequence[typing.SupportsFloat],  partial reactions: collections.abc.Mapping[tripoli5.delos.ReactionId, collections.abc.Sequence[typing.SupportsFloat]]*) → None
    :   Custom constructor from the lists of floats

*class* tripoli5.delos.CALENDFURR
:   __init__(*infos: tripoli5.delos.Infos*, *egrid: tripoli5.delos.EnergyInterpolatedGrid*, *tables: collections.abc.Sequence[tripoli5.delos.CALENDFPTable]*) → None
    :   Custom constructor

    *property* egrid

    *property* infos

    *property* ptables

*class* tripoli5.delos.CALENDFURRDataLibrary
:   Library for neutron data in the unresolved resonance region, in CALENDF format

    __init__(**args*, ***kwargs*)
    :   Overloaded function.

        1. __init__(self: tripoli5.delos.CALENDFURRDataLibrary, url: str) -> None

        Constructor from an archive at url

        2. __init__(self: tripoli5.delos.CALENDFURRDataLibrary) -> None

        Default constructor

    add(*filename: str*) → None

    has(*object_name: str*, *temperature: tripoli5.core.physics.Temperature*) → bool

    load(*object_name: str*, *temperature: tripoli5.core.physics.Temperature*) → tripoli5.delos.CALENDFURR

    printSummary() → None

*class* tripoli5.delos.Catalog
:   An interface for reading and getting information from the catalog file

    __init__(**args*, ***kwargs*)

    *property* base_dir
    :   The top level directory of a Nuclear Data Library

    *property* creation_date

    *static* fromEnvVariable() → tripoli5.delos.Catalog

    *static* fromFile(*yaml_file_path: str*) → tripoli5.delos.Catalog

    *static* fromString(*yaml_string: str*) → tripoli5.delos.Catalog

    getArchivePath(*data_type: str*, *preprocessing: str*) → str
    :   Retrieve the path to the archive

    getAvailableTemperatures(*data: str*, *data_type: str*, *preprocessing: str*) → list[tripoli5.core.physics.Temperature]
    :   Retrieve available temperature of a data (e.g. nuclide)

    getDefaultDirectory(*data_type: str*, *preprocessing: str*) → str
    :   Retrieve the directory of individual data

    getPath(*data: str*, *data_type: str*, *temperature: tripoli5.core.physics.Temperature*, *preprocessing: str*) → str
    :   Retrieve the path of a data (e.g. nuclide)

    hasData(*data: str*, *data_type: str*, *temperature: tripoli5.core.physics.Temperature*, *preprocessing: str*) → bool
    :   Check if the catalog contains a data (e.g. nuclide)

    hasItem(*name: str*, *data_type: str*, *preprocessing: str*) → bool
    :   Check if the catalog contains a data (e.g. nuclide) at any temperature

    *property* library_name

*class* tripoli5.delos.CoherentAngularDistribution2D
:   __init__(*edges: tripoli5.delos.BraggEdges*) → None
    :   Custom constructor from a [`BraggEdges`](#tripoli5.delos.BraggEdges)

    *property* edges

*class* tripoli5.delos.ComptonOutProduct
:   __init__(*primary_distribution: tripoli5.delos.ICorrelatedDistribution*, *electron_configuration: tripoli5.delos.ElectronConfiguration*) → None
    :   Build from components.

        Parameters:
        :   primary_distribution : delos.ICorrelatedDistribution
            :   Energy-angle distribution for a photon in the first step of the sampling

            electron_configuration : delos.ElectronConfiguration
            :   Electron configuration of the target atom

    *property* electron_configuration

    *property* primary_distribution

*class* tripoli5.delos.CorrelatedDistributions
:   __init__(*correlated: tripoli5.delos.ICorrelatedDistribution*) → None
    :   Custom constructor from an ICorrelatedDistribution

    *property* correlated

*class* tripoli5.delos.Delay
:   __init__(*constant: SupportsFloat*) → None
    :   Build from value of decay constant.

    *property* is_prompt

    prompt() → tripoli5.delos.Delay

*class* tripoli5.delos.DistributionBetheHeitlerPP
:   __init__(*z: SupportsInt*, *r: SupportsFloat*, *fc: SupportsFloat*) → None
    :   Build from required data.

        Parameters:
        z : int [0-100], Atomic number
        r : float, Reduced screeining radius
        fc : float, Value of Coulomb correction term

*class* tripoli5.delos.DistributionBremsstrahlung
:   __init__(*egrid: tripoli5.delos.EnergyInterpolatedGrid*, *distributions: collections.abc.Sequence[tripoli5.delos.DivergentDistribution1D]*) → None
    :   Initialise from an energy grid and vector of distributions.

        Parameters:
        :   egrid : tripoli5.delos.EnergyInterpolatedGrid
            :   Incident particle energy grid.

            distributions : list[tripoli5.delos.DivergentDistribution1D]
            :   Outgoing energy distribution at each incident energy.

*class* tripoli5.delos.DistributionComptonISF
:   __init__(*x: collections.abc.Sequence[SupportsFloat]*, *isf: collections.abc.Sequence[SupportsFloat]*, *int_v: collections.abc.Sequence[tripoli5.delos.PDFInterpolationType]*, *nbt_v: collections.abc.Sequence[SupportsInt]*) → None
    :   nbt_v : Upper bound indices of each interpolation region.

*class* tripoli5.delos.DistributionContinuousInelastic
:   __init__(*egrid: tripoli5.delos.EnergyInterpolatedGrid*, *distributions: collections.abc.Sequence[tripoli5.delos.DistributionContinuousInelasticSingle]*) → None
    :   Custom constructor from a [`EnergyInterpolatedGrid`](#tripoli5.delos.EnergyInterpolatedGrid) and a list of [`DistributionContinuousInelasticSingle`](#tripoli5.delos.DistributionContinuousInelasticSingle)

    *property* distributions

    *property* egrid

*class* tripoli5.delos.DistributionContinuousInelasticSingle
:   __init__(*energy: tripoli5.delos.TabularDistribution*, *cosine: collections.abc.Sequence[tripoli5.delos.EquiprobableDistribution]*) → None
    :   Custom constructor from a [`TabularDistribution`](#tripoli5.delos.TabularDistribution) and a list of [`EquiprobableDistribution`](#tripoli5.delos.EquiprobableDistribution)

    *property* cosine

    *property* energy

*class* tripoli5.delos.DistributionContinuousTabular
:   __init__(*egrid: tripoli5.delos.EnergyInterpolatedGrid*, *distributions: collections.abc.Sequence[tripoli5.delos.TabularDistribution]*) → None
    :   Custom constructor from a [`EnergyInterpolatedGrid`](#tripoli5.delos.EnergyInterpolatedGrid) and a list of [`TabularDistribution`](#tripoli5.delos.TabularDistribution)

    *property* distributions

    *property* egrid

*class* tripoli5.delos.DistributionElasticScattering
:   __init__(*alpha: SupportsFloat*) → None
    :   Custom constructor from one float

    *property* alpha

*class* tripoli5.delos.DistributionElasticScatteringTSL
:   __init__() → None
    :   Custom constructor

*class* tripoli5.delos.DistributionEquiprobInelastic
:   __init__(*egrid: tripoli5.delos.EnergyInterpolatedGrid*, *distributions: collections.abc.Sequence[tripoli5.delos.DistributionEquiprobInelasticSingle]*) → None
    :   Custom constructor from a [`EnergyInterpolatedGrid`](#tripoli5.delos.EnergyInterpolatedGrid) and a list of [`DistributionEquiprobInelasticSingle`](#tripoli5.delos.DistributionEquiprobInelasticSingle)

    *property* distributions

    *property* egrid

*class* tripoli5.delos.DistributionEquiprobInelasticSingle
:   __init__(*energy: tripoli5.delos.EquiprobableDistribution*, *cosine: collections.abc.Sequence[tripoli5.delos.EquiprobableDistribution]*) → None
    :   Custom constructor from a [`EquiprobableDistribution`](#tripoli5.delos.EquiprobableDistribution) (the energy distribution) and a list of [`EquiprobableDistribution`](#tripoli5.delos.EquiprobableDistribution) (the angular distributions)

    *property* cosine

    *property* energy

*class* tripoli5.delos.DistributionEvaporationSpectrum
:   __init__(*temperature: tripoli5.delos.EnergyFunction*, *restrictionEnergy: SupportsFloat*) → None
    :   Custom constructor from an [`EnergyFunction`](#tripoli5.delos.EnergyFunction) and a float

    *property* restrictionEnergy

    *property* temperature

*class* tripoli5.delos.DistributionKalbach
:   __init__(*egrid: tripoli5.delos.EnergyInterpolatedGrid*, *distributions: collections.abc.Sequence[tripoli5.delos.DistributionKalbachSingle]*) → None
    :   Custom constructor from a [`EnergyInterpolatedGrid`](#tripoli5.delos.EnergyInterpolatedGrid) and a list of [`DistributionKalbachSingle`](#tripoli5.delos.DistributionKalbachSingle)

    *property* distributions

    *property* egrid

*class* tripoli5.delos.DistributionKalbachSingle
:   __init__(*energy: tripoli5.delos.TabularDistribution*, *precompoundR: collections.abc.Sequence[SupportsFloat]*, *angularA: collections.abc.Sequence[SupportsFloat]*) → None
    :   Custom constructor from a [`TabularDistribution`](#tripoli5.delos.TabularDistribution) and two vectors of floats

    *property* angularA

    *property* energy

    *property* precompoundR

*class* tripoli5.delos.DistributionKalbachTabular
:   __init__(*egrid: tripoli5.delos.EnergyInterpolatedGrid*, *distributions: collections.abc.Sequence[tripoli5.delos.DistributionKalbachTabularSingle]*) → None
    :   Custom constructor from a [`EnergyInterpolatedGrid`](#tripoli5.delos.EnergyInterpolatedGrid) and a list of [`DistributionKalbachTabularSingle`](#tripoli5.delos.DistributionKalbachTabularSingle)

    *property* distributions

    *property* egrid

*class* tripoli5.delos.DistributionKalbachTabularSingle
:   __init__(*energy: tripoli5.delos.TabularDistribution*, *cosine: collections.abc.Sequence[tripoli5.delos.TabularDistribution]*) → None
    :   Custom constructor from a [`TabularDistribution`](#tripoli5.delos.TabularDistribution) (the energy distribution) and a list of [`TabularDistribution`](#tripoli5.delos.TabularDistribution) (the angular distributions)

    *property* cosine

    *property* energy

*class* tripoli5.delos.DistributionKleinNishina
:   __init__() → None
    :   Klein-Nishina distribution has no parameters and no constructor arguments

*class* tripoli5.delos.DistributionLevelScattering
:   __init__(*param_1: SupportsFloat*, *param_2: SupportsFloat*) → None
    :   Custom constructor from two floats

    *property* param_1

    *property* param_2

*class* tripoli5.delos.DistributionNBody
:   __init__(*nb_bodies: SupportsInt*, *param_1: SupportsFloat*, *param_2: SupportsFloat*, *q_value: SupportsFloat*) → None
    :   Custom constructor from an integer and three floats

    *property* nb_bodies

    *property* param_1

    *property* param_2

    *property* q_value

*class* tripoli5.delos.DistributionSimpleMaxwellianFissionSpectrum
:   __init__(*temperature: tripoli5.delos.EnergyFunction*, *restrictionEnergy: SupportsFloat*) → None
    :   Custom constructor from an [`EnergyFunction`](#tripoli5.delos.EnergyFunction) and a float

    *property* restrictionEnergy

    *property* temperature

*class* tripoli5.delos.DistributionSkewedInelastic
:   __init__(*egrid: tripoli5.delos.EnergyInterpolatedGrid*, *distributions: collections.abc.Sequence[tripoli5.delos.DistributionSkewedInelasticSingle]*) → None
    :   Custom constructor from a [`EnergyInterpolatedGrid`](#tripoli5.delos.EnergyInterpolatedGrid) and a list of [`DistributionSkewedInelasticSingle`](#tripoli5.delos.DistributionSkewedInelasticSingle)

    *property* distributions

    *property* egrid

*class* tripoli5.delos.DistributionSkewedInelasticSingle
:   __init__(*energy: tripoli5.delos.SkewedDistribution*, *cosine: collections.abc.Sequence[tripoli5.delos.EquiprobableDistribution]*) → None
    :   Custom constructor from a [`SkewedDistribution`](#tripoli5.delos.SkewedDistribution) and a list of [`EquiprobableDistribution`](#tripoli5.delos.EquiprobableDistribution)

    *property* cosine

    *property* energy

*class* tripoli5.delos.DistributionWattSpectrum
:   __init__(*a: tripoli5.delos.EnergyFunction*, *b: tripoli5.delos.EnergyFunction*, *restrictionEnergy: SupportsFloat*) → None
    :   Custom constructor from a pair of [`EnergyFunction`](#tripoli5.delos.EnergyFunction) and a float

    *property* a

    *property* b

    *property* restrictionEnergy

*class* tripoli5.delos.DivergentDistribution1D
:   __init__(*values: collections.abc.Sequence[SupportsFloat]*, *pdf: collections.abc.Sequence[SupportsFloat]*, *cdf: collections.abc.Sequence[SupportsFloat]*, *interpolation_type: tripoli5.delos.PDFInterpolationType*) → None
    :   Construct from components

        Parameters:
        :   values : list[float]
            :   Grid of values on which distribution is tabulated.

            pdf : list[float]
            :   Magnitude of the table at each value.

            cdf : list[float]
            :   Integrated table including the 1/x factor.

            interpolation_type : tripoli5.delos.PDFInterpolationType
            :   Type of interpolation for the data in the table

*class* tripoli5.delos.DoubleFunction
:   __init__(*grid: tripoli5.delos.DoubleInterpolatedGrid*, *values: collections.abc.Sequence[SupportsFloat]*, *istart: SupportsInt = 0*) → None
    :   Custom constructor from a [`DoubleInterpolatedGrid`](#tripoli5.delos.DoubleInterpolatedGrid), a list of values and a threshold index

    *property* egrid

    *property* istart

    *property* threshold

    *property* values

*class* tripoli5.delos.DoubleInterpolatedGrid
:   __init__(**args*, ***kwargs*)
    :   Overloaded function.

        1. __init__(self: tripoli5.delos.DoubleInterpolatedGrid, values: collections.abc.Sequence[typing.SupportsFloat], INT: tripoli5.delos.PDFInterpolationType) -> None

        Custom constructor from a list of floats and a [`PDFInterpolationType`](#tripoli5.delos.PDFInterpolationType)

        2. __init__(self: tripoli5.delos.DoubleInterpolatedGrid, values: collections.abc.Sequence[typing.SupportsFloat], int_values: collections.abc.Sequence[tripoli5.delos.PDFInterpolationType], nbt_values: collections.abc.Sequence[typing.SupportsInt]) -> None

        Custom constructor from a list of floats, a list of interpolation types and a list of integers

    *property* int_values

    *property* nbt_values

    size() → int

    *property* values

*class* tripoli5.delos.ElectronConfiguration
:   __init__(*z: SupportsInt*, *shells: collections.abc.Sequence[tripoli5.delos.ElectronSubshell]*) → None
    :   Build a ground state configuration of an atom.

        Parameters:
        :   z : int
            :   Atomic number of the element. Used to check subshell data.

            shells : list of delos.ElectronSubshell
            :   Sorted list of subshells that constitute the ground state configuration

*class* tripoli5.delos.ElectronSubshell
:   __init__(*id_: tripoli5.delos.SubshellId*, *num_electron: SupportsInt*, *binding_energy: tripoli5.core.physics.Energy*, *compton_profile: tripoli5.delos.IComptonProfile*, *transitions: collections.abc.Sequence[tuple[tripoli5.delos.SubshellId, tripoli5.delos.SubshellId, tripoli5.core.physics.Energy, SupportsFloat]]*) → None
    :   Build representation of a single electron subshell of an element.

        Parameters:
        :   id_ : tripoli5.delos.SubshellId
            :   Id of the subshell

            num_electron : int
            :   Number of electrons in the subshell

            binding_energy : tripoli5.delos.Energy
            :   Binding energy of the subshell [MeV]

            compton_profile : tripoli5.delos.IComptonProfile
            :   Z-axis momentum distribution of electron in the subshell

            transitions : Sequence[tuple[int, int, float, float]]
            :   List of relevant relaxation transitions that can take place from this subshell
                (primary_subshell, secondary_subshell, transition_energy, probability)

*class* tripoli5.delos.Element
:   *property* Z

    __init__(*name: str*, *atomic_number: SupportsInt*, *photoatomic: tripoli5.delos.Photoatomic*, *electron_ttb: tripoli5.delos.TTB*, *positron_ttb: tripoli5.delos.TTB*) → None
    :   Custom constructor for element

        > Parameters:
        > :   name : str
        >     :   String with the name of the element
        >
        >     atomic_number : int
        >     :   Atomic number of the element in [1-100]
        >
        >     photoatomic : tripoli5.delos.Photoatomic
        >     :   Package with the interaction physics
        >
        >     electron_ttb : tripoli5.delos.TTB
        >     :   Thick target bremsstrahlung data for electrons.
        >
        >     positron_ttb : tripoli5.delos.TTB
        >     :   Thick target bremsstrahlung data for positrons.

    *property* electron_ttb

    *property* name

    *property* photoatomic

    *property* positron_ttb

    printSummary(*depth: SupportsInt*) → None

*class* tripoli5.delos.EnergyFunction
:   __init__(*egrid: tripoli5.delos.EnergyInterpolatedGrid*, *values: collections.abc.Sequence[SupportsFloat]*, *istart: SupportsInt = 0*) → None
    :   Custom constructor from a [`EnergyInterpolatedGrid`](#tripoli5.delos.EnergyInterpolatedGrid), a list of values and a threshold index

    *property* egrid

    *property* istart

    *property* threshold

    *property* values

*class* tripoli5.delos.EnergyInterpolatedGrid
:   __init__(**args*, ***kwargs*)
    :   Overloaded function.

        1. __init__(self: tripoli5.delos.EnergyInterpolatedGrid, values: collections.abc.Sequence[tripoli5.core.physics.Energy], INT: tripoli5.delos.PDFInterpolationType) -> None

        Custom constructor from a list of [`Energy`](core-api.md#tripoli5.core.physics.Energy) and a [`PDFInterpolationType`](#tripoli5.delos.PDFInterpolationType)

        2. __init__(self: tripoli5.delos.EnergyInterpolatedGrid, values: collections.abc.Sequence[tripoli5.core.physics.Energy], int_values: collections.abc.Sequence[tripoli5.delos.PDFInterpolationType], nbt_values: collections.abc.Sequence[typing.SupportsInt]) -> None

        Custom constructor from a list of [`Energy`](core-api.md#tripoli5.core.physics.Energy), a list of interpolation types and a list of integers

    *property* int_values

    *property* nbt_values

    size() → int

    *property* values

*class* tripoli5.delos.EquiprobableDistribution
:   __init__(*values: collections.abc.Sequence[SupportsFloat]*) → None
    :   Custom constructor from a list of floats

    *property* values

*class* tripoli5.delos.ExcludedReactionFilter
:   __init__(*accepted_reactions: collections.abc.Sequence[SupportsInt]*) → None
    :   ExcludedReactionFilter constructor

    accept(*arg0: SupportsInt*) → bool

*class* tripoli5.delos.ExclusiveReactionFilter
:   __init__(*accepted_reactions: collections.abc.Sequence[SupportsInt]*) → None
    :   ExclusiveReactionFilter constructor

    accept(*arg0: SupportsInt*) → bool

*class* tripoli5.delos.ExponentialComptonProfile
:   __init__()
    :   __init__(self: tripoli5.delos.ExponentialComptonProfile, Build exponential Compton profile from its parameter

        > Parameters:
        > :   central_value: float
        >     :   Value of the compton profile at 0.0. Must be positive.

        central_value: typing.SupportsFloat) -> None

    *property* central_value

*class* tripoli5.delos.FreeGas
:   __init__(*egrid: tripoli5.delos.EnergyInterpolatedGrid*, *reactions: collections.abc.Mapping[tripoli5.delos.ReactionId, tripoli5.delos.Reaction]*) → None
    :   Custom constructor from a [`EnergyInterpolatedGrid`](#tripoli5.delos.EnergyInterpolatedGrid) and a dictionary mapping [`ReactionId`](#tripoli5.delos.ReactionId) objects to [`Reaction`](#tripoli5.delos.Reaction) objects

    collectSections(*arg0: collections.abc.Sequence[tripoli5.delos.ReactionId]*) → tripoli5.delos.XSection

    *property* egrid

    *property* fissile

    getAdditionalReaction(*reactionid: tripoli5.delos.ReactionId*) → tripoli5.delos.Reaction

    getListOfSimpleReactions(*arg0: tripoli5.delos.ReactionId*) → list[tripoli5.delos.ReactionId]

    getReaction(*reactionid: tripoli5.delos.ReactionId*) → tripoli5.delos.Reaction

    getReactions() → dict[tripoli5.delos.ReactionId, tripoli5.delos.Reaction]

    getSummedXSection(*reactionid: tripoli5.delos.ReactionId*) → tripoli5.delos.XSection

    hasReactionId(*reactionid: tripoli5.delos.ReactionId*) → bool

    hasSimpleReactionId(*reactionid: tripoli5.delos.ReactionId*) → bool

    *property* nbAdditionalReactions

    nbReactions() → int

    removeReaction(*reaction: tripoli5.delos.ReactionId*) → None

    *property* total

*class* tripoli5.delos.IAngularDistribution2D
:   __init__(**args*, ***kwargs*)

*class* tripoli5.delos.IComptonProfile
:   __init__(**args*, ***kwargs*)

*class* tripoli5.delos.ICorrelatedDistribution
:   __init__(**args*, ***kwargs*)

*class* tripoli5.delos.IDiscreteDistribution
:   __init__(**args*, ***kwargs*)

*class* tripoli5.delos.IDistribution1D
:   __init__(**args*, ***kwargs*)

*class* tripoli5.delos.IEnergyAngleDistribution
:   __init__(**args*, ***kwargs*)

*class* tripoli5.delos.IEnergyDistribution
:   __init__(**args*, ***kwargs*)

*class* tripoli5.delos.IMultiplicity
:   __init__(**args*, ***kwargs*)

*class* tripoli5.delos.IOutProduct
:   __init__(**args*, ***kwargs*)

*class* tripoli5.delos.IReactionFilter
:   __init__(**args*, ***kwargs*)

*class* tripoli5.delos.ITSLReaction
:   __init__(**args*, ***kwargs*)

*class* tripoli5.delos.IncoherentAngularDistribution2D
:   __init__(*egrid: tripoli5.delos.EnergyInterpolatedGrid*, *distributions: collections.abc.Sequence[tripoli5.delos.EquiprobableDistribution]*) → None
    :   Custom constructor from a [`EnergyInterpolatedGrid`](#tripoli5.delos.EnergyInterpolatedGrid) and a list of [`EquiprobableDistribution`](#tripoli5.delos.EquiprobableDistribution)

    *property* distributions

    *property* energy

*class* tripoli5.delos.Infos
:   A container for the nuclide’s major identification informations, i.e. atomic numbers, mass, temperature, state, name.

    *property* A
    :   Mass number

    *property* Z
    :   Atomic number

    __init__(*name: str*, *A: SupportsInt*, *Z: SupportsInt*, *mass: tripoli5.core.physics.Mass*, *temperature: tripoli5.core.physics.Temperature*, *state: tripoli5.delos.NuclideState*) → None
    :   Custom constructor from a string, two integers, a [`Mass`](core-api.md#tripoli5.core.physics.Mass), a [`Temperature`](core-api.md#tripoli5.core.physics.Temperature), and a [`NuclideState`](#tripoli5.delos.NuclideState)

    *property* conventional_name

    *property* mass
    :   Mass of the nucleus

    *property* name
    :   The name of the nuclide, in the form XA (e.g. H1 or Ac225 or C0)

    *property* state
    :   State of the nuclide

    *property* temperature
    :   Temperature at which the nuclide’s cross section are provided

*class* tripoli5.delos.Isotropic1DDistribution
:   __init__() → None
    :   Custom constructor

*class* tripoli5.delos.IsotropicDistribution
:   __init__() → None
    :   Custom constructor

*class* tripoli5.delos.LegendreDistribution
:   __init__(*coefficients: collections.abc.Sequence[SupportsFloat]*) → None
    :   Custom constructor from a list of floats

    *property* coefficients

*class* tripoli5.delos.MassDataLibrary
:   Library for nuclear masses

    __init__(**args*, ***kwargs*)
    :   Overloaded function.

        1. __init__(self: tripoli5.delos.MassDataLibrary, url: str) -> None

        Constructor from an archive at url

        2. __init__(self: tripoli5.delos.MassDataLibrary) -> None

        Default constructor

    add(**args*, ***kwargs*)
    :   Overloaded function.

        1. add(self: tripoli5.delos.MassDataLibrary, filename: str) -> None
        2. add(self: tripoli5.delos.MassDataLibrary, mass_entry: tripoli5.delos.MassEntry) -> None

    has(*object_name: str*, *temperature: tripoli5.core.physics.Temperature*) → bool

    load(*object_name: str*, *temperature: tripoli5.core.physics.Temperature*) → tripoli5.delos.MassEntry

    printSummary() → None

*class* tripoli5.delos.MassEntry
:   __init__(**args*, ***kwargs*)
    :   Overloaded function.

        1. __init__(self: tripoli5.delos.MassEntry, infos: tripoli5.delos.Infos) -> None

        Constructor for MassEntry

        2. __init__(self: tripoli5.delos.MassEntry, key: str, mass: tripoli5.core.physics.Mass) -> None

        Constructor for MassEntry

    *property* g

    *property* key

    *property* neutronMass

*exception* tripoli5.delos.NDLException

*class* tripoli5.delos.NeutronDataLibrary
:   Library for free-gas neutron data

    __init__(**args*, ***kwargs*)
    :   Overloaded function.

        1. __init__(self: tripoli5.delos.NeutronDataLibrary, url: str) -> None

        Constructor from an archive at url

        2. __init__(self: tripoli5.delos.NeutronDataLibrary) -> None

        Default constructor

    add(*filename: str*) → None

    has(*object_name: str*, *temperature: tripoli5.core.physics.Temperature*) → bool

    load(*object_name: str*, *temperature: tripoli5.core.physics.Temperature*) → tripoli5.delos.Nuclide

    printSummary() → None

*class* tripoli5.delos.Nuclide
:   *property* A

    *property* Z

    __init__(*infos: tripoli5.delos.Infos*, *freegas: tripoli5.delos.FreeGas*) → None
    :   Custom constructor for nuclide

    *property* atomic_weight_ratio

    *property* fissile

    *property* freegas

    hasReactionId(*reactioNnId: tripoli5.delos.ReactionId*) → bool

    *property* infos

    *property* name

    *property* temperature

*class* tripoli5.delos.NuclideState
:   Members:

    Ground

    Level_1

    Level_2

    Level_3

    Level_4

    Ground *= NuclideState.Ground*

    Level_1 *= NuclideState.Level_1*

    Level_2 *= NuclideState.Level_2*

    Level_3 *= NuclideState.Level_3*

    Level_4 *= NuclideState.Level_4*

    __init__(*value: SupportsInt*) → None

    *property* name

    *property* value

*class* tripoli5.delos.OutProduct
:   __init__(*distribution: tripoli5.delos.OutProductDistributions*) → None
    :   Custom constructor for out products

    *property* distribution

*class* tripoli5.delos.OutProductDistributions
:   __init__(*multiplicity: tripoli5.delos.IMultiplicity*, *distributions: tripoli5.delos.IEnergyAngleDistribution*, *mass: tripoli5.core.physics.Mass*, *type: tripoli5.core.physics.ParticleType*, *decay_constant: tripoli5.delos.Delay*, *frame: tripoli5.delos.ReferenceFrame*) → None
    :   Custom constructor from a [`IEnergyAngleDistribution`](#tripoli5.delos.IEnergyAngleDistribution), a [`Mass`](core-api.md#tripoli5.core.physics.Mass) and a [`ReferenceFrame`](#tripoli5.delos.ReferenceFrame)

    *property* decay_constant

    *property* distributions

    *property* frame

    *property* mass

    *property* multiplicity

    *property* type

*class* tripoli5.delos.OutProductDual
:   __init__(*E_cut: tripoli5.core.physics.Energy*, *distribution_left: tripoli5.delos.OutProductDistributions*, *distribution_right: tripoli5.delos.OutProductDistributions*) → None
    :   Custom constructor for out products

    *property* distribution_left

    *property* distribution_right

    *property* e_cut

*class* tripoli5.delos.PDFInterpolationType
:   Members:

    Histogram

    LinLin

    LogLog

    LinLog

    LogLin

    Histogram *= PDFInterpolationType.Histogram*

    LinLin *= PDFInterpolationType.LinLin*

    LinLog *= PDFInterpolationType.LinLog*

    LogLin *= PDFInterpolationType.LogLin*

    LogLog *= PDFInterpolationType.LogLog*

    __init__(*value: SupportsInt*) → None

    *property* name

    *property* value

*class* tripoli5.delos.PairProductionOutProduct
:   __init__(*energy_distribution: tripoli5.delos.IEnergyDistribution*, *angle_distribution: tripoli5.delos.IAngularDistribution2D*) → None
    :   Build from components.

        Parameters:
        :   energy_distribution : delos.IEnergyDistribution
            :   Energy distribution of the outgoing electron

            angle_distribution : delos.IAngularDistribution2D
            :   Angular distribution dependent on the energy of the emitted particle.

    *property* angle_distribution

    *property* energy_distribution

*class* tripoli5.delos.Photoatomic
:   __init__()
    :   __init__(self: tripoli5.delos.Photoatomic, Custom constructor.

        Parameters:
        :   egrid : delos.EnergyInterpolatedGrid
            :   Common energy grid for all reactions

            reactions : map of delos.ReactionId to delos.Reaction
            :   List of all reactions used in transport

        egrid: tripoli5.delos.EnergyInterpolatedGrid, reactions: collections.abc.Mapping[tripoli5.delos.ReactionId, tripoli5.delos.Reaction]) -> None

    computeTotal() → None

    *property* egrid

    getReactions() → dict[tripoli5.delos.ReactionId, tripoli5.delos.Reaction]

    hasReactionId(*reactionid: tripoli5.delos.ReactionId*) → bool

    nbReactions() → int

    reaction(*reactionid: tripoli5.delos.ReactionId*) → tripoli5.delos.Reaction

    removeReaction(*reaction: tripoli5.delos.ReactionId*) → None

    *property* total

*class* tripoli5.delos.PhotoelectricOutProduct
:   __init__(*id: tripoli5.delos.SubshellId*, *angle_distribution: tripoli5.delos.IAngularDistribution2D*, *electron_config: tripoli5.delos.ElectronConfiguration*) → None
    :   Build from components.

        Parameters:
        :   id : delos.SubshellId
            :   Id of the subshell from which the photoelectron will be ejected.

            angle_distribution : delos.IAngularDistribution2D
            :   Angular distribution dependent on the energy of emitted photoelectron.

            electron_config : delos.ElectronConfiguration
            :   Electron configuration of the target element.

    *property* angle_distribution

    *property* binding_energy

    *property* electron_config

    *property* hole_id

*class* tripoli5.delos.PhotonDataLibrary
:   Library for photon data

    __init__(**args*, ***kwargs*)
    :   Overloaded function.

        1. __init__(self: tripoli5.delos.PhotonDataLibrary, url: str) -> None

        Constructor from an archive at url

        2. __init__(self: tripoli5.delos.PhotonDataLibrary) -> None

        Default constructor

    add(*filename: str*) → None

    has(*object_name: str*, *temperature: tripoli5.core.physics.Temperature*) → bool

    load(*object_name: str*, *temperature: tripoli5.core.physics.Temperature*) → tripoli5.delos.Element

    printSummary() → None

*class* tripoli5.delos.PolynomialMultiplicity
:   __init__(*multiplicity: collections.abc.Sequence[SupportsFloat]*) → None
    :   Custom constructor from a vector

    *property* coefficients

*class* tripoli5.delos.RayleighAngularDistribution2D
:   __init__(*x_sq: collections.abc.Sequence[SupportsFloat]*, *ff_sq: collections.abc.Sequence[SupportsFloat]*, *ff_sq_int: collections.abc.Sequence[SupportsFloat]*, *inter: tripoli5.delos.PDFInterpolationType*) → None
    :   Initialise from members.

        Parameters:
        :   x_sq: values of square of the momentum transfer
            ff_sq: values of the square of the form factor
            ff_sq_int: integral of ff_sq from x_sq = 0.0
            inter: type of interpolation of ff_sq

*class* tripoli5.delos.Reaction
:   __init__(*Q: SupportsFloat*, *xsection: tripoli5.delos.XSection*, *frame: tripoli5.delos.ReferenceFrame*, *outproducts: collections.abc.Sequence[tripoli5.delos.IOutProduct]*) → None
    :   Custom constructor from the Q-value (a floating-point number), a [`XSection`](#tripoli5.delos.XSection), a [`ReferenceFrame`](#tripoli5.delos.ReferenceFrame) and a list of [`IOutProduct`](#tripoli5.delos.IOutProduct)

    *property* frame

    *property* nbOutProducts

    *property* outProducts

    *property* qvalue

    *property* startIndex

    *property* threshold

    *property* xsection

    *property* xsection_values

*class* tripoli5.delos.ReactionId
:   *property* MT

    __init__(*MT: SupportsInt*) → None
    :   Construct a [:cls:`ReactionId`](#id1) from an int representing the MT number

    *property* name

*class* tripoli5.delos.ReferenceFrame
:   Members:

    CM

    LAB

    CM *= ReferenceFrame.CM*

    LAB *= ReferenceFrame.LAB*

    __init__(*value: SupportsInt*) → None

    *property* name

    *property* value

*class* tripoli5.delos.SGHAngularDistribution2D
:   __init__() → None
    :   Sauter-Gluckstren-Hull distribution requires no element-dependent parameters.

*class* tripoli5.delos.SauterAngularDistribution2D
:   __init__() → None
    :   Sauter distribution requires no element-dependent parameters.

*class* tripoli5.delos.ScalarMultiplicity
:   __init__(*multiplicity: SupportsFloat*) → None
    :   Custom constructor from a float

    *property* multiplicity

*class* tripoli5.delos.SkewedDistribution
:   __init__(*values: collections.abc.Sequence[SupportsFloat]*) → None
    :   Custom constructor from a list of floats

    *property* values

*class* tripoli5.delos.StoppingPower
:   __init__(*egrid: tripoli5.delos.EnergyInterpolatedGrid*, *values: collections.abc.Sequence[SupportsFloat]*) → None
    :   Build a tabulated stopping power on top of an energy grid

    *property* egrid

    *property* values

*class* tripoli5.delos.SubshellId
:   __init__(*endf_idx: SupportsInt*) → None
    :   Build from ENDF subshell index

        Parameters:
        :   endf_idx: int
            :   Index of the subshell from ENDF [1-39]. Accepts 0 to create null Subshell which is used to mark radiative transitions

*class* tripoli5.delos.TSL
:   __init__(*reactions: collections.abc.Mapping[tripoli5.delos.TSLReactionId, tripoli5.delos.ITSLReaction]*, *name: str*, *temperature: tripoli5.core.physics.Temperature*) → None
    :   Custom constructor from a map of [`TSLReactionId`](#tripoli5.delos.TSLReactionId) to [`ITSLReaction`](#tripoli5.delos.ITSLReaction), a string representing the nuclide name, and a [`Temperature`](core-api.md#tripoli5.core.physics.Temperature)

    *property* name

    *property* temperature

*class* tripoli5.delos.TSLDataLibrary
:   Library for neutron data for thermal scattering

    __init__(**args*, ***kwargs*)
    :   Overloaded function.

        1. __init__(self: tripoli5.delos.TSLDataLibrary, url: str) -> None

        Constructor from an archive at url

        2. __init__(self: tripoli5.delos.TSLDataLibrary) -> None

        Default constructor

    add(*filename: str*) → None

    has(*object_name: str*, *temperature: tripoli5.core.physics.Temperature*) → bool

    load(*object_name: str*, *temperature: tripoli5.core.physics.Temperature*) → tripoli5.delos.TSL

    printSummary() → None

*class* tripoli5.delos.TSLReaction
:   __init__(*egrid: tripoli5.delos.EnergyInterpolatedGrid*, *xsection: tripoli5.delos.XSection*, *outproducts: collections.abc.Sequence[tripoli5.delos.IOutProduct]*) → None
    :   Custom constructor from a [`EnergyInterpolatedGrid`](#tripoli5.delos.EnergyInterpolatedGrid), a [`XSection`](#tripoli5.delos.XSection) and a list of [`IOutProduct`](#tripoli5.delos.IOutProduct)

    *property* egrid

    *property* outproducts

    *property* xsection

*class* tripoli5.delos.TSLReactionBragg
:   __init__(*egrid: tripoli5.delos.EnergyInterpolatedGrid*, *edges: tripoli5.delos.BraggEdges*, *distribution: collections.abc.Sequence[tripoli5.delos.IOutProduct]*) → None
    :   Custom constructor from a [`EnergyInterpolatedGrid`](#tripoli5.delos.EnergyInterpolatedGrid), a [`BraggEdges`](#tripoli5.delos.BraggEdges) and a [`IEnergyAngleDistribution`](#tripoli5.delos.IEnergyAngleDistribution)

    *property* edges

    *property* egrid

    *property* outproducts

*class* tripoli5.delos.TSLReactionId
:   __init__(*label: tripoli5.delos.TSLReactionLabel*) → None
    :   Custom constructor from a [`TSLReactionLabel`](#tripoli5.delos.TSLReactionLabel)

    to_mt() → int

*class* tripoli5.delos.TSLReactionLabel
:   Members:

    Inelastic

    CoherentElastic

    IncoherentElastic

    CoherentElastic *= <TSLReactionLabel.CoherentElastic: 1>*

    IncoherentElastic *= <TSLReactionLabel.IncoherentElastic: 2>*

    Inelastic *= <TSLReactionLabel.Inelastic: 0>*

    __init__(*value: SupportsInt*) → None

    *property* name

    *property* value

*class* tripoli5.delos.TTB
:   __init__(*stopping_power: tripoli5.delos.StoppingPower*, *hard_bremsstrahlung: tripoli5.delos.Reaction*) → None
    :   Initialise the Thick Target Bremsstrahlung data from components.

        Parameters:
        :   stopping_power : tripoli5.delos.StoppingPower
            :   Log-Log interpolated values of stopping power [MeV/barn/cm]

            hard_bremsstrahlung : tripoli5.delos.Reaction
            :   Reaction data for large energy loss radiative event. Must use
                the same grid as stopping_power

*class* tripoli5.delos.TabularComptonProfile
:   __init__(*pz_grid: collections.abc.Sequence[SupportsFloat]*, *profile: collections.abc.Sequence[SupportsFloat]*, *integrated_profile: collections.abc.Sequence[SupportsFloat]*, *interp: tripoli5.delos.PDFInterpolationType*) → None
    :   Build Compton profile table from components

        > Parameters:
        > :   pz_grid: list of float
        >     :   Must begin at 0.0. List of momentum values
        >
        >     profile: list of float
        >     :   Values of the compton profile
        >
        >     integrated_profile: list of float
        >     :   Integrated values of the compton profile (Cdf function)
        >
        >     interp: pyNDL.PDFInterpolationType
        >     :   Interpolation type for the data

    *property* table

*class* tripoli5.delos.TabularDistribution
:   __init__(*values: collections.abc.Sequence[SupportsFloat]*, *pdf: collections.abc.Sequence[SupportsFloat]*, *cdf: collections.abc.Sequence[SupportsFloat]*, *interpolation_type: tripoli5.delos.PDFInterpolationType*) → None
    :   Custom constructor from three lists of floats and a [`PDFInterpolationType`](#tripoli5.delos.PDFInterpolationType)

    *property* cdf

    *property* interpolation

    *property* pdf

    *property* values

*class* tripoli5.delos.TabularMultiplicity
:   __init__(*egrid: tripoli5.delos.EnergyInterpolatedGrid*, *values: collections.abc.Sequence[SupportsFloat]*) → None
    :   Custom constructor from a [`EnergyInterpolatedGrid`](#tripoli5.delos.EnergyInterpolatedGrid) and a list of floats

    *property* multiplicity

*class* tripoli5.delos.UncorrelatedDistributions
:   __init__(*angle: tripoli5.delos.IAngularDistribution2D*, *energy: tripoli5.delos.IEnergyDistribution*) → None
    :   Custom constructor from an angular and energetic distributions

    *property* angle

    *property* energy

*class* tripoli5.delos.XSection
:   __init__(*egrid: tripoli5.delos.EnergyInterpolatedGrid*, *values: collections.abc.Sequence[SupportsFloat]*, *istart: SupportsInt*) → None
    :   Custom constructor from an [`EnergyInterpolatedGrid`](#tripoli5.delos.EnergyInterpolatedGrid), a list of cross section values (floats), and an integer representing the offset of the first value in the energy grid

    *property* egrid

    *property* istart

    *property* threshold

    *property* values

tripoli5.delos.conventionalRounding(*temperature: tripoli5.core.physics.Temperature*) → int

tripoli5.delos.deserialize(**args*, ***kwargs*)
:   Overloaded function.

    1. deserialize(arg0: str, arg1: tripoli5.delos.Nuclide) -> None
    2. deserialize(arg0: str, arg1: tripoli5.delos.Element) -> None
    3. deserialize(arg0: str, arg1: tripoli5.delos.TSL) -> None
    4. deserialize(arg0: str, arg1: tripoli5.delos.ACEURR) -> None
    5. deserialize(arg0: str, arg1: tripoli5.delos.CALENDFURR) -> None

tripoli5.delos.deserializeACEURR(*arg0: str*) → tripoli5.delos.ACEURR

tripoli5.delos.deserializeCALENDFURR(*arg0: str*) → tripoli5.delos.CALENDFURR

tripoli5.delos.deserializeElement(*arg0: str*) → tripoli5.delos.Element

tripoli5.delos.deserializeNuclide(*arg0: str*) → tripoli5.delos.Nuclide

tripoli5.delos.deserializeTSL(*arg0: str*) → tripoli5.delos.TSL

tripoli5.delos.mt_to_string(*arg0: SupportsInt*) → str

tripoli5.delos.serialize(**args*, ***kwargs*)
:   Overloaded function.

    1. serialize(arg0: str, arg1: tripoli5.delos.Nuclide) -> None
    2. serialize(arg0: str, arg1: tripoli5.delos.Element) -> None
    3. serialize(arg0: str, arg1: tripoli5.delos.TSL) -> None
    4. serialize(arg0: str, arg1: tripoli5.delos.ACEURR) -> None
    5. serialize(arg0: str, arg1: tripoli5.delos.CALENDFURR) -> None
    6. serialize(arg0: str, arg1: tripoli5.delos.NeutronDataLibrary) -> None
    7. serialize(arg0: str, arg1: tripoli5.delos.TSLDataLibrary) -> None
    8. serialize(arg0: str, arg1: tripoli5.delos.ACEURRDataLibrary) -> None
    9. serialize(arg0: str, arg1: tripoli5.delos.CALENDFURRDataLibrary) -> None
    10. serialize(arg0: str, arg1: tripoli5.delos.PhotonDataLibrary) -> None
    11. serialize(arg0: str, arg1: tripoli5.delos.MassDataLibrary) -> None

tripoli5.delos.serialize_to_base(**args*, ***kwargs*)
:   Overloaded function.

    1. serialize_to_base(arg0: str, arg1: tripoli5.delos.IDiscreteDistribution) -> None
    2. serialize_to_base(arg0: str, arg1: tripoli5.delos.IEnergyDistribution) -> None
    3. serialize_to_base(arg0: str, arg1: tripoli5.delos.IAngularDistribution2D) -> None
    4. serialize_to_base(arg0: str, arg1: tripoli5.delos.ICorrelatedDistribution) -> None
