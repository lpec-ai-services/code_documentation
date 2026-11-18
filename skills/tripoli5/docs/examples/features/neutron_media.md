<!-- source: https://tripoli5.asnr.dev/documentation/latest-release/examples/features/neutron_media.html -->

# Neutron Media

The Neutron Media in TRIPOLI-5 contains all the nuclear data needed by compositions and collision physics models, which are necessary for performing a simulation.

In this notebook, we will demonstrate how to configure and build a Neutron Media object using the `tripoli5.materials.NeutronMediumBuilder` class. Once the `tripoli5.materials.NeutronMedia` object is built, it can be transmitted to the [simulation](simulation.md).

In order to build a Neutron Media object, the only two mandatory data are:

- A **catalog** indexing nuclear data paths (e.g. neutron data, thermal scattering laws, …).
- A list of [mixtures](mixtures.md) defining the material compositions.

Optionally, the user may configure through the builder several parameters of the particle physics modeling such as for instance a **lower bound energy cut**, a **reactions used in the transport**, or the method for handling the **Unresolved Resonance Range**

These options are set using the `NeutronMediumBuilder` class which allows for checking consistency of the various options and then build a neutron media object.

To configure the `NeutronMedia`, the `NeutronMediumBuilder` class needs to be instantiated with its constructor and can then be configured with the following methods:

**Mandatory Methods:**

- `withMixtures`: Specify the list of mixtures (material compositions).
- `withCatalog`: Specifies the nuclear data catalog.

**Optional Methods:**

- `withLowerEnergyCut`: Sets the simulation lower energy threshold.
- `withURR`: Selects the Unresolved Resonance Range options. Possible options are: “none”, “ace”, “calendf”.
- `withDopplerBroadening`: Choose the Doppler Broadening options for the free gas data. Possible methods are: “PreTabulated”, “Sigma1”.
- `withSigma1Scheduler`: Select the SIGMA1 GPU processing options.
- `withEpithermalBroadening`: Set the Epithermal Broadening options.
- `withOrigin`: Specifies the source of the nuclear data. Possible sources are: “Directory”, “Archive”.
- `withEnergyGridParameters`: Specify the energy grid parameters. Possible search types are: “BinarySearch”, “HashMap”.
- `withCollisionSampler`: Specify the sampling method for collisions. Possible sampling types are: “analog”, “implicit_capture”, “branchless”.
- `withTSLThreshold`: Specify the TSL energy threshold (for instance `4.95*eV`) for all nuclides. By default, the threshold is automatically taken from neutron thermal scattering data. The user defined threshold must be lower than the TSL nuclear data one.
- `withTemperatureInterpolationMethod`: Specify the temperature interpolation method. This method applies to free gas, thermal scattering and URR data in “PreTabulated” mode (see `withDopplerBroadening` option) and only to thermal scattering data in “Sigma1” mode. Thus, when applying “Sigma1” algorithm, this parameter will be unused if no thermal data are involved (note that the combination of “Sigma1” algorithm and URR treatment is not available yet). Possible methods are: “nearest”,
  “linear”, “sqrt”.

There are several methods for sampling the outgoing particles of a collision. Currently, one can choose between *analog sampling*, *nuclide-wise implicit capture* or *nuclide-wise branchless sampling*. The default is analog sampling; all reaction channels can be sampled and the reaction yield is used to determine the number of outgoing particles . In the following, we will depict in detail each option starting with building the “all-defaults” neutron media.

## Prerequisites: imports, Catalog and Mixtures

First, let’s import TRIPOLI-5 modules and necessary classes.

### Imports

```ipython3
import tripoli5
from tripoli5.core.literals import K, MeV, eV
```

### Catalog

The path to nuclear/mass data needs to be specified through the `tripoli5.delos` module.

Either by using an **environment variable**: `T5_CATALOG_PATH`, or by **specifying a file path directly**.

```ipython3
catalog = tripoli5.delos.Catalog.fromFile(
    f"/opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/endfb8r0_mcnp_v{tripoli5.delos.CATALOG_VERSION}.yaml"
)
```

```

[2026-04-10 13:24:00.439] [info] Loading catalog from file: /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/endfb8r0_mcnp_v2.2.0.yaml
```

### Mixtures

In order to create a neutron media, we first need to create [mixtures](mixtures.md), i.e., material compositions, using the `MixtureBuilder`.

```ipython3
reactor = (
    tripoli5.materials.MixtureBuilder("concentrations")
    .withName("reactor")
    .withCatalog(catalog)
    .withTemperature(294.0 * K)
    .add(
        ["U234", "U235", "U236", "U238"],
        [4.8416e-05, 4.8151e-03, 1.7407e-05, 4.3181e-02],
    )
    .build()
)

reflector = (
    tripoli5.materials.MixtureBuilder("concentrations")
    .withName("reflector")
    .withCatalog(catalog)
    .withTemperature(294.0 * K)
    .add(
        ["U234", "U235", "U236", "U238"],
        [2.8672e-07, 1.0058e-04, 1.1468e-06, 4.7677e-02],
    )
    .build()
)

mixtures = [reactor, reflector]
```

```

[2026-04-10 13:24:00.471] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/mass/njoy_ace/v0.2.0/archive/wrapped_mass_data.bin
[2026-04-10 13:24:00.476] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/mass/njoy_ace/v0.2.0/archive/wrapped_mass_data.bin
```

## Neutron Media with all default options

Defining a `NeutronMedia` with all default options, requiring only the mixtures and a catalog, is performed as below.

Note that building the media can be done either using a single liner or explicitely instantiating the builder and then building the media.

The two approaches are described here. For the rest of this notebook, only the first version will be used.

```ipython3
# one liner syntax
media = (
    tripoli5.materials.NeutronMediumBuilder()
    .withMixtures(mixtures)
    .withCatalog(catalog)
    .build()
)

# explicitely instantiating the builder
builder = tripoli5.materials.NeutronMediumBuilder()
builder.withMixtures(mixtures)
builder.withCatalog(catalog)
media = builder.build()
```

```

[2026-04-10 13:24:00.491] [info] Building U234 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-04-10 13:24:00.495] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U234.294.bin
[2026-04-10 13:24:00.510] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/urr/njoy_ace/v0.4.0/dir/U234.294.urr.ace.bin
[2026-04-10 13:24:00.515] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-04-10 13:24:00.516] [info]   Building reaction MTs = 20, 79, 21, 80, 66, 37, 51, 70, 71, 72, 74, 77, 73, 102, 89, 91, 67, 38, 90, 88, 87, 57, 86, 58, 54, 83, 60, 2, 61, 62, 63, 64, 65, 55, 84, 68, 56, 85, 69, 59, 53, 82, 16, 75, 17, 76, 19, 78, 81, 52
[2026-04-10 13:24:00.517] [info] Building U235 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-04-10 13:24:00.520] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U235.294.bin
[2026-04-10 13:24:00.583] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/urr/njoy_ace/v0.4.0/dir/U235.294.urr.ace.bin
[2026-04-10 13:24:00.586] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-04-10 13:24:00.587] [info]   Building reaction MTs = 814, 52, 813, 51, 818, 56, 76, 17, 817, 55, 75, 16, 77, 18, 816, 54, 72, 834, 815, 53, 822, 60, 821, 59, 5, 74, 82, 83, 84, 85, 86, 87, 81, 806, 91, 80, 805, 79, 804, 68, 830, 835, 73, 102, 810, 2, 89, 78, 803, 88, 802, 801, 800, 63, 825, 64, 826, 649, 65, 827, 828, 66, 67, 829, 61, 823, 831, 69, 812, 833, 71, 811, 62, 824, 832, 70, 809, 808, 807, 58, 820, 57, 819
[2026-04-10 13:24:00.587] [info] Building U236 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-04-10 13:24:00.589] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U236.294.bin
[2026-04-10 13:24:00.601] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/urr/njoy_ace/v0.4.0/dir/U236.294.urr.ace.bin
[2026-04-10 13:24:00.604] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-04-10 13:24:00.605] [info]   Building reaction MTs = 20, 79, 21, 80, 66, 37, 51, 70, 71, 72, 74, 77, 73, 102, 89, 91, 67, 38, 90, 88, 87, 57, 86, 58, 54, 83, 60, 2, 61, 62, 63, 64, 65, 55, 84, 68, 56, 85, 69, 59, 53, 82, 16, 75, 17, 76, 19, 78, 81, 52
[2026-04-10 13:24:00.606] [info] Building U238 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-04-10 13:24:00.608] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U238.294.bin
[2026-04-10 13:24:00.668] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/urr/njoy_ace/v0.4.0/dir/U238.294.urr.ace.bin
[2026-04-10 13:24:00.671] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-04-10 13:24:00.672] [info]   Building reaction MTs = 77, 18, 76, 17, 79, 51, 80, 52, 81, 82, 75, 16, 800, 56, 85, 78, 74, 73, 102, 62, 91, 65, 66, 61, 2, 60, 89, 67, 68, 69, 64, 5, 63, 70, 58, 87, 71, 57, 86, 649, 59, 88, 53, 72, 54, 83, 84, 55
[2026-04-10 13:24:00.674] [info] Building U234 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-04-10 13:24:00.675] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U234.294.bin
[2026-04-10 13:24:00.687] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/urr/njoy_ace/v0.4.0/dir/U234.294.urr.ace.bin
[2026-04-10 13:24:00.690] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-04-10 13:24:00.691] [info]   Building reaction MTs = 20, 79, 21, 80, 66, 37, 51, 70, 71, 72, 74, 77, 73, 102, 89, 91, 67, 38, 90, 88, 87, 57, 86, 58, 54, 83, 60, 2, 61, 62, 63, 64, 65, 55, 84, 68, 56, 85, 69, 59, 53, 82, 16, 75, 17, 76, 19, 78, 81, 52
[2026-04-10 13:24:00.692] [info] Building U235 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-04-10 13:24:00.694] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U235.294.bin
[2026-04-10 13:24:00.750] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/urr/njoy_ace/v0.4.0/dir/U235.294.urr.ace.bin
[2026-04-10 13:24:00.754] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-04-10 13:24:00.755] [info]   Building reaction MTs = 814, 52, 813, 51, 818, 56, 76, 17, 817, 55, 75, 16, 77, 18, 816, 54, 72, 834, 815, 53, 822, 60, 821, 59, 5, 74, 82, 83, 84, 85, 86, 87, 81, 806, 91, 80, 805, 79, 804, 68, 830, 835, 73, 102, 810, 2, 89, 78, 803, 88, 802, 801, 800, 63, 825, 64, 826, 649, 65, 827, 828, 66, 67, 829, 61, 823, 831, 69, 812, 833, 71, 811, 62, 824, 832, 70, 809, 808, 807, 58, 820, 57, 819
[2026-04-10 13:24:00.755] [info] Building U236 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-04-10 13:24:00.757] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U236.294.bin
[2026-04-10 13:24:00.767] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/urr/njoy_ace/v0.4.0/dir/U236.294.urr.ace.bin
[2026-04-10 13:24:00.771] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-04-10 13:24:00.771] [info]   Building reaction MTs = 20, 79, 21, 80, 66, 37, 51, 70, 71, 72, 74, 77, 73, 102, 89, 91, 67, 38, 90, 88, 87, 57, 86, 58, 54, 83, 60, 2, 61, 62, 63, 64, 65, 55, 84, 68, 56, 85, 69, 59, 53, 82, 16, 75, 17, 76, 19, 78, 81, 52
[2026-04-10 13:24:00.772] [info] Building U238 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-04-10 13:24:00.774] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U238.294.bin
[2026-04-10 13:24:00.834] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/urr/njoy_ace/v0.4.0/dir/U238.294.urr.ace.bin
[2026-04-10 13:24:00.837] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-04-10 13:24:00.838] [info]   Building reaction MTs = 77, 18, 76, 17, 79, 51, 80, 52, 81, 82, 75, 16, 800, 56, 85, 78, 74, 73, 102, 62, 91, 65, 66, 61, 2, 60, 89, 67, 68, 69, 64, 5, 63, 70, 58, 87, 71, 57, 86, 649, 59, 88, 53, 72, 54, 83, 84, 55
```

## Lower energy threshold

The lower energy limit of the simulation can be set as below taking as argument an `Energy` value. The default value is \(1.0 10^{-11}\) MeV.

```ipython3
media = (
    tripoli5.materials.NeutronMediumBuilder()
    .withMixtures(mixtures)
    .withCatalog(catalog)
    .withLowerEnergyCut(lower_bound=1.0e-5 * MeV)
    .build()
)
```

```

[2026-04-10 13:24:00.859] [info] Building U234 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-04-10 13:24:00.862] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U234.294.bin
[2026-04-10 13:24:00.872] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/urr/njoy_ace/v0.4.0/dir/U234.294.urr.ace.bin
[2026-04-10 13:24:00.876] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-04-10 13:24:00.877] [info]   Building reaction MTs = 20, 79, 21, 80, 66, 37, 51, 70, 71, 72, 74, 77, 73, 102, 89, 91, 67, 38, 90, 88, 87, 57, 86, 58, 54, 83, 60, 2, 61, 62, 63, 64, 65, 55, 84, 68, 56, 85, 69, 59, 53, 82, 16, 75, 17, 76, 19, 78, 81, 52
[2026-04-10 13:24:00.878] [info] Building U235 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-04-10 13:24:00.880] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U235.294.bin
[2026-04-10 13:24:00.911] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/urr/njoy_ace/v0.4.0/dir/U235.294.urr.ace.bin
[2026-04-10 13:24:00.914] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-04-10 13:24:00.915] [info]   Building reaction MTs = 814, 52, 813, 51, 818, 56, 76, 17, 817, 55, 75, 16, 77, 18, 816, 54, 72, 834, 815, 53, 822, 60, 821, 59, 5, 74, 82, 83, 84, 85, 86, 87, 81, 806, 91, 80, 805, 79, 804, 68, 830, 835, 73, 102, 810, 2, 89, 78, 803, 88, 802, 801, 800, 63, 825, 64, 826, 649, 65, 827, 828, 66, 67, 829, 61, 823, 831, 69, 812, 833, 71, 811, 62, 824, 832, 70, 809, 808, 807, 58, 820, 57, 819
[2026-04-10 13:24:00.916] [info] Building U236 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-04-10 13:24:00.918] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U236.294.bin
[2026-04-10 13:24:00.926] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/urr/njoy_ace/v0.4.0/dir/U236.294.urr.ace.bin
[2026-04-10 13:24:00.929] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-04-10 13:24:00.930] [info]   Building reaction MTs = 20, 79, 21, 80, 66, 37, 51, 70, 71, 72, 74, 77, 73, 102, 89, 91, 67, 38, 90, 88, 87, 57, 86, 58, 54, 83, 60, 2, 61, 62, 63, 64, 65, 55, 84, 68, 56, 85, 69, 59, 53, 82, 16, 75, 17, 76, 19, 78, 81, 52
[2026-04-10 13:24:00.931] [info] Building U238 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-04-10 13:24:00.933] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U238.294.bin
[2026-04-10 13:24:00.982] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/urr/njoy_ace/v0.4.0/dir/U238.294.urr.ace.bin
[2026-04-10 13:24:00.986] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-04-10 13:24:00.987] [info]   Building reaction MTs = 77, 18, 76, 17, 79, 51, 80, 52, 81, 82, 75, 16, 800, 56, 85, 78, 74, 73, 102, 62, 91, 65, 66, 61, 2, 60, 89, 67, 68, 69, 64, 5, 63, 70, 58, 87, 71, 57, 86, 649, 59, 88, 53, 72, 54, 83, 84, 55
```

## Unresolved Resonance Range treatment

The Unresolved Resonance Range (URR) refers to the energy region where the resonance structure of a nuclide is too complex to be resolved individually. In this region, statistical methods are used to describe the average behavior of the resonances.

Three options are available for treating the unresolved resonance range, specified with the `withURRParameters` method.

- `"none"`: No treatment for the URR.
- `"ace"`: probability tables from ACE formatted files (usually processed using [NJOY](https://github.com/njoy)’s module PURR). This is the default behavior.
- `"calendf"`: probability tables processed with the [CALENDF](https://www.oecd-nea.org/tools/abstract/detail/nea-1278/) software.

To select the *CALENDF* treatment for the URR, you can use the following code:

```ipython3
media = (
    tripoli5.materials.NeutronMediumBuilder()
    .withMixtures(mixtures)
    .withCatalog(catalog)
    .withURR(
        parameter="calendf"
    )  # here "none", "ace" or "calendf" may be used as parameter
    .build()
)
```

```

[2026-04-10 13:24:01.007] [info] Building U234 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-04-10 13:24:01.010] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U234.294.bin
[2026-04-10 13:24:01.019] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/urr/calendf/v0.2.0/dir/U234.294.urr.calendf.bin
[2026-04-10 13:24:01.024] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-04-10 13:24:01.026] [info]   Building reaction MTs = 20, 79, 21, 80, 66, 37, 51, 70, 71, 72, 74, 77, 73, 102, 89, 91, 67, 38, 90, 88, 87, 57, 86, 58, 54, 83, 60, 2, 61, 62, 63, 64, 65, 55, 84, 68, 56, 85, 69, 59, 53, 82, 16, 75, 17, 76, 19, 78, 81, 52
[2026-04-10 13:24:01.026] [info] Building U235 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-04-10 13:24:01.028] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U235.294.bin
[2026-04-10 13:24:01.056] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/urr/calendf/v0.2.0/dir/U235.294.urr.calendf.bin
[2026-04-10 13:24:01.061] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-04-10 13:24:01.062] [info]   Building reaction MTs = 814, 52, 813, 51, 818, 56, 76, 17, 817, 55, 75, 16, 77, 18, 816, 54, 72, 834, 815, 53, 822, 60, 821, 59, 5, 74, 82, 83, 84, 85, 86, 87, 81, 806, 91, 80, 805, 79, 804, 68, 830, 835, 73, 102, 810, 2, 89, 78, 803, 88, 802, 801, 800, 63, 825, 64, 826, 649, 65, 827, 828, 66, 67, 829, 61, 823, 831, 69, 812, 833, 71, 811, 62, 824, 832, 70, 809, 808, 807, 58, 820, 57, 819
[2026-04-10 13:24:01.063] [info] Building U236 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-04-10 13:24:01.065] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U236.294.bin
[2026-04-10 13:24:01.074] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/urr/calendf/v0.2.0/dir/U236.294.urr.calendf.bin
[2026-04-10 13:24:01.080] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-04-10 13:24:01.081] [info]   Building reaction MTs = 20, 79, 21, 80, 66, 37, 51, 70, 71, 72, 74, 77, 73, 102, 89, 91, 67, 38, 90, 88, 87, 57, 86, 58, 54, 83, 60, 2, 61, 62, 63, 64, 65, 55, 84, 68, 56, 85, 69, 59, 53, 82, 16, 75, 17, 76, 19, 78, 81, 52
[2026-04-10 13:24:01.082] [info] Building U238 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-04-10 13:24:01.084] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U238.294.bin
[2026-04-10 13:24:01.138] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/urr/calendf/v0.2.0/dir/U238.294.urr.calendf.bin
[2026-04-10 13:24:01.143] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-04-10 13:24:01.144] [info]   Building reaction MTs = 77, 18, 76, 17, 79, 51, 80, 52, 81, 82, 75, 16, 800, 56, 85, 78, 74, 73, 102, 62, 91, 65, 66, 61, 2, 60, 89, 67, 68, 69, 64, 5, 63, 70, 58, 87, 71, 57, 86, 649, 59, 88, 53, 72, 54, 83, 84, 55
```

## Doppler Broadening of freegas cross section

Cross sections at a given temperature are usually computed before calculation by an external preprocessing of nuclear data software. Cross sections are tabulated at several specific temperature. When the desired temperature is not available or if lots of temperature are required, it may be inconvenient/unfeasable to process tabulated cross section for every required temperatures. In order to circumvent this issue, TRIPOLI-5 allows the use of an on-the-fly Doppler Broadening of cross sections.
Currently, this is achieved using the SIGMA1 algorithm using tabulated cross section at a specific **base** temperature.

**Warning:** Note that the SIGMA1 algorithm applies only to freegas cross sections. **Currently**, it cannot be applied with a specific URR treatment. However, we can combine SIGMA1 algorithm and stochastic interpolation for the thermal scattering data.

This option can be selected using the `withDopplerBroadening` method with the following parameters:

- Doppler Broadening Method: `"PreTabulated"` (default) / `"Sigma1"`
- Base Temperature: Optionnal with the SIGMA1 method (Default is \(0.0 K\))
- Doppler Threshold: Optionnal with the SIGMA1 method (Default is \(1.0 MeV\))

Below is a syntax example of turning on the SIGMA1 Doppler Broadening:

```ipython3
media = (
    tripoli5.materials.NeutronMediumBuilder()
    .withMixtures(mixtures)
    .withCatalog(catalog)
    .withDopplerBroadening(
        doppler_broadening_method="Sigma1",
        base_temperature=294.0 * K,
        max_energy=20.0e-3 * MeV,
    )
    .withURR("none")  # URR is not compatible with Sigma1
    .build()
)

# below is the pretabulated version which is equivalent to NOT specify the Doppler Broadening option
media = (
    tripoli5.materials.NeutronMediumBuilder()
    .withMixtures(mixtures)
    .withCatalog(catalog)
    .withDopplerBroadening("PreTabulated")
    .build()
)
```

```

[2026-04-10 13:24:01.164] [info] Building U234 for SIGMA1 Doppler broadening
[2026-04-10 13:24:01.166] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U234.294.bin
[2026-04-10 13:24:01.175] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-04-10 13:24:01.177] [info]   Building reaction MTs = 20, 79, 21, 80, 66, 37, 51, 70, 71, 72, 74, 77, 73, 102, 89, 91, 67, 38, 90, 88, 87, 57, 86, 58, 54, 83, 60, 2, 61, 62, 63, 64, 65, 55, 84, 68, 56, 85, 69, 59, 53, 82, 16, 75, 17, 76, 19, 78, 81, 52
[2026-04-10 13:24:01.178] [info] Building U235 for SIGMA1 Doppler broadening
[2026-04-10 13:24:01.181] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U235.294.bin
[2026-04-10 13:24:01.217] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-04-10 13:24:01.219] [info]   Building reaction MTs = 814, 52, 813, 51, 818, 56, 76, 17, 817, 55, 75, 16, 77, 18, 816, 54, 72, 834, 815, 53, 822, 60, 821, 59, 5, 74, 82, 83, 84, 85, 86, 87, 81, 806, 91, 80, 805, 79, 804, 68, 830, 835, 73, 102, 810, 2, 89, 78, 803, 88, 802, 801, 800, 63, 825, 64, 826, 649, 65, 827, 828, 66, 67, 829, 61, 823, 831, 69, 812, 833, 71, 811, 62, 824, 832, 70, 809, 808, 807, 58, 820, 57, 819
[2026-04-10 13:24:01.220] [info] Building U236 for SIGMA1 Doppler broadening
[2026-04-10 13:24:01.221] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U236.294.bin
[2026-04-10 13:24:01.228] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-04-10 13:24:01.229] [info]   Building reaction MTs = 20, 79, 21, 80, 66, 37, 51, 70, 71, 72, 74, 77, 73, 102, 89, 91, 67, 38, 90, 88, 87, 57, 86, 58, 54, 83, 60, 2, 61, 62, 63, 64, 65, 55, 84, 68, 56, 85, 69, 59, 53, 82, 16, 75, 17, 76, 19, 78, 81, 52
[2026-04-10 13:24:01.230] [info] Building U238 for SIGMA1 Doppler broadening
[2026-04-10 13:24:01.232] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U238.294.bin
[2026-04-10 13:24:01.265] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-04-10 13:24:01.266] [info]   Building reaction MTs = 77, 18, 76, 17, 79, 51, 80, 52, 81, 82, 75, 16, 800, 56, 85, 78, 74, 73, 102, 62, 91, 65, 66, 61, 2, 60, 89, 67, 68, 69, 64, 5, 63, 70, 58, 87, 71, 57, 86, 649, 59, 88, 53, 72, 54, 83, 84, 55
[2026-04-10 13:24:01.282] [info] Building U234 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-04-10 13:24:01.284] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U234.294.bin
[2026-04-10 13:24:01.294] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/urr/njoy_ace/v0.4.0/dir/U234.294.urr.ace.bin
[2026-04-10 13:24:01.297] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-04-10 13:24:01.298] [info]   Building reaction MTs = 20, 79, 21, 80, 66, 37, 51, 70, 71, 72, 74, 77, 73, 102, 89, 91, 67, 38, 90, 88, 87, 57, 86, 58, 54, 83, 60, 2, 61, 62, 63, 64, 65, 55, 84, 68, 56, 85, 69, 59, 53, 82, 16, 75, 17, 76, 19, 78, 81, 52
[2026-04-10 13:24:01.299] [info] Building U235 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-04-10 13:24:01.301] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U235.294.bin
[2026-04-10 13:24:01.331] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/urr/njoy_ace/v0.4.0/dir/U235.294.urr.ace.bin
[2026-04-10 13:24:01.334] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-04-10 13:24:01.335] [info]   Building reaction MTs = 814, 52, 813, 51, 818, 56, 76, 17, 817, 55, 75, 16, 77, 18, 816, 54, 72, 834, 815, 53, 822, 60, 821, 59, 5, 74, 82, 83, 84, 85, 86, 87, 81, 806, 91, 80, 805, 79, 804, 68, 830, 835, 73, 102, 810, 2, 89, 78, 803, 88, 802, 801, 800, 63, 825, 64, 826, 649, 65, 827, 828, 66, 67, 829, 61, 823, 831, 69, 812, 833, 71, 811, 62, 824, 832, 70, 809, 808, 807, 58, 820, 57, 819
[2026-04-10 13:24:01.336] [info] Building U236 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-04-10 13:24:01.338] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U236.294.bin
[2026-04-10 13:24:01.346] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/urr/njoy_ace/v0.4.0/dir/U236.294.urr.ace.bin
[2026-04-10 13:24:01.349] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-04-10 13:24:01.350] [info]   Building reaction MTs = 20, 79, 21, 80, 66, 37, 51, 70, 71, 72, 74, 77, 73, 102, 89, 91, 67, 38, 90, 88, 87, 57, 86, 58, 54, 83, 60, 2, 61, 62, 63, 64, 65, 55, 84, 68, 56, 85, 69, 59, 53, 82, 16, 75, 17, 76, 19, 78, 81, 52
[2026-04-10 13:24:01.351] [info] Building U238 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-04-10 13:24:01.352] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U238.294.bin
[2026-04-10 13:24:01.385] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/urr/njoy_ace/v0.4.0/dir/U238.294.urr.ace.bin
[2026-04-10 13:24:01.389] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-04-10 13:24:01.390] [info]   Building reaction MTs = 77, 18, 76, 17, 79, 51, 80, 52, 81, 82, 75, 16, 800, 56, 85, 78, 74, 73, 102, 62, 91, 65, 66, 61, 2, 60, 89, 67, 68, 69, 64, 5, 63, 70, 58, 87, 71, 57, 86, 649, 59, 88, 53, 72, 54, 83, 84, 55
```

### GPU processing of the SIGMA1 algorithm

Due to its intensive computation effort, the SIGMA1 algorithm is a good candidate to be ported on GPU.

To that end, can set some parallelization options for Sigma1 cross-section computation using the `withSigma1Scheduler` method. By **default**, if this method is not called, there is **no GPU parallelization for Sigma1**.

The `withSigma1Scheduler` method argument is a `tripoli5.materials.Sigma1SchedulerOptions` object containing all parameters regarding the GPU ported version of the SIGMA1. The arguments for the `tripoli5.materials.Sigma1SchedulerOptions` object are:

- **target**: Specifies the target platform for parallelization. Options include:

  ```none
  - `"None"`: No parallelization.
  - `"Host"`: Parallelization on the host CPU.
  - `"Cuda"`: Parallelization using NVIDIA CUDA.
  - `"OpenACC"`: Parallelization using OpenACC.
  ```
- **nb_threads**: The number of threads that is used for parallelization. Note that this number of threads **must be equal to the number of threads set in the simulation parameters**.
- **gpu_rate**: The rate at which GPU resources are utilized. If `gpu_rate`\(<1\), part of the SIGMA1 tasks are then executed on the CPU. This is a value between 0 and 1, where 0 means no GPU usage, 1 means full GPU usage, 0.5 means that as many SIGMA1 calculations are done on CPU as on the GPU. Note that it is better to reduce the `gpu_rate` for slow GPUs (and use 1.0 for fast GPUs).
- **offload_size**: The number of Sigma1 computation tasks to be offloaded to the GPU for processing at the same time. A computation task is a triplet consisting of a nuclide, energy particle, and material temperature. The optimal value for this parameter depends on the device (GPU model) on which the calculation is performed. For example for a Nvidia RTX A5000, the optimal value seems to be around 1000. After the `gpu_rate`, this may be the parameter to which GPU performance is the more
  sensitive.
- **policy**: The scheduling policy for parallelization. Options include:

  ```none
  - `"Static"`: Static scheduling, where tasks are evenly distributed among threads.
  - `"Dynamic"`: Dynamic scheduling, where tasks are dynamically assigned to threads as they become available.
  ```

Another parameter that interracts with `offload_size`, and may affect the performance of the SIGMA1 computation on GPU is the `schedule_size` that is set in the `SimulationParameters`. This parameter sets the number of particles to follow in an event based manner, and thus also affects the number of SIGMA1 tasks that can be offloaded to GPU. For example, in a given medium, the larger the `schedule_size`, the “quicker” the SIGMA1 tasks buffer will be filled. For a substantial number of
nuclides, having a `schedule_size` that is too large could negatively impact performance. Optimal settings depend on the problem that is modeled (number of nuclide) and the hardware that is used for the calculation, but a simple rule of thumb would be to have `offload_size` \(\approx\) `schedule_size` \(\times\) `nubmer of nuclides`.

In the example below, the Sigma1 scheduler is configured to use CUDA for parallelization with 20 threads, a GPU rate of 0.95, an offload size of 1000 computation tasks and a dynamic scheduling policy.

```ipython3
opts = tripoli5.materials.Sigma1SchedulerOptions(
    target="Cuda",
    nb_threads=20,
    gpu_rate=0.95,
    offload_size=1000,
    policy="Dynamic",
)

media = (
    tripoli5.materials.NeutronMediumBuilder()
    .withMixtures(mixtures)
    .withCatalog(catalog)
    .withDopplerBroadening(
        doppler_broadening_method="Sigma1",
        base_temperature=294.0 * K,
        max_energy=20.0e-3 * MeV,
    )
    .withURR("none")  # URR is not compatible with Sigma1
    .withSigma1Scheduler(opts)
    .build()
)
```

```

[2026-04-10 13:24:01.409] [info] Building U234 for SIGMA1 Doppler broadening
[2026-04-10 13:24:01.412] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U234.294.bin
[2026-04-10 13:24:01.420] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-04-10 13:24:01.421] [info]   Building reaction MTs = 20, 79, 21, 80, 66, 37, 51, 70, 71, 72, 74, 77, 73, 102, 89, 91, 67, 38, 90, 88, 87, 57, 86, 58, 54, 83, 60, 2, 61, 62, 63, 64, 65, 55, 84, 68, 56, 85, 69, 59, 53, 82, 16, 75, 17, 76, 19, 78, 81, 52
[2026-04-10 13:24:01.422] [info] Building U235 for SIGMA1 Doppler broadening
[2026-04-10 13:24:01.424] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U235.294.bin
[2026-04-10 13:24:01.455] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-04-10 13:24:01.456] [info]   Building reaction MTs = 814, 52, 813, 51, 818, 56, 76, 17, 817, 55, 75, 16, 77, 18, 816, 54, 72, 834, 815, 53, 822, 60, 821, 59, 5, 74, 82, 83, 84, 85, 86, 87, 81, 806, 91, 80, 805, 79, 804, 68, 830, 835, 73, 102, 810, 2, 89, 78, 803, 88, 802, 801, 800, 63, 825, 64, 826, 649, 65, 827, 828, 66, 67, 829, 61, 823, 831, 69, 812, 833, 71, 811, 62, 824, 832, 70, 809, 808, 807, 58, 820, 57, 819
[2026-04-10 13:24:01.457] [info] Building U236 for SIGMA1 Doppler broadening
[2026-04-10 13:24:01.459] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U236.294.bin
[2026-04-10 13:24:01.465] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-04-10 13:24:01.467] [info]   Building reaction MTs = 20, 79, 21, 80, 66, 37, 51, 70, 71, 72, 74, 77, 73, 102, 89, 91, 67, 38, 90, 88, 87, 57, 86, 58, 54, 83, 60, 2, 61, 62, 63, 64, 65, 55, 84, 68, 56, 85, 69, 59, 53, 82, 16, 75, 17, 76, 19, 78, 81, 52
[2026-04-10 13:24:01.468] [info] Building U238 for SIGMA1 Doppler broadening
[2026-04-10 13:24:01.469] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U238.294.bin
[2026-04-10 13:24:01.500] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-04-10 13:24:01.502] [info]   Building reaction MTs = 77, 18, 76, 17, 79, 51, 80, 52, 81, 82, 75, 16, 800, 56, 85, 78, 74, 73, 102, 62, 91, 65, 66, 61, 2, 60, 89, 67, 68, 69, 64, 5, 63, 70, 58, 87, 71, 57, 86, 649, 59, 88, 53, 72, 54, 83, 84, 55
```

## Epithermal broadening of the elastic scattering kernel

In neutron interactions with matter, relative velocity effects between the incident neutron and the collided nucleus at thermal equilibrium must be considered. The thermal agitation of nuclei results in Doppler-broadened cross sections and scattering kernels. In this section, we described the options for handling the scattering kernels.

Two models are available for taking into account the Doppler broadening of elastic scattering kernels:

- the Sampling of the Velocity of the Target nucleus (SVT)
- the Doppler Broadening Rejection Correction (DBRC)

These methods can be applied to all nuclides or to a subset of nuclides. The SVT model is valid for light nuclei but breaks down for heavy resonant nuclei like \(^{235}U\). For such nuclei, the DBRC model is recommended.

The selection of the method and its parameters is performed using the `withEpithermalBroadening` method. This method takes as an argument an `EpithermalBroadeningParameters` object defined below.

The option selection mechanism is quite flexible and allow mixing models according to the energy range for each nuclide. This flexibility comes at a cost of complexity when defining these options though the use of a `NuclideSelector`. Thus, we chose, for this notebook, to expose the most common use cases before moving to a complete description of the available options.

### Default options

The default model in TRIPOLI-5 for Doppler broadening of elastic scattering kernels is the SVT (Sampling of the Velocity of the Target nucleus) model. This model assumes nuclei are at thermal equilibrium with a Maxwell-Boltzmann velocity distribution and derives scattered neutron parameters from two-body kinematics.

TRIPOLI-5 uses the SVT model in the region from \(10^{−5}\) eV to an upper threshold energy \(E_\mathrm{threshold} = 400k_BT\), where \(k_B = 8.617\times10^{-5}\) [eV/K] is the Boltzmann constant, and \(T\) is the medium temperature. Above \(E_\mathrm{threshold}\), the asymptotic scattering kernel is used.

The only exception is \(^{1}H\) for which we apply the SVT model on the energy range from \(10^{−5}\) eV to the upper limit of the simulation (usually 20 MeV).

If thermal scattering laws are available in the thermal region (typically between \(10^{−5}\) eV and \(E_\mathrm{therm}\), with \(E_\mathrm{therm}\) around 5 eV), TRIPOLI-5 uses these thermal sections up to \(E_\mathrm{therm}\). Above \(E_\mathrm{therm}\), it chooses the SVT or the asymptotic elastic kernel, based on whether the incident neutron energy is below or above \(E_\mathrm{threshold}\), respectively.

Although not required, one can explicitely specify the default Epithermal Doppler broadening treatment with the static method `EpithermalBroadeningParameters.defaultParams()` class.

```ipython3
default_params = tripoli5.materials.EpithermalBroadeningParameters.defaultParams()
media = (
    tripoli5.materials.NeutronMediumBuilder()
    .withMixtures(mixtures)
    .withCatalog(catalog)
    .withEpithermalBroadening(default_params)
    .build()
)

# which is equivalent to specifying nothing
media = (
    tripoli5.materials.NeutronMediumBuilder()
    .withMixtures(mixtures)
    .withCatalog(catalog)
    .build()
)
```

```

[2026-04-10 13:24:01.522] [info] Building U234 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-04-10 13:24:01.525] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U234.294.bin
[2026-04-10 13:24:01.535] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/urr/njoy_ace/v0.4.0/dir/U234.294.urr.ace.bin
[2026-04-10 13:24:01.539] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-04-10 13:24:01.540] [info]   Building reaction MTs = 20, 79, 21, 80, 66, 37, 51, 70, 71, 72, 74, 77, 73, 102, 89, 91, 67, 38, 90, 88, 87, 57, 86, 58, 54, 83, 60, 2, 61, 62, 63, 64, 65, 55, 84, 68, 56, 85, 69, 59, 53, 82, 16, 75, 17, 76, 19, 78, 81, 52
[2026-04-10 13:24:01.541] [info] Building U235 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-04-10 13:24:01.543] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U235.294.bin
[2026-04-10 13:24:01.574] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/urr/njoy_ace/v0.4.0/dir/U235.294.urr.ace.bin
[2026-04-10 13:24:01.578] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-04-10 13:24:01.579] [info]   Building reaction MTs = 814, 52, 813, 51, 818, 56, 76, 17, 817, 55, 75, 16, 77, 18, 816, 54, 72, 834, 815, 53, 822, 60, 821, 59, 5, 74, 82, 83, 84, 85, 86, 87, 81, 806, 91, 80, 805, 79, 804, 68, 830, 835, 73, 102, 810, 2, 89, 78, 803, 88, 802, 801, 800, 63, 825, 64, 826, 649, 65, 827, 828, 66, 67, 829, 61, 823, 831, 69, 812, 833, 71, 811, 62, 824, 832, 70, 809, 808, 807, 58, 820, 57, 819
[2026-04-10 13:24:01.580] [info] Building U236 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-04-10 13:24:01.581] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U236.294.bin
[2026-04-10 13:24:01.590] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/urr/njoy_ace/v0.4.0/dir/U236.294.urr.ace.bin
[2026-04-10 13:24:01.594] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-04-10 13:24:01.595] [info]   Building reaction MTs = 20, 79, 21, 80, 66, 37, 51, 70, 71, 72, 74, 77, 73, 102, 89, 91, 67, 38, 90, 88, 87, 57, 86, 58, 54, 83, 60, 2, 61, 62, 63, 64, 65, 55, 84, 68, 56, 85, 69, 59, 53, 82, 16, 75, 17, 76, 19, 78, 81, 52
[2026-04-10 13:24:01.596] [info] Building U238 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-04-10 13:24:01.600] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U238.294.bin
[2026-04-10 13:24:01.664] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/urr/njoy_ace/v0.4.0/dir/U238.294.urr.ace.bin
[2026-04-10 13:24:01.670] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-04-10 13:24:01.671] [info]   Building reaction MTs = 77, 18, 76, 17, 79, 51, 80, 52, 81, 82, 75, 16, 800, 56, 85, 78, 74, 73, 102, 62, 91, 65, 66, 61, 2, 60, 89, 67, 68, 69, 64, 5, 63, 70, 58, 87, 71, 57, 86, 649, 59, 88, 53, 72, 54, 83, 84, 55
[2026-04-10 13:24:01.704] [info] Building U234 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-04-10 13:24:01.705] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U234.294.bin
[2026-04-10 13:24:01.717] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/urr/njoy_ace/v0.4.0/dir/U234.294.urr.ace.bin
[2026-04-10 13:24:01.721] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-04-10 13:24:01.722] [info]   Building reaction MTs = 20, 79, 21, 80, 66, 37, 51, 70, 71, 72, 74, 77, 73, 102, 89, 91, 67, 38, 90, 88, 87, 57, 86, 58, 54, 83, 60, 2, 61, 62, 63, 64, 65, 55, 84, 68, 56, 85, 69, 59, 53, 82, 16, 75, 17, 76, 19, 78, 81, 52
[2026-04-10 13:24:01.723] [info] Building U235 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-04-10 13:24:01.725] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U235.294.bin
[2026-04-10 13:24:01.773] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/urr/njoy_ace/v0.4.0/dir/U235.294.urr.ace.bin
[2026-04-10 13:24:01.776] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-04-10 13:24:01.778] [info]   Building reaction MTs = 814, 52, 813, 51, 818, 56, 76, 17, 817, 55, 75, 16, 77, 18, 816, 54, 72, 834, 815, 53, 822, 60, 821, 59, 5, 74, 82, 83, 84, 85, 86, 87, 81, 806, 91, 80, 805, 79, 804, 68, 830, 835, 73, 102, 810, 2, 89, 78, 803, 88, 802, 801, 800, 63, 825, 64, 826, 649, 65, 827, 828, 66, 67, 829, 61, 823, 831, 69, 812, 833, 71, 811, 62, 824, 832, 70, 809, 808, 807, 58, 820, 57, 819
[2026-04-10 13:24:01.778] [info] Building U236 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-04-10 13:24:01.781] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U236.294.bin
[2026-04-10 13:24:01.792] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/urr/njoy_ace/v0.4.0/dir/U236.294.urr.ace.bin
[2026-04-10 13:24:01.795] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-04-10 13:24:01.796] [info]   Building reaction MTs = 20, 79, 21, 80, 66, 37, 51, 70, 71, 72, 74, 77, 73, 102, 89, 91, 67, 38, 90, 88, 87, 57, 86, 58, 54, 83, 60, 2, 61, 62, 63, 64, 65, 55, 84, 68, 56, 85, 69, 59, 53, 82, 16, 75, 17, 76, 19, 78, 81, 52
[2026-04-10 13:24:01.796] [info] Building U238 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-04-10 13:24:01.798] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U238.294.bin
[2026-04-10 13:24:01.845] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/urr/njoy_ace/v0.4.0/dir/U238.294.urr.ace.bin
[2026-04-10 13:24:01.849] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-04-10 13:24:01.850] [info]   Building reaction MTs = 77, 18, 76, 17, 79, 51, 80, 52, 81, 82, 75, 16, 800, 56, 85, 78, 74, 73, 102, 62, 91, 65, 66, 61, 2, 60, 89, 67, 68, 69, 64, 5, 63, 70, 58, 87, 71, 57, 86, 649, 59, 88, 53, 72, 54, 83, 84, 55
```

### Turning off the Epithermal broadening treatment

It is possible to turn off the Epithermal broadening treatment for all nuclides by using the following syntax:

```ipython3
no_epithermal_params = tripoli5.materials.EpithermalBroadeningParameters.empty()
media = (
    tripoli5.materials.NeutronMediumBuilder()
    .withMixtures(mixtures)
    .withCatalog(catalog)
    .withEpithermalBroadening(no_epithermal_params)
    .build()
)
```

```

[2026-04-10 13:24:01.878] [info] Building U234 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-04-10 13:24:01.880] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U234.294.bin
[2026-04-10 13:24:01.895] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/urr/njoy_ace/v0.4.0/dir/U234.294.urr.ace.bin
[2026-04-10 13:24:01.901] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-04-10 13:24:01.902] [info]   Building reaction MTs = 20, 79, 21, 80, 66, 37, 51, 70, 71, 72, 74, 77, 73, 102, 89, 91, 67, 38, 90, 88, 87, 57, 86, 58, 54, 83, 60, 2, 61, 62, 63, 64, 65, 55, 84, 68, 56, 85, 69, 59, 53, 82, 16, 75, 17, 76, 19, 78, 81, 52
[2026-04-10 13:24:01.903] [info] Building U235 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-04-10 13:24:01.909] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U235.294.bin
[2026-04-10 13:24:01.966] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/urr/njoy_ace/v0.4.0/dir/U235.294.urr.ace.bin
[2026-04-10 13:24:01.969] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-04-10 13:24:01.971] [info]   Building reaction MTs = 814, 52, 813, 51, 818, 56, 76, 17, 817, 55, 75, 16, 77, 18, 816, 54, 72, 834, 815, 53, 822, 60, 821, 59, 5, 74, 82, 83, 84, 85, 86, 87, 81, 806, 91, 80, 805, 79, 804, 68, 830, 835, 73, 102, 810, 2, 89, 78, 803, 88, 802, 801, 800, 63, 825, 64, 826, 649, 65, 827, 828, 66, 67, 829, 61, 823, 831, 69, 812, 833, 71, 811, 62, 824, 832, 70, 809, 808, 807, 58, 820, 57, 819
[2026-04-10 13:24:01.972] [info] Building U236 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-04-10 13:24:01.973] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U236.294.bin
[2026-04-10 13:24:01.983] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/urr/njoy_ace/v0.4.0/dir/U236.294.urr.ace.bin
[2026-04-10 13:24:01.986] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-04-10 13:24:01.987] [info]   Building reaction MTs = 20, 79, 21, 80, 66, 37, 51, 70, 71, 72, 74, 77, 73, 102, 89, 91, 67, 38, 90, 88, 87, 57, 86, 58, 54, 83, 60, 2, 61, 62, 63, 64, 65, 55, 84, 68, 56, 85, 69, 59, 53, 82, 16, 75, 17, 76, 19, 78, 81, 52
[2026-04-10 13:24:01.987] [info] Building U238 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-04-10 13:24:01.989] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U238.294.bin
[2026-04-10 13:24:02.027] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/urr/njoy_ace/v0.4.0/dir/U238.294.urr.ace.bin
[2026-04-10 13:24:02.031] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-04-10 13:24:02.032] [info]   Building reaction MTs = 77, 18, 76, 17, 79, 51, 80, 52, 81, 82, 75, 16, 800, 56, 85, 78, 74, 73, 102, 62, 91, 65, 66, 61, 2, 60, 89, 67, 68, 69, 64, 5, 63, 70, 58, 87, 71, 57, 86, 649, 59, 88, 53, 72, 54, 83, 84, 55
```

### Applying one model to all nuclides

In order to apply one option (“None”, “SVT” or “DBRC”) to all nuclides of the system over the entire energy range from the lower bound of the simulation to \(400k_BT\), one can use the syntax below.

The example below shows the selection of the “DBRC” option which can be replaced by “None” for no treatment or “SVT” for the SVT treatment.

```ipython3
# apply over the entire energy range
range_dbrc = tripoli5.materials.EnergyRange(
    None, tripoli5.materials.Threshold.temperature_dependent(400)
)
# select all nuclides
selection_all_nuclides = tripoli5.materials.NuclideSelector.all(energy_range=range_dbrc)
# apply dbrc for all nuclides over this range
epithermal_opts = tripoli5.materials.EpithermalBroadeningParameters.empty().add(
    method="DBRC", nuclide_selector=selection_all_nuclides
)
media = (
    tripoli5.materials.NeutronMediumBuilder()
    .withMixtures(mixtures)
    .withCatalog(catalog)
    .withEpithermalBroadening(epithermal_opts)
    .build()
)
```

```

[2026-04-10 13:24:02.056] [info] Building U234 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-04-10 13:24:02.058] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U234.294.bin
[2026-04-10 13:24:02.069] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/urr/njoy_ace/v0.4.0/dir/U234.294.urr.ace.bin
[2026-04-10 13:24:02.072] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-04-10 13:24:02.075] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U234.0.bin
[2026-04-10 13:24:02.084] [info]   Building reaction MTs = 20, 79, 21, 80, 66, 37, 51, 70, 71, 72, 74, 77, 73, 102, 89, 91, 67, 38, 90, 88, 87, 57, 86, 58, 54, 83, 60, 2, 61, 62, 63, 64, 65, 55, 84, 68, 56, 85, 69, 59, 53, 82, 16, 75, 17, 76, 19, 78, 81, 52
[2026-04-10 13:24:02.086] [info] Building U235 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-04-10 13:24:02.089] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U235.294.bin
[2026-04-10 13:24:02.121] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/urr/njoy_ace/v0.4.0/dir/U235.294.urr.ace.bin
[2026-04-10 13:24:02.124] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-04-10 13:24:02.126] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U235.0.bin
[2026-04-10 13:24:02.233] [info]   Building reaction MTs = 814, 52, 813, 51, 818, 56, 76, 17, 817, 55, 75, 16, 77, 18, 816, 54, 72, 834, 815, 53, 822, 60, 821, 59, 5, 74, 82, 83, 84, 85, 86, 87, 81, 806, 91, 80, 805, 79, 804, 68, 830, 835, 73, 102, 810, 2, 89, 78, 803, 88, 802, 801, 800, 63, 825, 64, 826, 649, 65, 827, 828, 66, 67, 829, 61, 823, 831, 69, 812, 833, 71, 811, 62, 824, 832, 70, 809, 808, 807, 58, 820, 57, 819
[2026-04-10 13:24:02.235] [info] Building U236 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-04-10 13:24:02.239] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U236.294.bin
[2026-04-10 13:24:02.252] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/urr/njoy_ace/v0.4.0/dir/U236.294.urr.ace.bin
[2026-04-10 13:24:02.259] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-04-10 13:24:02.262] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U236.0.bin
[2026-04-10 13:24:02.275] [info]   Building reaction MTs = 20, 79, 21, 80, 66, 37, 51, 70, 71, 72, 74, 77, 73, 102, 89, 91, 67, 38, 90, 88, 87, 57, 86, 58, 54, 83, 60, 2, 61, 62, 63, 64, 65, 55, 84, 68, 56, 85, 69, 59, 53, 82, 16, 75, 17, 76, 19, 78, 81, 52
[2026-04-10 13:24:02.276] [info] Building U238 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-04-10 13:24:02.279] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U238.294.bin
[2026-04-10 13:24:02.342] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/urr/njoy_ace/v0.4.0/dir/U238.294.urr.ace.bin
[2026-04-10 13:24:02.346] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-04-10 13:24:02.349] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U238.0.bin
[2026-04-10 13:24:02.446] [info]   Building reaction MTs = 77, 18, 76, 17, 79, 51, 80, 52, 81, 82, 75, 16, 800, 56, 85, 78, 74, 73, 102, 62, 91, 65, 66, 61, 2, 60, 89, 67, 68, 69, 64, 5, 63, 70, 58, 87, 71, 57, 86, 649, 59, 88, 53, 72, 54, 83, 84, 55
```

### Applying a model (different from the default one) to some nuclides

If one wants to use the default parameters for most of the nuclides and “DBRC” (for instance or “None”) for some of the nuclides (for instance the heavy ones), it is possible to select a specific treatment for a list of nuclides.

For instance in the example below, all nuclides uses the default SVT model except for the U235 and U238 which uses the DBRC method.

**Warning:** the list of nuclides must be a Python [set](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset)

```ipython3
# apply over the entire energy range
range_dbrc = tripoli5.materials.EnergyRange(
    None, tripoli5.materials.Threshold.temperature_dependent(400)
)
# select only U235 and U238 for applying the DBRC
list_nuclides = tripoli5.materials.NuclideSelector.from_list(
    list=set(["U235", "U238"]),  # the argument must be a Python set
    energy_range=range_dbrc,
)
# apply SVT as the default behavior but DBRC for nuclides selected at the previous line
epithermal_opts = tripoli5.materials.EpithermalBroadeningParameters.defaultParams().add(
    method="DBRC", nuclide_selector=list_nuclides
)
media = (
    tripoli5.materials.NeutronMediumBuilder()
    .withMixtures(mixtures)
    .withCatalog(catalog)
    .withEpithermalBroadening(epithermal_opts)
    .build()
)
```

```

[2026-04-10 13:24:02.471] [info] Building U234 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-04-10 13:24:02.474] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U234.294.bin
[2026-04-10 13:24:02.485] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/urr/njoy_ace/v0.4.0/dir/U234.294.urr.ace.bin
[2026-04-10 13:24:02.489] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-04-10 13:24:02.490] [info]   Building reaction MTs = 20, 79, 21, 80, 66, 37, 51, 70, 71, 72, 74, 77, 73, 102, 89, 91, 67, 38, 90, 88, 87, 57, 86, 58, 54, 83, 60, 2, 61, 62, 63, 64, 65, 55, 84, 68, 56, 85, 69, 59, 53, 82, 16, 75, 17, 76, 19, 78, 81, 52
[2026-04-10 13:24:02.491] [info] Building U235 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-04-10 13:24:02.494] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U235.294.bin
[2026-04-10 13:24:02.527] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/urr/njoy_ace/v0.4.0/dir/U235.294.urr.ace.bin
[2026-04-10 13:24:02.530] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-04-10 13:24:02.532] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U235.0.bin
[2026-04-10 13:24:02.641] [info]   Building reaction MTs = 814, 52, 813, 51, 818, 56, 76, 17, 817, 55, 75, 16, 77, 18, 816, 54, 72, 834, 815, 53, 822, 60, 821, 59, 5, 74, 82, 83, 84, 85, 86, 87, 81, 806, 91, 80, 805, 79, 804, 68, 830, 835, 73, 102, 810, 2, 89, 78, 803, 88, 802, 801, 800, 63, 825, 64, 826, 649, 65, 827, 828, 66, 67, 829, 61, 823, 831, 69, 812, 833, 71, 811, 62, 824, 832, 70, 809, 808, 807, 58, 820, 57, 819
[2026-04-10 13:24:02.643] [info] Building U236 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-04-10 13:24:02.645] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U236.294.bin
[2026-04-10 13:24:02.653] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/urr/njoy_ace/v0.4.0/dir/U236.294.urr.ace.bin
[2026-04-10 13:24:02.656] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-04-10 13:24:02.657] [info]   Building reaction MTs = 20, 79, 21, 80, 66, 37, 51, 70, 71, 72, 74, 77, 73, 102, 89, 91, 67, 38, 90, 88, 87, 57, 86, 58, 54, 83, 60, 2, 61, 62, 63, 64, 65, 55, 84, 68, 56, 85, 69, 59, 53, 82, 16, 75, 17, 76, 19, 78, 81, 52
[2026-04-10 13:24:02.657] [info] Building U238 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-04-10 13:24:02.659] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U238.294.bin
[2026-04-10 13:24:02.709] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/urr/njoy_ace/v0.4.0/dir/U238.294.urr.ace.bin
[2026-04-10 13:24:02.713] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-04-10 13:24:02.715] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U238.0.bin
[2026-04-10 13:24:02.813] [info]   Building reaction MTs = 77, 18, 76, 17, 79, 51, 80, 52, 81, 82, 75, 16, 800, 56, 85, 78, 74, 73, 102, 62, 91, 65, 66, 61, 2, 60, 89, 67, 68, 69, 64, 5, 63, 70, 58, 87, 71, 57, 86, 649, 59, 88, 53, 72, 54, 83, 84, 55
```

### Applying a model (different from the default one) to all bound versions of some nuclides

If one wants to use a model only for bound versions of some nuclides, it is possible to select a specific treatment for all bound versions for a list of nuclides.

For instance in the example below, all bound versions of H1 and H2 uses the `None` option.

**Warning:** the list of nuclides name **must** be the free name and not the bound ones.

**Warning:** the list of nuclides must be a Python [set](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset)

```ipython3
# select only H1 and H2 bound versions (H1_H20, H_ZRH, H2_D2O, ...)
list_bound_nuclides = tripoli5.materials.NuclideSelector.from_list_all_bounds(
    list=set(["H1", "H2"]),  # the argument must be a Python set
    energy_range=tripoli5.materials.EnergyRange(None, None),
)
# apply SVT as the default behavior except for bound versions of the nuclide listed above
epithermal_opts = tripoli5.materials.EpithermalBroadeningParameters.defaultParams().add(
    method="None", nuclide_selector=list_bound_nuclides
)
media = (
    tripoli5.materials.NeutronMediumBuilder()
    .withMixtures(mixtures)
    .withCatalog(catalog)
    .withEpithermalBroadening(epithermal_opts)
    .build()
)
```

```

[2026-04-10 13:24:02.858] [info] Building U234 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-04-10 13:24:02.861] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U234.294.bin
[2026-04-10 13:24:02.871] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/urr/njoy_ace/v0.4.0/dir/U234.294.urr.ace.bin
[2026-04-10 13:24:02.874] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-04-10 13:24:02.875] [info]   Building reaction MTs = 20, 79, 21, 80, 66, 37, 51, 70, 71, 72, 74, 77, 73, 102, 89, 91, 67, 38, 90, 88, 87, 57, 86, 58, 54, 83, 60, 2, 61, 62, 63, 64, 65, 55, 84, 68, 56, 85, 69, 59, 53, 82, 16, 75, 17, 76, 19, 78, 81, 52
[2026-04-10 13:24:02.876] [info] Building U235 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-04-10 13:24:02.880] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U235.294.bin
[2026-04-10 13:24:02.913] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/urr/njoy_ace/v0.4.0/dir/U235.294.urr.ace.bin
[2026-04-10 13:24:02.916] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-04-10 13:24:02.917] [info]   Building reaction MTs = 814, 52, 813, 51, 818, 56, 76, 17, 817, 55, 75, 16, 77, 18, 816, 54, 72, 834, 815, 53, 822, 60, 821, 59, 5, 74, 82, 83, 84, 85, 86, 87, 81, 806, 91, 80, 805, 79, 804, 68, 830, 835, 73, 102, 810, 2, 89, 78, 803, 88, 802, 801, 800, 63, 825, 64, 826, 649, 65, 827, 828, 66, 67, 829, 61, 823, 831, 69, 812, 833, 71, 811, 62, 824, 832, 70, 809, 808, 807, 58, 820, 57, 819
[2026-04-10 13:24:02.918] [info] Building U236 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-04-10 13:24:02.920] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U236.294.bin
[2026-04-10 13:24:02.931] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/urr/njoy_ace/v0.4.0/dir/U236.294.urr.ace.bin
[2026-04-10 13:24:02.935] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-04-10 13:24:02.937] [info]   Building reaction MTs = 20, 79, 21, 80, 66, 37, 51, 70, 71, 72, 74, 77, 73, 102, 89, 91, 67, 38, 90, 88, 87, 57, 86, 58, 54, 83, 60, 2, 61, 62, 63, 64, 65, 55, 84, 68, 56, 85, 69, 59, 53, 82, 16, 75, 17, 76, 19, 78, 81, 52
[2026-04-10 13:24:02.938] [info] Building U238 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-04-10 13:24:02.942] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U238.294.bin
[2026-04-10 13:24:02.989] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/urr/njoy_ace/v0.4.0/dir/U238.294.urr.ace.bin
[2026-04-10 13:24:02.992] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-04-10 13:24:02.993] [info]   Building reaction MTs = 77, 18, 76, 17, 79, 51, 80, 52, 81, 82, 75, 16, 800, 56, 85, 78, 74, 73, 102, 62, 91, 65, 66, 61, 2, 60, 89, 67, 68, 69, 64, 5, 63, 70, 58, 87, 71, 57, 86, 649, 59, 88, 53, 72, 54, 83, 84, 55
```

### Changing the upper limit of the Epithermal broadening treatment

Usually the Epithermal broadening treatment is applied up to \(400k_BT\), if one wants to apply up to a different limit, it may be changed using the range definition.

For instance, below, we impose the SVT model between the lower energy limit up to \(300k_BT\):

```ipython3
# apply over the energy range up to 300 k_b T
range_dbrc = tripoli5.materials.EnergyRange(
    None, tripoli5.materials.Threshold.temperature_dependent(300)
)
# select all nuclides
selection_all_nuclides = tripoli5.materials.NuclideSelector.all(energy_range=range_dbrc)
# apply dbrc for all nuclides over this range
epithermal_opts = tripoli5.materials.EpithermalBroadeningParameters.empty().add(
    method="SVT", nuclide_selector=selection_all_nuclides
)
media = (
    tripoli5.materials.NeutronMediumBuilder()
    .withMixtures(mixtures)
    .withCatalog(catalog)
    .withEpithermalBroadening(epithermal_opts)
    .build()
)
```

```

[2026-04-10 13:24:03.038] [info] Building U234 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-04-10 13:24:03.041] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U234.294.bin
[2026-04-10 13:24:03.051] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/urr/njoy_ace/v0.4.0/dir/U234.294.urr.ace.bin
[2026-04-10 13:24:03.054] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-04-10 13:24:03.056] [info]   Building reaction MTs = 20, 79, 21, 80, 66, 37, 51, 70, 71, 72, 74, 77, 73, 102, 89, 91, 67, 38, 90, 88, 87, 57, 86, 58, 54, 83, 60, 2, 61, 62, 63, 64, 65, 55, 84, 68, 56, 85, 69, 59, 53, 82, 16, 75, 17, 76, 19, 78, 81, 52
[2026-04-10 13:24:03.056] [info] Building U235 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-04-10 13:24:03.060] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U235.294.bin
[2026-04-10 13:24:03.094] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/urr/njoy_ace/v0.4.0/dir/U235.294.urr.ace.bin
[2026-04-10 13:24:03.097] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-04-10 13:24:03.098] [info]   Building reaction MTs = 814, 52, 813, 51, 818, 56, 76, 17, 817, 55, 75, 16, 77, 18, 816, 54, 72, 834, 815, 53, 822, 60, 821, 59, 5, 74, 82, 83, 84, 85, 86, 87, 81, 806, 91, 80, 805, 79, 804, 68, 830, 835, 73, 102, 810, 2, 89, 78, 803, 88, 802, 801, 800, 63, 825, 64, 826, 649, 65, 827, 828, 66, 67, 829, 61, 823, 831, 69, 812, 833, 71, 811, 62, 824, 832, 70, 809, 808, 807, 58, 820, 57, 819
[2026-04-10 13:24:03.099] [info] Building U236 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-04-10 13:24:03.101] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U236.294.bin
[2026-04-10 13:24:03.112] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/urr/njoy_ace/v0.4.0/dir/U236.294.urr.ace.bin
[2026-04-10 13:24:03.117] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-04-10 13:24:03.118] [info]   Building reaction MTs = 20, 79, 21, 80, 66, 37, 51, 70, 71, 72, 74, 77, 73, 102, 89, 91, 67, 38, 90, 88, 87, 57, 86, 58, 54, 83, 60, 2, 61, 62, 63, 64, 65, 55, 84, 68, 56, 85, 69, 59, 53, 82, 16, 75, 17, 76, 19, 78, 81, 52
[2026-04-10 13:24:03.119] [info] Building U238 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-04-10 13:24:03.123] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U238.294.bin
[2026-04-10 13:24:03.169] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/urr/njoy_ace/v0.4.0/dir/U238.294.urr.ace.bin
[2026-04-10 13:24:03.172] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-04-10 13:24:03.173] [info]   Building reaction MTs = 77, 18, 76, 17, 79, 51, 80, 52, 81, 82, 75, 16, 800, 56, 85, 78, 74, 73, 102, 62, 91, 65, 66, 61, 2, 60, 89, 67, 68, 69, 64, 5, 63, 70, 58, 87, 71, 57, 86, 649, 59, 88, 53, 72, 54, 83, 84, 55
```

### Custom selection of options

Now that we have seen how to handle the most common use cases, we will describe in more details the selection mechanism for applying the various methods.

First, it is important to explicit that the `EpithermalBroadeningParameters` is built as a [stack](https://en.wikipedia.org/wiki/Stack_(abstract_data_type)) of `NuclideSelector`s associated to a method. A `NuclideSelector` being a pair consisting of a list of nuclides and an energy range.

We will describe the behavior using an example. The nuclides in the mixtures we have used throughout this example are “U234”, “U235”, “U236” and “U238”.

Let’s assume that we want to use the following options:

- No model as the default behaviour (here it will concern “U234” and “U236”)
- for U235 :

  - SVT between \(10^{-5}\) eV and \(1\) eV
  - DBRC between \(5\) eV and \(22\) eV
  - default behavior otherwise
- for U238:

  - DBRC between \(10^{-5}\) eV and \(3\) eV
  - DBRC between \(5\) eV and \(22\) eV
  - default behavior otherwise

To apply these options we will have to create 3 `NuclideSelector`s:

1. (U235, U238) on the range \(5\) eV and \(22\) eV
2. (U235) on the range \(10^{-5}\) eV and \(1\) eV
3. (U238) on the range \(10^{-5}\) eV and \(3\) eV

```ipython3
selector_1 = tripoli5.materials.NuclideSelector.from_list(
    list=set(["U235", "U238"]),
    energy_range=tripoli5.materials.EnergyRange(
        tripoli5.materials.Threshold.energy(5 * eV),
        tripoli5.materials.Threshold.energy(22 * eV),
    ),
)
selector_2 = tripoli5.materials.NuclideSelector.from_list(
    list=set(["U235"]),
    energy_range=tripoli5.materials.EnergyRange(
        tripoli5.materials.Threshold.energy(1e-5 * eV),
        tripoli5.materials.Threshold.energy(1 * eV),
    ),
)
selector_3 = tripoli5.materials.NuclideSelector.from_list(
    list=set(["U238"]),
    energy_range=tripoli5.materials.EnergyRange(
        tripoli5.materials.Threshold.energy(1e-5 * eV),
        tripoli5.materials.Threshold.energy(3 * eV),
    ),
)
```

Now that selector have been defined, we will assign a method to each selector

```ipython3
# choose method for each selector
epithermal_opts = (
    tripoli5.materials.EpithermalBroadeningParameters.empty()
    .add(method="DBRC", nuclide_selector=selector_1)
    .add(method="SVT", nuclide_selector=selector_2)
    .add(method="DBRC", nuclide_selector=selector_3)
)
```

It should be noted that the options works as a stack: when running the simulation, the collided isotope at a given energy is compared to the last added selector (`selector_3` in our example). If it matches then the method is applied, if it does not match then it is compared the second selector from the top (`selector_2` in our example) and so on until we reach the base one which is the default behavior. If two selectors overlap on some region, the last added method is chosen.

For instance in the selectors below, the U235 applies the SVT method between \(10^{-5}\) eV and \(10\) eV and DBRC from \(10\) eV to \(22\) eV.

```ipython3
selector_1 = tripoli5.materials.NuclideSelector.from_list(
    list=set(["U235", "U238"]),
    energy_range=tripoli5.materials.EnergyRange(
        tripoli5.materials.Threshold.energy(5 * eV),
        tripoli5.materials.Threshold.energy(22 * eV),
    ),
)
selector_2 = tripoli5.materials.NuclideSelector.from_list(
    list=set(["U235"]),
    energy_range=tripoli5.materials.EnergyRange(
        tripoli5.materials.Threshold.energy(1e-5 * eV),
        tripoli5.materials.Threshold.energy(10 * eV),
    ),
)
# choose method for each selector
epithermal_opts = (
    tripoli5.materials.EpithermalBroadeningParameters.empty()
    .add(method="DBRC", nuclide_selector=selector_1)
    .add(method="SVT", nuclide_selector=selector_2)
)
```

## Temperature interpolation method

The temperature interpolation method can be given for free gas data, thermal scattering data and URR data when Sigma1 is not applied (i.e. in PreTabulated mode) or for thermal scattering only in Sigma1 mode. It is set to `nearest` by default.

```ipython3
# redefine mixtures involving thermal data
reactor = (
    tripoli5.materials.MixtureBuilder("concentrations")
    .withName("reactor")
    .withCatalog(catalog)
    .withTemperature(298.0 * K)
    .add(
        ["U234", "U235", "U236", "U238"],
        [4.8416e-05, 4.8151e-03, 1.7407e-05, 4.3181e-02],
    )
    .build()
)

reflector = (
    tripoli5.materials.MixtureBuilder("concentrations")
    .withName("reflector")
    .withCatalog(catalog)
    .withTemperature(298.0 * K)
    .add(
        ["H1_H2O"],
        [1e-03],
    )
    .build()
)

mixtures = [reactor, reflector]

media = (
    tripoli5.materials.NeutronMediumBuilder()
    .withMixtures(mixtures)
    .withCatalog(catalog)
    .withDopplerBroadening(
        doppler_broadening_method="Sigma1",
        base_temperature=294.0 * K,
        max_energy=20.0e-3 * MeV,
    )
    .withURR("none")  # URR is not compatible with Sigma1
    .withTemperatureInterpolationMethod("linear")
    .build()
)

# below is the pretabulated version. In such a case, the temperature interpolation method is used for free gas data as well since Sigma1 is not applied.
# Note also that in the pretabulated case the URR treatment can be switched on.
media = (
    tripoli5.materials.NeutronMediumBuilder()
    .withMixtures(mixtures)
    .withCatalog(catalog)
    .withDopplerBroadening("PreTabulated")
    .withTemperatureInterpolationMethod("linear")
    .withURR("ace")
    .build()
)
```

```

[2026-04-10 13:24:03.265] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/mass/njoy_ace/v0.2.0/archive/wrapped_mass_data.bin
[2026-04-10 13:24:03.271] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/mass/njoy_ace/v0.2.0/archive/wrapped_mass_data.bin
[2026-04-10 13:24:03.276] [info] Building H1_H2O for SIGMA1 Doppler broadening
[2026-04-10 13:24:03.279] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/H1.294.bin
[2026-04-10 13:24:03.286] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/tsl/njoy_ace/v0.3.0/dir/H1_H2O.294.bin
[2026-04-10 13:24:03.310] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/tsl/njoy_ace/v0.3.0/dir/H1_H2O.300.bin
[2026-04-10 13:24:03.326] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-04-10 13:24:03.327] [info]   Building reaction MTs = 102, 2
[2026-04-10 13:24:03.328] [info]   Building thermal collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-04-10 13:24:03.329] [info]   Building thermal reaction MTs = 1000000
[2026-04-10 13:24:03.329] [info]   Building thermal collisions at temperature 300 [K], 2.58519972e-08 [MeV], 26.850000000000023 [°C]
[2026-04-10 13:24:03.330] [info]   Building thermal reaction MTs = 1000000
[2026-04-10 13:24:03.331] [info] Building U234 for SIGMA1 Doppler broadening
[2026-04-10 13:24:03.333] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U234.294.bin
[2026-04-10 13:24:03.341] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-04-10 13:24:03.342] [info]   Building reaction MTs = 20, 79, 21, 80, 66, 37, 51, 70, 71, 72, 74, 77, 73, 102, 89, 91, 67, 38, 90, 88, 87, 57, 86, 58, 54, 83, 60, 2, 61, 62, 63, 64, 65, 55, 84, 68, 56, 85, 69, 59, 53, 82, 16, 75, 17, 76, 19, 78, 81, 52
[2026-04-10 13:24:03.343] [info] Building U235 for SIGMA1 Doppler broadening
[2026-04-10 13:24:03.346] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U235.294.bin
[2026-04-10 13:24:03.378] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
… [48 lines of output omitted] …
[2026-04-10 13:24:03.641] [info]   Building reaction MTs = 20, 79, 21, 80, 66, 37, 51, 70, 71, 72, 74, 77, 73, 102, 89, 91, 67, 38, 90, 88, 87, 57, 86, 58, 54, 83, 60, 2, 61, 62, 63, 64, 65, 55, 84, 68, 56, 85, 69, 59, 53, 82, 16, 75, 17, 76, 19, 78, 81, 52
[2026-04-10 13:24:03.642] [info] Building U238 at temperatures: TemperatureRange(298 [K], 2.5679650552e-08 [MeV], 24.850000000000023 [°C])
[2026-04-10 13:24:03.644] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U238.294.bin
[2026-04-10 13:24:03.683] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U238.600.bin
[2026-04-10 13:24:03.736] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/urr/njoy_ace/v0.4.0/dir/U238.294.urr.ace.bin
[2026-04-10 13:24:03.740] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/urr/njoy_ace/v0.4.0/dir/U238.600.urr.ace.bin
[2026-04-10 13:24:03.743] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-04-10 13:24:03.744] [info]   Building reaction MTs = 77, 18, 76, 17, 79, 51, 80, 52, 81, 82, 75, 16, 800, 56, 85, 78, 74, 73, 102, 62, 91, 65, 66, 61, 2, 60, 89, 67, 68, 69, 64, 5, 63, 70, 58, 87, 71, 57, 86, 649, 59, 88, 53, 72, 54, 83, 84, 55
[2026-04-10 13:24:03.745] [info]   Building free gas collisions at temperature 600 [K], 5.17039944e-08 [MeV], 326.85 [°C]
[2026-04-10 13:24:03.746] [info]   Building reaction MTs = 77, 18, 76, 17, 79, 51, 80, 52, 81, 82, 75, 16, 800, 56, 85, 78, 74, 73, 102, 62, 91, 65, 66, 61, 2, 60, 89, 67, 68, 69, 64, 5, 63, 70, 58, 87, 71, 57, 86, 649, 59, 88, 53, 72, 54, 83, 84, 55
```
