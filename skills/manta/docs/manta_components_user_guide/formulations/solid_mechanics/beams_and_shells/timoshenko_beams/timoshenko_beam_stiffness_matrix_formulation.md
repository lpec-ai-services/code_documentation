<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/formulations/solid_mechanics/beams_and_shells/timoshenko_beams/timoshenko_beam_stiffness_matrix_formulation.html -->

# TimoshenkoBeamStiffnessMatrixFormulation

## Introduction

This formulation implements the stiffness matrix for Timoshenko beam elements.
Timoshenko beam elements are relevant for calculation of structures that present
one geometric dimension that is significant with respect to the others, and
differs with Euler-Bernoulli beam elements via the consideration of shear effects.

## Example of usage

The usage of the formulation is slightly different and depends on the number of
geometric dimensions.

For a 2D structural hypothesis:

```c++
    auto &timoForm =
        rm.make<TimoshenkoBeamStiffnessMatrixFormulation<hypothesis,
                                                         YoungModulusEvaluatorType,
                                                         PoissonRatioEvaluatorType,
                                                         mixedGaussian>>(meshSet,
                                                                         quadId,
                                                                         Utranvar,
                                                                         Urotvar,
                                                                         youngModulus,
                                                                         poissonRatio,
                                                                         crossSectionArea,
                                                                         crossSectionArea * principalAxisShearAreaRatio,
                                                                         secondaryAxisSecondMomentArea);
```

For a 3D structural hypothesis:

```c++
    auto &timoForm =
        rm.make<TimoshenkoBeamStiffnessMatrixFormulation<hypothesis,
                                                         YoungModulusEvaluatorType,
                                                         PoissonRatioEvaluatorType,
                                                         mixedGaussian>>(meshSet,
                                                                         quadId,
                                                                         Utranvar,
                                                                         Urotvar,
                                                                         youngModulus,
                                                                         poissonRatio,
                                                                         crossSectionArea,
                                                                         crossSectionArea * principalAxisShearAreaRatio,
                                                                         crossSectionArea * secondaryAxisShearAreaRatio,
                                                                         principalAxisSecondMomentArea,
                                                                         secondaryAxisSecondMomentArea,
                                                                         torsionConstant,
                                                                         principalAxisVector);
```

## Constructors implementation

For a 2D structural hypothesis:

```c++
  TimoshenkoBeamStiffnessMatrixFormulation(const MeshSet &meshSet,
                                           const QuadId quadId,
                                           const DofVar &tranVar,
                                           const DofVar &rotVar,
                                           YoungModulusEvaluatorType E,
                                           PoissonRatioEvaluatorType nu,
                                           Real crossSectionArea,
                                           Real principalAxisShearArea,
                                           Real secondaryAxisSecondMomentArea)
    requires(hypothesis != StructuralHypothesis::tridimensional);
```

For a 3D structural hypothesis:

```c++
  TimoshenkoBeamStiffnessMatrixFormulation(const MeshSet &meshSet,
                                           const QuadId quadId,
                                           const DofVar &tranVar,
                                           const DofVar &rotVar,
                                           YoungModulusEvaluatorType E,
                                           PoissonRatioEvaluatorType nu,
                                           Real crossSectionArea,
                                           Real principalAxisShearArea,
                                           Real secondaryAxisShearArea,
                                           Real principalAxisSecondMomentArea,
                                           Real secondaryAxisSecondMomentArea,
                                           Real torsionConstant,
                                           const ColVector<geoDim> &principalAxisVector = setZero<ColVector<geoDim>>())
    requires(hypothesis == StructuralHypothesis::tridimensional);
```

## Parameters

`TimoshenkoBeamStiffnessMatrixFormulation` has the following template parameters:

- `hypothesis` is the **structural hypothesis** (see `StructuralHypothesis`).
  The value of `hypothesis` dictates which constructor should be called .

- `youngModulusEvaluatorType` is the **type of the Young Modulus** ;
- `poissonRatioEvaluatorType` is the **type of the Poisson Ratio** ;

- `mixedGaussian` is a boolean which allow the use of **mixed gaussian quadrature**,
  as described in the [theory manual](../../../../../theory_manual/solid_mechanics/beams/beam_theory.md#theory-beam).

`TimoshenkoBeamStiffnessMatrixFormulation` has the following parameters:

- `quadId` is the **quadrature identifier** ;

- `youngModulus` is the **Young Modulus** of the material ;
- `poissonRatio` is the **Poisson Ratio** of the material ;

- `tranVar`, is the `DofVar` of the `NodeField` defined over
  `meshSet` that represents the translation DOFs;
- `rotVar`, is the `DofVar` of the `NodeField` defined over
  `meshSet` that represents the rotation DOFs;

- `meshSet` is the **mesh set** over which the formulation is to be applied ;
- `crossSectionArea` is the geometric **area** of the cross-section ;
- `principalAxisVector` is the **orientation vector**, which defines the
  **principal axis** of the cross section (usually named **OY**);
- `principalAxisShearArea` is the **shear area** of the cross section along
  the principal cross section axis (**OY**);
- `secondaryAxisShearArea` is the **shear area** of the cross section along
  the secondary cross section axis (**OZ**);
- `principalAxisSecondMomentArea` is the **second moment of area** of the
  cross section along the principal cross section axis (**OY**);
- `secondaryAxisSecondMomentArea` is the **second moment of area** of the
  cross section along the secondary cross section axis (**OZ**);
- `torsionConstant` is the **torsion constant** of the cross-section around
  the beam axis.

## List of commented examples and verification tests

- [Euler and Timoshenko beams verification tests - Cantilever beam with end forces](../../../../../verification_tests/manta_components_verification_tests/solid_mechanics/fem_implicit_linear/beams/cantilever_endforce.md#cantilever-endforce-beam-verification-tests)
- [Euler and Timoshenko beam verification tests - The clamped_free_eigenmodes cases](../../../../../verification_tests/manta_components_verification_tests/solid_mechanics/fem_eigenmodes/beams/clamped_free_eigenmodes.md#clamped-free-eigenmodes-beam-verification-tests)

## Description

This formulation implements the **Timoshenko beam formulation**, which allows
the consideration of shear deformation effects alongside bending. It is
particularly suitable for scenarios where shear effects significantly influence
the beam's behavior, such as in situations where one dimension of the cross-section
cannot be neglected with respect to the beam length.

The formulation allows for a precise control over the influence of the shear
effects via `principalAxisShearArea` and `secondaryAxisShearArea`
parameters. The **ratio** between these quantities and `crossSectionArea`
should yield the **shear coefficient**, usually noted \(\kappa\).

Note

If `mixedGaussian` is set to `true`, the formulation uses an
`Integrand` that behaves identically as what is done in Cast3M.

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
