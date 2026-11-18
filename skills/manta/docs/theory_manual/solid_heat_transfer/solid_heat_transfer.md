<!-- source: https://manta-project.gitlab.io/manta/theory_manual/solid_heat_transfer/solid_heat_transfer.html -->

# Heat transfer in solids

The physical model mathematically describes, for an arbitrary material,
the relationship between transient enthalpy storage, heat flow due to
conduction and heat generation/removal due to a volume source.
The thermal formulations in MANTA are named

- *CapacityFormulation*
- *ConductionFormulation*
- *ThermalSourceFormulation*
- *HeatFluxFormulation*
- *ConvectionFormulation*

Their details in the documentation are yet to be described.

## Balance equations

The partial differential equation that models transient heat transfer in
quasi-rigid volumes is the following:

(236)\[ \rho c_p \frac{\partial T}{\partial t} = - \nabla \cdot \v{j} + s(\v{x},t) \quad \forall \v{x} \in \Omega\]

where the thermophysical properties may depend on space and/or time:

\[\rho = \rho(\v{x},t)\]

\[c_p = c_p(\v{x},t).\]

where \(\rho(\v{x},t)\) and \(c_p(\v{x},t)\) are arbitrary and explicit
functions of space and time. For mathematical closure, equation
[(236)](#equation-manta-theory-manual-heat-transfer-volume-heat-equation)
requires both boundary and initial conditions.

### Boundary conditions

The boundary conditions (B.C.) currently implemented in MANTA are of the
imposed temperature type (Dirichlet B.C.), the imposed thermal flux
(Neumann B.C) and convection boundary conditions (Robin B.C.). The boundary conditions
can be both spatially and temporally variable. They are defined in the
following:

1. Imposed temperature on Dirichlet Boundary \(\partial \Omega_{D}\)

(237)\[ T_{\partial \Omega_{D}} = T_{imposed} (\v{x}_{\partial \Omega_{D}},t)\]

2. Variable Flux on Neumann Boundary \(\partial \Omega_{N}\)

(238)\[ \v{j} \cdot \v{n} = q(\v{x}_{\partial \Omega_{N}},t)\]

where \(q\) represents the heat flux normal to the boundary \(\partial \Omega_{N}\).

3. Convection Flux on Robin Boundary \(\partial \Omega_{R}\)

(239)\[ \v{j}\cdot \v{n} = h_{conv}(\v{x}_{\partial \Omega_{R}},t) (T(\v{x}_{\partial \Omega_{R}},t) - T_{\infty})\]

### Initial conditions

The initial conditions have to be user defined and can be functions of
space and time:

\[T(\v{x}, t=0) = T_0(\v{x})\]

where \(T_0\) is an arbitrary function of space.

Note

The choice of initial conditions for strongly
diffusive parabolic differential conditions is generally not strict.
However, initial conditions are recommended to be consistent with the
imposed boundary conditions.

## Finite Element discretization

The partial differential equation used to describe the heat transfer
model is approximated in MANTA by the use of the Galerkin Finite Element
Method on the spatial differential terms. This approximation
begins first by the description of the weak form of equation
[(236)](#equation-manta-theory-manual-heat-transfer-volume-heat-equation), written
as follows:

\[0 = {R}_{T_{\Omega_r}} = \int_{\Omega} \rho c_p \frac{\partial T}{\partial t} N^\text{T} dV - \int_{\Omega} s(\v{x}, t) N^\text{T} dV - \int_{\Omega} \v{j} \cdot (\nabla N)^\text{T} \; dV + \int_{\partial \Omega} \v{j} N^\text{T} \cdot \v{n} \; dS\]

where \(N^\text{T}\) is a test function and
\({R}_{T_{\Omega_r}}\) is the thermal residual associated to the
weak formulation defined on the reference configuration
\({\Omega_r}\). Furthermore, the boundary domain can be currently
defined as the union of the different types of boundaries as defined in
equations
[(237)](#equation-manta-theory-manual-heat-transfer-imposed-temperature),
[(238)](#equation-manta-theory-manual-heat-transfer-imposed-flux),
[(239)](#equation-manta-theory-manual-heat-transfer-imposed-convection) along
\(\partial \Omega = \partial \Omega_D \cup \partial \Omega_N \cup
\partial \Omega_R\). Next, the above variational equation is combined with
the B.C equations
[(238)](#equation-manta-theory-manual-heat-transfer-imposed-flux) and
[(239)](#equation-manta-theory-manual-heat-transfer-imposed-convection) to
yield the following:

\[\begin{split}0 = {R}_{T_{\Omega_r}} &= \int_{\Omega} \rho c_p \frac{\partial T}{\partial t} N^\text{T} dV - \int_{\Omega} s(\v{x}, t) N^\text{T} dV - \int_{\Omega} \v{j} \cdot (\nabla N)^\text{T} \; dV + \int_{\partial \Omega_N} \v{j}\cdot \v{n} N^\text{T} \; dS \\
&- \int_{\partial \Omega_R} h_{conv} (T - T_{\infty}) N^\text{T} \; dR\end{split}\]

as for the inclusion of the imposed temperature boundary condition into
the above weak form, equation
[(237)](#equation-manta-theory-manual-heat-transfer-imposed-temperature) is
considered as a mathematical constraint. This requires the addition of a
Lagrange multiplier \(\beta_T\) to the above equation, which adds
equation equation
[(237)](#equation-manta-theory-manual-heat-transfer-imposed-temperature) as a
constraint and transforms the above weak form to the following:

(240)\[\begin{split}0 = {R}_{T_{\Omega_r}} &= \int_{\Omega} \rho c_p \frac{\partial T}{\partial t} N^\text{T} dV - \int_{\Omega} s(\v{x}, t) N^\text{T} dV - \int_{\Omega} \v{j} \cdot (\nabla N)^\text{T} \; dV + \int_{\partial \Omega_N} \v{j}\cdot \v{n} N^\text{T} \; dS \\
&- \int_{\partial \Omega_R} h_{conv} (T - T_{\infty}) N^\text{T} \; dR - \int_{\partial \Omega_D} \beta_T \; \delta(\v{x} - \v{x}_{\partial \Omega_D}) \; dS\end{split}\]

\[\int_{\partial \Omega_D} T \; \delta(\v{x} - \v{x}_{\partial \Omega_D}) \; dS = T_{imposed}\]

where the equation \(\delta(\v{x} -
\v{x}_{\partial \Omega_D})\) is the Dirac Delta operator that
selects all spatial points along the \(\partial \Omega_D\)
subdomain. The weak form described in equation
[(240)](#equation-manta-theory-manual-heat-transfer-weak-form-full) is now
ready for discretization. This is performed by discretizing the unknown
\(T_{\Omega}\) along the entire mesh which is defined by the nodes
\(i = [1, M_{e}]\) (with \(M_e\) the total number of nodes),
which results in the discretized unknown \(T_{i}\). The vector of
discretized unknowns can now be represented by \(\{T\} N =
\sum_{i=1}^{M_e} T_i N_i\) where \(N = \sum_{i=1}^{M_e} N_i\) is the
interpolation function and is the transpose of the test function
\(N^\text{T} = \sum_{j=1}^{M_e} N_j\). We can now separate the
vector \(\{ T \}\) from the interpolation function and rewrite
equation [(240)](#equation-manta-theory-manual-heat-transfer-weak-form-full)
as:

\[\begin{split}0 = \{R\}_{T_{\Omega_r}} &= \{\frac{\partial T}{\partial t}\} \int_{\Omega} \rho c_p N N^\text{T} dV - \int_{\Omega} s(\v{x}, t) N^\text{T} dV - \{T\} \int_{\Omega} \v{j} \cdot (\nabla N)^\text{T} \; dV + \int_{\partial \Omega_N} \v{j}\cdot \v{n} N^\text{T} \; dS \\
&- \{T\} \int_{\partial \Omega_R} h_{conv} N N^\text{T} \; dR + \int_{\partial \Omega_R} h_{conv} T_{\infty} N^\text{T} \; dR - \int_{\partial \Omega_D} \beta_T \; \delta(\v{x} - \v{x}_{\partial \Omega_D}) \; dS\end{split}\]

with the constraint still appended to it

\[\{ T \} \int_{\partial \Omega_D} \; \delta(\v{x} - \v{x}_{\partial \Omega_D}) \; dS = T_{imposed}\]
