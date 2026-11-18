<!-- source: https://tripoli5.asnr.dev/documentation/latest-release/theory/collision_physics/svt.html -->

# The SVT algorithm

The following algorithm is used to sample the target velocity in TRIPOLI-5.

The Maxwell-Distribution for the target velocity reads

\[f(v) = \sqrt{\dfrac{2}{\pi}} \left[ \dfrac{m}{k_B T} \right]^{\frac{3}{2}}v^2 \exp\left( -\dfrac{mv^2}{2k_B T} \right).\]

Comparing \(P_2\) to the Maxwell-Boltzmann distribution for speed gives

\[\beta = \sqrt{\dfrac{m}{2k_B T}}.\]

Currently, TRIPOLI5 samples from \(P(y)\) using a custom `MaxwellDistribution` class implemented in `Core/rng` module.

The first case is similar to MCNP procedure: with probability \(\alpha\), \(y\) is sampled using a [Gamma distribution](https://en.wikipedia.org/wiki/Gamma_distribution) of parameter with a shape parameter equal to 2 and a scale parameter equal to 1.

The speed is then computed as \(V = \dfrac{y}{\beta}\), which perfectly matches the first step described in MCNP procedure.

The second case (with probability \(1-\alpha\)) consists in sampling the velocity according to the following procedure.
`tripoli5::core::rng::MaxwellDistribution` is used to sample

\[y = x + z^2\]

where

\[\boxed{X\sim Exp\left(\lambda=\dfrac{1}{\theta}\right) \Leftrightarrow Gamma(1, \theta)}\]

\[Z\sim \mathcal{N}\left( \mu = 0,\sigma^2 = \dfrac{\theta}{2}\right)\]

Thus,

\[Q = \dfrac{Z^2}{\theta/2} \sim \chi^2_1\]

\[\dfrac{\theta}{2}\times Q = \boxed{Z^2 \sim Gamma\left(\dfrac{1}{2}, \theta\right).}\]

This arise from the fact than if \(Q\sim \chi^2(k) = \chi^2_k\), then \(Q \sim Gamma\left( \dfrac{k}{2},2c \right)\).

Now, considering \(X_1 \sim Gamma(a_1,b)\) and \(X_2\sim Gamma(a_2,b)\),
$\(X_1 + X_2 \sim Gamma(a_1+a_2,b).\)$

Thus,

\[\boxed{Y = X + Z^2 \sim Gamma\left( \dfrac{3}{2},\theta\right).}\]

Now, the target velocity is computed as

\[V = \sqrt{\frac{y}{\frac{m}{2k_BT}}}\]

where \(y\) is drawn from \(Gamma\left( \frac{3}{2},1 \right)\).
If we consider \(y' = yk_BT\), then

\[Y' \sim Gamma\left( \frac{3}{2},k_BT \right)\]

i.e. [\(\boxed{y'=E.}\)](https://en.wikipedia.org/wiki/Maxwell%E2%80%93Boltzmann_distribution#Distribution_for_the_energy)

Thus,

\[V = \sqrt{\frac{E}{\frac{1}{2}m}}\]

To simplify the code, the current implementation of the Maxwell distribution (based on an exponential distribution and a normal distribution) can be replaced by a Gamma distribution with shape parameter \(\dfrac{3}{2}\) and scale parameter \(\theta\). When \(\theta = k_BT\), it samples the energy from a Maxwell-Boltzmann distribution.
