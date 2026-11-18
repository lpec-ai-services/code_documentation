<!-- source: https://tripoli5.asnr.dev/documentation/latest-release/theory/scores/computing_moments.html -->

# Computing central statistical moments

## Definition of *central* statistical moments

The central statistical moment of order \(k\) of a random variable \(X\) is defined as

\[\mathbb{E}\left[ X^k \right] = \sum_{i} \left( x_i - \mu \right)^k p_i\]

where \(p_i\) is the probability to observe \(x_i\) and \(\mu = \mathbb{E}\Big[X\Big]\) is the expected value of \(X\).

One sees that the estimation of the moment of order \(k\) relies on the sum \(M_k = \Big( x_i - \mu \Big)^k\).

Thus, the \(k\)-th central moment can be computed in a naive way by summing the \(x_i^j\) up to the order \(k\).
Unfortunately, this can cause numerical stability issues.

Fortunately, algorithms exist to compute those orders in a clever way.

## Efficient numerical computation of statistical moments

To avoid numerical instability, one can update the sum \(M_k\) for each new observation, without storing the \(x_i^j\), before using \(M_k\) to derive statistical moments at the end of the simulation.

Doing this means updating \(M_k\) for each new observation, without knowledge of the detailed distribution.
Let’s consider two sets \(\mathcal{S}_1\) and \(\mathcal{S}_2\) of \(n_1\) and \(n_2\) observations respectively, where \(\mathcal{S_1}\cap \mathcal{S_2} = 0\).
Let’s consider that we have access to \(M_{k,\mathcal{S}_1}\) and \(M_{k,\mathcal{S}_2}\), the sum \(M_k\) for each set, and that we seek to compute \(M_{k,\mathcal{S}}\), where \(\mathcal{S} = \mathcal{S}_1 \cup \mathcal{S}_2\).

TRIPOLI-5 can compute the statistical moment of any score up to the order 4, using the formulas defined below.
The formulas below were taken from [Pébay 2008](https://doi.org/10.2172/1028931) and derived for the specific case in which \(n_2 = 1\) and \(n_1 = n-1\) (i.e., we add new observations one by one).

### First *raw* moment: average

For the first moment, one is generally interested in the *raw* moment, \(\mu\), since its central counterpart is always equal to 0.

The computation of the first two moments is here based on [Welford’s algorithm](https://en.wikipedia.org/wiki/Algorithms_for_calculating_variance#Welford's_online_algorithm).

For a update due to a single new observation \(y\)

\[\boxed{\tilde{\mu_n} = \tilde{\mu}_{n-1} + \frac{y-\tilde{\mu}_{n-1}}{n}}\]

where \(\tilde{\mu}_{n-1}\) is the estimate of the mean for \(n\) observations.

### Second central moment: the *sample variance*

The estimate of the second central moment (i.e., the *sample variance*) reads

From this, one can compute the *sample variance* using the following unbiased estimate

\[s^2 = \frac{M_{2,n}}{n}\]

where

\[M_{2,n} = \sum_{i=1}^n \Big( x_i - \mu \Big)^2.\]

However, the above variance estimate is biased if \(\mu\) is replaced by its estimate \(\tilde{\mu}_n\).
In this case, the unbiased estimate of the sample variance is

\[s^2 = \frac{M_2}{n-1}.\]

For a single new observation \(y\), the update formula is

\[\boxed{M_{2,n} = M_{2,n-1} + (y-\tilde{\mu}_{n-1})(y-\tilde{\mu}_n)}\]

### Third central moment

To compute the third central moment, one needs the following sum

\[M_3 = \sum_{i=1}^n \Big( x_i - \tilde{\mu}_n \Big)^3.\]

From this, one can estimate the *sample skewness* of the distribution from the estimates of the first two moments. TRIPOLI-5 relies on the one presented by [Doan and Seward](https://doi.org/10.1080/10691898.2011.11889611)

\[\text{Skewness} = \frac{n}{(n-1)(n-2)} \sum_{i=1}^n \Bigg( \frac{x_i - \tilde{\mu}_n}{s} \Bigg)^3 = \frac{n}{(n-1)(n-2)}\frac{M_{3,n}}{s^3}.\]

For a single new observation \(y\), the \(M_{3,n}\) update formula is

\[\boxed{M_{3,n} = M_{3,n-1} + \frac{(n-1)(n-2)}{n^2}\Big( y - \tilde{\mu}_{n-1} \Big)^3 - 3 M_{2,n-1} \frac{y - \tilde{\mu}_{n-1}}{n}}\]

## Fourth central moment

The estimate of the fourth central moment relies on the sum

\[M_{4,n} = \sum_{i=1}^n \Big( x_i - \tilde{\mu}_n \Big)^4.\]

From this, one can estimate the *excess kurtosis* (kurtosis minus 3) or *VoV* (variance of variance) of the distribution using the following unbiased estimates

\[\text{Kurtosis} = \frac{(n+1)n}{(n-1)(n-2)(n-3)}\frac{M_{4,n}}{s^4} - 3 \frac{(n-1)^2}{(n-2)(n-3)}.\]

\[\text{VoV} = \frac{M_4 - M_2^2}{n} + \frac{2 M_2^2}{n(n-1)}.\]

For a single new observation \(y\) the update formula is

\[\begin{split}\boxed{
\begin{split}
M_{4,n} = M_{4,n-1} &+ (n-1)(n^2 - 3 n + 3)\frac{\Big( y - \tilde{\mu}_{n-1} \Big)^4}{n^3}\\
&+ 6 M_{2,n-1} \frac{\Big(y - \tilde{\mu}_{n-1}\Big)^2}{n^2} \\
& -4 M_{3,n-1} \frac{y - \tilde{\mu}_{n-1}}{n}
\end{split}
}\end{split}\]
