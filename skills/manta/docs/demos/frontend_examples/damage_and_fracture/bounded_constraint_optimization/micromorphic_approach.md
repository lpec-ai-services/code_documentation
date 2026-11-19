<!-- source: https://manta-project.gitlab.io/manta/demos/frontend_examples/damage_and_fracture/bounded_constraint_optimization/micromorphic_approach.html -->

# A micromorphic approximation for bounded constraint optimization problems associated with gradient damage models

Note

The following files are needed to run this tutorial:

- [`bar2D.py`](https://manta-project.gitlab.io/manta/_downloads/c0c4d262849cab71b5c231cdf9462738/bar2D.py).
- [`MicromorphicDamage.mfront`](https://manta-project.gitlab.io/manta/_downloads/40ba88896b83c1618e660d8c1625d90f/MicromorphicDamage.mfront).

This tutorial closely follows the demo of J. Bleyer
[[Ble25](../../../../references/references.md#id21)] (which is part of the tutorials
[[Ble24a](../../../../references/references.md#id20)]). The reference solutions are taken
from the papers of Pham et al.
[[PAMM11](../../../../references/references.md#id19)]
[[PM13](../../../../references/references.md#id18)].

We search the minimizer \(d\left(x\right)\) of the following
functional:

\[\int_{\Omega}\left(d^{\star}+l_{0}^{2}\,\vec{\nabla}d^{\star}\,\cdot\,\vec{\nabla}d^{\star}\,\mathrm{d}\,V\right)\]

on a domain \(\Omega\) under the constraint
\(0 \leq d\left(x\right) \leq 1\) and some boundary conditions.

The constraint can be expressed using a characteristic function
\(\psi\left(x\right)\) such that:

\[\begin{split}\psi\left(d\right)=
\left\{
\begin{aligned}
\infty &\quad\text{if}\quad& d<0\\
0 &\quad\text{if}\quad& 0\leq d \leq 1\\
\infty &\quad\text{if}\quad& d>1\\
\end{aligned}
\right.\end{split}\]

Due to the constraints, such problem is not easily translated in terms
of weak forms. One solution is to use unilateral constraints with
assiociated Lagrange multipliers. Another solution, described in this
paper, relies on a micromorphic regularization.

The micromorphic approach introduces a relaxed unconstrained field
\(d_{\chi}\) such that the initial problem is replaced by:

\[\begin{split}\begin{aligned}
\left(d, d_{\chi}\right) &= \underset{\left(d^{\star}, d_{\chi}^{\star}\right)}{\mathrm{argmin}}\quad \int_{\Omega}\left(d^{\star}+l_{0}^{2}\,\vec{\nabla}d_{\chi}^{\star}\,\cdot\,\vec{\nabla}d_{\chi}^{\star}+\beta\,\left(d^{\star}-d_{\chi}^{\star}\right)^{2} + \phi\left(d^{\star}\right)\,\mathrm{d}\,V\right)\\
&= \underset{\left(d^{\star}, d_{\chi}^{\star}\right)}{\mathrm{argmin}}\quad \int_{\Omega}\psi\left(d^{\star}, d_{\chi}^{\star}, \vec{\nabla}\,d_{\chi}^{\star}\right) + \phi\left(d^{\star}\right)\,\mathrm{d}\,V\\
&= \underset{\left(d^{\star}, d_{\chi}^{\star}\right)}{\mathrm{argmin}}\quad \mathcal{L}\left(d^{\star}, d_{\chi}^{\star}\right)
\end{aligned}\end{split}\]

with appropriate boundary conditions. In the previous expression,
\(\beta\) is a penalization parameter.

## Problem considered

### Geometry

We consider a 2D rectangular domain \(\Omega\) of size
\([L, h]\).

### Boundary conditions

\(d_{\chi}\left(0, y\right) = d_{0}\)

## Expression of the micromorphic behaviour

It is then convenient to separate the Lagrangian \(\mathcal{L}\)
into two parts \(\mathcal{L}_{1}\) and \(\mathcal{L}_{2}\) as
follows:

\[\begin{split}\begin{aligned}
\mathcal{L}_{1}\left(d^{\star},d_{\chi}^{\star}\right) &=
\int_{\Omega}\psi\left(d^{\star}, d_{\chi}^{\star},\vec{\nabla}\,d_{\chi}^{\star}\right)\,\mathrm{d}\,V \\
\mathcal{L}_{2}\left(d^{\star}\right) &=
\int_{\Omega}\phi\left(d^{\star}\right)\,\mathrm{d}\,V
\end{aligned}\end{split}\]

In this report, we will admit the following mathematical results which
characterize the minima of the Lagrangian [[Son21](../../../../references/references.md#id22)]:

- The regular part of Lagrangian \(\mathcal{L}_{1}\) is minimal
  with respect to the displacement field \(\vec{u}\) and the
  micromorphic damage field \(d_{\chi}\).
- At each point, the thermodynamic force \(Y\) associated with the
  damage, is in the subgradient of the dissipation potential:

  \[Y \in \partial \phi\]

  where \(Y\) is defined by:

  \[Y = -{\displaystyle \frac{\displaystyle \partial \psi}{\displaystyle \partial d}}\]

### Balance equations for the micromorphic damage

The variation of \(\delta\,\mathcal{L}_{1}\) with respect to
micromorphic damage field is defined by:

\[\delta\,\mathcal{L}_{1}=
\mathcal{L}_{1}\left(d, d_{\chi} + \delta\,d_{\chi}\right) -
\mathcal{L}_{1}\left(d, d_{\chi}\right)\]

where the variation \(\delta\,d{\chi}\) is null on the part of the
boundary where micromophic damage is prescribed.

By retaining only first order terms, this variation can be computed as
follows:

\[\begin{aligned}
\delta\,\mathcal{L}_{1}&=
\int_{\Omega}
\left[
{\displaystyle \frac{\displaystyle \partial \psi}{\displaystyle \partial d_{\chi}}}\,\delta\,d_{\chi}+
{\displaystyle \frac{\displaystyle \partial \psi}{\displaystyle \partial \vec{\nabla}\,d_{\chi}}}\,\cdot\,\vec{\nabla}\,\delta\,d_{\chi}
\right]
\,\mathrm{d}\,V
&=
\int_{\Omega}
\left[
a_{\chi}\,\delta\,d_{\chi}+
\vec{b}_{\chi}\,\cdot\,\vec{\nabla}\,\delta\,d_{\chi}
\right]
\,\mathrm{d}\,V
\end{aligned}\]

where the following thermodynamic forces were introduced:

\[\begin{split}\begin{aligned}
a_{\chi} &= {\displaystyle \frac{\displaystyle \partial \psi}{\displaystyle \partial d_{\chi}}} &= -\beta\left(d-d_{\chi}\right)\\
\vec{b}_{\chi} &= {\displaystyle \frac{\displaystyle \partial \psi}{\displaystyle \partial \vec{\nabla}d_{\chi}}} &= 2\,l_{0}\vec{\nabla}d_{\chi}\\
\end{aligned}\end{split}\]

Applying the divergence theorem leads to:

\[\delta\,\mathcal{L}_{1}=
\int_{\Omega}
\left[
\left(a_{\chi}-\nabla\,\cdot\,\,\vec{b}_{\chi}\right)\,\delta\,d_{\chi} \right]
\,\mathrm{d}\,V+
\int_{\partial\,\Omega}
\left(\vec{b}_{\chi}\,\cdot\,\vec{n}\right)\,\delta\,\vec{d}_{\chi}
\,\mathrm{d}\,S\]

Classical arguments shows that this variation can characterize a minimum
only if all the integrands are zero, leading to the following balance
equation and boundary conditions:

(162)\[\begin{split}\left\{
\begin{aligned}
\nabla\,\cdot\,\,\vec{b}_{\chi} &= a_{\chi} &\text{ in }& \Omega \\
\vec{b}_{\chi}\,\cdot\,\vec{n}&=\vec{0} &\text{ on }& \partial\,\Omega
\end{aligned}
\right.\end{split}\]

### Evolution of damage

This dissipation potential is equivalent to define the following damage
surface:

(163)\[Y = 1 + \beta\left(d-d_{\chi}\right) = 0\]

In practice, the evolution of damage can be computed by the following
closed form formula:

(164)\[d=\min\left(0, \max\left(1 ,d_{\chi} - \frac{1}{\beta}\right)\right)\]

### Numerical schemes

The solution \(\left(d, d_{\chi}\right)\) of the problem must
satisfy both Equations [(162)](#equation-micromorphicdamage-d-chi) and
[(164)](#equation-micromorphicdamage-damage-evolution). Differents numerical schemes
have been studied in [[FHS+22](../../../../references/references.md#id26)].

The most efficient approach consists in exploiting the fact that
Equation eq:micromorphicdamage:damage_evolution is local and that
Equation [(164)](#equation-micromorphicdamage-damage-evolution) can be condensed as
classically done in solid mechanics. This turns Problem
[(162)](#equation-micromorphicdamage-d-chi) into a nonlinear problem whose
\(d_{\chi}\) is the only unknown.

The resolution of the nonlinear Problem [(162)](#equation-micromorphicdamage-d-chi) is
implemented by the `SolidMaterial` brick of the
`ImplicitMicromorphicDamage` model. This brick relies on an external
`MFront` behaviour which must compute:

1. the evolution of the damage for the current estimation of the
   micromorphic damage increment \(\Delta\,d_{\chi}\) over the time
   step,
2. the values of the thermodynamic forces \(a_{\chi}\) and
   \(\vec{b}_{\chi}\),
3. the values of the consistent tangent operators
   \({\displaystyle \frac{\displaystyle \partial a_{\chi}}{\displaystyle \partial \Delta\,d_{\chi}}}\)
   and
   \({\displaystyle \frac{\displaystyle \partial \vec{b}_{\chi}}{\displaystyle \partial \Delta\,d_{\chi}}}\).

The MFront implementation can be downloaded
[`here`](https://manta-project.gitlab.io/manta/_downloads/40ba88896b83c1618e660d8c1625d90f/MicromorphicDamage.mfront).

## Implementation of the test case in MANTA

The test cases begins by importing the manta module:

```python
import manta
```

Next, we define the parameters of the study:

- the length of the bar,
- the characteristic length \(l_{0}\),
- the penalisation factor \(\beta\);

```python
ps = manta.PhysicalSystem(mesh = {'generator': 'Grid',
                                  'spaceDimension': 2,
                                  'lengths': [l, 0.1 * l],
                                  'numberOfElements': [30, 1],
                                  'domain': 'bar'},
                          geometricHypothesis = 'inPlane')
```

### Definition of the physical system

The next step is to define a physical system. We use the grid
generator to define the mesh, as follows:

```python
ps = manta.PhysicalSystem(mesh = {'generator': 'Grid',
                                  'spaceDimension': 2,
                                  'lengths': [l, 0.1 * l],
                                  'numberOfElements': [30, 1],
                                  'domain': 'bar'},
                          geometricHypothesis = 'inPlane')
```

The geometric hypothesis specifies that we are not considering an
axisymmetrical computation.

### Definition of the micromorphic model

The micromorphic model and the numerical parameters used internally are
defined as follows:

```python
params = {'Newton': {'maximumNumberOfIterations': 20,
                     'convergenceTolerances': {
                         'relativeConvergenceTolerance': 1e-10}}}
damage = manta.Model('ImplicitMicromorphicDamage', ps,
                     nonlinearSolver = params)
```

This model must be completed by adding bricks defining the micromorphic
behaviour and the boundary conditions.

#### Definition of the brick associated with the micromorphic behaviour

```python
damage.add('SolidMaterial',
           material = 'bar',
           library = 'src/libBehaviour.so',
           behavior = 'MicromorphicDamage',
           hypothesis = 'PlaneStrain',
           quadratureOrder = 2)
```

#### Boundary conditions for micromorphic damage

```python
damage.add('DirichletBoundaryCondition',
           boundary = 'left',
           unknown = 'MicromorphicDamage',
           value = 1)
```

### Definition of the material properties

```python
for n, v in properties.items():
    ps.addProperty('Constant', material = 'bar', name = n, value = v)
```

### Projection of the damage at nodes for the post-processings

The `L2ProjectionAuxiliaryTask` auxiliary task is used for the projection
of the damage at nodes:

```python
nodal_damage = manta.Model('L2ProjectionAuxiliaryTask', ps,
                           value = 'Damage',
                           result = 'NodalDamage',
                           domain = 'bar',
                           quadratureOrder = 2)
```

This projection is required by the `LineCurves` post-processing
defined below.

### Coupling scheme

The coupling scheme used in this test case is quite simple: at each
time step, we compute the solution and then we project the damage at
nodes:

```python
cs = manta.CouplingScheme('LoopCouplingScheme', ps,
                          numberOfIterations = 1)
cs.add(damage)
cs.add(nodal_damage)
ps.setCouplingScheme(cs)
```

### Definition of the post-processing

In this test case, we define two post-processings:

- the first one exports the nodal values of the micromorphic damage
  and the nodal values of the projection of the damage internal
  variable at nodes along the line `bottom`,
- the second ones generates an `VTK` file containing the values
  of the micromorphic damage and the damage for each time step.

```python
ps.addPostProcessing('LineCurves',
                     file = 'micromorphic-damage.res',
                     line = 'bottom',
                     precision = 14,
                     nodalValues = ['MicromorphicDamage', 'NodalDamage'])
ps.addPostProcessing('VTKExport',
                     outputFileBaseName = 'bar2D-results',
                     fields = [{'field': 'MicromorphicDamage',
                                'fieldType': 'nodeField',
                                'material': 'bar'},
                               {'field': 'Damage',
                                'fieldType': 'ipField',
```

### Running the simulation

```python

s = manta.Simulation(ps, times = [0, 1],
                     allowSubStepping = False)
```

## Usage

### Compilation of the `MFront` file

```bash
mfront --obuild --interface=generic MicromorphicDamage.mfront
```

### Running the `manta`’s script

```bash
python3 bar2D.py
```

## Results

### Extracting data with `manta-extract_line_curve_values`

The `manta-extract_line_curve_values` allows to extract
the values generated by the `LineCurves` post-processing
(containing the micromorphic damage and damage) in a file
that can be plot using utilities such as `gnuplot`:

```bash
$ manta-extract_line_curve_values micromorphic-damage.res \
  1 -f txt -o micromorphic-damage-1.res
```

### Plotting the results

![figure](https://manta-project.gitlab.io/manta/_images/damage-values.png)

Fig. 32 Comparison of the micromorphic damage, the damage projected at nodes
and the analytical solution

The Figure [Comparison of the micromorphic damage, the damage projected at nodes
and the analytical solution](#damage-values) compares the values of the
micromorphic damage and damage with the analytical solution.
This figure shows that a penalisation factor of \(300\)
is sufficient to get accurate results.

### Convergence

```
| Iteration:  0 | normalized residual norm=1.0000e+00, tolerance: 1.0000e-10, absolute norm=5.4135e+00
| Iteration:  1 | normalized residual norm=3.5655e-01, tolerance: 1.0000e-10, absolute norm=1.9302e+00
| Iteration:  2 | normalized residual norm=6.5988e-02, tolerance: 1.0000e-10, absolute norm=3.5723e-01
| Iteration:  3 | normalized residual norm=3.5531e-02, tolerance: 1.0000e-10, absolute norm=1.9235e-01
| Iteration:  4 | normalized residual norm=2.2725e-02, tolerance: 1.0000e-10, absolute norm=1.2302e-01
| Iteration:  5 | normalized residual norm=1.6086e-02, tolerance: 1.0000e-10, absolute norm=8.7080e-02
| Iteration:  6 | normalized residual norm=9.2915e-03, tolerance: 1.0000e-10, absolute norm=5.0300e-02
| Iteration:  7 | normalized residual norm=5.3642e-03, tolerance: 1.0000e-10, absolute norm=2.9039e-02
| Iteration:  8 | normalized residual norm=2.9985e-03, tolerance: 1.0000e-10, absolute norm=1.6232e-02
| Iteration:  9 | normalized residual norm=7.6708e-04, tolerance: 1.0000e-10, absolute norm=4.1526e-03
| Iteration: 10 | normalized residual norm=2.1499e-04, tolerance: 1.0000e-10, absolute norm=1.1639e-03
| Iteration: 11 | normalized residual norm=2.2891e-16, tolerance: 1.0000e-10, absolute norm=1.2392e-15
```
