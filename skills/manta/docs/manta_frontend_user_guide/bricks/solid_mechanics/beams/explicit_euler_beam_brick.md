<!-- source: https://manta-project.gitlab.io/manta/manta_frontend_user_guide/bricks/solid_mechanics/beams/explicit_euler_beam_brick.html -->

# The `ExplicitEulerBeam` brick

The `ExplicitEulerBeam` implements the Euler beam model in explicit
mechanics.

## Example of usage

The following code adds the `ExplicitEulerBeam` brick to a mechanical model:

- In two dimensions :

```python
    model.add(
        'ExplicitEulerBeam', 
        domain = 'beam', 
        hypothesis = 'planeStress', 
        youngModulus = 'E',
        poissonRatio = 'nu',
        massDensity = 'rho',
        crossSectionArea = 'S',
        secondaryAxisSecondMomentArea = 'Iz',
        lumpingRotationMethod = lumping_method,
    )
```

- In three dimensions :

```python
    model.add(
        'ExplicitEulerBeam', 
        domain = 'beam', 
        hypothesis = 'tridimensional', 
        youngModulus = 'E',
        poissonRatio = 'nu',
        massDensity = 'rho',
        crossSectionArea = 'S',
        torsionConstant = 'Jx', 
        principalAxisSecondMomentArea = 'Iy',
        secondaryAxisSecondMomentArea = 'Iz',
        principalAxisVector = ORIENTATION_VECTOR,
        lumpingRotationMethod = lumping_method,
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
  order of Gauss quadrature. Defaults to \(4\).

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

- `lumpingTranslationMethod` (*optional*): lumping method for the translation
  degrees of freedom. If the cross-section and material properties are constant
  along each finite element, the chosen method has no impact on the results.

  - \(0\) (*default*): The chosen value for the lumped mass matrix is the sum of the
    terms found in the lines corresponding to the traction-compression DOFs, i.e.
    \(\rho S \varphi_u^i (\varphi_u^1 + \varphi_u^2) = \rho S \varphi_u^i\)
  - \(1\): The chosen value for the lumped mass matrix is the sum of the
    terms found in the lines corresponding to the bending DOFs, i.e.
    \(\rho S \varphi_v^i (\varphi_v^1 + \varphi_v^2) = \rho S \varphi_v^i\)
- `lumpingRotationMethod` (*optional*): lumping method for the rotation
  degrees of freedom.

  - \(0\) (*default*): User specific method is used. The coefficients are
    given in the `userLumpingCoefficients` parameter.
  - \(1\): Lepareux lumping method [[LG01](../../../../references/references.md#id62)] ;
  - \(2\): Ruszniewski lumping method [[Rus81](../../../../references/references.md#id61)] ;
  - \(3\): Belytschko and Mindle lumping method [[BM80](../../../../references/references.md#id63)] ;
  - \(4\): Key and Beisinger lumping method [[KB71](../../../../references/references.md#id64)].
- `userLumpingCoefficients` (*optional*): coefficients for the
  user lumping method of rotation DOFs. \(4\) parameters are expected in
  **2D** (integrated terms that include \(I_y\) are ignored), where as
  \(7\) parameters are expected in **3D**.

Table 2 Lumping strategy coefficients for bending

| Parameter | Integrand | Integrated term |
| --- | --- | --- |
| `diagonalEulerBending` | \(\rho S \varphi_\theta^2\) | \(\rho S L \cdot \frac{L^2}{105}\) |
| `summedEulerBending` | \(\rho S \varphi_\theta (\varphi_\theta^1 + \varphi_\theta^2)\) | \(\rho S L \cdot \frac{L^2}{420}\) |
| `principalAxisDiagonalRayleighBending` | \(\rho I_y (\partial_x \varphi_\theta)^2\) | \(\rho S L \frac{2}{15}\frac{I_y}{S}\) |
| `principalAxisSummedRayleighBending` | \(\rho I_y \partial_x \varphi_\theta (\partial_x\varphi_\theta^1 + \partial_x\varphi_\theta^2)\) | \(\rho S L \frac{1}{10}\frac{I_y}{S}\) |
| `secondaryAxisDiagonalRayleighBending` | \(\rho I_z (\partial_x \varphi_\theta)^2\) | \(\rho S L \frac{2}{15}\frac{I_z}{S}\) |
| `secondaryAxisSummedRayleighBending` | \(\rho I_z \partial_x \varphi_\theta (\partial_x\varphi_\theta^1 + \partial_x\varphi_\theta^2)\) | \(\rho S L \frac{1}{10}\frac{I_z}{S}\) |
| `maximumSummedRayleighBending` | \(\rho \max(I_y, I_z) \partial_x\varphi_\theta (\partial_x\varphi_\theta^1 + \partial_x\varphi_\theta^2)\) | \(\rho S L \frac{1}{10}\frac{\max(I_y, I_z)}{S}\) |

Note

Find more details on the lumping methods in [theory manual](../../../../theory_manual/solid_mechanics/beams/beam_theory.md#theory-beam).

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

This brick implements the **Euler beam** in **explicit mechanics**, which
neglects the shear effects contribution alongside bending. It is particularly
suitable for scenarios where shear effects do not significantly influence the
beam's behavior, such as in situations where the beam is slender.

The Euler beam theory is described in the [theory manual](../../../../theory_manual/solid_mechanics/beams/beam_theory.md#theory-beam).

You can also find details about lumping methods [here](../../../../theory_manual/solid_mechanics/beams/beam_theory.md#theory-beam-mass-matrix-lumping).
Specifically for rotation DOFs, details can be found [here](../../../../theory_manual/solid_mechanics/beams/beam_theory.md#theory-beam-bending-lumping).
If you use the user lumping method, the classical decomposition of the literature
coefficients is given in [this table](../../../../theory_manual/solid_mechanics/beams/beam_theory.md#theory-beam-implemented-bending-coefficients).

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

- [The ExplicitMechanics model](../../../models/solid_mechanics/explicit_solid_mechanics.md#explicit-mechanics-model)
