<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/formulations/solid_mechanics/beams_and_shells/timoshenko_beams/timoshenko_beam_internal_forces_formulation.html -->

# TimoshenkoBeamInternalForcesFormulation

## Introduction

This formulation implements the internal force vector for Timoshenko beam elements.
Timoshenko beam elements are relevant for the analysis of structures for which one
geometrical dimension is significantly larger than the others. Unlike Euler-Bernoulli
beam elements, Timoshenko beam elements take shear deformation into account.

Timoshenko beams are particularly suitable for moderately thick beams, for which shear
effects are not negligible.

## Example of usage

The use of the Timoshenko beam internal forces formulation depends on whether the
problem is two-dimensional or three-dimensional. The following examples show how the
formulation is initialized in both cases.

For 2D:

```c++
    auto &timoshenkoInternalForcesForm =
        rm.make<TimoshenkoBeamInternalForcesFormulation<hypothesis, YoungModulusEvaluatorType, PoissonRatioEvaluatorType>>(
            beam, quadId, Utranvar, Urotvar, Wtran, Wrot, youngModulus, poissonRatio, sec, Asy, Iz);
```

For 3D:

```c++
    auto &timoshenkoInternalForcesForm =
        rm.make<TimoshenkoBeamInternalForcesFormulation<hypothesis, YoungModulusEvaluatorType, PoissonRatioEvaluatorType>>(
            beam,
            quadId,
            Utranvar,
            Urotvar,
            Wtran,
            Wrot,
            youngModulus,
            poissonRatio,
            sec,
            Asy,
            Asz,
            Iy,
            Iz,
            Ix,
            principalAxisVector);
```

## Constructor implementation

There are two constructors for the Timoshenko beam internal forces formulation. The
2D constructor is defined as follows:

```c++
  TimoshenkoBeamInternalForcesFormulation(const MeshSet &meshSet,
                                          const QuadId quadId,
                                          const DofVar &tranVar,
                                          const DofVar &rotVar,
                                          const FieldRef<const NodeField<nDofsPerNodeTran, 1>> &translationField,
                                          const FieldRef<const NodeField<nDofsPerNodeRot, 1>> &rotationField,
                                          YoungModulusEvaluatorType E,
                                          PoissonRatioEvaluatorType nu,
                                          Real crossSectionArea,
                                          Real principalAxisShearArea,
                                          Real secondaryAxisSecondMomentArea)
    requires(hypothesis != StructuralHypothesis::tridimensional);
```

For the 3D case, the constructor is defined as follows:

```c++
  TimoshenkoBeamInternalForcesFormulation(const MeshSet &meshSet,
                                          const QuadId quadId,
                                          const DofVar &tranVar,
                                          const DofVar &rotVar,
                                          const FieldRef<const NodeField<nDofsPerNodeTran, 1>> &translationField,
                                          const FieldRef<const NodeField<nDofsPerNodeRot, 1>> &rotationField,
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

`TimoshenkoBeamInternalForcesFormulation` has the following template parameters:

- `hypothesis` is the **structural hypothesis** (see `StructuralHypothesis`).
  The value of `hypothesis` dictates which constructor should be called .

- `youngModulusEvaluatorType` is the **type of the Young Modulus** ;
- `poissonRatioEvaluatorType` is the **type of the Poisson Ratio** ;

`TimoshenkoBeamInternalForcesFormulation` has the following parameters:

- `quadId` is the **quadrature identifier** ;

- `tranVar`, is the `DofVar` of the `NodeField` defined over
  `meshSet` that represents the translation DOFs;
- `rotVar`, is the `DofVar` of the `NodeField` defined over
  `meshSet` that represents the rotation DOFs;

- `translationField` is the `NodeField` that contains the
  **translation field** used to compute the internal forces ;
- `rotationField` is the `NodeField` that contains the
  **rotation field** used to compute the internal forces ;

- `youngModulus` is the **Young Modulus** of the material ;
- `poissonRatio` is the **Poisson Ratio** of the material ;

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

- [Timoshenko beam verification tests - Explicit solution of a double pinned beam under a distributed force](../../../../../verification_tests/manta_components_verification_tests/solid_mechanics/fem_explicit_linear/beams/double_pinned_3d.md#double-pinned-timoshenko-beam-verification-tests-explicit)

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
