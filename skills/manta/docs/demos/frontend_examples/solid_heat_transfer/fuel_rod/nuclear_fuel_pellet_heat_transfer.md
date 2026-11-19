<!-- source: https://manta-project.gitlab.io/manta/demos/frontend_examples/solid_heat_transfer/fuel_rod/nuclear_fuel_pellet_heat_transfer.html -->

# Multiple material simulation: `nuclear_fuel_rod` example

In this tutorial we will show how to calculate the temperature profile
in the fuel rod of a Pressurized Water Reactor (PWR). Such a fuel rod is
made of a stack of almost cylindrical pellets made of Uranium Dioxide
enclosed in a cladding made of an alloy of Zirconium. The fuel rod is
pressurized with helium which fills the space left between the fuel rods
and the cladding.

Except in the conclusion, only one pellet is considered in this tutorial.
Following common practices in fuel performance codes,
various modeling hypotheses are considered:

- the \(2D\left(r, \theta\right)\) and \(3D\) hypotheses
  allow to take into account the fact that the pellet is
  divided into fragments during the reactor start-up. Note that
  due to the simplified assumptions made in this tutorial,
  this fragmentation has no impact on the results presented
  hereafter.
- the \(2D\left(r, z\right)\) and \(3D\) hypotheses
  allow to take into account the real geometry of the pellet,
  i.e. the chamfer and the dishing (see bellow).

The input files of each cases are very similar, so only the
\(2D\left(r, \theta\right)\) is detailed in depth in the following.

Warning

The computations are based on a (very) simplified model, especially when compared
to the models used in fuel performance codes developed in the PLEIADES
platform [[BRLM24](../../../../references/references.md#id5), [MRV+21](../../../../references/references.md#id4)].

Note

This tutorial is based on a pratical work given during the Master 2
Materials Science for Nuclear Energy (INP Grenoble - Phelma 2)
[[HBE20](../../../../references/references.md#id3)].

Note

The following MFront files are required to run all the simulations

- [`CladdingHeatTransfer.mfront`](https://manta-project.gitlab.io/manta/_downloads/aba0b76cafca006366c7f69e3bf828e0/CladdingHeatTransfer.mfront): the MFront implementation of the thermal conductivity of the cladding
- [`GasHeatTransfer.mfront`](https://manta-project.gitlab.io/manta/_downloads/95f249a09cdac6794c968b920ae49198/GasHeatTransfer.mfront): the MFront implementation of the thermal conductivity of the gas
- [`UO2HeatTransfer.mfront`](https://manta-project.gitlab.io/manta/_downloads/e1e5315f03fbf1646a1c4678aedd90b1/UO2HeatTransfer.mfront): the MFront implementation of the thermal conductivity of the fuel

The following files are required to run the tutorial for 2d in plane simulation:

- [`mesh_2d_inplane.dgibi`](https://manta-project.gitlab.io/manta/_downloads/c645c3b7d7bbef3e493e921408b5effb/mesh_2d_inplane.dgibi):
  the Cast3M input file required to generate the mesh.
- [`nuclear_fuel_pellet_2D_inplane.py`](https://manta-project.gitlab.io/manta/_downloads/3db7f11c2a12d0941d6ca3fa4241912d/nuclear_fuel_pellet_2D_inplane.py): the main script

The following files are required to run the tutorial for 2d axisymmetrical simulation:

- [`mesh_2d_axisymmetrical.dgibi`](https://manta-project.gitlab.io/manta/_downloads/b472d225bb3817edfff14a5e096c1e12/mesh_2d_axisymmetrical.dgibi):
  the Cast3M input file required to generate the mesh.
- [`nuclear_fuel_pellet_2D_axisymmetrical.py`](https://manta-project.gitlab.io/manta/_downloads/aaafe4960759d03306119c471915e8f0/nuclear_fuel_pellet_2D_axisymmetrical.py): the main script

The following files are required to run the tutorial for 2d axisymmetrical simulation with chamfer:

- [`mesh_2d_axisymmetrical_chamfer.dgibi`](https://manta-project.gitlab.io/manta/_downloads/44f9732f676d83cf02189a5bc6eeab38/mesh_2d_axisymmetrical_chamfer.dgibi):
  the Cast3M input file required to generate the mesh.
- [`nuclear_fuel_pellet_2D_axisymmetrical_chamfer.py`](https://manta-project.gitlab.io/manta/_downloads/e474763fcd99a29972386b114a13d1da/nuclear_fuel_pellet_2D_axisymmetrical_chamfer.py): the main script

The following files are required to run the tutorial for 3d simulation:

- [`mesh_3d.dgibi`](https://manta-project.gitlab.io/manta/_downloads/84d00f21abaf39e0e82acbc1d76c1eb4/mesh_3d.dgibi):
  the Cast3M input file required to generate the mesh.
- [`nuclear_fuel_pellet_3D.py`](https://manta-project.gitlab.io/manta/_downloads/29ae7e3996b07ac04a10731f76614fcd/nuclear_fuel_pellet_3D.py): the main script

The following files are required to run the tutorial for 3d simulation with chamfer:

- [`mesh_3d_chamfer.dgibi`](https://manta-project.gitlab.io/manta/_downloads/2b35776cc3537e5eefa167fcc483eb79/mesh_3d_chamfer.dgibi):
  the Cast3M input file required to generate the mesh.
- [`nuclear_fuel_pellet_3D_chamfer.py`](https://manta-project.gitlab.io/manta/_downloads/92b0d1b657cbab8945b9537ca4724740/nuclear_fuel_pellet_3D_chamfer.py): the main script

## Description

### Geometry

[![figure](https://manta-project.gitlab.io/manta/_images/meshes.png)](https://manta-project.gitlab.io/manta/_images/meshes.png)

Fig. 12 On the left, the geometry used in \(2D(r,\theta)\).
On the right, a typical \(2D(r, z)\) mesh.

[Fig. 12](#material-for-nuclear-fuel-pellet-heat-transfer) depicts the
geometry used for \(2D(r,\theta)\) calculations of the fuel rod. The
radius of the fuel \(R_f\) is equal to \(4.0\;mm\), of inner
radius of the cladding \(R_i\) is equal to \(4.2\;mm\) while the
external radius of the cladding \(R_e\) is equal to \(4.4\;mm\).
The geometrical values defining the chamfer and the dishing are given in
the mesh files when required.

[Fig. 12](#material-for-nuclear-fuel-pellet-heat-transfer) also depicts
a typical \(2D(r, z)\) mesh used in the `Alcyone` fuel
performance code is depicted. One may notice the dishing and the
chamfer. The cladding mesh is axially greater than the pellet mesh
to accomodate the difference in axial expansions under
irradidation.

### Boundary conditions

The external temperature, corresponding to the temperature at \(r =
R_e\), is fixed and equal to \(T_e = 614.15\; K\). The heat source
produced by the fuel is set to \(q_f=3.10^{8}\;W/m^{3}\)

### Materials

The nonlinear thermal conductivity laws are given:

- for the \(UO_2\) fuel by

  \[k_f(T) = \frac{1}{A_{f} + B_{f} \cdot T}\]

  with \(A_{f} = 0.0375\) and \(B_{f} = 2.165\cdot 10^{-4}\),
- for the gas by

  \[k_g (T) = A_g T^{n_g}\]

  where \(A_g = 2.8424 \cdot 10^{-4}\) and \(n_g = 0.7\).

The thermal conductivity of the cladding is assumed constant, equal to
\(16\).

### Analytical solutions

In the absence of chamfer and dishing, it is possible to establish
analytical solutions for the temperature profiles in the various
materials:

- the temperature in the cladding is given by:

  \[T(r) = T_e + \frac{Q_f}{4 k_c} \log \Big(\frac{r}{R_i}\Big)\]

  where \(Q_f= q_f R_{f}^{2}/2\),
- the temperature in the gas is given by:

  \[T(r) = \sqrt[{n_g + 1}]{T(R_f)^{n_g + 1} - \frac{n_g +1}{A_g}Q_f \log\Big( \frac{r}{R_C} \Big)}\]
- the temperature in the fuel is given by:

  \[T(r) = \frac{1}{B_f} \Bigg([A_f + B_f \;T_0] \exp{\Bigg(-\frac{q_f\,B_f}{2C_f}r^{2}\Bigg)} - A_f \Bigg)\]

  where \(T_0\) is the temperature in the center of the fuel.

In practice, one uses the first profile to determine the temperature at
the inner boundary of the cladding, then the second expression to
determine the temperature at the outer surface of the pellet and the
last one to determine the temperature in the center of the pellet.

Such expressions are useful to verify the implementation, even if the
\(2D\left(r, z\right)\) and \(3D\) simulations require to
consider a simplified geometry for the comparisons to be meaningful.

## Implementation

First, multiple materials need to be declared at the beginning of the physical system definition:

```python
ps = manta.PhysicalSystem(mesh = {'file': '../mesh/mesh_2d_inplane.med',
                                  'domains': ['GAS','FUEL','CLADDING'],
                                  'boundaries': ['0SOO', '1SOI', '1SOO', '1LR01',
                                                 '1LR02','0LR01','0LR02','BottomLineGAS',
                                                 'BottomLineCLADDING']},
                          geometricHypothesis = 'inPlane')
```

where the gas, fuel and cladding are three distinct materials defined in the med file.

Then, when declaring material behavior defined in MFront, we need to match the behavior with the material as follow:

```python
mth.add('SolidMaterial', material = 'GAS', library = './src/libBehaviour.so',
        behavior = 'GasHeatTransfer', hypothesis = 'PlaneStrain')

mth.add('SolidMaterial', material = 'FUEL', library = './src/libBehaviour.so',
        behavior = 'UO2HeatTransfer', hypothesis = 'PlaneStrain')
        
mth.add('SolidMaterial', material = 'CLADDING', library = './src/libBehaviour.so',
        behavior = 'CladdingHeatTransfer', hypothesis = 'PlaneStrain')
```

where each material as it's own behavior that can be linear (for the cladding) or non-linear.

Since the heat source is only defined in the fuel, it is simply declared as

```python
mth.add('HeatSource', material = 'FUEL',
        value = 'PowerDensity', configuration = 'reference')
```

Finally, to post-process the temperature field (VTK export) for all the domains, it is declared as

```python
ps.addPostProcessing('VTKExport',
                     outputFileBaseName = 'Temperature',
                     allTimeSteps = False,
                     fields = [{'field': 'Temperature', 'fieldType': 'nodeField', 'materials': ['GAS','FUEL','CLADDING']}])
```

## Execution

First, we build the MFront libraries with

```
$ mfront --obuild --interface=generic *HeatTransfer.mfront
```

We can generate the .med file using Cast3M:

```
$ castem24 mesh_2d_inplane.dgibi
```

and we finally can run the simulation with

```
$ python3 nuclear_fuel_pellet_2D_inplane.py
```

## Results

### Verifications tests

[![figure](https://manta-project.gitlab.io/manta/_images/Simulation_temp_field_results.png)](https://manta-project.gitlab.io/manta/_images/Simulation_temp_field_results.png)

Fig. 13 Temperature field for 2D in plane, 2D axisymmetrical and 3D simulations.
(Paraview)

[Fig. 13](#fig-fuel-rod-simulations-temp-field-results) shows the temperature
field calculated for the three considered modeling hypotheses.

[![figure](https://manta-project.gitlab.io/manta/_images/temperature_profil.png)](https://manta-project.gitlab.io/manta/_images/temperature_profil.png)

Fig. 14 Temperature conduction in the nuclear fuel pellet for
2d in plane, 2D axisymmetrical, 3D simulations and analytical solution.

[Fig. 14](#temperature-profil-nuclear-fuel-pellet) show the temperature
profile for all the geometric assumption and the analytical solution
using a simplified geometry. The numerical simulation gives good results
for all assumptions.

Note

A quantitative evaluation of the error between the analytical solution and
the calculated solutions is given by the evaluation of the \(L_{2}\)
distance, as detailed in Section
[Applied math: norms calculation for a linear thermal problem](../../numerical_analysis/norms_calculation/norms_calculation.md#applied-math-norms-calculation-for-linear-thermal-problem).

This evaluation is left as an exercise to the readers.

In order to further verify those calculations, we have calculated the
total heat flux through the external surface using the reaction on the
outer cladding boundary where the temperature is imposed, multiplied
by a geometric factor to take into account symmetries.

In a stationary setting, those values must be equal to the integral of
the heat source in the pellet (denoted *Analytical* in
[Table 15](#tbl-fuel-rod-total-heat-flux):).

Table 15 Total heat flux computed through the external surface

| Geometry | Total heat flux |
| --- | --- |
| 2D in plane | \(101.027\) |
| 2D axisymmetrical | \(101.034\) |
| 3D | \(100.711\) |
| Analytical | \(101.024\) |

### Results of the real geometry

[![figure](https://manta-project.gitlab.io/manta/_images/temperature_profil_comparison.png)](https://manta-project.gitlab.io/manta/_images/temperature_profil_comparison.png)

Fig. 15 Temperature conduction in the nuclear fuel pellet for
2D axisymmetrical and 3D simulations with inclusion of chamfer
and dishing and comparison with 2D axisymmetrical without.

[Fig. 15](#temperature-profil-comparison-chanfrein-nuclear-fuel-pellet)
emphasizes that some little geometric changes have an impact on the
solution. In this case, the total heat source is a bit lower since the
power density \(q\) has not been corrected to take into account the
dishing and the chamfer, leading to a lower temperature in the fuel.

Note

In practice, a common input in fuel performance codes is the linear
power, i.e. the heat source per unit of fuel length
(in the axial direction). The linear power is converted into a power
density using the real geometries and a neutronic model takes
into account the fact that nuclear fissions and uranium consumptions
are not homogeneous inside the fuel pellet.

## Conclusion

As mentioned in the introduction, the simulations presented in this
tutorial are crude compared to the myriad of multi-physics phenomena
taken into account in fuel performance codes.

[![figure](https://manta-project.gitlab.io/manta/_images/multi-pastilles.png)](https://manta-project.gitlab.io/manta/_images/multi-pastilles.png)

Fig. 16 Simulation of the full 3D domain with 2 pellets.

However, this tutorial paves the way toward more realistic computations.
Interestingly, [Fig. 16](#temperature-profil-multi-pastilles) shows that
the scripts presented here can be adapted straightforwardly to describe
several pellets.
