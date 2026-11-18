<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/formulations/utilities/finite_elements/regularized_l2_projection_formulation.html -->

# Regularized_projection of integration point values at nodes

## Example of usage

```c++
using IPEvaluatorType = FieldRef<IPField<>>;
constexpr auto h = GeometricHypothesis::inPlane;
constexpr auto sid = ShapeId::qua4;
auto &formulation = rm.make<RegularizedL2ProjectionFormulation<h, sid, IPEvaluatorType>>(
      ms, qid, Uvar, ipField, clength);
```

where:

- `Uvar` is the dof variable of the *NodeField* containing the projected values,
- `ipfield` is the *IPField* that will be projected,
- `ms` is the *meshset* on which the projection is made,
- `qid` is the quadrature on which the integration point values are known.
- `clength` is a characteristic length. By default, this length is a
  scalar, but the user may specify an arbitrary scalar evaluator.

## Description

This formulation implements an \(L_{2}\) projection of a field at
integration points by minimizing the following functional:

\[\int_{\Omega} \left|U-v\right|^{2}+l^{2}\,\left|\nabla\,U\right|^{2}\,\mathrm{d}\,V\]

where:

- \(\Omega\) is the domain on which the projection is done,
- \(U\) is the unknown function defined by the finite element approximation,
- \(v\) is a field which is only known at integration points,
- \(l\) is the characteristic length.

## Template Parameters

`RegularizedL2ProjectionFormulation` has four template parameters:

- the geometric hypothesis,
- the shape id,
- the type of the evaluator of the values at integration points.
- the type of the evaluator of the characteristic length integration points.
  This parameter defaults to `const Real`.
