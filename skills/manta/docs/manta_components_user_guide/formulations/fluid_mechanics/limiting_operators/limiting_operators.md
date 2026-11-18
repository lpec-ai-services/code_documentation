<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/formulations/fluid_mechanics/limiting_operators/limiting_operators.html -->

# Limiting Operators

The fluid mechanics formulations use on reconstruction operators that rely on limiting
operators. Those reconstruction operators are used to reconstruct a cell field
at the integration points of the facets of each element, the limiting operators main use being
the limitation of the gradient inside each cell, in order to ensure the stability of the scheme.

The following section lists all the limiting operators that are implemented in
MANTA. More detail on the theory behind each of them is given in the theory
manual (see [Reconstruction operators and limiters](../../../../theory_manual/fluid_mechanics/compressible_fluid_mechanics.md#euler-reconstruction-and-limiters)).

As of now, the user is not expected to instantiate a limiting operator, as those
objects are constructed as the formulations are constructed themselves.

## `DummyLimitingOperator`

The `DummyLimitingOperator` does **not** limit the gradient inside the cell.

There is no specific parameter that is tied to this limiter.

## `BarthJespersenLimitingOperator`

The `BarthJespersenLimitingOperator` is described in the following section
of the theory manual: [BarthJespersen limiter](../../../../theory_manual/fluid_mechanics/compressible_fluid_mechanics.md#euler-limiter-barth-jespersen).

There is no specific parameter that is tied to this limiter.

## `DuboisLimitingOperator`

The `DuboisLimitingOperator` is described in the following section
of the theory manual: [Dubois limiter](../../../../theory_manual/fluid_mechanics/compressible_fluid_mechanics.md#euler-limiter-dubois).

This limiter requires a parameter \(K \in [0, 1]\). Its role is fully defined
in the theory manual. \(K = 0\) corresponds to a first order scheme.
\(K = 0.75\) is often used.

## The `LimitingArguments` struct

The `LimitingArguments` struct encapsulates all the generic parameters that
can be used to instantiate any of the limiting operators. Most of the fluid
mechanics formulations rely on this struct in order to internally instantiate
a limiting operator. Each argument has a default value, and each limiting operator
only reads the value that is used for its instantiation such as irrelevant
parameters can be ignored (both by the code and the user).

The current definition of `LimitingArguments` is given hereunder.

```c++
/**
 * @brief Encapsulates all the arguments that are needed to construct a
 * limiting operator
 */
struct LimitingArguments {
  /** @brief Dubois parameter */
  Real k = 0.75;
};
```
