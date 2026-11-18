<!-- source: https://manta-project.gitlab.io/manta/manta_frontend_user_guide/bricks/solid_mechanics/beams/euler_beam_brick.html -->

# The `EulerBeam` brick

The `EulerBeam` implements the Euler beam model in implicit mechanics.

## Example of usage

The following code adds the a `EulerBeam` brick to a mechanical model:

- In two dimensions :

```python
    model.add(
        'EulerBeam', 
        domain = 'beam', 
        hypothesis = 'PlaneStress', 
        youngModulus = 'E',
        poissonRatio = 'nu',
        crossSectionArea = 'S', 
        secondaryAxisSecondMomentArea = 'Iz',
    )
```

- In three dimensions :

```python
    model.add(
        'EulerBeam', 
        domain = 'beam', 
        hypothesis = 'tridimensional', 
        youngModulus = 'E',
        poissonRatio = 'nu',
        crossSectionArea = 'S',
        torsionConstant = 'Jx', 
        principalAxisSecondMomentArea = 'Iy',
        secondaryAxisSecondMomentArea = 'Iz',
        principalAxisVector = ORIENTATION_VECTOR,
    )
```

## Main parameters

The main parameters used to initialize the brick are:

- `material` or `domain`:
  mesh set over which the brick is defined
- `materials` or `domains`:
  list of mesh set over which the brick is defined
- `hypothesis`:
  structural hypothesis (`axisymmetrical` is prohibited)

- `quadratureOrder` (*optional*):
  order of Gauss quadrature. Defaults to \(2\).

- `youngModulus` (*optional*):
  Name of the parameter holding the Young modulus
  of the material. Defaults to `youngModulus`.
- `poissonRatio` (*optional*):
  Name of the parameter holding the Poisson ratio
  of the material. Defaults to `poissonRatio`.

- `crossSectionArea` (*optional*):
  Value or name of the parameter holding
  the area of the cross section. Default to `crossSectionArea`.
- `secondaryAxisSecondMomentArea` (*optional*):
  Value or name of the parameter holding
  the second moment of area around the principal cross-section axis, usually noted
  \(I_z\). Defaults to `secondaryAxisSecondMomentArea`.

The following parameters are only valid in **3D**:

- `principalAxisSecondMomentArea` (*optional*):
  Value or name of the parameter holding
  the second moment of area around the secondary cross-section axis, usually noted
  \(I_y\). Defaults to `principalAxisSecondMomentArea`.
- `torsionConstant` (*optional*):
  Value or name of the parameter holding the torsion
  constant, usually noted \(J_x\). Defaluts to `torsionConstant`.
- `principalAxisVector` (*optional*):
  Vector defining the orientation of the cross section
  (local \(Oy\) vector)

## Physical description

This brick implements the **Euler beam** in **implicit mechanics**, which
neglects the shear effects contribution alongside bending. It is particularly
suitable for scenarios where shear effects do not significantly influence the
beam's behavior, such as in situations where the beam is slender.

The Euler beam theory is described in the [theory manual](../../../../theory_manual/solid_mechanics/beams/beam_theory.md#theory-beam).

As of now, only the stiffness matrix is implemented. Therefore, only
static or pseudo-static **linear** calculations are possible.

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
arbitrary vector is chosen to define the local basis. The arbitrary vector is
chosen such as its \(z\), \(y\) or \(x\) coordinate is equal to
zero, whichever comes first.

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

- [The ImplicitMechanics model](../../../models/solid_mechanics/implicit_solid_mechanics.md#implicit-mechanics-model)
