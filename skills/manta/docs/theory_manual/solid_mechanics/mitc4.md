<!-- source: https://manta-project.gitlab.io/manta/theory_manual/solid_mechanics/mitc4.html -->

# MITC4 shell (*deprecated doc*)

## Some elements of theory

### Basis

The following basis are considered at each point of the membrane:

- The covariant basis on the initial configuration:

\[\mathbf{G}_i=\frac{\partial \mathbf{X}}{\partial r_i},\: i\in\lbrace0,1,2\rbrace\]

- An orthonormal basis constructed from the covariant basis on the
  initial configuration:

\[\mathbf{T}_2=\frac{\mathbf{G}_0\times\mathbf{G}_1}{||\mathbf{G}_0\times\mathbf{G}_1||}\]

\[\mathbf{T}_0=\frac{\mathbf{G}_0}{||\mathbf{G}_0||}\]

\[\mathbf{T}_1=\mathbf{T}_2\times\mathbf{T}_0\]

- The covariant basis on the current configuration:

\[\mathbf{g}_i=\frac{\partial \mathbf{x}}{\partial r_i},\: i\in\lbrace0,1,2\rbrace\]

For the non-orthonormal basis, their dual counterparts
\(\left\{\mathbf{G}^i\right\}_{i\in\{0,1,2\}}\) and
\(\left\{\mathbf{g}^i\right\}_{i\in\{0,1,2\}}\) are also considered.

### Strain

The Green-Lagrange strain tensor covariant components are computed:

\[\boldsymbol{\varepsilon}=\tilde{\varepsilon}_{ij}\mathbf{G}^i\otimes\mathbf{G}^j\]

using the following formula and some specific treatment to prevent
transverse shear locking:

\[\tilde{\varepsilon}_{ij}=\frac{1}{2}\left(\mathbf{g}_i\cdot\mathbf{g}_j-\mathbf{G}_i\cdot\mathbf{G}_j\right)\]

Then its components in the orthonromal basis are computed:

\[\boldsymbol{\varepsilon}=\bar{\varepsilon}_{ij}\mathbf{T}_i\otimes\mathbf{T}_j\]

\[\bar{\varepsilon}_{ij}=\left(\mathbf{T}_i\cdot\mathbf{G}^k\right)\tilde{\varepsilon}_{kl}\left(\mathbf{G}^l\cdot\mathbf{T}_j\right)\]

### Elasticity Matrix and stress

With \(\mathbf{S}=\bar{S}^{ij}\mathbf{T}_i\otimes\mathbf{T}_j\) the
second Piola-Kirchhoff stress tensor, the plane-stress condition impose
that \(\bar{S}^{22}=0\). For a simple Saint Venant-Kirchhoff law, in
Voigt form:

\[\begin{split}\begin{bmatrix}
\bar{S}^{00}\\
\bar{S}^{11}\\
\bar{S}^{01}\\
\bar{S}^{02}\\
\bar{S}^{12}\\
\bar{S}^{22}
\end{bmatrix}
=
\begin{bmatrix}
\bar{S}^{00}\\
\bar{S}^{11}\\
\bar{S}^{01}\\
\bar{S}^{02}\\
\bar{S}^{12}\\
0
\end{bmatrix}
=
\begin{bmatrix}
\mathbf{C}_{aa}&\mathbf{C}_{ab}\\
\mathbf{C}_{ba}&C_{bb}
\end{bmatrix}
\begin{bmatrix}
\bar{\varepsilon}_{00}\\
\bar{\varepsilon}_{11}\\
\bar{\varepsilon}_{01}\\
\bar{\varepsilon}_{02}\\
\bar{\varepsilon}_{12}\\
\bar{\varepsilon}_{22}
\end{bmatrix}\end{split}\]

where \(\mathbf{C}_{aa}\f\), \(\mathbf{C}_{ab}\) and
\(\mathbf{C}_{ba}\) are respectively 5x5, 5x1 and 1x5 submatrices of
the elasticity matrix. Then \(\bar{\varepsilon}_{22}\) is eliminated
using the sixth equation:

\[\begin{split}\begin{bmatrix}
\bar{S}^{00}\\
\bar{S}^{11}\\
\bar{S}^{01}\\
\bar{S}^{02}\\
\bar{S}^{12}
\end{bmatrix}
=
\left(\mathbf{C}_{aa}-\frac{1}{C_{bb}}\mathbf{C}_{ab}\mathbf{C}_{ba}\right)
\begin{bmatrix}
\bar{\varepsilon}_{00}\\
\bar{\varepsilon}_{11}\\
\bar{\varepsilon}_{01}\\
\bar{\varepsilon}_{02}\\
\bar{\varepsilon}_{12}
\end{bmatrix}\end{split}\]

Then the components of the second Piola-Kirchhoff stress tensor in the
covariant basis of the initial configuration is computed:

\[\boldsymbol{S}=\tilde{S}^{ij}\mathbf{G}_i\otimes\mathbf{G}_j\]

\[\tilde{S}^{ij}=\left(\mathbf{G}^i\cdot\mathbf{T}_k\right)\bar{G}^{kl}\left(\mathbf{T}_l\cdot\mathbf{G}^j\right)\]

The components of second Piola-Kirchhoff stress tensor in the covariant
basis of the initial configuration are the same as the components of the
Kirchhoff stress tensor in the covariant basis of the current
configuration. Then the Cauchy stress tensor components in the covariant
basis of the current configuration are given by:

\[\boldsymbol{\sigma}=\tilde{\sigma}^{ij}\mathbf{g}_i\otimes\mathbf{g}_j\]

\[\tilde{\sigma}^{ij}=\frac{1}{det(\mathbf{F})}\tilde{S}^{ij}\]

where \(\mathbf{F}=\mathbf{g}_i\otimes\mathbf{G}^i\) is the gradient
of the transformation.

### Virtual power

The virtual density of power is:

\[P=\tilde{\sigma}^{ij}\tilde{\delta\varepsilon}_{ij}\]

where \(\tilde{\delta\varepsilon}_{ij}\) are the components of the
virtual linearized strain tensor in the covariant basis of the current
configuration:

\[\mathbf{\delta\varepsilon}=\tilde{\delta\varepsilon}_{ij}\mathbf{g}^i\otimes\mathbf{g}^j\]

These components are computed using the following formula and some
specific treatment to prevent transverse shear locking:

\[\tilde{\delta\varepsilon}_{ij}=\frac{1}{2}\left(\mathbf{g}_i\cdot\frac{\partial\mathbf{\delta u}}{\partial r_j}+\frac{\partial\mathbf{\delta u}}{\partial r_i}\cdot\mathbf{g}_j\right)\]

## Numerical application

Todo

Write here a commented example !
