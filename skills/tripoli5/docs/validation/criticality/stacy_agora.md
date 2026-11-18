<!-- source: https://tripoli5.asnr.dev/documentation/latest-release/validation/criticality/stacy_agora.html -->

# The modified STACY facility using AGORA geometry

The modified STACY facility is an installation designed to perform critical experiments. It is constituted of a square lattice of identical fuel pins, immersed in a cylindrical water tank. Criticality is approached by varying the water level in the cylindrical tank.

In the following, a simplified model of the experiment is built. It is demonstrated how the Python API of TRIPOLI-5 can be used to perform several successive simulations, in search for the critical water level in the experiment for a given lattice configuration.

Information about the STACY experiment and its associated model were kindly provided by JAEA. For more details about the STACY experiment and the geometrical model used in the present example, please refer to :

19. Gunji, et al., *Study on the specifications of the basic core configurations of the modified STACY* Annals of Nuclear Energy (209), 2024, 110783.

```ipython3
import matplotlib

matplotlib.set_loglevel(
    "critical"
)  # suppress "Matplotlib is building the font cache" message
```

```ipython3
import tripoli5 as t5

import matplotlib.pyplot as plt
import numpy as np
```

## Materials definition

```ipython3
# Temperature data will be provided in Kelvin
from tripoli5.core.literals import K

## Define a catalog file (equivalent to defining the acefile in other MC codes)
## In the present case, the catalog associated to the environment variable T5_CATALOG_PATH is used
catalog = t5.delos.Catalog.fromEnvVariable()

mixtures = []

# declare material with name "FUEL" (UO2 at 5% w.t. enrichment)
fuel = t5.materials.MixtureBuilder("concentrations")
fuel = fuel.withName("FUEL")
fuel = fuel.withTemperature(294 * K)
fuel = fuel.withCatalog(catalog)
fuel = fuel.add("U234", 1.1650e-05)
fuel = fuel.add("U235", 1.1554e-03)
fuel = fuel.add("U238", 2.1746e-02)
fuel = fuel.add("O16", 4.5913e-02)
fuel = fuel.build()

mixtures.append(fuel)

## a alternate and condensed way to build a material
water = (
    t5.materials.MixtureBuilder("concentrations")
    .withName("WATER")
    .withTemperature(294 * K)
    .withCatalog(catalog)
    .add("H1_H2O", 6.6648e-02)
    .add("H2_D2O", 9.9987e-06)
    .add("O16", 3.3329e-02)
    .build()
)
mixtures.append(water)

## Note the use of natural abundances, extracted from an external database
zircalloy = (
    t5.materials.MixtureBuilder("concentrations")
    .withName("CLAD")
    .withTemperature(294 * K)
    .withCatalog(catalog)
    .withNaturalAbundances(t5.materials.NaturalAbundances.fromNUBASE2020())
    .add("SN", 4.2e-06)
    .add("FE", 1.36e-04)
    .add("CR", 6.99e-05)
    .add("O", 3.18e-04)
    .add("C", 4.27e-05)
    .add("ZR", 2.185e-02)
    .build()
)
mixtures.append(zircalloy)

air = (
    t5.materials.MixtureBuilder("concentrations")
    .withName("AIR")
    .withTemperature(294 * K)
    .withCatalog(catalog)
    .withNaturalAbundances(t5.materials.NaturalAbundances.fromNUBASE2020())
    .add("N", 3.9e-05)
    .add("O", 1.0e-05)
    .build()
)
mixtures.append(air)

# Declare the collection of materials and build the nuclear data
media = t5.materials.NeutronMediumBuilder()
media = media.withCatalog(catalog)
media = media.withMixtures(mixtures)
media = media.build()
```

```

[2026-03-26 15:23:48.664] [info] Retrieving catalog data from environment variable T5_CATALOG_PATH.
[2026-03-26 15:23:48.666] [info] Loading catalog from file: /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/endfb8r0_mcnp_v2.2.0.yaml
[2026-03-26 15:23:48.689] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/mass/njoy_ace/v0.2.0/archive/wrapped_mass_data.bin
[2026-03-26 15:23:48.696] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/mass/njoy_ace/v0.2.0/archive/wrapped_mass_data.bin
[2026-03-26 15:23:48.700] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/mass/njoy_ace/v0.2.0/archive/wrapped_mass_data.bin
[2026-03-26 15:23:48.707] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/mass/njoy_ace/v0.2.0/archive/wrapped_mass_data.bin
[2026-03-26 15:23:48.713] [info] Building C12 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-03-26 15:23:48.715] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/C12.294.bin
[2026-03-26 15:23:48.724] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-03-26 15:23:48.726] [info]   Building reaction MTs = 60, 2, 53, 59, 61, 62, 91, 58, 56, 55, 107, 52, 104, 51, 103, 5, 57, 28, 54, 102
[2026-03-26 15:23:48.727] [info] Building C13 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-03-26 15:23:48.731] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/C13.294.bin
[2026-03-26 15:23:48.741] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-03-26 15:23:48.743] [info]   Building reaction MTs = 800, 102, 52, 51, 2, 53
[2026-03-26 15:23:48.744] [info] Building CR50 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-03-26 15:23:48.748] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/CR50.294.bin
[2026-03-26 15:23:48.764] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-03-26 15:23:48.766] [info]   Building reaction MTs = 103, 16, 5, 56, 52, 104, 91, 51, 22, 55, 107, 2, 28, 54, 102, 53
[2026-03-26 15:23:48.768] [info] Building CR52 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
… [123 lines of output omitted] …
[2026-03-26 15:23:49.518] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-03-26 15:23:49.519] [info]   Building reaction MTs = 804, 803, 802, 801, 800, 649, 826, 600, 836, 849, 112, 820, 58, 825, 839, 810, 102, 53, 815, 32, 91, 829, 838, 817, 55, 822, 816, 54, 59, 821, 808, 814, 52, 806, 807, 805, 837, 835, 834, 833, 832, 831, 5, 823, 105, 830, 827, 809, 2, 828, 824, 819, 57, 28, 811, 16, 104, 812, 17, 24, 22, 813, 51, 56, 818
[2026-03-26 15:23:49.520] [info] Building ZR94 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-03-26 15:23:49.522] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/ZR94.294.bin
[2026-03-26 15:23:49.530] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-03-26 15:23:49.532] [info]   Building reaction MTs = 825, 22, 24, 607, 17, 812, 104, 606, 16, 811, 28, 819, 57, 809, 822, 60, 821, 59, 649, 826, 32, 91, 608, 609, 829, 824, 62, 800, 801, 601, 837, 804, 817, 55, 803, 605, 816, 54, 808, 603, 839, 814, 52, 806, 604, 807, 602, 838, 805, 802, 102, 810, 827, 58, 820, 112, 53, 815, 849, 836, 600, 818, 56, 835, 834, 833, 832, 831, 5, 105, 51, 813, 830, 828, 2, 823, 61
[2026-03-26 15:23:49.532] [info] Building ZR96 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-03-26 15:23:49.534] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/ZR96.294.bin
[2026-03-26 15:23:49.540] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-03-26 15:23:49.542] [info]   Building reaction MTs = 801, 105, 807, 53, 24, 804, 601, 602, 805, 51, 22, 600, 803, 649, 802, 52, 806, 808, 54, 17, 104, 800, 849, 16, 5, 28, 2, 55, 809, 91, 102
```

## Geometry definition

The experiment consists of a square lattice of size 31x31 (pitch = 1.27 cm) immersed in a cylindrical tank partially filled with water.

The fuel pins inserted in the lattice are identical and look something like this :

```text
  _______________________ z = 148.5
  |             |
  |             |        enveloppe
  |  _________  |
  |  | _____ |  |        air above fuel
  |  | |   | |  |
  |  | |   | |  |        fuel + gap + clad
  |  | |   | |  |
  |  | |   | |  |
  |  | |   | |  |
----------------------     water_height
  |  | |   | |  |
  |  | |   | |  |
  |  | |   | |  |         fuel + gap + clad
  |  | |   | |  |
  |  | |   | |  |
  |  |_|___|_|  |_________ z = 0
  |             |
  |             |         enveloppe
  |_____________|_________ z = -1.5
```

A lattice of identical fuel pins is placed inside a water tank. The tank bottom is located at an abscissa of z = -21 cm.

In this example, we model the lattice associated to the first critical experiments described in the reference provided above

```ipython3
## The experiment is made out of a 31x31 square lattice
##    1 : fuel pin         2 : empty lattice position

lattice_string = """
2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
2 2 2 2 2 2 2 2 2 2 2 2 2 1 2 1 2 1 2 2 2 2 2 2 2 2 2 2 2 2 2
2 2 2 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 2 2 2
2 2 2 2 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 2 2 2 2
2 2 2 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 2 2 2
2 2 2 2 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 2 2 2 2
2 2 2 2 1 2 1 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 1 2 1 2 2 2 2
2 2 2 2 2 1 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 1 2 2 2 2 2
2 2 2 2 1 2 1 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 1 2 1 2 2 2 2
2 2 2 2 2 1 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 1 2 2 2 2 2
2 2 2 2 1 2 1 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 1 2 1 2 2 2 2
2 2 2 1 2 1 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 1 2 1 2 2 2
2 2 2 2 1 2 1 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 1 2 1 2 2 2 2
2 2 2 1 2 1 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 1 2 1 2 2 2
2 2 2 2 1 2 1 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 1 2 1 2 2 2 2
2 2 2 1 2 1 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 1 2 1 2 2 2
2 2 2 2 1 2 1 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 1 2 1 2 2 2 2
2 2 2 2 2 1 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 1 2 2 2 2 2
2 2 2 2 1 2 1 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 1 2 1 2 2 2 2
2 2 2 2 2 1 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 1 2 2 2 2 2
2 2 2 2 1 2 1 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 1 2 1 2 2 2 2
2 2 2 2 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 2 2 2 2
2 2 2 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 2 2 2
2 2 2 2 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 2 2 2 2
2 2 2 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 2 2 2
2 2 2 2 2 2 2 2 2 2 2 2 2 1 2 1 2 1 2 2 2 2 2 2 2 2 2 2 2 2 2
2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
"""
```

The overall geometry of the problem is made to depend on a global parameter, the water height inside the tank. To update the water level in the tank, the whole geometry is put inside a Python function, so that it can be re-uploaded at will.

Safeguards constraints on the experiment are such that one cannot perform a critcial experiment with water level lower than 40 cm or higher than 140 cm. To take this into account, the Python function returns `None` if the water level provided does not lie within these bounds.

```ipython3
from tripoli5.core.euclide import Point, Vector
from tripoli5 import agora

## The geometry definition is put inside a function, to easily vary the water level
def make_stacy_geom(water_height, lattice_string):
    ## Make sure the water height is within the experiment tolerances
    ## This could also be used to make sure that the input value does not
    ## break the geometrical model
    if water_height < 40 or water_height > 140:
        return None

    ##  Main dimensions of the model
    z_min = -21  # lower and upper dimensions of the problem
    z_max = 148.5

    r_fuel = 0.41  # ful, air gap and cladding radii
    r_gap = 0.42
    r_clad = 0.475

    r_max = 50  # outer radius

    ## bottom of the fuel pin lattice is at -1.5 cm
    ## so that the fuel pins all begin at z = 0 cm
    lattice_zmin = -1.5
    ###

    zpl_min = agora.ZPlane(z_min)
    zpl_max = agora.ZPlane(z_max)
    zpl_lat_min = agora.ZPlane(lattice_zmin)

    zpl_water_height = agora.ZPlane(water_height)

    zpl_fuel_bottom = agora.ZPlane(0.0)
    zpl_fuel_top = agora.ZPlane(142)
    zpl_air_above_top = agora.ZPlane(146)

    cylz_fuel = agora.ZCylinder(0.0, 0.0, r_fuel)
    cylz_gap = agora.ZCylinder(0.0, 0.0, r_gap)
    cylz_clad = agora.ZCylinder(0.0, 0.0, r_clad)

    ## ----------------------------
    ## --- Fuel pins under water
    ## ----------------------------
    ## Fuel
    fuel_below = agora.Shape(-cylz_fuel & +zpl_fuel_bottom)
    vol_fuel_below = agora.Volume(fuel_below, "FUEL")

    ## Gap
    gap_below = agora.Shape(-cylz_gap & +cylz_fuel & +zpl_fuel_bottom)
    vol_gap_below = agora.Volume(gap_below, "AIR")

    ## Clad
    clad_below = agora.Shape(
        (-cylz_clad & +cylz_gap & +zpl_fuel_bottom) | (-cylz_clad & -zpl_fuel_bottom)
    )
    vol_clad_below = agora.Volume(clad_below, "CLAD")

    ## Water
    vol_water_below = agora.Volume(agora.Shape(+cylz_clad), "WATER")

    u_fuel_pin_below = agora.Universe(
        [vol_fuel_below, vol_gap_below, vol_clad_below, vol_water_below]
    )

    ## ----------------------------
    ## --- Fuel pins above water
    ## ----------------------------
    ## Fuel
    fuel_above = agora.Shape(-cylz_fuel & -zpl_fuel_top)
    vol_fuel_above = agora.Volume(fuel_above, "FUEL")

    ## Gap
    gap_above = agora.Shape(
        (-cylz_gap & +cylz_fuel & -zpl_fuel_top)
        | (-cylz_gap & +zpl_fuel_top & -zpl_air_above_top)
    )
    vol_gap_above = agora.Volume(gap_above, "AIR")

    ## Clad
    clad_above = agora.Shape(
        (-cylz_clad & +cylz_gap & -zpl_air_above_top)
        | (-cylz_clad & +zpl_air_above_top)
    )
    vol_clad_above = agora.Volume(clad_above, "CLAD")

    ## Air
    vol_air_above = agora.Volume(agora.Shape(+cylz_clad), "AIR")

    u_fuel_pin_above = agora.Universe(
        [vol_fuel_above, vol_gap_above, vol_clad_above, vol_air_above]
    )

    air_above = agora.createInfinite(material="AIR")
    water_below = agora.createInfinite(material="WATER")

    ## LATTICE DEFINITION : square lattice with a 1.27 cm pitch
    lat_above = agora.RectLattice(
        Point(-19.685, -19.685, 0),
        Vector(1.27, 1.27, 0.0),
        31,
        31,
        0,
        universe=u_fuel_pin_above,
        outer_universe=air_above,
        label="stacy_lattice_above_crit_height",
    )

    lat_below = agora.RectLattice(
        Point(-19.685, -19.685, 0),
        Vector(1.27, 1.27, 0.0),
        31,
        31,
        0,
        universe=u_fuel_pin_below,
        outer_universe=water_below,
        label="stacy_lattice_below_crit_height",
    )

    ## set empty positions from the lattice_string variable given as input
    lattice_config = np.fromstring(lattice_string, sep=" ").reshape(31, 31)
    empty_positions = np.where(lattice_config == 2)

    for x, y in zip(empty_positions[0], empty_positions[1]):
        lat_below[x, y, 0] = water_below
        lat_above[x, y, 0] = air_above

    ## Define the boundary of the problem : the external tank
    cylz_tank = agora.ZCylinder(0, 0, r_max)

    tank_above = agora.Shape(-cylz_tank & zpl_water_height)
    ctank_above = agora.CompositeVolume(tank_above, filler=lat_above)

    tank_below = agora.Shape(-cylz_tank & zpl_lat_min & -zpl_water_height)
    ctank_below = agora.CompositeVolume(tank_below, filler=lat_below)

    tank_below_lat = agora.Shape(-cylz_tank & -zpl_lat_min)
    ctank_below_lat = agora.Volume(tank_below_lat, "WATER")

    u_tank = agora.Universe([ctank_above, ctank_below, ctank_below_lat])

    tank_region = -cylz_tank & zpl_min & -zpl_max
    tank_tot = agora.Shape(tank_region)
    tank_volume = agora.CompositeVolume(tank_tot, u_tank)

    ## outside of the geometry (particles entering this volume are killed)
    outside_volume = agora.Volume.outside(agora.Shape(-tank_region))

    root_universe = agora.Universe([tank_volume, outside_volume])
    geometry = agora.Geometry(root_universe)

    return geometry
```

### Plot geometry

```ipython3
## Set water height at z = 60 cm
geo = make_stacy_geom(60, lattice_string)

# Plot XY cut view of the model at Z=20 cm
t5_plt = t5.geoplotter.GeoPlotterPyplot(geo)

frame = t5.geoplotter.Frame.fromMinMax(
    plane_cut="XY", altitude=50, u_min=-20, u_max=20, v_min=-20, v_max=20
)

## The color palette and colors are those available in the matplotlib library
_ = t5_plt.plot(
    frame=frame,
    color_map="Accent",
    mapping_colors={
        "WATER": "cornflowerblue",
        "FUEL": "chartreuse",
        "AIR": "lightblue",
        "CLAD": "grey",
    },
    resolution=100,
)
```

![figure](https://tripoli5.asnr.dev/documentation/latest-release/_images/validation_criticality_stacy_agora_10_0.png)

```ipython3
frame = t5.geoplotter.Frame.fromMinMax(
    plane_cut="XZ", altitude=0, u_min=-30, u_max=30, v_min=-20, v_max=148
)

_ = t5_plt.plot(
    frame=frame,
    color_map="Accent",
    mapping_colors={
        "WATER": "cornflowerblue",
        "FUEL": "chartreuse",
        "AIR": "lightblue",
        "CLAD": "grey",
    },
    resolution=100,
)
```

![figure](https://tripoli5.asnr.dev/documentation/latest-release/_images/validation_criticality_stacy_agora_11_0.png)

## Source definition

```ipython3
## the fuel lattice total height is 142 cm (71x2)
src_space_distrib = t5.distributions.spatial.CylinderDistribution(
    Point(0.0, 0.0, 71.0), 15, 71
)
src_energy_distrib = t5.distributions.energy.MonoKinetic(
    t5.core.physics.Energy(2.0, t5.core.physics.Energy.Units.MeV)
)
src_angle_distrib = t5.distributions.angular.IsotropicAngularDistribution()

src = t5.source.FactorizedSource(
    src_space_distrib, src_energy_distrib, src_angle_distrib
)
```

## Sample Keff at different water heights

```ipython3
keff_vs_height = []

for sampled_height in range(46, 57):
    geo = make_stacy_geom(
        sampled_height, lattice_string
    )  ## paramater-dependent geometry

    ## Remember that a safeguard has been implemented in the function make_stacy_geom :
    ## if the provided water level does not fall within the experimental constraints, it returns None
    if geo is None:
        continue

    ## To change the random seed in each iteration of the loop,
    ## a different integer value must be passed to the simulationParameters object.
    ## In the present case, there's a natural candidate : the sampled water level,
    ## that increase by integrer increments
    simu_params = t5.simulation.SimulationParameters(
        nb_cycles=150,
        nb_events=10_000,  # Particles per cycle
        name="crit_height_search",
        nb_threads=20,
        discard=50,
        random_seed=sampled_height,  ## change random seed
    )

    ## initialize simulation object
    simu = (
        t5.simulation.SimulationBuilder(
            simulation_mode="criticality", parallelism_type="openmp"
        )
        .withMedia("neutron", media)
        .withSource(src)
        .withParameters(simu_params)
        .withGeometry(geo)
        .build()
    )
    simu.run()

    keff_vs_height.append(
        [sampled_height, simu.getScore(0).mean[0], np.sqrt(simu.getScore(0).var[0])]
    )

keff_vs_height = np.array(keff_vs_height)
```

```

[2026-03-26 15:24:34.579] [info] *** Beginning of simulation ***
[2026-03-26 15:24:34.623] [info] Cycle: 1 of 150
[2026-03-26 15:24:35.437] [info]   kstep = 0.45880
[2026-03-26 15:24:35.440] [info]   Mean number of collisions: 30.6633
[2026-03-26 15:24:35.440] [info] Cycle: 2 of 150
[2026-03-26 15:24:36.264] [info]   kstep = 0.80850
[2026-03-26 15:24:36.265] [info]   Mean number of collisions: 58.6303
[2026-03-26 15:24:36.265] [info] Cycle: 3 of 150
[2026-03-26 15:24:37.156] [info]   kstep = 0.96640
[2026-03-26 15:24:37.158] [info]   Mean number of collisions: 70.6971
[2026-03-26 15:24:37.160] [info] Cycle: 4 of 150
[2026-03-26 15:24:37.892] [info]   kstep = 0.99240
[2026-03-26 15:24:37.893] [info]   Mean number of collisions: 73.2051
[2026-03-26 15:24:37.893] [info] Cycle: 5 of 150
[2026-03-26 15:24:38.738] [info]   kstep = 1.00090
[2026-03-26 15:24:38.742] [info]   Mean number of collisions: 74.7219
[2026-03-26 15:24:38.742] [info] Cycle: 6 of 150
[2026-03-26 15:24:39.621] [info]   kstep = 0.96510
[2026-03-26 15:24:39.625] [info]   Mean number of collisions: 73.6462
… [4932 lines of output omitted] …
[2026-03-26 15:41:15.835] [info]   Mean number of collisions: 76.5618
[2026-03-26 15:41:15.835] [info] Cycle: 148 of 150
[2026-03-26 15:41:16.400] [info]   kstep = 1.01040
[2026-03-26 15:41:16.402] [info]   Mean number of collisions: 75.8032
[2026-03-26 15:41:16.403] [info] Cycle: 149 of 150
[2026-03-26 15:41:16.993] [info]   kstep = 1.00380
[2026-03-26 15:41:16.995] [info]   Mean number of collisions: 77.5983
[2026-03-26 15:41:16.996] [info] Cycle: 150 of 150
[2026-03-26 15:41:17.586] [info]   kstep = 1.04170
[2026-03-26 15:41:17.588] [info]   Mean number of collisions: 75.5691
```

```ipython3
plt.figure(figsize=(10, 8))
plt.errorbar(
    keff_vs_height[:, 0],
    keff_vs_height[:, 1],
    yerr=keff_vs_height[:, 2],
    fmt="o-",
    lw=1,
)
plt.ylabel("Simulated Keff", fontsize=14)
plt.xlabel("Water height [cm]", fontsize=14)
plt.grid()
plt.show()
```

![figure](https://tripoli5.asnr.dev/documentation/latest-release/_images/validation_criticality_stacy_agora_16_0.png)

```ipython3
## sampled height, estimated Keff, estimated standard deviation on Keff
np.set_printoptions(precision=5, suppress=True)
print(keff_vs_height)
```

```

[[46.       0.98638  0.00119]
 [47.       0.98785  0.00126]
 [48.       0.99292  0.00152]
 [49.       0.99403  0.00111]
 [50.       0.99716  0.00131]
 [51.       0.99777  0.00141]
 [52.       1.00137  0.00124]
 [53.       1.00409  0.00126]
 [54.       1.00518  0.00132]
 [55.       1.00651  0.00116]
 [56.       1.00755  0.0014 ]]
```

```ipython3
## Interpolate the critical water level using the linear interpolation method interp from numpy
interp_crit_height = np.interp(1.0, keff_vs_height[:, 1], keff_vs_height[:, 0])
print(f"Interpolated critical height = {interp_crit_height:.1f} cm")
```

```

Interpolated critical height = 51.6 cm
```
