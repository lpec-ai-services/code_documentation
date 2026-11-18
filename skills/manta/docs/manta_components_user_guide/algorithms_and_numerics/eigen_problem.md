<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/algorithms_and_numerics/eigen_problem.html -->

# Eigenproblem solver

## Objective

### The `EigenProblem` class

The `EigenProblem` class aims at solving linear (or general) eigenproblems respectively of the form:

(20)\[\begin{split}[ A - \lambda I ] \, \varphi &= 0 \\
[ A - \lambda B ] \, \varphi &= 0\end{split}\]

The solution are the eigenpairs composed of
eigenvalues \(\Lambda = \{... \lambda_i ...\}\)
and eigenvectors \(\Phi = [... \varphi_i ...]\).

Hence, the `EigenProblem` class is built from 1 (or 2) `LinearSystem`
which materializes the matrix \(A\) (and \(B\)).

After `solve` has been called, converged eigenpairs are sorted
by increasing real eigenvalue
and `getEigenValue` and `getEigenVector` methods
give access to \(\lambda\) and \(\varphi\) respectively.

### Examples of application

To cite a few:

- Computation of a modal basis for vibrations analysis :
  \(A \equiv K\) (stiffness matrix)
  and \(B \equiv M\) (mass matrix)
- Computation of a linear buckling mode :
  \(A \equiv K\) (stiffness matrix)
  and \(B \equiv K^{\sigma}\) (geometric stiffness)

## Methods used

This section describes only the functionalities of [SLEPc](https://slepc.upv.es/)
which are used in MANTA to solve [(20)](#equation-eq-evp).

Interested users/developers are invited to read
the [SLEPc user manual](https://slepc.upv.es/documentation/slepc.pdf)
fundamental textbooks [[GeradinR93](../../references/references.md#id81)],
or internal technical reports [[Bou15](../../references/references.md#id80)].

A lot of options can be set by the `petscrc` file, which are read just before `solve`.
Because MANTA's applications generally need a **shift-and-invert** strategy,
this option is set by default in `solve`.
It consists in defining a shift \(\sigma\) so that [(20)](#equation-eq-evp)
can be recast to a linear eigenproblem,
which will converge first to the eigenvalue close to the shift:

(21)\[\begin{split}[ (A - \sigma B) - (\lambda - \sigma) B] \, \varphi &= 0 \\
\Leftrightarrow \quad
[ I - (A - \sigma B)^{-1} (\lambda - \sigma) B] \, \varphi &= 0 \\
\Leftrightarrow \quad
[ \underbrace{(A - \sigma B)^{-1} B}_{A'} - \underbrace{\frac{1}{\lambda - \sigma}}_{\lambda'} I ] \, \varphi &= 0 \\\end{split}\]

Then the options which need to be set in the `petscrc` file are:

- `-eps_nev 15` : 15 eigenpairs are wanted.
- `-eps_target 0.` : eigenvalues closest to 0 are sought first as this value is used a shift.
- `-eps_gen_hermitian` : give information that both matrix are Hermitian (i.e. symmetric in the case of real-value matrix).

Other optional options may be interesting such as:

- `-eps_tol 1.e-12` : to change from the default set to 1e-8.
- `-eps_max_it 100` : to limit the number of iterations.
- `-eps_view`: for debugging purpose, list the options used by SLEPc.
- `-eps_monitor`: for debugging purpose, list convergence information during iterations

## Handling constraints

As explained in [The constraint sets](../../developer_guide/pipeline/linear_system.md#constraint-sets), constraint sets
introduce Lagrange multipliers increasing the system size
by the matrix \(C\) and its transpose,
leading to the constrained eigenproblem to solve:

(22)\[\begin{split} \left[
\begin{bmatrix} A & C^T \\ C & 0 \end{bmatrix}
- \lambda
\begin{bmatrix} B & 0 \\ 0 & 0 \end{bmatrix}
\right]
\begin{pmatrix} U \\ \mu \end{pmatrix}
&=
\begin{pmatrix} 0 \\ 0 \end{pmatrix}
\\
\Leftrightarrow \quad
\left[ \quad
{Z_A} \qquad
- \lambda
\quad {Z_B}
\quad \right]
\quad \varphi \quad
&=
\quad 0\end{split}\]

where \(\mu\) represents the Lagrange multipliers.

Several resolution methods exist in MANTA for the linear system problem
as described in
[The constraint sets](../../developer_guide/pipeline/linear_system.md#constraint-sets), [Constraint Set](../../developer_guide/blueprints/constraint_set.md#blueprint-constraint-set),
[Elimination of some constraint sets](../../developer_guide/pipeline/linear_system.md#elimination-of-some-jargconstraint-sets),
[Linear System](../../developer_guide/blueprints/linear_system_blueprint.md#blueprint-linear-system)
and [Elimination of constraint set](../../developer_guide/pipeline/constraints_set_eliminated.md#constraints-sets-eliminated).

1. Direct elimination methods modify \(A\) into \(A^*\) during the assembling stage
   so that corresponding \(C\) is not needed to enforce constraints.
   This is the case of simple Dirichlet and blocking conditions.
2. When direct elimination is not exhaustive
   (*monolithic* and *schur* cases
   which may occur for multiple point constraints for example),
   corresponding \(C\) matrix should be provided to the solver,
   leading to supplying the larger matrices \(Z_A\) and \(Z_B\).

These observations remain applicable for eigenproblems as well as for linear system,
so that the resolution algorithm is chosen depending on the situation (1. or 2.).

In [[BL09](../../references/references.md#id77)], a projection method is described to ensure the Krylov vectors
respect the constraints. The formulae is found equivalent
to [the Ainsworth one](../../developer_guide/pipeline/linear_system.md#linear-system-ainsworth-method).
Some closely related elimination techniques
are often encountered like in [[PBG+14](../../references/references.md#id79)].

## Mode normalization

The default SLEPC normalization is used for eigenvectors,
meaning that for a generalized Hermitian eigenvalue problem, we have:

\[|\varphi|_ B = \sqrt{\varphi^T B \varphi} = 1\]
