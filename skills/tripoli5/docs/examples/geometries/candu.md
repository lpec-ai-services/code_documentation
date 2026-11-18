<!-- source: https://tripoli5.asnr.dev/documentation/latest-release/examples/geometries/candu.html -->

# A CANDU assembly

We have selected a CANDU fuel assembly configuration with specifications taken from Ref. [1].

The assembly contains 37 fuel pins, arranged in 4 concentric rings. The model is at constant 300 K temperature.

[1] J. M. Pounders et al. “A 3D stylized half-core CANDU benchmark problem”. In: Annals of Nuclear Energy 38.4 (2011), pp. 876–896.

```ipython3
import tripoli5
import numpy as np
from tripoli5.core.euclide import Vector

# Geometry definitions

# Outer radius of fuel and clad
r_fuel = 0.6103
r_clad = 0.6522

# Pressure tube and calandria radii
pressure_tube_ir = 5.16890
pressure_tube_or = 5.60320
calandria_ir = 6.44780
calandria_or = 6.58750

# Radius to center of each ring of fuel pins
ring_radii = np.array([0.0, 1.4880, 2.8755, 4.3305])

# These are the surfaces that will divide each of the rings
radial_surf = [
    tripoli5.agora.ZCylinder(0.0, 0.0, r)
    for r in (ring_radii[:-1] + ring_radii[1:]) / 2
]

water_regions = []
for i in range(ring_radii.size):
    # Create annular region
    if i == 0:
        water_region = -radial_surf[i]
    elif i == ring_radii.size - 1:
        water_region = +radial_surf[i - 1]
    else:
        water_region = +radial_surf[i - 1] & -radial_surf[i]
    water_regions.append(water_region)

surf_fuel = tripoli5.agora.ZCylinder(0.0, 0.0, r_fuel)

fuel_cell = tripoli5.agora.Volume(tripoli5.agora.Shape(-surf_fuel), "fuel")
clad_cell = tripoli5.agora.Volume(tripoli5.agora.Shape(+surf_fuel), "zircaloy")

pin_universe = tripoli5.agora.Universe([fuel_cell, clad_cell])

num_pins = [1, 6, 12, 18]
angles = [0, 0, 15, 0]

pins = []
for i, (r, n, a) in enumerate(zip(ring_radii, num_pins, angles)):
    for j in range(n):
        # Determine location of center of pin
        theta = (a + j / n * 360.0) * np.pi / 180.0
        x = r * np.cos(theta)
        y = r * np.sin(theta)

        pin_boundary = tripoli5.agora.ZCylinder(x, y, r_clad)
        water_regions[i] &= +pin_boundary

        # Create each fuel pin -- note that we explicitly assign an ID so
        # that we can identify the pin later when looking at tallies
        translation = tripoli5.core.euclide.Translation(Vector(x, y, 0))
        transformation = tripoli5.core.euclide.AffineTransformation(translation, None)
        pin = tripoli5.agora.CompositeVolume(
            shape=tripoli5.agora.Shape(-pin_boundary),
            filler=pin_universe,
            affinetransformation=transformation,
        )
        pins.append(pin)

water_cells = []
for i in range(ring_radii.size):
    water_cells.append(
        tripoli5.agora.Volume(tripoli5.agora.Shape(water_regions[i]), "heavy water")
    )

bundle_universe = tripoli5.agora.Universe(water_cells + pins)

pt_inner = tripoli5.agora.ZCylinder(0.0, 0.0, pressure_tube_ir)
pt_outer = tripoli5.agora.ZCylinder(0.0, 0.0, pressure_tube_or)
calandria_inner = tripoli5.agora.ZCylinder(0.0, 0.0, calandria_ir)
calandria_outer = tripoli5.agora.ZCylinder(0.0, 0.0, calandria_or)

pitch = 28.5750
zpitch = 49.5300
left = tripoli5.agora.XPlane(-pitch / 2)
right = tripoli5.agora.XPlane(pitch / 2)
bottom = tripoli5.agora.YPlane(-pitch / 2)
top = tripoli5.agora.YPlane(pitch / 2)
down = tripoli5.agora.ZPlane(-zpitch / 2)
up = tripoli5.agora.ZPlane(zpitch / 2)

bundle = tripoli5.agora.CompositeVolume(
    tripoli5.agora.Shape(-pt_inner & +down & -up), filler=bundle_universe
)
pressure_tube = tripoli5.agora.Volume(
    tripoli5.agora.Shape(+pt_inner & -pt_outer & +down & -up), "zircaloy pt"
)
v1 = tripoli5.agora.Volume(
    tripoli5.agora.Shape(+pt_outer & -calandria_inner & +down & -up), "filler"
)
calandria = tripoli5.agora.Volume(
    tripoli5.agora.Shape(+calandria_inner & -calandria_outer & +down & -up),
    "zircaloy c",
)
moderator = tripoli5.agora.Volume(
    tripoli5.agora.Shape(
        +left & -right & +bottom & -top & +down & -up & +calandria_outer
    ),
    "heavy water",
)

root_universe = tripoli5.agora.Universe(
    [bundle, pressure_tube, v1, calandria, moderator]
)

bcs = tripoli5.agora.BoundaryConditions()
reflecting_bc = tripoli5.agora.ReflectionBoundaryCondition()

bcs.add(left, reflecting_bc)
bcs.add(right, reflecting_bc)
bcs.add(bottom, reflecting_bc)
bcs.add(top, reflecting_bc)
bcs.add(down, reflecting_bc)
bcs.add(up, reflecting_bc)

geo = tripoli5.agora.Geometry(root_universe, boundary_conditions=bcs)
```

```ipython3
plotter = tripoli5.geoplotter.GeoPlotterPyplot(geo)
frame = tripoli5.geoplotter.Frame.fromMinMax(
    "XY", altitude=0.0, u_min=-7, u_max=7, v_min=-7, v_max=7
)
_ = plotter.plot(frame=frame, resolution=50, mode="point")
```

![figure](https://tripoli5.asnr.dev/documentation/latest-release/_images/examples_geometries_candu_2_0.png)
