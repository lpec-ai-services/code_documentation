<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/formulations/constraints_and_bcs/imposed_pressure.html -->

# Imposed pressure

## Example of usage

The following snippet shows how to create a formulation imposing an
uniform (in space) and constant (in time) pressure on a *meshset*
named `yside`:

```c++
auto &pressure =
    rm.make<ImposedPressureFormulation<h, ShapeId::qua4, const Real>>(yside, QuadId::qua4, Uvar, p);
```

where:

- `h` is the geometric hypothesis,
- `Uvar` is the dof variable of the displacement field,
- `p` is a floating-point number giving value of imposed the
  pressure, assumed is thus constant and uniform in this example, as
  expressed by the third template parameter which is `const Real`.

## Parameters

The `ImposedPressureFormulation` has three template parameters:

- the geometric hypothesis,
- the shape identifier,
- the evaluator type for the computation of the imposed pressure at the
  integration points.

The main constructor of the `ImposedPressureFormulation` class has four
parameters:

- the *meshset* on which the pressure is imposed,
- the quadrature identifier,
- the dof variable of the displacement field,
- the pressure evaluator.

This constructor treats the boundary condition exactly. To explicitly select
the infinitesimal perturbation approximation, a second constructor is available.

## Description

Imposing a pressure is associated with the following variational operator:

\[-\int_{\delta\,\Omega_{c}}p\,\var{\v{u}}\,\cdot\,\v{n} \d\,s\]

where:

- \(\delta\,\Omega_{c}\) is the boundary in the current
  configuration on which the pressure is applied,
- \(p\) is the applied pressure (positive in compression, negative
  for a compression),
- \(\var{\v{u}}\) is virtual displacement,
- \(\v{n}\) is the outer normal to \(\delta\,\Omega_{c}\).

Under the infinitesimal pertubation hypothesis, imposing a pressure is
associated with the following variational operator:

\[-\int_{\delta\,\Omega_{r}}p\,\var{\v{u}}\,\cdot\,\v{N} \d\,S\]

where:

- \(\delta\,\Omega_{r}\) is the boundary in the reference
  configuration on which the pressure is applied,
- \(\v{N}\) is the outer normal to \(\delta\,\Omega_{r}\).

## Preconditions

The user is responsible to check the following pre-conditions:

- The *meshset* must only contain elements of the geometric type
  associated with the shape identifier given in the template parameters.
- The quadrature rule must be compatible of the geometric type of the
  entities of the *meshset*.
- The *meshset* must be included in the support of the
  displacement field.
- If the evaluator of the external pressure is a reference or contains
  references to external objects, the user is responible for
  managing the lifetime of the referenced objects: those objects
  must outlives the formulation.

## Notes

The `ImposedPressureFormulation` is the basis of the
`ImposedPressure` brick described in Section
[The ImposedPressure brick](../../../manta_frontend_user_guide/bricks/solid_mechanics/imposed_pressure.md#imposed-pressure-brick).
