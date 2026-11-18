<!-- source: https://manta-project.gitlab.io/manta/theory_manual/nonlinear_resolution/non_linear_resolution_theory.html -->

# Resolution of non-linear implicit problems in MANTA

The resolution of non-linear problem in MANTA is performed using Newton like algorithms
that are described in these pages.

## [Newton algorithm](#id15)

As is detailed in [this section](../../developer_guide/blueprints/newton_algorithm_blueprint.md#blueprint-newton-algorithm),
the system that is being resolved can be written as:

(324)\[\begin{split}\begin{bmatrix}
\m{J(\v{U}^k)} &
\v{C}^T\\
\v{C} &
\m{0}
\end{bmatrix}
\begin{bmatrix}
\delta \v{U}^k\\
\v{\lambda^k}
\end{bmatrix}
=-
\begin{bmatrix}
\v{R(\v{U}^k)}\\
\m{C} \v{U}^k - \v{D}
\end{bmatrix}\end{split}\]

With \(\m{J}\) the jacobian of the problem computed from the current iterated primal \(\v{U}^k\),
\(\v{R}\) the corresponding residual, and \(\m{C}\), \(\v{D}\),
the terms linked to the constraints. The unknowns of the problem are
\(\delta \v{U}^k = \v{U}^{k+1} - \v{U}^k\) and \(\v{\lambda}\).

Note

Note that in this page, we consider that \(\m{C}\) is constant throughout the iterations of one time-step.

The non-linear system of equations to be solved can be summarized as
setting a residual to 0. This residual generally expresses a physical imbalance.
We seek \(\v{U}^{k+1}\) such that:

\[\v{R(\v{U}^{k+1})} = 0\]

Newton-Raphson approach is based on the linearization of this residual around the current guess :

\[\v{R(\v{U}^{k+1})} \simeq \v{R(\v{U}^{k})} + \pdfrac{\v{R(\v{U}^{k})}}{\v{U}^{k}} \delta \v{U}^{k}\]

with

\[\delta \v{U}^{k} = \v{U}^{k+1} - \v{U}^{k}\]

and

(325)\[\pdfrac{\v{R(\v{U}^{k})}}{\v{U}^{k}}
= \m{J(\v{U}^k)}\]

Isolating \(\delta \v{U}^{k}\) in the equation above makes it possible to
write the expression of the increment necessary to approach the null residual.

\[\delta \v{U}^{k} = - (\m{J(\v{U}^k)})^{-1} \v{R(\v{U}^{k})}\]

The Newton approach thus supposes that the expression of a null residual can
be incrementally approached by computing this increment, by solving successively
the linear system in [(324)](#equation-theory-non-linear-system).

### [Limits to the Newton algorithm](#id16)

Newton's approach is characterized by this usage of the jacobian of the problem
to search space. This means that, close to the solution, convergence is quadratic.
However, this approach can be limited by three factors:

- far from the solution, nothing ensures us of convergency (and no certainty either about the rate of convergency).
- computing the consistent jacobian \((\m{J(\v{U}^k)})\) at every newton iterations can be very costly (or impossible).
- solving the system in eq.([(324)](#equation-theory-non-linear-system)) if \((\m{J(\v{U}^k)})\) changes for each k is very costly (or impossible).

In Cast3M, these limitations are mitigated by using several tricks that we are trying to imitate in MANTA,
and that are documented in this page, notably:

- using a "quasi-Newton" approach, meaning that an approximation of the consistent jacobian \((\m{J(\v{U}^k)})\) is used.
- trying to make a first guess, as close to the solution as possible ("non-linear forces computation" - coming soon)
- using convergence acceleration tools to mitigate the slower convergence of quasi-newton approaches.
- using the so-called "forced-convergence" trick to avoid non converging cases. - coming soon

Note that several other clever tricks are put forward in cast3M, but are not yet used in MANTA.
A more detailed description of some of the specifics of cast3M non-linear implicit solver are available
in [this page](castem_like_newton.md#castem-newton).

## [Quasi-Newton approaches](#id17)

As detailed in the previous section, most limitations of the Newton algorithm are linked to the
cost of computing (and assembling, and "inverting"), the consistent jacobian.

The idea behind quasi-Newton approaches is to use an approximation of the consistent jacobian
to lower this cost. For instance, consider an approach where the jacobian is computed only once per time step.
In this case the consistent jacobian must be assembled once, the LU factorization used to solve eq.([(324)](#equation-theory-non-linear-system)),
can be performed once, instead of at each iterations.

However, note that if this can save a lot of computing time for one iteration, such methods are
usually linked to much slower convergence rates (as we are not using a search operator consistent with
the problem at hand). Below are some 1D vizualization of the methods:

[![figure](https://manta-project.gitlab.io/manta/_images/fig_newton.png)](../../_images/fig_newton.png)

Fig. 119 Newton iterations over three load steps: the search operator is the tangent.

[![figure](https://manta-project.gitlab.io/manta/_images/fig_quasi_elastic_per_step.png)](../../_images/fig_quasi_elastic_per_step.png)

Fig. 120 Quasi-Newton iterations, the search operator being recomputed at the
beginning of every load step and kept for its iterations.

[![figure](https://manta-project.gitlab.io/manta/_images/fig_quasi_elastic_frozen.png)](../../_images/fig_quasi_elastic_frozen.png)

Fig. 121 Quasi-Newton iterations, the search operator being computed once at the
first load step and kept for the whole simulation.

Quasi-Newton like solvers can be set-up in MANTA using the `jacobianUpdateTrigger`, described
in [this section](../../manta_components_user_guide/algorithms_and_numerics/newton.md#jacobianupdatetrigger).

## [Computing the "non-linear forces"](#id18)

(coming soon in MANTA)

One key aspect of improving the convergence rate, and overall robustness and
performance of the method, is to use a good first approximate to start the
iterative procedure.

In Cast3M, a clever trick was introduced to get a better approximation
of this first iterate. It is based on the computation of so-called "non-linear forces".

At the beginning of the time-step, using information computed at the previous time-step,
the initial residual is corrected with an approximation of the "non-linear forces".

\[\v{R}^*_n(\v{U}_0) = \v{R}_n(\v{U}_0) - \alpha \v{F}^{NL}_{n-1}\]

with \(\alpha\) a load coefficient.

If the behaviour had been linear with respect to the displacement, for instance with an
elastic model in small strain, the increment of force computed over the previous time-step would
have been \(\v{K}_{elas} \Delta \v{U}_{n-1}\). However, due to the non-linear nature of the model
, a different force was found. The difference between the expected "linear" force
and the resulting force can be considered as the "non-linear" forces computed at the previous
time-step.

The trick is then to assume that this difference between the expected "linear" force and the
computed resulting force, will be the same at the current step. In a sense
it considers that the non linearity "rate" is the same between the two steps.

The non-linear forces are expressed as:

\[\v{F}^{NL}_{n-1} = \v{K}_{elas} (\v{U}^{ets}_{n-1} - \v{U}^{bts}_{n-1}) - \Delta \v{F}^{ext}_{n-1} - \v{R}^{ets}_{n-1}\]

with the tags `ets` for end of time-step and `bts` for beginning of time-step.

Note that the term \(\v{R}^{ets}_{n-1}\) is very close to 0 but still inputed.

The load ratio \(\alpha\) handles the possibility that the time-step (and/or imposed
external force or displacement) can be different between those two time steps.
Its expression makes it so that if the time-step and/or charge increment is constant, it is equal to 1,
while if the time-step and/or charge increment was multiplied by a constant \(n\)
, it is equal to \(n\).

In Fig. [Fig. 122](#fig-castem-nonlinear-forces) lies a one dimensional visual representation of the approach.

[![figure](https://manta-project.gitlab.io/manta/_images/nonlinear_forces_figure.png)](../../_images/nonlinear_forces_figure.png)

Fig. 122 Non-linear force correction. (a) At step \(n-1\), \(\v{F}^{NL}_{n-1}\) is the
gap between the elastic prediction \(\v{K}_e \Delta \v{U}_{n-1}\) and the force
actually reached. (b) At step \(n\), adding it to the external load moves the
first iterate much closer to the solution: the yellow point instead of the grey one.

Some information in this section come from the internal CEA technical report by Ali Mezher [[Mez24](../../references/references.md#id99)].

## [Convergence acceleration approaches](#id19)

In MANTA, following work in cast3M [[Ber](../../references/references.md#id100)] and other CEA internal codes ([[MHRamiereE18](../../references/references.md#id101), [RamiereH15](../../references/references.md#id98)]),
two convergence acceleration algorithms are available. They are both based on the Anderson acceleration approach, described
in depth in several articles (e.g. [[Eye96](../../references/references.md#id95)], [[FS09](../../references/references.md#id96)], [[WN11](../../references/references.md#id97)]).
In a similar way to the quasi-newton methods described above, the Anderson acceleration method
is based on the search of a new iterate without the full computation of the jacobian term. It relies on the information
of \(M\) previous iterate (of \(\v{R}\) or \(\v{U}\) for instance), to find a reliable direction
of search.
This section describe some of the theoretical elements behind those approaches.

A quasi-Newton approach can be recasted as a fixed point iteration problem,
as explicited in Fang et. al [[FS09](../../references/references.md#id96)]:
the problem is finding \(\v{x}^*\) such that \(g(\v{x}^*)=\v{x}^*\),
with \(g: \mathbb{R}^n \rightarrow \mathbb{R}^n\).
In the case of Newton algorithm, we search for

(326)\[ \v{U}^{k+1} = \v{G(\v{U}^{k})}\]

For a quasi-newton method, using a constant search operator
\((\m{J_{quasi}})\), we can rewrite eq.([(324)](#equation-theory-non-linear-system))

(327)\[ \v{G(\v{U}^{k})} = \v{U}^{k+1} = \v{U}^{k} - (\m{J}_{quasi})^{-1} \v{R(\v{U}^{k})}\]

Furthermore we can define the residual of the fixed point problem as:

(328)\[ \v{Q(\v{U}^{k})} = \v{G(\v{U}^{k})} - \v{U}^{k}\]

Note

In the specific case of non-linear implicit mechanics, the fixed point residual is
\(\delta \v{U}^k\).

The base principle of an Anderson type acceleration method is to
build an accelerated iterate from a least-squares fit
over the last few fixed-point images.

Following the formalism from Eyert [[Eye96](../../references/references.md#id95)],
we can write a term of the accelerated sequence of the solution as:

\[\boldsymbol{\bar{u}}_i = \boldsymbol{u}_i + \sum_{j=1}^M \Theta^j_i \left( \boldsymbol{u}_{i-j} - \boldsymbol{u}_i \right)\]

Meaning that the accelerated term is written as the current iterate, summed with a linear combination of the
previous iterates. We can write:

\[\boldsymbol{\bar{G}}(\boldsymbol{u}_i) = \boldsymbol{G}(\boldsymbol{u}_i) + \sum_{j=1}^M \Theta^j_i
\left( \boldsymbol{G}(\boldsymbol{u}_{i-j}) - \boldsymbol{G}(\boldsymbol{u}_i) \right)\]

And then, by writing \(\boldsymbol{\bar{G}} - \boldsymbol{\bar{u}}\), we have:

\[\boldsymbol{\bar{Q}}_i = \boldsymbol{Q}_i + \sum_{j=1}^M \Theta^j_i \left( \boldsymbol{Q}_{i-j} - \boldsymbol{Q}_i \right) = \boldsymbol{Q}_i + \boldsymbol{D}_i \boldsymbol{\Theta}_i\]

The idea is then to tune the \(\Theta^j\) parameters to minimize the norm of the accelerated fixed point
residual \(\boldsymbol{\bar{Q}}_i\).

The minimization is written as:

\begin{align}
\boldsymbol{\Theta}_i = \underset{\boldsymbol{\Theta}}{\mathrm{argmin}} \; ||\boldsymbol{\bar{Q}}_i||^2
\end{align}

with :

\begin{align}
||\boldsymbol{\bar{Q}}_i||^2 &= (\boldsymbol{Q}_i + \boldsymbol{D}_i \boldsymbol{\Theta}_i)^T (\boldsymbol{Q}_i + \boldsymbol{D}_i \boldsymbol{\Theta}_i) \\
&= \boldsymbol{Q}_i^T \boldsymbol{Q}_i + 2 \boldsymbol{\Theta_i}^T \boldsymbol{D}_i^T \boldsymbol{Q}_i + \boldsymbol{\Theta_i}^T \boldsymbol{D}^T_i \boldsymbol{D}_i \boldsymbol{\Theta}_i
\end{align}

\(\boldsymbol{\Theta}_i\) optimized by :

\begin{align}
& 2 \boldsymbol{D}_i^T \boldsymbol{Q}_i + 2 \boldsymbol{D}_i^T \boldsymbol{D}_i \boldsymbol{\Theta}_i = \boldsymbol{0} \\
& \implies \boldsymbol{\Theta}_i = -(\boldsymbol{D}_i^T \boldsymbol{D}_i)^{-1} \boldsymbol{D}_i^T \boldsymbol{Q}_i
\end{align}

In MANTA, we write the correction as:

\begin{align}
\boldsymbol{u}_{i+1} &= \boldsymbol{\bar{u}}_i + \boldsymbol{\bar{Q}}_i \\
&= \boldsymbol{\bar{G}}(\boldsymbol{u}_i) \\ &= \boldsymbol{G}(\boldsymbol{u}_i) + \sum_{j=1}^M \Theta^j_i
\left( \boldsymbol{G}(\boldsymbol{u}_{i-j}) - \boldsymbol{G}(\boldsymbol{u}_i) \right) \\
&= \boldsymbol{u}_i + \delta \boldsymbol{u}_i+ \sum_{j=1}^M \Theta^j_i
\left( \boldsymbol{u}_{i-j} + \delta \boldsymbol{u}_{i-j} - (\boldsymbol{u}_i + \delta \boldsymbol{u}_i) \right)
\end{align}

\begin{equation}
\delta \boldsymbol{u}_{i} = -\boldsymbol{J}^{-1} \boldsymbol{R}(\boldsymbol{u}_i)
\end{equation}

Note that considering Anderson acceleration with a depth of 1, in a one dimensional setting,
is exactly the same as the secant approach: approximating the search direction with the
slope going through the two previous points. It can be a low dimensional visual representation
of the approach, as shown in Fig. [Fig. 123](#fig-castem-conv-accel).

[![figure](https://manta-project.gitlab.io/manta/_images/1Dact3.png)](../../_images/1Dact3.png)

Fig. 123 One dimensional visual representation of Anderson approach if depth is 1.

### [Cast3M slight variation of Anderson's approach](#id20)

Cast3M's `ACT3` operator differs from the formalism above.
Let us consider the example of structural mechanics, for which the unknown iterate
is displacement. In this context, Cast3M performs a variant of Anderson's acceleration
that works on force rather than displacement.

Therefore, considering the formalism shown above, with the following accelerated iterate:

\[\boldsymbol{u}_{i+1} = \boldsymbol{G}_i + \sum_{j=1}^M \Theta^j_i
\left( \boldsymbol{G}_{i-j} - \boldsymbol{G}_i \right),
\qquad \text{with} \quad \boldsymbol{G}_i = \boldsymbol{G}(\boldsymbol{u}_i).\]

As explained in the [following page describing cast3M non-linear algorithm](castem_like_newton.md#castem-newton),
the search operator is usually the elastic stiffness, that we write \(\m{K}\)
(i.e. \(\m{J}_{quasi} = \m{K}\) in [(327)](#equation-fixedpoint2)).
To switch to forces we can multiply everything by this stiffness operator:

(329)\[\m{K} \boldsymbol{u}_{i+1} = \m{K} \boldsymbol{G}_i + \sum_{j=1}^M \Theta^j_i
\m{K} \left( \boldsymbol{G}_{i-j} - \boldsymbol{G}_i \right)\]

By definition, from equation [(327)](#equation-fixedpoint2) with \(\m{J}_{quasi} = \m{K}\),

\[\m{K} \boldsymbol{G}_i = \m{K} \boldsymbol{u}_i - \v{R}_i .\]

Therefore, with \(\delta \boldsymbol{u}_i = \boldsymbol{u}_{i+1} - \boldsymbol{u}_i\),
we can rewrite equation [(329)](#equation-force-anderson) as:

(330)\[\m{K} \delta \boldsymbol{u}_i = - \v{R}_i - \sum_{j=1}^M \Theta^j_i
\m{K} \left( \boldsymbol{G}_i - \boldsymbol{G}_{i-j} \right),\]

that is:

(331)\[\m{K} \delta \boldsymbol{u}_i = - \left( \v{R}_i + \v{R}^{acc}_i \right),
\qquad
\v{R}^{acc}_i = \sum_{j=1}^M \Theta^j_i \m{K} \left( \boldsymbol{G}_i - \boldsymbol{G}_{i-j} \right).\]

This formalism enables Cast3M to:

- Find the \(\Theta\) coefficients from the minimization of a "force" quantity,
- Correct the residual **before** solving,
- Then solve with the corrected residual and find the accelerated iterate.

More precisely, the \(\Theta\) coefficients minimize the norm of the accelerated residual
\(\v{R}_i + \sum_{j=1}^M \Theta^j_i \left( \v{R}_{i-j} - \v{R}_i \right)\),
instead of the norm of the accelerated fixed point residual \(\boldsymbol{\bar{Q}}_i\).
Since \(\m{K} \boldsymbol{Q}_i = - \v{R}_i\), this amounts to minimizing
\(||\m{K} \boldsymbol{\bar{Q}}_i||\) instead of \(||\boldsymbol{\bar{Q}}_i||\):
the structure of the method is the same, only the norm differs.

Note

To be more specific the minimization is performed on the residual weighted by the
element size. Without this coefficient, residuals on larger elements would
weight larger in the minimization process.

In Cast3M and MANTA implementation of this approach, \(\v{R}^{acc}_i\) is not written
directly as expressed in equation [(331)](#equation-acc-castem2).
The absolute differences (from \(i\) to \(i-j\)) are rewritten as sums of
consecutive differences (from \(i\) to \(i-1\)). This is equivalent to a change of basis.
Indeed, considering that \(\m{K}\) is constant throughout iterations, we can write:

\begin{align}
\m{K}(\boldsymbol{G}_i - \boldsymbol{G}_{i-1}) &= \m{K}(\boldsymbol{G}_i - \boldsymbol{G}_{i-1}), \\
\m{K}(\boldsymbol{G}_i - \boldsymbol{G}_{i-2}) &= \m{K}(\boldsymbol{G}_i - \boldsymbol{G}_{i-1}) + \m{K}(\boldsymbol{G}_{i-1} - \boldsymbol{G}_{i-2}), \\
\m{K}(\boldsymbol{G}_i - \boldsymbol{G}_{i-3}) &= \m{K}(\boldsymbol{G}_i - \boldsymbol{G}_{i-1}) + \m{K}(\boldsymbol{G}_{i-1} - \boldsymbol{G}_{i-2}) + \m{K}(\boldsymbol{G}_{i-2} - \boldsymbol{G}_{i-3}).
\end{align}

Following [[MHRamiereE18](../../references/references.md#id101)], we write the consecutive differences as:

(332)\[\v{R}^*_i = \m{K} (\boldsymbol{G}_i - \boldsymbol{G}_{i-1}).\]

In Cast3M, \(M = 3\) (the last four residuals are used).
Substituting the three expressions above in [(331)](#equation-acc-castem2), we get:

\[\v{R}^{acc}_i = \Theta^1_i \v{R}^*_i + \Theta^2_i \left( \v{R}^*_i + \v{R}^*_{i-1} \right)
+ \Theta^3_i \left( \v{R}^*_i + \v{R}^*_{i-1} + \v{R}^*_{i-2} \right),\]

and, regrouping by \(\v{R}^*\):

(333)\[\v{R}^{acc}_i = (\Theta^1_i + \Theta^2_i + \Theta^3_i) \v{R}^*_i + (\Theta^2_i + \Theta^3_i) \v{R}^*_{i-1} + \Theta^3_i \v{R}^*_{i-2}.\]

Finally, \(\v{R}^*_i\) is computed from the residuals. Developing \(\boldsymbol{G}_i\) and \(\boldsymbol{G}_{i-1}\)
in [(332)](#equation-rstar-def):

\[\v{R}^*_i = \m{K} (\boldsymbol{G}_i - \boldsymbol{G}_{i-1})
= \m{K} (\boldsymbol{u}_i - \boldsymbol{u}_{i-1}) - (\v{R}_i - \v{R}_{i-1})
= \m{K} \delta \boldsymbol{u}_{i-1} - (\v{R}_i - \v{R}_{i-1}),\]

and using [(331)](#equation-acc-castem2) at iteration \(i-1\),
\(\m{K} \delta \boldsymbol{u}_{i-1} = - \left( \v{R}_{i-1} + \v{R}^{acc}_{i-1} \right)\):

\[\v{R}^*_i = - \v{R}_{i-1} - \v{R}^{acc}_{i-1} - \v{R}_{i} + \v{R}_{i-1} = - \left( \v{R}_{i} + \v{R}^{acc}_{i-1} \right).\]

\(\v{R}^*_i\) is thus the current residual, corrected by the correction injected at the previous iteration.

Some details about the specific computation handled in `ACT3` are available in
[this page](castem_like_newton.md#castem-newton). Furthermore, a rigorous analogy between Anderson method and
cast3M's specific version is done in the work from B.Michel [[MHRamiereE18](../../references/references.md#id101)].

## [Forced convergence "trick"](#id21)

(coming soon)

With a strongly non-linear behaviour (damage, plasticity), Newton's algorithm
can stall during a time step: the residual stops decreasing, or keeps
oscillating.

Forced convergence is a trick used in Cast3M to avoid such non-convergence.
The name "forced convergence" to designate the trick is not so clear: it should rather be named
"sub-stepping without equilibrium".

When stagnation is detected, the **current, non converged, state is committed**: the
stresses and internal variables that the behaviour integrated at the last iterate
become the new state at the beginning of the step. The resolution then restarts
from this state **with the same loading**. The history of the material (damage,
plastic strain) has moved forward, which can help convergence.

The price is that an intermediate state, which satisfies the behaviour locally
but is not in global equilibrium, is introduced on the loading path. The final
solution of the time step is therefore not exactly the integration of the
prescribed loading path.
