<!-- source: https://manta-project.gitlab.io/manta/demos/frontend_examples/damage_and_fracture/mealor2-tp8/mealor2-tp8.html -->

# Ductile rupture of a notched bar using an implicit gradient regularization of the Gurson-Tvergaard-Needleman constitutive equations

This tutorial describes the ductile failure of a notched bar. The bar is
described by implicit gradient regularization of the
Gurson-Tvergaard-Needleman constitutive following the work of Tuham et
al. [[TFPQ+22](../../../../references/references.md#id10)].

Note

This tutorial is based on a pratical work given during the
[second MEALOR summer school](https://github.com/MEALORII/TP_MEALOR)
[[1]](#mealor) (see [[BBFP+23](../../../../references/references.md#id9)]). The original files are
available online here:
<https://github.com/MEALORII/TP_MEALOR>

Note

The following files are required to run the tutorial:

- [`mesh.dgibi`](../../../../_downloads/f9172a89b51c65bf6f50b6c5e9f3bb9c/mesh.dgibi):
  the `Cast3M` input file required to generated the mesh.
- [`ImplicitGradientGTN.mfront`](../../../../_downloads/305d802a30a16e7204630a06dbbfad64/ImplicitGradientGTN.mfront): the MFront implementation of the mechanical behaviour
- [`ImplicitGradientGTN.py`](../../../../_downloads/bb6f8b328cf924ee7563489b5dd7b0bf/ImplicitGradientGTN.py): the main script

Warning

In many situations involving large plastic strains, spurious
numerical artifacts may degrade the quality of the solution
when using standard finite elements. As of Release 0.1,
no robust solution is available in the MANTA's frontend
to mitigate such effects.

If this tutorial is to be considered for more serious work,
under integrated quadratic elements shall be at least
considered.

## [Description](#id12)

[![figure](https://manta-project.gitlab.io/manta/_images/mesh.svg)](../../../../_images/mesh.svg)

Fig. 28 Geometry and boundary conditions of the notched bar in an
\(2D(r,z)\) representation
(compared to standard conventions, this figure has been rotated
so that the axis of revolution \(Oz\) is horizontal).

### [Geometry of the notched bar](#id13)

The geometry of the notched bar is depicted on
[Fig. 28](#fig-mealor2-tp8-mesh).

Table 21 Geometric parameters

|  |  |
| --- | --- |
| Half-height of the specimen \(L\) | \(10\) mm |
| Maximum diameter \(\Phi\) | \(2.2\) mm |
| Minimum diameter \(\Phi_{0}\) | \(2.2\) mm |
| Notch radius \(R\) | \(0.92\) mm |

The main geometric parameters are reported on
[Table 21](#mealor2-tp8-geometric-parameters).

### [Boundary conditions](#id14)

As depicted on [Fig. 28](#fig-mealor2-tp8-mesh), the bar is submitted to
the following boundary conditions:

- The axial displacement of the bar is blocked on the bottom line
  (\(z=0\), beware of the fact that [Fig. 28](#fig-mealor2-tp8-mesh)
  has been rotated).
- A uniform displacement \(U\) is imposed gradually on the top line
  (\(z=L\)). The maximum value is equal to \(0.225\) mm.

Due to axisymmetrical hypothesis, no boundary condition in the radial
direction is needed.

### [Constitutive equations](#id15)

The Gurson-Tvergaard-Needleman constitutive equations, introduced by
Tvergaard and Needleman [[TN84](../../../../references/references.md#id11)] extending the
work of Gurson [[Gur77](../../../../references/references.md#id8)], describes the ductile
failure of an isotropic material. To perform a finite strain analysis,
the mechanical behavior is expressed in the logarithmic strain
framework. See [[MAL02](../../../../references/references.md#id12)] for details.

The total strain of the material is split into an elastic part, used to
compute the stress through Hooke's law, and a plastic part which is now
detailed.

#### [Plasticity, effective stress](#id16)

The evolution of plastic strain of the material is governed by the
following yield surface:

\[f_{p}\left(\tsigma\right) = \sigma_{\star} - R\left(p\right)\]

where \(\sigma_{\star}\) is an effective equivalent stress, defined
below, \(p\) is the equivalent plastic strain and
\(R\left(p\right)\) describes the isotropic hardening of the
material. \(R\left(p\right)\) is defined below.

The plastic strain rate \(\underline{\dot{\varepsilon}}^{p}\) is
then given by the normality rule:

\[\underline{\dot{\varepsilon}}^{p}=
\dot{\lambda}\,\frac{\partial f_{p}}{\partial\tsigma}=
\dot{\lambda}\,\frac{\partial\sigma_{\star}}{\partial\tsigma}\]

where \(\dot{\lambda}\) is the plastic multiplier.

In porous plasticity, the equivalent plastic strain \(p\)
generally differs from the plastic multiplier \(\lambda\).
In the case of the Gurson-Tvergaard-Needleman constitutive equations,
the relationsip adopted is generally given by:

\[\dot{\lambda} = \left(1 -f\right)\,\dot{p}\]

where \(f\) is the porosity.

The effective equivalent stress \(\sigma_{\star}\) is defined
implicitly by the following relation:

\[\paren{\frac{\sigma_{eq}}{\sigma_{\star}} }^2 + 2 q_1 f_{\star} \cosh{\paren{\frac{3}{2} q_2 \frac{\sigma_m}{\sigma_{\star}} }} - 1 - q_3 f_{\star}^2 = 0\]

where:

- \(q_1\), \(q_2\) and \(q_3\) are material parameters. Note
  that the physical meaning of choosing a value of \(q_3\) different
  from \(q_1^2\) is doubtful.
- \(\sigma_{eq}\) is the von Mises equivalent stress,
- \(\sigma_m\) the hydrostatic pressure,
- the effective porosity \(f_{\star}\) is defined such that:

  \[\begin{split}f_{\star} = \left\{
  \begin{array}{ll}
  \delta f & \mbox{if } f < f_c \\
  f_c + \delta (f - f_c) & \mbox{otherwise}
  \end{array}
  \right.
  \quad
  \quad
  \text{with}
  \quad
  \quad
  \delta = \left\{
  \begin{array}{ll}
  1 & \mbox{if } f < f_c \\
  \frac{f_u- f_c }{f_r - f_c} & \mbox{otherwise}
  \end{array}
  \right.\end{split}\]

  where \(f_{u}\) is the root of \(2\,q_1\,f-1-q_3\,f^{2}\).

In this tutorial, the isotropic hardening rule \(R\left(p\right)\)
is given by a Voce law:

\[R\left(p\right) = R_{0}+{\left(R_{\infty}-R_{0}\right)}\,{\left(1-\exp(-b\,p)\right)}\]

#### [Evolution of the porosity, non local regularization](#id17)

The porosity \(f\) is decomposed into a nucleation porosity
\(f_{n}\) and a growth porosity \(f_{g}\):

\[f = f_{n} + f_{g}\]

In the local counterpart of the Gurson-Tvergaard-Needleman constitutive
equations, the porosity evolution is driven by the local plastic strain
rate. More precisely, this evolution is driven by:

- the rate of the change of the volume induced by the plastic flow
  \(\dot{\omega}\), given by:

  \[\dot{\omega}=
  \dot{\lambda}\,\mathrm{trace}\left(\frac{\partial f_{p}}{\partial\tsigma}\right)=
  \dot{\lambda}\,\mathrm{trace}\left(\frac{\partial\sigma_{\star}}{\partial\tsigma}\right)\]
- the equivalent plastic strain rate \(\dot{p}\).

The local behavior is known to be ill-posed with spurious
mesh-sensitivity of the results.

In the proposed non local version of the Gurson-Tvergaard-Needleman
constitutive equations, the evolution of the porosity is assumed to be
driven by two non local variables \(\dot{\bar{\omega}}\) and
\(\dot{\bar{p}}\) associated respectively with \(\dot{\omega}\)
and \(\dot{p}\).

More precisely, \(\bar{\omega}\) and \(\bar{p}\) are defined by
the following Helmoltz equations:

(161)\[\begin{split}\left\{
\begin{aligned}
-l_{c}^{2}\,\nabla^{2}\bar{\omega}+\bar{\omega} &= \omega \\
-l_{c}^{2}\,\nabla^{2}\bar{p}+\bar{p} &= p
\end{aligned}
\right.\end{split}\]

Compared to the work of Tuham et al. [[TFPQ+22](../../../../references/references.md#id10)], the
following differences can be highlighted:

- The Helmoltz equations are expressed in the reference
  configuration.
- For the sake of simplicity, the length scales \(l_{c}\) is the same
  for the two variables \(\bar{\omega}\) and \(\bar{p}\).

Note

For technical reasons related to how external state variables were
handled by the `dolphinx_materials` package
[[Ble24b](../../../../references/references.md#id6)], which was in its
early stage of developments during the MEALOR2 summer school,
Equations [(161)](#equation-mealor2-tp8-helmoltz-equations) were replaced by:

\[\begin{split}\left\{
\begin{aligned}
-l_{c}^{2}\,\nabla^{2}\Delta\,\bar{\omega}+\Delta\,\bar{\omega} &= \Delta\,\omega \\
-l_{c}^{2}\,\nabla^{2}\Delta\,\bar{p}+\Delta\,\bar{p} &= \Delta\,p
\end{aligned}
\right.\end{split}\]

where \(\Delta\,\bar{\omega}\) and \(\Delta\,\bar{p}\) denotes the
increments over the considered time step of \(\bar{\omega}\) and
\(\bar{p}\).

The evolution of the porosity is then given by replacing \(\bar{\omega}\)
and \(\bar{p}\) by their non local counterparts. Hence the evolution
of the nucleation porosity \(f_{n}\) and growth porosity \(f_{g}\) is given
by:

\[\begin{split}\left\{
\begin{aligned}
\dot{f_{n}}&=A_{n}{\left(\bar{p}\right)}\,\dot{\bar{p}} \\
\dot{f_{g}}&={\left(1-f_{g}\right)}\,\dot{\bar{\omega}}
\end{aligned}
\right.\end{split}\]

In the previous equation, \(A_{n}{\left(\bar{p}\right)}\) is given by
the Chu-Needleman model [[CN80](../../../../references/references.md#id7)]:

\[A_n{\left(\bar{p}\right)} = \frac{f_N}{s_N \sqrt{2\pi}} \exp{{\left(-\frac{1}{2} {\left(\frac{\bar{p} - \epsilon_N}{s_N} \right)}^2 \right)} }\]

where \(\{f_N,s_N,\epsilon_N\}\) are material parameters.

#### [Summary of the material parameters](#id18)

Table 22 Material parameters

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Young's modulus | Poisson's ratio | Yield strength \(R0\) | Ultimate yield strength \(R^{\infty}\) | \(b\) |
| \(210\,\cdot\,10^{3}\, MPa\) | \(0.3\) | \(507\, MPa\) | \(810\, MPa\) | \(9.14\) |
| \(f_c\) | \(f_r\) | \(q_1\) | \(q_2\) | \(q_3\) |
| \(0.1\) | \(0.25\) | \(1.5\) | \(1.\) | \(2.25\) |
| \(f_N\) | \(\epsilon_N\) | \(s_N\) | \(l_c\) |  |
| \(0.02\) | \(0.3\) | \(0.1\) | \(5\,\cdot\,10^{-2}\) mm |  |

The material parameters of the model are summarized in
[Table 22](#mealor2-tp8-material-parameters). The regularization length
\(l_{c}\) is chosen equal to \(5\,\cdot\,10^{-2}\,m\).

### [Initial state](#id19)

The initial porosity is assumed equal to \(4\,\cdot\,10^{-3}\).

## [Description of the MANTA input file](#id20)

The test cases begins by importing the `manta` module:

```python
import numpy as np
```

Next, we define the main parameters of the simulation, including the
maximum imposed displacement, the initial porosity, the regularization
length and the number of time steps:

```python
# imposed displacement (mm) at the end of the simulation
Umax = 1.5 * 0.15
# initial porosity
pini = 4e-3
# regularization length
lc = 0.05
# number of time steps
nsteps = 500
```

For post-processing purposes, we also declares the geometric parameters
according to [Table 21](#mealor2-tp8-geometric-parameters):

```python
# half-height of the specimen
height = 10
# maximum diameter
Phi = 2.2
# minmum diameter
Phi_0 = 1.23
```

### [Definition of the physical system](#id21)

The next step is to define a physical system. The `Cast3M` script
generates a `MED` file that is imported as follows:

```python
ps = manta.PhysicalSystem(mesh = {'file': 'mesh.med',
                                  'domains': ['beam'],
                                  'boundaries': ['bottom', 'top'],
                                  'nodes' : ['p0', 'p1']},
                          geometricHypothesis = 'axisymmetrical')
```

The geometric hypothesis is used to specify that the problem considered
is axisymmetrical.

See Section [Physical system](../../../../manta_frontend_user_guide/physical_system/physical_system.md#physical-system) for further details.

### [Mechanical model, behaviour and boundary conditions](#id22)

The mechanical model is instanciated as follows:

```python
mechanics = manta.Model('ImplicitMechanics', ps,
                        nonlinearSolver = {'Newton': {'switchFromRelativeToAbsoluteCriterion': True,
                                                      'thresholdOnTheFirstResidualNorm': 1e-100,
                                                      'convergenceTolerances': {'relativeConvergenceTolerance': 1e-4}}})
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

The brick describing the mechanical behavior of the bar is then
defined by calling an external MFront behaviour that shall be compiled
before running the simulation:

```python
mechanics.add('SolidMaterial', material = 'beam',
              library = 'src/libBehaviour.so', behavior = 'ImplicitGradientGTN')
```

Bricks associated with boundary conditions are then added to the model,
as follows:

```python
mechanics.add('ImposedDisplacement', boundary = 'bottom', component = 'UZ')
mechanics.add('ImposedDisplacement', boundary = 'top',
              component = 'UZ',
              reaction = 'ReactionForce',
              value = 'ImposedDisplacementValue')

def getImposedDiplacement(t: float):
    return Umax * t

ps.addLoadingEvolution('ImposedDisplacementValue', getImposedDiplacement)
```

In this tutorial, we define a function `getImposedDiplacement` to
get the imposed displacement for the given time, rather than using an
anonymous function: this function will be reused later to define a custom
post-processing.

See Sections [Solid mechanics bricks](../../../../manta_frontend_user_guide/bricks/solid_mechanics/solid_mechanics_bricks.md#solid-mechanics-bricks) and [Loadings](../../../../manta_frontend_user_guide/loadings.md#loadings) for
further details.

### [Computation of the non local equivalent plastic strain and non local plastic change of volume](#id23)

The increment of the non local variables
\(\Delta\,\bar{\omega}\) and \(\Delta\,\bar{p}\) can
be calculated using two instances of the auxiliary task (i.e. a model
with no physical meaning) named `L2ProjectionAuxiliaryTask`. Those
auxiliary tasks are declared as follows:

```python
smoother1 = manta.Model('L2ProjectionAuxiliaryTask', ps,
                        value = 'EquivalentPlasticStrainIncrement',
                        result = 'NonLocalEquivalentPlasticStrainIncrement',
                        domain = 'beam',
                        characteristicLength = lc)
smoother2 = manta.Model('L2ProjectionAuxiliaryTask', ps,
                        value = 'PlasticVolumeIncrement',
                        result = 'NonLocalPlasticVolumeIncrement',
                        domain = 'beam',
                        characteristicLength = lc)
```

For post-processing purposes, a third instance, named `p_project`,
of this auxiliary task is created to project the value of the equivalent
plastic strain (computed by the mechanical behavior at integration
points) at nodes:

```python
p_project = manta.Model('L2ProjectionAuxiliaryTask', ps,
                        value = 'EquivalentPlasticStrain',
                        result = 'NodalEquivalentPlasticStrain',
                        domain = 'beam')
```

See Section [The L2Projection auxiliary task](../../../../manta_frontend_user_guide/auxiliary_tasks/l2_projection_auxiliary_task.md#l2-projection-auxiliary-taks) for further details.

### [Declaration of the coupling scheme](#id24)

The coupling is defined as follows:

```python
cs1 = manta.CouplingScheme('IterativeCouplingScheme', ps,
                           maximumNumberOfIterations = 500)
cs1.add(mechanics)
cs1.add(smoother1)
cs1.add(smoother2)
cs1.addConvergenceCriterion('StationaryResult',
                            fields = [{'field': 'Porosity', 'fieldType': 'ipField', 'material': 'beam'}],
                            tolerance = 1e-5)

cs =  manta.CouplingScheme('LoopCouplingScheme', ps,
                           numberOfIterations = 1)
cs.add(cs1)
cs.add(p_project)

ps.setCouplingScheme(cs)
```

The main coupling scheme, named `cs2` calls successively an inner
coupling scheme `cs1` and `p_project` one time a each time
step.

The `IterativeCouplingScheme` `cs1` declares a fixed point
algorithm which, at each time step, calls successively the mechanical
model and the auxiliary tasks `smoother1` and `smoother2` up
to convergence. The mechanical model is called knowing the increment of
the non local quantities \(\Delta\,\bar{\omega}\) and
\(\Delta\,\bar{p}\) from the previous iteration of the fixed point
algorithm and the smoothers are called knowing the updated values of the
(local) quantities quantities \(\Delta\,\omega\) and
\(\Delta\,p\) calculated by the mechanical model.

The convergence criterion `StationaryResults` is only satisfied if
the absolute value of correction to the non local equivalent plastic
strain between two iterations of the fixed point algorithm is on each
nodes below a threshold chosen equal to \(10^{-5}\).

[![figure](https://manta-project.gitlab.io/manta/_images/coupling_scheme.svg)](../../../../_images/coupling_scheme.svg)

Fig. 29 Staggered approach used in this tutorial

The coupling scheme `cs2` is represented schematically on
[Fig. 29](#fig-mealor2-tp8-coupling-scheme).

### [Post-processings](#id25)

Next, two built-in post-processings are defined:

- The first one exports the displacement and the porosity
  \(f\) in a `VTK` file. This `VTK`
  file can be opened with `paraview` for instance.
- The second post-processing exports some values into a `txt` file
  which will contain the reaction at the `top` boundary.

```python
ps.addPostProcessing('VTKExport',
                     outputFileBaseName = 'porosity',
                     fields = [{'field': 'Displacement', 'fieldType': 'nodeField', 'material': 'beam'},
                               {'field': 'Porosity', 'fieldType': 'ipField', 'material': 'beam'}])
ps.addPostProcessing('Curves',
                     file = 'force.res',
                     fileFormat = 'txt',
                     curves = [{'Value': {'value': 'ReactionForce[FZ]',
                                          'location': 'top'}}])
```

See Section [Post-processings](../../../../manta_frontend_user_guide/post_processings/post_processings.md#post-processings) for further details.

### [User-defined post-processing task](#id26)

The `Simulation` class allows to define user-defined
post-processing tasks, i.e. call-back functions called at the end of a
time step.

In order to create an handcrafted output file, we first create a
dictionary of curves that will be used inside our post-processing taks:

```python
curves = {'p' : ps.addCurve('NodalValue', field = 'NodalEquivalentPlasticStrain', node = 'p0'),
          'U' : ps.addCurve('NodalValue', field = 'Displacement', node = 'p1'),
          'f' : ps.addCurve('Maximum', field = 'Porosity', fieldType = 'ipField', material = 'beam'),
          'F' : ps.addCurve('Value', value = 'ReactionForce[FZ]', location = 'top')}
```

We then define a variable \(S_{0}\) containing the initial surface
at the bottom of the bar. This surface is used to evaluate the so-called
engineering stress defined by \(F/S_{0}\) where \(F\) is the
force imposed at the top boundary. We also define an empty array named
`results` in which we will accumulate the values calculated by the
curves previously defined at the end of each time step.

```python
S0 = np.pi * Phi_0 ** 2 / 4
results = []
```

We can now define our post-processing task:

```python
def post():
      t = ps.getClock().getTimeAtTheEndOfTheTimeStep()
      U =  getImposedDiplacement(t)
      pv = curves['p'].getValues(ets)[0]
      DeltaPhi = -2* curves['U'].getValues(ets)[0]
      f_max = curves['f'].getValues(ets)[0]
      Force = curves['F'].getValues(ets)[0]
      results.append([t, U / height, f_max, pv, Force / S0, DeltaPhi])
      np.savetxt("results.res",
                 np.asarray(results),
                 delimiter=" ",
                 header="# Time Strain f_max pv Sigma DeltaPhi")
```

### [Initialization of the porosity](#id27)

In order to initialize the porosity, the physical model must be
initialized: this operation, among other things, allocates the memory
associated with the internal state variables.

```python
ps.initialize()

p_bts = ps.getStateManager().getIPField('beam', bts, 'Porosity')
p_ets = ps.getStateManager().getIPField('beam', ets, 'Porosity')
p_bts.setValue(pini)
p_ets.setValue(pini)
```

### [Time discretization and simulation](#id28)

The next lines instantiates a `Simulation` object, declare our
post-processing task and starts the simulation:

```python
s = manta.Simulation(ps, times = [ i / nsteps for i in range(0, nsteps + 1)],
                     allowSubStepping = False)
s.addPostProcessingTask(post)
s.run()
```

See Section [Simulation](../../../../manta_frontend_user_guide/simulation/simulation.md#simulation) for further details.

## [Execution](#id29)

The mesh can be generated by calling `Cast3M`, as follows:

```
$ castem24 mesh.dgibi
```

The mechanical behaviour can compiled by invoking MFront:

```
$ mfront --obuild --interface=generic ImplicitGradientGTN.mfront
```

The simulation is run by executing Python:

```
$ python ImplicitGradientGTN.py
```

## [Results](#id30)

[![figure](https://manta-project.gitlab.io/manta/_images/porosity.png)](../../../../_images/porosity.png)

Fig. 30 Porosity map at the end of the simulation

The porosity map at the end of the simulation is reported on
[Fig. 30](#fig-mealor2-tp8-porosity). The localization of the porosity at
the bottom of the bar is clear. If a local version had been used, this
localization would have been much more severe as the porosity would have
localized in a band of the width of a finite element. The size of the
localization band is, in this non local version, related to the
characteristic length \(l_{c}\).

[![figure](https://manta-project.gitlab.io/manta/_images/traction_curve.svg)](../../../../_images/traction_curve.svg)

Fig. 31 Calculated traction curve

The calculated traction curves are reported on
[Fig. 31](#fig-mealor2-tp8-traction) for two meshes. This figure shows
that those results are mostly mesh independent.

[Fig. 31](#fig-mealor2-tp8-traction) also compares those results with the
results presented in the MEALOR school. This comparison shows a
qualitatively good agreement, but one shall bear in mind that the
MEALOR's tutorials had to be completed with limited time and resources,
and thus relies on a coarse mesh, relaxed convergence criteria, etc. A
rigorous comparison between those simulations would require to use the
same mesh, same convergence criteria (the convergence criteria in
MANTA is somehow more stringent), etc. It would also require to ensure
that no spurious phenomena, such as volumetric locking, degrade the
quality of the solutions. Such a task if far beyond the scope of the
tutorial.

Footnotes

[[1](#id2)]

MEALOR stands for "Mécanique de l'endommagement et approche locale de la rupture".
