<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/formulations/solid_mechanics/beams_and_shells/euler_beams/euler_beam_distributed_load_formulation.html -->

# EulerBeamDistributedLoadFormulation

## Introduction

This formulation implements the external distributed loads for Euler-Bernoulli
beam elements. Distributed loads and moments can be defined, whether constant
across the beam or not.

## Example of usage

The usage of the formulation is slightly different and depends on the number of
geometric dimensions.

For a 2D structural hypothesis:

```c++
  auto &eulerLoadForm = rm.make<EulerBeamDistributedLoadFormulation<hypothesis, LoadEvaluatorType>>(
      meshSet, quadId, Utranvar, Urotvar, fx, fy, mz, localCoord);
```

For a 3D structural hypothesis:

```c++
  auto &eulerLoadForm = rm.make<EulerBeamDistributedLoadFormulation<hypothesis, LoadEvaluatorType>>(
      meshSet, quadId, Utranvar, Urotvar, fx, fy, fz, mx, my, mz, principalAxisVector, localCoord);
```

## Constructors implementation

For a 2D structural hypothesis:

```c++
  EulerBeamDistributedLoadFormulation(const MeshSet &meshSet,
                                      const QuadId quadId,
                                      const DofVar &tranVar,
                                      const DofVar &rotVar,
                                      const LoadEvaluatorType fx,
                                      const LoadEvaluatorType fy,
                                      const LoadEvaluatorType mz,
                                      Bool localCoord = true)
    requires(hypothesis != StructuralHypothesis::tridimensional);
```

For a 3D structural hypothesis:

```c++
  EulerBeamDistributedLoadFormulation(const MeshSet &meshSet,
                                      const QuadId quadId,
                                      const DofVar &tranVar,
                                      const DofVar &rotVar,
                                      const LoadEvaluatorType fx,
                                      const LoadEvaluatorType fy,
                                      const LoadEvaluatorType fz,
                                      const LoadEvaluatorType mx,
                                      const LoadEvaluatorType my,
                                      const LoadEvaluatorType mz,
                                      const ColVector<geoDim> &principalAxisVector = setZero<ColVector<geoDim>>(),
                                      Bool localCoord                              = true)
    requires(hypothesis == StructuralHypothesis::tridimensional);
```

## Parameters

`EulerBeamDistributedLoadFormulation` has the following template parameter:

- `hypothesis` is the **structural hypothesis** (see `StructuralHypothesis`).
  The value of `hypothesis` dictates which constructor should be called .

- `LoadEvaluatorType` is the expected **type of the loads** (e.g. `Real`) ;

`EulerBeamDistributedLoadFormulation` has the following parameters:

- `tranVar`, is the `DofVar` of the `NodeField` defined over
  `meshSet` that represents the translation DOFs;
- `rotVar`, is the `DofVar` of the `NodeField` defined over
  `meshSet` that represents the rotation DOFs;

- `meshSet` is the **mesh set** over which the formulation is to be applied ;
- `principalAxisVector` is the **orientation vector**, which defines the
  **principal axis** of the cross section (usually named **OY**);

- `fx` is the distributed load along the \(x\) axis ;
- `fy` is the distributed load along the \(y\) axis ;
- `fz` is the distributed load along the \(z\) axis ;
- `mx` is the distributed moment around the \(x\) axis ;
- `my` is the distributed moment around the \(y\) axis ;
- `mz` is the distributed moment around the \(z\) axis ;
- `localCoord` is a boolean that should be set to `true` if the
  the loads are given in the **local coordinate system**, and set to
  `false` if they are given in the **global coordinate system**.

## List of commented examples and verification tests

- [Euler and Timoshenko beams verification tests - Cantilever beam with distributed external forces](../../../../../verification_tests/manta_components_verification_tests/solid_mechanics/fem_implicit_linear/beams/cantilever_distributed.md#cantilever-distributed-beam-verification-tests)
- [Euler beams verification tests - Explicit resolution of a cantilever beam under distributed force](../../../../../verification_tests/manta_components_verification_tests/solid_mechanics/fem_explicit_linear/beams/clamped_free.md#cantilever-endforce-beam-verification-tests-explicit)

## Description

This formulation implements **external distributed forces vector** for the Euler
beam formulation. Theoretical details are given in the
[theory manual](../../../../../theory_manual/solid_mechanics/beams/beam_theory.md#theory-beam-external-distributed-forces).

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
