<!-- source: https://tripoli5.asnr.dev/documentation/latest-release/examples/geometries/superphenix_assembly.html -->

# Superphénix assembly

Wa have selected a Superphénix (Sodium Fast Reactor, SFR) fuel assembly configuration with specifications taken from Ref. [1].

The assembly contains 271 fuel pins, arranged in 10 concentric rings and immersed in sodium.

A steel casing surrounds the assembly.

[1] A. Ponomarev, A. Bednarova, and K. Mikityuk. “New sodium fast reactor neutronics benchmark”. In: Proc. of the Physor 2018 conference. Cancun, Mexico, 2018.

```ipython3
import tripoli5
import numpy as np
from tripoli5.core.euclide import Point, Vector

# fissile pellet
void_radius = 0.1
fuel_or = 0.357
clad_ir = 0.3685
clad_or = 0.4292

# assembly
hexcan_pitch = 17.3
hexcan_cladding_width = 0.45
nb_rings = 10
hexcan_pitch_lattice = 0.98

fuel_elem_height = 0.0
nb_axial = 0

inner_hexcan_radius = (hexcan_pitch / 2.0) - hexcan_cladding_width
outer_hexcan_radius = hexcan_pitch / 2.0

ur_i = tripoli5.agora.Plane(np.sqrt(3) / 2, 0.5, 0, inner_hexcan_radius)  # upper right
ul_i = tripoli5.agora.Plane(-np.sqrt(3) / 2, 0.5, 0, -inner_hexcan_radius)  # upper left
bl_i = tripoli5.agora.Plane(
    -np.sqrt(3) / 2, -0.5, 0, inner_hexcan_radius
)  # bottom left
br_i = tripoli5.agora.Plane(
    np.sqrt(3) / 2, -0.5, 0, -inner_hexcan_radius
)  # bottom right
up_i = tripoli5.agora.YPlane(inner_hexcan_radius)
down_i = tripoli5.agora.YPlane(-inner_hexcan_radius)

inner_hexcan_region = (
    -bl_i & +ul_i & -up_i & -ur_i & +br_i & +down_i
)  # inner region of the hexcan assembly
s_inner_hexcan = tripoli5.agora.Shape(inner_hexcan_region)  # inner = TRUE

ur_o = tripoli5.agora.Plane(np.sqrt(3) / 2, 0.5, 0, outer_hexcan_radius)  # upper right
ul_o = tripoli5.agora.Plane(-np.sqrt(3) / 2, 0.5, 0, -outer_hexcan_radius)  # upper left
bl_o = tripoli5.agora.Plane(
    -np.sqrt(3) / 2, -0.5, 0, outer_hexcan_radius
)  # bottom left
br_o = tripoli5.agora.Plane(
    np.sqrt(3) / 2, -0.5, 0, -outer_hexcan_radius
)  # bottom right
up_o = tripoli5.agora.YPlane(outer_hexcan_radius)
down_o = tripoli5.agora.YPlane(-outer_hexcan_radius)

outer_hexcan_region = (
    -bl_o & +ul_o & -up_o & -ur_o & +br_o & +down_o
)  # inner region of the hexcan assembly (including cladding)
s_outer_hexcan = tripoli5.agora.Shape(
    -inner_hexcan_region & +outer_hexcan_region
)  # OUTER = TRUE

r_void = tripoli5.agora.ZCylinder(0.0, 0.0, void_radius)
r_fuel = tripoli5.agora.ZCylinder(0.0, 0.0, fuel_or)
r_gap = tripoli5.agora.ZCylinder(0.0, 0.0, clad_ir)
r_clad = tripoli5.agora.ZCylinder(0.0, 0.0, clad_or)

s_void = tripoli5.agora.Shape(-r_void)
s_fuel = tripoli5.agora.Shape(-r_fuel & +r_void)
s_gap = tripoli5.agora.Shape(+r_fuel & -r_gap)
s_clad = tripoli5.agora.Shape(+r_gap & -r_clad)
s_sodium = tripoli5.agora.Shape(+r_clad)

v_void = tripoli5.agora.Volume(s_void, "void")
v_fuel = tripoli5.agora.Volume(s_fuel, "fuel")
v_gap = tripoli5.agora.Volume(s_gap, "void")
v_clad = tripoli5.agora.Volume(s_clad, "clad")
v_sodium = tripoli5.agora.Volume(s_sodium, "sodium")

fissile_pin_universe = tripoli5.agora.Universe(
    [v_void, v_fuel, v_gap, v_clad, v_sodium]
)

center_point = Point(0.0, 0.0, 0.0)
background_universe = tripoli5.agora.createInfinite(material="sodium")

hex_lattice = tripoli5.agora.HexLattice(
    point=center_point,
    hex_pitch=hexcan_pitch_lattice,
    axial_pitch=fuel_elem_height,
    nb_rings=nb_rings,
    n_axial=nb_axial,
    universe=fissile_pin_universe,
    outer_universe=background_universe,
    label="hexcan_lattice",
)

rot = tripoli5.core.euclide.Rotation(Vector(0.0, 180.0, 90.0))
transf = tripoli5.core.euclide.AffineTransformation(None, rot)

lattice_volume = tripoli5.agora.CompositeVolume(
    s_inner_hexcan, filler=hex_lattice, affinetransformation=transf
)
hexcan_clad_volume = tripoli5.agora.Volume(s_outer_hexcan, material="clad")

root_universe = tripoli5.agora.Universe([lattice_volume, hexcan_clad_volume])

bcs = tripoli5.agora.BoundaryConditions()
reflecting_bc = tripoli5.agora.ReflectionBoundaryCondition()

bcs.add(ul_o, reflecting_bc)
bcs.add(ur_o, reflecting_bc)
bcs.add(br_o, reflecting_bc)
bcs.add(bl_o, reflecting_bc)
bcs.add(down_o, reflecting_bc)
bcs.add(up_o, reflecting_bc)

geo = tripoli5.agora.Geometry(root_universe, boundary_conditions=bcs)
```

```ipython3
plotter = tripoli5.geoplotter.GeoPlotterPyplot(geo)
frame = tripoli5.geoplotter.Frame.fromMinMax(
    "XY", altitude=0.0, u_min=-11, u_max=11.0, v_min=-11.0, v_max=11
)
_ = plotter.plot(frame=frame, resolution=40)
```

![figure](https://tripoli5.asnr.dev/documentation/latest-release/_images/examples_geometries_superphenix_assembly_2_0.png)
