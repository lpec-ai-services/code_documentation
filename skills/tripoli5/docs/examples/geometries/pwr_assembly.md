<!-- source: https://tripoli5.asnr.dev/documentation/latest-release/examples/geometries/pwr_assembly.html -->

# PWR fuel assembly

We have chosen two UOX and MOX fuel assembly configurations with specifications taken from Ref. [51]. The geometry of the two configurations is identical, with 17 × 17 pin-cells including 25 water holes, but the material compositions of the fuel are of course different. A water blade surrounds the assembly. The fuel is at 900 K, and the structures and the moderator are at 600 K.

```ipython3
import tripoli5
from tripoli5.core.euclide import Point, Vector

# Instantiate ZCylinder surfaces
fuel_or = tripoli5.agora.ZCylinder(0.0, 0.0, 0.41266)
clad_ir = tripoli5.agora.ZCylinder(0.0, 0.0, 0.41690)
clad_or = tripoli5.agora.ZCylinder(0.0, 0.0, 0.47436)

# Create a fuel pin universe
s_fuel = tripoli5.agora.Shape(-fuel_or)
fuel_cell = tripoli5.agora.Volume(s_fuel, "FUEL")
s_gap = tripoli5.agora.Shape(+fuel_or & -clad_ir)
gap_cell = tripoli5.agora.Volume(s_gap, "VOID")
s_clad = tripoli5.agora.Shape(+clad_ir & -clad_or)
clad_cell = tripoli5.agora.Volume(s_clad, "CLAD")
s_hot_water = tripoli5.agora.Shape(+clad_or)
hot_water_cell = tripoli5.agora.Volume(s_hot_water, "WATER")
fuel_pin_universe = tripoli5.agora.Universe(
    [fuel_cell, gap_cell, clad_cell, hot_water_cell]
)

# Instantiate ZCylinder surfaces
gtclad_ir = tripoli5.agora.ZCylinder(0, 0, 0.56343)
gtclad_or = tripoli5.agora.ZCylinder(0, 0, 0.6035)

# Create a control rod guide tube universe
s_water = tripoli5.agora.Shape(-gtclad_ir)
gt_inner_cell = tripoli5.agora.Volume(s_water, "WATER")
s_gt_clad = tripoli5.agora.Shape(+gtclad_ir & -gtclad_or)
gt_clad_cell = tripoli5.agora.Volume(s_gt_clad, "GTCLAD")
s_gt_hot_water = tripoli5.agora.Shape(+gtclad_or)
gt_outer_cell = tripoli5.agora.Volume(s_gt_hot_water, "WATER")
guide_tube_universe = tripoli5.agora.Universe(
    [gt_inner_cell, gt_clad_cell, gt_outer_cell]
)

pincell_pitch = 1.262082
nb_pincells = 17
pitch = pincell_pitch * nb_pincells

# Define the lower-left corner of the lattice
lower_left = Point(-pitch / 2, -pitch / 2, 0.0)

# Define the pitch vector for the lattice
lattice_pitch = Vector(pincell_pitch, pincell_pitch, 0.0)

# Create an infinite background universe filled with water
background_universe = tripoli5.agora.createInfinite(material="WATER")

# Create a 17x17 array of universes
assembly = tripoli5.agora.RectLattice(
    point=lower_left,
    pitch=lattice_pitch,
    nx=nb_pincells,
    ny=nb_pincells,
    nz=0,
    universe=fuel_pin_universe,
    outer_universe=background_universe,
)

# Set guide tubes
assembly[5, 2, 0] = guide_tube_universe
assembly[8, 2, 0] = guide_tube_universe
assembly[11, 2, 0] = guide_tube_universe
assembly[3, 3, 0] = guide_tube_universe
assembly[13, 3, 0] = guide_tube_universe
assembly[2, 5, 0] = guide_tube_universe
assembly[5, 5, 0] = guide_tube_universe
assembly[8, 5, 0] = guide_tube_universe
assembly[11, 5, 0] = guide_tube_universe
assembly[14, 5, 0] = guide_tube_universe
assembly[2, 8, 0] = guide_tube_universe
assembly[5, 8, 0] = guide_tube_universe
assembly[8, 8, 0] = guide_tube_universe
assembly[11, 8, 0] = guide_tube_universe
assembly[14, 8, 0] = guide_tube_universe
assembly[2, 11, 0] = guide_tube_universe
assembly[5, 11, 0] = guide_tube_universe
assembly[8, 11, 0] = guide_tube_universe
assembly[11, 11, 0] = guide_tube_universe
assembly[14, 11, 0] = guide_tube_universe
assembly[3, 13, 0] = guide_tube_universe
assembly[13, 13, 0] = guide_tube_universe
assembly[5, 14, 0] = guide_tube_universe
assembly[8, 14, 0] = guide_tube_universe
assembly[11, 14, 0] = guide_tube_universe

water_blade_thickness = 0.07792594
total_side = pitch + 2.0 * water_blade_thickness

# Create boundary planes to surround the geometry
min_x = tripoli5.agora.XPlane(-total_side / 2)
max_x = tripoli5.agora.XPlane(+total_side / 2)
min_y = tripoli5.agora.YPlane(-total_side / 2)
max_y = tripoli5.agora.YPlane(+total_side / 2)

root_shape = tripoli5.agora.Shape(+min_x & -max_x & +min_y & -max_y)

lattice_volume = tripoli5.agora.CompositeVolume(shape=root_shape, filler=assembly)

root_universe = tripoli5.agora.Universe([lattice_volume])

bcs = tripoli5.agora.BoundaryConditions()
reflecting_bc = tripoli5.agora.ReflectionBoundaryCondition()

bcs.add(min_x, reflecting_bc)
bcs.add(max_x, reflecting_bc)
bcs.add(min_y, reflecting_bc)
bcs.add(max_y, reflecting_bc)

geo = tripoli5.agora.Geometry(root_universe, boundary_conditions=bcs)
```

```ipython3
plotter = tripoli5.geoplotter.GeoPlotterPyplot(geo)
frame = tripoli5.geoplotter.Frame.fromMinMax(
    "XY",
    altitude=0.0,
    u_min=-total_side / 2,
    u_max=total_side / 2,
    v_min=-total_side / 2,
    v_max=total_side / 2,
)
_ = plotter.plot(frame=frame, resolution=50)
```

![figure](https://tripoli5.asnr.dev/documentation/latest-release/_images/examples_geometries_pwr_assembly_2_0.png)
