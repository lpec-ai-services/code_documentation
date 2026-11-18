<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/formulations/fluid_mechanics/reconstruction_operators/reconstruction_operators.html -->

# Reconstruction Operators

The fluid mechanics formulations rely on reconstruction operators to extrapolate
cell-centered field values to the integration points located on element facets.
In higher-order schemes, they rely on limiting operators (see [Limiting Operators](../limiting_operators/limiting_operators.md#fvm-limiting-operators))
to evaluate cell gradients.

More theoretical details about reconstruction schemes and limiters are provided in the theory
manual (see [Reconstruction operators and limiters](../../../../theory_manual/fluid_mechanics/compressible_fluid_mechanics.md#euler-reconstruction-and-limiters)).

## `PieceWiseConstantReconstructionOperator`

The `PieceWiseConstantReconstructionOperator` implements a piecewise constant
(first-order) reconstruction. The value evaluated at any integration point of a
cell facet is simply equal to the cell-centered value, and the gradient is identically zero.

### Example of usage

```c++
  using RecoOp = PieceWiseConstantReconstructionOperator<geoDim, nVar>;
```

### Parameters

`PieceWiseConstantReconstructionOperator` has the following template parameters:

- `geoDim`

  - Number of spatial dimensions
  - Type: `Int`
  - Default value: None
  - Available options:

    - 1
    - 2
    - 3
- `nVar`

  - Number of variables of the fields
  - Type: `Int`
  - Default value: None

## `LeastSquaresLinearReconstructionOperator`

The `LeastSquaresLinearReconstructionOperator` provides a second-order linear spatial
reconstruction using a least squares method. Gradients are computed on each cell
as described in the theory manual (cf. [Reconstruction operators and limiters](../../../../theory_manual/fluid_mechanics/compressible_fluid_mechanics.md#euler-reconstruction-and-limiters)).

### Example of usage

```c++
    using RecoOp = LeastSquaresLinearReconstructionOperator<geoDim, nVar, DuboisLimitingOperator>;
```

### Parameters

`LeastSquaresLinearReconstructionOperator` has the following template parameters:

- `geoDim`

  - Number of spatial dimensions
  - Type: `Int`
  - Default value: None
  - Available options:

    - 1
    - 2
    - 3
- `nVar`

  - Number of variables of the fields
  - Type: `Int`
  - Default value: None
- `LimitingOperatorType`

  - Type of the limiting operator
  - Default value: None
  - Available options: see [Limiting Operators](../limiting_operators/limiting_operators.md#fvm-limiting-operators)
