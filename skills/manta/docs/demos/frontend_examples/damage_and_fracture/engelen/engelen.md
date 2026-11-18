<!-- source: https://manta-project.gitlab.io/manta/demos/frontend_examples/damage_and_fracture/engelen/engelen.html -->

# Double notched plate described by a nonlocal implicit gradient-enhanced plastic law

This test is based on the paper of Feld-Payet et al.
[[FPBF11](../../../../references/references.md#id14)].

[![figure](https://manta-project.gitlab.io/manta/_images/double_notched_plate.svg)](../../../../_images/double_notched_plate.svg)

Fig. 25 Description of the geometry of the double notched plate and boundary conditions.

The test case considered is a double notched plate described by nonlocal
implicit gradient-enhanced law inspired by the work of Engelen et al
[[EGB03](../../../../references/references.md#id13)]. The geometry of the plate and the
loading considered are depicted on [Fig. 25](#fig-double-notched-plate).

Note

The following files are required to run the tutorial:

- [`mesh.dgibi`](../../../../_downloads/cb17055a488b64160e78996a7330a554/mesh.dgibi):
  the `Cast3M` input file required to generated the mesh.
- [`EngelenNonLocalElastoPlasticity.mfront`](../../../../_downloads/b280884116f9aac7d5a04ed12ec30852/EngelenNonLocalElastoPlasticity.mfront): the MFront implementation of the mechanical behavior
- [`Engelen.py`](../../../../_downloads/c5c66a052996c4960452f0a675e71092/Engelen.py): the main script

Warning

In many situations involving large plastic strains, spurious
numerical artifacts may degrade the quality of the solution
when using standard finite elements. As of Release 0.1,
no solution is available in the MANTA's frontend to mitigate
such effects.

## [Description](#id6)

### [Geometry](#id7)

Table 19 Main parameters used in this test

|  |  |
| --- | --- |
| Length \(L\) | \(10\,\cdot\,10^{-3}\) m |
| Length \(l\) | \(10\,\cdot\,10^{-3}-2.5\,\cdot\,10^{-3}\) m |
| Radius \(R\) | \(1\) mm |

The geometry of the plate is a square in which two circular notches were
introduced:

- the radius of the notches is denoted \(R\),
- the length of the square, before the introduction of notches, is
  denoted \(L\),
- the center of the notches is determined by the length \(l\) of one
  of the (vertical or horizontal) side of the plate after the
  introduction of the notches.

The values used in this are reported on [Table 19](#double-notched-plate-geometric-parameters).

### [Boundary conditions](#id8)

The plate is clamped on its bottom side and on its right side. On its
left side, only the horizontal displacements are blocked.

A uniform vertical displacement is imposed on its top boundary. This
displacement is imposed gradually up to a final value of
\(7.83\,\cdot\,10^{-2}\) mm.

### [Mechanical behavior](#id9)

To perform a finite strain analysis, the mechanical behavior is
expressed in the logarithmic strain framework. See
[[MAL02](../../../../references/references.md#id12)] for details.

The plate is assumed isotropic and elasto-plastic. The yield surface
\(f\) is given by:

\[f\left(\sigma_{\mathrm{eq}}, p, \kappa\right) = g\left(\kappa\right)\,\left(s_{0}+H\,p\right)\]

where:

- \(\sigma_{\mathrm{eq}}\) is the von Mises norm of the dual stress
  of the logarithmic strain.
- \(p\) is the equivalent plastic strain,
- \(\kappa\) is the maximum value in time of the non local
  counterpart of the equivalent plastic strain \(\bar{p}\), as
  defined below. In other words,

  \[\kappa = \mathop{max}_{\tau<t}\, \bar{p}\left(\tau\right)\]

  where \(t\) denotes the time.
- \(s_{0}\) is the yield strength of the undamaged material,
- \(H\) is the hardening slope of of the undamaged material,
- \(g\left(\kappa\right)\) is a degradation function defined by:

  \[g = \mathop{max}\left(1 - \frac{\kappa}{\kappa_{r}}, \epsilon_{g}\right),\]

  \(\kappa_r\) is a material threshold that, when reached, indicates that
  the material is broken. \(\epsilon_{g}\) being a small numerical value that avoids
  a complete degradation of the material. In this test, \(\epsilon_{g}\)
  is chosen equal to \(10^{-8}\).

The non local equivalent plastic strain is defined by the implicit
gradient approach, i.e. \(\bar{p}\) satisfies a linear Helmoltz
equation:

\[\bar{p} - l_{c}^{2} \Delta \bar{p} = p\]

Table 20 Main parameters used in this test

|  |  |
| --- | --- |
| Young's modulus | \(183\,\cdot\,10^{9}\) Pa |
| Poisson's ratio | \(0.3\) |
| Yield strength \(s_{0}\) | \(443e6\) Pa |
| Hardening slope \(H\) | \(300e6\) Pa |
| \(\kappa_{r}\) | \(0.1\) |
| characteristic length \(l_{c}\) | \(\sqrt{8\,10^{-8}}\) m |

The material parameters used in this test are reported on
[Table 20](#double-notched-plate-material-parameters).

## [Description of the MANTA input file](#id10)

The test cases begins by importing the `manta` module:

```python
import manta
```

Next, we define the material parameters of the study, according to
[Table 20](#double-notched-plate-material-parameters):

```python
lc = 0.08e-6 ** 0.5

material_properties = {"YoungModulus": 183e9,
                       "PoissonRatio": 0.3,
                       "UltimateNonLocalEquivalentPlasticStrain" : 0.1,
                       "YieldStrength": 443e6,
                       "HardeningSlope": 300e6}
```

The maximal value of the imposed displacement and the number of time
steps are then defined:

```python
# number of time step
nsteps = 300
# maximal imposed displacement
umax = 7.83e-5
```

### [Definition of the physical system](#id11)

The next step is to define a physical system. The `Cast3M` script
generates a `MED` file that is imported as follows:

```python
ps = manta.PhysicalSystem(mesh = {'file': 'mesh.med',
                                  'domains': ['plate'],
                                  'boundaries': ['bottom', 'top', 'left', 'right']},
                          geometricHypothesis = 'inPlane')
```

The geometric hypothesis is used to specify that the problem considered
is not axisymmetrical.

See Section [Physical system](../../../../manta_frontend_user_guide/physical_system/physical_system.md#physical-system) for further details.

### [Declaration of the material properties](#id12)

Once the physical system is defined, we can immediately define the
material properties:

```python
for n, v in material_properties.items():
    ps.addProperty('Constant', material = 'plate', name = n, value = v)
```

See Section [Properties](../../../../manta_frontend_user_guide/properties.md#properties) for further details.

### [Mechanical model, behavior and boundary conditions](#id13)

The mechanical model is instanciated as follows:

```python
mechanics = manta.Model('ImplicitMechanics', ps,
                        nonlinearSolver = {'Newton': {'switchFromRelativeToAbsoluteCriterion': True,
                                                      'thresholdOnTheFirstResidualNorm': 1e-100,
                                                      'convergenceTolerances': {'relativeConvergenceTolerance': 1e-4},
                                                      'maximumNumberOfIterations': 50}})
```

The `Newton` solver is selected. As the staggered
algorithm may call the mechanical problem numerous times during the same
time step, special care shall be taken when selecting the convergence
criterion. The `switchFromRelativeToAbsoluteCriterion` parameter
forces the `Newton` solver to use a relative criterion with a
tolerance \(\epsilon_{r}\) for the first resolution in a given time
step and keeps the initial residual norm \(R_{0}\) in memory to
switch to an absolute criterion for the new resolutions on the same time
step, the absolute tolerance then used is \(R_{0}\,\epsilon_{r}\).

See Sections [Generalities on models](../../../../manta_frontend_user_guide/models/generalities.md#generalities-on-models) and [Solid mechanics models](../../../../manta_frontend_user_guide/models/solid_mechanics/solid_mechanics.md#solid-mechanics-models)
for further details.

The brick describing the mechanical behavior of the plate is then
defined by calling an external MFront behavior that shall be compiled
before running the simulation:

```python
mechanics.add('SolidMaterial', material = 'plate',
              library = 'src/libBehaviour.so', behavior = 'EngelenNonLocalElastoPlasticity', hypothesis = 'planeStrain')
```

Bricks associated with boundary conditions are then added to the model,
as follows:

```python
mechanics.add('ImposedDisplacement', boundary = 'bottom', components = ['UX', 'UY'])
mechanics.add('ImposedDisplacement', boundary = 'right', components = ['UX', 'UY'])
mechanics.add('ImposedDisplacement', boundary = 'left', component = 'UX')
mechanics.add('ImposedDisplacement', boundary = 'top',
              component = 'UY',
              reaction = 'ReactionForce',
              value = 'ImposedDisplacementValue')
```

See Section [Solid mechanics bricks](../../../../manta_frontend_user_guide/bricks/solid_mechanics/solid_mechanics_bricks.md#solid-mechanics-bricks) for further details.

A loading evolution is used to define the evolution of the imposed displacement:

```python
ps.addLoadingEvolution('ImposedDisplacementValue',
                       lambda t: umax * t)
```

See Section [Loadings](../../../../manta_frontend_user_guide/loadings.md#loadings) for further details.

### [Computation of the non local equivalent plastic strain](#id14)

The non local equivalent plastic strain can be defined using the
auxiliary task (i.e. a model with no physical meaning) named
`L2ProjectionAuxiliaryTask`. This auxiliary task is declared as
follows:

```python
smoother = manta.Model('L2ProjectionAuxiliaryTask', ps,
                       value = 'EquivalentPlasticStrain',
                       result = 'NonLocalEquivalentPlasticStrain',
                       domain = 'plate',
                       characteristicLength = lc)
```

See Section [The L2Projection auxiliary task](../../../../manta_frontend_user_guide/auxiliary_tasks/l2_projection_auxiliary_task.md#l2-projection-auxiliary-taks) for further details.

In the following, this auxiliary task is referred to as the smoother.

### [Declaration of the coupling scheme](#id15)

The coupling is defined as follows:

```python
cs = manta.CouplingScheme('IterativeCouplingScheme', ps,
                          maximumNumberOfIterations = 500)

cs.add(mechanics)
cs.add(smoother)
cs.addConvergenceCriterion('StationaryResult',
                           fields = [{'field': 'NonLocalEquivalentPlasticStrain', 'fieldType': 'nodeField', 'material': 'plate'}],
                           tolerance = 1e-5)

ps.setCouplingScheme(cs)
```

The `IterativeCouplingScheme` declares a fixed point algorithm
which, at each time step, calls the mechanical model and the smoother
alternatively up to convergence. The mechanical model is called knowing
the non local equivalent plastic strain value from the previous
iteration of the fixed point algorithm and the smoother is called
knowing the updated values of the (local) equivalent plastic strain
computed by the mechanical model.

The convergence criterion `StationaryResults` is only satisfied if
the absolute value of correction to the non local equivalent plastic
strain between two iterations of the fixed point algorithm is on each
nodes below a threshold chosen equal to \(10^{-5}\).

### [Post-processings](#id16)

Two post-processings are defined in this example:

- The first one exports the displacement and the local equivalent plastic
  strain \(p\) in a `VTK` file. This `VTK`
  file can be opened with `paraview` for instance.
- The second post-processing exports some values into a `txt` file
  which will contain the reaction at the upper boundary.

```python
ps.addPostProcessing('VTKExport',
                     outputFileBaseName = 'results',
                     fields = [{'field': 'Displacement', 'fieldType': 'nodeField', 'material': 'plate'},
                               {'field': 'EquivalentPlasticStrain', 'fieldType': 'ipField', 'material': 'plate'}])
ps.addPostProcessing('Curves',
                     file = 'force.res',
                     fileFormat = 'txt',
                     curves = [{'Value': {'value': 'ReactionForce[FY]',
                                          'location': 'top'}}])
```

See Section [Post-processings](../../../../manta_frontend_user_guide/post_processings/post_processings.md#post-processings) for further details.

### [Time discretization and simulation](#id17)

To reduce the computational time, a coarse time discretization is used
between times \(0\) and \(0.3\), and a finer one between
\(0.3\) and \(1\):

- \(5\) temporal sequences are defined between \(0\) and \(0.3\),
- `nsteps` temporal sequences are defined between \(0.3\) and
  \(1\).

The next lines instantiates a `Simulation` object and starts the
simulation:

```python
s = manta.Simulation(ps, times = [0.3 * i / 6  for i in range(0, 6)] +
                     [0.3 + 0.7 * i / nsteps for i in range(0, nsteps + 1)],
                     allowSubStepping = False)
s.run()
```

See Section [Simulation](../../../../manta_frontend_user_guide/simulation/simulation.md#simulation) for further details.

## [Results](#id18)

[![figure](https://manta-project.gitlab.io/manta/_images/degradation_function.png)](../../../../_images/degradation_function.png)

Fig. 26 Degradation function at the end of the simulation.
MANTA's results (left) vs `mgis.fenics`'s results.

The maps of the degradation function at the end of the simulation
computed by MANTA's and `mgis.fenics` are reported on
[Fig. 26](#fig-double-notched-plate-degradation-function). Although both
maps looks similar, damage is more pronounced in the
`mgis.fenics`'s case.

[![figure](https://manta-project.gitlab.io/manta/_images/force.svg)](../../../../_images/force.svg)

Fig. 27 Evolution of the imposed force during the simulation, as
computed by MANTA's and `mgis.fenics`.

More quantitatively,
[Fig. 27](#fig-double-notched-plate-degradation-force) compares the
evolution of the imposed force during the simulation, as computed by
MANTA's and `mgis.fenics`. Although results prior to softening
are in very good agreement, the evolution after the maximum force
differs slightly and confirms a greater degradation of the material in
`mgis.fenics`'s case. .

A rigorous comparison between those simulations would require to use the
same mesh, same convergence criteria (the convergence criteria in
MANTA is somehow more stringent), etc. It would also require to ensure
that no spurious phenomena, such as volumetric locking, degrade the
quality of the solutions.
