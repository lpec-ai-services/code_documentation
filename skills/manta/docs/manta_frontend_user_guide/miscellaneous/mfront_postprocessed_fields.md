<!-- source: https://manta-project.gitlab.io/manta/manta_frontend_user_guide/miscellaneous/mfront_postprocessed_fields.html -->

# Compute custom postprocessed fields

Note

Objectives
These snippets show how to obtain postprocessed fields (like strain and
stress measures) using additional [MFront](https://thelfer.github.io/tfel/web/) files.

Note

For the sake of simplicity, this tutorial applies this technique to trivial
calculations. However, point-wise model in [MFront](https://thelfer.github.io/tfel/web/) allows using all the
features available in the TFEL/[Math](https://thelfer.github.io/tfel/web/tensors.html), [Material](https://thelfer.github.io/tfel/web/tfel-material.html) and [Material-Homogenization](https://thelfer.github.io/tfel/web/tfel-material-homogenization.html)
libraries. See also the [FailureCriteria](https://thelfer.github.io/FailureCriteria/web/index.html) project which provides common ready to use brittle and
ductile failure criteria for uncoupled analyses where damage indicator are
calculated as a post-processing of a mechanical analysis.

## Example: torsion of a slender nonlinear elastic solid

Let us consider a slender cuboid of square cross-section,with its longitudinal
axis aligned with the \(z\)-direction. The cuboid is clamped at its base
face (\(\Gamma_b\)) and subjected to a prescribed rigid rotation
\(\theta(t)\) of its top face by an angle (\(\Gamma_t\)) around the
\(z\)-axis. The cuboid is made of an isotropic elastic material described by
the Saint Venant-Kirchhoff (SVK) model, for which the strain-energy density is
given by:

(17)\[\psi(\mathbf{E}) =
\mu \, \mathbf{E} : \mathbf{E}
+ \frac{\lambda}{2} \operatorname{tr}\mathbf{E}\]

where \((\mu, \lambda)\) denote the Lamé parameters, and \(\mathbf{E}\)
denotes the Green-Lagrange (GL) strain tensor. The second Piola-Kirchhoff (PK2)
stress tensor \(\mathbf{S}\) can be derived from the relation:

(18)\[\mathbf{S} =
\frac{\partial \psi}{\partial \mathbf{E}}\]

The state of equilibrium on the reference configuration denoted \(\Omega_0\)
reads.

Find \(\mathbf{u} \in \mathcal{V}\) such that:

(19)\[\int_\Omega \mathbf{S}(\mathbf{u}) : \mathbf{E}(\mathbf{v}) \, d\mathbf{X} = 0
\quad \forall \mathbf{v} \in V_0\]

where \(\mathcal{V}\) denotes the space of kinematically admissible
displacement fields satisfying the prescribed Dirichlet boundary conditions.

\[\begin{split}\mathcal{V} = \left\{
\mathbf{u} \in \mathcal{H}^1 \;\middle|\;
\begin{aligned}
\mathbf{u}(\mathbf{x}) &= \mathbf{0}
&& \text{on} \, \Gamma_b, \\
\mathbf{u}(\mathbf{x}) &= \mathbf{u}_D
&& \text{on} \, \Gamma_t
\end{aligned}
\right\}.\end{split}\]

### Implementation

We first define the nonlinear elasticity problem, which includes:

Loading the required modules and generating the box mesh using hexahedral elements of degree 1.

```python
import manta
import numpy as np

manta.setDefaultVerbosityLevel(manta.VerbosityLevel.verboseLevel0)

bts = manta.TimeStepStage.beginningOfTimeStep
ets = manta.TimeStepStage.endOfTimeStep

# declare the PhysicalSystem
dom = "cuboid"
nel = 10

ps = manta.PhysicalSystem(
    mesh={
        "generator": "Grid",
        "spaceDimension": 3,
        "lengths": [1.0, 1.0, 5.0],
        "numberOfElements": [nel, nel, 5 * nel],
        "domain": dom,
        "boundaries": ["left", "right", "bottom", "top", "front", "back"],
    },
)
```

Defining the material properties and prescribed loading parameters.

The torsional loading is prescribed on the top surface by imposing the
corresponding rotational displacement as a function of time.

```python
# material properties
ps.addProperty("Constant", material=dom, name="YoungModulus", value=1.0)
ps.addProperty("Constant", material=dom, name="PoissonRatio", value=0.3)

# loading magnitude
ps.addScalarSpatiotemporalLoading(
    lambda t, x, y, z: (
        (np.cos(2. * np.pi * np.sin(np.pi / 180. * t)) - 1.) * x -
         np.sin(2. * np.pi * np.sin(np.pi / 180. * t)) * y
    ),
    name="OuterDisplX",
    boundary="top",
)
ps.addScalarSpatiotemporalLoading(
    lambda t, x, y, z: (
        np.sin(2. * np.pi * np.sin(np.pi / 180. * t)) * x +
        (np.cos(2. * np.pi * np.sin(np.pi / 180. * t)) - 1.) * y
    ),
    name="OuterDisplY",
    boundary="top",
)
```

Declaring the implicit mechanics model and its associated boundary conditions.

```python
### declare the Model
m = manta.Model(
    "ImplicitMechanics",
    ps,
    nonlinearSolver={
        "Newton": {
            "thresholdOnTheFirstResidualNorm": 1e-100,
            "convergenceTolerances": {"relativeConvergenceTolerance": 1e-6},
        }
    },
)

# Material
mat = m.add(
    "SolidMaterial",
    material=dom,
    library="./src/libBehaviour.so",
    behavior="SaintVenantKirchhoffElasticity.mfront",
)

# Boundary conditions
m.add(
    "ImposedDisplacement",
    boundary="bottom",
    components=["UX", "UY", "UZ"],
    strategy="elimination",
)
m.add(
    "ImposedDisplacement",
    boundary="top",
    component="UX",
    value="OuterDisplX",
)
m.add(
    "ImposedDisplacement",
    boundary="top",
    component="UY",
    value="OuterDisplY",
)
m.add(
    "ImposedDisplacement",
    boundary="top",
    component="UZ",
    strategy="elimination",
)
```

Note

Note: the `SaintVenantKirchhoffElasticity.mfront` can be downloaded at
this [link](https://thelfer.github.io/tfel/web/gallery/hyperelasticity/SaintVenantKirchhoffElasticity.mfront). You must modify the first line of the file to remove the
problem's dependence on temperature.

```text
@DSL DefaultModelDSL{
    automatic_declaration_of_the_temperature_as_first_external_state_variable : false
};
```

The label of postprocessed fields associated with the material model can be
displayed via the `manta.info(mat)` command, where `mat` is the
`"SolidMaterial"` brick of the model `m` that points to the MFront file.
For the SVK model given here, you will notice that only
`"DeformationGradient"` and `"FirstPiolaKirchhoffStress"` are given.

For each additional stress or strain measure, we define a dedicated
"MFrontPointWiseModel" custom instance. This instance solves an auxiliary
problem to compute the desired quantity and make it available as a postprocessed
field.

The following example illustrates how to compute the Cauchy stress.

```python
# Auxiliary model
cs = manta.Model(
    "MFrontPointWiseModel",
    ps,
    material=dom,
    library="./src/libBehaviour.so",
    model="CauchyStress",
    hypothesis="Tridimensional",
    quadratureOrder=2,
)
```

The MFront file associated to the cs model reads:

```text
@DSL DefaultModelDSL{
automatic_declaration_of_the_temperature_as_first_external_state_variable :
    false
};
@Model CauchyStress;

@AuxiliaryStateVariable StressStensor sig;
sig.setEntryName("CauchyStress");

@ExternalStateVariable StressTensor pk1;
pk1.setEntryName("FirstPiolaKirchhoffStress");

@ExternalStateVariable DeformationGradientTensor F;
F.setGlossaryName("DeformationGradient");

@Integrator{
sig = convertFirstPiolaKirchhoffStressToCauchyStress(pk1 + dpk1, F + dF);
}
```

And another example illustrates how to compute the second Piola-Kirchhoff stress.

```python
# Auxiliary model
pk2s = manta.Model(
    "MFrontPointWiseModel",
    ps,
    material=dom,
    library="./src/libBehaviour.so",
    model="SecondPiolaKirchhoffStress",
    hypothesis="Tridimensional",
    quadratureOrder=2,
)
```

with the associated MFront file:

```text
@DSL DefaultModelDSL{
automatic_declaration_of_the_temperature_as_first_external_state_variable :
    false
};
@Model SecondPiolaKirchhoffStress;

@AuxiliaryStateVariable StressStensor pk2;
pk2.setEntryName("SecondPiolaKirchhoffStress");

@ExternalStateVariable StressTensor pk1;
pk1.setEntryName("FirstPiolaKirchhoffStress");

@ExternalStateVariable DeformationGradientTensor F;
F.setGlossaryName("DeformationGradient");

@Integrator{
pk2 = syme(invert(F + dF) * (pk1 + dpk1));
}
```

All the models are then assembled into a coupling scheme, which is subsequently
passed to the physical system.

```python
c = manta.CouplingScheme("LoopCouplingScheme", ps, numberOfIterations=1)
c.add(m)
c.add(cs)
c.add(pk2s)
ps.setCouplingScheme(c)
```

The postprocessed fields are now available in Manta and can be exported in VTK
format for visualization in ParaView or Salomé.

```python
# post-processing:
# the components "Strain" and "Stress" are defined in the MFront file.
ps.addPostProcessing(
    "VTKExport",
    outputFileBaseName="meca_svk_torsion",
    fields=[
        {
            "field": "Displacement",
            "fieldType": "nodeField",
            "material": dom,
        },
        {
            "field": "DeformationGradient",
            "fieldType": "ipField",
            "material": dom,
        },
        {
            "field": "FirstPiolaKirchhoffStress",
            "fieldType": "ipField",
            "material": dom,
        },
        {
            "field": "CauchyStress",
            "fieldType": "ipField",
            "material": dom,
        },
        {
            "field": "SecondPiolaKirchhoffStress",
            "fieldType": "ipField",
            "material": dom,
        },
    ],
)
```

### Running a Simulation

After creating the Simulation instance:

```python
nsteps = 72

# Setting up the simulation and run
s = manta.Simulation(ps, times=[i for i in range(nsteps + 1)])
s.run()
```

And compiling all MFront libraries:

```bash
mfront --obuild --interface=generic *.mfront
```

the code can be executed using

```bash
python tuto-meca_svk_torsion.py
```

The results can then be postprocessed in Paraview or Salomé.

|  |  |
| --- | --- |
|  |  |
