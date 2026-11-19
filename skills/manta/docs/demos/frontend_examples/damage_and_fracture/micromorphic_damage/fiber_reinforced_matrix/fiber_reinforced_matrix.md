<!-- source: https://manta-project.gitlab.io/manta/demos/frontend_examples/damage_and_fracture/micromorphic_damage/fiber_reinforced_matrix/fiber_reinforced_matrix.html -->

# Description of damage evolution in fiber reinforced matrix

This tutorial shows how to reproduce a classical test case in the field
of phase-field approach to fracture popularized by the seminal work of
Bourdin, see [[BFM00](../../../../../references/references.md#id17)].

In this tutorial a micromorphic approach, see
[[For09](../../../../../references/references.md#id25)], is used to approximate the classical
phase-field model AT2, following the work of Siedel
[[FHS+22](../../../../../references/references.md#id26)], [[Sie23](../../../../../references/references.md#id24)] .

Note

The following files are required to run the tutorial:

- [`mesh.dgibi`](https://manta-project.gitlab.io/manta/_downloads/f5d918303141555fbeeffc523103aac9/mesh.dgibi):
  the Cast3M input file required to generated the mesh.
- [`MicromorphicDamageI_SpectralSplit.mfront`](https://manta-project.gitlab.io/manta/_downloads/4f01c77408e60c95e830e37a776f8106/MicromorphicDamageI_SpectralSplit.mfront): the MFront implementation of the mechanical behaviour
- [`MicromorphicDamageII.mfront`](https://manta-project.gitlab.io/manta/_downloads/232fb8628a6fc35352ca6b917a6fb436/MicromorphicDamageII.mfront): the MFront implementation of the micromorphic behaviour
- [`fiber_reinforced_matrix.py`](https://manta-project.gitlab.io/manta/_downloads/5c7447af4d0e986012cb6f8ea59bd40b/fiber_reinforced_matrix.py): the main script

The problem is that of a stiff circular inclusion embedded in a square
plate under imposed vertical displacement on its upper boundary.

The coupled problem between mechanics and damage is solved using
a staggered approach. The micromorphic approach being based on strong
variational bases, this staggered approach reduces the value of a global
energy, called the Lagrangian. This property explains why this staggered
approach is also called alternate minimization in the literature, see
[[BFM00](../../../../../references/references.md#id17)].

Note

This tutorial is adapted from a demo of the `mgis.fenics` module
([[BH20](../../../../../references/references.md#id16)]) which couples the open-source finite
element library `FEniCS` and the MGIS library,
[[HBF+20](../../../../../references/references.md#id15)]:

## Problem considered

### Geometry and mesh

We consider a 2D square domain \(\Omega\) of size \([1, 1]\)
composed of a circular fiber of radius \(0.2\) located at the center
of the square and a matrix which occupies the rest of the square. In
this tutorial, the fiber is considered extremely stiff, so it will only
be accounted through boundary conditions.

![figure](https://manta-project.gitlab.io/manta/_images/mesh.png)

Fig. 21 Mesh used to discretize the matrix.

The mesh used for the matrix is illustrated on Figure [Mesh used to discretize the matrix.](#matrix-mesh).

### Material behaviour

The micromorphic approach to fracture is a class of damage gradient
models where three unknowns are considered:

- the displacement \(\vec{u}\),
- the damage \(d\),
- the micromorphic damage \(d_{\chi}\).

The evolution of \(\vec{u}\), \(d\), \(d_{\chi}\) in the matrix is described by
the minimization of the following Lagrangian, denoted \(\mathcal{L}\):

\[\begin{aligned}
\left(\vec{u}, d, d_{\chi}\right) &=
\underset{\left(\vec{u}^{\star}, d^{\star}, d_{\chi}^{\star}\right)}{\mathrm{argmin}}\quad
\mathcal{L}^{e}\left(\vec{u}^{\star}, d^{\star}\right) + \mathcal{L}^{c}\left(d^{\star}, d_{\chi}^{\star}, \vec{\nabla}\, d_{\chi}^{\star}\right)
\end{aligned}\]

where:

- \(\mathcal{L}^{e}\) describes the energy stored elastically,
- \(\mathcal{L}^{c}\) describes the energy associated with the
  evolution of the damage and micromorphic damage,

\(\mathcal{L}^{e}\) is the integral of the elastic part of the free
energy denoted \(\Psi^{e}\). In this tutorial, the matrix is assumed
isotropic and the spectral-split decomposition is used to take into
account unilateral effects:

\[\begin{split}\begin{aligned}
\mathcal{L}^{e}\left(\vec{u}, d\right) &= \int_{\Omega} \Psi^{e}\left(\tepsilonto, d\right)\,\mathrm{d} V \\
\Psi^{e}\left(\vec{u}, d\right) &= g\paren{d}
\left(
\frac{\lambda}{2}\left<\mathrm{tr}\left(\tepsilonto\right)\right>_{+}^{2}
+\mu\,\left<\tepsilonto\right>_{+}\,\colon\,\left<\tepsilonto\right>_{+}
\right)
+\frac{\lambda}{2}\left<\mathrm{tr}\left(\tepsilonto\right)\right>_{-}^{2}
+\mu\,\left<\tepsilonto\right>_{-}\,\colon\,\left<\tepsilonto\right>_{-}
\end{aligned}\end{split}\]

where:

- \(\tepsilonto\) is the total linearised strain (small strain
  hypothesis are considered in this tutorial),
- \(\lambda\) is the first Lamé's coefficient,
- \(\mu\) is the shear modulus,
- \(<x>_{+}\) denotes the positive part of a scalar or the positive
  part of a tensor,
- \(g\left(d\right)\) is a degradation function.

To approximate the classical phase-field models, \(\mathcal{L}^{c}\) is chosen as follows:

\[\begin{split}\mathcal{L}^{c}\left(d, d_{\chi}, \vec{\nabla}\, d_{\chi}\right) =
\int_{\Omega} \frac{G_{c}}{c_w}
\left(
\frac{w\left(d\right)}{l_{0}}+
l_{0}\,\vec{\nabla}\, d_{\chi}\,\cdot\,\vec{\nabla}\, d_{\chi}+
\beta\,\paren{d-d_{\chi}}^{2}
\right)
+\phi\left(d-d_{t}\right)
\,\mathrm{d} V \\\end{split}\]

- \(G_{c}\) is the fracture energy,
- \(l_{0}\) is a characteristic length,
- \(c_{w}\) is a constant which depends on the selected model,
- \(\beta\) is a penalization parameter which enforces that \(d\)
  and \(d_{\chi}\) are close.
- \(\phi\) ensures the irreversibility constraint: \(d\geq
  d_{t}\) where \(d_{t}\) is the value of the damage at the beginning
  of the time step.

In this tutorial, we chose to approximate the AT2 model, which
corresponds to the following choices:

- \(g\left(d\right)=1-d^{2}\),
- \(w\left(d\right)=d^{2}\)
- \(c_w=2\).

The penalization factor is chosen equal to \(150\). The degradation
factor is also modified by a small parameter \(k\), a residual stiffness, to avoid numerical issues
if the material is fully damaged, *i,e* \(g(d) = (1-d)^2 + k\)

[[FHS+22](../../../../../references/references.md#id26)] shows that:

- minimizing Lagrangian \(\mathcal{L}\) with respect to the
  displacement field at constant damage and micromorphic damage leads to
  a standard mechanical problem.
- minimizing Lagrangian \(\mathcal{L}\) with respect to the
  micromorphic damage at constant displacement field leads to a
  nonlinear Helmoltz equation where the damage can be considered as an
  internal state variable.

In both cases, the physics can be described by a behaviour that can be
implemented using MFront.

### Material properties

Table 18 Material properties of the matrix

| Name | Value |
| --- | --- |
| `YoungModulus` | \(200\) (arbitrary unit, a. u.) |
| `PoissonRatio` | \(0.2\) |
| `RelativeResidualStiffness` | \(10^{-4}\) |
| `FractureEnergy` | \(1\) (a. u.) |
| `CharacteristicLength` | \(2\,\cdot\,10^{-2}\) (a. u.) |

The material properties used in this test are reported on Table
[Material properties of the matrix](#id9).

### Modeling hypothesis

Plane strain is assumed.

### Boundary conditions

The upper surface is blocked in the horizontal direction and a uniform
displacement is applied in the vertical direction. On the boundary with
the fiber, all the displacements are assumed null.

The micromorphic damage is assumed null on the boundary of the fiber,
mostly to prevent the propagation of the damage at this interface: the
damage is forced to develop in the matrix.

## Description of the MANTA input file

The test cases begins by importing the `numpy` and `manta`
module:

```python
import numpy as np
import manta
```

`numpy` will be used to interpolate the values of the imposed
displacement.

Next, we define the parameters of the study:

- the material properties Young's modulus, Poisson's ratio, fracture
  energy \(G_{c}\),
- the characteristic length \(l_{0}\),
- the penalisation factor \(\beta\),

```python
properties = {'YoungModulus' : 200,
              'PoissonRatio' : 0.2,
              'RelativeResidualStiffness':  1e-4,
              'FractureEnergy' : 1,
              'CharacteristicLength' : 0.02,
              'PenalisationFactor' : 150}
```

The Young's modulus and the Poisson's ratio are used by the mechanical
MFront behaviour to compute the first Lamé's coefficient and the shear
modulus.

We then define the value of the convergence criterion
used by the mechanical model and the micromorphic damage model:

```python
reps= 1e-6
```

Note that \(10^{-6}\) is generally considered as a stringent value.

The directory containing this example provides other implementations
(without spectral split or assuming plane stress). To simply switch
between those implementations, the name of the MFront behaviour is
declared as a variable:

```python
mechanical_behavior = 'MicromorphicDamageI_SpectralSplit'
# mechanical_behavior = 'MicromorphicDamageI'
# mechanical_behavior = 'MicromorphicDamageI_SpectralSplit_PlaneStress'
```

### Definition of the physical system

The next step is to define a physical system. The `Cast3M` script
generates a `MED` file that is imported as follows:

```python
ps = manta.PhysicalSystem(mesh = {'file': 'mesh.med',
                                  'domains': ['matrix'],
                                  'boundaries': ['upper_boundary',
                                                 'inner_boundary']},
                          geometricHypothesis = 'inPlane')
```

The geometric hypothesis is used to specify that the problem considered
is not axisymmetrical.

See Section [Physical system](../../../../../manta_frontend_user_guide/physical_system/physical_system.md#physical-system) for further details.

### Declaration of the material properties

Once the physical system is defined, we can immediately define the
material properties:

```python
for n, v in properties.items():
    ps.addProperty('Constant', material = 'matrix', name = n, value = v)
```

See Section [Properties](../../../../../manta_frontend_user_guide/properties.md#properties) for further details.

### Mechanical model, behaviour and boundary conditions

The mechanical model is instanciated as follows:

```python
mechanics = manta.Model('ImplicitMechanics', ps,
                        nonlinearSolver = {'Newton': {'switchFromRelativeToAbsoluteCriterion': True,
                                                      'thresholdOnTheFirstResidualNorm': 1e-100,
                                                      'convergenceTolerances': {'relativeConvergenceTolerance': reps}}})
```

The `Newton` solver is selected. As the alternate minimization
algorithm may call the mechanical problem numerous times during the same
time step, special care shall be taken when selecting the convergence
criterion. The `switchFromRelativeToAbsoluteCriterion` parameter
forces the `Newton` solver to use a relative criterion with a
tolerance \(\epsilon_{r}\) for the first resolution in a given time
step and keeps the initial residual norm \(R_{0}\) in memory to
switch to an absolute criterion for the new resolutions on the same time
step, the absolute tolerance then used is \(R_{0}\,\epsilon_{r}\).

The brick describing the mechanical behaviour of the matrix is then
defined by calling an external MFront behaviour that shall be compiled
before running the simulation:

```python
mechanics.add('SolidMaterial',
              material = 'matrix',
              library = 'src/libBehaviour.so',
              behavior = mechanical_behavior,
              hypothesis = 'PlaneStrain')
```

Bricks associated with boundary conditions are then added to the model,
as follows:

```python
mechanics.add('ImposedDisplacement', boundary = 'inner_boundary', components = ['UX', 'UY'])
mechanics.add('ImposedDisplacement', boundary = 'upper_boundary', component = 'UX')
mechanics.add('ImposedDisplacement', boundary = 'upper_boundary', component = 'UY',
              reaction = 'ReactionForce',
              value = 'ImposedDisplacementValue')
```

### Micromorphic model, behaviour and boundary conditions

The micromorphic model is defined:

```python
damage = manta.Model('ImplicitMicromorphicDamage', ps,
                     nonlinearSolver = {'Newton': {'switchFromRelativeToAbsoluteCriterion': True,
                                                   'thresholdOnTheFirstResidualNorm': 1e-100,
                                                   'convergenceTolerances': {'relativeConvergenceTolerance': reps},
                                                   'maximumNumberOfIterations': 500}})
```

The next line adds a brick describing the micromorphic behaviour:

```python
damage.add('SolidMaterial',
           material = 'matrix',
           library = 'src/libBehaviour.so',
           behavior = 'MicromorphicDamageII',
           hypothesis = 'PlaneStrain')
```

To avoid localization of damage at the interface between the fiber and
the matrix, the micromorphic damage is imposed null at the associated
boundary:

```python
damage.add('DirichletBoundaryCondition',
           boundary = 'inner_boundary',
           unknown = 'MicromorphicDamage',
           value = 0)
```

### Declaration of the coupling scheme

The coupling is defined as follows:

```python
cs = manta.CouplingScheme('IterativeCouplingScheme', ps,
                          maximumNumberOfIterations = 1000)
cs.add(mechanics)
cs.add(damage)
cs.addConvergenceCriterion('FirstIteration')

ps.setCouplingScheme(cs)
```

The `IterativeCouplingScheme` declares a fixed point algorithm
which, at each time step, calls the mechanical model and the
micromorphic model alternatively up to convergence. The mechanical model
is called knowing the damage value from the previous iteration of the
fixed point algorithm and the damage model is called knowing the updated
values computed by the mechanical model.

The convergence criterion `FirstIteration` checks that each models
must converge at the first iteration, i.e. the residuals of each models
satisfies their respective convergence criteria without making any
iteration. In other words, an update of the damage does not perturb the
mechanical equilibrium and an update of the mechanical variable does not
perturb the micromorphic solution.

### Definition of the evolution of the imposed displacement at the upper boundary of the matrix

The following line declares a loading evolution, i.e. a function of time:

```python
def getImposedDisplacementValue(t: float):
    tvalues = [0, 1, 2]
    dvalues = [0, 70e-3, 125e-3]
    return np.interp(t, tvalues, dvalues)

ps.addLoadingEvolution('ImposedDisplacementValue', getImposedDisplacementValue)
```

A loading evolution is not associated to a material or a boundary, it
is used to fulfill the requirement of the brick defining the imposed
displacement on the upper boundary of the matrix.

Here, we use `numpy`'s `interp` function to make a piecewise
linear interpolation of discrete values. The value of the imposed
displacement at time \(1\) correspond to an almost undamaged
material allowing a coarse time discretization. Between times \(1\)
and \(2\), a finer time discretization is used.

See Section [Loadings](../../../../../manta_frontend_user_guide/loadings.md#loadings) for further details.

### Post-processings

Two post-processings are defined in this example:

- The first one exports the damage field \(d\) and the micromorphic
  damage field \(d_{\chi}\) in a `VTK` file. This `VTK`
  file can be opened with `paraview` for instance.
- The second post-processing exports some values into a `txt` file
  which will contains the reaction at the upper boundary and some
  integral values of the stored and dissipated energies.

```python
ps.addPostProcessing('VTKExport',
                     outputFileBaseName = 'damage',
                     fields = [{'field': 'MicromorphicDamage', 'fieldType': 'nodeField', 'material': 'matrix'},
                               {'field': 'Damage', 'fieldType': 'ipField', 'material': 'matrix'}])

ps.addPostProcessing('Curves',
                     file = 'force.res',
                     fileFormat = 'txt',
                     curves = [{'Value': {'value': 'ReactionForce[FY]',
                                          'location': 'upper_boundary'}},
                               {'Integral': {'field': 'StoredPositiveElasticEnergy',
                                             'fieldType': 'ipField',
                                             'material': 'matrix'}},
                               {'Integral': {'field': 'DissipatedEnergy',
                                             'fieldType': 'ipField',
                                             'material': 'matrix'}},
                               {'Integral': {'field': 'DamageDissipatedEnergy',
                                             'fieldType': 'ipField',
                                             'material': 'matrix'}},
                               {'Integral': {'field': 'PenalisationEnergy',
                                             'fieldType': 'ipField',
                                             'material': 'matrix'}},
                               {'Integral': {'field': 'MicromorphicDamageGradientEnergy',
                                             'fieldType': 'ipField',
                                             'material': 'matrix'}}])
```

See Section [Post-processings](../../../../../manta_frontend_user_guide/post_processings/post_processings.md#post-processings) for further details.

### Time discretization

To reduce the computational time, a coarse time discretization is used
between times \(0\) and \(1\), and a finer one between \(1\)
and \(2\):

- \(5\) temporal sequences are defined between \(0\) and \(1\),
- \(25\) temporal sequences are defined between \(0\) and \(2\).

```python
nsteps1 = 5
nsteps2 = 25
dt1 = float(1) / nsteps1
dt2 = float(1) / nsteps2
times = [i * dt1 for i in range(0, nsteps1 + 1)] + [1 + i * dt2 for i in range(0, nsteps2 + 1)][1:]
```

See Section [Simulation](../../../../../manta_frontend_user_guide/simulation/simulation.md#simulation) for further details.

### Running the simulation

The next lines instantiates a `Simulation` object and starts the
simulation:

```python
s = manta.Simulation(ps, times = times)
s.run()
```

See Section [Simulation](../../../../../manta_frontend_user_guide/simulation/simulation.md#simulation) for further details.

## Results

The post-processings defined above allow to visualize the damage map at each
time steps and plot the imposed force or the stored and dissipated
energies as a function of time.

### Damage evolution

![figure](https://manta-project.gitlab.io/manta/_images/damage.png)

Fig. 22 Damage map at the end of the simulation.

[Fig. 22](#damage-map) shows the damage map obtained at the end of the
simulation. Visualizing the evolution of the damage map shows that a
first unstable propagation occurs, followed by a stable propagation. Then,
as already reported by Bourdin et al. (see
[[BFM00](../../../../../references/references.md#id17)]), the vertical symmetry of the solution
is broken with, in our simulation, an unstable propagation toward the
left boundary followed by an unstable propagation toward the right
boundary.

### Imposed force

![figure](https://manta-project.gitlab.io/manta/_images/force.png)

Fig. 23 Evolution of the imposed force on the upper boundary, as
computed by MANTA and `mgis.fenics`.

The evolution of the reaction force reported on [Fig. 23](#force)
confirms the analysis made in the previous paragraph and the impact of
the various unstable propagations can readily be observed. The force
computed by MANTA is compared to the one computed by
`mgis.fenics`. A relatively good agreement between those solutions
can be observed and the differences can be explained by the fact that:

- a coarser mesh is used in `mgis.fenics`,
- a looser criterion is used in `mgis.fenics` to stop the
  alternate minimization algorithm.

### Stored and dissipated energies

![figure](https://manta-project.gitlab.io/manta/_images/energies.png)

Fig. 24 Evolution of the integral of the positive part of the free energy, as
computed by MANTA and `mgis.fenics`. Evolution of the
total dissipated energy, as computed by MANTA.

Finally, [Fig. 24](#energies) compares stored and dissipated energies.
Again a good agreement between MANTA and `mgis.fenics` can be
observed.
