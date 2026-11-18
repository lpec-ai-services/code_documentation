<!-- source: https://tripoli5.asnr.dev/documentation/latest-release/examples/criticality/pin_cell.html -->

# A pin cell from the Mosteller suite

## Imports

```ipython3
from tripoli5.core.euclide import Point
from tripoli5.core.physics import ParticleType
from tripoli5.core.literals import K, MeV
import tripoli5
```

```ipython3
title = "Mosteller pin cell"
```

## Geometry

First, we define the basic shapes and universes. The fuel rod lives in an infinite universe, which we use to fill the unit pin cell.

```ipython3
c_fuel = tripoli5.agora.ZCylinder(0.0, 0.0, 0.39398)
s_fuel = tripoli5.agora.Shape(-c_fuel)
v_fuel = tripoli5.agora.Volume(s_fuel, "FUEL", label="FUEL")

c_gap = tripoli5.agora.ZCylinder(0.0, 0.0, 0.40226)
s_gap = tripoli5.agora.Shape(c_fuel & -c_gap)
v_gap = tripoli5.agora.Volume(s_gap, "GAP", label="GAP")

c_clad = tripoli5.agora.ZCylinder(0.0, 0.0, 0.45972)
s_clad = tripoli5.agora.Shape(c_gap & -c_clad)
v_clad = tripoli5.agora.Volume(s_clad, "ZIRCALLOY", label="ZIRCALLOY")

s_water = tripoli5.agora.Shape(c_clad)
v_water = tripoli5.agora.Volume(s_water, "WATER", label="WATER")

u_cell = tripoli5.agora.Universe([v_fuel, v_gap, v_clad, v_water])

pin_pitch = 2.0 * 0.63339
px_lo = tripoli5.agora.XPlane(-0.5 * pin_pitch)
px_hi = tripoli5.agora.XPlane(0.5 * pin_pitch)
py_lo = tripoli5.agora.YPlane(-0.5 * pin_pitch)
py_hi = tripoli5.agora.YPlane(0.5 * pin_pitch)
pz_lo = tripoli5.agora.ZPlane(-10.0)
pz_hi = tripoli5.agora.ZPlane(10.0)
r_cell = px_lo & -px_hi & py_lo & -py_hi & pz_lo & -pz_hi
s_cell = tripoli5.agora.Shape(r_cell)

v_cell = tripoli5.agora.CompositeVolume(s_cell, filler=u_cell, label="CELL")

root_universe = tripoli5.agora.Universe([v_cell])
```

Now we need to apply boundary conditions to the six planes of the pin cell. The boundary conditions will only apply to particles which cross the given surface. Note also that only one boundary condition is allowed on each surface-universe pair.

```ipython3
bcs = tripoli5.agora.BoundaryConditions()
reflection_bc = tripoli5.agora.ReflectionBoundaryCondition()
for p in px_lo, py_lo, pz_lo, px_hi, py_hi, pz_hi:
    bcs.add(p, reflection_bc)
```

Finally, we associate the boundary conditions to the geometry.

```ipython3
geo = tripoli5.agora.Geometry(root_universe, boundary_conditions=bcs)
```

## Plotting the geometry

```ipython3
plotter = tripoli5.geoplotter.GeoPlotterPyplot(geo)

frame = tripoli5.geoplotter.Frame.fromMinMax(
    "XY", altitude=0.0, u_min=-1, u_max=1, v_min=-1, v_max=1
)
_ = plotter.plot(frame=frame, resolution=200)
```

![figure](https://tripoli5.asnr.dev/documentation/latest-release/_images/examples_criticality_pin_cell_11_0.png)

```ipython3
frame = tripoli5.geoplotter.Frame.fromMinMax(
    "YZ", altitude=0.0, u_min=-1, u_max=1, v_min=-15, v_max=15
)
_ = plotter.plot(frame=frame, resolution=200)
```

![figure](https://tripoli5.asnr.dev/documentation/latest-release/_images/examples_criticality_pin_cell_12_0.png)

## Nuclear Data and Material Compositions

```ipython3
catalog = tripoli5.delos.Catalog.fromFile(
    f"/opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/endfb8r0_mcnp_v{tripoli5.delos.CATALOG_VERSION}.yaml"
)
```

```

[2026-06-05 12:59:35.687] [info] Loading catalog from file: /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/endfb8r0_mcnp_v2.3.0.yaml
```

Creates `mixtures`, i.e. material compositions, using the `MixtureBuilder`

```ipython3
m_fuel = (
    tripoli5.materials.MixtureBuilder("concentrations")
    .withName("FUEL")
    .withCatalog(catalog)
    .withTemperature(600.0 * K)
    .add("O16", 0.0461297)
    .add("U234", 5.81576e-06)
    .add("U235", 0.000723867)
    .add("U238", 0.0223352)
    .build()
)

m_gap = (
    tripoli5.materials.MixtureBuilder("concentrations")
    .withName("GAP")
    .withCatalog(catalog)
    .withTemperature(600.0 * K)
    .add("HE4", 1e-16)
    .build()
)

m_clad = (
    tripoli5.materials.MixtureBuilder("concentrations")
    .withName("ZIRCALLOY")
    .withCatalog(catalog)
    .withTemperature(600.0 * K)
    .add("ZR90", 0.0217035651)
    .add("ZR91", 0.00473302236)
    .add("ZR92", 0.0072345217)
    .add("ZR94", 0.00733154444)
    .add("ZR96", 0.0011811464)
    .build()
)

m_water = (
    tripoli5.materials.MixtureBuilder("concentrations")
    .withName("WATER")
    .withCatalog(catalog)
    .withTemperature(600.0 * K)
    .add("H1_H2O", 4.42326e-2)
    .add("B10", 1.02133e-5)
    .add("B11", 4.11098e-5)
    .add("O16", 2.21163e-2)
    .build()
)

mixtures = [m_fuel, m_gap, m_clad, m_water]

for mix in mixtures:
    mix.printSummary()
```

```

[2026-06-05 12:59:35.722] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/mass/njoy_ace/v0.2.0/archive/wrapped_mass_data.bin
[2026-06-05 12:59:35.730] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/mass/njoy_ace/v0.2.0/archive/wrapped_mass_data.bin
[2026-06-05 12:59:35.735] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/mass/njoy_ace/v0.2.0/archive/wrapped_mass_data.bin
[2026-06-05 12:59:35.740] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/mass/njoy_ace/v0.2.0/archive/wrapped_mass_data.bin
[2026-06-05 12:59:35.745] [info] Mixture: FUEL
[2026-06-05 12:59:35.746] [info] Temperature field:  Temperature is: 600 [K], 5.17039944e-08 [MeV], 326.85 [°C]

[2026-06-05 12:59:35.748] [info] === Owning mixture composition: ===
Number of IDs: 1
Number of nuclides: 4
IDs: O16 U234 U235 U238
0 0.0461297 5.81576e-06 0.000723867 0.0223352

[2026-06-05 12:59:35.748] [info] Mixture: GAP
[2026-06-05 12:59:35.750] [info] Temperature field:  Temperature is: 600 [K], 5.17039944e-08 [MeV], 326.85 [°C]

[2026-06-05 12:59:35.750] [info] === Owning mixture composition: ===
Number of IDs: 1
Number of nuclides: 1
IDs: HE4
0 1e-16

[2026-06-05 12:59:35.751] [info] Mixture: ZIRCALLOY
[2026-06-05 12:59:35.752] [info] Temperature field:  Temperature is: 600 [K], 5.17039944e-08 [MeV], 326.85 [°C]

[2026-06-05 12:59:35.753] [info] === Owning mixture composition: ===
Number of IDs: 1
Number of nuclides: 5
IDs: ZR90 ZR91 ZR92 ZR94 ZR96
0 0.0217035651 0.00473302236 0.0072345217 0.00733154444 0.0011811464

[2026-06-05 12:59:35.754] [info] Mixture: WATER
[2026-06-05 12:59:35.755] [info] Temperature field:  Temperature is: 600 [K], 5.17039944e-08 [MeV], 326.85 [°C]

[2026-06-05 12:59:35.756] [info] === Owning mixture composition: ===
Number of IDs: 1
Number of nuclides: 4
IDs: H1_H2O B10 B11 O16
0 0.0442326 1.02133e-05 4.11098e-05 0.0221163
```

```ipython3
media = (
    tripoli5.materials.NeutronMediumBuilder()
    .withCatalog(catalog)
    .withMixtures(mixtures)
    .build()
)
```

```

[2026-06-05 12:59:35.770] [info] Building B10 at temperatures: TemperatureRange(600 [K], 5.17039944e-08 [MeV], 326.85 [°C])
[2026-06-05 12:59:35.774] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/B10.600.bin
[2026-06-05 12:59:35.783] [info]   Building free gas collisions at temperature 600 [K], 5.17039944e-08 [MeV], 326.85 [°C]
[2026-06-05 12:59:35.784] [info]   Building reaction MTs = 700, 51, 57, 58, 60, 59, 77, 79, 80, 56, 85, 78, 52, 81, 801, 800, 104, 102, 68, 601, 70, 600, 69, 602, 71, 53, 82, 604, 73, 83, 54, 605, 74, 75, 76, 67, 66, 65, 64, 63, 62, 61, 2, 72, 603, 84, 55
[2026-06-05 12:59:35.786] [info] Building B11 at temperatures: TemperatureRange(600 [K], 5.17039944e-08 [MeV], 326.85 [°C])
[2026-06-05 12:59:35.789] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/B11.600.bin
[2026-06-05 12:59:35.796] [info]   Building free gas collisions at temperature 600 [K], 5.17039944e-08 [MeV], 326.85 [°C]
[2026-06-05 12:59:35.797] [info]   Building reaction MTs = 60, 2, 59, 58, 91, 102, 57, 28, 54, 56, 52, 51, 22, 55, 103, 16, 107, 105, 53
[2026-06-05 12:59:35.798] [info] Building H1_H2O at temperatures: TemperatureRange(600 [K], 5.17039944e-08 [MeV], 326.85 [°C])
[2026-06-05 12:59:35.802] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/H1.600.bin
[2026-06-05 12:59:35.809] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/tsl/njoy_ace/v0.3.0/dir/H1_H2O.600.bin
[2026-06-05 12:59:35.844] [info]   Building free gas collisions at temperature 600 [K], 5.17039944e-08 [MeV], 326.85 [°C]
[2026-06-05 12:59:35.845] [info]   Building reaction MTs = 102, 2
[2026-06-05 12:59:35.846] [info]   Building thermal collisions at temperature 600 [K], 5.17039944e-08 [MeV], 326.85 [°C]
[2026-06-05 12:59:35.847] [info]   Building thermal reaction MTs = 1000000
[2026-06-05 12:59:35.847] [info] Building HE4 at temperatures: TemperatureRange(600 [K], 5.17039944e-08 [MeV], 326.85 [°C])
[2026-06-05 12:59:35.849] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/HE4.600.bin
[2026-06-05 12:59:35.852] [info]   Building free gas collisions at temperature 600 [K], 5.17039944e-08 [MeV], 326.85 [°C]
[2026-06-05 12:59:35.853] [info]   Building reaction MTs = 2, 101
… [33 lines of output omitted] …
[2026-06-05 12:59:36.141] [info] Building ZR94 at temperatures: TemperatureRange(600 [K], 5.17039944e-08 [MeV], 326.85 [°C])
[2026-06-05 12:59:36.143] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/ZR94.600.bin
[2026-06-05 12:59:36.153] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/urr/njoy_ace/v0.4.0/dir/ZR94.600.urr.ace.bin
[2026-06-05 12:59:36.156] [info]   Building free gas collisions at temperature 600 [K], 5.17039944e-08 [MeV], 326.85 [°C]
[2026-06-05 12:59:36.157] [info]   Building reaction MTs = 825, 22, 24, 607, 17, 812, 104, 606, 16, 811, 28, 819, 57, 809, 822, 60, 821, 59, 649, 826, 32, 91, 608, 609, 829, 824, 62, 800, 801, 601, 837, 804, 817, 55, 803, 605, 816, 54, 808, 603, 839, 814, 52, 806, 604, 807, 602, 838, 805, 802, 102, 810, 827, 58, 820, 112, 53, 815, 849, 836, 600, 818, 56, 835, 834, 833, 832, 831, 5, 105, 51, 813, 830, 828, 2, 823, 61
[2026-06-05 12:59:36.158] [info] Building ZR96 at temperatures: TemperatureRange(600 [K], 5.17039944e-08 [MeV], 326.85 [°C])
[2026-06-05 12:59:36.160] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/freegas/njoy_ace/v0.11.0/dir/ZR96.600.bin
[2026-06-05 12:59:36.168] [info] Loading /opt/tripoli-5/delos/nuclide/endfb8r0_mcnp/urr/njoy_ace/v0.4.0/dir/ZR96.600.urr.ace.bin
[2026-06-05 12:59:36.172] [info]   Building free gas collisions at temperature 600 [K], 5.17039944e-08 [MeV], 326.85 [°C]
[2026-06-05 12:59:36.173] [info]   Building reaction MTs = 801, 105, 807, 53, 24, 804, 601, 602, 805, 51, 22, 600, 803, 649, 802, 52, 806, 808, 54, 17, 104, 800, 849, 16, 5, 28, 2, 55, 809, 91, 102
```

## Sources

Define a source that is:

- isotropic
- point (0.,0.,0.)
- 2 MeV incident energy

```ipython3
src = tripoli5.source.PointIsotropicSource(
    ParticleType("Neutron"),
    tripoli5.distributions.energy.MonoKinetic(2.0 * MeV),
    Point(0.0, 0.0, 0.0),  # point source
    1.0,  # norm
    0.0,  # time
)
```

## Score

Define a flux score over an energy grid of 1000 groups defined with equivalent bins in lethargy.

```ipython3
score_mgr = tripoli5.score.ScoreManager(title)
flux = tripoli5.score.FluxSpectrumAllVolumes(
    1, 1e-11, 20.0, 1000, "FluxSpectrumAllVolumes"
)
score_mgr.addScore(flux)
```

## Simulation setup

Simulation parameters

```ipython3
simu_params = tripoli5.simulation.SimulationParameters(
    nb_cycles=120,
    nb_events=10000,
    nb_threads=10,
    name=title,
    discard=10,
)
print(f"{simu_params.name=}")
print(f"{simu_params.nb_threads=}")
print(f"{simu_params.nb_cycles=}")
print(f"{simu_params.nb_events=}")
print(f"{simu_params.discard=}")
```

```

simu_params.name='Mosteller pin cell'
simu_params.nb_threads=10
simu_params.nb_cycles=120
simu_params.nb_events=10000
simu_params.discard=10
```

## Launching the code

```ipython3
simu = (
    tripoli5.simulation.SimulationBuilder(
        simulation_mode="criticality", parallelism_type="openmp"
    )
    .withSource(src)
    .withGeometry(geo)
    .withMedia("Neutron", media)
    .withParameters(simu_params)
    .withScores(score_mgr)
    .build()
)
```

Running the simulation

```ipython3
simu.run()
```

```

[2026-06-05 12:59:36.253] [info] *** Beginning of simulation ***
[2026-06-05 12:59:36.303] [info] Cycle: 1 of 120
[2026-06-05 12:59:37.009] [info]   kstep = 1.21280
[2026-06-05 12:59:37.011] [info] Cycle: 2 of 120
[2026-06-05 12:59:37.545] [info]   kstep = 1.19170
[2026-06-05 12:59:37.549] [info] Cycle: 3 of 120
[2026-06-05 12:59:38.084] [info]   kstep = 1.18640
[2026-06-05 12:59:38.086] [info] Cycle: 4 of 120
[2026-06-05 12:59:38.617] [info]   kstep = 1.19030
[2026-06-05 12:59:38.618] [info] Cycle: 5 of 120
[2026-06-05 12:59:39.158] [info]   kstep = 1.18550
[2026-06-05 12:59:39.159] [info] Cycle: 6 of 120
[2026-06-05 12:59:39.700] [info]   kstep = 1.18160
[2026-06-05 12:59:39.704] [info] Cycle: 7 of 120
[2026-06-05 12:59:40.247] [info]   kstep = 1.17130
[2026-06-05 12:59:40.252] [info] Cycle: 8 of 120
[2026-06-05 12:59:40.790] [info]   kstep = 1.17670
[2026-06-05 12:59:40.791] [info] Cycle: 9 of 120
[2026-06-05 12:59:41.329] [info]   kstep = 1.16140
… [212 lines of output omitted] …
[2026-06-05 13:00:39.578] [info] Cycle: 116 of 120
[2026-06-05 13:00:40.103] [info]   kstep = 1.17500   kstep_avg = 1.17546 +/- 0.00112
[2026-06-05 13:00:40.105] [info] Cycle: 117 of 120
[2026-06-05 13:00:40.643] [info]   kstep = 1.18320   kstep_avg = 1.17553 +/- 0.00111
[2026-06-05 13:00:40.645] [info] Cycle: 118 of 120
[2026-06-05 13:00:41.176] [info]   kstep = 1.18680   kstep_avg = 1.17564 +/- 0.00110
[2026-06-05 13:00:41.177] [info] Cycle: 119 of 120
[2026-06-05 13:00:41.715] [info]   kstep = 1.16870   kstep_avg = 1.17557 +/- 0.00110
[2026-06-05 13:00:41.717] [info] Cycle: 120 of 120
[2026-06-05 13:00:42.253] [info]   kstep = 1.16770   kstep_avg = 1.17550 +/- 0.00109
```

## Inspecting results

### keff

```ipython3
import numpy as np

kstep = simu.getKStep()
t5_kstep_mean = kstep.mean[0]
t5_kstep_var = kstep.var[0]
t5_kstep_sigma = np.sqrt(t5_kstep_var)
print(f"TRIPOLI-5: k_step = {t5_kstep_mean:.5f} ± {t5_kstep_sigma:.5f}")
```

```

TRIPOLI-5: k_step = 1.17550 ± 0.00109
```

Here are the reference TRIPOLI-4 results:

```ipython3
t4_kstep_mean = 1.177819e00
# T4 expresses standard errors as relative values, in percent
t4_kstep_sigma = 1.027623e-01 * 1e-2 * t4_kstep_mean
t4_kstep_var = t4_kstep_sigma**2

print(f"TRIPOLI-4: k_step = {t4_kstep_mean:.5f} ± {t4_kstep_sigma:.5f}")
```

```

TRIPOLI-4: k_step = 1.17782 ± 0.00121
```

The TRIPOLI-4/TRIPOLI-5 comparison passes Student’s t-test:

```ipython3
t_student = (t5_kstep_mean - t4_kstep_mean) / np.sqrt(t5_kstep_var + t4_kstep_var)
print(f"{t_student = :.2f}")
assert np.abs(t_student) < 3.0
```

```

t_student = -1.42
```

## Delta-Tracking

In the previous simulation, we ran the problem using the surface tracking algorithm, which is the default method used by TRIPOLI-5 is no method is specified. We can also use the delta-tracking algorithm, which can provide run time improvements for various types of systems. First, we can create the delta-tracking obect we want to use in our simulation. This creates an energy-dependent majorant cross section based on the `media` in our problem, and also applies a small multiplicative factor of
1.001 to this majorant, which protects particles from landing at a phase-space coordinate were the majorant cross seciton is not actually a majorant. We also build the majorant in parallel with OpenMP to save time.

```ipython3
delta_tracking = (
    tripoli5.simulation.TrackingBuilder(
        tripoli5.simulation.MajorantType.EnergyDependent
    )
    .withMajorantParameters(media, tripoli5.simulation.MajorantExecutor.OpenMP)
    .withMajorantFudgeFactors([0.0, 20.0], [1.001])
    .withPopulationControl()
    .build()
)
```

```

[2026-06-05 13:00:42.326] [info] Building B10 at temperatures: TemperatureRange(600 [K], 5.17039944e-08 [MeV], 326.85 [°C])
[2026-06-05 13:00:42.331] [info]   Building free gas collisions at temperature 600 [K], 5.17039944e-08 [MeV], 326.85 [°C]
[2026-06-05 13:00:42.332] [info]   Building reaction MTs = 700, 51, 57, 58, 60, 59, 77, 79, 80, 56, 85, 78, 52, 81, 801, 800, 104, 102, 68, 601, 70, 600, 69, 602, 71, 53, 82, 604, 73, 83, 54, 605, 74, 75, 76, 67, 66, 65, 64, 63, 62, 61, 2, 72, 603, 84, 55
[2026-06-05 13:00:42.333] [info] Building B11 at temperatures: TemperatureRange(600 [K], 5.17039944e-08 [MeV], 326.85 [°C])
[2026-06-05 13:00:42.337] [info]   Building free gas collisions at temperature 600 [K], 5.17039944e-08 [MeV], 326.85 [°C]
[2026-06-05 13:00:42.338] [info]   Building reaction MTs = 60, 2, 59, 58, 91, 102, 57, 28, 54, 56, 52, 51, 22, 55, 103, 16, 107, 105, 53
[2026-06-05 13:00:42.339] [info] Building H1_H2O at temperatures: TemperatureRange(600 [K], 5.17039944e-08 [MeV], 326.85 [°C])
[2026-06-05 13:00:42.345] [info]   Building free gas collisions at temperature 600 [K], 5.17039944e-08 [MeV], 326.85 [°C]
[2026-06-05 13:00:42.347] [info]   Building reaction MTs = 102, 2
[2026-06-05 13:00:42.348] [info]   Building thermal collisions at temperature 600 [K], 5.17039944e-08 [MeV], 326.85 [°C]
[2026-06-05 13:00:42.349] [info]   Building thermal reaction MTs = 1000000
[2026-06-05 13:00:42.350] [info] Building HE4 at temperatures: TemperatureRange(600 [K], 5.17039944e-08 [MeV], 326.85 [°C])
[2026-06-05 13:00:42.353] [info]   Building free gas collisions at temperature 600 [K], 5.17039944e-08 [MeV], 326.85 [°C]
[2026-06-05 13:00:42.358] [info]   Building reaction MTs = 2, 101
[2026-06-05 13:00:42.359] [info] Building O16 at temperatures: TemperatureRange(600 [K], 5.17039944e-08 [MeV], 326.85 [°C])
[2026-06-05 13:00:42.367] [info]   Building free gas collisions at temperature 600 [K], 5.17039944e-08 [MeV], 326.85 [°C]
[2026-06-05 13:00:42.369] [info]   Building reaction MTs = 659, 600, 707, 800, 802, 45, 91, 705, 56, 704, 55, 749, 53, 702, 112, 669, 668, 32, 667, 664, 703, 54, 52, 701, 708, 650, 709, 666, 663, 28, 108, 801, 2, 57, 706, 41, 803, 5, 654, 102, 44, 651, 16, 665, 51, 700, 601, 660, 602, 661, 603, 662, 652, 653, 655, 656, 22, 657, 658, 23
[2026-06-05 13:00:42.370] [info] Building U234 at temperatures: TemperatureRange(600 [K], 5.17039944e-08 [MeV], 326.85 [°C])
[2026-06-05 13:00:42.374] [info]   Building free gas collisions at temperature 600 [K], 5.17039944e-08 [MeV], 326.85 [°C]
[2026-06-05 13:00:42.376] [info]   Building reaction MTs = 20, 79, 21, 80, 66, 37, 51, 70, 71, 72, 74, 77, 73, 102, 89, 91, 67, 38, 90, 88, 87, 57, 86, 58, 54, 83, 60, 2, 61, 62, 63, 64, 65, 55, 84, 68, 56, 85, 69, 59, 53, 82, 16, 75, 17, 76, 19, 78, 81, 52
[2026-06-05 13:00:42.377] [info] Building U235 at temperatures: TemperatureRange(600 [K], 5.17039944e-08 [MeV], 326.85 [°C])
[2026-06-05 13:00:42.382] [info]   Building free gas collisions at temperature 600 [K], 5.17039944e-08 [MeV], 326.85 [°C]
[2026-06-05 13:00:42.383] [info]   Building reaction MTs = 814, 52, 813, 51, 818, 56, 76, 17, 817, 55, 75, 16, 77, 18, 816, 54, 72, 834, 815, 53, 822, 60, 821, 59, 5, 74, 82, 83, 84, 85, 86, 87, 81, 806, 91, 80, 805, 79, 804, 68, 830, 835, 73, 102, 810, 2, 89, 78, 803, 88, 802, 801, 800, 63, 825, 64, 826, 649, 65, 827, 828, 66, 67, 829, 61, 823, 831, 69, 812, 833, 71, 811, 62, 824, 832, 70, 809, 808, 807, 58, 820, 57, 819
[2026-06-05 13:00:42.384] [info] Building U238 at temperatures: TemperatureRange(600 [K], 5.17039944e-08 [MeV], 326.85 [°C])
[2026-06-05 13:00:42.390] [info]   Building free gas collisions at temperature 600 [K], 5.17039944e-08 [MeV], 326.85 [°C]
[2026-06-05 13:00:42.391] [info]   Building reaction MTs = 77, 18, 76, 17, 79, 51, 80, 52, 81, 82, 75, 16, 800, 56, 85, 78, 74, 73, 102, 62, 91, 65, 66, 61, 2, 60, 89, 67, 68, 69, 64, 5, 63, 70, 58, 87, 71, 57, 86, 649, 59, 88, 53, 72, 54, 83, 84, 55
[2026-06-05 13:00:42.392] [info] Building ZR90 at temperatures: TemperatureRange(600 [K], 5.17039944e-08 [MeV], 326.85 [°C])
[2026-06-05 13:00:42.397] [info]   Building free gas collisions at temperature 600 [K], 5.17039944e-08 [MeV], 326.85 [°C]
[2026-06-05 13:00:42.398] [info]   Building reaction MTs = 5, 16, 606, 55, 56, 607, 28, 608, 849, 54, 605, 808, 807, 649, 59, 610, 604, 112, 53, 58, 609, 102, 91, 104, 800, 105, 801, 2, 611, 600, 803, 601, 804, 57, 802, 805, 51, 22, 602, 806, 52, 603
[2026-06-05 13:00:42.399] [info] Building ZR91 at temperatures: TemperatureRange(600 [K], 5.17039944e-08 [MeV], 326.85 [°C])
[2026-06-05 13:00:42.404] [info]   Building free gas collisions at temperature 600 [K], 5.17039944e-08 [MeV], 326.85 [°C]
[2026-06-05 13:00:42.405] [info]   Building reaction MTs = 604, 819, 57, 818, 56, 51, 813, 22, 24, 16, 811, 849, 810, 102, 827, 826, 649, 825, 812, 104, 32, 91, 823, 822, 800, 801, 55, 817, 804, 605, 816, 54, 59, 821, 803, 41, 808, 814, 52, 806, 807, 805, 802, 836, 600, 839, 603, 838, 602, 837, 601, 835, 834, 833, 832, 831, 5, 105, 830, 829, 828, 2, 112, 58, 820, 53, 815, 809, 824, 28
[2026-06-05 13:00:42.406] [info] Building ZR92 at temperatures: TemperatureRange(600 [K], 5.17039944e-08 [MeV], 326.85 [°C])
[2026-06-05 13:00:42.409] [info]   Building free gas collisions at temperature 600 [K], 5.17039944e-08 [MeV], 326.85 [°C]
[2026-06-05 13:00:42.411] [info]   Building reaction MTs = 804, 803, 802, 801, 800, 649, 826, 600, 836, 849, 112, 820, 58, 825, 839, 810, 102, 53, 815, 32, 91, 829, 838, 817, 55, 822, 816, 54, 59, 821, 808, 814, 52, 806, 807, 805, 837, 835, 834, 833, 832, 831, 5, 823, 105, 830, 827, 809, 2, 828, 824, 819, 57, 28, 811, 16, 104, 812, 17, 24, 22, 813, 51, 56, 818
[2026-06-05 13:00:42.412] [info] Building ZR94 at temperatures: TemperatureRange(600 [K], 5.17039944e-08 [MeV], 326.85 [°C])
[2026-06-05 13:00:42.417] [info]   Building free gas collisions at temperature 600 [K], 5.17039944e-08 [MeV], 326.85 [°C]
[2026-06-05 13:00:42.418] [info]   Building reaction MTs = 825, 22, 24, 607, 17, 812, 104, 606, 16, 811, 28, 819, 57, 809, 822, 60, 821, 59, 649, 826, 32, 91, 608, 609, 829, 824, 62, 800, 801, 601, 837, 804, 817, 55, 803, 605, 816, 54, 808, 603, 839, 814, 52, 806, 604, 807, 602, 838, 805, 802, 102, 810, 827, 58, 820, 112, 53, 815, 849, 836, 600, 818, 56, 835, 834, 833, 832, 831, 5, 105, 51, 813, 830, 828, 2, 823, 61
[2026-06-05 13:00:42.419] [info] Building ZR96 at temperatures: TemperatureRange(600 [K], 5.17039944e-08 [MeV], 326.85 [°C])
[2026-06-05 13:00:42.423] [info]   Building free gas collisions at temperature 600 [K], 5.17039944e-08 [MeV], 326.85 [°C]
[2026-06-05 13:00:42.425] [info]   Building reaction MTs = 801, 105, 807, 53, 24, 804, 601, 602, 805, 51, 22, 600, 803, 649, 802, 52, 806, 808, 54, 17, 104, 800, 849, 16, 5, 28, 2, 55, 809, 91, 102
[2026-06-05 13:00:42.426] [info] Building majorant cross section...
[2026-06-05 13:00:42.435] [info] ... sorting the unionized grid...
[2026-06-05 13:00:42.457] [info] ... removing duplicate points from the grid...
[2026-06-05 13:00:42.459] [info] ... removing energies outside the simulation range...
[2026-06-05 13:00:42.462] [info] ... unionized grid has 271772 points...
[2026-06-05 13:00:43.499] [info] ... majorant cross section built!
```

We can then build a new simulation instance to run.

```ipython3
dt_simu = (
    tripoli5.simulation.SimulationBuilder(
        simulation_mode="criticality", parallelism_type="openmp"
    )
    .withSource(src)
    .withGeometry(geo)
    .withMedia("Neutron", media)
    .withParameters(simu_params)
    .withScores(score_mgr)
    .withParticleTracking("Neutron", delta_tracking)
    .build()
)

dt_simu.run()
```

```

[2026-06-05 13:00:43.517] [info] *** Beginning of simulation ***
[2026-06-05 13:00:43.554] [info] Cycle: 1 of 120
[2026-06-05 13:00:43.850] [info]   kstep = 1.20660
[2026-06-05 13:00:43.852] [info] Cycle: 2 of 120
[2026-06-05 13:00:44.112] [info]   kstep = 1.16210
[2026-06-05 13:00:44.114] [info] Cycle: 3 of 120
[2026-06-05 13:00:44.368] [info]   kstep = 1.18750
[2026-06-05 13:00:44.370] [info] Cycle: 4 of 120
[2026-06-05 13:00:44.620] [info]   kstep = 1.18410
[2026-06-05 13:00:44.622] [info] Cycle: 5 of 120
[2026-06-05 13:00:44.872] [info]   kstep = 1.17360
[2026-06-05 13:00:44.874] [info] Cycle: 6 of 120
[2026-06-05 13:00:45.127] [info]   kstep = 1.20030
[2026-06-05 13:00:45.129] [info] Cycle: 7 of 120
[2026-06-05 13:00:45.379] [info]   kstep = 1.18860
[2026-06-05 13:00:45.380] [info] Cycle: 8 of 120
[2026-06-05 13:00:45.634] [info]   kstep = 1.18410
[2026-06-05 13:00:45.635] [info] Cycle: 9 of 120
[2026-06-05 13:00:45.886] [info]   kstep = 1.19470
… [212 lines of output omitted] …
[2026-06-05 13:01:13.374] [info] Cycle: 116 of 120
[2026-06-05 13:01:13.631] [info]   kstep = 1.16680   kstep_avg = 1.17902 +/- 0.00117
[2026-06-05 13:01:13.633] [info] Cycle: 117 of 120
[2026-06-05 13:01:13.913] [info]   kstep = 1.16310   kstep_avg = 1.17887 +/- 0.00117
[2026-06-05 13:01:13.915] [info] Cycle: 118 of 120
[2026-06-05 13:01:14.172] [info]   kstep = 1.17910   kstep_avg = 1.17887 +/- 0.00116
[2026-06-05 13:01:14.174] [info] Cycle: 119 of 120
[2026-06-05 13:01:14.425] [info]   kstep = 1.19230   kstep_avg = 1.17899 +/- 0.00115
[2026-06-05 13:01:14.427] [info] Cycle: 120 of 120
[2026-06-05 13:01:14.681] [info]   kstep = 1.17450   kstep_avg = 1.17895 +/- 0.00114
```

Let’s compare the results obtained with surface-tracking and delta-tracking:

```ipython3
dt_kstep = dt_simu.getKStep()
t5_dt_kstep_mean = dt_kstep.mean[0]
t5_dt_kstep_var = dt_kstep.var[0]
t5_dt_kstep_sigma = np.sqrt(t5_kstep_var)
print(f"Surface-Tracking: k_step = {t5_kstep_mean:.5f} ± {t5_kstep_sigma:.5f}")
print(f"Delta-Tracking:   k_step = {t5_dt_kstep_mean:.5f} ± {t5_dt_kstep_sigma:.5f}")
t_student = (t5_kstep_mean - t5_dt_kstep_mean) / np.sqrt(t5_kstep_var + t5_dt_kstep_var)
print(f"{t_student = :.2f}")
assert np.abs(t_student) < 3.0
```

```

Surface-Tracking: k_step = 1.17550 ± 0.00109
Delta-Tracking:   k_step = 1.17895 ± 0.00109
t_student = -2.18
```
