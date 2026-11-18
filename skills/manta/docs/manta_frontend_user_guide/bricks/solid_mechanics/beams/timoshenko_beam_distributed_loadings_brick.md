<!-- source: https://manta-project.gitlab.io/manta/manta_frontend_user_guide/bricks/solid_mechanics/beams/timoshenko_beam_distributed_loadings_brick.html -->

# The `TimoshenkoBeamDistributedLoadings` brick

The `TimoshenkoBeamDistributedLoadings` implements distributed loads for the
Timoshenko beam model.

This brick can be used in both implicit and explicit mechanics.

## Example of usage

The following code adds the a `TimoshenkoBeamDistributedLoadings` brick to a mechanical model:

- In two dimensions :

```python
    model.add(
        'TimoshenkoBeamDistributedLoadings',  
        domain = 'beam', 
        hypothesis = 'PlaneStress', 
        distributedForces = loads, 
        distributedAxialMoment = 0., 
        localCoordinate = local_coordinate,
        youngModulus = 'E',
        poissonRatio = 'nu',
        crossSectionArea = 'S', 
        principalAxisShearArea = 'Ay',
        secondaryAxisSecondMomentArea = 'Iz',
    )
```

- In three dimensions :

```python
    model.add(
        'TimoshenkoBeamDistributedLoadings',  
        domain = 'beam', 
        hypothesis = 'tridimensional', 
        distributedForces = loads, 
        distributedMoments = (0., 0., 0.),
        localCoordinate = local_coordinate,
        principalAxisVector = ORIENTATION_VECTOR,
        youngModulus = 'E',
        poissonRatio = 'nu',
        crossSectionArea = 'S',
        principalAxisShearArea = 'Ay',
        secondaryAxisShearArea = 'Az',
        torsionConstant = 'Jx', 
        principalAxisSecondMomentArea = 'Iy',
        secondaryAxisSecondMomentArea = 'Iz',
    )
```

## Main parameters

The main parameters used to initialize the brick are:

- `material` or `domain`: mesh set over which the brick is defined
- `materials` or `domains`: list of mesh set over which the brick is defined
- `hypothesis`: structural hypothesis (`axisymmetrical` is prohibited)
- `quadratureOrder` (*optional*):
  order of Gauss quadrature. Defaults to \(2\).
- `localCoordinate` (*optional*): Defines if the loads are given in the local coordinate system
  (`true`) or in the global coordinate system (`false`). Defaults to
  `true`.
- `distributedForces` (*optional*): Vector defining the distributed forces. Each component
  of the vector must be a real value or a string. Defaults to `(0., 0., 0.)`.

- `youngModulus` (*optional*):
  Name of the parameter holding the Young modulus
  of the material. Defaults to `youngModulus`.
- `poissonRatio` (*optional*):
  Name of the parameter holding the Poisson ratio
  of the material. Defaults to `poissonRatio`.

- `crossSectionArea` (*optional*):
  Value or name of the parameter holding
  the area of the cross section. Default to `crossSectionArea`.
- `principalAxisShearArea` (*optional*):
  Value or name of the parameter holding
  the shear area of the cross section along the principal cross-section axis,
  usually noted \(A_y\). Default to `principalAxisShearArea`.
- `secondaryAxisSecondMomentArea` (*optional*):
  Value or name of the parameter holding
  the second moment of area around the principal cross-section axis, usually noted
  \(I_z\). Defaults to `secondaryAxisSecondMomentArea`.

The following parameters are only valid in **2D**:

- `distributedAxialMoment` (*optional*):
  Parameter defining the distributed axial moment. This parameter must be a real
  value or a string. Defaults to `0.`

The following parameters are only valid in **3D**:

- `distributedMoments` (*optional*):
  Vector defining the distributed moments. Each component of the vector must be
  a real value or a string. Defaults to `(0., 0., 0.)`.
- `principalAxisVector` (*optional*):
  Vector defining the orientation of the cross section (local \(Oy\) vector).
  Defaults to `(0., 0., 0.)`.

Note

If the distributed forces are given in the global coordinate system, then
`principalAxisVector` must be given to be able to write the distributed
loads in the local coordinate system.

Note

At least one load must be defined. One cannot instantiate this brick with
all distributed forces and moment set to zero.

## Physical description

This brick implements distributed forces and moments for **Timoshenko beams**.

The Timoshenko beam theory is described in the [theory manual](../../../../theory_manual/solid_mechanics/beams/beam_theory.md#theory-beam).

For **2D** formulations, the local basis is constructed as such :

- The first vector is the **direction vector** of the considered element ;
- The second vector is **orthogonal** to the first vector (\(90°\)
  counterclockwise).

For **3D** formulations, the local basis is constructed as such:

- The first vector is the **direction vector** of the considered element ;
- The second vector is **generated** via `principalAxisVector` and is
  orthogonal to the first vector. As such, `principalAxisVector` must not
  be colinear with the direction vector of any mesh element, otherwise the local
  basis cannot be computed ;
- The third vector is equal to the **cross-product** between the first two vectors.

Note

In **3D**, if `principalAxisVector` is not given or is of zero norm
(which is only allowed if the beam is symmetrical along both its axis), an
arbitrary vector is chosen to define the local basis. The arbitrary vector
is chosen such as its \(z\), \(y\) or \(x\) coordinate is equal
to zero, whichever comes first.

## Supported structural hypotheses and elements

The following table summarizes the list of supported structural
hypotheses and, for each hypothesis, the list of elements.

| Structural hypothesis | Supported elements |
| --- | --- |
| *Tridimensional* | *seg2* |
| *PlaneStrain* | *seg2* |
| *PlaneStress* | *seg2* |
| *Axisymmetrical* | (unimplemented) |

## Compatible models

This brick is compatible with the following models:

- [The ExplicitMechanics model](../../../models/solid_mechanics/explicit_solid_mechanics.md#explicit-mechanics-model)
- [The ImplicitMechanics model](../../../models/solid_mechanics/implicit_solid_mechanics.md#implicit-mechanics-model)
