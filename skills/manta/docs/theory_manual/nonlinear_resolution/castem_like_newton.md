<!-- source: https://manta-project.gitlab.io/manta/theory_manual/nonlinear_resolution/castem_like_newton.html -->

# A Cast3M like, Newton algorithm implementation

Several ideas introduced in cast3M's Newton algorithm can be reused
in MANTA considering the robustness and performance of their approach.

This section aims at describing some of the tricks that are used
in `UNPAS.procedur`, the subroutine dedicated to the newton like algorithm
used to solve non linear mechanics problems in cast3M. These tricks
are (or will be) implemented in MANTA.

The notations in this page are introduced in [this theory manual page](non_linear_resolution_theory.md#newton-theory).

## Search operator

Computing the consistent tangent search operator \(\v{J}(\v{U}_k)\)
at every iteration of a Newton's algorithm can be very costly in terms of
computing time. Indeed, it can be costly (or impossible) to express
or compute \(\pdfrac{\v{R}(\v{U}_k)}{\v{U}_k}\). Furthermore, if this matrix changes, this means
that the inversion of the system must be performed again from scratch. Reusing a
search operator lighten those operations as the factorization of the system can
be performed once and reused. Finally, some formulations can induce issues in the conditioning
of the matrix, or even in its well-posedness.

Therefore, cast3M uses quasi-Newton like methods where \(\v{J}(\v{U}_k)\)
is almost always approximated, rather than explicitly computed. Furthermore,
this approximation is usually reused through the iterations to keep the initial factorization.

cast3M uses different search operators, that are recomputed following specific rhythms.
Here is a non-exhaustive list of those possible variations, read directly from
`UNPAS.procedur`.

| Mechanical model / configuration | Search operator used | Recompute frequency |
| --- | --- | --- |
| Elastic or plastic model, small strain hypothesis | Elastic stiffness \(\v{K}_e\) | Computed once, at the first step and reused for the rest of the simulation |
| Elastic or plastic model, finite strain | Elastic stiffness, pushed to the current configuration | Recomputed at the beginning of the time step, then again every 20 iterations |
| Damage, viscodamage or ceramic model, small strain | Elastic stiffness rescaled by the current damage state | Computed once, at the beginning of the time step |

These assessments hold in the specific cases that the user has not
requested use of the tangent matrix, or that the boundary conditions are not
too complex and that the model and material parameters remain constant.

Using those approximated search operators usually means that the convergence rate can be
significantly slower than the expected quadratic rate of Newton's approach. A tradeoff is
being made: much more iteration are required with approximated search operators, but those
iterations may be much faster, and more robust (no need to compute the real search operator, and
possibility to reuse the factorization). In cast3M,
several tricks are employed in `UNPAS.procedur` to mitigate this loss of convergence rate,
while retaining the advantages of a quasi-newton.

## Convergence acceleration method

In order to mitigate the loss of convergence rate even further, cast3M uses a convergence
acceleration approach that can be interpreted as an Anderson Acceleration approach [[And65](../../references/references.md#id94), [Ber](../../references/references.md#id100)].

The Anderson approach is described in the [following section](non_linear_resolution_theory.md#theory-convergence-acceleration).
Cast3M's approach differs slightly, mainly as it is driven by forces instead of displacement.
In cast3M, the acceleration is performed from the fourth iteration on, then every other iteration
(4th, 6th, 8th...). It is postponed by 4 iterations when the search operator is rebuilt within the
time step.

(334)\[\boldsymbol{\bar{u}}_i = \boldsymbol{u}_i + \sum_{j=1}^M \Theta^j_i \left( \boldsymbol{u}_{i-j} - \boldsymbol{u}_i \right)\]

Here, the accelerated iterate \(\boldsymbol{\bar{u}}_i\) is written as the current displacement
summed with a linear combination of its differences with the \(M\) previous displacements.
For various reasons explained in [[Eye96](../../references/references.md#id95), [RamiereH15](../../references/references.md#id98)], equation [(334)](#equation-castem-accel-displacement)
can be rewritten with the residual of the mechanical problem.

\[\boldsymbol{\bar{R}}_i = \boldsymbol{R}_i + \sum_{j=1}^M \Theta^j_i \left( \boldsymbol{R}_{i-j} - \boldsymbol{R}_i \right) = \boldsymbol{R}_i + \boldsymbol{D}_i \boldsymbol{\Theta}_i\]

The next iterate is then obtained by a quasi-Newton step from the accelerated iterate, with the
search operator \(\m{K}\) (the elastic stiffness in Cast3M)
\(\delta \v{u} = -\m{K}^{-1} \v{R}\):

(335)\[\boldsymbol{u}_{i+1} = \boldsymbol{\bar{u}}_i - \m{K}^{-1} \boldsymbol{\bar{R}}_i\]

The idea is then to tune the \(\Theta^j_i\) parameters to minimize the norm of the "accelerated" residual
\(\boldsymbol{\bar{R}}_i\). With :

\begin{align}
||\boldsymbol{\bar{R}}_i||^2 &= (\boldsymbol{R}_i + \boldsymbol{D}_i \boldsymbol{\Theta}_i)^T (\boldsymbol{R}_i + \boldsymbol{D}_i \boldsymbol{\Theta}_i) \\
&= \boldsymbol{R}_i^T \boldsymbol{R}_i + 2 \boldsymbol{\Theta_i}^T \boldsymbol{D}_i^T \boldsymbol{R}_i + \boldsymbol{\Theta_i}^T \boldsymbol{D}^T_i \boldsymbol{D}_i \boldsymbol{\Theta}_i
\end{align}

\(\boldsymbol{\Theta}_i\) optimized by :

\begin{align}
& 2 \boldsymbol{D}_i^T \boldsymbol{R}_i + 2 \boldsymbol{D}_i^T \boldsymbol{D}_i \boldsymbol{\Theta}_i = \boldsymbol{0} \\
& \implies \boldsymbol{\Theta}_i = -(\boldsymbol{D}_i^T \boldsymbol{D}_i)^{-1} \boldsymbol{D}_i^T \boldsymbol{R}_i
\end{align}

The value of the coefficients are found by inverting the system shown above.
For the case of 3 previous residuals, \(\v{D}_i = [\Delta\v{R}^1_i\ \Delta\v{R}^2_i\ \Delta\v{R}^3_i]\)
with \(\Delta\v{R}^j_i = \v{R}_{i-j} - \v{R}_i\) (the same directions already
summed over in the definition of \(\bar{\v{R}}_i\) above).
In the following, solving the least-squares problem on \(n\) of these directions
\(\Delta\v{R}^j_i\) is called an "\(n\)-direction fit".

The true system \(\v{D}_i^T\v{D}_i\,\Theta_i = -\v{D}_i^T\v{R}_i\) -- the
actual normal equations, no rescaling -- then reads:

(336)\[\begin{split}\begin{bmatrix}
\|\Delta\v{R}^1_i\|^2 & \Delta\v{R}^1_i\cdot\Delta\v{R}^2_i & \Delta\v{R}^1_i\cdot\Delta\v{R}^3_i \\
\Delta\v{R}^1_i\cdot\Delta\v{R}^2_i & \|\Delta\v{R}^2_i\|^2 & \Delta\v{R}^2_i\cdot\Delta\v{R}^3_i \\
\Delta\v{R}^1_i\cdot\Delta\v{R}^3_i & \Delta\v{R}^2_i\cdot\Delta\v{R}^3_i & \|\Delta\v{R}^3_i\|^2
\end{bmatrix}
\begin{bmatrix} \Theta^1_i \\ \Theta^2_i \\ \Theta^3_i \end{bmatrix}
=
-\begin{bmatrix} \v{R}_i \cdot \Delta\v{R}^1_i \\ \v{R}_i \cdot \Delta\v{R}^2_i \\ \v{R}_i \cdot \Delta\v{R}^3_i \end{bmatrix}\end{split}\]

cast3M does not solve this system directly: to keep the Gaussian elimination's
pivots close to 1 (and improve conditioning), it first normalizes every row by
its own diagonal term \(\|\Delta\v{R}^j_i\|^2\). This is the system actually
assembled and solved in `ACT3.eso`.

(337)\[\begin{split}\begin{bmatrix}
1 & (\Delta\v{R}^1_i\cdot\Delta\v{R}^2_i)/\|\Delta\v{R}^1_i\|^2 & (\Delta\v{R}^1_i\cdot\Delta\v{R}^3_i)/\|\Delta\v{R}^1_i\|^2 \\
(\Delta\v{R}^1_i\cdot\Delta\v{R}^2_i)/\|\Delta\v{R}^2_i\|^2 & 1 & (\Delta\v{R}^2_i\cdot\Delta\v{R}^3_i)/\|\Delta\v{R}^2_i\|^2 \\
(\Delta\v{R}^1_i\cdot\Delta\v{R}^3_i)/\|\Delta\v{R}^3_i\|^2 & (\Delta\v{R}^2_i\cdot\Delta\v{R}^3_i)/\|\Delta\v{R}^3_i\|^2 & 1
\end{bmatrix}
\begin{bmatrix} \Theta^1_i \\ \Theta^2_i \\ \Theta^3_i \end{bmatrix}
=
-\begin{bmatrix}
(\v{R}_i \cdot \Delta\v{R}^1_i)/\|\Delta\v{R}^1_i\|^2 \\
(\v{R}_i \cdot \Delta\v{R}^2_i)/\|\Delta\v{R}^2_i\|^2 \\
(\v{R}_i \cdot \Delta\v{R}^3_i)/\|\Delta\v{R}^3_i\|^2
\end{bmatrix}\end{split}\]

Most of the code present in `ACT3.eso` handles the inversion of this system.
During this step by step hand-made gaussian pivot, conditioning of the system is
evaluated to avoid issues during the inversion.

The next sub-sections describe some of the checks that are performed before,
during, and after this gaussian pivot to make the method more robust (improve
the conditioning, avoid non independant basis, avoid spurious accelerations).

### Flip-flop check

Before attempting the general 3-direction fit, `ACT3` checks for a
specific pathological pattern on the differences \(\Delta\v{R}^j_i = \v{R}_{i-j} - \v{R}_i\):
\(\|\Delta\v{R}^1_i\|^2 > 1.2\,\|\Delta\v{R}^2_i\|^2\) while
\(\|\Delta\v{R}^3_i\|^2\) is close to \(\|\Delta\v{R}^1_i\|^2\)
(ratio between \(0.707\) and \(1.414\)). In other words,
\(\v{R}_{i-2}\) is close to \(\v{R}_i\) and \(\v{R}_{i-3}\) is close to
\(\v{R}_{i-1}\): the iterates alternate between two states
(A, B, A, B) instead of converging monotonically. When detected, `ACT3` does
not attempt the general least-squares fit at all; it raises a warning and
directly sets:

\[\Theta^1_i = \frac{1}{2} + \frac{\|\Delta\v{R}^2_i\|}{2\|\Delta\v{R}^1_i\|}
\,,\qquad \Theta^2_i = 0 \,,\qquad \Theta^3_i = 0\]

With \(\Theta^1_i\) only, the accelerated iterate
\(\bar{\v{u}}_i = \v{u}_i + \Theta^1_i(\v{u}_{i-1} - \v{u}_i)\) lies on the
segment between A (\(\Theta^1_i = 0\)) and B (\(\Theta^1_i = 1\)).
If the cycle is perfect (\(\v{R}_{i-2} = \v{R}_i\)), then
\(\Theta^1_i = 1/2\) and the next iteration restarts from the midpoint
between A and B. This is the natural guess: an iteration that keeps
overshooting the solution by the same amount on each side has the solution
in the middle. If the cycle is not perfect, the second term moves the point
slightly beyond the midpoint, towards B. This correction is empirical.

### Poor independence of the basis vectors

The system [(337)](#equation-castem-act3-system-normalized) is solved by a hand-written
Gaussian elimination. When a division looks unsafe, `ACT3` drops the oldest
direction and solves again with one direction less (3, then 2, then 1).

A division is considered unsafe in two cases:

- a pivot is close to 0: the directions are nearly dependent, which is the
  expected reason;
- an off-diagonal term is close to 0 (\(\Delta\v{R}^1_i\cdot\Delta\v{R}^2_i\)
  or \(\Delta\v{R}^1_i\cdot\Delta\v{R}^3_i\)). This comes from the way
  `ACT3` computes \(\Theta^2_i\) and \(\Theta^3_i\) (it divides by
  these terms). The side effect is that nearly orthogonal directions, which are
  the most useful ones, also lead to dropping directions.

The squared norms \(\|\Delta\v{R}^j_i\|^2\) are floored to \(10^{-10}\)
to avoid dividing by 0 (e.g. two identical consecutive residuals). In Cast3M, this floor only
exists in the 3-direction case; MANTA applies it in the 2- and 1-direction cases too, where
Cast3M would compute \(0/0\). Hence, the 1-direction fit is always applied:
if \(\|\Delta\v{R}^1_i\|\) is nearly 0, \(\Theta^1_i\) can become very
large instead of being set to 0. In Cast3M, only the "large acceleration"
check described below limits it (it is disabled in MANTA).

A second, independent check runs *after* the system is solved: if the
resulting \(\Theta_i\) would make the accelerated residual coincide with
one of the residuals already in memory, the fit is considered degenerate: it
only reproduces past information instead of genuinely extrapolating
(each component within \(0.1\)):

- \(\Theta_i \approx (1,0,0)\), i.e. \(\bar{\v{R}}_i \approx \v{R}_{i-1}\):
  no correction is applied;
- \(\Theta_i \approx (0,1,0)\), i.e. \(\bar{\v{R}}_i \approx \v{R}_{i-2}\):
  solved again with 1 direction;
- \(\Theta_i \approx (0,0,1)\), i.e. \(\bar{\v{R}}_i \approx \v{R}_{i-3}\):
  solved again with 2 directions.

Going back to a previous iterate is useless: with the same search operator,
the next step would lead again to an iterate already computed, and the
iterations would loop.

In short: the number of directions actually used by `ACT3` changes from one
iteration to the next, from the full 3-direction fit down to no correction at
all (the latter only through this second check).

### Bounce back and large acceleration

In `UNPAS.procedur`, right after `ACT3` and *before* the correction
\(\v{C}^i\) is injected in the residual, two checks compare a "work" of the
raw and of the corrected residual along the last displacement increment
\(\delta\v{U}\) (the solution of the last linear solve):

\[W_R = \v{R}^i \cdot \delta\v{U}
\,,\qquad
W_C = (\v{R}^i - \v{C}^i) \cdot \delta\v{U}
\,,\qquad
\alpha = \frac{W_C}{W_R}\]

- \(\alpha > \alpha_{lim}\): the acceleration goes too far, the correction
  is scaled by \(\alpha_{lim}/\alpha\). \(\alpha_{lim} = 1\) if
  \(W_R < 0\), a large value otherwise (\(10^5\) in Cast3M 2026,
  \(256\) in the transcription kept in MANTA);
- \(\alpha \leq 0\): the acceleration goes backward, the correction is
  discarded.

In Cast3M, these checks are not always active. In MANTA, they are transcribed in `act3.cpp` but
they are currently disabled.

## Other tricks

Further tricks described in other pages, or coming soon:

- Non-linear forces (in [this section](non_linear_resolution_theory.md#castem-non-linear-forces))
- Forced convergence (in [this section](non_linear_resolution_theory.md#theory-forced-convergence))
- Cast3M convergence criterion (coming soon)
