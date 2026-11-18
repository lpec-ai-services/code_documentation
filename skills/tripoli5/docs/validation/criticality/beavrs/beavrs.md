<!-- source: https://tripoli5.asnr.dev/documentation/latest-release/validation/criticality/beavrs/beavrs.html -->

# The BEAVRS benchmark

The BEAVRS benchmark represents a full-core Pressurized Water Reactor (PWR) model, encompassing fuel depletion on two operational cycles of a commercial nuclear power plant. It offers a high level of detail in the description of the geometry and the material compositions, as well as an extensive list of experimental measurements, and is publicly available through an MIT license at <https://github.com/mit-crpg/BEAVRS>.

The model provided correspond to the “all rods out” (ARO) configuration.

This model is issued from:

P. Garces, C. Larmier and A. Jinaphanh, “*Validation of TRIPOLI-5® Monte Carlo code using the BEAVRS Benchmark*”, Physor 2026

```ipython3
import tripoli5
from tripoli5.core.euclide import Point
from tripoli5.core.literals import MeV
```

As the geometric model of BEAVRS is quite large, it has been wrapped into a function which parameters are the control rods banks level.

The full model is available upon request.

```ipython3
from BEAVRS_geom import make_BEAVRS_geometry

geometry = make_BEAVRS_geometry(
    228,  # Rods A_level
    228,  # Rods B_level
    228,  # Rods C_level
    213,  # Rods D_level
    228,  # Rods Sa_level
    228,  # Rods Sb_level
    228,  # Rods Sc_level
    228,  # Rods Sd_level
    228,  # Rods Se_level
)
# plot radial view
plotter = tripoli5.geoplotter.GeoPlotterPyplot(geometry)
frame = tripoli5.geoplotter.Frame.fromMinMax(
    "XY", altitude=230, u_min=-250, u_max=250, v_min=-250, v_max=250
)
_ = plotter.plot(
    frame=frame, resolution=15, nb_threads=10, color_map="twilight_shifted"
)
```

![figure](https://tripoli5.asnr.dev/documentation/latest-release/_images/validation_criticality_beavrs_beavrs_3_0.png)

Similarly to the geometric model, the mixtures definition is quite large and does not fit into a readable jupyter notebook.

They have been wrapped into a function which takes as an argument the catalog adressing nuclear data and the boron concentration in ppm.

They are defined at \(600K\)

```ipython3
from BEAVRS_mixture import make_BEAVRS_mixtures

# define catalog from explicit file path
# catalog = tripoli5.delos.Catalog.fromFile(
#    f"/opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/endfb8r0_mcnp_v{tripoli5.delos.CATALOG_VERSION}.yaml"
# )
# or from env variable
catalog = tripoli5.delos.Catalog.fromEnvVariable()
boron_atom_density_ppm = 975
mixtures = make_BEAVRS_mixtures(catalog, boron_atom_density_ppm)
```

```

[2026-03-11 17:11:30.606] [info] Retrieving catalog data from environment variable T5_CATALOG_PATH.
[2026-03-11 17:11:30.606] [info] Loading catalog from file: /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/endfb8r0_mcnp_v2.2.0.yaml
[2026-03-11 17:11:30.649] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/mass/njoy_ace/v0.2.0/archive/wrapped_mass_data.bin
[2026-03-11 17:11:30.658] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/mass/njoy_ace/v0.2.0/archive/wrapped_mass_data.bin
[2026-03-11 17:11:30.662] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/mass/njoy_ace/v0.2.0/archive/wrapped_mass_data.bin
[2026-03-11 17:11:30.666] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/mass/njoy_ace/v0.2.0/archive/wrapped_mass_data.bin
[2026-03-11 17:11:30.671] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/mass/njoy_ace/v0.2.0/archive/wrapped_mass_data.bin
[2026-03-11 17:11:30.675] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/mass/njoy_ace/v0.2.0/archive/wrapped_mass_data.bin
[2026-03-11 17:11:30.679] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/mass/njoy_ace/v0.2.0/archive/wrapped_mass_data.bin
[2026-03-11 17:11:30.684] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/mass/njoy_ace/v0.2.0/archive/wrapped_mass_data.bin
[2026-03-11 17:11:30.688] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/mass/njoy_ace/v0.2.0/archive/wrapped_mass_data.bin
[2026-03-11 17:11:30.692] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/mass/njoy_ace/v0.2.0/archive/wrapped_mass_data.bin
[2026-03-11 17:11:30.697] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/mass/njoy_ace/v0.2.0/archive/wrapped_mass_data.bin
[2026-03-11 17:11:30.701] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/mass/njoy_ace/v0.2.0/archive/wrapped_mass_data.bin
[2026-03-11 17:11:30.705] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/mass/njoy_ace/v0.2.0/archive/wrapped_mass_data.bin
[2026-03-11 17:11:30.710] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/mass/njoy_ace/v0.2.0/archive/wrapped_mass_data.bin
[2026-03-11 17:11:30.714] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/mass/njoy_ace/v0.2.0/archive/wrapped_mass_data.bin
```

Materials are constructed from the mixture definition, it selects the “ACE” URR model and applies the epithermal broadening options (SVT).

```ipython3
media = (
    tripoli5.materials.NeutronMediumBuilder()
    .withCatalog(catalog)
    .withMixtures(mixtures)
    .withURR(parameter="ace")
    .build()
)
```

```

[2026-03-11 17:11:30.739] [info] Building AG107 at temperatures: TemperatureRange(600 [K], 5.17039944e-08 [MeV], 326.85 [°C])
[2026-03-11 17:11:30.742] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/AG107.600.bin
[2026-03-11 17:11:30.822] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/urr/njoy_ace/v0.4.0/dir/AG107.600.urr.ace.bin
[2026-03-11 17:11:30.833] [info]   Building free gas collisions at temperature 600 [K], 5.17039944e-08 [MeV], 326.85 [°C]
[2026-03-11 17:11:30.834] [info]   Building reaction MTs = 59, 58, 61, 62, 91, 64, 65, 66, 63, 102, 107, 53, 52, 51, 22, 56, 17, 55, 103, 16, 54, 28, 57, 2, 60
[2026-03-11 17:11:30.836] [info] Building AG109 at temperatures: TemperatureRange(600 [K], 5.17039944e-08 [MeV], 326.85 [°C])
[2026-03-11 17:11:30.839] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/AG109.600.bin
[2026-03-11 17:11:30.927] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/urr/njoy_ace/v0.4.0/dir/AG109.600.urr.ace.bin
[2026-03-11 17:11:30.934] [info]   Building free gas collisions at temperature 600 [K], 5.17039944e-08 [MeV], 326.85 [°C]
[2026-03-11 17:11:30.935] [info]   Building reaction MTs = 615, 611, 629, 630, 64, 628, 62, 91, 622, 61, 2, 58, 56, 55, 59, 649, 60, 800, 623, 626, 54, 41, 625, 624, 801, 620, 619, 617, 616, 28, 618, 57, 627, 68, 67, 849, 613, 66, 65, 16, 606, 17, 607, 53, 24, 614, 22, 612, 51, 52, 63, 621, 600, 601, 602, 603, 604, 605, 608, 609, 610, 102
[2026-03-11 17:11:30.937] [info] Building AL27 at temperatures: TemperatureRange(600 [K], 5.17039944e-08 [MeV], 326.85 [°C])
[2026-03-11 17:11:30.940] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/AL27.600.bin
[2026-03-11 17:11:30.968] [info]   Building free gas collisions at temperature 600 [K], 5.17039944e-08 [MeV], 326.85 [°C]
[2026-03-11 17:11:30.969] [info]   Building reaction MTs = 80, 611, 83, 84, 55, 817, 708, 73, 53, 815, 85, 108, 610, 616, 102, 79, 818, 56, 51, 813, 613, 619, 111, 54, 668, 33, 804, 814, 52, 71, 706, 63, 805, 663, 28, 808, 806, 612, 22, 657, 81, 811, 809, 810, 816, 45, 807, 812, 651, 16, 61, 2, 710, 75, 62, 705, 70, 819, 57, 82, 78, 849, 667, 803, 32, 77, 76, 74, 709, 72, 707, 615, 609, 112, 60, 59, 117, 58, 5, 64, 699, 65, 700, 66, 701, 67, 702, 68, 703, 69, 704, 86, 600, 87, 601, 88, 602, 89, 603, 604, 91, 605, 606, 607, 608, 614, 617, 618, 649, 650, 652, 653, 654, 655, 656, 658, 659, 660, 661, 662, 664, 665, 666, 669, 749, 800, 801, 802
[2026-03-11 17:11:30.970] [info] Building AR36 at temperatures: TemperatureRange(600 [K], 5.17039944e-08 [MeV], 326.85 [°C])
[2026-03-11 17:11:30.973] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/AR36.600.bin
[2026-03-11 17:11:30.984] [info]   Building free gas collisions at temperature 600 [K], 5.17039944e-08 [MeV], 326.85 [°C]
[2026-03-11 17:11:30.987] [info]   Building reaction MTs = 66, 65, 104, 52, 28, 57, 103, 16, 51, 22, 68, 69, 70, 71, 102, 55, 107, 56, 108, 67, 54, 53, 60, 59, 58, 2, 61, 62, 91, 63, 64
[2026-03-11 17:11:30.988] [info] Building AR38 at temperatures: TemperatureRange(600 [K], 5.17039944e-08 [MeV], 326.85 [°C])
… [376 lines of output omitted] …
[2026-03-11 17:11:35.536] [info] Building ZR94 at temperatures: TemperatureRange(600 [K], 5.17039944e-08 [MeV], 326.85 [°C])
[2026-03-11 17:11:35.539] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/ZR94.600.bin
[2026-03-11 17:11:35.553] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/urr/njoy_ace/v0.4.0/dir/ZR94.600.urr.ace.bin
[2026-03-11 17:11:35.561] [info]   Building free gas collisions at temperature 600 [K], 5.17039944e-08 [MeV], 326.85 [°C]
[2026-03-11 17:11:35.562] [info]   Building reaction MTs = 825, 22, 24, 607, 17, 812, 104, 606, 16, 811, 28, 819, 57, 809, 822, 60, 821, 59, 649, 826, 32, 91, 608, 609, 829, 824, 62, 800, 801, 601, 837, 804, 817, 55, 803, 605, 816, 54, 808, 603, 839, 814, 52, 806, 604, 807, 602, 838, 805, 802, 102, 810, 827, 58, 820, 112, 53, 815, 849, 836, 600, 818, 56, 835, 834, 833, 832, 831, 5, 105, 51, 813, 830, 828, 2, 823, 61
[2026-03-11 17:11:35.563] [info] Building ZR96 at temperatures: TemperatureRange(600 [K], 5.17039944e-08 [MeV], 326.85 [°C])
[2026-03-11 17:11:35.566] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/ZR96.600.bin
[2026-03-11 17:11:35.578] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/urr/njoy_ace/v0.4.0/dir/ZR96.600.urr.ace.bin
[2026-03-11 17:11:35.585] [info]   Building free gas collisions at temperature 600 [K], 5.17039944e-08 [MeV], 326.85 [°C]
[2026-03-11 17:11:35.586] [info]   Building reaction MTs = 801, 105, 807, 53, 24, 804, 601, 602, 805, 51, 22, 600, 803, 649, 802, 52, 806, 808, 54, 17, 104, 800, 849, 16, 5, 28, 2, 55, 809, 91, 102
```

The source is defined as a cylinder encompassing the reactor core

```ipython3
src = tripoli5.source.FactorizedSource(
    tripoli5.distributions.spatial.CylinderDistribution(
        Point(0.0, 0.0, 230.0), 200, 230.0
    ),
    tripoli5.distributions.energy.MonoKinetic(2.0 * MeV),
    tripoli5.distributions.angular.IsotropicAngularDistribution(),
    1.0,  # norm
)
```

The tally is defined as the flux decomposed over an 281 groups energy bin and geometry integrated.

```ipython3
from energy_group_mesh import Mesh_281g

mesh_281g = Mesh_281g()
flux_spect_general = tripoli5.score.FluxSpectrumCollGeneral(
    mesh_281g, "Integrated Flux over 281 groups"
)
score_mgr = tripoli5.score.ScoreManager("BEAVRS")
score_mgr.addScore(flux_spect_general)
score_mgr.initialize("")
```

Simulation parameters are defined below.

They are **willingly very low** to fit into our every day running continuous integration system.

Please don’t use these parameters!

```ipython3
param = tripoli5.simulation.SimulationParameters(
    nb_cycles=170,
    nb_events=20000,  # Particles per cycle
    name="BEAVRS",
    nb_threads=20,
    discard=50,
    bundle_size=100,
)
```

```ipython3
tracking = tripoli5.simulation.TrackingBuilder().catchExceptions(True).build()
```

Simulation is defined and executed

```ipython3
simu = (
    tripoli5.simulation.SimulationBuilder(
        simulation_mode="criticality", parallelism_type="openmp"
    )
    .withParticleTracking("neutron", tracking)
    .withSource(src)
    .withGeometry(geometry)
    .withMedia("Neutron", media)
    .withParameters(param)
    .withScores(score_mgr)
    .build()
)
simu.run()
```

```

[2026-03-11 17:11:35.650] [info] *** Beginning of simulation ***
[2026-03-11 17:11:35.745] [info] Cycle: 1 of 170
[2026-03-11 17:11:38.899] [info]   kstep = 0.60200
[2026-03-11 17:11:38.900] [info]   Mean number of collisions: 47.7628
[2026-03-11 17:11:38.901] [info] Cycle: 2 of 170
[2026-03-11 17:11:41.292] [info]   kstep = 0.96120
[2026-03-11 17:11:41.293] [info]   Mean number of collisions: 35.0837
[2026-03-11 17:11:41.294] [info] Cycle: 3 of 170
[2026-03-11 17:11:43.635] [info]   kstep = 0.98780
[2026-03-11 17:11:43.636] [info]   Mean number of collisions: 34.6221
[2026-03-11 17:11:43.637] [info] Cycle: 4 of 170
[2026-03-11 17:11:45.965] [info]   kstep = 0.97315
[2026-03-11 17:11:45.966] [info]   Mean number of collisions: 34.1108
[2026-03-11 17:11:45.967] [info] Cycle: 5 of 170
[2026-03-11 17:11:48.266] [info]   kstep = 0.98655
[2026-03-11 17:11:48.268] [info]   Mean number of collisions: 33.9610
[2026-03-11 17:11:48.269] [info] Cycle: 6 of 170
[2026-03-11 17:11:50.611] [info]   kstep = 1.00320
[2026-03-11 17:11:50.613] [info]   Mean number of collisions: 33.9780
… [482 lines of output omitted] …
[2026-03-11 17:17:48.607] [info]   Mean number of collisions: 33.6486
[2026-03-11 17:17:48.608] [info] Cycle: 168 of 170
[2026-03-11 17:17:50.851] [info]   kstep = 1.00195
[2026-03-11 17:17:50.853] [info]   Mean number of collisions: 33.7181
[2026-03-11 17:17:50.854] [info] Cycle: 169 of 170
[2026-03-11 17:17:53.045] [info]   kstep = 1.02495
[2026-03-11 17:17:53.046] [info]   Mean number of collisions: 33.6291
[2026-03-11 17:17:53.047] [info] Cycle: 170 of 170
[2026-03-11 17:17:55.236] [info]   kstep = 0.99600
[2026-03-11 17:17:55.237] [info]   Mean number of collisions: 33.5721
```

Then we extract the \(k_{eff}\) and plot the energy resolved flux.

```ipython3
import numpy as np
import json

with open("references.json") as f:
    codes_results = json.load(f)
T4 = codes_results["TRIPOLI-4"]
OpenMC = codes_results["OpenMC"]

k_step = simu.getKStep()
mean = k_step.mean[0]
std = np.sqrt(k_step.var)[0]
print(f"TRIPOLI-5 k-eff: {mean:.5f} ± {std:.5f}")
print(f"TRIPOLI-4 k-eff: {T4['keff'][0]:.5f} ± {T4['keff'][1]:.5f}")
print(f"OpenMC    k-eff: {OpenMC['keff'][0]:.5f} ± {OpenMC['keff'][1]:.5f}")
```

```

TRIPOLI-5 k-eff: 0.99979 ± 0.00076
TRIPOLI-4 k-eff: 1.00044 ± 0.00006
OpenMC    k-eff: 0.99958 ± 0.00003
```

```ipython3
import matplotlib.pyplot as plt

# Plot the mean flux spectrum per unit lethargy for each volumes
for flux, label in zip(
    (flux_spect_general.mean, T4["flux"][0], OpenMC["flux"][0]),
    ("TRIPOLI-5", "TRIPOLI-4", "OpenMC"),
):
    flux_normalized = flux / np.sum(flux)
    flux_per_lethargy = flux_normalized / np.ediff1d(np.log(mesh_281g))
    plt.plot(
        mesh_281g[:-1],
        flux_per_lethargy,
        linestyle="-",
        linewidth=0.7,
        drawstyle="steps-post",
        label=label,
    )
plt.xlabel("Energy (MeV)")
plt.ylabel("Flux per unit lethargy")
plt.xscale("log")
plt.yscale("log")
_ = plt.legend()
```

![figure](https://tripoli5.asnr.dev/documentation/latest-release/_images/validation_criticality_beavrs_beavrs_19_0.png)
