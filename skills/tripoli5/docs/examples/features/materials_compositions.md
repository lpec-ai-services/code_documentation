<!-- source: https://tripoli5.asnr.dev/documentation/latest-release/examples/features/materials_compositions.html -->

# Overview of Material compositions and physics

This notebook provides a quick overview of how to build material compositions data and select collision physics parameters in TRIPOLI-5.

The composition (nuclides , temperature, concentrations, …) of a material is specified using the `mixtures` object.

Then the physics (e.g. URR treatment, Doppler broadening, energy lower bounds, …) is specified leading to the construction of a `NeutronMedia` object that gathers the material composition and the physics modeling choices. Both object are constructed using a `builder` pattern, respectively with the `tripoli5.materials.MixtureBuilder` and `tripoli5.materials.NeutronMediumBuilder` classes.

For a complete descriptions of the available options, you may refer to the [mixtures](mixtures.md) and [neutron_media](neutron_media.md) notebooks.

## Imports

First, let’s import TRIPOLI-5 modules and necessary classes.

```ipython3
import tripoli5
from tripoli5.core.literals import K, gPerCm3
```

## Catalog

The path to nuclear data needs to be specified through the `Catalog` class of the `tripoli5.delos` module. Either by using an environment variable: `T5_CATALOG_PATH`, or by directly setting a path.

```ipython3
catalog = tripoli5.delos.Catalog.fromFile(
    f"/opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/endfb8r0_mcnp_v{tripoli5.delos.CATALOG_VERSION}.yaml"
)
```

```

[2026-01-30 16:45:38.681] [info] Loading catalog from file: /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/endfb8r0_mcnp_v2.2.0.yaml
```

## Defining Mixtures

Material compositions can be defined using the `MixtureBuilder`. They can be defined by providing the amount of nuclides in terms of “concentrations”, “mass_fractions” or “atom_fractions”.

A temperature is selected for that material and a name is associated to this `mixture`. This name allows linking to the name defined in the geometry cell.

A catalog to nuclear data is required to access the nuclides’ mass in order to compute the material density or convert fractions into concentrations.

### Using concentrations

Below you will find an example of a fuel defined using nuclides’ concentrations.

```ipython3
fuel = (
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
fuel.printSummary()
```

```

[2026-01-30 16:45:38.718] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/mass/njoy_ace/v0.2.0/archive/wrapped_mass_data.bin
[2026-01-30 16:45:38.722] [info] Mixture: FUEL
[2026-01-30 16:45:38.722] [info] Temperature field:  Temperature is: 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]

[2026-01-30 16:45:38.722] [info] === Owning mixture composition: ===
Number of IDs: 1
Number of nuclides: 4
IDs: U234 U235 U236 U238
0 4.8416e-05 0.0048151 1.7407e-05 0.043181
```

### Using mass fractions

Build a water mixture using mass fractions. The `H1_H2O` indicates the use of Thermal Scattering Law of hydrogen in water.

Also note that adding nuclides can be provided nuclide-wise or as a list.

```ipython3
water_with_tsl = (
    tripoli5.materials.MixtureBuilder("mass_fractions")
    .withName("WATER")
    .withCatalog(catalog)
    .withDensity(1.00705 * gPerCm3)
    .withTemperature(294 * K)
    .add(["H1_H2O", "O16", "B10", "B11"], [0.11081, 0.880077, 0.00631736, 0.00279584])
    .build()
)
water_with_tsl.printSummary()
```

```

[2026-01-30 16:45:38.740] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/mass/njoy_ace/v0.2.0/archive/wrapped_mass_data.bin
[2026-01-30 16:45:38.744] [warning] The sum of fractions for mixture WATER differs from 1.0 by more than 1e-10. Sum: 1.0000002000000001. The fractions will be automatically renormalized.
[2026-01-30 16:45:38.744] [info] Mixture: WATER
[2026-01-30 16:45:38.744] [info] Temperature field:  Temperature is: 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]

[2026-01-30 16:45:38.744] [info] === Owning mixture composition: ===
Number of IDs: 1
Number of nuclides: 4
IDs: H1_H2O O16 B10 B11
0 0.06668003317991214 0.033368801742690156 0.00038262733669826906 0.00015401231365162515
```

### Using atom fractions and use of natural abundances

Build a clad mixture using atom fraction nuclides with a Zirconium Natural Abundance from NUBASE2020

```ipython3
clad = (
    tripoli5.materials.MixtureBuilder("atom_fractions")
    .withName("CLAD")
    .withCatalog(catalog)
    .withTemperature(294 * K)
    .withDensity(6.490 * gPerCm3)
    .withNaturalAbundances(tripoli5.materials.NaturalAbundances.fromNUBASE2020())
    .add("ZR", 0.5)
    .add("H1", 0.5)
    .build()
)
clad.printSummary()
```

```

[2026-01-30 16:45:38.766] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/mass/njoy_ace/v0.2.0/archive/wrapped_mass_data.bin
[2026-01-30 16:45:38.772] [info] Mixture: CLAD
[2026-01-30 16:45:38.772] [info] Temperature field:  Temperature is: 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]

[2026-01-30 16:45:38.772] [info] === Owning mixture composition: ===
Number of IDs: 1
Number of nuclides: 6
IDs: ZR90 ZR91 ZR92 ZR94 ZR96 H1
0 0.02180227609977075 0.0047545488404164785 0.007267425366590249 0.007364889380252975 0.0011865184271984078 0.04237565811422886
```

## Configure and Build a NeutronMedia

The `NeutronMediumBuilder` allows us selecting the physics (e.g. Doppler broadening, URR treatment, …). The media is built relying on the list of mixtures previsouly defined and a catalog which contains the location of the selected nuclear data library. The only mandatory parameters are the mixtures and the catalog provided through the `withMixtures` and `withCatalog` methods. Note also that the relevant nuclear data for the physics models are loading at this stage.

For a complete description of the options of the `NeutronMediumBuilder`, please refer to the [neutron_media](neutron_media.md) notebook.

Below you will find an example of using the default collision physics and turning on the Unresolved Resonance Range treatment using the CALENDF probability tables. The created media can then be passed to the simulation.

```ipython3
media = (
    tripoli5.materials.NeutronMediumBuilder()
    .withMixtures([fuel, clad, water_with_tsl])
    .withCatalog(catalog)
    .withURR(parameter="calendf")
    .build()
)
```

```

[2026-01-30 16:45:38.793] [info] Building B10 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-01-30 16:45:38.796] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/B10.294.bin
[2026-01-30 16:45:38.802] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-01-30 16:45:38.802] [info]   Building reaction MTs = 700, 51, 57, 58, 60, 59, 77, 79, 80, 56, 85, 78, 52, 81, 801, 800, 104, 102, 68, 601, 70, 600, 69, 602, 71, 53, 82, 604, 73, 83, 113, 54, 605, 74, 75, 76, 67, 66, 65, 64, 63, 62, 61, 2, 72, 603, 84, 55
[2026-01-30 16:45:38.802] [info] Building B11 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-01-30 16:45:38.805] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/B11.294.bin
[2026-01-30 16:45:38.810] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-01-30 16:45:38.810] [info]   Building reaction MTs = 60, 2, 59, 58, 91, 102, 57, 28, 54, 56, 52, 51, 22, 55, 103, 16, 107, 105, 53
[2026-01-30 16:45:38.810] [info] Building H1 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-01-30 16:45:38.812] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/H1.294.bin
[2026-01-30 16:45:38.816] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-01-30 16:45:38.816] [info]   Building reaction MTs = 102, 2
[2026-01-30 16:45:38.816] [info] Building H1_H2O at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-01-30 16:45:38.819] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/tsl/njoy_ace/v0.3.0/dir/H1_H2O.294.bin
[2026-01-30 16:45:38.858] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-01-30 16:45:38.858] [info]   Building reaction MTs = 102, 2
[2026-01-30 16:45:38.858] [info]   Building thermal collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-01-30 16:45:38.858] [info]   Building thermal reaction MTs = 1000000
[2026-01-30 16:45:38.858] [info] Building O16 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
… [38 lines of output omitted] …
[2026-01-30 16:45:39.207] [info] Building ZR94 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-01-30 16:45:39.210] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/ZR94.294.bin
[2026-01-30 16:45:39.227] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/urr/calendf/v0.2.0/dir/ZR94.294.urr.calendf.bin
[2026-01-30 16:45:39.240] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-01-30 16:45:39.240] [info]   Building reaction MTs = 825, 22, 24, 607, 17, 812, 104, 606, 16, 811, 28, 819, 57, 809, 822, 60, 821, 59, 649, 826, 32, 91, 608, 609, 829, 824, 62, 800, 801, 601, 837, 804, 817, 55, 803, 605, 816, 54, 808, 603, 839, 814, 52, 806, 604, 807, 602, 838, 805, 802, 102, 810, 827, 58, 820, 112, 53, 815, 849, 836, 600, 818, 56, 835, 834, 833, 832, 831, 5, 105, 51, 813, 830, 828, 2, 823, 61
[2026-01-30 16:45:39.240] [info] Building ZR96 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-01-30 16:45:39.243] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/ZR96.294.bin
[2026-01-30 16:45:39.258] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/urr/calendf/v0.2.0/dir/ZR96.294.urr.calendf.bin
[2026-01-30 16:45:39.272] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-01-30 16:45:39.272] [info]   Building reaction MTs = 801, 105, 807, 53, 24, 804, 601, 602, 805, 51, 22, 600, 803, 649, 802, 52, 806, 808, 54, 17, 104, 800, 849, 16, 5, 28, 2, 55, 809, 91, 102
```
