<!-- source: https://manta-project.gitlab.io/manta/theory_manual/fluid_mechanics/varying_section_1d.html -->

# Finite Volume Method Quasi-1D for inviscid flow in a varying section pipe

## Introduction

This section presents the numerical modeling of a 1D flow in a pipe with a
varying section. It can be used to model systems such as water flow in pipes
(eg. for a [LOCA](https://en.wikipedia.org/wiki/Loss-of-coolant_accident)
simulation) or for [nozzle flows](https://en.wikipedia.org/wiki/Isentropic_nozzle_flow).

## Disclaimer: purely 1D model

The present implementation of this model in Manta is purely 1D: if the mesh
of a 3D line is given as input, only the first component of each mesh point
is retained. It means that the model implicitly constructs and uses a 1D
projection of the 3D line on the x-axis.

It means that, presently, the implementation of this numerical model cannot handle
3D lines properly. Such feature could be required, for instance, to couple 3D
pipe with 3D volume structures in LOCA simulations.

## Constitutive equation and numerical model for a rigid pipe

Here is the mathematical model for a quasi-1D (i.e. varying section) compressible
flow:

\[\partial_t S u + \partial_x S f = c\]

with:

\[\begin{split}c = \begin{pmatrix} 0 \\ p \frac {dS}{dx} \\ 0 \end{pmatrix}\end{split}\]

- \(S\) is the section
- \(x\) is the Eulerian coordinate on the curve described by all the centers
  of normal sections of the pipe.
- \(u\) is the 1D vector of conservative variables
- \(f\) is the 1D flux of Euler equations
- \(c\) is a source term, arising from the section variation.

It can be derived from the 3D Euler equations, under the following assumptions:

- the flow has an unambiguous single locally dominant characteristic length:
  typically a pipe with small section.
- the section varies smoothly (no edge, no drastic change in section)
- the pipe is rigid. Namely, the pipe's section is fixed over time
- the pipe is straight. If the pipe is curved, the deviation of the fluid should
  cause a reaction on the pipe. This is not captured by this model.

Note

Because of the spatial derivative of the section appearing in the source term
\(c\), the equations are not valid for abrupt section variations. This
spatial derivative arises from a space linearization, which would not hold
relevant in this context.

By integrating over a small length \(\Delta x\), between \(a\) and
\(b\), two points of the surface centers curve (the mean curve of the flow
domain), one gets:

\[\begin{split}\int_a^b S(x) u(x,t) dx = \int_a^b u(x, t) S(x) dx = \int_V u(x,t) dV \\\end{split}\]

hence:

\[\begin{split}\quad \frac 1 V \int_a^b u(x, t) S(x) dx = \frac 1 V \int_V u(x,t) dV \\\end{split}\]

where the volume \(V\) can be defined as:

(242)\[V = \int_a^b S(x) dx = \frac {\Delta x}{3} (S_L + S_R + \sqrt{S_L S_R})\]

This is the formula for the volume of a truncated cone. With a slowly varying
section, the assumption that the section evolves linearly between two close mean
path points is relevant.

Let \(U\) be the mean state of a cell of the 1D mesh (all quantities below
are related to this same cell).

![figure](https://manta-project.gitlab.io/manta/_images/quasi-1d-fvm.svg)

(243)\[\frac {d}{dt} U = \frac 1 V \left( S_L F_L - S_R F_R + C \right)\]

with:

\[\begin{split}C =
\begin{pmatrix}
0 \\
p (S_R - S_L) \\
0
\end{pmatrix}\end{split}\]

\(C\) is obtained from the integral of the source term \(c\) over the
cell length:

\[\begin{split}C = \int_a^b \begin{pmatrix}
0 \\
p \frac {dS}{dx} \\
0
\end{pmatrix}
dx\end{split}\]

### Formulations

Two formulations are available, one for explicit time integration and one for
implicit time integration.

Here is the construction of an explicit formulation.

```c++
    PerfectGasEOS eos(gamma);
    using FluidModel = SingleFluidModel<1, 0, decltype(eos), HLLCRiemannSolver<geoDim, decltype(eos)>>;
    using Form       = EulerExplicitPipeFormulation<FluidModel>;
    auto &fluxForm   = rm.make<Form>(cells, eos, U, Uvar, W, leftBoundary, areaFunction);
```

The variable *areaFunction* designates a lambda which gives \(S(x)\),
the section value depending on the mean path coordinate.

```c++
    // This lambda defines the geometry of the nozzle by defining the area as a function of the distance to pipe extremity
    auto areaFunction = [&L](const RowVector<3> &x) {
      const Real s = norm(x) / L;    // assume mesh lives on the straight-axis, intersecting (0,0), and is of length L.
      Real area;
      if (s < 0.5) {
        area = 1.75 - 0.75 * std::cos((2. * s - 1.) * std::numbers::pi);
      }
      else {
        area = 1.25 - 0.25 * std::cos((2. * s - 1.) * std::numbers::pi);
      }
      return Matrix<1, 1>(area);
    };
```

### Boundary conditions for a compressible flow in a nozzle

Both standard Manta Finite Volume boundary conditions or user implemented
boundary conditions can be used.

For a nozzle flow computation, imposing an inflow condition from a value of
total pressure and total temperature can be convenient.

Warning

The boundary conditions designed for the nozzle flow are only compatible
with a perfect gas assumption. Thus, it must be added to a fomulation which
uses a *PerfectGasEOS* as its template arguments only.

To retrieve temperature from total temperature, for a compressible perfect gas:

\[T = \frac{T_t}{1 + \frac{(\gamma - 1)}{2} M^2}\]

where \(T_t\) is the total temperature, and \(T\) is the static (i.e.
standard) temperature.

In the same fashion, one can compute static pressure from total pressure:

\[p = p_t \left(
1 +
{ \left( \frac{(\gamma - 1)}{2} M^2 \right) } ^ { -\frac{\gamma}{\gamma - 1} }
\right)\]

As the static temperature is not a variable of the formulation, a density value
is derived from temperature:

\[\rho = \frac {p} {T}\]

The below code computes the value of an inflow ghost cell accordingly:

```c++
    fluxForm.addBc<local::NozzleInflowBC<geoDim, nVar>>(ctx, leftBoundary, eos, tTot, pTot);
```

For the outflow boundary condition, the static pressure is directly prescribed
if the flow is subsonic. Nothing is prescribed if the flow is supersonic.

```c++
    fluxForm.addBc<local::NozzleOutflowBC<geoDim, nVar>>(ctx, rightBoundary, eos, pExt);
```

### Extension of the model

- Some source terms could be added to simulate 1D head loss.
- The macroscopic 3D-curvature of the pipe could be taken into account. It would
  requires to integrate momentum on each element which models the pipe. The
  resulting integral would represent the reaction force.
- The fluid element can be coupled with a flexible solid element to model the
  deformation of the pipe due to Euler theorem (compute forces on the pipe from
  momentum balance equation of the fluid inside). See [EPX](http://www-epx.cea.fr/) for a reference implementation.

### Additional discussion

Some simplifications are made in the computation of the source term. The
integral, by itself, does not give the result obtained in \(C\). In this
integral, the pressure term is considered constant in the cell. However, I find
this simplification debatable. By considering \(p\) constant in an element,
one obtains, indeed, the equations of \(C\). But looking more closely, the
exact expression of the quantity \(p\) appearing in \(C\) is:

\[\hat{p} = \frac 1 {\Delta x} \int_a^b p \,dx\]

This is not the exact same \(p\) as defined in the conservative vector \(U\):

\[p = \frac 1 V \int_V p \, dV =
\frac 1 V \int_V pS(x) \, dx\]

In the first case, the pressure is assumed constant in the cell, while in the
second case, the quantity p is pondered by the section variation. Thus, some
error is added here in the numerical scheme. However, with the hypothesis of a
linear evolution of the section in the cell, it may be possible to prove that
this error is negligible or null.

This very [useful discussion](https://scicomp.stackexchange.com/questions/11090/eulers-equations-for-a-tube-with-varying-cross-section)
proposes another set of variables, simplifying the equations. The discussion
they have on the integration of the source term is closely linked to the
discussion on the discretization of the source term integral above. They also
cite useful sources, namely LeVeque work on Euler 1D with varying section.
