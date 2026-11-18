<!-- source: https://manta-project.gitlab.io/manta/theory_manual/fluid_mechanics/compressible_fluid_mechanics.html -->

# Compressible inviscid fluid mechanics

Transient inviscid compressible flows are especially used to handle shock waves
and explosions. Fluid mechanic applications in MANTA mainly cover compressible
flows. MANTA is able to simulate both fast transient computations for
accidental conditions using explicit time schemes, and nominal quasi-steady
states with implicit time schemes. In most cases, the flow is considered as
inviscid and is mathematically represented by the Euler conservation equations.
The spatial discretization of the Euler equations is presently implemented
within the Finite Volumes Method. The conservative property of this method
allows for an accurate representation of the velocity and amplitude of shock
waves.

Industrial applications in the scope of MANTA gather many nominal or accidental situations
in nuclear power plants. They also include a broad range of safety-related
applications. Fluid flows are often computed to evaluate the loadings applied on
the structures (pressure waves, vibrations, drag forces,...) and many cases
imply couplings to handle fluid-structure interaction.

As typical applications, we can cite, for example:

- Solid explosions (e.g. TNT) in air or water
- Combustion models for reactive flows (\(H_2\) explosion)
- Pipe modeling (pipe whip, water hammer,...)
- Loss Of Coolant Accident : rarefaction wave propagation after pipe break in
  the primary circuit of a Pressurized Water Reactor
- Tank perforation
- Prompt bursts in Molten Salt Reactors

The main reference for this section is [[Tor09](../../references/references.md#id38)], additional
information about the modeling of compressible flows and about Riemann solvers
can be found in it.

## Compressible Euler equations

Euler equations match the Navier-Stokes equations, considering no viscosity nor
thermal conductivity. They are usually written in conservation form and express
the conservation of mass, momentum and energy in a control volume fixed in space:

(241)\[\begin{split}\frac{\partial \rho}{\partial t} + \nabla \cdot (\rho \mathbf{u}) = 0 \\
\frac{\partial (\rho \mathbf{u})}{\partial t} + \nabla \cdot (\rho \mathbf{u} \otimes \mathbf{u} + p\mathbf{I}) = 0 \\
\frac{\partial (\rho E)}{\partial t} + \nabla \cdot ((\rho E + p)\mathbf{u}) = 0\end{split}\]

where:

- \(\rho\) is the density,
- \(\mathbf{u}\) the velocity vector,
- \(p\) the pressure,
- \(E\) the specific total energy,
- \(\mathbf{I}\) the identity matrix,
- \(\otimes\) denotes the outer product.

We also introduce the specific internal energy \(e\), with

- \(E = e + \frac{u^2}{2}\).

State variables \(\rho\), \(\mathbf{u}\), \(p\), and \(e\) are
the four unknowns of the problem. The system is closed through an equation of
state (EOS) \(f\), an analytical relation between state variables characterizing the
fluid such as \(f(p, \rho, e) = 0\)

In the rest of this documentation, \(\mathbf{U}\) designates the vector of conservative variables
and \(\mathbf{W}\) the vector of primitive variables:

\[ \begin{align}\begin{aligned}\begin{split}\mathbf{U} =
\begin{bmatrix}
\rho \\
\rho \mathbf{u} \\
\rho E
\end{bmatrix}\end{split}\\\begin{split}\mathbf{W} =
\begin{bmatrix}
\rho \\
\mathbf{u} \\
p
\end{bmatrix}\end{split}\end{aligned}\end{align} \]

Each one of them uniquely describes the state of the fluid (combined with the EOS).
\(\mathbf{U}\) constitutes the solution vector of the Euler equations,
whereas \(\mathbf{W}\) regroups natural variables to initialize or
post-process the fluid state.

### Transport of scalar variables

In certain cases, one wants to transport scalar variables that do not interact with the other fluid variables (they are said to be passive).
Let \(z\) be one such passive variable, then \(z\) follows the transport equation:

\[\frac{\partial z}{\partial t} + \mathbf{u} \cdot \nabla z = 0\]

Or, written in a conservative form:

\[\frac{\partial \rho z}{\partial t} + \nabla \cdot (\rho z \mathbf{u}) = 0\]

Thus, numerically, one will solve for \(\rho z\) like any other conservative variable.

## Numerical scheme - Finite Volume method (FVM)

Euler conservation equations can be written in the compact form:

\[\frac{\partial \mathbf{U}}{\partial t} + \nabla \cdot \mathbf{F}(\mathbf{U}) =
0\]

where \(\mathbf{F}(\mathbf{U})\) is the flux vector:

\[\begin{split}\mathbf{F}(\mathbf{U}) =
\begin{bmatrix}
\rho \mathbf{u} \\
\rho \mathbf{u} \otimes \mathbf{u} + p\mathbf{I} \\
(\rho E + p)\mathbf{u}
\end{bmatrix}\end{split}\]

The state is discretized on each cell of the mesh, which constitutes a finite
volume. The state \(\mathbf{U}_i\) on cell \(i\) is the average value on
the volume \(V_i\) : \(\mathbf{U}_i = \frac{1}{V_i}\int_{V_i}
\mathbf{U} \,dV\). State variables are expressed on the barycenter of the cell,
that's why the numerical scheme is called "cell-centered".

Expressing the equations in integral form on the control volume, and using
Gauss' divergence theorem, yields:

\[\frac{\partial}{\partial t} \int_{V_i} \mathbf{U} \,dV + \int_{S_i} \mathbf{F}(\mathbf{U}).\mathbf{n}\,dS = 0\]

with \(S_i\) the boundary of the volume \(V_i\) and \(\mathbf{n}\) its
normal vector. Then, considering the *facets* of each cell:

\[V_i.\frac{\partial \mathbf{U}_i}{\partial t} + \sum_{f \in facets} \mathbf{F}(\mathbf{U}_f).\mathbf{n}_f S_f = 0\]

These equations are solved through Godunov's scheme, a conservative finite
volume method considering Riemann problems at each cell boundary
(*facet*). Solving the Riemann problem provides the flux at each *facet*
based on the state on each side (called left and right):

\[\mathbf{F}(\mathbf{U}_f) = f(\mathbf{U}_L, \mathbf{U}_R)\]

The function \(f\) describes how the Riemann Problem is solved, either through an
Exact Riemann Solver or an approximate one. Left and right state are evaluated
from the state in neighboring cells. The stencil depends on the spatial order of
the scheme.

## Riemann solvers

A Riemann solver defines how the flux on each facet is estimated from data in
adjacent cells. Extensive documentation about Riemann solvers can be found in
[[Tor09](../../references/references.md#id38)]. Provide an exact solution of the Riemann Problem is
possible but is restricted for Perfect Gases and is computationally very costly.
That's why many approximate Riemann solvers have been developed over the years,
with their own advantages and drawbacks.

### The `Exact` Riemann solver

The `Exact` Riemann solver provides the flux on the facet by providing an
exact solution of the Riemann Problem. It finds locally the exact solution of the 1D
compressible Euler equations. The solution depends on the equation of state, and
it is only applicable with the `PerfectGas` EOS. It is recommended for
verification purposes.

### The `HLLC` Riemann solver

The `HLLC` Riemann solver is an extension of the `HLL` Riemann solver
(for Harten, Lax & Van Leer), which considers three constant states, separated by
two acoustic waves \(S_L\) and \(S_R\). \(S_L\) and \(S_R\) are
respectively the smallest and largest wave velocities in the exact solution of
the Riemann problem. In `HLLC`, the intermediary state is split in two
states, separated by a contact discontinuity (C is for "contact") of velocity
\(S^*\). There are various ways to compute extremal velocities \(S_L\)
and \(S_R\). In MANTA we use the estimates proposed by
[[Ein88](../../references/references.md#id40)].

\[ \begin{align}\begin{aligned}S_L = u_{Roe} - ĉ \mid S_R = u_{Roe} + ĉ\\ĉ^2 = c_{Roe} + \frac{1}{2} \frac{\sqrt{\rho_L} \sqrt{\rho_R}}{(\sqrt{\rho_L} + \sqrt{\rho_R})^2} (u_R - u_L)^2\end{aligned}\end{align} \]

With \(a_{Roe}\) the Roe average :

\[a_{Roe} = \frac{\sqrt{\rho_L} a_L + \sqrt{\rho_R} a_R }{\sqrt{\rho_L} + \sqrt{\rho_R} }\]

- \(\rho_{L/R}\) the left/right density
- \(u_{L/R}\) the left/right velocity
- \(c_{L/R}\) the left/right sound speed

The `HLLC` Riemann solver preserves contact discontinuities, guarantees the
entropy condition, and is independant of the equation of state. It is largely
used for problems involving shocks, and offers in most cases a good compromise
between precision, stability and performance.

## Reconstruction operators and limiters

The `ReconstructionOperator` specifies how the state variables are
spatially discretized on the cell volume. It then provides how the values at
facets can be obtained from field values at cell centers. The spatial order is
directly related to the reconstruction. At higher order, limiters are needed to
ensure the scheme still verifies the Total Variation Diminishing (TVD)
condition, i.e. it preserves monotonicity in space.

### `PieceWiseConstant` reconstruction operator

The `PieceWiseConstant` reconstruction operator indicates that
\(\mathbf{U}\) (and \(\mathbf{W}\)) are constant over the cell, such
than the facet value equals the cell value. This is first-order accurate. No
limiter is associated with this scheme, it is essentially TVD.

### `Linear` reconstruction operator

The `Linear` reconstruction operator indicates that
\(\mathbf{U}\) (and \(\mathbf{W}\)) are linear over the cell.

\[\mathbf{U}(\mathbf{x}) = \mathbf{U}_i + \nabla \mathbf{U} \cdot (\mathbf{x} - \mathbf{x}_i)\]

With \(\mathbf{x}_i\) the position of the center of cell \(i\). The
gradient \(\nabla \mathbf{U}\) is constant over the cell. This is
second-order accurate.

Two limiters are available to add a ponderation on the gradient when computing
the facet value.

\[\mathbf{U}_f = \mathbf{U}_i + \phi \nabla \mathbf{U}_i \cdot (\mathbf{x}_f - \mathbf{x}_i)\]

With \(\mathbf{x}_f\) the position of the facet barycenter.

### Limiters

This ponderation is needed to ensure that, at each facet,
\(\mathbf{U}_{min} < \mathbf{U}_{L/R} < \mathbf{U}_{max}\). With:

- \(\mathbf{U}_{max} = \max (\mathbf{U}_i, \max \mathbf{U}_{neighbors})\)
- \(\mathbf{U}_{min} = \min (\mathbf{U}_i, \min \mathbf{U}_{neighbors})\)

Neighbor cells are cells sharing a facet with the current cell \(\mathbf{i}\).

#### `BarthJespersen` limiter

The `BarthJespersen` limiter is defined by (see [[BJ89](../../references/references.md#id74)]):

\[\begin{split}\phi = \min_{f}
\begin{cases}
\min \left (1, \frac{\mathbf{U}_{max} - \mathbf{U}_i}{\nabla \mathbf{U}_i \cdot (\mathbf{x}_f - \mathbf{x}_i)}\right) & \text{if} & \nabla \mathbf{U}_i \cdot (\mathbf{x}_f - \mathbf{x}_i) > 0 \\
\min \left (1, \frac{\mathbf{U}_{min} - \mathbf{U}_i}{\nabla \mathbf{U}_i \cdot (\mathbf{x}_f - \mathbf{x}_i)}\right) & \text{if} & \nabla \mathbf{U}_i \cdot (\mathbf{x}_f - \mathbf{x}_i) < 0 \\
1 & \text{if} & \nabla \mathbf{U}_i \cdot (\mathbf{x}_f - \mathbf{x}_i) = 0 \\
\end{cases}\end{split}\]

#### `Dubois` limiter

The `Dubois` limiter is defined by (see [[SG10](../../references/references.md#id75)]):

\[\phi = \min \left (1, K. \displaystyle \frac{\min \left(\mathbf{U}_{max} - \mathbf{U}_i, \mathbf{U}_i - \mathbf{U}_{min}\right)}{\max_f \left(\nabla \mathbf{U}_i \cdot (\mathbf{x}_f - \mathbf{x}_i)\right)}\right)\]

The Dubois limiter depends on a parameter \(K \in [0,1]\). It is more
flexible and also has lower computational cost than the Barth&Jespersen limiter.
\(K = 0\) corresponds to a first order scheme. \(K\) approaching 1 means
the scheme will better capture discontinuities at the cost of lower diffusivity,
and stability. \(K = 0.75\) is often used.

## Time integration

### The CFL condition and the stability factor

Details on the CFL condition are given [here](cfl_stability_factor_estimate.md#cfl-stability-factor-estimate).

`CFLStabilityfactorEstimate`, denoted \(C_e\) in the following, is a user-defined parameter used to compute each time step increment \(\Delta t\) of an explicit FVM *time integrators*, in such way:

\[\begin{equation}
\Delta t = \Delta t_c C_e
\end{equation}\]

where \(\Delta t_c\) is a critical time step, computed internally (see paragraph below).

Except for local time stepping methods (not treated here), \(\Delta t\) is common to the entire domain.

Computed this way, \(\Delta t\) is the maximum possible value ensuring that
the CFL number in each cell is inferior to \(C_e\).

In most cases, the optimal value of \(C_e\) is unknown. It's up
to the end-user to provide an **estimation** of this factor, based on empirical studies.

If \(C_e\) is chosen too high, the CFL condition may not be fulfilled (see [1]), and the numerical time integration may be unstable.
If \(C_e\) is chosen too low, the CFL condition is correctly fulfilled, but the time steps may be unnecessarily small.
Overall, if the time scheme is unstable, lowering this factor may be part of the solution.

\(C_e\) is usually chosen less than or equal to `1` for first-order FVM schemes, and less than or equal to `0.5` for second-order FVM schemes.

### Available time integrators

The `timeIntegrator` parameter specifies the temporal algorithm. For an
explicit scheme, it gives \(\mathbf{U}^{n+1} = f(\mathbf{U}^{n})\). Two time
integrators are available, the `ForwardEuler` for first order computations
and the `MusclHancock` for second order computations.

#### The `ForwardEuler` time integrator

The explicit forward Euler (first order in time and space) scheme gives :

\[\mathbf{U}_i^{n+1} = \mathbf{U}_i^{n} - \frac{\Delta t}{V_i} \sum_{f \in facets} \mathbf{F}(\mathbf{U}_f^n).\mathbf{n}_f S_f\]

#### The `MusclHancock` time integrator

The MUSCL-Hancock (second order in time and space) scheme follows :

- Advance left and right primitive facet states at half time step
  \(\frac{\Delta t}{2}\) using the linear approximation of the jacobian
  matrix \(\mathbf{A} = \frac{\partial \mathbf{F}(\mathbf{W})}{\partial
  \mathbf{W}}\). The Linear Reconstruction operator provides the gradients.

\[\mathbf{W}_{L/R}^{n+1/2} = \mathbf{W}_{L/R}^{n} - \frac{\Delta t}{2} \mathbf{A} \cdot \nabla \mathbf{W}^n\]

- Compute the fluxes \(\mathbf{F}(\mathbf{U}_f^{n+1/2})\) at halt time step with Riemann solvers.
- Compute \(\mathbf{U}_i^{n+1}\) using half time step fluxes:

\[\mathbf{U}_i^{n+1} = \mathbf{U}_i^{n} - \frac{\Delta t}{V_i} \sum_{f \in facets} \mathbf{F}(\mathbf{U}_f^{n+1/2}).\mathbf{n}_f S_f\]
