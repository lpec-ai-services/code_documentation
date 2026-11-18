<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/formulations/fluid_mechanics/fvm_compressible_fluid_mechanics/source_terms/gravity.html -->

# Gravity source term

For some problems, such as Rayleigh-Taylor instabilities or water hammer
effects in pipes with a height difference, gravity effects cannot be
neglected. When gravity is taken into account, the compressible Euler equations
[(241)](../../../../../theory_manual/fluid_mechanics/compressible_fluid_mechanics.md#equation-euler-eq) become (see [[Tor09](../../../../../references/references.md#id38)]):

\[\begin{split}\begin{aligned}
\frac{\partial \rho}{\partial t}
+ \nabla \cdot (\rho \mathbf{u})
&= 0, \\
\frac{\partial (\rho \mathbf{u})}{\partial t}
+ \nabla \cdot
\left(
\rho \mathbf{u} \otimes \mathbf{u} + p\mathbf{I}
\right)
&= \rho \mathbf{g}, \\
\frac{\partial (\rho E)}{\partial t}
+ \nabla \cdot
\left(
(\rho E + p)\mathbf{u}
\right)
&= \rho \mathbf{u} \cdot \mathbf{g}.
\end{aligned}\end{split}\]

Here, \(\mathbf{g}\) is the gravitational acceleration vector.

Because the source terms cannot be written in divergence form, the problem is
solved using a splitting method. At each time step, the problem is first solved
without the gravity terms. This corresponds to the classical problem
[(241)](../../../../../theory_manual/fluid_mechanics/compressible_fluid_mechanics.md#equation-euler-eq) and yields an intermediate conservative state
\(\mathbf{U}_{n+1}^{\star}\). Gravity is then taken into account by updating
the conservative variables associated with the momentum and energy equations:

\[\begin{split}\begin{aligned}
(\rho \mathbf{u})_{n+1}
&= (\rho \mathbf{u})_{n+1}^{\star}
+ \Delta t\,\rho_{n+1}^{\star}\mathbf{g}, \\
(\rho E)_{n+1}
&= (\rho E)_{n+1}^{\star}
+ \Delta t\,\rho_{n+1}^{\star}
\mathbf{u}_{n+1}^{\star} \cdot \mathbf{g}.
\end{aligned}\end{split}\]

For formulations which dimension is lesser than the mesh dimension, such as
one-dimensional pipes oriented in space, the projection of
\(\mathbf{g}\) onto the formulation is used instead of the full vector
\(\mathbf{g}\).

The method `addGravity` is compatible with every Euler explicit formulation.

## Example of usage:

Here is an example to add a gravity source term to an Euler formulation

```c++
    using Form     = EulerExplicitFormulation<SingleFluidModel<2, 0, decltype(eos), HLLCRiemannSolver<geoDim, decltype(eos)>>>;
    auto &fluxForm = rm.make<Form>(tube, eos, U, Uvar, W);
```

```c++
    // ----------- Add gravity source term --------------
    const Real gy = -9.81;
    // define gravity direction
    ColVector<geoDim> g = {0, gy};
    fluxForm.addGravity(ctx, g);
```

Note

Each `addGravity` has an overload taking an additional
`MeshSet` argument, to restrict the gravity source term to a subset
of cells instead of applying it to the whole formulation's domain.

Note

The way gravity is specified depends on the formulation:

- Generic Euler formulations (`EulerFluxFormulation::addGravity`)
  take a local gravity vector of size `geoDim`, used as-is.
- One-dimensional pipe formulations (`EulerExplicitPipeFormulation`,
  `EulerImplicitPipeFormulation`) instead take a global 3D gravity
  vector: it is automatically projected onto the pipe axis at each cell.

Note

Each `addGravity` has an overload taking an additional
`MeshSet` argument, to restrict the gravity source term to a subset
of cells instead of applying it to the whole formulation's domain.

Note

Implicit Euler formulations, such as `EulerImplicitPipeFormulation`,
are not yet compatible with `addGravity`: `GravityTerm` does
not currently implement `computeJacobian`, which is required for
implicit time integration.
