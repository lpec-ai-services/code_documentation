<!-- source: https://manta-project.gitlab.io/manta/theory_manual/fluid_mechanics/cfl_stability_factor_estimate.html -->

# The `CFLStabilityfactorEstimate` parameter

This section describes the role of the `CFLStabilityfactorEstimate` parameter.
The first subsection is a short straightforward explanation of its role,
without much details. For more thorough explanations, please read the
remainder of the page.

---

## Short documentation

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

## Introduction

A simulation based on Finite Volume Method (FVM) applied to time dependant
hyperbolic system of PDE consists in the computation of successive solution
fields, representing the solution at successive time stages.

For explicit time integration schemes, such as the Forward Euler scheme, the
time interval between two time stages cannot be set arbitrarily. Notably, the
very important stability condition, called the *CFL condition*, must be fulfilled,
in order for the time integration to remain stable.

First, the concept of CFL number is defined. Secondly, the CFL condition is
described. Then, we explain the definition the time step, based on the
user-defined parameter `CFLStabilityfactorEstimate`. Finally, we mention
some caveat about possible confusion between some of the technical terms
involved.

## Principal notations

Each time stage of the simulation has an associated index \(n\), and an
associated time step \(\Delta t^n\). To alleviate notations, all the
remainder of the document concern an arbitrary time stage \(n\).

The computational spatial domain is a mesh composed of cells. Each cell has an
associated index \(i\). The set of indices of cells is denoted as
\(\mathcal{I}\). All quantities with the subscript \(i\) are associated
with the cell \(i\).

The field of unknowns of the simulation is called \(U\). Each cell \(i\)
has an associated unknown \(U_i\).

## Definition of the CFL number

Each cell of the mesh has an associated Courant-Friedrichs-Lewy number (CFL number) defined as:

\[\forall i \in \mathcal{I}, \quad C_i = \frac {\Delta t S_i}{l_i}\]

where:

- \(S_i\) is an estimation of the maximal signal speed in the cell \(i\). It's a function of the unknown state in the cell : \(S_i = f(U_i)\).
- \(l_i\) is a characteristic length of the cell \(i\). This can be for instance the volume of the cell divided by its surface, or the diameter of the bounding circle of the cell. It gives an estimation of the length a signal must travel to go across the cell in an arbitrary direction.

Note that each cell has an associated CFL number, at a stage of the simulation,
which depends on the cell dimensions and shape, the unknown \(U_i\) and the time
step.

## Description of the CFL condition

Any explicit FVM numerical scheme has an associated stability number
\(\tilde{C}\), associated to the following stability condition (see [[LeV02](../../references/references.md#id37)], section 4.4):

\[\begin{equation}
\forall i \in \mathcal{I}, \quad C_i < \tilde{C}
\end{equation}\]

If this condition is not respected, the time integration scheme diverges. For
instance, for 1D linear advection with forward Euler time scheme,
\(\tilde{C} = 1\).

For most of FVM numerical scheme, it is very important to keep in mind that
\(\tilde{C}\) is unknown. It depends on the space scheme, the time scheme, and the
mesh.

Note that the CFL number and the CFL condition only has a rigorous definition
for 1D linear equations. For multidimensionnal cases with nonlinear hyperbolic
equations, this formula is only an approximate multidimensional extension of the
CFL condition.

## Definition of the critical time step

The critical time step \(\Delta t_c\) is defined as:

\[\begin{equation}
\Delta t_c = \min_{i \in \mathcal{I}}(\frac{l_i}{S_i})
\end{equation}\]

Note that \(\frac{l_i}{S_i}\) is an approximation of the time it takes for a signal to go through the cell \(i\). Hence, \(\Delta t_c\) represents, over the mesh, the minimal time it takes for signals emerging from a cell to go through the cell itself.

This quantity allows to easily set an upper bound on the CFL number of all the cells of the mesh.

## The role of the parameter \(C_e\)

\(C_e\) is the main user-defined parameter of an explicit time scheme.

The time step of an explicit time scheme is computed as:

\[\begin{equation}
\Delta t = \Delta t_c C_e
\end{equation}\]

where \(\Delta t_c\) is a critical time step (see above).

Computed this way, \(\Delta t\) is the maximum possible value ensuring that
the CFL number in each cell is lower than \(C_e\):

\[\begin{equation}
\forall i \in \mathcal{I}, \quad C_i \leq C_e
\end{equation}\]

### Demonstration

The time step is set as:

\[\begin{split}\begin{align}
\Delta t =& C_e \Delta t_c \\ =& C_e \min_{ i \in \mathcal{I} } (\frac{l_i}{S_i})
\end{align}\end{split}\]

and the definition of the CFL number, for an arbitrary cell \(i\) is:

\[\begin{equation}
C_i = \frac{\Delta t S_i}{l_i}
\end{equation}\]

By substituting \(\Delta t\) by its expression above, we get:

\[\begin{split}\begin{align}
C_i &= C_e \min_{i \in \mathcal{I}}(\frac{l_i}{S_i}) \frac{S_i}{l_i} \\
&= C_e \frac{ \min_{i \in \mathcal{I}} (\frac{l_i}{S_i}) } { \frac{l_i}{S_i} }
\end{align}\end{split}\]

by definition,

\[\begin{equation}
\min_{i \in \mathcal{I}} ( \frac{l_i}{S_i} ) \leq \frac{l_i}{S_i}
\end{equation}\]

hence, we demonstrate that, for any cell \(i\):

\[\begin{equation}
C_i \leq C_e
\end{equation}\]

\(\blacksquare\)

### Discussion about the choice of \(C_e\)

The goal is to set \(C_e\) lower than the unknown parameter \(\tilde{C}\) to ensure the CFL
stability condition, but as high as possible to reduce computation time.
Here are the consequences of various scenarios:

- \(C_e << \tilde{C}\), stability is ensured but computation time is unnecessary high
- \(C_e \lesssim \tilde{C}\), stability is ensured, computation time is optimal
- \(C_e = \tilde{C}\), scheme is at its stability limit
- \(C_e > \tilde{C}\), scheme is unstable

As the value of \(\tilde{C}\) is, most of the time, unknown, the value of \(C_e\)
must be set through empirical knowledge and trial and errors procedures. When
the time integration is unstable, lowering \(C_e\) may solve these stability issues.

## The stability time step

The stability time step, denoted as \(\Delta t_s\), is the maximum allowable time step satisfying the CFL condition. Its expression is:

\[\begin{equation}
\Delta t_s = \Delta t_c \tilde{C}
\end{equation}\]

### Demonstration

The CFL condition can be reformulated, by replacing the definition of the CFL number of a cell:

\[\begin{split}\begin{align}
\forall i \in \mathcal{I}, \quad & C_i < \tilde{C} \\
\forall i \in \mathcal{I}, \quad & \frac{\Delta t S_i}{l_i} < \tilde{C}
\end{align}\end{split}\]

which then gives

\[\begin{equation}
\forall i \in \mathcal{I}, \quad \Delta t < \frac{l_i \tilde{C}}{S_i}
\end{equation}\]

As the time step \(\Delta t\) is the same for all the cells of the mesh, this
condition is equivalent to:

\[\begin{split}\begin{align}
\forall i \in \mathcal{I}, \quad \Delta t <& \min_{i \in \mathcal{I}} (\frac{l_i}{S_i}) \tilde{C}\\
& \Delta t_c \tilde{C}\\
\end{align}\end{split}\]

Hence, the maximum allowable time step, denoted \(\Delta t_s\) is:

\[\begin{equation}
\Delta t_s = \Delta t_c \tilde{C}
\end{equation}\]

By construction, if \(\Delta t < \Delta t_s\), the CFL condition is ensured.

\(\blacksquare\)

Note that, as \(\tilde{C}\) remains unknown, \(\Delta t_s\) is unknown too.

### Difference between critical and stability time step

An important point is that \(\Delta t_s\) is not equal to \(\Delta t_c\). If the
scheme has a stability coefficient \(\tilde{C} \approx 1\), then
\(\Delta t_s \approx \Delta t_c\), but it is not often the case.

## References

- [[LeV02](../../references/references.md#id37)]
