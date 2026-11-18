<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/algorithms_and_numerics/contact/contact.html -->

# Contact algorithms

## Time integrators

### CentralDifferenceWContactTimeIntegrator

FICTIVE PREDICTED CONFIGURATION TO COMPUTE CONTACT CONDITIONS

This integrates the problem using a central difference time integrator,
and computes the contact conditions from a fictive predicted
configuration.

Assuming that the configuration \(\v{X}_{n}\) and velocities
\(\v{V}_{n-1/2}\) at discrete times \(n\) and \(n-1/2\)
respectively are known, one would like to compute the acceleration
\(\v{G}_{n}\) at time \(n\).

The problem to solve to get this acceleration can be writen:

\[\begin{split}\begin{bmatrix}
\m{M} & \m{B}^t & (\m{C}^*)^t \\
\m{B} & \m{0} & \m{0} \\
\m{C}^* & \m{0} & \m{0} \\
\end{bmatrix}
\begin{bmatrix}
\v{G}_n\\
\v{\mu}\\
\v{\lambda} \\
\end{bmatrix}
=
\begin{bmatrix}
\v{F}_n^e - \v{F}_n^i\\
\v{D}\\
\v{E}^*\\
\end{bmatrix}\end{split}\]

where \(\m{M}\) is a diagonal mass matrix, \(F_n^i\) is the
internal forces vector, and \(F_n^e\) is the external forces vector.
The matrix \(\m{B}\) and the vector \(\v{D}\) enforce the
kynematic boundary conditions which are not related ton contact, while
\(\m{C}^*\) and \(\m{E}^*\) enforce the contact conditions.
\(\m{C}^*\) and \(\m{E}^*\) are computed a fictive configuration
\(\v{X}_{n+1}^*\) and velocities \(\v{V}_{n+1/2}^*\):
\(\m{C}^*=\m{C}(\v{X}_{n+1}^*, \v{V}_{n+1/2}^*)\) and
\(\v{E}^*=\v{E}(\v{X}_{n+1}^*, \v{V}_{n+1/2}^*)\).

Multiplying the first equation by \(\m{B}\m{M}^{-1}\), one gets:

\[\v{D}+\m{B}\m{M}^{-1}\m{B}^t\v{\mu}+\m{B}\m{M}^{-1}(\m{C}^*)^t\v{\lambda}=\m{B}\m{M}^{-1}(\v{F}_n^e - \v{F}_n^i)\]

If one assumes that \(\m{B}(\m{C}^*)^t=\m{0}\), which means that
there is no degree of freedom involved in both the contact and the other
boundary conditions, it implies that
\(\m{B}\m{M}^{-1}(\m{C}^*)^t=\m{0}\) as \(\m{M}\) is diagonal.
Then one can compute \(\v{\mu}\):

\[\v{\mu}=(\m{B}\m{M}^{-1}\m{B}^t)^{-1}\left[\m{B}\m{M}^{-1}(\v{F}_n^e - \v{F}_n^i)-\v{D}\right]\]

A fictive acceleration \(\v{G}_{n}^*\) is computed assuming that
there is no contact:

\[\v{G}_{n}^*=\m{M}^{-1}(\v{F}_n^e - \v{F}_n^i-\m{B}^t\v{\mu})\]

Then fictive velocites and configuration are computed with the central
difference time integration scheme:

\[\begin{split}\begin{aligned}
\v{V}_{n+1/2}^*&=\v{V}_{n-1/2}+\Delta t \v{G}_{n}^*\\
\v{X}_{n+1}^*&=\v{X}_{n}+\Delta t \v{V}_{n+1/2}^*\\
\end{aligned}\end{split}\]

Then one can compute \(\v{\lambda}\):

\[\v{\lambda}=(\m{C}^*\m{M}^{-1}(\m{C}^*)^t)^{-1}\left[\m{C}^*\v{G}^*-\v{E}^*\right]\]

And finally the acceleration:

\[\v{G}_{n}=\v{G}_{n}^* + (\m{C}^*)^t\v{\lambda}\]

### CentralDifferenceWFrictionTimeIntegrator

Friction modeling requires a specific algorithm in order to solve
the acceleration with friction forces.

At time step \(n+1\):

1. Compute displacement and half-step velocity

> - \(U_{n+1} = U_{n} + V_n \Delta t + G_n \frac{\Delta t^2}{2}\)
> - \(V_{n+\frac{1}{2}} = V_n + G_n \frac{\Delta t}{2}\)

2. Assemble and solve \(G_{n+1}^*\) with active contact and active
   sticking but not sliding forces

> - sticking and sliding status are determined in the *assemble* stage
>   from previous state (at time step \(n\))

3. Determine sliding forces

> - Compute reaction from first resolution \(\v{R} = - \m{C}^T \v{\lambda}\)
> - Compute sliding forces according to the friction model*
> - Apply the sliding forces to the *RHS*

4. Assemble and solve \(G_{n+1}\) as a complete problem
5. Compute the end of time step velocity

> - \(V_{n+1} = V_{n+\frac{1}{2}} + G_{n+1} \frac{\Delta t}{2}\)

Note

At the moment, stage 4 is very costly because the *RHS* terms are
entirely re-assembled in order to add the sliding forces into the
*RHS* vector
