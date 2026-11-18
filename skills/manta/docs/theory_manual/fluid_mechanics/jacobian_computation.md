<!-- source: https://manta-project.gitlab.io/manta/theory_manual/fluid_mechanics/jacobian_computation.html -->

# Computing the Jacobian matrix for Euler Implicit Formulations

When solving Euler equations for inviscid compressible flows with an implicit
time scheme, estimating the jacobian matrix is needed:

\[A = \frac{\partial \mathbf{F(U)}}{\partial \mathbf{U}}\]

with:

- \(\mathbf{U}\) the vector of conservative variables
- \(\mathbf{F(U)}\) the flux vector

## Options

Various options exist in MANTA to determine the Jacobian. The desired option
is given as a template parameter of the Euler Implicit Formulation constructor,
as the type of Integrand used to compute elementary terms of the Jacobian.

Available options are:

- `RoeJacobianIntegrand`: computes the Jacobian using Roe RiemannSolver;
- `RusanovJacobianIntegrand`: computes the Jacobian using Rusanov RiemannSolver;
- `HLLCJacobianIntegrand`: computes the Jacobian using HLLC RiemannSolver;
- `HLLCExactJacobianIntegrand` (default): exactly computes the Jacobian using HLLC RiemannSolver;

  The term `exact` means that the analytical expression of the Jacobian
  has been derived using symbolic computations (`sympy` module of Python,
  here). The produced analytical symbolic expression has then been
  implemented in C++ using automatic code generation (a `sympy` feature).
  Note that most of the Riemann solvers are not differentiable on all their
  domain of definition. This is often due to the presence of absolute
  values in the analytical expression of the Riemann solver. In case where
  the present jacobian is evaluated on such non-differentiable point, the
  computed jacobian value depends on floating point approximations and thus
  might be unstable across systems.
- `FiniteDifferencesJacobianIntegrand`: computes the Jacobian by perturbation;

  This Jacobian is much more expensive to compute compared to
  other jacobians, due to the numerous perturbations to compute. However,
  it allows to have a ready-to-use, well-approximated jacobian for any
  Riemann solver. In comparison, when no exact (analytical) jacobian is
  available for a given Riemann solver, the present `FiniteDifferences`
  jacobian might give much more accurate approximation than using an
  unrelated jacobian (e.g. using a Rusanov jacobian for an HLLC Riemann
  solver), leading to much higher convergence rate. The higher convergence
  rate might compensate for the additional computation cost of finite
  differences mentioned above. Also note that an exact jacobian of a given
  Riemann solver is often quite complex to implement (see, for instance,
  `HLLCExactJacobianIntegrand`).

### Notes on the choice of a jacobian expression for the implicit formulation

Compared to an explicit formulation, the main difference rely in the choice of a
jacobian expression of the chosen Riemann solver. This jacobian is often very
complex to compute exactly. It may even be undefined on some points of the
definition domain of the Riemann solver. The jacobian is thus often
approximated. Such approximation impacts the convergence rate of the iterations
of the implicit time scheme. It might even lead to a convergence failure.

For a theoretical perfect convergence of the implicit iteration, if the
underlying linear system to invert has a unique solution, the choice of the
jacobian has no impact on the result. Compressible fluid flow systems sometime
have multiple steady-state solutions (e.g. weak/strong shock over a wedge). In
this case, the choice of the jacobian has an impact on the final solution.

Each jacobian has a different computation cost. There is a compromise between
the computation cost of the jacobian and its impact on the convergence rate of
the implicit time scheme, in order to find the combination of operators which
gives the shortest computation time.

Note

The `RecoOperator` and the `LimitOperator` considered for
the computation of the jacobian are always the `PieceWiseConstant`
reconstruction and the `None` limiter, i.e. trivial, no-op operators. If any
other reconstruction or limiter is chosen, the jacobians do not take their
effect into account, leading to a jacobian possibly very far from the
theoretically exact jacobian.
