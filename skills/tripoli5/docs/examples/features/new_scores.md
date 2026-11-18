<!-- source: https://tripoli5.asnr.dev/documentation/latest-release/examples/features/new_scores.html -->

# Scores

In Monte-Carlo particle transport simulations, a score is a computed quantity that provides information about the behavior of particles within the simulation. Scores are used to analyze various aspects of particle transport, such as flux, reaction rates, k-effective, and more.

The `tripoli5.future_score` module is a submodule of Tripoli-5, serving as the main entry point for defining and managing scores within the `simulation`. This module allows you to declare the scores you want to compute, manage them during the simulation, and retrieve the results after the simulation is complete.

## Types of Scores

The `tripoli5.future_score` module provides a variety objects to build your own scores, to compute specific quantities of interest. Below is an overview of the different classes available in this module.

1. **Detector**: the main class to compute a set of quantitites (called **responses**) sharing the same set of binning/filters/estimator. You can have multiple detector per simulation.

   - `Detector`: if you want to retrieve statistical moments of your scores (average, variance, third and fourth moments and derived quantities, see the [theory section](https://tripoli5.asnr.dev/documentation/latest-release/theory/scores/computing_moments.html) for more information).
   - `DistributionDetector`: if you want to retrieve the entire sample for each response of that detector (e.g., the \(k_\text{eff}\) per batch).
2. **Filters**: objects to filter and/or order events that will contribute to your score and/or in which bin of a mesh/grid they contribute. You can have multiple filters per detector, the whole list being applied sequentially to the events that may contribute to the scores defined by the detector (e.g., if you have an `IncidentEnergy` and a spatial mesh filter, you end up with a 4-dimensional binning for the resulting score). The following objetcs are part of the `filters` submodule:

   - `filters.IncidentEnergy`: filter and order the results on an energy grid (e.g., to be used to compute spectra)
   - `filters.Materials`: filter according to material names. Each material or union of materials leads to a dedicated bin in this filter dimension.
   - `filters.Volumes`: filter according to volume names. Each volume or union of volumes leads to a dedicated bin in this filter dimension.
3. **Responses**: the quantities you want your detector to compute. You can have multiple responses per detector, each response is applied independently of the others. The following objects are part of the `responses` submodule:

   - `responses.Flux`: the neutron flux
   - `responses.ReactionRates`: MT reaction rates

Scores are computed using different types of estimators, which are methods for calculating the quantities of interest. The estimators include:

- **Track Estimator**: Integrates contributions along the particle’s flight.
- **Collision Estimator**: Sums contributions at collision points.

We will describe the various score with an example configuration.

## Setting up a Configuration

In this example, we will use the [Jezebel](../criticality/Jezebel.md) configuration consisting of a sphere. The sphere has been artificially divided into two spherical shells (an inner and an outer shell) leading to two volumes: one inner shell and one outer shell (labeled “pu_inner” and “pu_outer”) with leakage boundary conditions. The material composition is a highly enriched Plutonium (Pu). See the following notebookes for details for constructing a [geometry](agora_geometry.md),
defining a [material composition](materials_compositions.md) and setting up the [physics options](neutron_media.md), defining the [source](source.md).

```ipython3
import tripoli5
from tripoli5.core.physics import ParticleType
from tripoli5.core.literals import K, MeV
from tripoli5.core.euclide import Point

# Define a sphere centered at the origin with a radius of 6.39157
center_sphere = tripoli5.agora.Sphere(Point(0.0, 0.0, 0.0), 6.39157 / 2.0)
sphere = tripoli5.agora.Sphere(Point(0.0, 0.0, 0.0), 6.39157)

# Define a volume inside the sphere with the material "Pu"
pu_inner_volume = tripoli5.agora.Volume(
    shape=tripoli5.agora.Shape(-center_sphere), material="Pu-inner", label="pu_inner"
)
pu_outer_volume = tripoli5.agora.Volume(
    shape=tripoli5.agora.Shape(+center_sphere & -sphere),
    material="Pu-outer",
    label="pu_outer",
)

# Leakage boundary condition
bcs = tripoli5.agora.BoundaryConditions()
bcs.add(sphere, tripoli5.agora.LeakageBoundaryCondition())

# Create the geometry with the defined volumes
geo = tripoli5.agora.Geometry(
    tripoli5.agora.Universe([pu_inner_volume, pu_outer_volume]), boundary_conditions=bcs
)
# Load the nuclear data catalog from the environment variable
catalog = tripoli5.delos.Catalog.fromFile(
    f"/opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/endfb8r0_mcnp_v{tripoli5.delos.CATALOG_VERSION}.yaml"
)

# Define a material mixture for Plutonium (Pu)
Pu_in = (
    tripoli5.materials.MixtureBuilder(
        "concentrations"
    )  # Initialize the mixture builder with concentration mode
    .withName("Pu-inner")  # Set the name of the material to "Pu"
    .withCatalog(catalog)  # Associate the nuclear data catalog with the material
    .withTemperature(294 * K)  # Set the temperature of the material to 294 Kelvin
    .add(
        ["PU239", "PU240", "PU241", "GA69", "GA71"],  # Add isotopes to the mixture
        [
            0.037047,
            0.0017512,
            0.00011674,
            0.00083603,
            0.00053917,
        ],  # Specify the concentrations of the isotopes
    )
    .build()  # Build the material mixture
)
# Define a material mixture for Plutonium (Pu)
Pu_out = (
    tripoli5.materials.MixtureBuilder(
        "concentrations"
    )  # Initialize the mixture builder with concentration mode
    .withName("Pu-outer")  # Set the name of the material to "Pu"
    .withCatalog(catalog)  # Associate the nuclear data catalog with the material
    .withTemperature(294 * K)  # Set the temperature of the material to 294 Kelvin
    .add(
        ["PU239", "PU240", "PU241", "GA69", "GA71"],  # Add isotopes to the mixture
        [
            0.037047,
            0.0017512,
            0.00011674,
            0.00083603,
            0.00053917,
        ],  # Specify the concentrations of the isotopes
    )
    .build()  # Build the material mixture
)

# Initialize the NeutronMediumBuilder and build the media
media = (
    tripoli5.materials.NeutronMediumBuilder()
    .withCatalog(catalog)
    .withMixtures([Pu_in, Pu_out])
    .withURR("ace")
    .build()
)
src = tripoli5.source.PointIsotropicSource(
    ParticleType("Neutron"),
    tripoli5.distributions.energy.MonoKinetic(2.0 * MeV),
    Point(0.0, 0.0, 0.0),
)
active_batches = 100
inactive_batches = 10
param = tripoli5.simulation.SimulationParameters(
    nb_cycles=active_batches + inactive_batches,
    nb_events=10000,  # Particles per cycle
    name="Score_notebook",
    nb_threads=20,
    discard=inactive_batches,
)
```

```

[2026-06-05 13:01:43.703] [info] Loading catalog from file: /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/endfb8r0_mcnp_v2.3.0.yaml
[2026-06-05 13:01:43.724] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/mass/njoy_ace/v0.2.0/archive/wrapped_mass_data.bin
[2026-06-05 13:01:43.728] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/mass/njoy_ace/v0.2.0/archive/wrapped_mass_data.bin
[2026-06-05 13:01:43.733] [info] Building GA69 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-06-05 13:01:43.735] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/GA69.294.bin
[2026-06-05 13:01:43.740] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-06-05 13:01:43.742] [info]   Building reaction MTs = 60, 72, 2, 61, 57, 28, 54, 55, 59, 62, 32, 91, 63, 64, 65, 53, 66, 67, 68, 69, 70, 58, 71, 56, 73, 102, 74, 103, 51, 22, 111, 52, 104, 16, 75, 105, 107, 106
[2026-06-05 13:01:43.743] [info] Building GA71 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-06-05 13:01:43.745] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/GA71.294.bin
[2026-06-05 13:01:43.752] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-06-05 13:01:43.753] [info]   Building reaction MTs = 60, 2, 111, 53, 59, 58, 91, 102, 105, 107, 52, 51, 22, 56, 104, 17, 55, 103, 16, 54, 106, 28, 57
[2026-06-05 13:01:43.754] [info] Building PU239 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-06-05 13:01:43.757] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/PU239.294.bin
[2026-06-05 13:01:43.796] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/urr/njoy_ace/v0.4.0/dir/PU239.294.urr.ace.bin
[2026-06-05 13:01:43.800] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-06-05 13:01:43.804] [info]   Building reaction MTs = 75, 16, 17, 76, 18, 77, 66, 37, 74, 78, 79, 51, 80, 73, 102, 89, 91, 90, 62, 63, 64, 65, 61, 2, 60, 67, 68, 69, 57, 86, 70, 58, 87, 71, 59, 88, 53, 82, 72, 54, 83, 81, 52, 84, 55, 85, 56
[2026-06-05 13:01:43.804] [info] Building PU240 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-06-05 13:01:43.806] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/PU240.294.bin
[2026-06-05 13:01:43.843] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/urr/njoy_ace/v0.4.0/dir/PU240.294.urr.ace.bin
[2026-06-05 13:01:43.846] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-06-05 13:01:43.847] [info]   Building reaction MTs = 75, 16, 17, 76, 18, 77, 66, 37, 74, 78, 79, 51, 80, 73, 102, 89, 91, 90, 62, 63, 64, 65, 61, 2, 60, 67, 68, 69, 57, 86, 70, 58, 87, 71, 59, 88, 53, 82, 72, 54, 83, 81, 52, 84, 55, 85, 56
[2026-06-05 13:01:43.848] [info] Building PU241 at temperatures: TemperatureRange(294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C])
[2026-06-05 13:01:43.850] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/PU241.294.bin
[2026-06-05 13:01:43.861] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/urr/njoy_ace/v0.4.0/dir/PU241.294.urr.ace.bin
[2026-06-05 13:01:43.864] [info]   Building free gas collisions at temperature 294 [K], 2.5334957256000003e-08 [MeV], 20.850000000000023 [°C]
[2026-06-05 13:01:43.865] [info]   Building reaction MTs = 53, 59, 58, 61, 62, 91, 64, 65, 52, 51, 57, 18, 56, 17, 55, 16, 54, 2, 60, 102, 63
```

## Score Declaration

Before running a simulation, you need to declare the scores you want to compute. This involves specifying `Detector` and/or `DistributionDetector` objects the corresponding constructor and providing any necessary parameters for the computation. Here is an example of how to declare scores:

### Building the elements required to build a `Detector` or a `DistributionDetector`

#### Filters

`IncidentEnergy`: the following filter is used to score in 81 energy bins according to the incident neutron energy, uniformly spaced according to lethargy (logarithmically spaced according to energy) from \(10^{-4}\) MeV to 20 MeV.

```ipython3
import numpy as np

# energy bounds of the grid
energy_bounds = [e * MeV for e in np.logspace(-4, np.log10(20), 81)]
# building an IncidentEnergyGridFilter from a list of energy bounds
energy_filter = tripoli5.future_score.filters.IncidentEnergy(energy_bounds)
```

`Materials`: the following filters is used to score in 3 different bins, one for the `Pu-inner` material, one for the `Pu-outer` and one for the union of those two materials.

```ipython3
mat_filter = tripoli5.future_score.filters.Materials(
    material_names=["Pu-inner", "Pu-outer"],
    material_unions=[["Pu-inner", "Pu-outer"]],
)
```

`Volumes`: the following filters is used to score in 3 different bins, one for the `Pu-inner` volume, one for the `Pu-outer` and one for the union of those two volumes. If multiple volumes have the same name, a warning is issued and all volumes with the same name will be considered as a union of volumes.

```ipython3
vol_filter = tripoli5.future_score.filters.Volumes(
    volume_labels=["pu_inner", "pu_outer"],
    volume_unions=[["pu_inner", "pu_outer"]],
)
```

#### Responses

`Flux`: we want to score the neutron flux, resulting in +1 bin in the final dimension (the responses one) of the detector

```ipython3
# flux
flux_response = tripoli5.future_score.responses.Flux()
```

`ReactionRates` : indicates that we want to score macroscopic reaction rates for reactions MT=1 (total), 102 (\((n,\gamma)\)) and 18 (fission), thus resulting in +3 bins in the final dimension of our detector

```ipython3
import tripoli5.delos as delos

# MT=1, 102 and 18 reaction rates
mt_numbers = [1, 102, 18]
mt_ids = [delos.ReactionId(i) for i in mt_numbers]
mt_responses = tripoli5.future_score.responses.ReactionRates(media, mt_ids)
```

### Building the detectors

The two following detectors will thus compute the flux and MT reaction rates spectra for MT=1,102 and 18.

#### `Detector`: used to compute statistical moments

This one also scores according to materials in which collisions will occur, due to the presence of the `mat_filter` in the `filters` parameter.

```ipython3
moments_detector_mat = tripoli5.future_score.Detector(
    name="score_by_material_moments",
    filters=[energy_filter, mat_filter],  # list of filters
    responses=[flux_response, mt_responses],  # list of responses
    estimator="collision",  # estimator, either "collision" or "track"
    storage_type="shared",  # "thread local" or "shared"
    nthreads=20,  # number of threads used in the parallel section of the simulation (must be equal to the one set in the SimulationParameter)
    moments=2,  # max statistical moments order to be computed, here 2 means that we want to compute the average value and second order moments (standard deviation, variance, standard error, ...)
)
```

This one also scores according to volumes in which collisions will occur, due to the presence of the `vol_filter` in the `filters` parameter.

```ipython3
moments_detector_vol = tripoli5.future_score.Detector(
    name="score_by_volume_moments",
    filters=[energy_filter, vol_filter],  # list of filters
    responses=[flux_response, mt_responses],  # list of responses
    estimator="collision",  # estimator, either "collision" or "track"
    storage_type="shared",  # "thread local" or "shared"
    nthreads=20,  # number of threads used in the parallel section of the simulation (must be equal to the one set in the SimulationParameter)
    moments=2,  # max statistical moments order to be computed, here 2 means that we want to compute the average value and second order moments (standard deviation, variance, standard error, ...)
)
```

#### `DistributionDetector`: used to retrieve the entire sample

```ipython3
# Distribution detector
distribution_detector = tripoli5.future_score.DistributionDetector(
    name="my_flux_per_batch",
    filters=[energy_filter],
    responses=[flux_response],
    estimator="track",
    storage_type="thread local",
    nthreads=20,
)
```

The option `storage_type` is mandatory and can either be equal to `"thread local"` or `"shared"`. It defines if the underlying vector is copied on or shared amongst the threads in the parallel section of the code.

| Option | What It Does | When to Use |
| --- | --- | --- |
| **``”shared”``** | A single, global vector is shared by all threads. Each thread locks a bin before updating it, preventing simultaneous writes. | Large, fine‑grained histograms (e.g., pin‑by‑pin flux spectra). The vector is huge enough that copying it per thread would be prohibitive. |
| **``”thread local”``** | Each thread gets its own private copy of the entire vector and a reduction is performed at the end of the batch. No locks are needed, so there are no race conditions. | Small results (e.g., a handful of energy‑group fluxes or a single \(k_\text{eff}\)). Memory usage is low because the vectors are small. |

## Configure and Run Simulation

Finally we assemble the calculation using a simulation object. We also need to provide additional, specific calculation settings:

```ipython3
simu = (
    tripoli5.simulation.SimulationBuilder(
        simulation_mode="criticality", parallelism_type="openmp"
    )
    .withSource(src)
    .withGeometry(geo)
    .withMedia("Neutron", media)
    .withParameters(param)
    .withNewScores(
        [moments_detector_mat, moments_detector_vol, distribution_detector]
    )  # here we add our detectors to the simulation
    .build()
)
simu.run()
```

```

[2026-06-05 13:01:43.993] [info] *** Beginning of simulation ***
[2026-06-05 13:01:44.042] [info] Cycle: 1 of 110
[2026-06-05 13:01:44.129] [info]   kstep = 1.38180
[2026-06-05 13:01:44.130] [info] Cycle: 2 of 110
[2026-06-05 13:01:44.198] [info]   kstep = 1.12630
[2026-06-05 13:01:44.199] [info] Cycle: 3 of 110
[2026-06-05 13:01:44.254] [info]   kstep = 1.05080
[2026-06-05 13:01:44.255] [info] Cycle: 4 of 110
[2026-06-05 13:01:44.310] [info]   kstep = 1.02550
[2026-06-05 13:01:44.312] [info] Cycle: 5 of 110
[2026-06-05 13:01:44.365] [info]   kstep = 1.02270
[2026-06-05 13:01:44.366] [info] Cycle: 6 of 110
[2026-06-05 13:01:44.416] [info]   kstep = 1.05150
[2026-06-05 13:01:44.418] [info] Cycle: 7 of 110
[2026-06-05 13:01:44.466] [info]   kstep = 1.00410
[2026-06-05 13:01:44.467] [info] Cycle: 8 of 110
[2026-06-05 13:01:44.516] [info]   kstep = 1.01510
[2026-06-05 13:01:44.519] [info] Cycle: 9 of 110
[2026-06-05 13:01:44.565] [info]   kstep = 1.01410
… [192 lines of output omitted] …
[2026-06-05 13:01:49.848] [info] Cycle: 106 of 110
[2026-06-05 13:01:49.939] [info]   kstep = 1.00990   kstep_avg = 0.99956 +/- 0.00165
[2026-06-05 13:01:49.940] [info] Cycle: 107 of 110
[2026-06-05 13:01:49.996] [info]   kstep = 0.97950   kstep_avg = 0.99935 +/- 0.00164
[2026-06-05 13:01:50.001] [info] Cycle: 108 of 110
[2026-06-05 13:01:50.055] [info]   kstep = 0.98870   kstep_avg = 0.99924 +/- 0.00163
[2026-06-05 13:01:50.056] [info] Cycle: 109 of 110
[2026-06-05 13:01:50.108] [info]   kstep = 0.99660   kstep_avg = 0.99921 +/- 0.00161
[2026-06-05 13:01:50.109] [info] Cycle: 110 of 110
[2026-06-05 13:01:50.160] [info]   kstep = 0.96990   kstep_avg = 0.99892 +/- 0.00162
```

## Score Results

After running the simulation, you will want to retrieve the computed scores. Several common methods and properties are available across all score classes to help you access the results.

First, you can access a specific detector using `getDetector(index)` on your simulation. The index of a detector is the one corresponding to its position in the list given as input above.

```ipython3
moments_det_mat = simu.getDetector(
    0
)  # first detector put in the simulation, a `Detector` in our case
moments_det_vol = simu.getDetector(
    1
)  # second detector put in the simulation, a `Detector` in our case
distribution_det = simu.getDetector(
    2
)  # third detector put in the simulation, a `DistributionDetector` in our case
```

Then, you can retrieve several quantities using either read-only properties for those which are stored in the detector object, or using the appropriate method for those which are computed on-the-fly.

**Read-only Properties**

- For `Detector`:

  - `sampleMean`: Provides the mean value of the sample (\(\overline{x}\)).
  - `M2`: Provides the sum \(\sum_i (x_i - \overline{x})^2\)
  - `M3`: Provides the sum \(\sum_i (x_i - \overline{x})^3\)
  - `M4`: Provides the sum \(\sum_i (x_i - \overline{x})^4\)
- For `DistributionDetector`:

  - `distribution`: Provides the whole distribution of the sample (each \(x_i\)).

**On-the-fly computed quantities**

- For `Detector`:

  - `standardError()`: Provides the absolute standard error of the mean, i.e., the statistical uncertainty of the mean estimate.
  - `varianceOfTheMean()`: Provides the variance of the mean (i.e., square of the `standardErrorOfTheMean`).
  - `sampleVariance()`: Provides the variance of the sample (i.e., the **observed** fluctuations in the sample).
  - `sampleSkewness()`: Provides the skewness of the sample distribution, i.e., a measure of the asymetry of the distribution shape about its mean value.
  - `sampleExcessKurtosis()`: Provides the excess kurtosis of the sample distribution, i.e., the degree of *tailedness* in the sample distribution. The excess of kurtosis is equal to 0 for a normal distribution.
  - `meanVoV()`: Provides the Variance of Variance of the mean.

Retrieving results for the detector scoring over materials:

```ipython3
moments_det_mat_mean = moments_det_mat.sampleMean  # read-only property, no ()
moments_det_mat_sem = (
    moments_det_mat.standardError
)  # on-the-fly computation, we call a method here with the ()
```

Retrieving results for the detector scoring over volumes:

```ipython3
moments_det_vol_mean = moments_det_vol.sampleMean  # read-only property, no ()
moments_det_vol_sem = (
    moments_det_vol.standardError
)  # on-the-fly computation, we call a method here with the ()
```

Retrieving results for the distribution detector:

```ipython3
sample_distribution = distribution_detector.distribution
number_of_active_batches = sample_distribution.shape[0]

mean_from_distribution = np.mean(sample_distribution, axis=0)
# here we manually compute the standard error of the mean from the sample distribution
sem_from_distribution = np.std(sample_distribution, axis=0, ddof=1) / np.sqrt(
    number_of_active_batches
)
```

Each method or property returns a numpy-like array (according to the [array protocal](https://numpy.org/doc/stable/reference/arrays.interface.html)) of shape `(first filter size, second filter size, ..., last filter size, number of responses)` for a `Detector`, and of shape `(number of active batches, first filter size, second filter size, ..., last filter size, number of responses)` for the `distribution` read-only property of a `DistributionDetector`. Results are normalized for
one source particle.

```ipython3
print(f"sampleMean shape             : {moments_det_mat_mean.shape}")
print(f"standardErrorOfTheMean shape : {moments_det_mat_sem.shape}")
print(f"distribution shape           : {sample_distribution.shape}")
```

```

sampleMean shape             : (80, 3, 4)
standardErrorOfTheMean shape : (80, 3, 4)
distribution shape           : (100, 80, 1)
```

Coordinates order depends on the order in which filters and responses were given to the simulation. For `DistributionDetector`s, the first coordinate is always the batch index. In our case:

- For `moments_detector_mat`

  - first coordinate: **energy**
  - second coordinate: **materials**; 0 = `Pu-inner`, 1 = `Pu-outer`, 2 = `Pu-inner` + `Pu-outer`
  - last coordinate: **responses**; 0 = flux, 1 = MT 1, 2 = MT 102, 3 = MT 18
- For `moments_detector_vol`

  - first coordinate: **energy**
  - second coordinate: **volumes**; 0 = `Pu-inner`, 1 = `Pu-outer`, 2 = `Pu-inner` + `Pu-outer`
  - last coordinate: **responses**; 0 = flux, 1 = MT 1, 2 = MT 102, 3 = MT 18
- For `distribution_detector`

  - first coordinate: **batches**
  - second coordinate: **energy**
  - third coordinate: **materials**; 0 = `Pu-inner`, 1 = `Pu-outer`, 2 = `Pu-inner` + `Pu-outer`
  - last coordinate: **responses**; 0 = flux, 1 = MT 1, 2 = MT 102, 3 = MT 18

```ipython3
# --- plotting results
from matplotlib import pyplot as plt

energy_bounds_in_mev = [e.MeV for e in energy_bounds[:-1]]
number_of_sigma = 1.96

plt.plot(
    energy_bounds_in_mev,
    moments_det_mat_mean[:, 2, 0],
    label="From moments (collision, materials)",
    ds="steps-post",
    alpha=0.65,
)
plt.fill_between(
    energy_bounds_in_mev,
    moments_det_mat_mean[:, 2, 0] - number_of_sigma * moments_det_mat_sem[:, 2, 0],
    moments_det_mat_mean[:, 2, 0] + number_of_sigma * moments_det_mat_sem[:, 2, 0],
    alpha=0.3,
    step="post",
)

plt.plot(
    energy_bounds_in_mev,
    moments_det_vol_mean[:, 2, 0],
    label="From moments (collision, volumes)",
    linestyle="dotted",
    ds="steps-post",
    alpha=0.65,
)
plt.fill_between(
    energy_bounds_in_mev,
    moments_det_vol_mean[:, 2, 0] - number_of_sigma * moments_det_vol_sem[:, 2, 0],
    moments_det_vol_mean[:, 2, 0] + number_of_sigma * moments_det_vol_sem[:, 2, 0],
    alpha=0.3,
    step="post",
)

plt.plot(
    energy_bounds_in_mev,
    mean_from_distribution[:, 0],
    label="From distribution (track-length)",
    linestyle="--",
    ds="steps-post",
    alpha=0.65,
)
plt.fill_between(
    energy_bounds_in_mev,
    mean_from_distribution[:, 0] - number_of_sigma * sem_from_distribution[:, 0],
    mean_from_distribution[:, 0] + number_of_sigma * sem_from_distribution[:, 0],
    alpha=0.3,
    step="post",
)
plt.xlabel("Energy [MeV]")
plt.xscale("log")
plt.yscale("log")
plt.ylabel(r"$\phi$ [per source particle]")
plt.title("Integrated flux with 95% confidence interval")
plt.legend()
plt.show()
```

![figure](https://tripoli5.asnr.dev/documentation/latest-release/_images/examples_features_new_scores_44_0.png)

You can also access other responses by modifying the last index.

```ipython3
for i, mt in enumerate(mt_numbers):
    plt.plot(
        energy_bounds_in_mev,
        moments_det_mat_mean[:, 2, i + 1],
        label=f"MT = {mt}",
        ds="steps-post",
    )
    plt.fill_between(
        energy_bounds_in_mev,
        moments_det_mat_mean[:, 2, i + 1]
        - number_of_sigma * moments_det_mat_sem[:, 2, i + 1],
        moments_det_mat_mean[:, 2, i + 1]
        + number_of_sigma * moments_det_mat_sem[:, 2, i + 1],
        alpha=0.3,
        step="post",
    )

plt.xlabel("Energy [MeV]")
plt.xscale("log")
plt.yscale("log")
plt.ylabel("Rate [per source particle]")
plt.title("Integrated reaction rates with 95% confidence interval")
plt.legend()
plt.show()
```

![figure](https://tripoli5.asnr.dev/documentation/latest-release/_images/examples_features_new_scores_46_0.png)

The following plot displays the fission rate per material, but you can also plot it by volumes by replacing the material wise detector `moments_det_mat` by its volume wise counterpart `moments_det_vol`.

```ipython3
# --- pu inner material
plt.plot(
    energy_bounds_in_mev,
    moments_det_mat_mean[:, 0, i + 1],
    label="Pu-inner",
    ds="steps-post",
)
plt.fill_between(
    energy_bounds_in_mev,
    moments_det_mat_mean[:, 0, i + 1]
    - number_of_sigma * moments_det_mat_sem[:, 0, i + 1],
    moments_det_mat_mean[:, 0, i + 1]
    + number_of_sigma * moments_det_mat_sem[:, 0, i + 1],
    alpha=0.3,
    step="post",
)

# --- pu outer material
plt.plot(
    energy_bounds_in_mev,
    moments_det_mat_mean[:, 1, i + 1],
    label="Pu-outer",
    ds="steps-post",
)
plt.fill_between(
    energy_bounds_in_mev,
    moments_det_mat_mean[:, 1, i + 1]
    - number_of_sigma * moments_det_mat_sem[:, 1, i + 1],
    moments_det_mat_mean[:, 1, i + 1]
    + number_of_sigma * moments_det_mat_sem[:, 1, i + 1],
    alpha=0.3,
    step="post",
)

# --- [pu outer | pu inner] material
plt.plot(
    energy_bounds_in_mev,
    moments_det_mat_mean[:, 2, i + 1],
    label="Union",
    ds="steps-post",
)
plt.fill_between(
    energy_bounds_in_mev,
    moments_det_mat_mean[:, 2, i + 1]
    - number_of_sigma * moments_det_mat_sem[:, 2, i + 1],
    moments_det_mat_mean[:, 2, i + 1]
    + number_of_sigma * moments_det_mat_sem[:, 2, i + 1],
    alpha=0.3,
    step="post",
)

plt.xlabel("Energy [MeV]")
plt.xscale("log")
plt.yscale("log")
plt.ylabel("Rate [per source particle]")
plt.title("Fission rate per material with 95% confidence interval")
plt.legend()
plt.show()
```

![figure](https://tripoli5.asnr.dev/documentation/latest-release/_images/examples_features_new_scores_48_0.png)
