<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/formulations/solid_mechanics/beams_and_shells/euler_beams/euler_beam_explicit_formulation.html -->

# EulerBeamExplicitFormulation

## Introduction

This formulation implements the Euler-Bernoulli beam elements suited for
**explicit integration scheme**. It encapsulates both stiffness and mass terms,
and is usable out-of-the-box to model the necessary euler beam behaviours.

Euler-Bernoulli beam elements are relevant for the calculation of structures that present
one geometric dimension that is significant with respect to the others, and
differs with Timoshenko beam elements via the non-consideration of shear effects.

Euler-Bernoulli beams are particularly adapted for beam that are slender.

## Example of usage

The usage of the formulation is slightly different and depends on the number of
geometric dimensions.

For a 2D structural hypothesis:

```c++
  auto &eulerForm = rm.make<EulerBeamExplicitFormulation<hypothesis,
                                                         YoungModulusEvaluatorType,
                                                         PoissonRatioEvaluatorType,
                                                         MassDensityEvaluatorType,
                                                         kinematicDescription>>(beam,
                                                                                QuadId::seg4,
                                                                                QuadId::seg2,
                                                                                Atranvar,
                                                                                Arotvar,
                                                                                Utran,
                                                                                Urot,
                                                                                youngModulus,
                                                                                poissonRatio,
                                                                                rho,
                                                                                beamProperties,
                                                                                lumpingTransStrat,
                                                                                lumpingRotaStrat);
```

For a 3D structural hypothesis:

```c++
  auto &eulerForm = rm.make<EulerBeamExplicitFormulation<hypothesis,
                                                         YoungModulusEvaluatorType,
                                                         PoissonRatioEvaluatorType,
                                                         MassDensityEvaluatorType,
                                                         kinematicDescription>>(beam,
                                                                                QuadId::seg4,
                                                                                QuadId::seg2,
                                                                                Atranvar,
                                                                                Arotvar,
                                                                                Utran,
                                                                                Urot,
                                                                                youngModulus,
                                                                                poissonRatio,
                                                                                rho,
                                                                                beamProperties,
                                                                                lumpingTransStrat,
                                                                                lumpingRotaStrat);
```

## Constructors implementation

For a 2D structural hypothesis:

```c++
  EulerBeamExplicitFormulation(const MeshSet &meshSet,
                               const QuadId quadIdMass,
                               const QuadId quadIdForces,
                               const DofVar &tranVar,
                               const DofVar &rotVar,
                               const FieldRef<const NodeField<nDofsPerNodeTran, 1>> &translationField,
                               const FieldRef<const NodeField<nDofsPerNodeRot, 1>> &rotationField,
                               YoungModulusEvaluatorType E,
                               PoissonRatioEvaluatorType nu,
                               MassDensityEvaluatorType rho,
                               Real crossSectionArea,
                               Real secondaryAxisSecondMomentArea,
                               const LumpingTranslationStrategy transStrat,
                               Real diagonalEulerBending,
                               Real summedEulerBending,
                               Real secondaryAxisDiagonalRayleighBending,
                               Real secondaryAxisSummedRayleighBending)
    requires(hypothesis != StructuralHypothesis::tridimensional);
```

For a 3D structural hypothesis:

```c++
  EulerBeamExplicitFormulation(const MeshSet &meshSet,
                               const QuadId quadIdMass,
                               const QuadId quadIdForces,
                               const DofVar &tranVar,
                               const DofVar &rotVar,
                               const FieldRef<const NodeField<nDofsPerNodeTran, 1>> &translationField,
                               const FieldRef<const NodeField<nDofsPerNodeRot, 1>> &rotationField,
                               YoungModulusEvaluatorType E,
                               PoissonRatioEvaluatorType nu,
                               MassDensityEvaluatorType rho,
                               Real crossSectionArea,
                               Real principalAxisSecondMomentArea,
                               Real secondaryAxisSecondMomentArea,
                               Real torsionConstant,
                               const LumpingTranslationStrategy transStrat,
                               Real diagonalEulerBending,
                               Real summedEulerBending,
                               Real principalAxisDiagonalRayleighBending,
                               Real principalAxisSummedRayleighBending,
                               Real secondaryAxisDiagonalRayleighBending,
                               Real secondaryAxisSummedRayleighBending,
                               Real maximumSummedRayleighBending,
                               const ColVector<geoDim> &principalAxisVector = setZero<ColVector<geoDim>>())
    requires(hypothesis == StructuralHypothesis::tridimensional);
```

## Parameters

`EulerBeamExplicitFormulation` has the following template parameters:

- `hypothesis` is the **structural hypothesis** (see `StructuralHypothesis`).
  The value of `hypothesis` dictates which constructor should be called .

- `youngModulusEvaluatorType` is the **type of the Young Modulus** ;
- `poissonRatioEvaluatorType` is the **type of the Poisson Ratio**.

- `massDensityEvaluatorType` is the **type of the mass density**.

- `kinematicDescription` is the **kinematic description**. It can be Lagrangian or corotational.

Note

If the `kinematicDescription` is Lagrangian the total displacement must
be used for the `translationField` and `rotationField` parameters
(see below for the description of these parameters). However, if the
corotational description is used, the translation and rotation increments
must be used instead.

`EulerBeamExplicitFormulation` has the following parameters:

- `quadIdMass` is the **quadrature identifier** for the integration of the
  lumped mass matrix ;
- `quadIdForces` is the **quadrature identifier** for the integration of the
  internal forces vector ;

- `youngModulus` is the **Young Modulus** of the material ;
- `poissonRatio` is the **Poisson Ratio** of the material ;

- `massDensity` is the **mass density** of the material ;

- `tranVar`, is the `DofVar` of the `NodeField` defined over
  `meshSet` that represents the translation DOFs;
- `rotVar`, is the `DofVar` of the `NodeField` defined over
  `meshSet` that represents the rotation DOFs;

- `translationField` is the `NodeField` that contains the
  **translation field** used to compute the internal forces ;
- `rotationField` is the `NodeField` that contains the
  **rotation field** used to compute the internal forces ;

- `meshSet` is the **mesh set** over which the formulation is to be applied ;
- `principalAxisVector` is the **orientation vector**, which defines the
  **principal axis** of the cross section (usually named **OY**);

- `crossSectionArea` is the geometric **area** of the cross-section ;
- `principalAxisSecondMomentArea` is the **second moment of area** of the
  cross section along the principal cross section axis (**OY**);
- `secondaryAxisSecondMomentArea` is the **second moment of area** of the
  cross section along the secondary cross section axis (**OZ**);
- `torsionConstant` is the **torsion constant** of the cross-section around
  the beam axis.

- `lumpingTranslationStrategy` is the **lumping strategy** for the translation
  motions, which can be either `LumpingTranslationStrategy::traction` or
  `LumpingTranslationStrategy::bending`.

All other lumping strategy parameters are real multiplicative constants that
correspond to the following terms (refer to the
[theory manual](../../../../../theory_manual/solid_mechanics/beams/beam_theory.md#theory-beam-implemented-bending-coefficients) for further details):

Table 5 Lumping strategy coefficients for bending

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

`tranVar` and `rotVar` parameters should be the dof variables of the
acceleration node fields, and `translationField` and `rotationField`
parameters should contain the displacement and rotation node fields
(or displacement and rotation increments for the corotational kinematic description)
for this formulation to be used as intended.

## List of commented examples and verification tests

- [Euler beams verification tests - Explicit resolution of a cantilever beam under distributed force](../../../../../verification_tests/manta_components_verification_tests/solid_mechanics/fem_explicit_linear/beams/clamped_free.md#cantilever-endforce-beam-verification-tests-explicit)
- [Euler beams verification tests - Calculation of the critical time step for explicit schemes](../../../../../verification_tests/manta_components_verification_tests/solid_mechanics/fem_explicit_linear/beams/critical_time_step.md#euler-beam-explicit-critical-time-step)
- [Euler beams verification tests - Beam undergoing out-of-plane large deflection](../../../../../verification_tests/manta_components_verification_tests/solid_mechanics/fem_explicit_linear/beams/large_deflection.md#euler-beam-large-deflection)

## Description

This formulation implements the **Euler beam formulation**, which neglects the
shear effects contribution alongside bending. It is particularly
suitable for scenarios where shear effects do not significantly influence the beam's
behavior, such as in situations where the beam is slender.

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

The lumping strategies are left to the choice of the user such as they have
a fine control on the terms that will be used in the lumped mass matrix. Classical
lumping coefficients available in literature are described in the
[theory manual](../../../../../theory_manual/solid_mechanics/beams/beam_theory.md#theory-beam-implemented-bending-coefficients).

Additionally, this formulation comes with **critical time step calculation**,
as described in the [appropriate beam theory section](../../../../../theory_manual/solid_mechanics/beams/beam_theory.md#theory-beam-critical-time-step).
To that end, the geometrical and material properties are assumed to be constant
over each element.

## Pre-conditions

The user is responsible to check the following pre-conditions:

- `poissonRatio` has a value (strictly) between \(-1\) and \(0.5\).
- All other geometrical or material properties have strictly positive values ;
- `principalAxisVector` is not colinear with any of the direction vector of
  the mesh elements.

## Notes

- `principalAxisVector` only dictates the direction of the principal axis
  of the beam. Formulations that relies on the global mesh coordinates do not
  account for this vector (i.e. the local and global basis may be different).
