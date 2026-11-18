<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/algorithms_and_numerics/gtheta_method_2D.html -->

# GTheta Numerical Method 2D

## Description

This page describes the `GTheta2D` class, which enables the numerical computation
of the energy release rate \(G\) in the context of 2D linear elastic fracture mechanics.

The method is based on the **Destuynder formulation** cite{Destuynder1981} of the G-theta method, which
relies on a domain integral involving the stress, displacement, and a user-defined
perturbation field \(\Theta\).

The integral is written as:

\[G = \int_\Omega \mathrm{tr}\left( \sigma \cdot \nabla u \cdot \nabla \Theta \right) d\Omega
- \frac{1}{2} \int_\Omega \mathrm{tr}\left( \sigma \cdot \nabla u \right) \, \mathrm{div}(\Theta) \, d\Omega\]

The computation uses:
- the displacement field \(u\)
- the stress field \(\sigma\)
- a user-defined \(\Theta\) field

Note that, at the moment users must instantiate their own \(\Theta\) perturbation field.

## Class Definition

The class is templated by:

- `shapeId` : shape function
- `quadId` : quadrature rule

### Constructor

> ```c++
>     GTheta2D GthetaMethod = GTheta2D<ShapeId::qua4, QuadId::qua4>(cells, U, Theta, cauchy);
> ```

Inputs parameters:

- `meshSet` : the `MeshSet` support of the class.
- `U` : the `NodeField` of the displacement field.
- `Theta` : the \(\Theta\) field used to compute G passed as a `NodeField`
- `sigma` : the `IPField` of the stress field.

## Theta Field Definition

The \(\Theta\) field is defined by the user as a `NodeField`. It is representative of a perturbation of the crack front.
It is therefore defined as a vector field of the same dimension as the problem at hand.

To understand how the field should be defined for this numerical method you can look at [[CR18](../../references/references.md#id88)] .
Furtermore note that example of the creation of such fields are available in the [fracture mechanics tests](../../verification_tests/manta_components_verification_tests/manta_components_verification_tests.md#manta-components-verification-tests).,
and a [commented example](../../demos/components_examples/fracture_mechanics/gtheta_example.md#g-theta-example).

In 2D, it is usually built following the following principles:

- centered around the crack tip
- constant inside a radius \(a\)
- smoothly decreasing between \(a\) and \(b\)
- zero outside radius \(b\)
- oriented along the crack propagation direction

## Typical usage of the class

This class is used as a post-processing tool. Therefore, a typical cpp calling it usually goes like:

1. Instanciate a displacement field `U` , and a stress field `sigma`
2. Instanciate a \(\Theta\) field (user-defined)
3. Instantiate a `GTheta2D` class
4. Initialize ressource manager `rm.init`
5. Solve an elasticity problem to obtain `U` and \(\sigma\)
6. Call `computeGTheta2D()` to evaluate \(G\)

Here is how to call `computeGTheta2D()`, that returns the energy release rate in a `Real`:

```c++
    gtheta = GthetaMethod.computeGTheta2D(ctx);
```

## Notes

- The \(\Theta\) field must be filled **after** `rm.init()`
- The stress field must be computed before calling the `GTheta2D` class
- The current implementation can only be used in the context of isothermal small strain, with an elastic formulation
