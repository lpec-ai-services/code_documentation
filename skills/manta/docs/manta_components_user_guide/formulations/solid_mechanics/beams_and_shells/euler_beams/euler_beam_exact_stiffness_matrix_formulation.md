<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/formulations/solid_mechanics/beams_and_shells/euler_beams/euler_beam_exact_stiffness_matrix_formulation.html -->

# EulerBeamExactStiffnessMatrixFormulation

## Introduction

This formulation implements the stiffness matrix for Euler-Bernoulli beam elements,
integrated **exactly** at the element nodes. Euler-Bernoulli beam elements are
relevant for the calculation of structures that present one geometric dimension
that is significant with respect to the others, and differs with Timoshenko
beam elements via the non-consideration of shear effects.

Euler-Bernoulli beams are particularly adapted for beam that are slender.

This particular formulation can only be used if the material and geometric
properties of the beam are constant across each element, as it relies on an
exact integration method formulated with the hypothesis that the properties
are constant.

## Example of usage

The usage of the formulation is slightly different and depends on the number of
geometric dimensions.

For a 2D structural hypothesis:

```c++
    auto &eulerForm = rm.make<EulerBeamExactStiffnessMatrixFormulation<hypothesis>>(
        meshSet, Utranvar, Urotvar, youngModulus, poissonRatio, crossSectionArea, secondaryAxisSecondMomentArea);
```

For a 3D structural hypothesis:

```c++
    auto &eulerForm = rm.make<EulerBeamExactStiffnessMatrixFormulation<hypothesis>>(meshSet,
                                                                                    Utranvar,
                                                                                    Urotvar,
                                                                                    youngModulus,
                                                                                    poissonRatio,
                                                                                    crossSectionArea,
                                                                                    principalAxisSecondMomentArea,
                                                                                    secondaryAxisSecondMomentArea,
                                                                                    torsionConstant,
                                                                                    principalAxisVector);
```

## Constructors implementation

For a 2D structural hypothesis:

```c++
  EulerBeamExactStiffnessMatrixFormulation(const MeshSet &meshSet,
                                           const DofVar &tranVar,
                                           const DofVar &rotVar,
                                           Real E,
                                           Real nu,
                                           Real crossSectionArea,
                                           Real secondaryAxisSecondMomentArea)
    requires(hypothesis != StructuralHypothesis::tridimensional);
```

For a 3D structural hypothesis:

```c++
  EulerBeamExactStiffnessMatrixFormulation(const MeshSet &meshSet,
                                           const DofVar &tranVar,
                                           const DofVar &rotVar,
                                           Real E,
                                           Real nu,
                                           Real crossSectionArea,
                                           Real principalAxisSecondMomentArea,
                                           Real secondaryAxisSecondMomentArea,
                                           Real torsionConstant,
                                           const ColVector<geoDim> &principalAxisVector = setZero<ColVector<geoDim>>())
    requires(hypothesis == StructuralHypothesis::tridimensional);
```

## Parameters

`EulerBeamExactStiffnessMatrixFormulation` has the following template parameter:

- `hypothesis` is the **structural hypothesis** (see `StructuralHypothesis`).
  The value of `hypothesis` dictates which constructor should be called .

`EulerBeamExactStiffnessMatrixFormulation` has the following parameters:

- `youngModulus` is the **Young Modulus** of the material ;
- `poissonRatio` is the **Poisson Ratio** of the material ;

- `tranVar`, is the `DofVar` of the `NodeField` defined over
  `meshSet` that represents the translation DOFs;
- `rotVar`, is the `DofVar` of the `NodeField` defined over
  `meshSet` that represents the rotation DOFs;

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

## List of commented examples and verification tests

- [Euler and Timoshenko beams verification tests - Cantilever beam with end forces](../../../../../verification_tests/manta_components_verification_tests/solid_mechanics/fem_implicit_linear/beams/cantilever_endforce.md#cantilever-endforce-beam-verification-tests)

## Description

This formulation implements the **Euler beam formulation**, which neglects the
shear effects contribution alongside bending. It is particularly
suitable for scenarios where shear effects do not significantly influence the beam's
behavior, such as in situations where the beam is slender.

Note

Contrary to [EulerBeamStiffnessMatrixFormulation](euler_beam_stiffness_matrix_formulation.md#formulation-euler-beam-stiffness), this formulation does not use any
quadrature, as the elementary stiffness matrix is integrated exactly at the
element **nodes**. This however demands an additional hypothesis: the geometric
and material properties must be constant through the element. Results are
not guaranteed if those hypothesis are not met.

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

- This formulation does not allow material and geometric properties that are not
  constant through the element.
