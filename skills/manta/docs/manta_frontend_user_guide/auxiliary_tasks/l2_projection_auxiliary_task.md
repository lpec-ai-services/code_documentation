<!-- source: https://manta-project.gitlab.io/manta/manta_frontend_user_guide/auxiliary_tasks/l2_projection_auxiliary_task.html -->

# The L2Projection auxiliary task

The `L2ProjectionAuxiliaryTask` auxiliary task allows to compute a
field resulting from the projection of values at integration points to
nodes. Optionally, a regularization is performed.

## Examples of usage

- projection of a scalar field:

  ```python
  mm = manta.Model('L2ProjectionAuxiliaryTask', ps,
                   value = 'ip_values',
                   result = 'node_values',
                   domain = 'cube',
                   quadratureOrder = 2)
  ```
- projection of a multi-component field with regularization:

  ```python
  p = manta.Model('L2ProjectionAuxiliaryTask', ps,
                  value = 'Stress',
                  result = 'NodalStress',
                  domain = 'material',
                  numberOfRows = 4,
                  characteristicLength = 1e-3)
  ```

## Main parameters

The main parameters used to initialize the brick are:

- `domain` (which must be a string) or `domains` (which
  must be an array of strings). Each of those strings are interpreted as
  regular expressions.

  - `material` and `boundary` are equivalent to
    `domain`.
  - `materials` and `boundaries` are equivalent to
    `domains`
- `value` (which must be a string), which indicates the name
  of the values at integration points projected.
- `result` (which must be a string), which indicates
  the name of the projected field.
- `numberOfRows` (which must be a positive integer). This
  parameter is *optional* and allows to specify the number of rows of
  the projected values. This parameters defaults to 1.
- `numberOfColumns` (which must be a positive integer). This
  parameter is *optional* and allows to specify the number of columns of
  the projected values. This parameters defaults to 1.
- `quadratureOrder` (which must be a positive integer). This
  parameter is *optional* and allows to select the quadrature order.
- `characteristicLength` (which must be a positive value or a string). This
  parameter is *optional* and allows to specify a regularisation length.

Note

If the parameter `quadratureOrder` is not specified, manta
will try to find a suitable provider for the values. Those
values must then be uniquely defined for this mechanism to work.
This is typically the case when treating values computed by
another model. However, loadings or material properties
can generally be computed on arbitrary quadratures, so
this mechanism would fail in those cases.

## Description

Without regularization, this auxiliary task implements an \(L_{2}\)
projection of a field at integration points by minimizing the following
functional:

\[\int_{\Omega} \left|U-v\right|^{2}\,\mathrm{d}\,V\]

where:

- \(\Omega\) is the domain on which the projection is done,
- \(U\) is the unknown function defined by the finite element approximation,
- \(v\) is a field which is only known at integration points.

With regularization, this auxiliary task minimizes the following functional:

\[\int_{\Omega} \left|U-v\right|^{2}+l^{2}\left|\nabla U\right|^{2}\,\mathrm{d}\,V\]

where \(l\) is a characteristic length.

Note

This auxiliary task is based on the `L2ProjectionFormulation` formulation
described in Section [Projection of integration point values at nodes](../../manta_components_user_guide/formulations/utilities/finite_elements/l2_projection_formulation.md#l2-projection-formulation) without regularization
and on the `RegularizedL2ProjectionFormulation` formulation
described in Section [Regularized_projection of integration point values at nodes](../../manta_components_user_guide/formulations/utilities/finite_elements/regularized_l2_projection_formulation.md#regularized-l2-projection-formulation) otherwise.
