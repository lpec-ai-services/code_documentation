# Key equations

Transcribed in LaTeX from the rendered pages of the sources, because the extracted text garbles symbols. **P** = physics, **M** = methods. Page numbers are printed pages of *Les méthodes de la neutronique* (CEA, 2013). Equation numbers are those of the source.

Notation: $\psi(\vec r,E,\vec\Omega,t)$ angular flux; $\phi=\int_{4\pi}\psi\,d\Omega$ scalar flux; $N_k$ concentration of nuclide $k$; $\sigma$ microscopic and $\Sigma=\sum_k N_k\sigma_k$ macroscopic cross sections; $\nu$ neutrons per fission; $\chi$ emission spectra.

---

## P1 — Boltzmann equation, time-dependent (eq. 1, p. 47)

$$
\begin{aligned}
\frac{1}{v}\frac{\partial\psi(\vec r,E,\vec\Omega,t)}{\partial t} ={}& -\vec\Omega\cdot\vec\nabla\psi(\vec r,E,\vec\Omega,t) - \sum_k N_k(\vec r,t)\,\sigma_k(E)\,\psi(\vec r,E,\vec\Omega,t)\\
&+ \sum_k N_k(\vec r,t)\int_0^\infty dE'\int_{4\pi} d\vec\Omega'\,\sigma_{s,k}(E'\to E,\vec\Omega'\to\vec\Omega)\,\psi(\vec r,E',\vec\Omega',t)\\
&+ \frac{1}{4\pi}\sum_k N_k(\vec r,t)\int_0^\infty dE'\,\nu_{p,k}(E')\,\sigma_{f,k}(E')\,\chi_{p,k}(E'\to E)\,\phi(\vec r,E',t)\\
&+ \frac{1}{4\pi}\sum_k \nu_{p,fs,k}\,\lambda_{fs,k}\,N_k(\vec r,t)\,\chi_{p,fs,k}(E)
 + \frac{1}{4\pi}\sum_k \lambda_{d,k}\,N_k(\vec r,t)\,\chi_{d,k}(E) + S_{ext}(\vec r,E,\vec\Omega,t)
\end{aligned}
$$

Terms, in order: streaming, removal (total collision), scattering, prompt neutrons from induced fission, prompt neutrons from spontaneous fission ($\lambda_{fs,k}$ spontaneous-fission decay constant), delayed neutrons ($\lambda_{d,k}$ partial decay constant through the (β⁻,n) channel), external source. Further sources (p. 47): (α,n) with yield $\zeta^{(k)}_{(\alpha,n)}(E)$, and photonuclear reactions, which couple neutron and gamma transport.

## P2 — Generalized Bateman equations (eq. 2, p. 49)

$$
\frac{dN_k(\vec r,t)}{dt} = \sum_{m\neq k}\varsigma_{k\leftarrow m}(\vec r,t)\,N_m(\vec r,t) + \sum_{m\neq k}\lambda_{k\leftarrow m}N_m(\vec r,t) - \lambda_k N_k(\vec r,t) - \varsigma_k(\vec r,t)\,N_k(\vec r,t)
$$

with microscopic reaction rates
$$
\varsigma_{k\leftarrow m}(\vec r,t)=\sum_q\int_0^\infty \sigma_{q,k\leftarrow m}(E)\,\phi(\vec r,E,t)\,dE,\qquad
\varsigma_k(\vec r,t)=\sum_q\int_0^\infty \sigma_{q,k}(E)\,\phi(\vec r,E,t)\,dE .
$$
P1 and P2 are coupled through $\phi$ and $N_k$, and together form a closed system.

## P3 — Stationary integral transport equation (eq. 2, p. 56)

$$
\begin{aligned}
\psi(\vec r,E,\vec\Omega) ={}& \int_0^\infty ds\,\exp\!\Big(-\!\int_0^s \Sigma(\vec r-s'\vec\Omega,E)\,ds'\Big)\,S(\vec r-s\vec\Omega,E,\vec\Omega)\\
&+\int_0^\infty ds\,\exp\!\Big(-\!\int_0^s \Sigma(\vec r-s'\vec\Omega,E)\,ds'\Big)\int_0^\infty dE'\int_{4\pi} d\vec\Omega'\,\Sigma_s(\vec r-s\vec\Omega,E'\to E,\vec\Omega'\to\vec\Omega)\,\psi(\vec r-s\vec\Omega,E',\vec\Omega')
\end{aligned}
$$
Collision density $\zeta=\Sigma\,\psi$. In operator form $\zeta = TC\zeta + TS$, with $T$ the displacement (transport) operator and $C$ the collision operator (p. 57). This is the starting point of Monte Carlo (M4).

## P4 — Critical equation and k_eff (eq. 3, p. 56)

$$
\vec\Omega\cdot\vec\nabla\psi(\vec r,E,\vec\Omega) + \sum_k N_k(\vec r)\sigma_k(E)\psi(\vec r,E,\vec\Omega)
= \sum_k N_k(\vec r)\int_0^\infty\!dE'\!\int_{4\pi}\!d\vec\Omega'\,\sigma_{s,k}(E'\to E,\vec\Omega'\to\vec\Omega)\psi(\vec r,E',\vec\Omega')
+ \frac{1}{k_{eff}}\frac{1}{4\pi}\sum_k N_k(\vec r)\int_0^\infty\!dE'\,\nu_{t,k}(E')\sigma_{f,k}(E')\chi_{p,k}(E'\to E)\,\phi(\vec r,E')
$$
$k_{eff}$ is the largest eigenvalue, and $\psi$ the associated fundamental mode ("critical flux"). It equals the ratio of neutrons in generation $i+1$ to generation $i$.

## P5 — Delayed-neutron precursors (eqs. 5–6, p. 59)

For a precursor $p$ (fissile nuclides $k\in F$):
$$
\frac{dC_p(\vec r,t)}{dt} = -\lambda_{d,p}C_p(\vec r,t) + \sum_{k\in F}N_k(\vec r)\,\beta_p^{(k)}\int_0^\infty dE'\,\nu_{t,k}(E')\sigma_{f,k}(E')\phi(\vec r,E',t)
$$
Grouped into families $(k,i)$ (usually 6 or 8 per fissile nuclide):
$$
\frac{dC_i^{(k)}(\vec r,t)}{dt} = -\lambda_i^{(k)}C_i^{(k)}(\vec r,t) + N_k(\vec r)\,\beta_i^{(k)}\int_0^\infty dE'\,\nu_{t,k}(E')\sigma_{f,k}(E')\phi(\vec r,E',t)
$$

## P6 — Point kinetics, Nordheim equation, delayed-neutron data (pp. 118–119)

With neutron lifetime $\ell$ and $I$ families (eq. 16):
$$
\frac{dn}{dt}=\frac{k_{eff}(1-\beta)-1}{\ell}\,n(t)+\sum_i\lambda_iC_i(t),\qquad
\frac{dC_i}{dt}=\frac{k_{eff}\beta_i}{\ell}\,n(t)-\lambda_iC_i(t)
$$
With reactivity $\rho$, $k_{eff}=1/(1-\rho)$ and $\ell^*=\ell/k_{eff}$ (eq. 17):
$$
\frac{dn}{dt}=\frac{\rho-\beta}{\ell^*}\,n(t)+\sum_i\lambda_iC_i(t),\qquad
\frac{dC_i}{dt}=\frac{\beta_i}{\ell^*}\,n(t)-\lambda_iC_i(t)
$$
Solutions $n(t)=\sum_{j=1}^{I+1}A_j e^{\omega_j t}$, where the $\omega_j$ are roots of the **Nordheim equation** (eq. 18):
$$
\rho=\ell^*\omega+\sum_i\frac{\beta_i\,\omega}{\omega+\lambda_i}
$$
$I$ roots are negative (transients). The remaining root, with the sign of $\rho$, is the asymptotic mode.
- Large reactivity ($\rho>\beta$, prompt critical): $\omega_0\simeq(\rho-\beta)/\ell^*$, period $T_0\simeq \ell^*/(\rho-\beta)=\ell/(k_{eff}(1-\beta)-1)$.
- Small reactivity ($\rho<\beta$): $\omega_0\simeq\rho/\tau$, with $\tau=\ell^*+\sum_i\beta_i/\lambda_i\simeq\sum_i\beta_i/\lambda_i$ ($\approx 0.0866$ s for U-235), and $T_0\simeq\tau/\rho\simeq\tau/(k_{eff}-1)$.

U-235 fission, 8 groups, JEFF-3.1 (table 17, p. 118):

| Group | λᵢ (s⁻¹) | τᵢ = 1/λᵢ (s) | βᵢ (pcm) |
|---|---|---|---|
| 1 | 1.247e-2 | 80.21 | 22 |
| 2 | 2.829e-2 | 35.35 | 102 |
| 3 | 4.252e-2 | 23.52 | 61 |
| 4 | 1.330e-1 | 7.516 | 131 |
| 5 | 2.925e-1 | 3.419 | 220 |
| 6 | 6.665e-1 | 1.500 | 60 |
| 7 | 1.635 | 0.6117 | 54 |
| 8 | 3.555 | 0.2813 | 15 |
| Mean / total | 7.681e-2 | 13.02 | 665 |

---

## M1 — Multigroup equations and cross sections (eqs. 1–3, p. 65)

Stationary, with external source, group $g$:
$$
\vec\Omega\cdot\vec\nabla\psi^g(\vec r,\vec\Omega)+\sum_k N_k(\vec r)\sigma_k^g\psi^g(\vec r,\vec\Omega)
=\sum_k N_k(\vec r)\sum_{g'}\int_{4\pi}d\vec\Omega'\,\sigma_{s,k}(g'\to g,\vec\Omega'\to\vec\Omega)\,\psi^{g'}(\vec r,\vec\Omega')+S^g_{ext}(\vec r,\vec\Omega)
$$
Flux-weighted group cross section, and reaction-rate preservation in lethargy $u$:
$$
\sigma^g(\vec r)=\frac{\int_g\sigma(E)\phi(\vec r,E)\,dE}{\int_g\phi(\vec r,E)\,dE},\qquad
\sigma_q^g(\vec r)\,\phi^g(\vec r)=\int_g\sigma_q(u)\,\phi(\vec r,u)\,du
$$
Using the true flux $\phi(\vec r,u)$ gives **self-shielded** cross sections, which depend on space. Using a known weighting spectrum $\phi_w(u)$ gives **infinite-dilution** cross sections. Self-shielding models (equivalence, subgroups) bridge the two.

## M2 — PN, SPN and diffusion (pp. 75)

1D PN, with $\psi^{1D}(z,\mu)=\sum_n\psi_n^{1D}(z)P_n(\mu)$, $\Sigma_{rn}=\Sigma-\Sigma_{sn}$ and $\Sigma_s(\vec r,\vec\Omega'\cdot\vec\Omega)=\sum_n(2n+1)\Sigma_{sn}(\vec r)P_n(\mu)$:
$$
\frac{d\psi_1}{dz}+\Sigma_{r0}\psi_0=S,\quad
\frac{n+1}{2n+1}\frac{d\psi_{n+1}}{dz}+\Sigma_{rn}\psi_n+\frac{n}{2n+1}\frac{d\psi_{n-1}}{dz}=0\ (1\le n<N),\quad
\Sigma_{rN}\psi_N+\frac{N}{2N+1}\frac{d\psi_{N-1}}{dz}=0
$$
**SPN** (3D extension: even harmonics scalar, odd harmonics vectors $\vec\psi_n$):
$$
\begin{cases}
\vec\nabla\cdot\vec\psi_1+\Sigma_{r0}\psi_0=S\\[2pt]
\frac{n+1}{2n+1}\vec\nabla\psi_{n+1}+\Sigma_{rn}\vec\psi_n+\frac{n}{2n+1}\vec\nabla\psi_{n-1}=\vec 0 & n\ \text{odd}\\[2pt]
\frac{n+1}{2n+1}\vec\nabla\cdot\vec\psi_{n+1}+\Sigma_{rn}\psi_n+\frac{n}{2n+1}\vec\nabla\cdot\vec\psi_{n-1}=0 & n\ \text{even}\\[2pt]
\Sigma_{rN}\vec\psi_N+\frac{N}{2N+1}\vec\nabla\psi_{N-1}=\vec 0
\end{cases}
$$
Order 1 gives back diffusion. SPN converges to transport in 1D slab and infinite homogeneous media, but not in general.

**Diffusion**: truncate the angular expansion after two terms (isotropic sources), $\psi^g(\vec r,\vec\Omega)\cong\phi^g(\vec r)+\vec J^g(\vec r)\cdot\vec\Omega$ (eq. 14, written as in the source). This leads to Fick's law and the diffusion equation (p. 76).

## M3 — Method of characteristics (eqs. 23–30, p. 83)

One group: $\vec\Omega\cdot\vec\nabla\psi+\Sigma\psi=q$. Domain split into regions $D_i$ with constant $\Sigma_i$, $q_i(\vec\Omega)$; angular quadrature $\int_{4\pi}f(\vec\Omega)d\vec\Omega=\sum_n\omega_nf(\vec\Omega_n)$. Along a characteristic line $k$ ($\vec r=\vec r_{0k}+s\vec\Omega$):
$$
\frac{d\psi(\vec r_{0k}+s\vec\Omega,\vec\Omega)}{ds}+\Sigma(\vec r_{0k}+s\vec\Omega)\,\psi=q(\vec r_{0k}+s\vec\Omega,\vec\Omega)
$$
Inside region $i$:
$$
\psi(\vec r_{0k}+s\vec\Omega,\vec\Omega)=\psi(\vec r_{0k}+s'\vec\Omega,\vec\Omega)\,e^{-\Sigma_i(s-s')}+\frac{q_i(\vec\Omega)}{\Sigma_i}\big(1-e^{-\Sigma_i(s-s')}\big)
$$
**Transmission equation** across a chord of length $l_i^k$:
$$\psi_{out}=\psi_{in}\,e^{-\Sigma_il_i^k}+\frac{1-e^{-\Sigma_il_i^k}}{\Sigma_i}\,q_i(\vec\Omega)$$
It is followed by a balance equation for the region-average flux (p. 84).

## M4 — Monte Carlo sampling laws (eqs. 15–20, p. 92)

Source point $P_0$ and successive events $P_i$, sampled from the transport kernel $K$:
$$
f_0(P_0)=\frac{S_0(P_0)}{\int_{DS}S_0(P_0)\,dP_0},\qquad
f_i(P_i)=\frac{K(P_{i-1}\to P_i)}{\int_D K(P_{i-1}\to P_i)\,dP_i}
$$
Path length in a homogeneous medium, and its sampling ($\xi$ uniform on [0,1)):
$$
f(s)=\Sigma(E)\,e^{-\Sigma(E)s},\qquad s=-\frac{1}{\Sigma(E)}\ln(1-\xi)
$$
Collision kernel for a mixture of nuclides $j$ and reactions $i$:
$$
C(\vec r,E'\to E,\vec\Omega'\to\vec\Omega)=\sum_j\frac{\Sigma_j(\vec r,E')}{\Sigma(\vec r,E')}\sum_i\left[\frac{\sigma_{sj}(E')}{\sigma_j(E')}\right]\frac{\sigma_{ij}(E')}{\sigma_{sj}(E')}\,\nu_{ij}\,f_{ij}(E'\to E,\vec\Omega'\to\vec\Omega)
$$
This samples, in order: the nuclide, the reaction, then the multiplicity $\nu_{ij}$ and the outgoing energy/direction law $f_{ij}$.

## M5 — Power iteration and dominance ratio (eq. 4, p. 56; eqs. 23–24, p. 99)

Deterministic power iteration, fission source from iteration $n-1$:
$$
\vec\Omega\cdot\vec\nabla\psi^{(n)}+\sum_kN_k\sigma_k\psi^{(n)}=\sum_kN_k\!\int\!\!\int\sigma_{s,k}\,\psi^{(n)}+\frac{1}{k_{eff}^{(n-1)}}\frac{1}{4\pi}\sum_kN_k\!\int_0^\infty\!dE'\,\nu_{t,k}\sigma_{f,k}\chi_{p,k}(E'\to E)\,\phi^{(n-1)}
$$
In operator form $M\phi=\frac1{k}F\phi$, with the update (fig. 41) $k^{(n+1)}=\dfrac{\int Q^{(n+1)}d^3r}{\frac{1}{k^{(n)}}\int Q^{(n)}d^3r}$. Monte Carlo does the same with successive batches (cycles).

Convergence, limited to the first harmonic:
$$
k_{eff}^{(n+1)}\approx k_1\left[1+c\left(\frac{k_2}{k_1}\right)^n\left(\frac{k_2}{k_1}-1\right)\right],\qquad
\phi^{(n+1)}\propto u_1+c\left(\frac{k_2}{k_1}\right)^{n+1}
$$
The dominance ratio $k_2/k_1$ is close to 1 in large, loosely coupled cores such as PWRs, so convergence is slow. k_eff converges faster than the source and flux distribution.
