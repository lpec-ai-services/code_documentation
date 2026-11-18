<!-- source: https://tripoli5.asnr.dev/documentation/latest-release/examples/features/simulation.html -->

# Simulation

The `Simulation` class is the centerpiece of most TRIPOLI-5 calculations. It collects and coordinates all the necessary parameters and information, which makes it a rather complex object. For this reason, TRIPOLI-5 provides a `SimulationBuilder` class that helps the user construct their `Simulation` object.

The purpose of this notebook is to illustrate the different options available in `SimulationBuilder`. For this purpose, we will concentrate on a simple use case: a uniform box. We start with a few imports:

```ipython3
from tripoli5.core.euclide import Point
from tripoli5.core.literals import K, MeV
import tripoli5
```

There are many cases where you might wish to preserve the output logged to the terminal by TRIPOLI-5 in a separate text file. You can tell TRIPOLI-5 to wirte all logged information to both the terminal (or Jupyter notebook) and a user specified file:

```ipython3
tripoli5.core.set_output_file("simulation_output.txt")
```

Now, all of the logged output can be examined from this file.

## The system

We set up a few important objects, such as the [geometry](agora_geometry.md), the [materials](materials_compositions.md), the [scores](score.md), and the [source](source.md). We will not discuss this part in detail; take a look at the other notebooks if want to learn more.

### Mixtures

```ipython3
catalog = tripoli5.delos.Catalog.fromFile(
    f"/opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/endfb8r0_mcnp_v{tripoli5.delos.CATALOG_VERSION}.yaml"
)

uranium_mix = (
    tripoli5.materials.MixtureBuilder("concentrations")
    .withName("uranium")
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

[2026-06-05 13:02:18.099] [info] Loading catalog from file: /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/endfb8r0_mcnp_v2.3.0.yaml
[2026-06-05 13:02:18.130] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/mass/njoy_ace/v0.2.0/archive/wrapped_mass_data.bin
```

### Geometry

```ipython3
# define the dimensions
side = 15

# planes
plane_xmin = tripoli5.agora.XPlane(-0.5 * side, label="plane_xmin")
plane_xmax = tripoli5.agora.XPlane(0.5 * side, label="plane_xmax")
plane_ymin = tripoli5.agora.YPlane(-0.5 * side, label="plane_ymin")
plane_ymax = tripoli5.agora.YPlane(0.5 * side, label="plane_ymax")
plane_zmin = tripoli5.agora.ZPlane(-0.5 * side, label="plane_zmin")
plane_zmax = tripoli5.agora.ZPlane(0.5 * side, label="plane_zmax")

# shapes
box_region = (
    plane_xmin & -plane_xmax & plane_ymin & -plane_ymax & plane_zmin & -plane_zmax
)
box_shape = tripoli5.agora.Shape(box_region)

# volumes
box_volume = tripoli5.agora.Volume(box_shape, "uranium", label="box")

root_universe = tripoli5.agora.Universe([box_volume])
bcs = tripoli5.agora.BoundaryConditions()
for p in [plane_xmin, plane_xmax, plane_ymin, plane_ymax, plane_zmin, plane_zmax]:
    bcs.add(p, tripoli5.agora.LeakageBoundaryCondition())
geometry = tripoli5.agora.Geometry(root_universe, bcs)
```

### Media

```ipython3
media = (
    tripoli5.materials.NeutronMediumBuilder()
    .withCatalog(catalog)
    .withMixtures([uranium_mix])
    .build()
)
```

```

[2026-06-05 13:02:18.153] [info] Building U234 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-06-05 13:02:18.157] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U234.294.bin
[2026-06-05 13:02:18.179] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/urr/njoy_ace/v0.4.0/dir/U234.294.urr.ace.bin
[2026-06-05 13:02:18.183] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-06-05 13:02:18.184] [info]   Building reaction MTs = 20, 79, 21, 80, 66, 37, 51, 70, 71, 72, 74, 77, 73, 102, 89, 91, 67, 38, 90, 88, 87, 57, 86, 58, 54, 83, 60, 2, 61, 62, 63, 64, 65, 55, 84, 68, 56, 85, 69, 59, 53, 82, 16, 75, 17, 76, 19, 78, 81, 52
[2026-06-05 13:02:18.185] [info] Building U235 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-06-05 13:02:18.187] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U235.294.bin
[2026-06-05 13:02:18.287] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/urr/njoy_ace/v0.4.0/dir/U235.294.urr.ace.bin
[2026-06-05 13:02:18.291] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-06-05 13:02:18.292] [info]   Building reaction MTs = 814, 52, 813, 51, 818, 56, 76, 17, 817, 55, 75, 16, 77, 18, 816, 54, 72, 834, 815, 53, 822, 60, 821, 59, 5, 74, 82, 83, 84, 85, 86, 87, 81, 806, 91, 80, 805, 79, 804, 68, 830, 835, 73, 102, 810, 2, 89, 78, 803, 88, 802, 801, 800, 63, 825, 64, 826, 649, 65, 827, 828, 66, 67, 829, 61, 823, 831, 69, 812, 833, 71, 811, 62, 824, 832, 70, 809, 808, 807, 58, 820, 57, 819
[2026-06-05 13:02:18.293] [info] Building U236 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-06-05 13:02:18.295] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U236.294.bin
[2026-06-05 13:02:18.309] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/urr/njoy_ace/v0.4.0/dir/U236.294.urr.ace.bin
[2026-06-05 13:02:18.313] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-06-05 13:02:18.314] [info]   Building reaction MTs = 20, 79, 21, 80, 66, 37, 51, 70, 71, 72, 74, 77, 73, 102, 89, 91, 67, 38, 90, 88, 87, 57, 86, 58, 54, 83, 60, 2, 61, 62, 63, 64, 65, 55, 84, 68, 56, 85, 69, 59, 53, 82, 16, 75, 17, 76, 19, 78, 81, 52
[2026-06-05 13:02:18.315] [info] Building U238 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-06-05 13:02:18.316] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U238.294.bin
[2026-06-05 13:02:18.407] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/urr/njoy_ace/v0.4.0/dir/U238.294.urr.ace.bin
[2026-06-05 13:02:18.411] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-06-05 13:02:18.412] [info]   Building reaction MTs = 77, 18, 76, 17, 79, 51, 80, 52, 81, 82, 75, 16, 800, 56, 85, 78, 74, 73, 102, 62, 91, 65, 66, 61, 2, 60, 89, 67, 68, 69, 64, 5, 63, 70, 58, 87, 71, 57, 86, 649, 59, 88, 53, 72, 54, 83, 84, 55
```

### Scores

```ipython3
flux = tripoli5.score.FluxSpectrumCollGeneral(
    [1e-11, 0.625e-6, 20.0], "FluxSpectrumCollGeneral"
)

score_mgr = tripoli5.score.ScoreManager("box")
score_mgr.addScore(flux)
score_mgr.initialize("")
```

### Source

```ipython3
src = tripoli5.source.FactorizedSource(
    tripoli5.distributions.spatial.PointDistribution(Point(1.0, 1.0, 1.0)),
    tripoli5.distributions.energy.MonoKinetic(2.0 * MeV),
    tripoli5.distributions.angular.IsotropicAngularDistribution(),
    1.0,  # norm
)
```

## Simulation parameters

The most important simulation parameters, such as the number of particles and the number of cycles, are stored in a `SimulationParameters` object. It is relatively straightforward:

```ipython3
param = tripoli5.simulation.SimulationParameters(
    nb_cycles=10,
    nb_events=1000,
    name="box",
)
```

Here:

- `nb_cycles` is the total number of cycles (batches).
- `nb_events` is the number of events (source particles) per cycle.
- `name` is just a string that helps you identify the simulation.

### Advanced Simulation parameters

More advanced parameters can be controled using the simulation parameters.

- `bundle_size` : this integer controls the number of particle histories simulated between tallying events. Indeed, during the simulation, particle tracks are recorded and accumulated; after a certain number of histories, the scores consume the tracks and free up their memory. Smaller values of this parameter help with mitigating the memory occupation due to this strategy.
- `random_seed` : change the random seed of the simulation.

## The simulation builder

With all the setup out of the way, we can now turn to the `SimulationBuilder` class. Its idea is similar to other builder classes used by TRIPOLI-5: you start by creating a builder, you add options to it, and you call `.build()` at the end to retrieve a `Simulation` object. For example, here is a very simple fixed-source simulation, in mono-processor mode:

```ipython3
simu = (
    tripoli5.simulation.SimulationBuilder(
        simulation_mode="fixed_source", parallelism_type="mono"
    )
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

[2026-06-05 13:02:18.457] [info] *** Beginning of simulation ***
[2026-06-05 13:02:18.459] [info] Cycle: 1 of 10
[2026-06-05 13:02:18.556] [info] Cycle: 2 of 10
[2026-06-05 13:02:18.630] [info] Cycle: 3 of 10
[2026-06-05 13:02:18.703] [info] Cycle: 4 of 10
[2026-06-05 13:02:18.773] [info] Cycle: 5 of 10
[2026-06-05 13:02:18.848] [info] Cycle: 6 of 10
[2026-06-05 13:02:18.917] [info] Cycle: 7 of 10
[2026-06-05 13:02:18.985] [info] Cycle: 8 of 10
[2026-06-05 13:02:19.057] [info] Cycle: 9 of 10
[2026-06-05 13:02:19.140] [info] Cycle: 10 of 10
```

We can run the same simulation in parallel, in shared-memory mode, by changing the `parallelism_type` argument to `openmp`. We will also need to specify the number of threads to use via the `SimulationParameters` object:

```ipython3
param = tripoli5.simulation.SimulationParameters(
    nb_cycles=10,
    nb_events=1000,
    name="box",
    nb_threads=20,
)
simu = (
    tripoli5.simulation.SimulationBuilder(
        simulation_mode="fixed_source", parallelism_type="openmp"
    )
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

[2026-06-05 13:02:19.228] [info] *** Beginning of simulation ***
[2026-06-05 13:02:19.231] [info] Cycle: 1 of 10
[2026-06-05 13:02:19.269] [info] Cycle: 2 of 10
[2026-06-05 13:02:19.283] [info] Cycle: 3 of 10
[2026-06-05 13:02:19.297] [info] Cycle: 4 of 10
[2026-06-05 13:02:19.310] [info] Cycle: 5 of 10
[2026-06-05 13:02:19.323] [info] Cycle: 6 of 10
[2026-06-05 13:02:19.335] [info] Cycle: 7 of 10
[2026-06-05 13:02:19.349] [info] Cycle: 8 of 10
[2026-06-05 13:02:19.361] [info] Cycle: 9 of 10
[2026-06-05 13:02:19.374] [info] Cycle: 10 of 10
```

Much faster! Now let’s change the type of simulation to `criticality`. In criticality calculations, we probably also want to specify a certain number of inactive cycles, to allow the fission source to relax to its asymptotic distribution. In this example, we just use 10 inactive cycles and 20 active cycles:

```ipython3
param = tripoli5.simulation.SimulationParameters(
    nb_cycles=30,
    discard=10,
    nb_events=1000,
    name="box",
    nb_threads=20,
)
simu = (
    tripoli5.simulation.SimulationBuilder(
        simulation_mode="criticality", parallelism_type="openmp"
    )
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

[2026-06-05 13:02:19.401] [info] *** Beginning of simulation ***
[2026-06-05 13:02:19.404] [info] Cycle: 1 of 30
[2026-06-05 13:02:19.411] [info]   kstep = 0.59400
[2026-06-05 13:02:19.414] [info] Cycle: 2 of 30
[2026-06-05 13:02:19.421] [info]   kstep = 0.36600
[2026-06-05 13:02:19.422] [info] Cycle: 3 of 30
[2026-06-05 13:02:19.429] [info]   kstep = 0.34600
[2026-06-05 13:02:19.430] [info] Cycle: 4 of 30
[2026-06-05 13:02:19.437] [info]   kstep = 0.31800
[2026-06-05 13:02:19.438] [info] Cycle: 5 of 30
[2026-06-05 13:02:19.444] [info]   kstep = 0.35800
[2026-06-05 13:02:19.445] [info] Cycle: 6 of 30
[2026-06-05 13:02:19.452] [info]   kstep = 0.30000
[2026-06-05 13:02:19.457] [info] Cycle: 7 of 30
[2026-06-05 13:02:19.463] [info]   kstep = 0.36600
[2026-06-05 13:02:19.465] [info] Cycle: 8 of 30
[2026-06-05 13:02:19.471] [info]   kstep = 0.34800
[2026-06-05 13:02:19.473] [info] Cycle: 9 of 30
[2026-06-05 13:02:19.479] [info]   kstep = 0.36800
… [32 lines of output omitted] …
[2026-06-05 13:02:19.606] [info] Cycle: 26 of 30
[2026-06-05 13:02:19.612] [info]   kstep = 0.30100   kstep_avg = 0.31600 +/- 0.00881
[2026-06-05 13:02:19.613] [info] Cycle: 27 of 30
[2026-06-05 13:02:19.619] [info]   kstep = 0.37300   kstep_avg = 0.31935 +/- 0.00893
[2026-06-05 13:02:19.621] [info] Cycle: 28 of 30
[2026-06-05 13:02:19.627] [info]   kstep = 0.35000   kstep_avg = 0.32106 +/- 0.00859
[2026-06-05 13:02:19.629] [info] Cycle: 29 of 30
[2026-06-05 13:02:19.635] [info]   kstep = 0.34000   kstep_avg = 0.32205 +/- 0.00818
[2026-06-05 13:02:19.636] [info] Cycle: 30 of 30
[2026-06-05 13:02:19.642] [info]   kstep = 0.35600   kstep_avg = 0.32375 +/- 0.00795
```

Note that criticality simulation objects have a `KStep` score:

```ipython3
import math

kstep = simu.getKStep()
print(f"k_eff = {kstep.mean[0]:.5f} ± {math.sqrt(kstep.var[0]):.5f}")
```

```

k_eff = 0.32375 ± 0.00795
```

## Particle tracking

An important feature of the simulation builder is that it can be used to fine-tune the particle transport algorithm. Since particle tracking is also a complex beast, it has its own builder class! It is called `TrackingBuilder`.

First, let’s go back to the parameters for a small fixed-source simulation:

```ipython3
param = tripoli5.simulation.SimulationParameters(
    nb_cycles=10,
    nb_events=1000,
    name="box",
    nb_threads=20,
)
```

### Surface tracking and delta tracking

By default, *surface tracking* is used. In some situations, however, you may want to use *delta tracking* instead. Delta tracking is useful, in particular, when the cross section has a continuous dependence on the position, because of a continuous temperature or density field.

Let’s construct a particle tracking configuration that uses surface tracking:

```ipython3
surface_tracking = tripoli5.simulation.TrackingBuilder().build()
```

That was easy! Surface tracking does not have a lot of free parameters. We can pass the tracking configuration to the `SimulationBuilder` with the `withParticleTracking()` method. (Note that, in the following, we are not systematically running all the simulations.)

```ipython3
simu = (
    tripoli5.simulation.SimulationBuilder(
        simulation_mode="fixed_source", parallelism_type="openmp"
    )
    .withSource(src)
    .withGeometry(geometry)
    .withMedia("Neutron", media)
    .withParameters(param)
    .withScores(score_mgr)
    .withParticleTracking("neutron", surface_tracking)
    .build()
)
```

Delta tracking requires a bit more configuration. First, you have to decide what kind of majorant cross section you want to use. There are two options:

- `Global`: this corresponds to using a global majorant cross section value.
- `EnergyDependent`: unsurprisingly, this corresponds to an energy-dependent majorant cross section.

The `TrackingBuilder` tries to help with the calculation of the majorant cross section. Here is how it works:

```ipython3
global_delta_tracking = (
    tripoli5.simulation.TrackingBuilder(tripoli5.simulation.MajorantType.Global)
    .withMajorantParameters(media, tripoli5.simulation.MajorantExecutor.OpenMP)
    .build()
)
```

```

[2026-06-05 13:02:19.702] [info] Building majorant cross section...
[2026-06-05 13:02:19.714] [info] ... sorting the unionized grid...
[2026-06-05 13:02:19.731] [info] ... removing duplicate points from the grid...
[2026-06-05 13:02:19.734] [info] ... removing energies outside the simulation range...
[2026-06-05 13:02:19.736] [info] ... unionized grid has 270614 points...
[2026-06-05 13:02:20.390] [info] ... majorant cross section built!
```

In this example, a *global* majorant is computed, based on the media in our simulation. In case the media contain temperature or density fields, `TrackingBuilder` tries to maximize the total macroscopic cross section by taking the worst-case scenario of maximum density and minimum temperature everywhere. This works 95% of the time.

Since this calculation can be expensive, you can let `TrackingBuilder` know that you would like to run the calculation of the majorant in parallel, using `tripoli5.simulation.MajorantExecutor.OpenMP`.

Let’s try to use delta tracking in a simulation:

```ipython3
simu = (
    tripoli5.simulation.SimulationBuilder(
        simulation_mode="fixed_source", parallelism_type="openmp"
    )
    .withSource(src)
    .withGeometry(geometry)
    .withMedia("Neutron", media)
    .withParameters(param)
    .withScores(score_mgr)
    .withParticleTracking("neutron", global_delta_tracking)
    .build()
)
simu.run()
```

```

[2026-06-05 13:02:20.400] [info] *** Beginning of simulation ***
[2026-06-05 13:02:20.403] [info] Cycle: 1 of 10
[2026-06-05 13:02:21.475] [info] Cycle: 2 of 10
[2026-06-05 13:02:22.381] [info] Cycle: 3 of 10
[2026-06-05 13:02:23.398] [info] Cycle: 4 of 10
[2026-06-05 13:02:24.270] [info] Cycle: 5 of 10
[2026-06-05 13:02:25.088] [info] Cycle: 6 of 10
[2026-06-05 13:02:25.891] [info] Cycle: 7 of 10
[2026-06-05 13:02:26.683] [info] Cycle: 8 of 10
[2026-06-05 13:02:27.442] [info] Cycle: 9 of 10
[2026-06-05 13:02:28.339] [info] Cycle: 10 of 10
```

If you’re following along and running the cells as you go, you may have noticed that the calculation with delta tracking is much slower than surface tracking! That is usually the case, because particles make shorter flights on average in delta tracking.

Let’s try an energy-dependent majorant now:

```ipython3
edep_delta_tracking = (
    tripoli5.simulation.TrackingBuilder(
        tripoli5.simulation.MajorantType.EnergyDependent
    )
    .withMajorantParameters(media, tripoli5.simulation.MajorantExecutor.OpenMP)
    .withMajorantFudgeFactors([1e-11, 20.0], [1.1])
    .build()
)
```

```

[2026-06-05 13:02:29.177] [info] Building U234 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-06-05 13:02:29.183] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-06-05 13:02:29.184] [info]   Building reaction MTs = 20, 79, 21, 80, 66, 37, 51, 70, 71, 72, 74, 77, 73, 102, 89, 91, 67, 38, 90, 88, 87, 57, 86, 58, 54, 83, 60, 2, 61, 62, 63, 64, 65, 55, 84, 68, 56, 85, 69, 59, 53, 82, 16, 75, 17, 76, 19, 78, 81, 52
[2026-06-05 13:02:29.186] [info] Building U235 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-06-05 13:02:29.190] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-06-05 13:02:29.191] [info]   Building reaction MTs = 814, 52, 813, 51, 818, 56, 76, 17, 817, 55, 75, 16, 77, 18, 816, 54, 72, 834, 815, 53, 822, 60, 821, 59, 5, 74, 82, 83, 84, 85, 86, 87, 81, 806, 91, 80, 805, 79, 804, 68, 830, 835, 73, 102, 810, 2, 89, 78, 803, 88, 802, 801, 800, 63, 825, 64, 826, 649, 65, 827, 828, 66, 67, 829, 61, 823, 831, 69, 812, 833, 71, 811, 62, 824, 832, 70, 809, 808, 807, 58, 820, 57, 819
[2026-06-05 13:02:29.192] [info] Building U236 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-06-05 13:02:29.195] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-06-05 13:02:29.196] [info]   Building reaction MTs = 20, 79, 21, 80, 66, 37, 51, 70, 71, 72, 74, 77, 73, 102, 89, 91, 67, 38, 90, 88, 87, 57, 86, 58, 54, 83, 60, 2, 61, 62, 63, 64, 65, 55, 84, 68, 56, 85, 69, 59, 53, 82, 16, 75, 17, 76, 19, 78, 81, 52
[2026-06-05 13:02:29.197] [info] Building U238 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-06-05 13:02:29.200] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-06-05 13:02:29.201] [info]   Building reaction MTs = 77, 18, 76, 17, 79, 51, 80, 52, 81, 82, 75, 16, 800, 56, 85, 78, 74, 73, 102, 62, 91, 65, 66, 61, 2, 60, 89, 67, 68, 69, 64, 5, 63, 70, 58, 87, 71, 57, 86, 649, 59, 88, 53, 72, 54, 83, 84, 55
[2026-06-05 13:02:29.202] [info] Building majorant cross section...
[2026-06-05 13:02:29.209] [info] ... sorting the unionized grid...
[2026-06-05 13:02:29.235] [info] ... removing duplicate points from the grid...
[2026-06-05 13:02:29.237] [info] ... removing energies outside the simulation range...
[2026-06-05 13:02:29.239] [info] ... unionized grid has 270614 points...
[2026-06-05 13:02:29.313] [info] ... majorant cross section built!
```

```ipython3
simu = (
    tripoli5.simulation.SimulationBuilder(
        simulation_mode="fixed_source", parallelism_type="openmp"
    )
    .withSource(src)
    .withGeometry(geometry)
    .withMedia("Neutron", media)
    .withParameters(param)
    .withScores(score_mgr)
    .withParticleTracking("neutron", edep_delta_tracking)
    .build()
)
simu.run()
```

```

[2026-06-05 13:02:29.335] [info] *** Beginning of simulation ***
[2026-06-05 13:02:29.336] [info] Cycle: 1 of 10
[2026-06-05 13:02:29.366] [info] Cycle: 2 of 10
[2026-06-05 13:02:29.387] [info] Cycle: 3 of 10
[2026-06-05 13:02:29.404] [info] Cycle: 4 of 10
[2026-06-05 13:02:29.418] [info] Cycle: 5 of 10
[2026-06-05 13:02:29.432] [info] Cycle: 6 of 10
[2026-06-05 13:02:29.446] [info] Cycle: 7 of 10
[2026-06-05 13:02:29.460] [info] Cycle: 8 of 10
[2026-06-05 13:02:29.476] [info] Cycle: 9 of 10
[2026-06-05 13:02:29.490] [info] Cycle: 10 of 10
```

This is fast again! We had to take some safety margins, though: the fudge factor of 1.1 means that `TrackingBuilder` will try to compute the optimal majorant cross section, but multiply it by 1.1 between \(10^{-11}\) and \(20\) MeV. A small fudge factor is usually necessary when working with energy-dependent majorants.

### Collision Sampling Algorithm

All the examples shown above use analog sampling (see the options of the defined media).

Let’s take a look at how to build a surface tracking object with *nuclide-wise implicit capture*. However, by applying implicit capture (or branchless), particles may become immortal, as the capture channels cannot be sampled. Thus, it forces us to apply population control. Here is how it may be defined:

```ipython3
implicit_capture_media = (
    tripoli5.materials.NeutronMediumBuilder()
    .withCatalog(catalog)
    .withMixtures([uranium_mix])
    .withCollisionSampler("implicit_capture")
    .build()
)
implicit_capture_tracking = (
    tripoli5.simulation.TrackingBuilder().withPopulationControl().build()
)
```

```

[2026-06-05 13:02:29.511] [info] Building U234 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-06-05 13:02:29.514] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U234.294.bin
[2026-06-05 13:02:29.528] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/urr/njoy_ace/v0.4.0/dir/U234.294.urr.ace.bin
[2026-06-05 13:02:29.531] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-06-05 13:02:29.532] [info]   Building reaction MTs = 20, 79, 21, 80, 66, 37, 51, 70, 71, 72, 74, 77, 73, 102, 89, 91, 67, 38, 90, 88, 87, 57, 86, 58, 54, 83, 60, 2, 61, 62, 63, 64, 65, 55, 84, 68, 56, 85, 69, 59, 53, 82, 16, 75, 17, 76, 19, 78, 81, 52
[2026-06-05 13:02:29.532] [info] Building U235 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-06-05 13:02:29.536] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U235.294.bin
[2026-06-05 13:02:29.626] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/urr/njoy_ace/v0.4.0/dir/U235.294.urr.ace.bin
[2026-06-05 13:02:29.629] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-06-05 13:02:29.629] [info]   Building reaction MTs = 814, 52, 813, 51, 818, 56, 76, 17, 817, 55, 75, 16, 77, 18, 816, 54, 72, 834, 815, 53, 822, 60, 821, 59, 5, 74, 82, 83, 84, 85, 86, 87, 81, 806, 91, 80, 805, 79, 804, 68, 830, 835, 73, 102, 810, 2, 89, 78, 803, 88, 802, 801, 800, 63, 825, 64, 826, 649, 65, 827, 828, 66, 67, 829, 61, 823, 831, 69, 812, 833, 71, 811, 62, 824, 832, 70, 809, 808, 807, 58, 820, 57, 819
[2026-06-05 13:02:29.630] [info] Building U236 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-06-05 13:02:29.632] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U236.294.bin
[2026-06-05 13:02:29.646] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/urr/njoy_ace/v0.4.0/dir/U236.294.urr.ace.bin
[2026-06-05 13:02:29.650] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-06-05 13:02:29.651] [info]   Building reaction MTs = 20, 79, 21, 80, 66, 37, 51, 70, 71, 72, 74, 77, 73, 102, 89, 91, 67, 38, 90, 88, 87, 57, 86, 58, 54, 83, 60, 2, 61, 62, 63, 64, 65, 55, 84, 68, 56, 85, 69, 59, 53, 82, 16, 75, 17, 76, 19, 78, 81, 52
[2026-06-05 13:02:29.651] [info] Building U238 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-06-05 13:02:29.655] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U238.294.bin
[2026-06-05 13:02:29.745] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/urr/njoy_ace/v0.4.0/dir/U238.294.urr.ace.bin
[2026-06-05 13:02:29.749] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-06-05 13:02:29.749] [info]   Building reaction MTs = 77, 18, 76, 17, 79, 51, 80, 52, 81, 82, 75, 16, 800, 56, 85, 78, 74, 73, 102, 62, 91, 65, 66, 61, 2, 60, 89, 67, 68, 69, 64, 5, 63, 70, 58, 87, 71, 57, 86, 649, 59, 88, 53, 72, 54, 83, 84, 55
```

Then we can run the simulation

```ipython3
simu = (
    tripoli5.simulation.SimulationBuilder(
        simulation_mode="fixed_source", parallelism_type="openmp"
    )
    .withSource(src)
    .withGeometry(geometry)
    .withMedia("Neutron", implicit_capture_media)
    .withParameters(param)
    .withScores(score_mgr)
    .withParticleTracking("neutron", implicit_capture_tracking)
    .build()
)
simu.run()
```

```

[2026-06-05 13:02:29.762] [info] *** Beginning of simulation ***
[2026-06-05 13:02:29.763] [info] Cycle: 1 of 10
[2026-06-05 13:02:29.798] [info] Cycle: 2 of 10
[2026-06-05 13:02:29.816] [info] Cycle: 3 of 10
[2026-06-05 13:02:29.834] [info] Cycle: 4 of 10
[2026-06-05 13:02:29.867] [info] Cycle: 5 of 10
[2026-06-05 13:02:29.890] [info] Cycle: 6 of 10
[2026-06-05 13:02:29.909] [info] Cycle: 7 of 10
[2026-06-05 13:02:29.925] [info] Cycle: 8 of 10
[2026-06-05 13:02:29.943] [info] Cycle: 9 of 10
[2026-06-05 13:02:29.961] [info] Cycle: 10 of 10
```

Selecting the branchless mode can be performed as follows:

```ipython3
branchless_media = (
    tripoli5.materials.NeutronMediumBuilder()
    .withCatalog(catalog)
    .withMixtures([uranium_mix])
    .withCollisionSampler("branchless")
    .build()
)
branchless_tracking = (
    tripoli5.simulation.TrackingBuilder().withPopulationControl().build()
)
simu = (
    tripoli5.simulation.SimulationBuilder(
        simulation_mode="fixed_source", parallelism_type="openmp"
    )
    .withSource(src)
    .withGeometry(geometry)
    .withMedia("Neutron", branchless_media)
    .withParameters(param)
    .withScores(score_mgr)
    .withParticleTracking("neutron", branchless_tracking)
    .build()
)
simu.run()
```

```

[2026-06-05 13:02:29.985] [info] Building U234 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-06-05 13:02:29.988] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U234.294.bin
[2026-06-05 13:02:30.003] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/urr/njoy_ace/v0.4.0/dir/U234.294.urr.ace.bin
[2026-06-05 13:02:30.006] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-06-05 13:02:30.006] [info]   Building reaction MTs = 20, 79, 21, 80, 66, 37, 51, 70, 71, 72, 74, 77, 73, 102, 89, 91, 67, 38, 90, 88, 87, 57, 86, 58, 54, 83, 60, 2, 61, 62, 63, 64, 65, 55, 84, 68, 56, 85, 69, 59, 53, 82, 16, 75, 17, 76, 19, 78, 81, 52
[2026-06-05 13:02:30.007] [info] Building U235 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-06-05 13:02:30.010] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U235.294.bin
[2026-06-05 13:02:30.099] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/urr/njoy_ace/v0.4.0/dir/U235.294.urr.ace.bin
[2026-06-05 13:02:30.103] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-06-05 13:02:30.103] [info]   Building reaction MTs = 814, 52, 813, 51, 818, 56, 76, 17, 817, 55, 75, 16, 77, 18, 816, 54, 72, 834, 815, 53, 822, 60, 821, 59, 5, 74, 82, 83, 84, 85, 86, 87, 81, 806, 91, 80, 805, 79, 804, 68, 830, 835, 73, 102, 810, 2, 89, 78, 803, 88, 802, 801, 800, 63, 825, 64, 826, 649, 65, 827, 828, 66, 67, 829, 61, 823, 831, 69, 812, 833, 71, 811, 62, 824, 832, 70, 809, 808, 807, 58, 820, 57, 819
[2026-06-05 13:02:30.104] [info] Building U236 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-06-05 13:02:30.108] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U236.294.bin
[2026-06-05 13:02:30.123] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/urr/njoy_ace/v0.4.0/dir/U236.294.urr.ace.bin
[2026-06-05 13:02:30.126] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-06-05 13:02:30.126] [info]   Building reaction MTs = 20, 79, 21, 80, 66, 37, 51, 70, 71, 72, 74, 77, 73, 102, 89, 91, 67, 38, 90, 88, 87, 57, 86, 58, 54, 83, 60, 2, 61, 62, 63, 64, 65, 55, 84, 68, 56, 85, 69, 59, 53, 82, 16, 75, 17, 76, 19, 78, 81, 52
[2026-06-05 13:02:30.127] [info] Building U238 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-06-05 13:02:30.130] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/U238.294.bin
[2026-06-05 13:02:30.220] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/urr/njoy_ace/v0.4.0/dir/U238.294.urr.ace.bin
[2026-06-05 13:02:30.224] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-06-05 13:02:30.224] [info]   Building reaction MTs = 77, 18, 76, 17, 79, 51, 80, 52, 81, 82, 75, 16, 800, 56, 85, 78, 74, 73, 102, 62, 91, 65, 66, 61, 2, 60, 89, 67, 68, 69, 64, 5, 63, 70, 58, 87, 71, 57, 86, 649, 59, 88, 53, 72, 54, 83, 84, 55
[2026-06-05 13:02:30.229] [info] *** Beginning of simulation ***
[2026-06-05 13:02:30.230] [info] Cycle: 1 of 10
[2026-06-05 13:02:30.262] [info] Cycle: 2 of 10
[2026-06-05 13:02:30.282] [info] Cycle: 3 of 10
[2026-06-05 13:02:30.300] [info] Cycle: 4 of 10
[2026-06-05 13:02:30.317] [info] Cycle: 5 of 10
[2026-06-05 13:02:30.336] [info] Cycle: 6 of 10
[2026-06-05 13:02:30.354] [info] Cycle: 7 of 10
[2026-06-05 13:02:30.373] [info] Cycle: 8 of 10
[2026-06-05 13:02:30.392] [info] Cycle: 9 of 10
[2026-06-05 13:02:30.409] [info] Cycle: 10 of 10
```

### Population control parameters

Population control has the following parameters:

- `roulette_threshold`: threshold below which Russian roulette is applied (default = 0.25)
- `roulette_survival_weight`: weight of particle surviving the Russian roulette (default = 1.0)
- `splitting_threshold`: threshold above which splitting is applied (default = 4.0)
- `splitting_target_weight`: average weight of particles after splitting (default = 1.0)

However roulette and splitting parameters can be specified as below:

```ipython3
pop_control_tracking = (
    tripoli5.simulation.TrackingBuilder()
    .withPopulationControl(
        roulette_threshold=0.1,
        roulette_survival_weight=0.2,
        splitting_threshold=10,
        splitting_target_weight=1.0,
    )
    .build()
)
simu = (
    tripoli5.simulation.SimulationBuilder(
        simulation_mode="fixed_source", parallelism_type="openmp"
    )
    .withSource(src)
    .withGeometry(geometry)
    .withMedia("Neutron", implicit_capture_media)
    .withParameters(param)
    .withScores(score_mgr)
    .withParticleTracking("neutron", pop_control_tracking)
    .build()
)
simu.run()
```

```

[2026-06-05 13:02:30.438] [info] *** Beginning of simulation ***
[2026-06-05 13:02:30.438] [info] Cycle: 1 of 10
[2026-06-05 13:02:30.456] [info] Cycle: 2 of 10
[2026-06-05 13:02:30.472] [info] Cycle: 3 of 10
[2026-06-05 13:02:30.487] [info] Cycle: 4 of 10
[2026-06-05 13:02:30.503] [info] Cycle: 5 of 10
[2026-06-05 13:02:30.519] [info] Cycle: 6 of 10
[2026-06-05 13:02:30.535] [info] Cycle: 7 of 10
[2026-06-05 13:02:30.551] [info] Cycle: 8 of 10
[2026-06-05 13:02:30.567] [info] Cycle: 9 of 10
[2026-06-05 13:02:30.583] [info] Cycle: 10 of 10
```

### Advanced parameters

There are a few more advanced tracking parameters that you may want to play around with, especially in very large calculations. One of them is `catchExceptions()`, which tells particle tracking to keep going, even in the presence of errors during transport. For example, let’s take the previous energy-dependent simulation. Note the very small number of particles!

```ipython3
param = tripoli5.simulation.SimulationParameters(
    nb_cycles=1,
    nb_events=10,
    name="box",
)

edep_delta_tracking = (
    tripoli5.simulation.TrackingBuilder(
        tripoli5.simulation.MajorantType.EnergyDependent
    )
    .withMajorantParameters(media, tripoli5.simulation.MajorantExecutor.OpenMP)
    .catchExceptions(True)
    .build()
)
```

```

[2026-06-05 13:02:30.607] [info] Building U234 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-06-05 13:02:30.611] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-06-05 13:02:30.612] [info]   Building reaction MTs = 20, 79, 21, 80, 66, 37, 51, 70, 71, 72, 74, 77, 73, 102, 89, 91, 67, 38, 90, 88, 87, 57, 86, 58, 54, 83, 60, 2, 61, 62, 63, 64, 65, 55, 84, 68, 56, 85, 69, 59, 53, 82, 16, 75, 17, 76, 19, 78, 81, 52
[2026-06-05 13:02:30.612] [info] Building U235 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-06-05 13:02:30.620] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-06-05 13:02:30.621] [info]   Building reaction MTs = 814, 52, 813, 51, 818, 56, 76, 17, 817, 55, 75, 16, 77, 18, 816, 54, 72, 834, 815, 53, 822, 60, 821, 59, 5, 74, 82, 83, 84, 85, 86, 87, 81, 806, 91, 80, 805, 79, 804, 68, 830, 835, 73, 102, 810, 2, 89, 78, 803, 88, 802, 801, 800, 63, 825, 64, 826, 649, 65, 827, 828, 66, 67, 829, 61, 823, 831, 69, 812, 833, 71, 811, 62, 824, 832, 70, 809, 808, 807, 58, 820, 57, 819
[2026-06-05 13:02:30.621] [info] Building U236 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-06-05 13:02:30.625] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-06-05 13:02:30.626] [info]   Building reaction MTs = 20, 79, 21, 80, 66, 37, 51, 70, 71, 72, 74, 77, 73, 102, 89, 91, 67, 38, 90, 88, 87, 57, 86, 58, 54, 83, 60, 2, 61, 62, 63, 64, 65, 55, 84, 68, 56, 85, 69, 59, 53, 82, 16, 75, 17, 76, 19, 78, 81, 52
[2026-06-05 13:02:30.626] [info] Building U238 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-06-05 13:02:30.632] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-06-05 13:02:30.634] [info]   Building reaction MTs = 77, 18, 76, 17, 79, 51, 80, 52, 81, 82, 75, 16, 800, 56, 85, 78, 74, 73, 102, 62, 91, 65, 66, 61, 2, 60, 89, 67, 68, 69, 64, 5, 63, 70, 58, 87, 71, 57, 86, 649, 59, 88, 53, 72, 54, 83, 84, 55
[2026-06-05 13:02:30.634] [info] Building majorant cross section...
[2026-06-05 13:02:30.641] [info] ... sorting the unionized grid...
[2026-06-05 13:02:30.650] [info] ... removing duplicate points from the grid...
[2026-06-05 13:02:30.651] [info] ... removing energies outside the simulation range...
[2026-06-05 13:02:30.653] [info] ... unionized grid has 270614 points...
[2026-06-05 13:02:30.708] [info] ... majorant cross section built!
```

```ipython3
simu = (
    tripoli5.simulation.SimulationBuilder(
        simulation_mode="fixed_source", parallelism_type="mono"
    )
    .withSource(src)
    .withGeometry(geometry)
    .withMedia("Neutron", media)
    .withParameters(param)
    .withScores(score_mgr)
    .withParticleTracking("neutron", edep_delta_tracking)
    .build()
)
simu.run()
```

```

[2026-06-05 13:02:30.719] [info] *** Beginning of simulation ***
[2026-06-05 13:02:30.720] [info] Cycle: 1 of 1
[2026-06-05 13:02:30.723] [error] Exception raised during transport. The particle will be killed. Exception: Could not evaluate collision at energy 0.819575531318989 [MeV]
Method: particleCollisionStep, File: /builds/tripoli-5/tripoli-5/PATMOS/src/simulation/deltaparticletracking.cxx, Line: 224
[2026-06-05 13:02:30.724] [error] Exception raised during transport. The particle will be killed. Exception: Could not evaluate collision at energy 1.9982797918792201 [MeV]
Method: particleCollisionStep, File: /builds/tripoli-5/tripoli-5/PATMOS/src/simulation/deltaparticletracking.cxx, Line: 224
[2026-06-05 13:02:30.725] [error] Exception raised during transport. The particle will be killed. Exception: Could not evaluate collision at energy 1.994084026223577 [MeV]
Method: particleCollisionStep, File: /builds/tripoli-5/tripoli-5/PATMOS/src/simulation/deltaparticletracking.cxx, Line: 224
[2026-06-05 13:02:30.726] [error] Exception raised during transport. The particle will be killed. Exception: Could not evaluate collision at energy 1.9336711527119586 [MeV]
Method: particleCollisionStep, File: /builds/tripoli-5/tripoli-5/PATMOS/src/simulation/deltaparticletracking.cxx, Line: 224
[2026-06-05 13:02:30.726] [error] Exception raised during transport. The particle will be killed. Exception: Could not evaluate collision at energy 0.9410582500184707 [MeV]
Method: particleCollisionStep, File: /builds/tripoli-5/tripoli-5/PATMOS/src/simulation/deltaparticletracking.cxx, Line: 224
[2026-06-05 13:02:30.727] [error] Exception raised during transport. The particle will be killed. Exception: Could not evaluate collision at energy 1.8448143277616609 [MeV]
Method: particleCollisionStep, File: /builds/tripoli-5/tripoli-5/PATMOS/src/simulation/deltaparticletracking.cxx, Line: 224
[2026-06-05 13:02:30.728] [error] Exception raised during transport. The particle will be killed. Exception: Could not evaluate collision at energy 3.1128570967679137 [MeV]
Method: particleCollisionStep, File: /builds/tripoli-5/tripoli-5/PATMOS/src/simulation/deltaparticletracking.cxx, Line: 224
[2026-06-05 13:02:30.728] [error] Exception raised during transport. The particle will be killed. Exception: Could not evaluate collision at energy 0.3666569074141357 [MeV]
Method: particleCollisionStep, File: /builds/tripoli-5/tripoli-5/PATMOS/src/simulation/deltaparticletracking.cxx, Line: 224
```

As you can see, some errors were generated, but the simulation kept running and just discarded the problematic particles. This can be useful for very long running simulations, which run the risk of hitting a rare bug. You don’t want your massively parallel simulation to die because one particle out of \(10^{12}\) ran into some weird edge case.
