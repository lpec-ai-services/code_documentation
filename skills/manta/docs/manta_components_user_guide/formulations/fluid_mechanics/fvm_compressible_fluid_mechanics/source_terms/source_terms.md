<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/formulations/fluid_mechanics/fvm_compressible_fluid_mechanics/source_terms/source_terms.html -->

# Source terms

In the context of the Finite Volume method, a source term represents the effects of
phenomena that are not captured by the main conservation laws.
It is a vector \(S\) that is added to the right-hand side of the system of equations,
modifying the rate of change of the conservative variables \(U\).

For a system of conservation laws of the form:

\[\frac{\partial U}{\partial t} + \nabla \cdot \mathbf{F}(U) = 0\]

a source term S(U) is added as follows:

\[\frac{\partial U}{\partial t} + \nabla \cdot \mathbf{F}(U) = S(U)\]

Available source terms in MANTA are:

- Gravity
- Energy Injection (only with `EPXTabulatedWaterEOS`)
- Regular head loss

Note

For implicit time integration, a source term may optionally provide the
analytical Jacobian \(\partial S / \partial U\) by overriding
`computeJacobian`. If not overridden, the Jacobian defaults to
zero, corresponding to an explicit treatment of the source term.

Note

Source terms can be applied either to the whole computational domain or
restricted to a specific region. When registering a source term via
`createSourceTerm`, an optional `MeshSet` can be provided; if
omitted, the source term is applied to the default cells of the
formulation.

Note

To implement a new source term, derive from `SourceTerm`, implement
`getLabel()` and `computeRate()`, and optionally
`computeJacobian()`. The new term can then be registered on a
formulation via `createSourceTerm<MyTerm>(cells, args...)`.

Contents

- [Gravity source term](gravity.md)
- [Energy injection source term](energy_injection.md)
- [Regular headloss source term](regular_headloss.md)
