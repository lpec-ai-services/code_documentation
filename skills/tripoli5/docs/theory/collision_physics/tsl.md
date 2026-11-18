<!-- source: https://tripoli5.asnr.dev/documentation/latest-release/theory/collision_physics/tsl.html -->

# Thermal scattering laws

## Introduction

The collisions between so-called “thermal” neutrons (energy of less than
a few electronvolts) and nuclei are affected by the thermal agitation
and, in some cases, by the presence of other surrounding nuclei
(*chemical bindings* and *cristallographic structure*, etc.) In the
purely free gas model, these effects are ignored but, for some
materials/applications, they can no longer be neglected.

Nuclides for which the neutron thermal scattering has the largest impact
are mainly moderator materials such as light water (1H in
H2O), heavy water (2H in D2O), carbon
in graphite or beryllium in metal. These effects can be modeled using a
complete representation provided by nuclear data: the thermal tables
\(S(\alpha, \beta)\).

The neutron thermal scattering can be decomposed into three
interactions:

- inelastic reaction: both energy and cosine are modified after the
  collision;
- incoherent elastic reaction (no change of energy);
- coherent elastic reaction (no change of energy) when the neutron
  wavelength is close to the space between atoms of the target
  material.

TRIPOLI-5 relies on nuclear data under the ACE format for the thermal
tables \(S(\alpha, \beta)\). In the module ACEConverter of TRIPOLI-5,
thermal ACE files are parsed and converted into Thermal Scattering Laws
readable by the following modules of TRIPOLI-5: DELOS and PATMOS.

## Inelastic scattering reaction

In the ACE format, the inelastic scattering reaction is always present
for any thermal isotope. By denoting \(E\) the incident energy, \(E'\) the
outgoing energy, \(\mu\) the cosine of the scattering angle and \(T\) the
temperature of the nuclide, the cross section of the inelastic
scattering can be represented as follows:

\[
\sigma(E\rightarrow E', \mu, T) = \frac{\sigma_b}{2k_BT} \sqrt{\frac{E}{E'}} \exp \left(-\frac{\beta}{2} \right) S \left(\alpha, \beta, T \right)\]

where \(\sigma_b\) corresponds to the characteristic bound cross section,
\(k_B\) denotes Boltzmann’s constant and \(S(\alpha, \beta, T)\) corresponds
to the “Thermal Scattering Law” containing data about chemical bindings
of the nuclide. In the term \(S(\alpha, \beta, T)\), \(\alpha\) refers to
the momentum transfer given by

\[\alpha = \frac{E+E' - 2\mu \sqrt{EE'}}{A_0k_BT}\]

and \(\beta\) to the
energy transfer given by

\[\beta = \frac{E'-E}{k_BT}\]

with \(A_0\) the
mass ratio between the incoming neutron and the target nuclide.

### Evaluation of the cross section

For the inelastic reaction, the evaluation of the cross section
\(\sigma(E, T)\) is performed as for any free gas reaction. For a given
nuclide at the temperature \(T\) and for this reaction, the thermal ACE
file provides a grid of energies \(E_i\) (with \(0 \leq i < N\), in MeV) and
an associated table of microscopic cross section \(\sigma_i\) (in barns).
The interpolated cross section of the inelastic reaction at the incoming
energy \(E\) such that \(E_i \leq E < E_{i+1}\) is then computed as follows:

\[
\sigma(E, T) = \sigma_{i,j} + f \times (\sigma_{i+1,j} - \sigma_{i,j})\]

where \(f\) corresponds to the interpolation fraction
\(f = \dfrac{E - E_i}{E_{i+1} - E_{i}}\).

### Sampling of the outgoing energy

In the ACE thermal files, three possibles modes are available:
equally-likely, skewed or continuous. This setting rules in particular
the sampling of the outgoing energy. The mode is deduced from the field
NXS(7) in the thermal ACE file by the following correspondence:

- if NXS(7)=0, the mode is set to equally-likely;
- if NXS(7)=1, the mode is set to skewed;
- if NXS(7)=2, the mode is set to continuous.

#### Equally-likely mode

The ACE format provides, for each index \(i \in [0, N]\), a table of
discrete outgoing energies \(E_{i,j}\) (\(0 \leq j < N_e\)).

In order to compute the outgoing energy distribution, the code performs
the following steps:

1. compute the index \(i\) such that \(E_i \leq E < E_{i+1}\)
2. sample the index \(j\) uniformly in the discrete range \([0, N_e[\)
3. compute the outgoing energy \(E'\) as:

\[E' = E_{i,j} + f \times (E_{i+1,j} - E_{i,j})\]

where \(f\)
corresponds to the interpolation fraction
\(f = \dfrac{E - E_i}{ E_{i+1} - E_{i}}\).

#### Skewed mode

The skewed mode is similar to the equally-likely mode, with a single
difference: only the step for the sampling of the index \(j\) differs. It
is performed as follows: each index \(k\) is sampled with a weight \(w_k\)

\[\begin{split}
w_k =
\begin{cases}
1 & \text{if } k = 0 \text{or } k = N_e-1\\
4 & \text{if } k = 1 \text{or } k = N_e-2\\
10 & \text{if } 2 \leq k < N_e-2\\
\end{cases}
\end{split}\]

#### Continuous mode

For each index \(i \in [0, N[\), the thermal ACE file provides the
tabulated cumulative density function \(c_{i,j}\) and the tabulated
probability density function \(p_{i,j}\) for the outgoing energy before
post-treatment (\(0 \leq j < M_i\)).

In order to compute the outgoing energy distribution, the code performs
the following steps:

1. compute the index \(i'\) such that \(E_i' \leq E < E_{i'+1}\)
2. sample the index \(i\) of the outgoing discrete energy: \(i'\) with a
   probability \(\frac{1}{2}\), \(i'+1\) otherwise
3. sample an index \(j\) such that \(c_{i,j} \leq \xi < c_{i,j+1}\), \(\xi\)
   being sampled from a uniform distribution in \([0, 1]\)
4. compute an intermediate value \(E''\) using

\[\begin{split}
E'' =
\begin{cases}
E_i + \dfrac{\sqrt{ \max(0, p_{i,j} p_{i,j+1} + 2 r (\xi -c_{i, j}))} - p_{i, j+1}}{r} &\text{if } r \ne 0 \\
E_i + \dfrac{\xi - c_{i,j}}{p_{i,j}} & \text{if } r = 0
\end{cases}
\end{split}\]

where
\(r=\dfrac{p_{i,j+1} - p_{i,j}}{E_{i+1} - E_i}\);

5. adjust the outgoing energy \(E'\) as:

\[\begin{split}
E' =
\begin{cases}
E'' \left( 2 \dfrac{E}{E_i} -1 \right) & \text{if } E''< \dfrac{1}{2} E_i \\
E'' + E - E_i & \text{otherwise}
\end{cases}\end{split}\]

### Sampling of the outgoing cosine

The sampling of the outgoing cosine also differs as a function of the
setting: equally-likely or skewed mode on one hand, continuous mode on
the other hand. In both cases, the sampling of the cosine is strongly
coupled with the sampling of the outgoing energy, since it re-uses
indices \(i\) and \(j\) computed at this previous step.

#### Equally-likely or skewed mode

The ACE format provides discrete outgoing cosine \(\mu_{i,j}\)
(\(0 \leq i < N\), \(0 \leq j < N_e\), \(0 \leq k < N_{\mu}\)).

The code performs the following steps:

1. sample the index \(k\) uniformly in the discrete range \([0, N_{\mu}[\)
2. compute the outgoing cosine \(\mu\) as follows:

\[
\mu = \mu_{i,j,k} + f \times (\mu_{i+1,j, k} - \mu_{i,j, k})
\]

with the interpolation fraction \(f\)
and indices \(i\) and \(j\) defined as [for the equally-likely
mode](#equally-like-energy-inelastic) or [for the skewed
mode](#skewed-energy-inelastic), during the sampling of the outgoing
energy.

#### Continuous mode

The ACE format provides discrete outgoing cosine \(\mu_{i,j,k}\)
(\(0 \leq i < N\), \(0 \leq j < M_i\), \(0 \leq k < N_{\mu}\)).

The code performs the following steps:

1. sample the index \(k\) uniformly in the discrete range \([0, N_{\mu}[\)
2. compute an intermediate cosine \(\mu'\) as:

\[
\mu' = \mu_{i,j,k} + f (\mu_{i,j+1,k} - \mu_{i,j,k})
\]

where
\(f = \dfrac{\xi - c_{i,j}}{c_{i,j+1} - c_{i, j}}\), with indices \(i\)
and \(j\) defined as [in the continuous
mode](#continuous-energy-inelastic).

3. apply a smearing procedure to compute the outgoing cosine \(\mu\):

\[
\mu = \mu' + \min(\mu' - \mu_{\mathrm{left}}, \mu' + \mu_{\mathrm{right}})
\times (\xi' - \dfrac{1}{2})
\]

with \(\xi'\) sampled uniformly
sampled in \([0, 1]\) and with

\[
\mu_{\mathrm{left}} = \mu_{i,j, k-1} + f (\mu_{i, j+1, k-1} - \mu_{i,j,
k-1})
\]

\[
\mu_{\mathrm{right}} = \mu_{i,j, k+1} + f (\mu_{i, j+1, k+1} - \mu_{i,j,
k+1})
\]

## Incoherent elastic reaction

The cross section of the incoherent elastic scattering can be
represented as follows:

\[
\sigma(E\rightarrow E',\mu,T) = \frac{\sigma_b}{2} exp \left[-\dfrac{2E(1-\mu)}{A_0 k_BT} \sum \limits_i \omega_i \lambda_i \right]\]

where \(\sigma_b\) corresponds to the characteristic bound cross section,
\(k_B\) to Boltzmann’s constant, \(A_0\) to the mass ratio between the
incoming neutron and the target nuclide, \(\lambda_i\) to values related
to quantum modes and \(\omega_i\) to weights related to quantum modes.

The outgoing energy \(E'\) is preserved during this interaction, i.e.
\(E'=E\).

### Evaluation of the cross section

For the incoherent elastic reaction, the cross section is trivially
computed as [the inelastic scattering cross section](#inelastic-xs),
i.e. with a linear-linear interpolation. For a given nuclide at a given
temperature, the ACE format provides a specific energy grid \(E_i\) and
associated microscopic cross sections \(\sigma_i\) for this interaction.

### Sampling of the outgoing cosine

In order to compute the outgoing cosine, the code performs the following
steps:

1. compute the index \(i\) such that \(E_i < E \leq E_{i+1}\) and the
   fraction \(f = \dfrac{E - E_i}{ E_{i+1} - E_{i}}\)
2. sample the index \(j\) in a equiprobable way (all angular bins have
   the same weight)
3. compute an intermediate cosine \(\mu'\) as:

\[
\mu' = \mu_{i,j} + f (\mu_{i+1,j} - \mu_{i,j})
\]

4. apply a smearing procedure to compute the outgoing cosine \(\mu\):

\[
\mu = \mu' + \min(\mu' - \mu_{\mathrm{left}}, \mu' + \mu_{\mathrm{right}})
\times (\xi' - \dfrac{1}{2})
\]

with \(\xi'\) sampled
uniformly sampled in \([0, 1]\) and with

\[
\mu_{\mathrm{left}} = \mu_{i,j-1} + f \times (\mu_{i+1, j-1} - \mu_{i,
j-1})
\]

\[
\mu_{\mathrm{right}} = \mu_{i,j+1} + f \times (\mu_{i+1, j-1} - \mu_{i,
j+1})
\]

## Coherent elastic reaction

The coherent elastic scattering from a powdered crystalline material
(typically, carbon in graphite or beryllium in metal) may be represented
as follows:

\[
\sigma \left(E\rightarrow E',\mu,T \right) = \frac{1}{2\pi E} \sum
\limits_{E_i<E} s_i(T) \delta(E-E') \delta \left[\mu - \left(\frac{E-2E_i}{E}
\right) \right]\]

where \(E_i\) correspond to energies of the Bragg
edges and \(s_i(T)\) are proportional to the structure factors.

As for the incoherent elastic reaction, the energy is preserved during
this interaction.

### Evaluation of the cross section

For a given thermal isotope at temperature \(T\), the thermal ACE files
provides the Bragg energies \(E_i\) (\(0 \leq i < N)\) and the cumulative
structure factors \(c_i = \sum \limits_{0 \leq j \leq i} s_j\). The cross
section of the coherent elastic scattering interaction at the incoming
energy \(E\) is computed as follows:

\[
\sigma(E, T) = \frac{1}{E} \sum \limits_{E_i<E} s_i\]

Contrary to incoherent elastic or inelastic scattering interactions,
this section is not interpolated in a linear-linear way.

### Sampling of the outgoing cosine

In order to compute the outgoing cosine, the code performs the following
steps:

1. compute the index \(k\) such that \(E_k \leq E < E_{k+1}\)
2. sample an index \(i\), each index \(j\) being sampled with a probability
   \(p_j\)

\[
p_j = \dfrac{s_j}{\sum \limits_{j'=0}^{k} s_{j'}}\]

3. compute the outgoing cosine \(\mu\) as follows:

\[
\mu = 1 - 2 \dfrac{E_i}{E}\]

## Integration of thermal scattering laws in TRIPOLI-5

After the implementation of i) the evaluation of the microscopic cross
section of thermal interactions at a given energy ii) the sampling of
the joint angle/energy distributions for the [inelastic
reaction](#inelastic) and iii) the sampling of the cosine distribution
for the [incoherent](#incoherent-elastic) and
[coherent](#coherent-elastic) elastic scattering reactions, the complete
integration of the treatment of the neutron thermal scattering requires
additional steps.

It is indeed necessary to replace the purely “free gas” elastic reaction
(identified by MT 2 in ENDF rules) by the new thermal interactions for
particles with an incoming energy \(E\) under a given threshold \(E_s\). So
far, in TRIPOLI-5, we have chosen to set \(E_s\) as the maximal value of
the energy grid of the inelastic reaction (NB: in the future, this
threshold could become a user setting parameter). Thus, the total cross
section of a thermal isotope at a given temperature \(T\) and incoming
energy \(E\) has to be corrected as follows:

\[\begin{split}
\sigma_{t}'(E, T) =
\begin{cases}
\sigma_{t}(E, T) + \sigma_{TSL}(E, T) - \sigma_{MT=2}(E, T) & \text{if } E < E_{s} \\
\sigma_{t}(E, T) & \text{ if } E \geq E_{s}
\end{cases}\end{split}\]

where \(\sigma_{TSL}(E, T)\) corresponds to the sum of
cross section of thermal interactions.

In addition, it is necessary to adjust the calculation of the majorant
of the cross section by taking the thermal interactions into account, in
order to support the delta-tracking simulation with thermal isotopes.
