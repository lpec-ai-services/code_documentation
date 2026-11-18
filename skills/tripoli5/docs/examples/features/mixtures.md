<!-- source: https://tripoli5.asnr.dev/documentation/latest-release/examples/features/mixtures.html -->

# Mixtures

Material compositions in TRIPOLI-5 are defined as a list of mixtures. Each `mixture` is an object of the `tripoli5.materials` Python module. In this notebook, we will focus on describing how to create a mixture from technological data, including:

- The composition of the mixture (nuclides and their concentrations)
- The state of the medium (temperature and density)
- The correspondence between compositions and geometric volumes (composition name)

## Imports

The necessary TRIPOLI-5 Python modules for `Mixtures` are available by importing tripoli5:

```ipython3
import tripoli5
from tripoli5.core.physics import Temperature, Density
from tripoli5.core.literals import K, gPerCm3
```

## Mixture Builder

Mixtures are created using the `tripoli5.materials.MixtureBuilder` class.

A `MixtureBuidler` is a helper for creating a mixture that contains one material composition. The `MixtureBuidler` is instantiated with an input method for the nuclide amounts : `"concentrations"`, `"mass_fractions"` or `"atom_fractions"`. Once instantiated, one can define a mixture with the following data:

- A **name** (making the “association” to the physical volume having the same `tripoli5.pyAGORA.Volume` attribut) using the `.addName(...)` method.
- A **mass data library** using the `.withCatalog(...)` method.
- A **temperature** using the `.withTemperature(...)` method.
- A **set of nuclides** (names in the `Delos` format) and their respective **density**, **mass fraction**, or **atom fraction** using the `.add(...)` method.
- A **total material density** (for “mass_fractions” and “atom_fractions” arguments) using the `.withDensity(...)` method.

It is also possible to define:

- A **temperature field** using the `.withTemperatureField(...)` method.
- A **density field** using the `.withDensityField(...)` method.
- A **Natural elements** decomposition using the `.withNaturalAbundances(...)` method.

Finally, the `.build()` method is required to build the material composition.

### Example: Create a fuel mixture

Loading nuclides mass data is required by the `tripoli5.materials.MixtureBuilder` class to compute densities. The path to the nuclear/mass data can be specified by setting the catalog path.

```ipython3
catalog = tripoli5.delos.Catalog.fromFile(
    f"/opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/endfb8r0_mcnp_v{tripoli5.delos.CATALOG_VERSION}.yaml"
)
```

```

[2026-01-30 16:45:41.016] [info] Loading catalog from file: /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/endfb8r0_mcnp_v2.2.0.yaml
```

For instance, we can create a fuel mixture as follows:

```ipython3
fuel_mixture = (
    tripoli5.materials.MixtureBuilder("concentrations")  # in [at./barn.cm]
    .withName("FUEL")
    .withCatalog(catalog)
    .withTemperature(294 * K)
    .add("U234", 4.8416e-05)
    .add("U235", 4.8151e-03)
    .add("U236", 1.7407e-05)
    .add("U238", 4.3181e-02)
    .build()
)
```

```

[2026-01-30 16:45:41.053] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/mass/njoy_ace/v0.2.0/archive/wrapped_mass_data.bin
```

In order to verify the mixture data, one can print the content of a mixture

```ipython3
# Get a Summary of the mixture
fuel_mixture.printSummary()
```

```

[2026-01-30 16:45:41.071] [info] Mixture: FUEL
[2026-01-30 16:45:41.072] [info] Temperature field:  Temperature is: 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]

[2026-01-30 16:45:41.072] [info] === Owning mixture composition: ===
Number of IDs: 1
Number of nuclides: 4
IDs: U234 U235 U236 U238
0 4.8416e-05 0.0048151 1.7407e-05 0.043181
```

Nuclides and their concentrations can also be specified as lists. Below, we create a clad mixture using directly a list of nuclides and concentrations in `at/barn.cm`

```ipython3
clad_nuclides = ["ZR90", "ZR91", "ZR92", "ZR94", "ZR96"]
clad_concentrations = [
    1.957843e-02,
    4.269010e-03,
    6.526535e-03,
    6.613164e-03,
    1.064150e-03,
]

clad_mixture = (
    tripoli5.materials.MixtureBuilder("concentrations")
    .withName("CLAD")
    .withTemperature(294 * K)
    .withCatalog(catalog)
    .add(clad_nuclides, clad_concentrations)
    .build()
)

clad_mixture.printSummary()
```

```

[2026-01-30 16:45:41.091] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/mass/njoy_ace/v0.2.0/archive/wrapped_mass_data.bin
[2026-01-30 16:45:41.096] [info] Mixture: CLAD
[2026-01-30 16:45:41.096] [info] Temperature field:  Temperature is: 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]

[2026-01-30 16:45:41.096] [info] === Owning mixture composition: ===
Number of IDs: 1
Number of nuclides: 5
IDs: ZR90 ZR91 ZR92 ZR94 ZR96
0 0.01957843 0.00426901 0.006526535 0.006613164 0.00106415
```

### Input methods for nuclides amounts

Now, we will build a water mixture for each input method of `MixtureBuilder`:

- Concentrations
- Mass fractions
- Atom fractions

The fractions specified for each nuclide/element are relative and are automatically renormalized if their sum differs from 1.0 by more than 1.e-10. The acceptable tolerance is 0.05.

Their concentrations are computed based on the total density of the material. The total density is set using `.withDensity` method.

The total density can be specified in gram per cubic centimeter (\(\mathrm{g}/\mathrm{cm}^3\)).

```ipython3
# water data
water_density = 1.00705 * gPerCm3
nuclides = ["H1", "O16", "B10", "B11"]
concentrations = [0.0666798, 0.0333687, 0.000382626, 0.000154012]  # [at./barn.cm]
mass_fractions = [0.11081, 0.880077, 0.00631736, 0.00279584]
atom_fractions = [0.662919, 0.331746, 0.003804, 0.00153116]
```

#### Concentrations

The densities are specified for each nuclide/element in atoms per barn-cm.

It is not mandatory to define the total density, but if it is provided, the concentrations are renormalized based on the total density of the material.

```ipython3
water_c = (
    tripoli5.materials.MixtureBuilder("concentrations")
    .withName("WATER")
    .withCatalog(catalog)
    .withTemperature(294 * K)
    .add(nuclides, concentrations)
    .build()
)
water_c.printSummary()
```

```

[2026-01-30 16:45:41.135] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/mass/njoy_ace/v0.2.0/archive/wrapped_mass_data.bin
[2026-01-30 16:45:41.141] [info] Mixture: WATER
[2026-01-30 16:45:41.141] [info] Temperature field:  Temperature is: 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]

[2026-01-30 16:45:41.141] [info] === Owning mixture composition: ===
Number of IDs: 1
Number of nuclides: 4
IDs: H1 O16 B10 B11
0 0.0666798 0.0333687 0.000382626 0.000154012
```

#### Mass fractions

Below is an example of defining a mixture using mass fractions.

In this case, poviding a density is mandatory and the fractions should sum to 1.

```ipython3
water_m = (
    tripoli5.materials.MixtureBuilder("mass_fractions")
    .withName("WATER")
    .withCatalog(catalog)
    .withDensity(water_density)
    .withTemperature(294 * K)
    .add(nuclides, mass_fractions)
    .build()
)
water_m.printSummary()
```

```

[2026-01-30 16:45:41.162] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/mass/njoy_ace/v0.2.0/archive/wrapped_mass_data.bin
[2026-01-30 16:45:41.188] [warning] The sum of fractions for mixture WATER differs from 1.0 by more than 1e-10. Sum: 1.0000002000000001. The fractions will be automatically renormalized.
[2026-01-30 16:45:41.188] [info] Mixture: WATER
[2026-01-30 16:45:41.188] [info] Temperature field:  Temperature is: 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]

[2026-01-30 16:45:41.188] [info] === Owning mixture composition: ===
Number of IDs: 1
Number of nuclides: 4
IDs: H1 O16 B10 B11
0 0.06668003317991214 0.033368801742690156 0.00038262733669826906 0.00015401231365162515
```

#### Atom Fraction

Below is an example of defining a mixture using atom fractions.

In this case, poviding a density is mandatory and the fractions should sum to 1.

```ipython3
water_a = (
    tripoli5.materials.MixtureBuilder("atom_fractions")
    .withName("WATER")
    .withCatalog(catalog)
    .withDensity(water_density)
    .withTemperature(294 * K)
    .add(nuclides, atom_fractions)
    .build()
)
water_a.printSummary()
```

```

[2026-01-30 16:45:41.209] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/mass/njoy_ace/v0.2.0/archive/wrapped_mass_data.bin
[2026-01-30 16:45:41.215] [warning] The sum of fractions for mixture WATER differs from 1.0 by more than 1e-10. Sum: 1.0000001600000001. The fractions will be automatically renormalized.
[2026-01-30 16:45:41.215] [info] Mixture: WATER
[2026-01-30 16:45:41.215] [info] Temperature field:  Temperature is: 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]

[2026-01-30 16:45:41.215] [info] === Owning mixture composition: ===
Number of IDs: 1
Number of nuclides: 4
IDs: H1 O16 B10 B11
0 0.0666799758046644 0.03336880562073827 0.00038262687894138404 0.00015401234804413502
```

### Natural Abundances

It is possible to build mixtures using natural abundances database using the `tripoli5.materials.NaturalAbundances` object as an argument of the `.withNaturalAbundances` method of `MixtureBuilder`. The `NaturalAbundances` class allows you to define the natural abundances of an element by providing nuclides from the neutron data library with their corresponding natural atom fractions.

TRIPOLI-5 provides some pre-defined database of element decomposition: `NUBASE2020`, `MORET6` and `OpenMC`.

Users can defined their own custom database if needed.

#### Build mixture using natural abundances

Specifying a database of element decomposition when building a mixture is performed using the `withNaturalAbundances` method. Below is an example of using the `NUBASE2020` database for decomposing the `Fe` element into its isotopes.

```ipython3
# build fer mixture using NUBASE2020 natural abundances

fer_with_natural_abundance = (
    tripoli5.materials.MixtureBuilder("atom_fractions")
    .withName("FER_NuBase2020")
    .withCatalog(catalog)
    .withTemperature(294 * K)
    .withDensity(5.883561 * gPerCm3)
    .withNaturalAbundances(tripoli5.materials.NaturalAbundances.fromNUBASE2020())
    .add("FE", 1.0)
    .build()
)
fer_with_natural_abundance.printSummary()
```

```

[2026-01-30 16:45:41.236] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/mass/njoy_ace/v0.2.0/archive/wrapped_mass_data.bin
[2026-01-30 16:45:41.244] [info] Mixture: FER_NuBase2020
[2026-01-30 16:45:41.244] [info] Temperature field:  Temperature is: 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]

[2026-01-30 16:45:41.244] [info] === Owning mixture composition: ===
Number of IDs: 1
Number of nuclides: 4
IDs: FE54 FE56 FE57 FE58
0 0.003708431396439277 0.0582144421469443 0.0013444253428665234 0.0001789183325570361
```

#### Exploring the element decomposition database

Below we show how the user may explore the element decomposition database.

The example is taken with the `NUBASE2020` data but is application to all pre-defined database.

To retrieve a `NaturalAbundances` object based on data from `NUBASE2020`, you can use the static method `fromNUBASE2020`.

The `OpenMC` and `MORET6` databases can be retrieved using the `fromOpenMC` and `fromMORET6` respectively.

```ipython3
# Using the fromNUBASE2020 method to create a NaturalAbundances object
na_nb20 = tripoli5.materials.NaturalAbundances.fromNUBASE2020()
```

Methods are defined to retrieve information about the `NaturalAbundances` object, including the origin of the natural abundance data (e.g., ‘User defined’, ‘MORET6’, ‘NUBASE2020’, ‘OpenMC’), the element names, the nuclide abundances for an element, the abundance of a specific nuclide, and whether an element is defined.

```ipython3
# Print the origin of the natural abundances data
print(f"Origin: {na_nb20.origin}")

# Print the names of the elements in the natural abundances data
print(f"Element Names: {na_nb20.getElementNames()}")

# Check if the element 'ZR' is present in the natural abundances list
if na_nb20.hasElement("ZR"):
    print("ZR element is contained in the natural abundances list")

# Print the nuclide abundances for the element 'ZR'
print(f"Nuclide abundances of ZR: {na_nb20['ZR']}")

# Print the abundance of a specific nuclide 'ZR90'
print(f"ZR90: {na_nb20.getNuclideAbundance('ZR', 'ZR90')}")
```

```

Origin: NUBASE2020
Element Names: ['AU', 'OS', 'TA', 'LU', 'HG', 'TM', 'YB', 'HO', 'RE', 'TB', 'U', 'DY', 'GD', 'EU', 'SM', 'MN', 'Y', 'BI', 'NI', 'ER', 'C', 'V', 'CE', 'N', 'AS', 'RB', 'SI', 'PD', 'H', 'S', 'CU', 'I', 'HF', 'SC', 'LI', 'O', 'CL', 'K', 'ZN', 'NE', 'SR', 'F', 'PB', 'CR', 'PT', 'CO', 'FE', 'SN', 'W', 'NA', 'AR', 'HE', 'RH', 'TI', 'IN', 'P', 'AG', 'PA', 'TH', 'B', 'MG', 'GA', 'IR', 'RU', 'GE', 'KR', 'SE', 'MO', 'BR', 'ZR', 'BE', 'CD', 'TE', 'NB', 'SB', 'TL', 'XE', 'AL', 'CS', 'BA', 'LA', 'CA', 'PR', 'ND']
ZR element is contained in the natural abundances list
Nuclide abundances of ZR: [('ZR90', 0.5145000000000001), ('ZR91', 0.11220000000000001), ('ZR92', 0.17149999999999999), ('ZR94', 0.17379999999999998), ('ZR96', 0.027999999999999997)]
ZR90: 0.5145000000000001
```

Another method, `filterWithNuclidesIn`, allows you to filter the natural abundances based on the nuclides present in the neutron data library at a specified temperature. This method takes a neutron data library and a temperature as arguments.

```ipython3
# Load neutron data library for specific nuclides
ndl = tripoli5.materials.NeutronDataLibraryDirectorySource(catalog)

# Filter the natural abundances with the nuclides present in the neutron data library at 294 Kelvin
na_nb20.filterWithNuclidesIn(ndl, 294 * K)

# Print the filtered natural abundances
print(
    "Filter the natural abundances with the nuclides present in the neutron data library at 294 K: "
)
print(f"{na_nb20.getElementNames()}")
```

```

Filter the natural abundances with the nuclides present in the neutron data library at 294 K:
['AU', 'OS', 'TA', 'LU', 'HG', 'TM', 'YB', 'HO', 'RE', 'TB', 'U', 'DY', 'GD', 'EU', 'SM', 'MN', 'Y', 'BI', 'NI', 'ER', 'C', 'V', 'CE', 'N', 'AS', 'RB', 'SI', 'PD', 'H', 'S', 'CU', 'I', 'HF', 'SC', 'LI', 'O', 'CL', 'K', 'ZN', 'NE', 'SR', 'F', 'PB', 'CR', 'PT', 'CO', 'FE', 'SN', 'W', 'NA', 'AR', 'HE', 'RH', 'TI', 'IN', 'P', 'AG', 'PA', 'TH', 'B', 'MG', 'GA', 'IR', 'RU', 'GE', 'KR', 'SE', 'MO', 'BR', 'ZR', 'BE', 'CD', 'TE', 'NB', 'SB', 'TL', 'XE', 'AL', 'CS', 'BA', 'LA', 'CA', 'PR', 'ND']
```

```ipython3
# Filter the natural abundances with the nuclides present in the neutron data library at 300 Kelvin
na_nb20.filterWithNuclidesIn(ndl, 300 * K)

# Print the filtered natural abundances
print(
    "Filter the natural abundances with the nuclides present in the neutron data library at 300 K: "
)
print(f"{na_nb20.getElementNames()}")
```

```

Filter the natural abundances with the nuclides present in the neutron data library at 300 K:
[]
```

#### Defining a custom natural abundances database

To define a custom natural abundances using the NaturalAbundances class, one may provide a dictionary with the isotopic data. Note that the abundances have to be given as atom fractions.

First, let’s examine the available data in the mass data base and the neutron data library. For example, to check for the existence of mass data on Zirconium element or the presence of isotopes of Zr in the Neutron Data Library, you can use the `.has()` method in both cases on the `MassDataLibraryArchiveSource` and `NeutronDataLibraryDirectorySource` objects.

```ipython3
# Load mass data for the ZR element
mass_data = tripoli5.materials.MassDataLibraryArchiveSource(catalog)
```

```

[2026-01-30 16:45:41.697] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/mass/njoy_ace/v0.2.0/archive/wrapped_mass_data.bin
```

```ipython3
# Check if the natural abundance of ZR is provided in the mass data base
print(
    f"Is ZR natural abundance provided in the mass data base: {mass_data.has('ZR', (294 * K).K)}"
)
```

```

Is ZR natural abundance provided in the mass data base: False
```

```ipython3
# Load neutron data library for specific nuclides
ndl = tripoli5.materials.NeutronDataLibraryDirectorySource(catalog)

# Check if specific nuclides (ZR90, ZR91, ZR92, ZR94, ZR96) are provided in the neutron data library
print(f"Is ZR90 nuclide provided in the ndl: {ndl.has('ZR90', 294)}")
print(f"Is ZR91 nuclide provided in the ndl: {ndl.has('ZR91', 294)}")
print(f"Is ZR92 nuclide provided in the ndl: {ndl.has('ZR92', 294)}")
print(f"Is ZR94 nuclide provided in the ndl: {ndl.has('ZR94', 294)}")
print(f"Is ZR96 nuclide provided in the ndl: {ndl.has('ZR96', 294)}")
```

```

Is ZR90 nuclide provided in the ndl: True
Is ZR91 nuclide provided in the ndl: True
Is ZR92 nuclide provided in the ndl: True
Is ZR94 nuclide provided in the ndl: True
Is ZR96 nuclide provided in the ndl: True
```

Then we define a dictionnary describing the decomposition of an element into its isotopes.

```ipython3
data_user = {
    "H": [("H1", 0.5), ("H2", 0.5)],
    "U": [("U234", 5.4e-05), ("U235", 0.007204), ("U238", 0.992742)],
    "FE": [("FE54", 0.05845), ("FE56", 0.91754), ("FE57", 0.02119), ("FE58", 0.00286)],
}

na_ud = tripoli5.materials.NaturalAbundances("User defined", data_user)

print(f"{na_ud.getElementNames()}")
```

```

['FE', 'U', 'H']
```

```ipython3
# build fer mixture using user defined natural abundances
natural_abundances = tripoli5.materials.NaturalAbundances(
    "User defined",
    {"Fe": [("FE54", 0.03841879), ("FE56", 0.9454551), ("FE57", 0.0161261)]},
)

fer_with_natural_abundance = (
    tripoli5.materials.MixtureBuilder("atom_fractions")
    .withName("FER_user")
    .withCatalog(catalog)
    .withTemperature(294 * K)
    .withDensity(5.883561 * gPerCm3)
    .withNaturalAbundances(natural_abundances)
    .add("Fe", 1.0)
    .build()
)
fer_with_natural_abundance.printSummary()
```

```

[2026-01-30 16:45:41.791] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/mass/njoy_ace/v0.2.0/archive/wrapped_mass_data.bin
[2026-01-30 16:45:41.797] [info] Mixture: FER_user
[2026-01-30 16:45:41.797] [info] Temperature field:  Temperature is: 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]

[2026-01-30 16:45:41.797] [info] === Owning mixture composition: ===
Number of IDs: 1
Number of nuclides: 3
IDs: FE54 FE56 FE57
0 0.0024362501275768376 0.05995412942451263 0.0010226041263224801
```

### Specifying Temperature and Density fields

With the purpose of being coupled to a thermal hydraulic code, temperature and densities can be defined using `MedCouplingField`s.

In this case, the temperature or the density of the material is not constant and is defined over a field. In case `Tripoli5` has been compiled with the `MEDCoupling` option, then the following classes are available:

- `tripoli5.materials.MedCouplingFieldTemperature`
- `tripoli5.materials.MedCouplingFieldDensity`

An instance of these classes can be used as arguments of `.withTemperatureField(...)` and `.withDensityField(...)` methods of MixtureBuilder.

#### An example of water mixture with a temperature field and a density field

Create a MEDCouplingField for water

```ipython3
import medcoupling

# create a 1D mesh in x axis
mesh_water = medcoupling.MEDCouplingCMesh.New("Water_Mesh")
mesh_water.setCoords(medcoupling.DataArrayDouble([-25.0, -15.0, -5.0, 5.0, 15.0, 25.0]))

# create a field with water temperature values on mesh
water_temperature_field = medcoupling.MEDCouplingFieldDouble(medcoupling.ON_CELLS)
water_temperature_field.setMesh(mesh_water)
water_temperature_field.setName("Temperature_field_Water")
water_temperature_field.setArray(
    medcoupling.DataArrayDouble([294, 600.0, 0.0, 900, 1200])
)

# create a field with water density values on mesh
d_ref_water = 1.00705
water_dens_values = [
    d_ref_water * 1.2,
    d_ref_water * 0.8,
    0.0,
    d_ref_water * 0.7,
    d_ref_water * 1.4,
]

water_density_field = medcoupling.MEDCouplingFieldDouble(medcoupling.ON_CELLS)
water_density_field.setMesh(mesh_water)
water_density_field.setName("Density_field_Water")
water_density_field.setArray(medcoupling.DataArrayDouble(water_dens_values))
```

Create a `tripoli5.materials.MedCouplingFieldTemperature` object and a `tripoli5.materials.MedCouplingFieldDensity` object

```ipython3
# create temperature & density field for MixtureBuilder
water_temp_field = tripoli5.materials.MedCouplingFieldTemperature(
    a_field=water_temperature_field, unit=Temperature.Units.K
)
water_dens_field = tripoli5.materials.MedCouplingFieldDensity(
    a_field=water_density_field, unit=Density.Units.gPerCm3
)
```

Create a water mixture with a field Temperature and a field Density.

Note that the methods `.withTemperature` and `.withTemperatureField` are mutually exclusive. You should use one or the other, but not both.

In contrast, the reference density using the `.withDensity` method is linked to the computation of the concentration of nuclides. Even when using `.withDensityField`, it is still required for the “atom_fractions” or “mass_fractions” methods and is optional for the “concentrations” method.

```ipython3
water = (
    tripoli5.materials.MixtureBuilder("atom_fractions")
    .withName("Water")
    .withCatalog(catalog)
    .withDensity(water_density)
    .withTemperatureField(water_temp_field)
    .withDensityField(water_dens_field)
    .add(nuclides, atom_fractions)
    .build()
)
water.printSummary()
```

```

[2026-01-30 16:45:41.890] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/mass/njoy_ace/v0.2.0/archive/wrapped_mass_data.bin
[2026-01-30 16:45:41.894] [warning] The sum of fractions for mixture Water differs from 1.0 by more than 1e-10. Sum: 1.0000001600000001. The fractions will be automatically renormalized.
[2026-01-30 16:45:41.894] [info] Mixture: Water
[2026-01-30 16:45:41.894] [info] Temperature field: The Temperature is a MEDCoupling Field with Units [K]; minimum = 0 [K], 0 [MeV], -273.15 [°C], maximum = 1200 [K], 1.034079888e-07 [MeV], 926.85 [°C]
MEDCouplingFieldDouble C++ instance at 0x156fd610. Name : "Temperature_field_Water".
Nature of field : NoNature.
P0 spatial discretization.

Mesh info : MEDCouplingCMesh C++ instance at 0x157b7a50. Name : "Water_Mesh".

Array info : DataArrayDouble C++ instance at 0x14e6a060. Number of tuples : 5. Number of components : 1.
[294, 600, 0, 900, 1200]

[2026-01-30 16:45:41.894] [info] === Owning mixture composition: ===
Number of IDs: 1
Number of nuclides: 4
IDs: H1 O16 B10 B11
0 0.0666799758046644 0.03336880562073827 0.00038262687894138404 0.00015401234804413502
```

#### An example of fuel mixture with a field temperature

Create a MEDCouplingField for the fuel temperature:

```ipython3
# create a 1D mesh in x axis
mesh_fuel = medcoupling.MEDCouplingCMesh.New("Fuel_Mesh")
mesh_fuel.setCoords(medcoupling.DataArrayDouble([-5.0, 0.0, 5.0]))

# create a field with water temperature values on mesh
fuel_temperature_field = medcoupling.MEDCouplingFieldDouble(medcoupling.ON_CELLS)
fuel_temperature_field.setMesh(mesh_fuel)
fuel_temperature_field.setName("Temperature_field_fuel")
fuel_temperature_field.setArray(medcoupling.DataArrayDouble([294.0, 1200.0]))
```

Create a `tripoli5.materials.MedCouplingFieldTemperature` object:

```ipython3
fuel_temp_field = tripoli5.materials.MedCouplingFieldTemperature(
    a_field=fuel_temperature_field, unit=Temperature.Units.K
)
```

```ipython3
uox_nuclides = ["U234", "U235", "U236", "U238", "O16"]
uox_atom_fractions = [0.000112438, 0.0125106, 1.00738e-06, 0.3205, 0.666876]

fuel = (
    tripoli5.materials.MixtureBuilder("atom_fractions")
    .withName("Fuel")
    .withCatalog(catalog)
    .withDensity(10.2731 * gPerCm3)
    .withTemperatureField(fuel_temp_field)
    .add(uox_nuclides, uox_atom_fractions)
    .build()
)
```

```

[2026-01-30 16:45:41.954] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/mass/njoy_ace/v0.2.0/archive/wrapped_mass_data.bin
[2026-01-30 16:45:41.960] [warning] The sum of fractions for mixture Fuel differs from 1.0 by more than 1e-10. Sum: 1.00000004538. The fractions will be automatically renormalized.
```
