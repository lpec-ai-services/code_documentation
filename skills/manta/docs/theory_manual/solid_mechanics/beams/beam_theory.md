<!-- source: https://manta-project.gitlab.io/manta/theory_manual/solid_mechanics/beams/beam_theory.html -->

# Beam theory - Euler-Bernoulli and Timoshenko

The following documentation presents the general theory of beams, notably the
**Euler-Bernoulli** and **Timoshenko** models.

For ease of comprehension, data specific to each model is presented in relevant
tabs:

Euler-Bernoulli

*Information specific to Euler-Bernoulli model*

Timoshenko

*Information specific to Timoshenko model*

## Introduction

A beam is a structure where two of its geometric dimensions are negligible
compared to the third. As such, beams are represented as the conjunction of:

- A **cross-section** that carries the geometric information over two dimensions that are indeed neglected ;
- A **neutral axis** that represents the overall displacement of the beam, centered at the center of inertia of the cross-section.

As the **neutral axis** is positioned at the **center of inertia**, one has
\(\int_S y dS = 0\), \(\int_S z dS = 0\) and \(\int_S yz dS = 0\) ;
where \(S\) is the cross-section of the beam, and \(y\) and \(z\)
are the coordinates along the cross-section.

In beam theory, the following hypotheses are made:

- The cross-section is **non-deformable** ;
- The transverse displacements are **constant** over the cross-section ;

Euler-Bernoulli

Additionally, in **Euler-Bernoulli** beam theory, these hypotheses are added:

- The cross-section's plane stays **orthogonal** to the beam's neutral axis,
  which translates into the neglection of shear effects ;
- The **inertial effects due to the rotation** of the cross-section are
  neglected when compared to the inertial terms due to translation.

Note

**Euler-Bernoulli** beam theory includes an additional hypothesis when compared
to **Timoshenko** beam theory. As such,
Euler-Bernoulli beam is but a **simplification Timoshenko beam**.

Timoshenko

(*Intentionally left blank*)

These hypotheses allow the description of the movement of any point of the beam,
wherever it may be on the cross-section, as a function of the displacement of
a point on the neutral axis.

The geometric support of the element is a `seg2`.

In 2D, each node carries **three** degrees of freedom: 2 for **translation**
\((u, v)\) and 1 for **rotation** \(\theta_{z}\).

In 3D, each node carries **six** degrees of freedom: 3 for **translation**
\((u, v, w)\) and 3 for **rotation** \((\theta_{x}, \theta_{y}, \theta_{z})\).

![figure](https://manta-project.gitlab.io/manta/_images/beam_dof.svg)

Fig. 116 Degrees of freedom of a beam element

Within this documentation, the degrees of freedom will be written as such:

\[ \begin{align}\begin{aligned}\begin{split}\boldsymbol{U^{\transpose{}}}(x,t) = (u(x,t), v(x,t), w(x,t), \theta_x(x,t), \theta_y(x,t), \theta_z(x,t))\\\end{split}\\\boldsymbol{u}_e^{\transpose{}} = (u_{1}, v_{1}, w_{1}, \theta_{x,1}, \theta_{y,1}, \theta_{z,1}, u_{2}, v_{2}, w_{2}, \theta_{x,2}, \theta_{y,2}, \theta_{z,2})\end{aligned}\end{align} \]

and all equations will be written such that the neutral axis is the \((Ox)\)
axis. Without any loss of generality, all equations will be written in the local
coordinate system.

For ease of readability, dependence in \(x\) and \(t\) (space and time
respectively) might be omitted.

## Local coordinate system

Let us determine the expression of the local coordinate system as a function of
the global coordinate system.

Within this documentation, the vectors making up the local coordinate system
will be written as such:

\[(\boldsymbol{e_u}, \boldsymbol{e_v}, \boldsymbol{e_w})\]

\(\boldsymbol{e_u}\) is aligned with the direction of the beam element,
meaning that it can be written as a function of the position vectors of both nodes.

Noting \(O\) the origin of **global** coordinate system, and \(M_1\) and
\(M_2\) the nodes of the element, one has:

\[\boldsymbol{e_u} = \frac{\boldsymbol{M_1M_2}}{\| \boldsymbol{M_1M_2} \|}\]

such as \(\| \boldsymbol{e_u} \| = 1\).

Following that, \(\boldsymbol{e_v}\) and \(\boldsymbol{e_w}\) define
the plane that is orthogonal to the first vector, i.e. the cross-section plane.

\(\boldsymbol{e_v}\) can be chosen arbitrarily, as long as
\(\| \boldsymbol{e_v} \| = 1\) and \(\boldsymbol{e_u}\cdot \boldsymbol{e_v} = 0\).

Finally, \(\boldsymbol{e_w}\) is constructed in such a way that the **local**
coordinate system constitutes a **direct basis**, i.e.:

\[\boldsymbol{e_w} = \frac{\boldsymbol{e_u} \times \boldsymbol{e_v}}{\| \boldsymbol{e_u} \times \boldsymbol{e_v} \|}\]

Finally, one can assemble the **transition matrix** from the local coordinate
system to the global coordinate system, which is a matrix that describes a
rotation and which can simply be written as the coordinates of the local system
vectors in the global coordinate system.

\[\begin{split}\boldsymbol{P} = \begin{pmatrix}
e_{u, x} & e_{v, x} & e_{w, x} \\
e_{u, y} & e_{v, y} & e_{w, y} \\
e_{u, z} & e_{v, z} & e_{w, z} \\
\end{pmatrix}\end{split}\]

where \(e_{i, j} = \boldsymbol{e}_i \cdot \boldsymbol{e}_j\), which immediately
gives:

\[\begin{split}\begin{pmatrix}
x_{global} \\
y_{global} \\
z_{global}
\end{pmatrix} = \boldsymbol{P} \begin{pmatrix}
x_{local} \\
y_{local} \\
z_{local}
\end{pmatrix}\end{split}\]

The same holds for rotations and for either node in such a way that one can
link the DOFs expressed in the local and global coordinate system:

\[\begin{split}\boldsymbol{u}_{e, global} = \begin{pmatrix}
\boldsymbol{P} & 0 & 0 & 0\\
0 & \boldsymbol{P} & 0 & 0\\
0 & 0 & \boldsymbol{P} & 0\\
0 & 0 & 0 & \boldsymbol{P}\\
\end{pmatrix} \boldsymbol{u}_{e, local} = \boldsymbol{\tilde{P}} \boldsymbol{u}_{e, local}\end{split}\]

In \(2D\), the following points differ:

- In addition of the properties that satisfy its \(3D\) counterpart, \(\boldsymbol{e_v}\) is chosen such as \((\boldsymbol{e_u}, \boldsymbol{e_v})\) is a direct basis ;
- There is no \(\boldsymbol{e_w}\) vector as the beam exist only in a \(2D\) plane ;
- \(\boldsymbol{P}\) and \(\boldsymbol{\tilde{P}}\) satisfy:

(283)\[\begin{split}\boldsymbol{P} & = \begin{pmatrix}
e_{u, x} & e_{v, x} \\
e_{u, y} & e_{v, y} \\
\end{pmatrix} \\
\boldsymbol{u}_{e, global} & = \begin{pmatrix}
e_{u, x} & e_{v, x} & 0 & 0 & 0 & 0\\
e_{u, y} & e_{v, y} & 0 & 0 & 0 & 0\\
0 & 0 & 1 & 0 & 0 & 0\\
0 & 0 & 0 & e_{u, x} & e_{v, x} & 0\\
0 & 0 & 0 & e_{u, y} & e_{v, y} & 0\\
0 & 0 & 0 & 0 & 0 & 1\\
\end{pmatrix} \begin{pmatrix}
u_1 \\ v_1 \\ \theta_{z, 1} \\ u_2 \\ v_2 \\ \theta_{z, 2}
\end{pmatrix} = \boldsymbol{\tilde{P}} \boldsymbol{u}_{e, local}\end{split}\]

Note

For the rest of this documentation, coordinates and DOFs will be written in
the local coordinate system, unless specified otherwise.

## Kinematics description formulation

Two formulations are available to describe the kinematics.

The first formulation is the total Lagrangian formulation. In this formulation, all calculations are done in the initial reference configuration (for instance, the terms of [Principle of virtual work](#theory-beam-virtual-work)) are computed in the initial reference configuration. The total displacement is used to describe the transformation between the initial configuration and the current configuration. This formulation is well suited for linear or weakly non-linear problems. It could be used for example when displacements and rotations are small.

When stronger non-linearities are considered, a corotational formulation must be used. For instance, the corotational formulation must be used when considering large displacements and large rotations. In the corotational formulation, the integrals are computed in the current configuration, such as one needs to define an increment of displacement. In problems where a time step is defined, that increment corresponds to the evolution of the
displacement between two time steps. In problems where the load is subdivided in several increments, the
increment of displacement corresponds to its evolution between two load increments.
In the corotational formulation, the stress is measured in a local frame rotating with the element, as shown in [Fig. 117](#corot-schema).

![figure](https://manta-project.gitlab.io/manta/_images/corotational_description.png)

Fig. 117 Local frame rotating with the element.

Moreover, the increment of displacement \(d \boldsymbol{u}_{e}\) from the step \(n\) to the next step \(n+1\) is used to compute the stress with the following steps:

- The mesh coordinates are updated and the local frame is computed,
- The global displacement increment \(d \boldsymbol{u}_{e, global}\) is computed in the local frame: \(d \boldsymbol{u}_{e, local}\),
- The strain increment \(d \epsilon(d \boldsymbol{u}_{e, local})\) is computed considering the new mesh coordinates,
- The stress increment \(d \sigma(d \epsilon)\) is computed from the strain increment and the constitutive law,
- The total stress is updated: \(\sigma^{n+1} = \sigma^n + d \sigma\)

The local frame is computed as explained in the [Local coordinate system](#theory-beam-local-coord) section. However, the vector \(\boldsymbol{e_v}\), initially given by the user, should be updated with the rotation of the element. The average of the rotation of the two nodes of the element is used to update the vector.

At each step, the vector \(d \psi\) of the average rotation increment of the element is computed with the rotations increments of the two nodes as follows:

\[\begin{split}d \psi = \frac{1}{2} \left( \begin{pmatrix}
d\theta_{x,1} \\
d\theta_{y,1} \\
d\theta_{z,1}
\end{pmatrix}
+
\begin{pmatrix}
d\theta_{x,2} \\
d\theta_{y,2} \\
d\theta_{z,2}
\end{pmatrix}
\right)\end{split}\]

The previous vector \(\boldsymbol{e_v}^n\) at the time step \(n\) is first written in the new local frame: \(\boldsymbol{e_{v, local}}^{n+1}\).
The vector variation due to the frame rotation is then:

\[d \boldsymbol{e_{v, local}}^{n+1} = d \psi \times \boldsymbol{e_{v, local}}^n\]

The new vector is then \(\boldsymbol{e_{v, local}}^{n+1} = \boldsymbol{e_{v, local}}^n + d \boldsymbol{e_{v, local}}\). This can also be written as:

\[\begin{split}\boldsymbol{e_{v, local}}^{n+1} = \begin{pmatrix}
1 & -d\psi_3 & d\psi_2 \\
d\psi_3 & 1 & -d\psi_1 \\
-d\psi_2 & d\psi_1 & 1
\end{pmatrix}
\boldsymbol{e_{v, local}}^n\end{split}\]

where \(d \psi^{\transpose{}} = (d \psi_1, d \psi_2, d \psi_3)^{\transpose{}}\).

The vector \(\boldsymbol{e_{v, local}}^{n+1}\) is then written back in the global frame.

## Kinematics

First, let us write the displacement vector of a given point \(M\). Let
\(M'\) be the point on the neutral axis that shares \(M\)'s \(x\)
coordinate.

The displacement of point \(M\) can be decomposed as the displacement of
point \(M'\) for the translation, which should be completed by taking into
account the contribution of the rotation DOFs.

Therefore:

\[\begin{split}\boldsymbol{u}(M) = \begin{pmatrix}
u(M)\\
v(M)\\
w(M)
\end{pmatrix} = \begin{pmatrix}
u(x)\\
v(x)\\
w(x)
\end{pmatrix} + \begin{pmatrix}
0\\
-z \sin(\theta_x(x))\\
y \sin(\theta_x(x))
\end{pmatrix} + \begin{pmatrix}
z \sin(\theta_y(x))\\
0\\
z (1-\cos(\theta_y(x)))
\end{pmatrix} + \begin{pmatrix}
-y \sin(\theta_z(x))\\
y (1-\cos(\theta_z(x)))\\
0
\end{pmatrix}\end{split}\]

Hereabove, \(x\) designates the position over the neutral axis of point
\(M'\).

For small rotations, this simplifies to:

(284)\[\begin{split}\boxed{
\boldsymbol{u}(M) = \begin{pmatrix}
u + z \theta_y - y \theta_z\\
v - z \theta_x\\
w + y \theta_x
\end{pmatrix}(x) = \begin{pmatrix}
1 & 0 & 0 & 0 & z & -y \\
0 & 1 & 0 & -z & 0 & 0 \\
0 & 0 & 1 & y & 0 & 0 \\
\end{pmatrix}\boldsymbol{U}(x)
}\end{split}\]

Euler-Bernoulli

Additionally, for Euler-Bernoulli beams, the cross-section's plane are assumed
to stay **orthogonal** to the beam's neutral axis, which translates as:

![figure](https://manta-project.gitlab.io/manta/_images/angle_deflection_relation.svg)

Fig. 118 Relation between angle and deflection DOF for an Euler-Bernoulli beam

\[ \begin{align}\begin{aligned}\tan(\theta_z) & = \partial_x v\\\tan(\theta_y) & = - \partial_x w\end{aligned}\end{align} \]

which for small rotations simplifies to:

(285)\[ \begin{align}\begin{aligned}\theta_z & = \partial_x v\\\theta_y & = - \partial_x w\end{aligned}\end{align} \]

Timoshenko

(*Intentionally left blank*)

## Strains

Strains are written as such:

\[\begin{split}\boldsymbol{\epsilon}(M) = \begin{pmatrix}
\epsilon_{xx} \\
\epsilon_{yy} \\
\epsilon_{zz} \\
2 \epsilon_{xy} \\
2 \epsilon_{xz} \\
2 \epsilon_{yz}
\end{pmatrix}(M) = \begin{pmatrix}
\partial_x u \\
\partial_y v \\
\partial_z w \\
\partial_x v + \partial_y u \\
\partial_x w + \partial_z u \\
\partial_y w + \partial_z v
\end{pmatrix}(M) = \begin{pmatrix}
\partial_x u + z \partial_x \theta_y - y \partial_x \theta_z\\
\partial_y v - z \partial_y \theta_x \\
\partial_z w + y \partial_z \theta_x\\
\partial_x v - z \partial_x \theta_x + \partial_y u + z \partial_y \theta_y - y \partial_y \theta_z - \theta_z\\
\partial_x w + y \partial_x \theta_x + \partial_z u + z \partial_z \theta_y + \theta_y -y \partial_z \theta_z\\
\partial_y w + y \partial_y \theta_x + \theta_x + \partial_z v - z \partial_z \theta_x - \theta_x
\end{pmatrix}(x)\end{split}\]

Using the fact that [the cross-section is non-deformable](#theory-beam-hypotheses),
i.e. all partial derivative along the cross-section directions (\(\partial_y\)
and \(\partial_z\)) are equal to zero, one concludes:

\[\begin{split} \boldsymbol{\epsilon}(M) = \begin{pmatrix}
\epsilon_{xx} \\
\epsilon_{yy} \\
\epsilon_{zz} \\
2 \epsilon_{xy} \\
2 \epsilon_{xz} \\
2 \epsilon_{yz}
\end{pmatrix}(M) = \begin{pmatrix}
\partial_x u + z \partial_x \theta_y - y \partial_x \theta_z\\
0 \\
0\\
\partial_x v - z \partial_x \theta_x - \theta_z\\
\partial_x w + y \partial_x \theta_x + \theta_y\\
0
\end{pmatrix}(x)\end{split}\]

Euler-Bernoulli

> Using [(285)](#equation-theory-beam-relation-angle-deflection-small-rot), this becomes:
>
> \[\begin{split}\boldsymbol{\epsilon}(M) = \begin{pmatrix}
> \epsilon_{xx} \\
> \epsilon_{yy} \\
> \epsilon_{zz} \\
> 2 \epsilon_{xy} \\
> 2 \epsilon_{xz} \\
> 2 \epsilon_{yz}
> \end{pmatrix}(M) = \begin{pmatrix}
> \partial_x u + z \partial_x \theta_y - y \partial_x \theta_z\\
> 0 \\
> 0\\
> - z \partial_x \theta_x \\
> y \partial_x \theta_x\\
> 0
> \end{pmatrix}(x)\end{split}\]

Timoshenko

(*Intentionally left blank*)

## Generalized forces, external forces and equations of equilibrium

In this section, all fundamental quantities and equations that are fundamental
to any beam behavior are defined and described. They are all derived from
the **principle of virtual work** written over the volume of the beam and
integrated over its cross-section.

### Principle of virtual work

Let \(\boldsymbol{\hat{u}}\) be a virtual displacement, and
\(\boldsymbol{\hat{\epsilon}}\) be the associated virtual strains.

The **principle of virtual work** can be written as:

(286)\[- \int_{V} (\boldsymbol{\sigma} \cdot \boldsymbol{\hat{\epsilon}}) dV
+ \int_{V} (\boldsymbol{f}_{ext}^{v} \cdot \boldsymbol{\hat{u}}) dV
+ \int_{\partial V} (\boldsymbol{t}_{ext}^{s} \cdot \boldsymbol{\hat{u}}) dS
= \int_{V} (\rho \partial_t^2\boldsymbol{u} \cdot \boldsymbol{\hat{u}}) dV\]

where:

- \(\boldsymbol{\sigma}\) is the **stress** tensor ;
- \(\boldsymbol{f}_{ext}^{v} = \left(\begin{array}\\f_x^v&f_y^v&f_z^v\end{array}\right)^{T}\)
  is the **external volumic forces** vector, expressed in the local coordinate
  system ;
- \(\boldsymbol{t}_{ext}^{s} = \left(\begin{array}\\t_x^s&t_y^s&t_z^s\end{array}\right)^{T}\)
  is the **external surfacic forces** vector, expressed in the local coordinate
  system ;
- \(\rho\) is the **density** of the material ;
- \(V\) is the **volume** of the beam ;
- \(\partial V\) is the **countour** of the volume.

### Generalized forces

The **generalized forces**, also named **internal forces** of the beam, correspond
to the integration over the cross-section of components of the stress tensor.

They are defined as follows:

(287)\[\begin{split}N_x & = \int_{S} \sigma_{xx} dS \\
T_y & = \int_{S} \sigma_{xy} dS \\
T_z & = \int_{S} \sigma_{xz} dS \\
M_x & = \int_{S} (y \sigma_{xz} - z \sigma_{xy}) dS \\
M_y & = \int_{S} z \sigma_{xx} dS \\
M_z & = \int_{S} - y \sigma_{xx} dS \\\end{split}\]

where:

- \(N_x\) the **axial force** along the \((Ox)\) direction ;
- \(T_y\) the **shear force** along the \((Oy)\) direction ;
- \(T_z\) the **shear force** along the \((Oz)\) direction ;
- \(M_x\) the **torsion moment** around the \((Ox)\) direction ;
- \(M_y\) the **bending moment** around the \((Oy)\) direction (bending
  in the \((xOz)\) plane) ;
- \(M_z\) the **bending moment** around the \((Oz)\) direction (bending
  in the \((xOy)\) plane).

### External forces

External forces are derived from the external volumic and surfacic forces.

Let us first decompose the virtual work of the surfacic forces, such as it is
integrated on each of the two ends of the beam on the one part, and integrated
over the contour of the cross-section along the length of the beam on the other
part:

\[\int_{\partial V} \boldsymbol{t}_{ext}^{s} \cdot \boldsymbol{\hat{u}} dS
= \int_{S} \boldsymbol{t}_{ext}^{s} \cdot \boldsymbol{\hat{u}}(x=L) dS
- \int_{S} \boldsymbol{t}_{ext}^{s} \cdot \boldsymbol{\hat{u}}(x=0) dS
+ \int_x \left(\int_{\partial l} \boldsymbol{t}_{ext}^{s} \cdot \boldsymbol{\hat{u}} dl \right) dx\]

where \(\partial l\) is the contour of the cross-section at the \(x\)
coordinate.

The \(\int_{\partial l} \boldsymbol{t}_{ext}^{s} \cdot \boldsymbol{\hat{u}} dl\)
term cannot be computed in the general case as it depends on the precise
geometry of the cross-section, but can be further down decomposed
along each of the virtual displacement coordinate. The following quantites arise
from this decomposition:

\[\int_{\partial l} \boldsymbol{t}_{ext}^{s} \cdot \boldsymbol{\hat{u}} dl
= t_x^l \hat{u} + t_y^l \hat{v} + t_z^l \hat{w}
+ \tau_x^l \hat{\theta_x} + \tau_y^l \hat{\theta_y} + \tau_z^l \hat{\theta_z}\]

Finally, the **linear external forces** are defined as the sum of the integration
of surfacic external forces over the contour of the cross-section and the
integration of the volumic external forces over the cross-section:

(288)\[\begin{split}f_{x} & = t_x^l + \int_{S} f_x^v dS \\
f_{y} & = t_y^l + \int_{S} f_y^v dS \\
f_{z} & = t_z^l + \int_{S} f_z^v dS \\
m_{x} & = \tau_x^l + \int_{S} (y f_z^v - z f_y^v) dS \\
m_{y} & = \tau_y^l + \int_{S} z f_x^v dS \\
m_{z} & = \tau_z^l + \int_{S} - y f_x^v dS \\\end{split}\]

And the **external forces at the end of the beam** are defined as the integration
of the surfacic external forces over the end cross-section:

(289)\[\begin{split}N_{x}^{ext} & = \int_{S} t_x^s dS \\
T_{y}^{ext} & = \int_{S} t_y^s dS \\
T_{z}^{ext} & = \int_{S} t_z^s dS \\
M_{x}^{ext} & = \int_{S} (y t_z^s - z t_x^s) dS \\
M_{y}^{ext} & = \int_{S} z t_x^s dS \\
M_{z}^{ext} & = \int_{S} - y t_x^s dS \\\end{split}\]

### Equations of equilibrium

Given the virtual work principle [(286)](#equation-theory-beam-virtual-work-principle) and the
definition of the generalized [(287)](#equation-theory-beam-generalized-forces) and external
forces [(288)](#equation-theory-beam-linear-ext-forces) [(289)](#equation-theory-beam-ext-forces), the
equations of equilibrium can be derived.

Let us distinguish each virtual work independently of the others.

#### Virtual work of the internal forces

The virtual work of the **internal forces** is written this way:

Euler-Bernoulli

\[ \begin{align}\begin{aligned}\delta \hat{W_i} & = - \int_V \boldsymbol{\sigma}.\boldsymbol{\hat{\epsilon}} dV\\& = - \int_V (\sigma_{xx}\hat{\epsilon_{xx}} + 2 \sigma_{xy}\hat{\epsilon_{xy}}
+ 2 \sigma_{xz}\hat{\epsilon_{xz}}) dV\\& = - \int_V (\sigma_{xx}(\partial_x \hat{u} + z \partial_x \hat{\theta_y}
- y \partial_x \hat{\theta_z}) - \sigma_{xy} z \partial_x \hat{\theta_x}
+ \sigma_{xz} y \partial_x \hat{\theta_x} ) dV\end{aligned}\end{align} \]

Timoshenko

\[ \begin{align}\begin{aligned}\delta \hat{W_i} & = - \int_V \boldsymbol{\sigma}.\boldsymbol{\hat{\epsilon}} dV\\& = - \int_V (\sigma_{xx}\hat{\epsilon_{xx}} + 2 \sigma_{xy}\hat{\epsilon_{xy}}
+ 2 \sigma_{xz}\hat{\epsilon_{xz}}) dV\\& = - \int_V (\sigma_{xx}(\partial_x \hat{u} + z \partial_x \hat{\theta_y}
- y \partial_x \hat{\theta_z})
+ \sigma_{xy} (\partial_x \hat{v} - \hat{\theta_z} - z \partial_x \hat{\theta_x})
+ \sigma_{xz} (\partial_x \hat{w} + \hat{\theta_y} + y \partial_x \hat{\theta_x}) dV\end{aligned}\end{align} \]

Using the definition of the generalized forces [(287)](#equation-theory-beam-generalized-forces)
and the fact that the displacements are constant across the cross-section (cf.
[beam hypotheses](#theory-beam-hypotheses)), the heareabove expression
becomes

Euler-Bernoulli

(290)\[ \begin{align}\begin{aligned}\delta \hat{W_i} & = - \int_x (N_x \partial_x \hat{u}
+ M_x \partial_x \hat{\theta_x} + M_y \partial_x \hat{\theta_y}
+ M_z \partial_x \hat{\theta_z}) dx\\& = - \left[ N_x \hat{u} + M_x \hat{\theta_x} + M_y \hat{\theta_y}
+ M_z \hat{\theta_z} \right]_{0}^{L}\\& + \int_x (\partial_x N_x \hat{u}
+ \partial_x M_x \hat{\theta_x} + \partial_x M_y \hat{\theta_y}
+ \partial_x M_z \hat{\theta_z}) dx\end{aligned}\end{align} \]

Using the **relation between the deflections and the angles**
[(285)](#equation-theory-beam-relation-angle-deflection-small-rot):

\[ \begin{align}\begin{aligned}\delta \hat{W_i} & = - \left[ N_x \hat{u} + M_x \hat{\theta_x} + M_y \hat{\theta_y}
+ M_z \hat{\theta_z} \right]_{0}^{L} + \int_x (\partial_x N_x \hat{u}
+ \partial_x M_x \hat{\theta_x} - \partial_x M_y \partial_x \hat{w}
+ \partial_x M_z \partial_x \hat{v}) dx\\& = - \left[ N_x \hat{u} + M_x \hat{\theta_x} + M_y \hat{\theta_y}
+ M_z \hat{\theta_z} + \partial_x M_y \hat{w} - \partial_x M_z \hat{v}
\right]_{0}^{L} + \int_x (\partial_x N_x \hat{u} + \partial_x M_x \hat{\theta_x}
+ \partial_x^2 M_y \hat{w} - \partial_x^2 M_z \hat{v}) dx\end{aligned}\end{align} \]

Timoshenko

(291)\[ \begin{align}\begin{aligned}\delta \hat{W_i} & = - \int_x (N_x \partial_x \hat{u}
+ T_y (\partial_x \hat{v} - \hat{\theta_z})
+ T_z (\partial_x \hat{w} + \hat{\theta_y})
+ M_x \partial_x \hat{\theta_x} + M_y \partial_x \hat{\theta_y}
+ M_z \partial_x \hat{\theta_z}) dx\\& = - \left[ N_x \hat{u} + T_y \hat{v} + T_z \hat{w}
+ M_x \hat{\theta_x} + M_y \hat{\theta_y} + M_z \hat{\theta_z}
\right]_{0}^{L}\\& + \int_x (\partial_x N_x \hat{u} + \partial_x T_y \hat{v}
+ \partial_x T_z \hat{w}
+ \partial_x M_x \hat{\theta_x}
+ (\partial_x M_y - T_z) \hat{\theta_y}
+ (\partial_x M_z + T_y) \hat{\theta_z}) dx\end{aligned}\end{align} \]

where \(L\) is the length of the element.

#### Virtual work of the external forces

Using the same reasoning as for the internal forces, the virtual work of the
**external forces** can be written this way:

\[ \begin{align}\begin{aligned}\delta \hat{W}_{ext} & = \int_{V} (\boldsymbol{f}_{ext}^{v} \cdot \boldsymbol{\hat{u}}) dV
+ \int_{\partial V} (\boldsymbol{t}_{ext}^{s} \cdot \boldsymbol{\hat{u}}) dS\\& = \int_V (f_x^v(\hat{u} + z \hat{\theta_y} - y \hat{\theta_z})
+ f_y^v (\hat{v} - z \hat{\theta_x}) + f_z^v (\hat{w} + y \hat{\theta_x} ) dV\\& + \int_x \left(\int_{\partial l} \boldsymbol{t}_{ext}^{s} \cdot \boldsymbol{\hat{u}} dl \right) dx
+ \int_{S} \boldsymbol{t}_{ext}^{s} \cdot \boldsymbol{\hat{u}}(x=L) dS
- \int_{S} \boldsymbol{t}_{ext}^{s} \cdot \boldsymbol{\hat{u}}(x=0) dS\end{aligned}\end{align} \]

Using the definition of the external forces:

Euler-Bernoulli

\[\delta \hat{W}_{ext} = \left[ N_x^{ext} \hat{u} + T_y^{ext} \hat{v} + T_z^{ext} \hat{w}
+ M_x^{ext} \hat{\theta_x} + M_y^{ext} \hat{\theta_y} + M_z^{ext} \hat{\theta_z} \right]_{0}^{L}
+ \int_x (f_x \hat{u} + f_y \hat{v} + f_z \hat{w}
+ m_x \hat{\theta_x} + m_y \hat{\theta_y} + m_z \hat{\theta_z}) dx\]

Using the **relation between the deflections and the angles**
[(285)](#equation-theory-beam-relation-angle-deflection-small-rot):

\[ \begin{align}\begin{aligned}\delta \hat{W}_{ext} & = \left[ N_x^{ext} \hat{u} + T_y^{ext} \hat{v} + T_z^{ext} \hat{w}
+ M_x^{ext} \hat{\theta_x} + M_y^{ext} \hat{\theta_y} + M_z^{ext} \hat{\theta_z} \right]_{0}^{L}
+ \int_x (f_x \hat{u} + f_y \hat{v} + f_z \hat{w} + m_x \hat{\theta_x}
- m_y \partial_x\hat{w} + m_z \partial_x \hat{v}) dx\\& = \left[ N_x^{ext} \hat{u} + T_y^{ext} \hat{v} + T_z^{ext} \hat{w}
+ M_x^{ext} \hat{\theta_x} + M_y^{ext} \hat{\theta_y} + M_z^{ext} \hat{\theta_z}
+ m_z \hat{v} - m_y \hat{w} \right]_0^L\\& + \int_x (f_x \hat{u}
+ (f_y-\partial_x m_z) \hat{v} + (f_z+\partial_x m_y) \hat{w}
+ m_x \hat{\theta_x}) dx\end{aligned}\end{align} \]

Timoshenko

\[\delta \hat{W}_{ext} = \left[ N_x^{ext} \hat{u} + T_y^{ext} \hat{v} + T_z^{ext} \hat{w}
+ M_x^{ext} \hat{\theta_x} + M_y^{ext} \hat{\theta_y} + M_z^{ext} \hat{\theta_z} \right]_{0}^{L}
+ \int_x (f_x \hat{u} + f_y \hat{v} + f_z \hat{w}
+ m_x \hat{\theta_x} + m_y \hat{\theta_y} + m_z \hat{\theta_z}) dx\]

#### Virtual work of the inertial forces

The virtual work of the **inertial forces** can be determined this way:

\[ \begin{align}\begin{aligned}\hat{\delta W_a} & = \int_V \rho \frac{\partial^2 \boldsymbol{u}}{\partial t^2} \boldsymbol{\hat{u}} dV\\& = \int_V \rho [(\partial_t^2 u + z \partial_t^2 \theta_y - y \partial_t^2 \theta_z)(\hat{u} + z \hat{\theta_y} - y \hat{\theta_z}) + (\partial_t^2 v - z \partial_t^2 \theta_x)(\hat{v} - z \hat{\theta_x}) + (\partial_t^2 w + y \partial_t^2 \theta_x)(\hat{w} + y \hat{\theta_x})] dV\end{aligned}\end{align} \]

Using the fact that the [neutral axis is positioned at the center of inertia](#theory-beam-geom-integrals), the previous expression can be simplified by
omitting the terms that are linear in \(y\), \(z\) and \(yz\):

\[ \begin{align}\begin{aligned}\hat{\delta W_a} & = \int_V \rho (\partial_t^2 u \hat{u} + \partial_t^2 v \hat{v}
+ \partial_t^2 w \hat{w} + (y^2+z^2)\partial_t^2 \theta_x \hat{\theta_x}
+ z^2 \partial_t^2 \theta_y \hat{\theta_y}
+ y^2 \partial_t^2 \theta_z \hat{\theta_z}) dV\\& = \int_x (\rho S \partial_t^2 u \hat{u} + \rho S \partial_t^2 v \hat{v}
+ \rho S \partial_t^2 w \hat{w} + \rho J \partial_t^2 \theta_x \hat{\theta_x}
+ \rho I_y \partial_t^2 \theta_y \hat{\theta_y}
+ \rho I_z \partial_t^2 \theta_z \hat{\theta_z}) dx\end{aligned}\end{align} \]

where:

- \(S\) is the cross-section **area** ;
- \(J\) is the **polar moment of area** ;
- \(I_y\) and \(I_z\) are the **second moments of area**.

Euler-Bernoulli

Neglecting the inertial terms corresponding to the rotation of the cross-section
(see the [Euler-Bernoulli beam hypotheses](#theory-beam-hypotheses)),
one has:

\[\hat{\delta W_a} = \int_x (\rho S \partial_t^2 u \hat{u}
+ \rho S \partial_t^2 v \hat{v} + \rho S \partial_t^2 w \hat{w}
+ \rho J \partial_t^2 \theta_x \hat{\theta_x}) dx\]

Timoshenko

(*Intentionally left blank*)

#### Determining the equations of equilibrium

The **equations of equilibrium** can be determined by injecting the expression of
each virtual work in the principle of virtual work.

As the expressions hold for each virtual displacement, they also hold true for
any particular displacement that is equal to zero at each end of the beam, meaning
that only the integral part of each expression subsist. For such virtual
displacements, one has:

Euler-Bernoulli

\[ \begin{align}\begin{aligned}0 = \delta \hat{W_i} + \delta \hat{W}_{ext} - \hat{\delta W_a}
& = \int_x (\partial_x N_x \hat{u} + \partial_x M_x \hat{\theta_x}
+ \partial_x^2 M_y \hat{w} - \partial_x^2 M_z \hat{v}) dx\\& + \int_x (f_x \hat{u} + (f_y-\partial_x m_z) \hat{v}
+ (f_z+\partial_x m_y) \hat{w} + m_x \hat{\theta_x}) dx\\& - \int_x (\rho S \partial_t^2 u \hat{u}
+ \rho S \partial_t^2 v \hat{v} + \rho S \partial_t^2 w \hat{w}
+ \rho J \partial_t^2 \theta_x \hat{\theta_x}) dx\end{aligned}\end{align} \]

Timoshenko

\[ \begin{align}\begin{aligned}0 = \delta \hat{W_i} + \delta \hat{W}_{ext} - \hat{\delta W_a}
& = \int_x (\partial_x N_x \hat{u} + \partial_x T_y \hat{v}
+ \partial_x T_z \hat{w}
+ \partial_x M_x \hat{\theta_x}
+ (\partial_x M_y - T_z) \hat{\theta_y}
+ (\partial_x M_z + T_y) \hat{\theta_z}) dx\\& + \int_x (f_x \hat{u} + f_y \hat{v} + f_z \hat{w}
+ m_x \hat{\theta_x} + m_y \hat{\theta_y} + m_z \hat{\theta_z}) dx\\& - \int_x (\rho S \partial_t^2 u \hat{u} + \rho S \partial_t^2 v \hat{v}
+ \rho S \partial_t^2 w \hat{w} + \rho J \partial_t^2 \theta_x \hat{\theta_x}
+ \rho I_y \partial_t^2 \theta_y \hat{\theta_y}
+ \rho I_z \partial_t^2 \theta_z \hat{\theta_z}) dx\end{aligned}\end{align} \]

This holds for **each** admissible virtual displacement, which means that for
each component of the virtual displacement (\(\hat{u}\), \(\hat{v}\), etc.),
the sum of its factors equates to zero. This directly gives the equations of
equilibrium:

Euler-Bernoulli

(292)\[ \begin{align}\begin{aligned}\partial_x N_x + f_x & = \rho S \partial_t^{2} u\\\partial_x M_x + m_x & = \rho J \partial_t^{2} \theta_x\\\partial_x^2 M_y + \partial_x m_y + f_z & = \rho S \partial_t^2 w\\\partial_x^2 M_z + \partial_x m_z - f_y & = - \rho S \partial_t^2 v\end{aligned}\end{align} \]

Timoshenko

(293)\[ \begin{align}\begin{aligned}\partial_x N_x + f_x & = \rho S \partial_t^{2} u\\\partial_x T_y + f_y & = \rho S \partial_t^2 v\\\partial_x T_z + f_z & = \rho S \partial_t^2 w\\\partial_x M_x + m_x & = \rho J \partial_t^{2} \theta_x\\\partial_x M_y - T_z + m_{y} & = \rho I_y \partial_t^{2} \theta_y\\\partial_x M_z + T_y + m_{z} & = \rho I_z \partial_t^{2} \theta_z\end{aligned}\end{align} \]

## Constitutive behaviours

### Linear elastic

#### Stresses

For an elastic and isotropic material, the constitutive law for beams are the
following:

(294)\[\begin{split}\boldsymbol{\sigma} = \begin{pmatrix}
\sigma_{xx} \\
\sigma_{xy} \\
\sigma_{xz}
\end{pmatrix} = \begin{pmatrix}
E \epsilon_{xx} \\
2 G \epsilon_{xy} \\
2 G \epsilon_{xz}
\end{pmatrix} = \begin{pmatrix}
E & 0 & 0 \\
0 & G & 0\\
0 & 0 & G
\end{pmatrix} \boldsymbol{\epsilon}\end{split}\]

with:

- \(E\) the **Young modulus** ;
- \(G = \frac{E}{2(1+\nu)}\) the **shear modulus** ;
- \(\nu\) the **Poisson ratio**

Note

Hereabove, no hypothesis over the variation of the geometric and material
properties has been made, i.e. these properties may as well **vary** over the
length of the beam.

#### Internal forces

By definition, the internal forces in a beam are deduced by integrating the
stress components over the cross-section:

\[ \begin{align}\begin{aligned}N & = \int_{S} \sigma_{xx} dS\\T_y & = \int_{S} \sigma_{xy} dS\\T_z & = \int_{S} \sigma_{xz} dS\\M_x & = \int_{S} (y \sigma_{xz} - z \sigma_{xy}) dS\\M_y & = \int_{S} z \sigma_{xx} dS\\M_z & = - \int_{S} y \sigma_{xx} dS\end{aligned}\end{align} \]

Using the relations between stresses and strains [(294)](#equation-theory-beam-stresses), this
yields:

Euler-Bernoulli

(295)\[ \begin{align}\begin{aligned}N & = \int_{S} E \epsilon_{xx} dS = \int_{S} E (\partial_x u + z \partial_x \theta_y - y \partial_x \theta_z) dS\\T_y & = \int_{S} G \epsilon_{xy} dS = \int_{S} - G z \partial_x \theta_x dS\\T_z & = \int_{S} G \epsilon_{xz} dS = \int_{S} G y \partial_x \theta_x dS\\M_x & = \int_{S} G (y \epsilon_{xz} - z \epsilon_{xy}) dS = \int_{S} G (y (\partial_x w + y \partial_x \theta_x + \theta_y) - z (\partial_x v - z \partial_x \theta_x - \theta_z)) dS\\M_y & = \int_{S} E z \epsilon_{xx} dS = \int_{S} E z (\partial_x u + z \partial_x \theta_y - y \partial_x \theta_z) dS\\M_z & = - \int_{S} E y \epsilon_{xx} dS = - \int_{S} E y (\partial_x u + z \partial_x \theta_y - y \partial_x \theta_z) dS\end{aligned}\end{align} \]

Combining the expression of internal forces as a function of strains
[(295)](#equation-theory-beam-internal-forces-strains-euler)
and [the fact that the neutral axis is at the center of inertia](#theory-beam-geom-integrals),
and using the fact that each quantity is constant across the cross-section
(cf. [beam hypotheses](#theory-beam-hypotheses)):

(296)\[ \begin{align}\begin{aligned}N & = \int_{S} E \partial_x u dS = E \partial_x u \int_{S} dS = E S \partial_x u\\T_y & = 0\\T_z & = 0\\M_x & = \int_{S} G (y^{2} \partial_x \theta_x + z^{2} \partial_x \theta_x) dS = G \partial_x \theta_x \int_{S} ( y^{2} + z^{2}) dS = G J \partial_x \theta_x\\M_y & = \int_{S} E z^{2} \partial_x \theta_y dS = E \partial_x \theta_y \int_{S} z^{2} dS = E I_y \partial_x \theta_y = - E I_y \partial_x^2 w\\M_z & = \int_{S} E y^{2} \partial_x \theta_z dS = E \partial_x \theta_z \int_{S} y^{2} dS = E I_z \partial_x \theta_z = E I_z \partial_x^2 v\end{aligned}\end{align} \]

Timoshenko

(297)\[ \begin{align}\begin{aligned}N & = \int_{S} E \epsilon_{xx} dS = \int_{S} E (\partial_x u + z \partial_x \theta_y - y \partial_x \theta_z) dS\\T_y & = \int_{S} G \epsilon_{xy} dS = \int_{S} G (\partial_x v - z \partial_x \theta_x - \theta_z) dS\\T_z & = \int_{S} G \epsilon_{xz} dS = \int_{S} G (\partial_x w + y \partial_x \theta_x + \theta_y) dS\\M_x & = \int_{S} G (y \epsilon_{xz} - z \epsilon_{xy}) dS = \int_{S} G (y (\partial_x w + y \partial_x \theta_x + \theta_y) - z (\partial_x v - z \partial_x \theta_x - \theta_z)) dS\\M_y & = \int_{S} E z \epsilon_{xx} dS = \int_{S} E z (\partial_x u + z \partial_x \theta_y - y \partial_x \theta_z) dS\\M_z & = - \int_{S} E y \epsilon_{xx} dS = - \int_{S} E y (\partial_x u + z \partial_x \theta_y - y \partial_x \theta_z) dS\end{aligned}\end{align} \]

Combining the expression of internal forces as a function of strains
[(297)](#equation-theory-beam-internal-forces-strains-timoshenko)
and [the fact that the neutral axis is at the center of inertia](#theory-beam-geom-integrals),
and using the fact that each quantity is constant across the cross-section
(cf. [beam hypotheses](#theory-beam-hypotheses)):

(298)\[ \begin{align}\begin{aligned}N & = \int_{S} E \partial_x u dS = E \partial_x u \int_{S} dS = E S \partial_x u\\T_y & = \int_{S} G (\partial_x v - \theta_z) dS = G (\partial_x v - \theta_z) \int_{S} dS = G S (\partial_x v - \theta_z)\\T_z & = \int_{S} G (\partial_x w + \theta_y) dS = G (\partial_x w + \theta_y) \int_{S} dS = G S(\partial_x w + \theta_y)\\M_x & = \int_{S} G (y^{2} \partial_x \theta_x + z^{2} \partial_x \theta_x) dS = G \partial_x \theta_x \int_{S} ( y^{2} + z^{2}) dS = G J \partial_x \theta_x\\M_y & = \int_{S} E z^{2} \partial_x \theta_y dS = E \partial_x \theta_y \int_{S} z^{2} dS = E I_y \partial_x \theta_y\\M_z & = \int_{S} E y^{2} \partial_x \theta_z dS = E \partial_x \theta_z \int_{S} y^{2} dS = E I_z \partial_x \theta_z\end{aligned}\end{align} \]

where:

- \(S\) is the cross-section **area** ;
- \(J\) is the **polar moment of area** ;
- \(I_y\) and \(I_z\) are the **second moments of area**.

which definitions are given hereabove.

Euler-Bernoulli

To account for the **cross-section warping**, the **torsion constant** \(J_x\)
is introduced, which value directly depend of the cross-section geometry.

This corrective coefficient is defined such as the **moment around the beam axis
become**:

\[M_x = G J_x \partial_x \theta_x\]

Timoshenko

To account for the **cross-section warping**, several corrective coefficient are
introduced, which values directly depend of the cross-section geometry:

> - \(\kappa_y\) and \(\kappa_z\) the **shear coefficients** ;
> - \(J_x\), the **torsion constant**.

Those corrective coefficients are defined such that the
internal forces [(298)](#equation-theory-beam-internal-forces-strains-simpl-timoshenko)
become:

(299)\[ \begin{align}\begin{aligned}T_y & = G S \kappa_y (\partial_x v - \theta_z)\\T_z & = G S \kappa_z (\partial_x w + \theta_y)\\M_x & = G J_x \partial_x \theta_x\end{aligned}\end{align} \]

## Shape functions and interpolation

\(\boldsymbol{U}(x)\) is interpolated inside the element using **shape
functions**.

Euler-Bernoulli

Such interpolation should at least verify the **equilibrium equations**
[(292)](#equation-theory-beam-equilibrium-eq-euler) in **static**
(\(\partial_t = 0\)) and in the absence of any external force, with a linear
elastic material. Thus verifying:

\[\begin{split}\partial_x N & = 0 \\
\partial_x M_x & = 0 \\
\partial_x^2 M_y & = 0 \\
\partial_x^2 M_z & = 0\end{split}\]

Writing the internal forces as function of the degrees of freedom
[(296)](#equation-theory-beam-internal-forces-strains-simpl-euler), one deduces the
following:

(300)\[\begin{split}\partial_x^2 u & = 0 \\
\partial_x^2 \theta_x & = 0 \\
\partial_x^4 v & = 0 \\
\partial_x^4 w & = 0\end{split}\]

As the Euler-Bernoulli hypotheses imposes a relation between the
angles and the deflections, any possible interpolation must be of the following
form:

\[ \begin{align}\begin{aligned}u(x) & = u_1 \varphi^1_{u}(x) + u_2 \varphi^2_{u}(x)\\\theta_x(x) & = \theta_{x,1} \varphi^1_{\theta_x}(x) + \theta_{x,2} \varphi^2_{\theta_x}(x)\\v(x) & = v_1 \varphi^1_{v}(x) + v_2 \varphi^2_{v}(x) + \theta_{z,1} \varphi^1_{\theta_z}(x) + \theta_{z,2} \varphi^2_{\theta_z}(x)\\w(x) & = w_1 \varphi^1_{w}(x) + w_2 \varphi^2_{w}(x) - \theta_{y,1} \varphi^1_{\theta_y}(x) - \theta_{y,2} \varphi^2_{\theta_y}(x)\end{aligned}\end{align} \]

which yields, given the relations between the angles and the deflections
[(285)](#equation-theory-beam-relation-angle-deflection-small-rot):

\[ \begin{align}\begin{aligned}\theta_y(x) & = - w_1 \partial_x \varphi^{1}_{w}(x) - w_2 \partial_x \varphi^2_{w}(x) + \theta_{y,1} \partial_x \varphi^1_{\theta_y}(x) + \theta_{y,2} \partial_x \varphi^2_{\theta_y}(x)\\\theta_z(x) & = v_1 \partial_x \varphi^1_{v}(x) + v_2 \partial_x \varphi^2_{v}(x) + \theta_{z,1} \partial_x \varphi^1_{\theta_z}(x) + \theta_{z,2} \partial_x \varphi^2_{\theta_z}(x)\end{aligned}\end{align} \]

with the following conditions at each end (\(L\) being the length of the element):

\[ \begin{align}\begin{aligned}\varphi^1_{u}(0) = 1 & ; & \varphi^1_{u}(L) = 0\\\varphi^2_{u}(0) = 0 & ; & \varphi^2_{u}(L) = 1\\\varphi^1_{\theta_x}(0) = 1 & ; & \varphi^1_{\theta_x}(L) = 0\\\varphi^2_{\theta_x}(0) = 0 & ; & \varphi^2_{\theta_x}(L) = 1\\\varphi^1_{v}(0) = 1 & ; & \varphi^1_{v}(L) = 0 & ; & \partial_x \varphi^1_{v}(0) = 0 & ; & \partial_x \varphi^1_{v}(L) = 0\\\varphi^2_{v}(0) = 0 & ; & \varphi^2_{v}(L) = 1 & ; & \partial_x \varphi^2_{v}(0) = 0 & ; & \partial_x \varphi^2_{v}(L) = 0\\\varphi^1_{\theta_z}(0) = 0 & ; & \varphi^1_{\theta_z}(L) = 0 & ; & \partial_x \varphi^1_{\theta_z}(0) = 1 & ; & \partial_x \varphi^1_{\theta_z}(L) = 0\\\varphi^2_{\theta_z}(0) = 0 & ; & \varphi^2_{\theta_z}(L) = 0 & ; & \partial_x \varphi^2_{\theta_z}(0) = 0 & ; & \partial_x \varphi^2_{\theta_z}(L) = 1\\\varphi^1_{w}(0) = 1 & ; & \varphi^1_{w}(L) = 0 & ; & \partial_x \varphi^1_{w}(0) = 0 & ; & \partial_x \varphi^1_{w}(L) = 0\\\varphi^2_{w}(0) = 0 & ; & \varphi^2_{w}(L) = 1 & ; & \partial_x \varphi^2_{w}(0) = 0 & ; & \partial_x \varphi^2_{w}(L) = 0\\\varphi^1_{\theta_y}(0) = 0 & ; & \varphi^1_{\theta_y}(L) = 0 & ; & \partial_x \varphi^1_{\theta_y}(0) = 1 & ; & \partial_x \varphi^1_{\theta_y}(L) = 0\\\varphi^2_{\theta_y}(0) = 0 & ; & \varphi^2_{\theta_y}(L) = 0 & ; & \partial_x \varphi^2_{\theta_y}(0) = 0 & ; & \partial_x \varphi^2_{\theta_y}(L) = 1\end{aligned}\end{align} \]

Combining with the previous differential equations
[(300)](#equation-theory-beam-static-conditions-euler), those conditions yield
the following solutions:

\[\begin{split}\varphi_u^1(x) & = & \varphi_{\theta_x}^1(x) & = 1-\frac{x}{L} \\
\varphi_u^2(x) & = & \varphi_{\theta_x}^2(x) & = \frac{x}{L} \\
\varphi_v^1(x) & = & \varphi_w^1(x) & = 2(\frac{x}{L})^3-3(\frac{x}{L})^2+1 \\
\varphi_v^2(x) & = & \varphi_w^2(x) & = -2(\frac{x}{L})^3+3(\frac{x}{L})^2\\
\varphi_{\theta_y}^1(x) & = & \varphi_{\theta_z}^1(x) & = L [(\frac{x}{L})^3-2(\frac{x}{L})^2+\frac{x}{L}]\\
\varphi_{\theta_y}^2(x) & = & \varphi_{\theta_z}^2(x) & = L[(\frac{x}{L})^3-(\frac{x}{L})^2]\\\end{split}\]

Finally, the relation between \(\boldsymbol{U}(x)\) and
\(\boldsymbol{u}_e\) are as such:

\[\begin{split}\boldsymbol{U}(x) = \begin{pmatrix}
\varphi^1_u & 0 & 0 & 0 & 0 & 0 & \varphi^2_u & 0 & 0 & 0 & 0 & 0 \\
0 & \varphi^1_v & 0 & 0 & 0 & \varphi^1_{\theta_z} & 0 & \varphi^2_v & 0 & 0 & 0 & \varphi^2_{\theta_z} \\
0 & 0 & \varphi^1_w & 0 & -\varphi^1_{\theta_y} & 0 & 0 & 0 & \varphi^2_w & 0 & -\varphi^2_{\theta_y} & 0 \\
0 & 0 & 0 & \varphi^1_{\theta_x} & 0 & 0 & 0 & 0 & 0 & \varphi^2_{\theta_x} & 0 & 0 \\
0 & 0 & -\partial_x \varphi^1_w & 0 & \partial_x \varphi^1_{\theta_y} & 0 & 0 & 0 & -\partial_x \varphi^2_w & 0 & \partial_x\varphi^2_{\theta_y} & 0 \\
0 & \partial_x\varphi^1_v & 0 & 0 & 0 & \partial_x\varphi^1_{\theta_z} & 0 & \partial_x\varphi^2_v & 0 & 0 & 0 & \partial_x\varphi^2_{\theta_z}
\end{pmatrix}(x) \boldsymbol{u}_{e} = \boldsymbol{N}(x)\boldsymbol{u}_{e}\end{split}\]

Timoshenko

Such interpolation should at least verify the **equilibrium equations**
[(293)](#equation-theory-beam-equilibrium-eq-timoshenko) in **static**
(\(\partial_t = 0\)) and in the absence of any external force, with a linear
elastic material. Thus verifying:

\[\begin{split}\partial_x N & = 0 \\
\partial_x T_y & = 0 \\
\partial_x T_z & = 0 \\
\partial_x M_x & = 0 \\
\partial_x M_y - T_z & = 0 \\
\partial_x M_z + T_y & = 0 \\\end{split}\]

Writing the internal forces as function of the degrees of freedom
[(298)](#equation-theory-beam-internal-forces-strains-simpl-timoshenko), one deduces the
following:

(301)\[\begin{split}\partial_x^2 u & = 0 \\
\partial_x^2 v - \partial_x \theta_z & = 0 \\
\partial_x^2 w + \partial_x \theta_y & = 0 \\
\partial_x^2 \theta_x & = 0 \\
EI_y \partial_x^2 \theta_y - GS\kappa_z(\partial_x w + \theta_y) & = 0 \\
EI_z \partial_x^2 \theta_z + GS\kappa_y(\partial_x v - \theta_z) & = 0 \\\end{split}\]

Such conditions imply that \(v\) and \(\theta_z\) (respectively \(w\)
and \(\theta_y\)) are coupled, meaning that any interpolation must at least
make appear dependence of \(v\) to \(\theta_{z, 1}\) and \(\theta_{z, 2}\),
(respectively dependence of \(w\) to \(\theta_{y, 1}\) and
\(\theta_{y, 2}\)). One can show that the interpolation hereunder is
sufficient to respect the static conditions:

(302)\[ \begin{align}\begin{aligned}u(x) & = u_1 \varphi^1_{u}(x) + u_2 \varphi^2_{u}(x)\\v(x) & = v_1 \varphi^1_{v}(x) + v_2 \varphi^2_{v}(x) + \theta_{z,1} \psi^1_v(x) + \theta_{z,2} \psi^2_v(x)\\w(x) & = w_1 \varphi^1_{w}(x) + w_2 \varphi^2_{w}(x) - \theta_{y,1} \psi^1_w(x) - \theta_{y,2} \psi^2_w(x)\\\theta_x(x) & = \theta_{x,1} \varphi^1_{\theta_x}(x) + \theta_{x,2} \varphi^2_{\theta_x}(x)\\\theta_y(x) & = -w_1 \psi^1_{\theta_y}(x) -w_2 \psi^2_{\theta_y}(x) + \theta_{y,1} \varphi^1_{\theta_y}(x) + \theta_{y,2} \varphi^2_{\theta_y}(x)\\\theta_z(x) & = v_1 \psi^1_{\theta_z}(x) + v_2 \psi^2_{\theta_z}(x) + \theta_{z,1} \varphi^1_{\theta_z}(x) + \theta_{z,2} \varphi^2_{\theta_z}(x)\end{aligned}\end{align} \]

with the following conditions at each end in order to verify that any
interpolated DOF is equal to its nodal value at \(0\) and \(L\)
(\(L\) being the length of the element):

\[ \begin{align}\begin{aligned}\varphi^1_{u}(0) = 1 & ; & \varphi^1_{u}(L) = 0\\\varphi^2_{u}(0) = 0 & ; & \varphi^2_{u}(L) = 1\\\varphi^1_{v}(0) = 1 & ; & \varphi^1_{v}(L) = 0\\\varphi^2_{v}(0) = 0 & ; & \varphi^2_{v}(L) = 1\\\psi^1_v(0) = 0 & ; & \psi^1_v(L) = 0\\\psi^2_v(0) = 0 & ; & \psi^2_v(L) = 0\\\varphi^1_{w}(0) = 1 & ; & \varphi^1_{w}(L) = 0\\\varphi^2_{w}(0) = 0 & ; & \varphi^2_{w}(L) = 1\\\psi^1_w(0) = 0 & ; & \psi^1_w(L) = 0\\\psi^2_w(0) = 0 & ; & \psi^2_w(L) = 0\\\varphi^1_{\theta_x}(0) = 1 & ; & \varphi^1_{\theta_x}(L) = 0\\\varphi^2_{\theta_x}(0) = 0 & ; & \varphi^2_{\theta_x}(L) = 1\\\varphi^1_{\theta_y}(0) = 1 & ; & \varphi^1_{\theta_y}(L) = 0\\\varphi^2_{\theta_y}(0) = 0 & ; & \varphi^2_{\theta_y}(L) = 1\\\psi^1_{\theta_y}(0) = 0 & ; & \psi^1_{\theta_y}(L) = 0\\\psi^2_{\theta_y}(0) = 0 & ; & \psi^2_{\theta_y}(L) = 0\\\varphi^1_{\theta_z}(0) = 1 & ; & \varphi^1_{\theta_z}(L) = 0\\\varphi^2_{\theta_z}(0) = 0 & ; & \varphi^2_{\theta_z}(L) = 1\\\psi^1_{\theta_z}(0) = 0 & ; & \psi^1_{\theta_z}(L) = 0\\\psi^2_{\theta_z}(0) = 0 & ; & \psi^2_{\theta_z}(L) = 0\end{aligned}\end{align} \]

Combining with the previous differential equations
[(301)](#equation-theory-beam-static-conditions-timoshenko), those conditions yield
the following solutions:

(303)\[\begin{split}\varphi_u^1(x) & = 1-\frac{x}{L} \\
\varphi_u^2(x) & = \frac{x}{L} \\
\varphi_w^1(x) & = \frac{1}{1+\Phi_y}[2(\frac{x}{L})^3-3(\frac{x}{L})^2-\Phi_y\frac{x}{L}+(1+\Phi_y)] \\
\varphi_w^2(x) & = \frac{1}{1+\Phi_y}[-2(\frac{x}{L})^3+3(\frac{x}{L})^2+\Phi_y\frac{x}{L}] \\
\psi_w^1(x) & = \frac{L}{1+\Phi_y}[(\frac{x}{L})^3-\frac{4+\Phi_y}{2}(\frac{x}{L})^2+\frac{2+\Phi_y}{2}\frac{x}{L}] \\
\psi_w^2(x) & = \frac{L}{1+\Phi_y}[(\frac{x}{L})^3-\frac{2-\Phi_y}{2}(\frac{x}{L})^2-\frac{\Phi_y}{2}\frac{x}{L}] \\
\varphi_{\theta_x}^1(x) & = \varphi_u^1(x) \\
\varphi_{\theta_x}^2(x) & = \varphi_u^2(x) \\
\varphi_{\theta_y}^1(x) & = \frac{1}{1+\Phi_y}[3(\frac{x}{L})^2 - (4+\Phi_y)\frac{x}{L}+(1+\Phi_y)] \\
\varphi_{\theta_y}^2(x) & = \frac{1}{1+\Phi_y}[3(\frac{x}{L})^2 - (2-\Phi_y)\frac{x}{L}] \\
\psi_{\theta_y}^1(x) & = \frac{6}{L(1+\Phi_y)}\frac{x}{L}[1-\frac{x}{L}] \\
\psi_{\theta_y}^2(x) & = \frac{-6}{L(1+\Phi_y)}\frac{x}{L}[1-\frac{x}{L}] \\\end{split}\]

with \(\Phi_y = \frac{12EI_y}{GS\kappa_z L^2}\), and with the other shape
functions (\(\varphi_v^1\), \(\varphi_v^2\), \(\psi_v^1\),
\(\psi_v^2\), \(\varphi_{\theta_z}^1\), \(\varphi_{\theta_z}^2\),
\(\psi_{\theta_z}^1\) and \(\psi_{\theta_z}^2\))
being the same as their respective counterpart with the replacement of
\(\Phi_y\) by \(\Phi_z = \frac{12EI_z}{GS\kappa_y L^2}\).

Note

For the exhibited shape functions to actually be solutions of the static
equations, \(\Phi_y\) and \(\Phi_z\) actually need to be constant
through the element. In that case, even if the shape functions depend on the
geometric and material properties of the element, this does not constitute
a problem theory-wise.

For the rest of this documentation, the hypothesis that \(\Phi_y\) and
\(\Phi_z\) are constant (or at least *vary slowly*) over the element
will be made, which is a reasonable hypothesis to make when they are not
constant but if the structural element is finely meshed.

Note

One could see that \(\Phi_y = \Phi_z = 0\) in the expressions
hereabove yield the **Euler-Bernoulli beam shape functions**, which is
consistent with the fact that \(\Phi_y = \Phi_z = 0\) is equivalent to
the Euler-Bernoulli beam hypotheses.

Finally, the relation between \(\boldsymbol{U}(x)\) and
\(\boldsymbol{u}_e\) are as such:

\[\begin{split}\boldsymbol{U}(x) = \begin{pmatrix}
\varphi^1_u & 0 & 0 & 0 & 0 & 0 & \varphi^2_u & 0 & 0 & 0 & 0 & 0 \\
0 & \varphi^1_v & 0 & 0 & 0 & \psi^1_v & 0 & \varphi^2_v & 0 & 0 & 0 & \psi^2_v \\
0 & 0 & \varphi^1_w & 0 & -\psi^1_w & 0 & 0 & 0 & \varphi^2_w & 0 & -\psi^2_w & 0 \\
0 & 0 & 0 & \varphi^1_{\theta_x} & 0 & 0 & 0 & 0 & 0 & \varphi^2_{\theta_x} & 0 & 0 \\
0 & 0 & -\psi^1_{\theta_y} & 0 & \varphi^1_{\theta_y} & 0 & 0 & 0 & -\psi^2_{\theta_y} & 0 & \varphi^2_{\theta_y} & 0 \\
0 & \psi^1_{\theta_z} & 0 & 0 & 0 & \varphi^1_{\theta_z} & 0 & \psi^2_{\theta_z} & 0 & 0 & 0 & \varphi^2_{\theta_z}
\end{pmatrix}(x) \boldsymbol{u}_{e} = \boldsymbol{N}(x)\boldsymbol{u}_{e}\end{split}\]

## Determination of the stiffness matrix

Warning

The work done in this part covers only the **linear elastic** behaviour.

### Definition of the stiffness matrix

The **elementary stiffness matrix** \(\boldsymbol{K}_e\) of the element is
defined through the virtual work of the **internal forces** for any given virtual
displacement:

\[\delta \hat{W_i} = - \int_V \boldsymbol{\sigma}.\boldsymbol{\hat{\epsilon}} dV
= - \boldsymbol{u}_e^{\transpose{}} \boldsymbol{K}_e \boldsymbol{\hat{u}}_e\]

### Determination of the integrand stiffness matrix

Euler-Bernoulli

The virtual work of the internal forces has already been written in
[(290)](#equation-theory-beam-virtual-work-internal-euler). Using the expression of
the internal forces for a linear elastic material
[(296)](#equation-theory-beam-internal-forces-strains-simpl-euler):

\[ \begin{align}\begin{aligned}\delta \hat{W_i} & = - \int_x (N_x \partial_x \hat{u}
+ M_x \partial_x \hat{\theta_x} + M_y \partial_x \hat{\theta_y}
+ M_z \partial_x \hat{\theta_z}) dx\\& = - \int_x (E S \partial_x u \partial_x \hat{u}
+ G J_x \partial_x \theta_x \partial_x \hat{\theta_x}
+ E I_y \partial_x \theta_y \partial_x \hat{\theta_y}
+ E I_z \partial_x \theta_z \partial_x \hat{\theta_z}) dx\end{aligned}\end{align} \]

Timoshenko

The virtual work of the internal forces has already been written in
[(291)](#equation-theory-beam-virtual-work-internal-timoshenko). Using the expression of
the internal forces for a linear elastic material
[(298)](#equation-theory-beam-internal-forces-strains-simpl-timoshenko):

\[ \begin{align}\begin{aligned}\delta \hat{W_i} & = - \int_x (N_x \partial_x \hat{u}
+ T_y (\partial_x \hat{v} - \hat{\theta_z})
+ T_z (\partial_x \hat{w} + \hat{\theta_y})
+ M_x \partial_x \hat{\theta_x} + M_y \partial_x \hat{\theta_y}
+ M_z \partial_x \hat{\theta_z}) dx\\& = - \int_x (E S \partial_x u \partial_x \hat{u}
+ G S \kappa_y (\partial_x v - \theta_z)(\partial_x \hat{v} - \hat{\theta_z})
+ G S \kappa_z (\partial_x w + \theta_y)(\partial_x \hat{w} + \hat{\theta_y})\\& + G J_x \partial_x \theta_x \partial_x \hat{\theta_x}
+ E I_y \partial_x \theta_y \partial_x \hat{\theta_y}
+ E I_z \partial_x \theta_z \partial_x \hat{\theta_z}) dx\end{aligned}\end{align} \]

Re-writing the expression under the integral as a bi-linear form, one deduces that:

\[\delta \hat{W_i} = - \int_{x} \boldsymbol{U}^{\transpose{}}(x) \boldsymbol{D}^{\transpose{}} \boldsymbol{C} \boldsymbol{D} \boldsymbol{\hat{U}}(x) dx\]

where:

Euler-Bernoulli

\[\begin{split}\boldsymbol{D} & = \begin{pmatrix}
\partial_x & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & \partial_x & 0 & 0 \\
0 & 0 & 0 & 0 & \partial_x & 0 \\
0 & 0 & 0 & 0 & 0 & \partial_x
\end{pmatrix} ; \boldsymbol{C} & = \begin{pmatrix}
ES & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & GJ_{x} & 0 & 0 \\
0 & 0 & 0 & 0 & E I_y & 0 \\
0 & 0 & 0 & 0 & 0 & E I_z
\end{pmatrix}\end{split}\]

Timoshenko

\[\begin{split}\boldsymbol{D} & = \begin{pmatrix}
\partial_x & 0 & 0 & 0 & 0 & 0 \\
0 & \partial_x & 0 & 0 & 0 & -1 \\
0 & 0 & \partial_x & 0 & 1 & 0 \\
0 & 0 & 0 & \partial_x & 0 & 0 \\
0 & 0 & 0 & 0 & \partial_x & 0 \\
0 & 0 & 0 & 0 & 0 & \partial_x
\end{pmatrix} ; \boldsymbol{C} & = \begin{pmatrix}
ES & 0 & 0 & 0 & 0 & 0 \\
0 & GS\kappa_y & 0 & 0 & 0 & 0 \\
0 & 0 & GS\kappa_z & 0 & 0 & 0 \\
0 & 0 & 0 & GJ_{x} & 0 & 0 \\
0 & 0 & 0 & 0 & E I_y & 0 \\
0 & 0 & 0 & 0 & 0 & E I_z
\end{pmatrix}\end{split}\]

Using the interpolation of the DOFs inside the element, one has:

\[\begin{split}\delta \hat{W_i} & = - \int_{x} \boldsymbol{u}_e^{\transpose{}} \boldsymbol{N}(x)^{\transpose{}} \boldsymbol{D}^{\transpose{}} \boldsymbol{C} \boldsymbol{D} \boldsymbol{N}(x)\boldsymbol{\hat{u_e}} dx\\
& = - \boldsymbol{u}_e^{\transpose{}} \left( \int_{x} \boldsymbol{N}(x)^{\transpose{}} \boldsymbol{D}^{\transpose{}} \boldsymbol{C} \boldsymbol{D} \boldsymbol{N}(x) dx \right) \boldsymbol{\hat{u_e}}\\\end{split}\]

Thus defining the **integrand stiffness matrix** \(\boldsymbol{k}_e\):

(304)\[\begin{split}\boldsymbol{k}_e (x) & = \boldsymbol{N}(x)^{\transpose{}} \boldsymbol{D}^{\transpose{}} \boldsymbol{C} \boldsymbol{D} \boldsymbol{N}(x) \\
& = \boldsymbol{B}^{\transpose{}}(x) \boldsymbol{C} \boldsymbol{B}(x)\end{split}\]

where \(\boldsymbol{B}(x) = \boldsymbol{D}\boldsymbol{N}(x)\):

Euler-Bernoulli

\[\boldsymbol{B}(x) = \left( \boldsymbol{B}_1(x) | \boldsymbol{B}_2(x) \right)\]

(305)\[\begin{split}\boldsymbol{B}_i(x) = \begin{pmatrix}
\partial_x \varphi^i_u & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & \partial_x \varphi^i_{\theta_x} & 0 & 0 \\
0 & 0 & -\partial^2_x \varphi^i_w & 0 & \partial^2_x \varphi^i_{\theta_y} & 0 \\
0 & \partial^2_x\varphi^i_v & 0 & 0 & 0 & \partial^2_x\varphi^i_{\theta_z}
\end{pmatrix}(x)\end{split}\]

Timoshenko

\[\boldsymbol{B}(x) = \left( \boldsymbol{B}_1(x) | \boldsymbol{B}_2(x) \right)\]

(306)\[\begin{split}\boldsymbol{B}_i(x) = \begin{pmatrix}
\partial_x\varphi^i_u & 0 & 0 & 0 & 0 & 0\\
0 & \partial_x\varphi^i_v - \psi^i_{\theta_z} & 0 & 0 & 0 & \partial_x\psi^i_v - \varphi^i_{\theta_z}\\
0 & 0 & \partial_x\varphi^i_w -\psi^i_{\theta_y}& 0 & -\partial_x\psi^i_w+\varphi^i_{\theta_y} & 0 \\
0 & 0 & 0 & \partial_x\varphi^i_{\theta_x} & 0 & 0 \\
0 & 0 & -\partial_x\psi^i_{\theta_y} & 0 & \partial_x\varphi^i_{\theta_y} & 0 \\
0 & \partial_x\psi^i_{\theta_z} & 0 & 0 & 0 & \partial_x\varphi^i_{\theta_z}
\end{pmatrix}(x)\end{split}\]

The **elementary stiffness matrix** \(\boldsymbol{K}_e\) being related to
the integrand stiffness matrix this way:

(307)\[\boldsymbol{K}_e = \int_x \boldsymbol{k}_e(x) dx\]

The **internal forces vector** being derived directly from the elementary stiffness
matrix:

\[\boldsymbol{F}_i = \boldsymbol{K_e} \boldsymbol{u}_e\]

Expliciting \(\boldsymbol{k}_e\):

\[\begin{split}\boldsymbol{k}_e = \begin{pmatrix}
\boldsymbol{k}_{11} & \boldsymbol{k}_{12} \\
\boldsymbol{k}_{21} & \boldsymbol{k}_{22} \\
\end{pmatrix}\end{split}\]

which can be decomposed the following way:

(308)\[\boldsymbol{k}_{ij} = \boldsymbol{k}_{ij}^{traction} + \boldsymbol{k}_{ij}^{torsion} + \boldsymbol{k}_{ij}^{bending_y} + \boldsymbol{k}_{ij}^{bending_z}\]

Expliciting each sub-term:

Euler-Bernoulli

\[\begin{split}\boldsymbol{k}_{ij}^{traction} = \begin{pmatrix}
E S \partial_x \varphi^i_u \partial_x \varphi^j_u & 0 & 0 & 0 & 0 & 0\\
0 & 0 & 0 & 0 & 0 & 0\\
0 & 0 & 0 & 0 & 0 & 0\\
0 & 0 & 0 & 0 & 0 & 0\\
0 & 0 & 0 & 0 & 0 & 0\\
0 & 0 & 0 & 0 & 0 & 0\\
\end{pmatrix}\end{split}\]

\[\begin{split}\boldsymbol{k}_{ij}^{torsion} = \begin{pmatrix}
0 & 0 & 0 & 0 & 0 & 0\\
0 & 0 & 0 & 0 & 0 & 0\\
0 & 0 & 0 & 0 & 0 & 0\\
0 & 0 & 0 & G J_x \partial_x \varphi^i_{\theta_x} \partial_x \varphi^j_{\theta_x} & 0 & 0\\
0 & 0 & 0 & 0 & 0 & 0\\
0 & 0 & 0 & 0 & 0 & 0\\
\end{pmatrix}\end{split}\]

\[\begin{split}\boldsymbol{k}_{ij}^{bending_y} = \begin{pmatrix}
0 & 0 & 0 & 0 & 0 & 0\\
0 & E I_z \partial^2_x \varphi^i_v \partial^2_x \varphi^j_v & 0 & 0 & 0 & E I_z \partial^2_x \varphi^i_v \partial^2_x \varphi^j_{\theta_z} \\
0 & 0 & 0 & 0 & 0 & 0\\
0 & 0 & 0 & 0 & 0 & 0\\
0 & 0 & 0 & 0 & 0 & 0\\
0 & E I_z \partial^2_x \varphi^j_v \partial^2_x \varphi^i_{\theta_z} & 0 & 0 & 0 & E I_z \partial^2_x \varphi^i_{\theta_z} \partial^2_x \varphi^j_{\theta_z}\\
\end{pmatrix}\end{split}\]

\[\begin{split}\boldsymbol{k}_{ij}^{bending_z} = \begin{pmatrix}
0 & 0 & 0 & 0 & 0 & 0\\
0 & 0 & 0 & 0 & 0 & 0\\
0 & 0 & E I_y \partial^2_x \varphi^i_w \partial^2_x \varphi^j_w & 0 & - E I_y \partial^2_x \varphi^i_w \partial^2_x \varphi^j_{\theta_y} & 0 \\
0 & 0 & 0 & 0 & 0 & 0\\
0 & 0 & - E I_y \partial^2_x \varphi^j_w \partial^2_x \varphi^i_{\theta_y} & 0 & E I_y \partial^2_x \varphi^i_{\theta_y} \partial^2_x \varphi^j_{\theta_y} & 0 \\
0 & 0 & 0 & 0 & 0 & 0\\
\end{pmatrix}\end{split}\]

Timoshenko

\[\begin{split}\boldsymbol{k}_{ij}^{traction} = \begin{pmatrix}
E S \partial_x \varphi^i_u \partial_x \varphi^j_u & 0 & 0 & 0 & 0 & 0\\
0 & 0 & 0 & 0 & 0 & 0\\
0 & 0 & 0 & 0 & 0 & 0\\
0 & 0 & 0 & 0 & 0 & 0\\
0 & 0 & 0 & 0 & 0 & 0\\
0 & 0 & 0 & 0 & 0 & 0\\
\end{pmatrix}\end{split}\]

\[\begin{split}\boldsymbol{k}_{ij}^{torsion} = \begin{pmatrix}
0 & 0 & 0 & 0 & 0 & 0\\
0 & 0 & 0 & 0 & 0 & 0\\
0 & 0 & 0 & 0 & 0 & 0\\
0 & 0 & 0 & G J_x \partial_x \varphi^i_{\theta_x} \partial_x \varphi^j_{\theta_x} & 0 & 0\\
0 & 0 & 0 & 0 & 0 & 0\\
0 & 0 & 0 & 0 & 0 & 0\\
\end{pmatrix}\end{split}\]

\[\begin{split}\boldsymbol{k}_{ij}^{bending_y} = \begin{pmatrix}
0 & 0 & 0 & 0 & 0 & 0\\
0 & EI_z \partial_x \psi_{\theta_z}^i \partial_x \psi_{\theta_z}^j & 0 & 0 & 0 & EI_z \partial_x \psi_{\theta_z}^i \partial_x \varphi_{\theta_z}^j\\
& + GS\kappa_y (\partial_x \varphi_v^i - \psi_{\theta_z}^i)(\partial_x \varphi_v^j - \psi_{\theta_z}^j) & & & & + GS\kappa_y (\partial_x \varphi_v^i - \psi_{\theta_z}^i)(\partial_x \psi_v^j - \varphi_{\theta_z}^j) \\
0 & 0 & 0 & 0 & 0 & 0\\
0 & 0 & 0 & 0 & 0 & 0\\
0 & 0 & 0 & 0 & 0 & 0\\
0 & EI_z \partial_x \varphi_{\theta_z}^i \partial_x \psi_{\theta_z}^j & 0 & 0 & 0 & EI_z \partial_x \varphi_{\theta_z}^i \partial_x \varphi_{\theta_z}^j\\
& + GS\kappa_y (\partial_x \psi_v^i - \varphi_{\theta_z}^i)(\partial_x \varphi_v^j - \psi_{\theta_z}^j) & & & & + GS\kappa_y (\partial_x \psi_v^i - \varphi_{\theta_z}^i)(\partial_x \psi_v^j - \varphi_{\theta_z}^j)\\
\end{pmatrix}\end{split}\]

\[\begin{split}\boldsymbol{k}_{ij}^{bending_z} = \begin{pmatrix}
0 & 0 & 0 & 0 & 0 & 0\\
0 & 0 & 0 & 0 & 0 & 0\\
0 & 0 & EI_y \partial_x \psi_{\theta_y}^i \partial_x \psi_{\theta_y}^j & 0 & - EI_y \partial_x \psi_{\theta_y}^i \partial_x \varphi_{\theta_y}^j & 0\\
& & + GS\kappa_z (\partial_x \varphi_w^i - \psi_{\theta_y}^i)(\partial_x \varphi_w^j - \psi_{\theta_y}^j) & & - GS\kappa_z (\partial_x \varphi_w^i - \psi_{\theta_y}^i)(\partial_x \psi_w^j - \varphi_{\theta_y}^j) & \\
0 & 0 & 0 & 0 & 0 & 0\\
0 & 0 & -EI_y \partial_x \varphi_{\theta_y}^i \partial_x \psi_{\theta_y}^j & 0 & EI_y \partial_x \varphi_{\theta_y}^i \partial_x \varphi_{\theta_y}^j & 0\\
& & - GS\kappa_z (\partial_x \psi_w^i - \varphi_{\theta_y}^i)(\partial_x \varphi_w^j - \psi_{\theta_y}^j) & & + GS\kappa_z (\partial_x \psi_w^i - \varphi_{\theta_y}^i)(\partial_x \psi_w^j - \varphi_{\theta_y}^j) & \\
0 & 0 & 0 & 0 & 0 & 0\\
\end{pmatrix}\end{split}\]

### Integration of the integrand stiffness matrix

The integral that must be computed is explicited in [(307)](#equation-theory-beam-elementary-stiffness-integral).

First, notice that no hypothesis has yet been made over the evolution of the
material of geometric properties. As such, if a Gauss quadrature is to be used,
it must account for the potential variation of those properties.

In the following paragraphs, several approaches are exhibited for the
integration of the integrand stiffness matrix.

Using the expression of the integrand stiffness matrix
[(304)](#equation-theory-beam-integrand-stiffness-definition),
it is possible to determine an appropriate Gauss quadrature that should be used
in order to precisely integrate it.

The quadrature depends on the variation of:

Euler-Bernoulli

- The **shape functions** that are used to interpolate \(\boldsymbol{U}(x)\) ;
- The **material properties** \(E\) and \(G\) ;
- The **geometric properties** \(S\), \(J_x\), \(I_y\) and \(I_z\).

Timoshenko

- The **shape functions** that are used to interpolate \(\boldsymbol{U}(x)\) ;
- The **material properties** \(E\) and \(G\) ;
- The **geometric properties** \(S\), \(\kappa_y\), \(\kappa_z\), \(J_x\), \(I_y\) and \(I_z\).

In the event where all those quantities are polynomial, one can determine the
maximum polynomial degree of each term of the integrand stiffness matrix.
Choosing an appropriate quadrature yields the following:

\[\boldsymbol{K}_e = \sum_i w_i \boldsymbol{k}_e (x_i)\]

where \(x_i\) is the coordinate of the Gauss point \(i\), and \(w_i\)
is its weight in the quadrature.

Euler-Bernoulli

Note

In the case where all material and geometric properties are constant
through the element, \(\boldsymbol{k}_e(x)\) has a polynomial degree of **2**,
which means that a quadrature that has **2** Gauss points is sufficient, as
it can integrate exactly polynomial of degrees up to **3**.

Timoshenko

Note

In the case where all material and geometric properties are constant
through the element, \(\boldsymbol{k}_e(x)\) has a polynomial degree of **4**,
which means that a quadrature that has **3** Gauss points is sufficient, as
it can integrate exactly polynomial of degrees up to **5**.

#### Exact integration of the integrand stiffness matrix

Due to the low complexity of the integrand stiffness matrix, it is also possible
to exactly integrate it in some specific cases.

Note

For the remainder of this paragraph, the geometric and material properties
are supposed to be constant through the element.

Using the definition of the **elementary stiffness matrix** in
[(307)](#equation-theory-beam-elementary-stiffness-integral) and the expression of the
**virtual work of internal forces**, and
given the fact that these expressions hold for any virtual displacement, one can
choose appropriate virtual displacements that simplify the calculation of the
integrated elementary stiffness matrix.

Therefore, we will consider successively virtual displacements that are non-zero
only at a single degree of freedom.

##### Traction-compression motion

We consider the following virtual displacements:

- For \(\hat{u}_1\): \(\hat{u}(x) = \hat{u}_1 \varphi_u^1(x) = \hat{u}_1 (1-\frac{x}{L})\)
- For \(\hat{u}_2\): \(\hat{u}(x) = \hat{u}_2 \varphi_u^1(x) = \hat{u}_2 \frac{x}{L}\)

where \(L\) is the length of the element.

\[ \begin{align}\begin{aligned}\delta \hat{W}_{i, \hat{u}_1} & = - \int_x ES \partial_x u \partial_x \hat{u} dx\\& = - \int_x ES \partial_x u \partial_x (\hat{u}_1 (1-\frac{x}{L})) dx\\& = - \int_x ES \partial_x u \hat{u}_1 \frac{-1}{L} dx\\& = - \frac{-ES}{L} \hat{u}_1 \int_x \partial_x u dx\\& = - \frac{-ES}{L} \hat{u}_1 (u(L) - u(0))\end{aligned}\end{align} \]

which can also be written as:

\[\begin{split}\delta \hat{W}_{i, \hat{u}_1} = - \begin{pmatrix} u_1 & u_2 \end{pmatrix}
\frac{ES}{L} \begin{pmatrix}
1 & -1
\end{pmatrix}
\begin{pmatrix} \hat{u}_1 \\ 0 \end{pmatrix}\end{split}\]

For \(\hat{u}_2\), similar calculations give:

\[\begin{split}\delta \hat{W}_{i, \hat{u}_2} = - \begin{pmatrix} u_1 & u_2 \end{pmatrix}
\frac{ES}{L} \begin{pmatrix}
-1 & 1
\end{pmatrix}
\begin{pmatrix} 0 \\ \hat{u}_2 \end{pmatrix}\end{split}\]

Both equations give the integration of \(\boldsymbol{k}_{ij}^{traction}\), as
defined in the decomposition of the integrand stiffness matrix
[(308)](#equation-theory-beam-stiffness-decomposition):

(309)\[\begin{split}\boldsymbol{K}_e^{traction} = \frac{ES}{L} \begin{pmatrix}
1 & -1 \\
-1 & 1
\end{pmatrix}\end{split}\]

##### Torsion motion

Doing a similar work as was performed for the traction-compression motion, one easily
deduces that:

(310)\[\begin{split}\boldsymbol{K}_e^{torsion} = \frac{GJ_x}{L} \begin{pmatrix}
1 & -1 \\
-1 & 1
\end{pmatrix}\end{split}\]

##### Bending motion in the (xOz) plane

Euler-Bernoulli

Before choosing the virtual displacements, let us first write the virtual work
in the most general case:

(311)\[ \begin{align}\begin{aligned}- \delta \hat{W}_i & = \int_x EI_y \partial_x \theta_y \partial_x \hat{\theta_y} dx\\& = E I_y [\theta_y(L)\partial_x \hat{\theta_y}(L) - \theta_y(0)\partial_x \hat{\theta_y}(0)] - \int_x E I_y \theta_y \partial^2_x \hat{\theta_y} dx\\& = E I_y [\theta_y(L)\partial_x \hat{\theta_y}(L) - \theta_y(0)\partial_x \hat{\theta_y}(0)] - \int_x E I_y \partial_x w \partial^3_x \hat{w} dx\\& = E I_y [\theta_y(L)\partial_x \hat{\theta_y}(L) - \theta_y(0)\partial_x \hat{\theta_y}(0) - w(L) \partial^3_x\hat{w}(L) + w(0) \partial^3_x\hat{w}(0)] + \int_x E I_y w \partial^4_x \hat{w} dx\end{aligned}\end{align} \]

To exhibit an exact integral, i.e. a virtual work that can be written as such:

(312)\[- \delta \hat{W}_i = E I_y [\theta_y(L)\partial_x \hat{\theta_y}(L) - \theta_y(0)\partial_x \hat{\theta_y}(0) - w(L) \partial^3_x\hat{w}(L) + w(0) \partial^3_x\hat{w}(0)]\]

one must find test-functions that set the spare integral
[(311)](#equation-theory-beam-stifness-exact-bendingy-euler)
at zero, which means that it is sufficient that the virtual displacement verifies
the following differential equation:

\[\partial_x^4 \hat{w} = 0\]

which is already a condition that the shape functions verify
[(300)](#equation-theory-beam-static-conditions-euler).

Therefore, the following virtual displacements are chosen successively to
determine the expression of the stiffness matrix (virtual rotations are simply
deduced by differentiation):

- For \(\hat{w}_1\):

\[ \begin{align}\begin{aligned}\hat{w}(x) & = \hat{w}_1 \varphi_w^1(x)\\\hat{\theta_y}(x) & = -\hat{w}_1 \partial_x \varphi_w^1(x)\end{aligned}\end{align} \]

- For \(\hat{w}_2\):

\[ \begin{align}\begin{aligned}\hat{w}(x) & = \hat{w}_2 \varphi_w^2(x)\\\hat{\theta_y}(x) & = - \hat{w}_2 \partial_x \varphi_w^2(x)\end{aligned}\end{align} \]

- For \(\hat{\theta_y}_1\)

\[ \begin{align}\begin{aligned}\hat{w}(x) & = -\hat{\theta_y}_1 \varphi_{\theta_y}^1(x)\\\hat{\theta_y}(x) & = \hat{\theta_y}_1 \partial_x \varphi_{\theta_y}^1(x)\end{aligned}\end{align} \]

- For \(\hat{\theta_y}_2\)

\[ \begin{align}\begin{aligned}\hat{w}(x) & = -\hat{\theta_y}_2 \varphi_{\theta_y}^2(x)\\\hat{\theta_y}(x) & = \hat{\theta_y}_2 \partial_x \varphi_{\theta_y}^2(x)\end{aligned}\end{align} \]

Plugging in each couple of functions in [(312)](#equation-theory-beam-exact-bendingy2-euler),
one can obtain the elementary stiffness matrix in bending:

(313)\[\begin{split}\boldsymbol{K}_e^{bending_y} = \frac{12EI_y}{L^3} \begin{pmatrix}
1 & -\frac{L}{2} & -1 & -\frac{L}{2} \\
-\frac{L}{2} & \frac{L^2}{3} & \frac{L}{2} & \frac{L^2}{6} \\
-1 & \frac{L}{2} & 1 & \frac{L}{2} \\
-\frac{L}{2} & \frac{L^2}{6} & \frac{L}{2} & \frac{L^2}{3}
\end{pmatrix}\end{split}\]

Note

One could notice that this results actually correspond to **Timoshenko's beam**
where \(\Phi_y = 0\), which translates into \(L^2 >> \frac{12EI_y}{GS\kappa_z}\),
which is true if the beam is slender. In other words, Timoshenko's beam and
Euler's beam converge to the same solution as the beam becomes more slender,
i.e. as the contribution of shear effects becomes smaller.

Timoshenko

Before choosing the virtual displacements, let us first write the virtual work
in the most general case:

(314)\[ \begin{align}\begin{aligned}- \delta \hat{W}_i & = \int_x (GS \kappa_z (\partial_x w + \theta_y)(\partial_x \hat{w} + \hat{\theta_y}) + EI_y \partial_x \theta_y \partial_x \hat{\theta_y}) dx\\& = GS \kappa_z [w(L)[\partial_x(\hat{w})(L) + \hat{\theta_y}(L)] - w(0)[\partial_x(\hat{w})(0) + \hat{\theta_y}(0)]]\\& + E I_y [\theta_y(L)\partial_x (\hat{\theta_y})(L) - \theta_y(0)\partial_x (\hat{\theta_y})(0)]\\& - \int_x G S \kappa_z w (\partial_x^2 \hat{w} + \partial_x \hat{\theta_y}) dx\\& - \int_x \theta_y (EI_y \partial_x^2 \hat{\theta_y} - GS\kappa_z (\partial_x \hat{w} + \hat{\theta_y})) dx\end{aligned}\end{align} \]

To exhibit an exact integral, i.e. a virtual work that can be written as such:

\[ \begin{align}\begin{aligned}- \delta \hat{W}_i & = GS \kappa_z [w(L)[\partial_x(\hat{w})(L) + \hat{\theta_y}(L)] - w(0)[\partial_x(\hat{w})(0) + \hat{\theta_y}(0)]]\\& + E I_y [\theta_y(L)\partial_x (\hat{\theta_y})(L) - \theta_y(0)\partial_x (\hat{\theta_y})(0)]\end{aligned}\end{align} \]

one must find test-functions that set the spare integral in
[(314)](#equation-theory-beam-stifness-exact-bendingy-timoshenko)
at zero, which means that it is sufficient that the virtual displacement verifies
the following differential equations:

(315)\[ \begin{align}\begin{aligned}\partial_x^2 \hat{w} + \partial_x \hat{\theta_y} & = 0\\EI_y \partial_x^2 \hat{\theta_y} - GS\kappa_z (\partial_x \hat{w} + \hat{\theta_y}) & = 0\end{aligned}\end{align} \]

which is already a condition that the shape functions verify
[(301)](#equation-theory-beam-static-conditions-timoshenko).

Therefore, the following virtual displacements are chosen successively to
determine the expression of the stiffness matrix:

- For \(\hat{w}_1\):

\[ \begin{align}\begin{aligned}\hat{w}(x) & = \hat{w}_1 \varphi_w^1(x)\\\hat{\theta_y}(x) & = -\hat{w}_1 \psi_{\theta_y}^1(x)\end{aligned}\end{align} \]

- For \(\hat{w}_2\):

\[ \begin{align}\begin{aligned}\hat{w}(x) & = \hat{w}_2 \varphi_w^2(x)\\\hat{\theta_y}(x) & = -\hat{w}_2 \psi_{\theta_y}^2(x)\end{aligned}\end{align} \]

- For \(\hat{\theta_y}_1\)

\[ \begin{align}\begin{aligned}\hat{w}(x) & = -\hat{\theta_y}_1 \psi_w^1(x)\\\hat{\theta_y}(x) & = \hat{\theta_y}_1 \varphi_{\theta_y}^1(x)\end{aligned}\end{align} \]

- For \(\hat{\theta_y}_2\)

\[ \begin{align}\begin{aligned}\hat{w}(x) & = -\hat{\theta_y}_2 \psi_w^2(x)\\\hat{\theta_y}(x) & = \hat{\theta_y}_2 \varphi_{\theta_y}^2(x)\end{aligned}\end{align} \]

Plugging in each couple of functions in [(315)](#equation-theory-beam-exact-bendingy2-timoshenko),
one can obtain the elementary stiffness matrix in bending:

\[\begin{split}\boldsymbol{K}_e^{bending_y} = \frac{12EI_y}{L^3(1+\Phi_y)} \begin{pmatrix}
1 & -\frac{L}{2} & -1 & -\frac{L}{2} \\
-\frac{L}{2} & \frac{(4+\Phi_y)L^2}{12} & \frac{L}{2} & \frac{(2-\Phi_y)L^2}{12} \\
-1 & \frac{L}{2} & 1 & \frac{L}{2} \\
-\frac{L}{2} & \frac{(2-\Phi_y)L^2}{12} & \frac{L}{2} & \frac{(4+\Phi_y)L^2}{12}
\end{pmatrix}\end{split}\]

##### Bending motion in the (xOy) plane

The methodology is similar for the other bending axis. The
differential equation that the test-functions must meet becomes:

Euler-Bernoulli

\[\partial_x^4 \hat{v} = 0\]

The same calculation steps give the following elementary stiffness matrix:

\[\begin{split}\boldsymbol{K}_e^{bending_z} = \frac{12EI_z}{L^3} \begin{pmatrix}
1 & \frac{L}{2} & -1 & \frac{L}{2} \\
\frac{L}{2} & \frac{L^2}{3} & -\frac{L}{2} & \frac{L^2}{6} \\
-1 & -\frac{L}{2} & 1 & -\frac{L}{2} \\
\frac{L}{2} & \frac{L^2}{6} & -\frac{L}{2} & \frac{L^2}{3}
\end{pmatrix}\end{split}\]

Timoshenko

\[ \begin{align}\begin{aligned}\partial_x^2 \hat{v} - \partial_x \hat{\theta_z} & = 0\\E I_z \partial_x^2 \hat{\theta_y} + G S \kappa_y (\partial_x\hat{v} - \hat{\theta_y}) & = 0\end{aligned}\end{align} \]

The same calculation steps give the following elementary stiffness matrix:

\[\begin{split}\boldsymbol{K}_e^{bending_z} = \frac{12EI_z}{L^3(1+\Phi_z)} \begin{pmatrix}
1 & \frac{L}{2} & -1 & \frac{L}{2} \\
\frac{L}{2} & \frac{(4+\Phi_z)L^2}{12} & -\frac{L}{2} & \frac{(2-\Phi_z)L^2}{12} \\
-1 & -\frac{L}{2} & 1 & -\frac{L}{2} \\
\frac{L}{2} & \frac{(2-\Phi_z)L^2}{12} & -\frac{L}{2} & \frac{(4+\Phi_z)L^2}{12}
\end{pmatrix}\end{split}\]

##### Assembling the elementary stiffness matrix

Assembling the matrix given by the four previous ones gives an elementary stiffness
matrix for the element that has the same profile as sum of the matrices given
in [(308)](#equation-theory-beam-stiffness-decomposition).

In the current section, the assembled elementary stiffness matrix is the
product of an exact integral over the element, which guarantees that the
finite element solution will be exact at the element nodes.

## Determination of the consistent mass matrix

### Definition of the mass matrix

The **elementary mass matrix** \(\boldsymbol{M}_e\) of the element is
defined through the virtual work of the **inertial forces** for any given virtual
displacement:

\[\delta \hat{W_a} = \int_V \rho \frac{\partial^2 \boldsymbol{u}}{\partial t^2} \boldsymbol{\hat{u}} dV
= \boldsymbol{u}_e^{\transpose{}} \boldsymbol{M}_e \boldsymbol{\hat{u}}_e\]

### Determination of the integrand mass matrix

Using the expression of the displacement field [(284)](#equation-theory-beam-displacement-simplified):

\[ \begin{align}\begin{aligned}\hat{\delta W_a} & = \int_V \rho \frac{\partial^2 \boldsymbol{u}}{\partial t^2}
\boldsymbol{\hat{u}} dV\\& = \int_V \rho [(\partial_t^2 u + z \partial_t^2 \theta_y - y \partial_t^2 \theta_z)(\hat{u}
+ z \hat{\theta_y} - y \hat{\theta_z}) + (\partial_t^2 v - z \partial_t^2 \theta_x)(\hat{v}
- z \hat{\theta_x}) + (\partial_t^2 w + y \partial_t^2 \theta_x)(\hat{w} + y \hat{\theta_x})] dV\end{aligned}\end{align} \]

Using the fact that the [neutral axis is positioned at the center of
inertia](#theory-beam-geom-integrals), the previous expression can be simplified
by omitting the terms that are linear in \(y\), \(z\) and \(yz\):

(316)\[ \begin{align}\begin{aligned}\hat{\delta W_a} & = \int_V \rho [\partial_t^2 u \hat{u} + \partial_t^2 v \hat{v}
+ \partial_t^2 w \hat{w} + (y^2+z^2)\partial_t^2 \theta_x \hat{\theta_x}
+ z^2 \partial_t^2 \theta_y \hat{\theta_y}
+ y^2 \partial_t^2 \theta_z \hat{\theta_z}] dV\\& = \int_x [\rho S \partial_t^2 u \hat{u} + \rho S \partial_t^2 v \hat{v}
+ \rho S \partial_t^2 w \hat{w} + \rho J \partial_t^2 \theta_x \hat{\theta_x}
+ \rho I_y \partial_t^2 \theta_y \hat{\theta_y}
+ \rho I_z \partial_t^2 \theta_z \hat{\theta_z}] dx\end{aligned}\end{align} \]

Euler-Bernoulli

Neglecting the inertial terms corresponding to the rotation of the cross-section
(see the [Euler-Bernoulli beam hypotheses](#theory-beam-hypotheses)),
one has:

\[\hat{\delta W_a} = \int_x [\rho S \partial_t^2 u \hat{u}
+ \rho S \partial_t^2 v \hat{v} + \rho S \partial_t^2 w \hat{w}
+ \rho J \partial_t^2 \theta_x \hat{\theta_x}] dx\]

Timoshenko

(*Intentionally left blank*)

Re-writing the expression under the integral as a bi-linear form, one deduces that:

(317)\[\hat{\delta W_a} = \int_x \partial_t^2 \boldsymbol{U}^{\transpose{}} (x) \boldsymbol{C} \boldsymbol{\hat{U}}(x) dx\]

with:

Euler-Bernoulli

\[\begin{split}\boldsymbol{C} = \begin{pmatrix}
\rho S & 0 & 0 & 0 & 0 & 0 \\
0 & \rho S & 0 & 0 & 0 & 0 \\
0 & 0 & \rho S & 0 & 0 & 0 \\
0 & 0 & 0 & \rho J & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0
\end{pmatrix}\end{split}\]

Timoshenko

\[\begin{split}\boldsymbol{C} = \begin{pmatrix}
\rho S & 0 & 0 & 0 & 0 & 0 \\
0 & \rho S & 0 & 0 & 0 & 0 \\
0 & 0 & \rho S & 0 & 0 & 0 \\
0 & 0 & 0 & \rho J & 0 & 0 \\
0 & 0 & 0 & 0 & \rho I_y & 0 \\
0 & 0 & 0 & 0 & 0 & \rho I_z
\end{pmatrix}\end{split}\]

Using the shape functions interpolation, and under the hypothesis that the second
derivative of the DOFs is interpolated similarly inside the element as the DOFs
themselves, the expression of the virtual work of inertial forces
[(317)](#equation-theory-beam-mass-matrix-bilinear) yields:

\[ \begin{align}\begin{aligned}\delta \hat{W_a} & = \int_{x} \partial_t^2\boldsymbol{u}_e^{\transpose{}} \boldsymbol{N}(x)^{\transpose{}}
\boldsymbol{C} \boldsymbol{N}(x)\boldsymbol{\hat{u_e}} dx\\& = \partial_t^2\boldsymbol{u}_e^{\transpose{}} \left( \int_{x} \boldsymbol{N}(x)^{\transpose{}}
\boldsymbol{C} \boldsymbol{N}(x) dx \right) \boldsymbol{\hat{u_e}}\end{aligned}\end{align} \]

Thus defining the **integrand mass matrix** \(\boldsymbol{m}_e\):

\[\boldsymbol{m}_e(x) = \boldsymbol{N}(x)^{\transpose{}} \boldsymbol{C} \boldsymbol{N}(x)\]

The **elementary mass matrix** \(\boldsymbol{M}_e\) being related to
the integrand mass matrix this way:

(318)\[\boldsymbol{M}_e = \int_x \boldsymbol{m}_e(x) dx\]

Expliciting \(\boldsymbol{m}_e\):

(319)\[\begin{split}\boldsymbol{m}_e = \begin{pmatrix}
\boldsymbol{m}_{11} & \boldsymbol{m}_{12} \\
\boldsymbol{m}_{21} & \boldsymbol{m}_{22} \\
\end{pmatrix}\end{split}\]

Euler-Bernoulli

(320)\[\begin{split}\boldsymbol{m}_{ij} = \begin{pmatrix}
\rho S \varphi_u^i \varphi_u^j & 0 & 0 & 0 & 0 & 0 \\
0 & \rho S \varphi_v^i \varphi_v^j & 0 & 0 & 0 & \rho S \varphi_v^i \varphi_{\theta_z}^j \\
0 & 0 & \rho S \varphi_w^i \varphi_w^j& 0 & - \rho S \varphi_w^i \varphi_{\theta_y}^j & 0 \\
0 & 0 & 0 & \rho J \varphi_{\theta_x}^i \varphi_{\theta_x}^j & 0 & 0 \\
0 & 0 & - \rho S \varphi_{\theta_y}^i \varphi_w^j & 0 & \rho S \varphi_{\theta_y}^i \varphi_{\theta_y}^j & 0 \\
0 & \rho S \varphi_{\theta_z}^i \varphi_v^j & 0 & 0 & 0 & \rho S \varphi_{\theta_z}^i \varphi_{\theta_z}^j \\
\end{pmatrix}\end{split}\]

Timoshenko

\[\begin{split}\boldsymbol{m}_{ij} = \begin{pmatrix}
\rho S \varphi_u^i \varphi_u^j & 0 & 0 & 0 & 0 & 0 \\
0 & \rho S \varphi_v^i \varphi_v^j & 0 & 0 & 0 & \rho S \varphi_v^i \psi_{v}^j \\
& + \rho I_z \psi_{\theta_z}^i \psi_{\theta_z}^j & & & & + \rho I_z \psi_{\theta_z}^i\varphi_{\theta_z}^j \\
0 & 0 & \rho S \varphi_w^i \varphi_w^j & 0 & - \rho S \varphi_w^i \psi_{w}^j & 0 \\
& & + \rho I_y \psi_{\theta_y}^i \psi_{\theta_y}^j & & - \rho I_y \psi_{\theta_y}^i\varphi_{\theta_y}^j & \\
0 & 0 & 0 & \rho J \varphi_{\theta_x}^i \varphi_{\theta_x}^j & 0 & 0 \\
0 & 0 & - \rho S \psi_{w}^i \varphi_w^j & 0 & \rho S \psi_{w}^i \psi_{w}^j & 0 \\
& & - \rho I_y \varphi_{\theta_y}^i \psi_{\theta_y}^j & & + \rho I_y \varphi_{\theta_y}^i \varphi_{\theta_y}^j & \\
0 & \rho S \psi_{v}^i \varphi_v^j & 0 & 0 & 0 & \rho S \psi_{v}^i \psi_{v}^j \\
& + \rho I_z \varphi_{\theta_z}^i \psi_{\theta_z}^j & & & & + \rho I_z \varphi_{\theta_z}^i \varphi_{\theta_z}^j \\
\end{pmatrix}\end{split}\]

The **integrand mass matrix** can be decomposed in such a
way that the different motions are clearly distinguished:

\[\boldsymbol{m}_{ij} = \boldsymbol{m}_{ij}^{traction} + \boldsymbol{m}_{ij}^{torsion}
+ \boldsymbol{m}_{ij}^{bending_{y}} + \boldsymbol{m}_{ij}^{bending_{z}}\]

where:
:   - \(\boldsymbol{m}_{ij}^{traction}\) contains only the term in
      \(\varphi_u\) ;
    - \(\boldsymbol{m}_{ij}^{torsion}\) contains only the term in
      \(\varphi_{\theta_x}\) ;
    - \(\boldsymbol{m}_{ij}^{bending_y}\) contains the terms in
      \(\varphi_{w}\) and \(\varphi_{\theta_y}\) ;
    - \(\boldsymbol{m}_{ij}^{bending_z}\) contains the terms in
      \(\varphi_{v}\) and \(\varphi_{\theta_z}\).

### Integration of the integrand mass matrix

The integral that must be computed is explicited in [(318)](#equation-theory-beam-elementary-mass-integral).

First, notice that no hypothesis has yet been made over the evolution of the
material of geometric properties. As such, if a Gauss quadrature is to be used,
it must account for the potential variation of those properties.

In the following paragraphs, two different approaches are exhibited for the
integration of the integrand stiffness matrix.

Also note that in order to assemble the **consistent** mass matrix, one has to
choose an interpolation and shape functions that are consistent with those that
were chosen for the stiffness matrix.

#### Classic integration using Gauss quadrature

Using the expression of the integrand mass matrix [(319)](#equation-theory-beam-integrand-mass),
it is possible to determine an appropriate Gauss quadrature that should be used
in order to precisely integrate it.

The quadrature depends on the variation of:

Euler-Bernoulli

- The **shape functions** that are used to interpolate \(\boldsymbol{u}(x)\) ;
- The **material properties** \(\rho\) ;
- The **geometric properties** \(S\) and \(J\).

Timoshenko

- The **shape functions** that are used to interpolate \(\boldsymbol{u}(x)\) ;
- The **material properties** \(\rho\) ;
- The **geometric properties** \(S\), \(J\), \(I_y\) and \(I_z\).

In the event where all those quantities are polynomial, one can determine the
maximum polynomial degree of each term of the integrand mass matrix.
Choosing an appropriate quadrature yields the following:

\[\boldsymbol{M}_e = \sum_i w_i \boldsymbol{m}_e (x_i)\]

where \(x_i\) is the coordinate of the Gauss point \(i\), and \(w_i\)
is its weight in the quadrature.

Note

In the case where all material and geometric properties are constant
through the element, given that shape functions for the \(u\) and
\(\theta_x\) DOFs are linear, and cubic for the rest of the DOFs,
\(\boldsymbol{m}_e(x)\) would have a polynomial degree of **6**, which means
that a quadrature that has **4** Gauss points is sufficient, as it can integrate
exactly polynomial of degrees up to **7**.

#### Exact integration of the integrand mass matrix

Due to the low complexity of the integrand mass matrix, it is also possible
to exactly integrate it in some specific cases.

Note

For the remainder of this paragraph, the geometric and material properties
are supposed to be constant through the element.

To obtain the **consistent** mass matrix, one should choose the same shape
functions and interpolation as the one used in [Exact integration of the integrand stiffness matrix](#theory-beam-exact-integration-stiffness).

Plugging in the corresponding shape functions in the [(319)](#equation-theory-beam-integrand-mass)
one directly deduces the exact expression of the **integrand** mass matrix, and
can thus integrate it exactly.

##### Traction-compression motion

Integrating exactly the terms of the **integrand** mass matrix yields the
following expression for its traction-compression subterm:

(321)\[\begin{split}\boldsymbol{M}_e^{traction} = \rho S L \begin{pmatrix}
\frac{1}{3} & \frac{1}{6} \\
\frac{1}{6} & \frac{1}{3}
\end{pmatrix}\end{split}\]

##### Torsion motion

Integrating exactly the terms of the **integrand** mass matrix yields the
following expression for its torsion subterm:

(322)\[\begin{split}\boldsymbol{M}_e^{torsion} = \rho J L \begin{pmatrix}
\frac{1}{3} & \frac{1}{6} \\
\frac{1}{6} & \frac{1}{3}
\end{pmatrix}\end{split}\]

##### Bending motion in the (xOz) plane

Integrating exactly the terms of the **integrand** mass matrix yields the
following expression for its bending subterm along the \((xOz)\) plane:

Euler-Bernoulli

\[\begin{split}\boldsymbol{M}_e^{bending_y} = \rho S L \begin{pmatrix}
\frac{13}{35} & \frac{-11 L}{210} & \frac{9}{70} & \frac{13 L}{420} \\
\frac{-11 L}{210} & \frac{L^2}{105} & \frac{-13 L}{420} & \frac{-L^2}{140} \\
\frac{9}{70} & \frac{-13 L}{420} & \frac{13}{35} & \frac{11 L}{210} \\
\frac{13 L}{420} & \frac{-L^2}{140} & \frac{11 L}{210} & \frac{L^2}{105}
\end{pmatrix}\end{split}\]

Timoshenko

\[\begin{split}\boldsymbol{M}_e^{bending_y} & = \frac{\rho S L}{(1+\Phi_y)^2} \begin{pmatrix}
\frac{13}{35} & \frac{-11 L}{210} & \frac{9}{70} & \frac{13 L}{420} \\
\frac{-11 L}{210} & \frac{L^2}{105} & \frac{-13 L}{420} & \frac{-L^2}{140} \\
\frac{9}{70} & \frac{-13 L}{420} & \frac{13}{35} & \frac{11 L}{210} \\
\frac{13 L}{420} & \frac{-L^2}{140} & \frac{11 L}{210} & \frac{L^2}{105}
\end{pmatrix} & \\
& + \frac{\rho S L \Phi_y}{(1+\Phi_y)^2} \begin{pmatrix}
\frac{7}{10} & \frac{-11 L}{120} & \frac{3}{10} & \frac{3 L}{40} \\
\frac{-11 L}{120} & \frac{L^2}{60} & \frac{-3 L}{40} & \frac{-L^2}{60} \\
\frac{3}{10} & \frac{-3 L}{40} & \frac{7}{10} & \frac{11 L}{120} \\
\frac{3 L}{40} & \frac{-L^2}{60} & \frac{11 L}{120} & \frac{L^2}{60}
\end{pmatrix}
& + \frac{\rho S L \Phi_y^2}{(1+\Phi_y)^2} \begin{pmatrix}
\frac{1}{3} & \frac{-L}{24} & \frac{1}{6} & \frac{L}{24} \\
\frac{-L}{24} & \frac{L^2}{120} & \frac{-L}{24} & \frac{-L^2}{120} \\
\frac{1}{6} & \frac{-L}{24} & \frac{1}{3} & \frac{L}{24} \\
\frac{L}{24} & \frac{-L^2}{120} & \frac{L}{24} & \frac{L^2}{120}
\end{pmatrix} \\
& = \frac{\rho I_y}{L(1+\Phi_y)^2} \begin{pmatrix}
\frac{6}{5} & \frac{-L}{10} & \frac{-6}{5} & \frac{- L}{10} \\
\frac{-L}{10} & \frac{2L^2}{15} & \frac{L}{10} & \frac{-L^2}{30} \\
\frac{-6}{5} & \frac{L}{10} & \frac{6}{5} & \frac{L}{10} \\
\frac{-L}{10} & \frac{-L^2}{30} & \frac{L}{10} & \frac{2L^2}{15}
\end{pmatrix} & \\
& + \frac{\rho I_y\Phi_y}{L(1+\Phi_y)^2} \begin{pmatrix}
0 & \frac{L}{2} & 0 & \frac{L}{2} \\
\frac{L}{2} & \frac{L^2}{6} & \frac{-L}{2} & \frac{-L^2}{6} \\
0 & \frac{-L}{2} & 0 & \frac{-L}{2} \\
\frac{L}{2} & \frac{-L^2}{6} & \frac{-L}{2} & \frac{L^2}{6}
\end{pmatrix}
& + \frac{\rho I_y\Phi_y^2}{L(1+\Phi_y)^2} \begin{pmatrix}
0 & 0 & 0 & 0 \\
0 & \frac{L^2}{3} & 0 & \frac{L^2}{6} \\
0 & 0 & 0 & 0 \\
0 & \frac{L^2}{6} & 0 & \frac{L^2}{3}
\end{pmatrix}\end{split}\]

##### Bending motion in the (xOy) plane

Integrating exactly the terms of the **integrand** mass matrix yields the
following expression for its bending subterm along the \((xOy)\) plane:

Euler-Bernoulli

\[\begin{split}\boldsymbol{M}_e^{bending_z} = \rho S L \begin{pmatrix}
\frac{13}{35} & \frac{11 L}{210} & \frac{9}{70} & \frac{-13 L}{420} \\
\frac{11 L}{210} & \frac{L^2}{105} & \frac{13 L}{420} & \frac{-L^2}{140} \\
\frac{9}{70} & \frac{13 L}{420} & \frac{13}{35} & \frac{-11 L}{210} \\
\frac{-13 L}{420} & \frac{-L^2}{140} & \frac{-11 L}{210} & \frac{L^2}{105}
\end{pmatrix}\end{split}\]

Timoshenko

\[\begin{split}\boldsymbol{M}_e^{bending_z} & = \frac{\rho S L}{(1+\Phi_z)^2} \begin{pmatrix}
\frac{13}{35} & \frac{11 L}{210} & \frac{9}{70} & \frac{-13 L}{420} \\
\frac{11 L}{210} & \frac{L^2}{105} & \frac{13 L}{420} & \frac{-L^2}{140} \\
\frac{9}{70} & \frac{13 L}{420} & \frac{13}{35} & \frac{-11 L}{210} \\
\frac{-13 L}{420} & \frac{-L^2}{140} & \frac{-11 L}{210} & \frac{L^2}{105}
\end{pmatrix} & \\
& + \frac{\rho S L \Phi_z}{(1+\Phi_z)^2} \begin{pmatrix}
\frac{7}{10} & \frac{11 L}{120} & \frac{3}{10} & \frac{-3 L}{40} \\
\frac{11 L}{120} & \frac{L^2}{60} & \frac{3 L}{40} & \frac{-L^2}{60} \\
\frac{3}{10} & \frac{3 L}{40} & \frac{7}{10} & \frac{-11 L}{120} \\
\frac{-3 L}{40} & \frac{-L^2}{60} & \frac{-11 L}{120} & \frac{L^2}{60}
\end{pmatrix}
& + \frac{\rho S L \Phi_z^2}{(1+\Phi_z)^2} \begin{pmatrix}
\frac{1}{3} & \frac{L}{24} & \frac{1}{6} & \frac{-L}{24} \\
\frac{L}{24} & \frac{L^2}{120} & \frac{L}{24} & \frac{-L^2}{120} \\
\frac{1}{6} & \frac{L}{24} & \frac{1}{3} & \frac{-L}{24} \\
\frac{-L}{24} & \frac{-L^2}{120} & \frac{-L}{24} & \frac{L^2}{120}
\end{pmatrix} \\
& = \frac{\rho I_y}{L(1+\Phi_z)^2} \begin{pmatrix}
\frac{6}{5} & \frac{L}{10} & \frac{-6}{5} & \frac{L}{10} \\
\frac{L}{10} & \frac{2L^2}{15} & \frac{-L}{10} & \frac{-L^2}{30} \\
\frac{-6}{5} & \frac{-L}{10} & \frac{6}{5} & \frac{-L}{10} \\
\frac{L}{10} & \frac{-L^2}{30} & \frac{-L}{10} & \frac{2L^2}{15}
\end{pmatrix} & \\
& + \frac{\rho I_y\Phi_z}{L(1+\Phi_z)^2} \begin{pmatrix}
0 & \frac{-L}{2} & 0 & \frac{-L}{2} \\
\frac{-L}{2} & \frac{L^2}{6} & \frac{L}{2} & \frac{-L^2}{6} \\
0 & \frac{L}{2} & 0 & \frac{L}{2} \\
\frac{-L}{2} & \frac{-L^2}{6} & \frac{L}{2} & \frac{L^2}{6}
\end{pmatrix}
& + \frac{\rho I_y\Phi_z^2}{L(1+\Phi_z)^2} \begin{pmatrix}
0 & 0 & 0 & 0 \\
0 & \frac{L^2}{3} & 0 & \frac{L^2}{6} \\
0 & 0 & 0 & 0 \\
0 & \frac{L^2}{6} & 0 & \frac{L^2}{3}
\end{pmatrix}\end{split}\]

##### Assembling the elementary mass matrix

Assembling the matrix given by the four previous ones gives an elementary mass
matrix for the element that has the same profile as the matrix given in
[(319)](#equation-theory-beam-integrand-mass).

In the current section, the assembled elementary mass matrix is the
product of an exact integral over the element, which guarantees that the
finite element solution will be exact at the element nodes.

## Mass matrix lumping

Euler-Bernoulli

The mass matrix that was determined in [(320)](#equation-theory-beam-mass-matrix-euler) is the
**consistent** mass matrix associated with the shape functions chosen for the
previously determined stiffness matrix. As such, and as
it shows, it is by no mean diagonal,
which hardens the calculation of its inverse. **Lumping the mass matrix**
actually offers a way to write the mass matrix as a diagonal matrix, which
trivializes its inversion.

Moreover, in order to optimize the number of matrices inversion, one aims at the
diagonalization, thus lumping, of the mass matrix expressed in the global coordinate
system.

Several lumping techniques exist. Techniques that are implemented in MANTA
are presented hereafter.

Timoshenko

Note

Theory relative to Timoshenko beams has not been written yet, as
such calculations are still impossible in MANTA. Theory will
be completed once the associated formulations will be developed.

### General expression of a lumped mass matrix

Euler-Bernoulli

The lumped mass matrix should be diagonal in the global coordinate system. In
order to assemble the matrix in the local coordinate system and to be able
to guarantee that the global matrix stays diagonal at each time step, regardless
of the rotation basis, the mass matrix should be diagonal in both coordinate systems.
Using thr same notations as in [(283)](#equation-theory-beam-transition-matrices), one has the
following (the same holds for both nodes treated simultaneously, as
\(\boldsymbol{\tilde{P}}\) is **block diagonal**):

\[\begin{split}\boldsymbol{m_{ii, global}} & = \begin{pmatrix}
\boldsymbol{P} & 0 \\
0 & \boldsymbol{P} \\
\end{pmatrix} \boldsymbol{m_{ii, local}} \begin{pmatrix}
\boldsymbol{P}^{\transpose{}} & 0 \\
0 & \boldsymbol{P}^{\transpose{}} \\
\end{pmatrix} \\
\begin{pmatrix}
\beta_1 & 0 & 0 & 0 & 0 & 0 \\
0 & \beta_2 & 0 & 0 & 0 & 0 \\
0 & 0 & \beta_3 & 0 & 0 & 0 \\
0 & 0 & 0 & \delta_1 & 0 & 0 \\
0 & 0 & 0 & 0 & \delta_2 & 0 \\
0 & 0 & 0 & 0 & 0 & \delta_3 \\
\end{pmatrix} & = \begin{pmatrix}
\boldsymbol{P} & 0 \\
0 & \boldsymbol{P} \\
\end{pmatrix} \begin{pmatrix}
\alpha_1 & 0 & 0 & 0 & 0 & 0 \\
0 & \alpha_2 & 0 & 0 & 0 & 0 \\
0 & 0 & \alpha_3 & 0 & 0 & 0 \\
0 & 0 & 0 & \gamma_1 & 0 & 0 \\
0 & 0 & 0 & 0 & \gamma_2 & 0 \\
0 & 0 & 0 & 0 & 0 & \gamma_3 \\
\end{pmatrix} \begin{pmatrix}
\boldsymbol{P}^{\transpose{}} & 0 \\
0 & \boldsymbol{P}^{\transpose{}} \\
\end{pmatrix}\end{split}\]

and on the anti-diagonal:

\[\boldsymbol{m_{12, global}} = \boldsymbol{m_{21, global}}
= \boldsymbol{m_{12, local}} = \boldsymbol{m_{21, local}} = \boldsymbol{0}\]

Let us first look at the top left corner of the diagonal matrices. One has:

\[\begin{split}\begin{pmatrix}
\beta_1 & 0 & 0 \\
0 & \beta_2 & 0 \\
0 & 0 & \beta_3 \\
\end{pmatrix} & = \boldsymbol{P} \begin{pmatrix}
\alpha_1 & 0 & 0 \\
0 & \alpha_2 & 0 \\
0 & 0 & \alpha_3 \\
\end{pmatrix} \boldsymbol{P}^{\transpose{}}\end{split}\]

which must hold for every possible rotation matrix \(\boldsymbol{P}\).

As \(\boldsymbol{P}\) is a **rotation matrix**, the equation hereabove must
hold for three particular rotation matrices matrices,
\(\boldsymbol{R}_x(\theta)\), \(\boldsymbol{R}_y(\theta)\) and
\(\boldsymbol{R}_z(\theta)\) written hereunder:

\[\begin{split}\boldsymbol{R}_x(\theta) & = \begin{pmatrix}
1 & 0 & 0\\
0 & \cos(\theta) & -\sin(\theta)\\
0 & \sin(\theta) & \cos(\theta)\\
\end{pmatrix} \\
\boldsymbol{R}_y(\theta) & = \begin{pmatrix}
\cos(\theta) & 0 & \sin(\theta)\\
0 & 1 & 0\\
-\sin(\theta) & 0 & \cos(\theta)\\
\end{pmatrix} \\
\boldsymbol{R}_z(\theta) & = \begin{pmatrix}
\cos(\theta) & -\sin(\theta) & 0\\
\sin(\theta) & \cos(\theta) & 0\\
0 & 0 & 1\\
\end{pmatrix}\end{split}\]

In particular, for \(\boldsymbol{R}_x(\theta)\):

\[\begin{split}\begin{pmatrix}
\beta_1 & 0 & 0 \\
0 & \beta_2 & 0 \\
0 & 0 & \beta_3 \\
\end{pmatrix} & = \begin{pmatrix}
1 & 0 & 0\\
0 & \cos(\theta) & -\sin(\theta)\\
0 & \sin(\theta) & \cos(\theta)\\
\end{pmatrix} \begin{pmatrix}
\alpha_1 & 0 & 0 \\
0 & \alpha_2 & 0 \\
0 & 0 & \alpha_3 \\
\end{pmatrix} \begin{pmatrix}
1 & 0 & 0\\
0 & \cos(\theta) & \sin(\theta)\\
0 & -\sin(\theta) & \cos(\theta)\\
\end{pmatrix} \\
& = \begin{pmatrix}
\alpha_1 & 0 & 0\\
0 & \alpha_2\cos(\theta) & -\alpha_3\sin(\theta)\\
0 & \alpha_2\sin(\theta) & \alpha_3\cos(\theta)\\
\end{pmatrix} \begin{pmatrix}
1 & 0 & 0\\
0 & \cos(\theta) & \sin(\theta)\\
0 & -\sin(\theta) & \cos(\theta)\\
\end{pmatrix} \\
& = \begin{pmatrix}
\alpha_1 & 0 & 0\\
0 & \alpha_2\cos^2(\theta) + \alpha_3\sin^2(\theta) & (\alpha_2-\alpha_3)\cos(\theta)\sin(\theta)\\
0 & (\alpha_2-\alpha_3)\cos(\theta)\sin(\theta) & \alpha_2\sin^2(\theta) + \alpha_3\cos^2(\theta)\\
\end{pmatrix} \\\end{split}\]

which namely yields, as this is true for each \(\theta\):

\[\begin{split}\beta_1 & = \alpha_1\\
\alpha_2 & = \alpha_3\end{split}\]

Similar work on \(\boldsymbol{R}_y(\theta)\) gives:

\[\begin{split}\beta_2 & = \alpha_2\\
\alpha_1 & = \alpha_3\end{split}\]

and on \(\boldsymbol{R}_z(\theta)\) gives:

\[\begin{split}\beta_3 & = \alpha_3\\
\alpha_1 & = \alpha_2\end{split}\]

Expanding this work on the angles, one actually deduces that:

\[\begin{split}\boldsymbol{m_{ii, global}} = \boldsymbol{m_{ii, local}} = \begin{pmatrix}
\alpha \boldsymbol{I}_3 & 0 \\
0 & \gamma \boldsymbol{I}_3 \\
\end{pmatrix}\end{split}\]

which is a matrix that is invariant through any transformation defined as
\(\begin{pmatrix}\boldsymbol{P}&0\\0&\boldsymbol{P}\end{pmatrix}\), given that
\(\boldsymbol{P}^{-1} = \boldsymbol{P}^{\transpose{}}\).

Note

The fact that such a lumped mass matrix is invariant thourgh any transformation
as defined above is but a by-product of the choice of a general expression,
and does not take any root in a fondamental work hypothesis.

Finally, the **integrand mass matrix** can be written as such (independently
on the coordinate system):

(323)\[\begin{split}\boldsymbol{m}_e = \begin{pmatrix}
\alpha_1\boldsymbol{I}_3 & 0 & 0 & 0\\
0 & \gamma_1\boldsymbol{I}_3 & 0 & 0\\
0 & 0 & \alpha_2\boldsymbol{I}_3 & 0\\
0 & 0 & 0 & \gamma_2\boldsymbol{I}_3\\
\end{pmatrix}\end{split}\]

Timoshenko

Note

Theory relative to Timoshenko beams has not been written yet, as
such calculations are still impossible in MANTA. Theory will
be completed once the associated formulations will be developed.

### General principles of mass matrix lumping

Euler-Bernoulli

The usual approach for lumping is to sum over either the columns or lines of
the mass matrix. Given the general expression of a lumped integrand mass matrix,
and given the fact that the integrand mass matrix is symmetrical
[(320)](#equation-theory-beam-mass-matrix-euler),
one can sum over either one as both approaches give the exact
same result.

Moreover, only terms that are homogenous to the initial diagonal term are added.
In particular, for both bending directions, the mixed terms that contain
shape functions relative to both a translation and an angle are not and cannot
be added.

Finally, \(\alpha_1\) and \(\alpha_2\) (as defined in
[(323)](#equation-theory-beam-lumped-mass-integrand)) should be choosed such as they represent
analogous values, meaning that lumping should be done in a similar way for both
nodes. Same holds for \(\gamma_1\) and \(\gamma_2\).

Timoshenko

Note

Theory relative to Timoshenko beams has not been written yet, as
such calculations are still impossible in MANTA. Theory will
be completed once the associated formulations will be developed.

### Choosing a coefficient for traction and transverse displacement motions

Euler-Bernoulli

Let us first look at \(\alpha_1\) and \(\alpha_2\). Summing
[(320)](#equation-theory-beam-mass-matrix-euler) over its lines, two
possible values for each parameter arise (the shape functions for both
transverse displacements being identical):

- Diagonal term for **traction**:
  \(\rho S \varphi_u^i (\varphi_u^1 + \varphi_u^2) = \rho S \varphi_u^i\) ;
- Diagonal term for **first transverse displacement**:
  \(\rho S \varphi_v^i (\varphi_v^1 + \varphi_v^2) = \rho S \varphi_v^i\).

In the general case, there is no reason for any of those term to be equal to
another, nor for one of them to prevail on the other. However, the appropriate
value to be looking at would actually be the value of the integral over the
element of each of those expression, which can be computed by choosing an
approriate gaussian quadrature.

In the case where \(\rho S\) is constant, one actually has:

\[\begin{split}\int_0^L \rho S \varphi_u^i(x) dx & = \rho S \int_0^L \varphi_u^i(x) dx \\
& = \frac{\rho S L}{2}\\
& = \rho S \int_0^L \varphi_v^i(x) dx \\
& = \int_0^L \rho S \varphi_v^i(x) dx\end{split}\]

which **negates the need for a choice**.

However, in the case where \(\rho S\) is not constant, for instance when
\(S\) contains a linear term:

\[\begin{split}\int_0^L \rho S \varphi_u^1(x) dx & = \rho \int_0^L (S_0 + \Delta S \frac{x}{L}) \varphi_u^1(x) dx \\
& = \frac{\rho S_0 L}{2} + \rho \Delta S \int_0^L \frac{x}{L}(1-\frac{x}{L}) dx \\
& = \frac{\rho S_0 L}{2} + \frac{\rho \Delta S L}{6}\end{split}\]

\[\begin{split}\int_0^L \rho S \varphi_v^1(x) dx & = \rho \int_0^L (S_0 + \Delta S \frac{x}{L}) \varphi_v^1(x) dx \\
& = \frac{\rho S_0 L}{2} + \rho \Delta S \int_0^L \frac{x}{L}(2\frac{x}{L}^3 - 3\frac{x}{L}^2 +1) dx \\
& = \frac{\rho S_0 L}{2} + \frac{3 \rho \Delta S L}{20}\end{split}\]

rendering **necessary** the choice between one of the two quantities.

In MANTA, the choice is given to the user to choose either expression, in the
case where any material or geometric properties would vary.

Note

In the case where all those properties are constant, we showed that the
integration over the element would yields \(\frac{\rho S L}{2}\), which
corresponds to half the total weight of the beam, thus confirming the
fact that lumping the mass matrix actually behaves as if the mass were
concentrated at each node.

Timoshenko

Note

Theory relative to Timoshenko beams has not been written yet, as
such calculations are still impossible in MANTA. Theory will
be completed once the associated formulations will be developed.

### Choosing a coefficient for torsion and bending motions

Euler-Bernoulli

Doing the same work for \(\gamma_1\) and \(\gamma_2\), one deduces two
possible values for those parameters (the shape functions for both bendings
being identical):

- Diagonal term for **torsion**:
  \(\rho J \varphi_{\theta_x}^i (\varphi_{\theta_x}^1 + \varphi_{\theta_x}^2) = \rho J \varphi_{\theta_x}^i\) ;
- Diagonal term for **bending**:
  \(\rho S \varphi_{\theta_y}^i (\varphi_{\theta_y}^1 + \varphi_{\theta_y}^2)\).

which are two different terms that have no reason to be equal even after being
integrated over the length of the element, which suggests that the integrand
mass matrix in the local frame is not naturally in the form exhibited in
[(323)](#equation-theory-beam-lumped-mass-integrand).

This implies that \(\gamma_1\) and \(\gamma_2\) shall represent two
different kind of terms, which in turn means that at least one of the motions
**will be ill-represented**.

Note

In MANTA, the user is given a fine control over the choice of the coefficient,
as it can be seen in the following section.

Timoshenko

Note

Theory relative to Timoshenko beams has not been written yet, as
such calculations are still impossible in MANTA. Theory will
be completed once the associated formulations will be developed.

#### Different approaches for the choice of coefficients

Euler-Bernoulli

In literature, several coefficients are proprosed, usually integrated over the
length of the element and assuming all properties are constant through it:

- \(\rho S L \cdot \frac{L^2}{105}\) proposed by Ruszniewski in [[Rus81](../../../references/references.md#id61)];
- \(\rho S L \cdot \frac{L^2}{24}\) proposed by Key and Beisinger in [[KB71](../../../references/references.md#id64)] ;
- \(\rho S L \cdot (\frac{L^2}{105} + \frac{I_y + I_z}{2 S})\) proposed by Lepareux in [[LG01](../../../references/references.md#id62)];
- \(\rho S L \cdot (\frac{L^2}{24} + \frac{1}{2}\frac{\max(I_y, I_z)}{S})\) proposed by Belytschko and Mindle in [[BM80](../../../references/references.md#id63)];

Each of those coefficient could be derived from several expression that arise
in the integrand mass matrix, assuming all material and geometric properties are
constant.

Without any loss of generality, in the following subsections, \(\varphi_\theta\)
designates the shape function relative to \(\theta_y\) or \(\theta_z\)
at any of the nodes.

Timoshenko

Note

Theory relative to Timoshenko beams has not been written yet, as
such calculations are still impossible in MANTA. Theory will
be completed once the associated formulations will be developed.

##### Ruszniewski's coefficient

Euler-Bernoulli

One simply has:

\[\int_0^L \rho S \varphi_\theta^2 = \rho S \int_0^L \varphi_\theta^2 = \rho S L \frac{L^2}{105}\]

which actually corresponds to the diagonal term of the integrand mass matrix
[(320)](#equation-theory-beam-mass-matrix-euler).

Timoshenko

Note

Theory relative to Timoshenko beams has not been written yet, as
such calculations are still impossible in MANTA. Theory will
be completed once the associated formulations will be developed.

##### Key and Beisinger's coefficient

Euler-Bernoulli

In [[KB71](../../../references/references.md#id64)], Key and Beisinger derive their coefficient
from the following expression, mutliplied by a multiplicative coefficient
\(\alpha\), complemented by Belytschko and Mindle in [[BM80](../../../references/references.md#id63)]
that fix the optimal value of \(\alpha\) (regarding the representativeness
of the frequency spectrum) at \(\alpha = \frac{420}{24} = 17.5\):

\[\begin{split}\int_0^L \alpha \rho S \varphi_\theta (\varphi_\theta^1 + \varphi_\theta^2) & = \alpha \rho S \int_0^L \varphi_\theta (\varphi_\theta^1 + \varphi_\theta^2) \\
& = \rho S L \frac{\alpha L^2}{420}\\
& = \rho S L \frac{L^2}{24}\end{split}\]

which corresponds (ignoring \(\alpha\)) at the sum of the homogenous terms
of the integrand mass matrix [(320)](#equation-theory-beam-mass-matrix-euler) over the line.

Note

\(\rho S L \frac{L^2}{24}\) conviently corresponds to the case where half
the inertia of the element around its center of gravity would have been
concentrated at each node, as total inertia of the element is
\(S L \frac{L^2}{12}\).

Timoshenko

Note

Theory relative to Timoshenko beams has not been written yet, as
such calculations are still impossible in MANTA. Theory will
be completed once the associated formulations will be developed.

##### Lepareux's coefficient

Euler-Bernoulli

As this coefficient involves the contribution of both second moments of area,
mainly their arithmetic mean \(\frac{I_y + I_z}{2}\), it cannot be easily
deduced from the integrand mass matrix [(320)](#equation-theory-beam-mass-matrix-euler).

To actually associate that term to an integrand mass matrix, one cannot neglect
the inertial effects due to rotation, even if that hypothesis constitutes one
of [Euler-Bernoulli's hypotheses](#theory-beam-hypotheses). To do so, one has
to deduce the integrand mass matrix from the unsimplified virtual work of inertial
forces [(316)](#equation-theory-beam-virtual-inertial), i.e.:

\[\hat{\delta W_a} = \int_x [\rho S \partial_t^2 u \hat{u} + \rho S \partial_t^2 v \hat{v} + \rho S \partial_t^2 w \hat{w} + \rho J \partial_t^2 \theta_x \hat{\theta_x} + \rho I_y \partial_t^2 \theta_y \hat{\theta_y} + \rho I_z \partial_t^2 \theta_z \hat{\theta_z}] dx\]

Note

That virtual work of inertial forces written this way actually corresponds
to Rayleigh beam theory (see [[Ray77](../../../references/references.md#id65)] and
[[SdCAdSH16](../../../references/references.md#id66)]).

Lepareux's coefficient corresponds to the isolation of the diagonal term of the
integrand mass matrix obtained this way, with a slight correction of the rotatory
inertial term:

\[\begin{split}\int_0^L \rho S (\varphi_\theta^i)^2 + \frac{15}{2}\rho \frac{I_y + I_z}{2} (\partial_x \varphi_{\theta}^i)^2 & = \rho S \left( \int_0^L (\varphi_\theta^i)^2 \right) + \frac{15}{2} \rho \frac{I_y + I_z}{2} \left( \int_0^L (\partial_x \varphi_{\theta}^i)^2 \right) \\
& = \rho S L \frac{L^2}{105} + \frac{15}{2} \rho \frac{I_y + I_z}{2} \left( \int_0^L (\partial_x \varphi_{\theta}^i)^2 \right) \\
& = \rho S L \frac{L^2}{105} + \rho L \frac{I_y + I_z}{2} \\
& = \rho S L (\frac{L^2}{105} + \frac{I_y + I_z}{2 S}) \\\end{split}\]

Note

Note that under Rayleigh beam theory, the transverse translation term
is slightly modified under the consideration of the rotatory inertias. As
such, the diagonal integrand term relative to transverse translation, once
lumped, becomes:

\[\rho S \varphi_v^i(\varphi_v^1 + \varphi_v^2) \longrightarrow \rho S \varphi_v^i(\varphi_v^1 + \varphi_v^2) + \rho I_z \partial_x \varphi_v^i(\partial_x \varphi_v^1 + \partial_x \varphi_v^2)\]

However, as \(\partial_x \varphi_v^1 = -\partial_x \varphi_v^2\), one
could easily see why the lumped transverse translation term remains unchanged,
thus not affecting any of the previous choices that were made regarding
this term.

Timoshenko

Note

Theory relative to Timoshenko beams has not been written yet, as
such calculations are still impossible in MANTA. Theory will
be completed once the associated formulations will be developed.

##### Belytschko and Mindle's coefficient

Euler-Bernoulli

Belytschko and Mindle's coefficient also arise from the integrand matrix
obtained from Rayleigh's beam theory, and corresponds to the summation over the
line of the integrand mass matrix angle terms:

\[\begin{split}\int_0^L \rho I_y \partial_x \varphi_{\theta_y}^i (\partial_x \varphi_{\theta_y}^1 + \partial_x \varphi_{\theta_y}^2) & = \rho S L \cdot \frac{1}{10}\frac{I_y}{S} \\
\int_0^L \rho I_z \partial_x \varphi_{\theta_z}^i (\partial_x \varphi_{\theta_z}^1 + \partial_x \varphi_{\theta_z}^2) & = \rho S L \cdot \frac{1}{10}\frac{I_z}{S} \\\end{split}\]

which yields:

\[\begin{split}\int_0^L \rho \max(I_y, I_z) \partial_x \varphi_{\theta}^i (\partial_x \varphi_{\theta}^1 + \partial_x \varphi_{\theta}^2) & = \rho S L \cdot \frac{1}{10}\frac{\max(I_y, I_z)}{S} \\\end{split}\]

Belytschko and Mindle's coefficient can then be easily deduced from these new
expressions and from previously written terms, namely from Key and Beisinger's
coefficient.

Timoshenko

Note

Theory relative to Timoshenko beams has not been written yet, as
such calculations are still impossible in MANTA. Theory will
be completed once the associated formulations will be developed.

#### Implementation of the choice of the coefficient in MANTA

Euler-Bernoulli

In MANTA, the user is given a fine control over the choice of the terms that
appear in the integrand mass matrix for the torsion/bending directions, which is
expressed as a linear combination of minimal terms that allow the emulation of
the terms found in literature and listed [above](#theory-beam-literature-coefficients).
Two additional terms are implemented to allow the precise discrimination between
each second moment of area:

\[\begin{split}\tilde{\gamma}_1 & = \rho S \varphi_\theta^2 \\
\tilde{\gamma}_2 & = \rho S \varphi_\theta (\varphi_\theta^1 + \varphi_\theta^2) \\
\tilde{\gamma}_3 & = \rho I_y (\partial_x \varphi_\theta)^2 \\
\tilde{\gamma}_4 & = \rho I_y \partial_x \varphi_\theta (\partial_x\varphi_\theta^1 + \partial_x\varphi_\theta^2) \\
\tilde{\gamma}_5 & = \rho I_z (\partial_x \varphi_\theta)^2 \\
\tilde{\gamma}_6 & = \rho I_z \partial_x \varphi_\theta (\partial_x\varphi_\theta^1 + \partial_x\varphi_\theta^2) \\
\tilde{\gamma}_7 & = \rho \max(I_y, I_z) \partial_x\varphi_\theta (\partial_x\varphi_\theta^1 + \partial_x\varphi_\theta^2)\end{split}\]

For the terms found in literature, the following coefficient are to
be applied to emulate them in any given calculation:

|  | \(\tilde{\gamma}_1\) | \(\tilde{\gamma}_2\) | \(\tilde{\gamma}_3\) | \(\tilde{\gamma}_4\) | \(\tilde{\gamma}_5\) | \(\tilde{\gamma}_6\) | \(\tilde{\gamma}_7\) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Ruszniewski [[Rus81](../../../references/references.md#id61)] | \(1\) |  |  |  |  |  |  |
| Key and Beisinger [[KB71](../../../references/references.md#id64)] |  | \(\frac{420}{24}\) |  |  |  |  |  |
| Lepareux in 2D [[LG01](../../../references/references.md#id62)] | \(1\) |  |  |  | \(\frac{15}{2}\) |  |  |
| Lepareux in 3D [[LG01](../../../references/references.md#id62)] | \(1\) |  | \(\frac{15}{4}\) |  | \(\frac{15}{4}\) |  |  |
| Belytschko and Mindle [[BM80](../../../references/references.md#id63)] |  | \(\frac{420}{24}\) |  |  |  |  | \(5\) |

Note

In 2D, the Lepareux's coefficient cannot be represented as the geometrical
mean of \(I_y\) and \(I_z\) as \(I_y\) is not defined. Thus,
the coefficient is simply equal
to \(\tilde{\gamma}_1 + \frac{15}{2}\tilde{\gamma}_4 = \rho S \varphi_
\theta^2 + \frac{15}{2}\rho I_z (\partial_x \varphi_\theta)^2\).

Timoshenko

Note

Theory relative to Timoshenko beams has not been written yet, as
such calculations are still impossible in MANTA. Theory will
be completed once the associated formulations will be developed.

## Determination of the external distributed forces vector

The **elementary external distributed forces vector**
\(\boldsymbol{F}_{ext, d}\) of the element is defined through the distributed
forces part of the virtual work of **external forces** for any given
virtual displacement (given [here](#theory-beam-virtual-work-external-forces)):

\[\delta \hat{W}_{ext, d} = \int_x (f_x \hat{u} + f_y \hat{v} + f_z \hat{w}
+ m_x \hat{\theta_x} + m_y \hat{\theta_y}
+ m_z \hat{\theta_z}) dx
= \hat{\boldsymbol{u_e}}^{t} \boldsymbol{F}_{ext, d}\]

Defining the **integrand external distributed forces vector**:

\[\boldsymbol{f}_{ext, d} = \left( f_x , f_y , f_z , m_x , m_y , m_z\right)^{t}\]

Rewriting the hereabove equation, one has:

\[\begin{split}\delta \hat{W}_{ext, d} & = \int_x \hat{\boldsymbol{u}}^{t}(x) \cdot \boldsymbol{f}_{ext, d} dx \\
& = \int_x \hat{\boldsymbol{u_e}}^{t} \boldsymbol{N}^{t}(x) \boldsymbol{f}_{ext, d} dx \\
& = \hat{\boldsymbol{u_e}}^{t} \int_x \boldsymbol{N}^{t}(x) \boldsymbol{f}_{ext, d} dx\end{split}\]

Which in turn directly gives the expression of **elementary external distributed
forces vector**:

\[\boldsymbol{F}_{ext, d} = \int_x \boldsymbol{N}^{t}(x) \boldsymbol{f}_{ext, d} dx\]

## Critical time step for explicit time integration

Euler-Bernoulli

For explicit time integration, a critical time step must be determined for each
element to determine the maximal value of the time step in order to ensure the
scheme's stability.

For a central difference time integration, [[KB71](../../../references/references.md#id64)]
gives the expression of the **critical time step**:

\[\Delta t = \frac{2}{\omega_{max}}\]

where \(\omega_{max}\) is the maximal angular eigenfrequency of the
**elementary matrices**, i.e. the maximal solution of
\(\det{\boldsymbol{K}_e - \omega^2 \boldsymbol{M}_e} = 0\) (using the
lumped mass matrix).

To determine the critical time step in this section, we will assume constant
geometrical and material properties through the beam element. Without any loss
of generality, each motion can be treated separately from one another.

Timoshenko

Note

Theory relative to Timoshenko beams has not been written yet, as
such calculations are still impossible in MANTA. Theory will
be completed once the associated formulations will be developed.

### Traction-compression motion

Euler-Bernoulli

Equation [(309)](#equation-theory-beam-exact-stiffness-traction) gives the
**elementary stiffness matrix**, and the **lumped elementary mass matrix** is
given [here](#theory-beam-translation-lumping).

Solving for the maximal angular eigenfrequency means finding the maximal solution
of the following equation:

\[\begin{split}0 & = \det{\boldsymbol{K}_e^{traction} - \omega^2 \boldsymbol{M}_e^{traction}} \\
& = \left| \begin{matrix}
\frac{ES}{L} - \omega^2 \frac{\rho S L}{2} & -\frac{ES}{L} \\
-\frac{ES}{L} & \frac{ES}{L} - \omega^2 \frac{\rho S L}{2}
\end{matrix} \right|\end{split}\]

One trivially shows that the two eigenvalues of that matrix are such as the
two columns of the matrix are either equal or have opposite sign, i.e.:

\[\begin{split}\begin{cases}
\frac{ES}{L} - \omega^2 \frac{\rho S L}{2} & = \frac{ES}{L} \\
\frac{ES}{L} - \omega^2 \frac{\rho S L}{2} & = -\frac{ES}{L}
\end{cases}\end{split}\]

which translates as:

\[\begin{split}\begin{cases}
\omega = 0 \\
\omega = \frac{2}{L}\sqrt{\frac{E}{\rho}}
\end{cases}\end{split}\]

Thus,

\[\omega_{max}^{traction} = \frac{2}{L}\sqrt{\frac{E}{\rho}}\]

which gives:

\[\boxed{\Delta t_c^{traction} = \frac{2}{\omega_{max}^{traction}} = L \sqrt{\frac{\rho}{E}}}\]

Timoshenko

Note

Theory relative to Timoshenko beams has not been written yet, as
such calculations are still impossible in MANTA. Theory will
be completed once the associated formulations will be developed.

### Torsion motion

Euler-Bernoulli

Using the same method as before, one shows that:

\[\omega_{max}^{torsion} = \frac{2}{L}\sqrt{\frac{G}{\rho}} \sqrt{\frac{J_x}{J}}\]

By definition, \(G\) and \(J_x\) are respectively lower than
\(E\) and \(J\) respectively. Thus, one deduces that:

\[\boxed{\Delta t_c^{torsion} > \Delta t_c^{traction}}\]

Timoshenko

Note

Theory relative to Timoshenko beams has not been written yet, as
such calculations are still impossible in MANTA. Theory will
be completed once the associated formulations will be developed.

### Bending motion

Euler-Bernoulli

The expression of the elementary lumped mass matrix may differ depending on the
chosen strategy for lumping, as seen in [this section](#theory-beam-bending-lumping).

Let us denote \(\tilde{\gamma}\) the chosen coefficient such as the **elementary
lumped mass matrix** becomes (for one direction of bending only):

\[\begin{split}\boldsymbol{M}_e^{bending} = \rho S L \begin{pmatrix}
\frac{1}{2} & 0 & 0 & 0 \\
0 & \frac{1}{2} & 0 & 0 \\
0 & 0 & \tilde{\gamma} & 0 \\
0 & 0 & 0 & \tilde{\gamma} \\
\end{pmatrix}\end{split}\]

Combining that expression with the expression of the elementary stiffness
matrix [(313)](#equation-theory-beam-exact-stiffness-bendingy), solving the eigenvalue
problems yields the following expression for the maximal angular
eigenfrequency:

\[\omega_{max}^{bending} = \sqrt{6 \frac{E}{\rho L^2}\frac{I}{S L^2}\frac{L^2 + 8\tilde{\gamma}}{\tilde{\gamma}}}\]

where \(I = \max(I_y, I_z)\).

This means that the chosen coefficient for lumping has a significant
impact on the determination of the critical time step, as:

\[\boxed{\Delta t_c^{bending} = L^2 \sqrt{\frac{\rho S}{E I}} \sqrt{\frac{4\tilde{\gamma}}{6(L^2 + 8\tilde{\gamma})}}}\]

Timoshenko

Note

Theory relative to Timoshenko beams has not been written yet, as
such calculations are still impossible in MANTA. Theory will
be completed once the associated formulations will be developed.

### Calulcation of the critical time step

Euler-Bernoulli

Finally, one can compute the critical time step for Euler beams be taking
the minimal value of the critical time steps determined for each motion:

\[\boxed{\Delta t_c = L \sqrt{\frac{\rho}{E}} \cdot \min\left(1; L \sqrt{\frac{S}{I}} \sqrt{\frac{4\tilde{\gamma}}{6(L^2 + 8\tilde{\gamma})}}\right)}\]

where the usual values of \(\tilde{\gamma}\) can be found in
[this section](#theory-beam-literature-coefficients), ie:

- Ruszniewski [[Rus81](../../../references/references.md#id61)]: \(\frac{L^2}{105}\);
- Key and Beisinger [[KB71](../../../references/references.md#id64)]: \(\frac{L^2}{24}\) ;
- Lepareux [[LG01](../../../references/references.md#id62)]: \(\frac{L^2}{105} + \frac{I_y + I_z}{2 S}\);
- Belytschko and Mindle [[BM80](../../../references/references.md#id63)]: \(\frac{L^2}{24} + \frac{1}{2}\frac{\max(I_y, I_z)}{S}\);

Timoshenko

Note

Theory relative to Timoshenko beams has not been written yet, as
such calculations are still impossible in MANTA. Theory will
be completed once the associated formulations will be developed.

## Other possible interpolations and formulations

Euler-Bernoulli

(*Intentionally left blank*)

Timoshenko

----- **Interpolation with uncoupled transverse deflection and angle** -----

Another possible classical interpolation is possible, which typically does not
depend on the material and geometrical properties to define the
shape functions [(303)](#equation-theory-beam-shape-func-timoshenko). Such interpolation
cannot possibly respect all static conditions [(301)](#equation-theory-beam-static-conditions-timoshenko),
as those involve those properties.

One possible other interpolation involve interpolating each continuous
displacement by its respective degrees of freedom only, contrary to what is done
[(302)](#equation-theory-beam-interpolation-timoshenko), which can be written as such:

\[ \begin{align}\begin{aligned}u(x) & = u_1 \varphi^1_{u}(x) + u_2 \varphi^2_{u}(x)\\v(x) & = v_1 \varphi^1_{v}(x) + v_2 \varphi^2_{v}(x)\\w(x) & = w_1 \varphi^1_{w}(x) + w_2 \varphi^2_{w}(x)\\\theta_x(x) & = \theta_{x,1} \varphi^1_{\theta_x}(x) + \theta_{x,2} \varphi^2_{\theta_x}(x)\\\theta_y(x) & = \theta_{y,1} \varphi^1_{\theta_y}(x) + \theta_{y,2} \varphi^2_{\theta_y}(x)\\\theta_z(x) & = \theta_{z,1} \varphi^1_{\theta_z}(x) + \theta_{z,2} \varphi^2_{\theta_z}(x)\end{aligned}\end{align} \]

or alternatively,

\[\begin{split}\boldsymbol{U}(x) = \begin{pmatrix}
\varphi^1_u & 0 & 0 & 0 & 0 & 0 & \varphi^2_u & 0 & 0 & 0 & 0 & 0 \\
0 & \varphi^1_v & 0 & 0 & 0 & 0 & 0 & \varphi^2_v & 0 & 0 & 0 & 0 \\
0 & 0 & \varphi^1_w & 0 & 0 & 0 & 0 & 0 & \varphi^2_w & 0 & 0 & 0 \\
0 & 0 & 0 & \varphi^1_{\theta_x} & 0 & 0 & 0 & 0 & 0 & \varphi^2_{\theta_x} & 0 & 0 \\
0 & 0 & 0 & 0 & \varphi^1_{\theta_y} & 0 & 0 & 0 & 0 & 0 & \varphi^2_{\theta_y} & 0 \\
0 & 0 & 0 & 0 & 0 & \varphi^1_{\theta_z} & 0 & 0 & 0 & 0 & 0 & \varphi^2_{\theta_z}
\end{pmatrix}(x) \boldsymbol{u}_{e}\end{split}\]

**Choosing the shape functions**

As the chosen interpolation cannot possibly comply with the static conditions,
they can virtually be chosen arbitrarily, namely can be chosen to be as simple
as possible, for instance linear, such as:

\[\begin{split}\varphi_{DOF}^1(x) & = 1-\frac{x}{L} \\
\varphi_{DOF}^2(x) & = \frac{x}{L} \\\end{split}\]

**Integrand stiffness matrix**

Re-writing the integrand stiffness matrix as seen in [(308)](#equation-theory-beam-stiffness-decomposition),
one has:

\[\begin{split}\boldsymbol{k}_{ij} = \begin{pmatrix}
E S \partial_x \varphi^i_u \partial_x \varphi^j_u & 0 & 0 & 0 & 0 & 0\\
0 & G S \kappa_y \partial_x \varphi^i_v \partial_x \varphi^j_v & 0 & 0 & 0 & - G S \kappa_y \partial_x \varphi^i_v \varphi^j_{\theta_z} \\
0 & 0 & G S \kappa_z \partial_x \varphi^i_w \partial_x \varphi^j_w & 0 & G S \kappa_z \partial_x \varphi^i_w \varphi^j_{\theta_y} & 0 \\
0 & 0 & 0 & G J_x \partial_x \varphi^i_{\theta_x} \partial_x \varphi^j_{\theta_x} & 0 & 0 \\
0 & 0 & G S \kappa_z \partial_x \varphi^j_w \varphi^i_{\theta_y} & 0 & E I_y \partial_x \varphi^i_{\theta_y} \partial_x \varphi^j_{\theta_y} & 0 \\
& & & & + G S \kappa_z \varphi^i_{\theta_y} \varphi^j_{\theta_y} & \\
0 & - G S \kappa_y \partial_x \varphi^j_v \varphi^i_{\theta_z} & 0 & 0 & 0 & E I_z \partial_x \varphi^i_{\theta_z} \partial_x \varphi^j_{\theta_z}\\
& & & & & + G S \kappa_y \varphi^i_{\theta_z} \varphi^j_{\theta_z} \\
\end{pmatrix}\end{split}\]

which can be interpreted as a simplification of regular integrand stiffness matrix
seen in [(308)](#equation-theory-beam-stiffness-decomposition).

**Integration using mixed shaped functions / gaussian quadrature**

It is shown in [[HTK77](../../../references/references.md#id54)] that using the *classical*
integration results in numerical locking and
an overstiff solution especially when the thickness of the beam in one
direction becomes very small.

[[HTK77](../../../references/references.md#id54)]

*For very thick plates two-by-two Gaussian quadrature leads to acceptable
results, however, for thin plates it causes 'locking' [...]. In this case we
use two-by-two Gaussian quadrature on the bending energy term and one-point
Gaussian quadrature on the shear energy term.*

As such, the integration of the integrand matrix can be written with mixed
shape functions to avoid numerical locking, for instance by choosing constant
shape functions for the terms that correspond to the shear energy term. This can
indeed be interpreted as an under integration of some subterms of the
integrand matrix (hence equivalent to a *mixed gaussian quadrature*).

This translates in the choice of a different order for shape functions in
integrand stiffness matrix, with the appropriate order in the general case and a
constant shape function for all terms in \(\boldsymbol{k}_{ij}^{bending_{y}}\) y
and \(\boldsymbol{k}_{ij}^{bending_{z}}\) that exhibits an un-differentiated
shape function.

This yields the following (which also holds for
\(\boldsymbol{k}_{ij}^{bending_{z}}\)):

\[ \begin{align}\begin{aligned}\begin{split}\boldsymbol{k}_{ij}^{bending_{y}} & = \begin{pmatrix}
0 & 0 & 0 & 0 & 0 & 0 \\
0 & G S \kappa_y \partial_x \varphi^i_v \partial_x \varphi^j_v & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & E I_z \partial_x \varphi^i_{\theta_z} \partial_x \varphi^j_{\theta_z} \\
\end{pmatrix}\end{split}\\\begin{split}& + \begin{pmatrix}
0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & - G S \kappa_y \partial_x \varphi^i_v \varphi^j_{\theta_z} \\
0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 \\
0 & - G S \kappa_y \partial_x \varphi^i_v \varphi^j_{\theta_z} & 0 & 0 & 0 & G S \kappa_y \varphi^i_{\theta_z} \varphi^j_{\theta_z} \\
\end{pmatrix}\end{split}\end{aligned}\end{align} \]

where the first matrix uses the shape functions defined hereabove, and where
the second matrix uses a constant function for \(\varphi^j_{\theta_z}\).

Note

This mixed integration corresponds to
[what is done in Cast3m](https://www-cast3m.cea.fr/html/doc_theo/mecanique_revue_modeles_beton/rappels_poutres.html).

The corresponding matrix \(\boldsymbol{B}(x) = \boldsymbol{D}\boldsymbol{N}(x)\),
as defined in [(304)](#equation-theory-beam-integrand-stiffness-definition) is the following:

\[\boldsymbol{B}(x) = \left( \boldsymbol{B}_1(x) | \boldsymbol{B}_2(x) \right)\]

\[\begin{split}\boldsymbol{B}_i(x) = \begin{pmatrix}
\partial_x\varphi^i_u & 0 & 0 & 0 & 0 & 0\\
0 & \partial_x\varphi^i_v & 0 & 0 & 0 & - \varphi^i_{\theta_z}\\
0 & 0 & \partial_x\varphi^i_w & 0 & \varphi^i_{\theta_y} & 0 \\
0 & 0 & 0 & \partial_x\varphi^i_{\theta_x} & 0 & 0 \\
0 & 0 & 0 & 0 & \partial_x\varphi^i_{\theta_y} & 0 \\
0 & 0 & 0 & 0 & 0 & \partial_x\varphi^i_{\theta_z}
\end{pmatrix}(x)\end{split}\]
