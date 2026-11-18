<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/formulations/fluid_mechanics/fvm_compressible_fluid_mechanics/source_terms/regular_headloss.html -->

# Regular headloss source term

For some problems, such as pipe flows, regular headloss effects cannot be neglected. When
head loss is taken into account, the compressible Euler equations
[(241)](../../../../../theory_manual/fluid_mechanics/compressible_fluid_mechanics.md#equation-euler-eq) become:

\[\begin{split}\begin{aligned}
\frac{\partial \rho}{\partial t}
+ \nabla \cdot (\rho \mathbf{u})
&= 0, \\
\frac{\partial (\rho \mathbf{u})}{\partial t}
+ \nabla \cdot
\left(
\rho \mathbf{u} \otimes \mathbf{u} + p\mathbf{I}
\right)
&= -\frac{\rho}{2} K
\lVert \mathbf{u} \rVert \mathbf{u}, \\
\frac{\partial (\rho E)}{\partial t}
+ \nabla \cdot
\left(
(\rho E + p)\mathbf{u}
\right)
&= -\frac{\rho}{2} K
\lVert \mathbf{u} \rVert
\mathbf{u} \cdot \mathbf{u}.
\end{aligned}\end{split}\]

Here, \(K\) is the headloss coefficient. It may for instance be computed as
\(K = f_D / D_h\) (\(K\) has units of \(\text{m}^{-1}\)), where \(f_D\)
is the Darcy friction factor and \(D_h\) is the hydraulic diameter, but
any user-supplied coefficient is accepted. The source term is always dissipative:
it acts opposite to the flow direction.

Because the source terms cannot be written in divergence form, the problem is
solved using a splitting method. At each time step, the problem is first solved
without the head-loss terms. This corresponds to the classical problem
[(241)](../../../../../theory_manual/fluid_mechanics/compressible_fluid_mechanics.md#equation-euler-eq) and yields an intermediate conservative state
\(\mathbf{U}_{n+1}^{\star}\). The head loss is then taken into account by
updating the conservative variables associated with the momentum and energy
equations:

\[\begin{split}\begin{aligned}
(\rho \mathbf{u})_{n+1}
&= (\rho \mathbf{u})_{n+1}^{\star}
- \Delta t\,
\frac{\rho_{n+1}^{\star}}{2}
K
\lVert \mathbf{u}_{n+1}^{\star} \rVert
\mathbf{u}_{n+1}^{\star}, \\
(\rho E)_{n+1}
&= (\rho E)_{n+1}^{\star}
- \Delta t\,
\frac{\rho_{n+1}^{\star}}{2}
K
\lVert \mathbf{u}_{n+1}^{\star} \rVert
\mathbf{u}_{n+1}^{\star}
\cdot \mathbf{u}_{n+1}^{\star}.
\end{aligned}\end{split}\]

## Example of usage:

Here is an example to add a head loss source term to an Euler formulation

```c++
    using FluidModel = HEMFluidModel<geoDim>;
    using Form       = EulerExplicitPipeFormulation<FluidModel>;
    auto &fluxForm   = rm.make<Form>(tube, eos, U, Uvar, W, zIn, areaFunction);
```

```c++
    for (size_t i = 0; i < headlossCoefs.size(); ++i) {
      fluxForm.addHeadloss(ctx, headlossCoefs[i], pipeSegmentMeshSets[i]);
    }
```

The method `addHeadLoss` is compatible with every Euler explicit formulation.

Note

Each `addHeadLoss` has an overload taking an additional
`MeshSet` argument, to restrict the regular headloss source term to a subset
of cells instead of applying it to the whole formulation's domain.

Note

Implicit Euler formulations, such as `EulerImplicitPipeFormulation`,
are not yet compatible with `addHeadLoss`: `HeadlossTerm` does
not currently implement `computeJacobian`, which is required for
implicit time integration.
