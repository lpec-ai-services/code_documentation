<!-- source: https://manta-project.gitlab.io/manta/demos/frontend_examples/non_linear_behaviour/plasticity/rate_dependent_plasticity/swift_voce_cowper_symonds_notched_plate.html -->

# Finite strain simulation of a strain sensitive plastic notched bar in tension

This tutorial describes a tensile test on a notched plate in finite
strain. The material is described by a plastic behavior whose yield
surface depends on the plastic strain rate.

Note

The following files are required to run the tutorial:

- [`mesh3D.dgibi`](../../../../../_downloads/8605a51b0c356a84563a6e1b3cb259e6/mesh3D.dgibi):
  the Cast3M input file required to generate the mesh.
- [`SwiftVoce-CowperSymonds.mfront`](../../../../../_downloads/fb12841be6b94971fccd092836eead81/SwiftVoce-CowperSymonds.mfront): the MFront implementation of the mechanical behaviour
- [`test3D.py`](../../../../../_downloads/bf28f9cea2798c1eb3a12011ca1e1d16/test3D.py): the main script

Note

This test case reproduces a simulation made with `Abaqus`
by Thibault Barret during his PhD at IRDL
(Institut de Recherche Dupuy de Lôme).
His results are used to verify MANTA's one.

## [Description](#id8)

### [Geometry](#id9)

[![figure](https://manta-project.gitlab.io/manta/_images/mesh1.svg)](../../../../../_images/mesh1.svg)

Fig. 17 Geometry considered.

The test case considered is a single-edge notched plate depicted in
[Fig. 17](#fig-examples-swift-voce-cowper-symonds-notched-plate-mesh). In
the mesh file, the plate is named `vtot` and the boundaries
`bottom`, `left`, `rear` and `front`.

Table 16 Geometric parameters used in this test

|  |  |
| --- | --- |
| Width \(w\) | \(5\,\cdot\,10^{-3}\) m |
| Length \(L\) | \(15\,\cdot\,10^{-3}\) m |
| Radius \(R\) | \(2.5\,\cdot\,10^{-3}\) m |
| Thickness \(e\) | \(0.4\) mm |

The main geometric parameters defining the plate are reported in
[Table 16](#single-notched-plate-geometric-parameters).

### [Boundary conditions](#id10)

First, on Boundary `front`, the component \(U_{y}\) of the
displacement is prescribed, such that:

\[U_y(t) = v\,t\]

where \(v = 5.10^{-3} \; m.s^{-1}\) is the displacement rate and
\(t\) the current time.

The following components of the displacement are then imposed null:

- \(U_{x}\) on Boundary `left`,
- \(U_{z}\) on Boundary `bottom`,
- \(U_{y}\) on Boundary `rear`,

### [Mechanical behavior](#id11)

We consider an homogeneous and isotropic material which is described by
a plastic law whose yield surface depends on the equivalent
plastic strain rate.

#### [Finite strain kinematics](#id12)

Finite strain are handled by MFront using the logarithmic framework
(see [[MAL02](../../../../../references/references.md#id12)] for details).

The logarithmic strain is defined as

\[\underline{\varepsilon}_{log} = \log(\underline{\mathbf{U}}) = \frac{1}{2} \log(\underline{\mathbf{C}})\]

where \(\underline{\mathbf{U}}\) is the lagrangian stretch tensor
and \(\underline{\mathbf{C}}\) is the right Cauchy tensor.
\(\underline{\varepsilon}_{log}\) is also known as Hencky strain.

The dual stress of the logarithmic strain is denoted
\(\underline{\mathbf{T}}\) in the following.

Note

The logarithmic strain framework is handled by MFront.
From MANTA's point of view, the mechanical behavior
is a black box taking the deformation gradient on input
and returning the first Piola-Kirchhoff stress and
the appropriate consistent tangent operator.

An additive split of the strain \(\underline{\varepsilon}^{to}\)
into an elastic part \(\underline{\varepsilon}^{el}\) and a plastic
part \(\underline{\varepsilon}^{p}\) is assumed:

\[\underline{\varepsilon}^{to}= \underline{\varepsilon}^{el} + \underline{\varepsilon}^{p}\]

#### [Elastic behavior](#id13)

The stress is computed following Hooke's law, as follows:

\[\underline{T}=\lambda \, \text{tr}(\underline{\varepsilon}^{el}) + 2 \mu \underline{\varepsilon}^{el}\]

where \(\lambda\) and \(\mu\) are respectively the first and
second Lamé's coefficients and \(\text{tr}(\underline{\bullet})\)
denotes the trace of the \(\underline{\bullet}\) tensor.

#### [Plastic flow](#id14)

The *plastic* inelastic flow part, is driven by the following yield
surface:

\[f\left(T_{eq}, p, \dot{p}\right) = T_{eq} - R\left(p, \dot{p}\right)\]

- \(T_{eq}\) is the von Mises norm of the dual stress,
- \(p\) is the equivalent plastic strain,
- \(R\) is the the radius of the yield surface.

The plastic strain rate is given by assuming the normality of the flow
rule:

\[\underline{\dot{\varepsilon}}_{p} = \dot{p}\,\frac{\partial f}{\partial \underline{T}} = \dot{p}\,\underline{n}\]

where:

- the equivalent plastic strain rate \(\dot{p}\) has already been
  identified as a plastic multiplier,
- \(\underline{n}\) is the von Mises normal.

The evolution of the plastic multiplier is given by the classical
Karush-Kuhn-Tucker conditions:

\[\begin{split}f\left(T_{eq}, p, \dot{p}\right)\, \dot{p} = 0 \quad\text{with}\quad
\left\{
\begin{aligned}
\dot{p} &= 0 &\text{if}\quad f\left(T_{eq}, p, \dot{p}\right)<0\\
\dot{p} &\geq 0 &\text{if}\quad f\left(T_{eq}, p, \dot{p}\right)=0
\end{aligned}
\right.\end{split}\]

#### [Strain sensitive isotropic hardening rule](#id15)

In this tutorial, the radius of the yield surface is assumed to have the
following form:

\[R(p,\dot{p}) = R_0(p)\,R_{rs}(\dot{p})\]

where

- \(R_0(p)\) is the yield radius corresponding to an infinitely
  slow loading.
- \(R_{rs}(\dot{p})\) is the correction describing the strain rate
  sensitivity. \(R_{rs}(0)\) must be equal to 1. In this tutorial,
  the Cowper-Symonds law is used.

##### Voce and Swift law

The yield radius \(R_0(p)\) is defined as:

\[R_0(p) = p_{\alpha}\,R_{s}\left(p\right)+\left(1-p_{\alpha}\right)\,R_{v}\left(p\right)\]

where \(p_{\alpha}\) is a weight coefficient allowing to switch between
a Swift law \(R_{s}\left(p\right)\) and a Voce law
\(R_{v}\left(p\right)\).

The Swift part is defined by:

\[R_{s}(p) = R_0 \Big(\frac{p + p_0}{p_0} \Big)^{n_{s}}\]

The Voce part is defined by:

\[R_v(p) = Q_{1}+Q_{2}\,\left(1-\exp\left(-b\,p\right)\right)\]

##### Cowper Symonds law

The Cowper-Symonds law takes the following form:

\[R_{rs} (\dot{p}) = 1 + A \Big( \frac{\dot{p}}{\dot{p_0}} \Big)^{1/e}\]

where \(A\) and \(e\) are material properties.

#### [Material properties](#id16)

The MFront behavior requires a set of material properties (see the
`@MaterialProperty` keyword in the implementation) to compute the
evolution of the material.

Note

The name of the properties are defined in the MFront file.

There are two ways to retrieve this information:

```
mfront-query --material-properties SwiftVoce-CowperSymonds.mfront
```

Another way is to retrieve the information in `python`
from MANTA's `SolidMaterial` brick using the
`manta.info` function.

Table 17 List of material properties

| MFront name | Symbol | Value | Unit |
| --- | --- | --- | --- |
| YoungModulus | \(E\) | \(210\,\cdot\,10^{9}\) | \(Pa\) |
| PoissonRatio | \(\nu\) | \(0.3\) | **-** |
| pAlpha | \(p_{\alpha}\) | \(0.62\) | **-** |
| coefK | \(R_0\) | \(1115.15\,\cdot\,10^{6}\) | \(Pa\) |
| epsi0 | \(p_0\) | \(0.0013\) | \(Pa\) |
| expN | \(n_s\) | \(0.31\) | **-** |
| Q1 | \(Q1\) | \(1050.30\,\cdot\,10^{6}\) | \(Pa\) |
| Q2 | \(Q2\) | \(0.445\) | **-** |
| Q3 | \(b\) | \(13.06\) | \(Pa^{-1}\) |
| coefD | \(A\) | \(9013\) | \(Pa\) |
| expE | \(e\) | \(3.19\) | **-** |

The first ones \(E\) and \(\nu\) are the Young's Modulus and the
Poisson's ratio of the material which are used internally by the
mechanical behavior to calculate the Lamé's coefficients.

\(p_{\alpha}\) is a ponderation
parameter (to sum Voce and Swift law) while \(R_0\), \(p_0\) and
\(n_s\) are parameters from Swift law. \(Q1\), \(Q2\) and
\(Q3\) are parameters from Voce law. Finaly, \(D\) and \(e\)
are parameters from Cowper-Symonds law.

## [Implementation](#id17)

After having imported the `manta` module, the first declaration is:

```
manta.setDefaultVerbosityLevel(manta.VerbosityLevel.verboseLevel3)
```

It is used to manage the verbosity of MANTA's output. When set to
`verboseLevel3`, it allows the code to print information about internal
operations of each model, *e.g*, the internal iterations of each model.

### [Definition of the physical system](#id18)

The mesh has been generated using Cast3M and saved with the name
`mesh3D.med`.

The creation of the physical system is then defined as follows:

```python
ps = manta.PhysicalSystem(mesh = {'file': 'mesh3D.med',
                                  'domains': ['vtot'],
                                  'boundaries': ['bottom', 'left', 'rear', 'front']})
```

This statement needs some information like the name of the notched plate
(here `vtot`) and the name of the boundaries.

### [Definition of the material properties](#id19)

The material properties needed by the behavior are declared using the
`addProperty` method of the `PhysicalSystem`:

```python
mm.add('SolidMaterial',
       material = 'vtot',
       library = './src/libBehaviour.so',
       behavior = 'SwiftVoceCowperSymonds')

for n, v in {'YoungModulus': 210e9,
             'PoissonRatio': 0.3,
             'pAlpha': 0.62,
             'coefK': 1115.15e6,
             'epsi0': 0.0013,
             'expN': 0.31,
             'Q1': 1050.30e6,
             'Q2': 0.445,
             'Q3': 13.06,
             'coefD': 9013,
```

In the above lines of code, a Python dictionary, associating each
property with its value, is used for convenience.

### [Definition of the mechanical model, boundary conditions and behavior law](#id20)

#### [Model declaration](#id21)

An implicit mechanical model is declared by calling the `Model`
abstract factory with the name `ImplicitMechanics`.

Since the behaviour is nonlinear, we have to use a nonlinear solver. We
select the standard Newton-Raphson algorithm and specify a relative
convergence tolerance of \(10^{-4}\).

```python
# tag::ksp_options_pymanta_raw_escape[]
linear_solver_options = {'fgmres': {'preconditioner': 'ilu'}}
```

#### [Declaration of boundary conditions](#id22)

The boundary conditions are created as follows:

- for the boundaries with blocked displacement boundary conditions

  ```python

  mm = manta.Model('ImplicitMechanics', ps,
                   nonlinearSolver = {'Newton': {'convergenceTolerances': {'relativeConvergenceTolerance': 1e-4},
                                                 'linearSolver': linear_solver_options}})
  ```
- for the boundary where the displacement is imposed:

  ```python
      mm.add('ImposedDisplacement',
             boundary = b,
             component = c,
             strategy = 'elimination')
      
  mm.add('ImposedDisplacement',
  ```

  with the function `ImposedDisplacementValue` declared as a loading
  evolution:

  ```python
  ps.addLoading('ConstantUniformScalar',
                material = 'vtot',
  ```

#### [Declaration of the mechanical behavior](#id23)

This following snippet adds the `SolidMaterial` brick that assigns
to the `vtot` material the behavior `SwiftVoceCowperSymonds`
found in the `./src/libBehaviour.so` shared library:

```python
       component = 'UY',
       reaction = 'ReactionForce',
       value = 'ImposedDisplacementValue',
       strategy = 'elimination')
```

This shared library must be generated by MFront before running the
simulation.

### [Declaration of the coupling scheme](#id24)

The declaration of a coupling scheme is required even if only one
mechanical model is used. In this tutorial, we use the `setModel`
method which declares a trivial coupling scheme that calls the
mechanical model once at each time step:

```python
              value = 293.15)
```

### [Declaration of the post-processings](#id25)

We define two post-processings:

- the first one exports in `VTK` format the `Displacement`
  and the `EquivalentPlasticStrain` fields of the material
  `vtot`:

  ```python
  ps.addLoadingEvolution('ImposedDisplacementValue', lambda t: displacement_rate * t)

  # creating the coupling scheme
  ps.setModel(mm)

  ps.addPostProcessing('VTKExport',
                       outputFileBaseName = 'results',
                       fields = [
                           {'field': 'Displacement',
  ```

  This snippet specified that the `Displacement` is calculated at nodes
  (`nodeField`) and the `EquivalentPlasticStrain` at the
  integration points (`ipField`).
- the second one writes the value of the reaction associated with the
  imposed displacement in a file:

  ```python
                          'fieldType': 'nodeField',
                            'material': 'vtot'},
                           {'field': 'EquivalentPlasticStrain',
                            'fieldType': 'ipField',
  ```

### [Running the simulation](#id26)

```python
ps.addPostProcessing('Curves',
                     file = 'force.res',
                     fileFormat = 'txt',
                     curves = [{'Value': {'value': 'ReactionForce[FY]', 'location': 'front'}}])
#
```

This piece of code allows to start the simulation. Between each time
\(t^n\) and \(t^{n+1}\), the code resolves the model, searching for mechanical equilibrium.
If no convergence is reached, the time step will be decreased. Output
in *VTK* formats will also be written at each of the specified time
steps.

Finally, the last command, `s.run` starts the simulation.

## [Execution](#id27)

The mesh is generated using Cast3M with the command

```
$ castem24 mesh3D.dgibi
```

The MFront file is built with:

```
$ mfront --obuild --interface=generic SwiftVoce-CowperSymonds.mfront
```

Then, the simulation is run by executing python

```
$ python test3D.py
```

or with mpi

```
$ mpirun -n [nproc] python test3D.py
```

## [Simulation results](#id28)

The simulation leads to the following result (see
[Fig. 18](#single-notched-plate-result-figure-simulation-equivalent-plastic-strain))
where we can see the equivalent plastic strain at the end of the
simulation. As expected, the plastic strain is localized in the notched
corner opposed to the boundary with an imposed displacement rate.

![figure](https://manta-project.gitlab.io/manta/_images/result_internalstate.png)

Fig. 18 Simulation result at the final time step for the
`SwiftVoceCowperSymonds` law of equivalent plastic strain.

The force as a function of displacement is shown in
[Fig. 19](#single-notched-plate-result-figure-force-displacement). This
figure shows that MANTA gives a result similar to Abaqus's one.

Note

To match Abaqus's result, quadratic elements have to be used.

From a physical point of view, a classical evolution is observed:

- from Time 0 to approximatively Time 0.2, the force evolves linearly, which
  corresponds to an elastic regime,
- after Time 0.2, the force evolves non-linearly due to plasticity.

![figure](https://manta-project.gitlab.io/manta/_images/force_manta_abaqus_comparison.svg)

Fig. 19 Evolution of the applied force as a function of displacement for MANTA and Abaqus

One can investigate the influence of the imposed displacement rate on
the overall mechanical response of the plate by comparing the previous
result with a second simulation where this rate is amplified by a
factor \(2\).

![figure](https://manta-project.gitlab.io/manta/_images/force_displacement_rate_comparison.svg)

Fig. 20 Evolution of the applied force as a function of displacement for two different displacement rates

This comparison is reported in Figure
[Fig. 20](#single-notched-plate-result-figure-force-displacement-speed):
for the material properties used in this example, the effect of
displacement rate is visible but limited.
