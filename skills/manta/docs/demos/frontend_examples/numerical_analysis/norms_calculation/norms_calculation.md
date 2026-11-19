<!-- source: https://manta-project.gitlab.io/manta/demos/frontend_examples/numerical_analysis/norms_calculation/norms_calculation.html -->

# Applied math: norms calculation for a linear thermal problem

The following tutorial deals with a simple thermal problem with a known
analytical solution. We show how to post-process norms
with MANTA, specifically the \(L^{2}(\Omega)\) and
\(L^{\infty}(\Omega)\) norms of the errors, in order to obtain
convergence order and other error given information, from MANTA.

This example is split into two parts:
- One dimension with a constant source term;
- Two dimensions with a non-constant source term.

The finite element solutions will be compared to both the analytical
solution and the ones computed with Cast3M. The domain considered is
the same for both cases: a rectangle [0; 5] x [0; 1] (for the 1D case,
there is only 1 mesh in the \(y\) direction).

Note

The following files are required to run the tutorial:

- [`castem_1d_case.dgibi`](https://manta-project.gitlab.io/manta/_downloads/54bb4f6e9aed7a5cc117c69521f3a2d1/castem_1d_case.dgibi):
  the Cast3M input file required to generate the mesh in 1D case.
- [`castem_2d_case.dgibi`](https://manta-project.gitlab.io/manta/_downloads/66f8d067f7e46b534cb2df6966e57ad6/castem_2d_case.dgibi):
  the Cast3M input file required to generate the mesh in 2D case.
- [`LinearHeatTransfer.mfront`](https://manta-project.gitlab.io/manta/_downloads/2698de5e63b237f7d723ab4adb3f8d2a/LinearHeatTransfer.mfront): the MFront implementation of the linear heat transfer
- [`test1.py`](https://manta-project.gitlab.io/manta/_downloads/7baf15bf597f63310debd8572bb698e3/test1.py): the main script for 1D case
- [`test2.py`](https://manta-project.gitlab.io/manta/_downloads/c120d64fe21eeb9a62c411263c7527d2/test2.py): the main script for 2D case

## Error and norm computation

We use two different norms, \(L^{2}(\Omega)\) and
\(L^{\infty}(\Omega)\).

The error is computed as follows:

\[e_h = u - u_h\]

where \(u\) is the analytical solution and \(u_h\) the finite
element solution.

The norms of the error are

- \[||e_h||_{L^{2}(\Omega)} = ||u - u_h||_{L^{2}(\Omega)} = \sqrt{\int_{\Omega} (u-u_h)² d\Omega} = \sqrt{ \sum_{K \in \Omega} \int_{K} (u-u_h)² dK};\]
- \[||e_h||_{L^{\infty}(\Omega)} = ||u - u_h||_{L^{\infty}(\Omega)} = \max(|u - u_h|) .\]

In the implementation section, we will see how to declare error norms type post-processings in MANTA.

## Physical system

### 1D constant source term case

The equation is

\[-\lambda T'' = s\]

with the boundary conditions

\[T|_{x=0} = T_i \text{ and } -\lambda T'|_{x=xmax} = g\]

where \(\lambda\) is the thermal conductivity, \(g\) the imposed
flux, \(s\) the source term and \(T_i\) the imposed temperature.
We take \(\lambda = 230\) (aluminium), \(g=500\), \(s = 20\)
and \(T_i = 25\).

### 2D non constant source term case

For the 2D case, the equation is

\[-\lambda \Delta T =\frac{\pi^{2}}{2}\sin{(\frac{\pi}{2}x)}\sin{(\frac{\pi}{2}y)}\]

with the boundary conditions

\[T|_{x=0} = T|_{y=0} = T_i \text{ and } -\lambda \frac{\partial T}{\partial x}\Big|_{x=xmax} = -\lambda \frac{\partial T}{\partial y}\Big|_{y=ymax} = 0\]

where \(\lambda\) is the thermal conductivity, \(g\) the imposed
flux, \(s\) the source term and \(T_i\) the imposed temperature.
We take \(\lambda = 1\) and \(T_i = 25\).

## Description of the input file

In this section we will only discuss how to implement norms calculation in MANTA, to have an overview
of the script of this test case, please refer to the appendix.

We first need, as a function, the analytical solution that we declare in MANTA as a scalar spatio temporal loading

```python
# Declaring 'HeatSourceValue' and 'ImposedHeatFluxValue'
ps.addLoadingEvolution('ImposedHeatFluxValue', lambda t: g * t)
ps.addLoadingEvolution('HeatSourceValue', lambda t: q * t)

ps.setModel(m)
```

Then, we can declare the wanted norms as MANTA post-processings (`L2Distance` for the \(L^{2}(\Omega)\) norm for example).
For these post-processings :cxx:firstField is the computed temperature, and `secondField` the analytical solution.
The error can be computed on nodes or integration points. On the choice of the integration point support,
a quadrature order is needed

```python

ps.addScalarSpatiotemporalLoading(computeReferenceSolution, name = 'ReferenceSolution', material = 'bar')

ps.addPostProcessing('LineCurves', file = 'temperature.res', line = 'bottom',
                     precision = 14, nodalValues = ['Temperature'])

ps.addPostProcessing('Curves', file = 'results.res', fileFormat = 'txt',
```

the `L2Distance` and `AbsoluteDistance` are computed on
integration points and another `AbsoluteDistance` is computed on the
nodes.

## Execution

First, we build MFront library with

```
$ mfront --obuild --interface=generic LinearHeatTransfer.mfront
```

and we can run the simulation

```
$ python3 test1.py
```

## Simulation

### First case

[Fig. 33](#temperature-profile-ex1) shows that temperature is decreasing with \(x\) and that
MANTA and Cast3M give the same result.

[![figure](https://manta-project.gitlab.io/manta/_images/temperature_profile.png)](https://manta-project.gitlab.io/manta/_images/temperature_profile.png)

Fig. 33 Temperature as a fonction of \(x\) coordinate [0;5] given by MANTA and Cast3M.

The error comparison for the quadratic finite element in [Fig. 34](#error-norms-1d)
outlines the fact that the convergence order is 2 and that MANTA exhibits
a larger error than Cast3M.

This figure also highlights the difference between norms, with the
absolute norm always performing better than the L2 norm.

[![figure](https://manta-project.gitlab.io/manta/_images/error_norms.png)](https://manta-project.gitlab.io/manta/_images/error_norms.png)

Fig. 34 Comparison of \(L^{2}(\Omega)\) and \(L^{\infty}(\Omega)\)
error norms for MANTA and Cast3M for case one.

### Second case

The MANTA computed temperature field is shown in [Fig. 35](#result-field-temperature-2d).

[![figure](https://manta-project.gitlab.io/manta/_images/result_field_temperature.png)](https://manta-project.gitlab.io/manta/_images/result_field_temperature.png)

Fig. 35 Temperature field computed by MANTA for the case two.

[Fig. 36](#error-result-ex2-castem-vs-manta), shows that the error norms are the same
for both Cast3M and MANTA. Note that the order of convergence is
2, and the \(L^{2}(\Omega)\) norm is larger than the
\(L^{\infty}(\Omega)\) norm.

[![figure](https://manta-project.gitlab.io/manta/_images/error_result_ex2_castem_vs_manta.png)](https://manta-project.gitlab.io/manta/_images/error_result_ex2_castem_vs_manta.png)

Fig. 36 Comparison of \(L^{2}(\Omega)\) and
\(L^{\infty}(\Omega)\) error norms for MANTA and Cast3M
for case two.

Note

[Fig. 37](#error-result-ex2-castem-ip-vs-nodes) displays, for Cast3M error norms, the difference
between source terms defined on nodes and those defined on integration
points. As we can see, source terms defined on nodes perform worse
compared to those defined on integration points. In fact, the factor
between the same norms for nodes and integration point
(\(\frac{||e_h^N||_{L^p(\Omega)}}{||e_h^{IP}||_{L^{p}(\Omega)}}\))
is approximately 3. MANTA automatically provides source terms defined on integration points that makes
MANTA errors lower than Cast3M ones.

[![figure](https://manta-project.gitlab.io/manta/_images/error_result_ex2_castem_ip_vs_nodes.png)](https://manta-project.gitlab.io/manta/_images/error_result_ex2_castem_ip_vs_nodes.png)

Fig. 37 Comparison of \(L^{2}(\Omega)\) and
\(L^{\infty}(\Omega)\) error norms for integration point or nodes
defined source term in Cast3M.

## Appendix

### Appendix 1 : Analytical solution

For the first case, 1d with a constant source term, the analytical solution is given by

\[T(x) = -\frac{s}{2 \lambda} x^{2} + \frac{(s x_{max}-g)}{\lambda} x + T_i\]

For the second case, 2D with a non constant source term, the analytical solution is given by

\[T(x,y) = \frac{1}{\lambda}\sin{(\frac{\pi}{2}x)}\sin{(\frac{\pi}{2}y)} + T_i\]

### Appendix 2 : Implementation

In this appendix, we only discuss how to implement the first case since the second case is easily transposable.
After `import manta`, we set the verbosity level to 3 in order to get
information of internal iterations. Moreover, we set two variables that
will contain the values of the time step at the beginging and the end.

```python
bts = manta.TimeStepStage.beginningOfTimeStep
ets = manta.TimeStepStage.endOfTimeStep
manta.setDefaultVerbosityLevel(manta.VerbosityLevel.verboseLevel3)
```

We also declare values of the properties

```python
k,q,Ti,g,l = 230.,20.,25.,500.,5.
```

The constants of the problems are not the same for both cases.

#### Physical system

The physical system is created using the MANTA `Grid` generator as
follows:

```python
ps = manta.PhysicalSystem(mesh = {'generator': 'Grid', 'spaceDimension': 2,
                                  'lengths': [l, 1], 'numberOfElements': [500, 1],
                                  'centerPosition': [l/2, 0.5], 'domain': 'bar'},
                          geometricHypothesis = 'inPlane')
```

for the 2D case, since the
domain remains the same, we only need to modify `numberOfElements` by
parameterizing the space discretization in the \(y\) direction.

#### Implicit heat transfer model and material declaration

Even if the properties are linear, the user has to declare the thermal model solver
as nonlinear since MANTA need an MFront declared material.

```python
linear_solver_options = {'direct': {},
                         'methodForConstraint': 'schurComplement'}
```

Then the MFront behavior library is added

```python
# Creating the thermal model
m = manta.Model('ImplicitHeatTransfer', ps,
```

and the thermal conductivity property (that is needed by MFront) can
be inserted

```python

```

#### Boundary conditions and heat source

The boundary conditions and heat source have to be declared as follows:

```python
m.add('SolidMaterial', material = 'bar',
      library = 'src/libBehaviour.so', behavior = 'LinearHeatTransfer', hypothesis = 'planeStrain')

# Declaring properties
ps.addProperty('Constant', name = 'ThermalConductivity', material = 'bar', value = k)

# Declaring the boundary conditions
```

Note that for the second example the `HeatSourceValue` is a space
dependent function and must be declared using
the `addScalarSpatiotemporalLoading` function.

#### Coupling scheme

A coupling scheme is needed, and the simplest one (since we only deal
with thermal simulation) is declared by:

```python
m.add('HeatSource', material = 'bar', value = 'HeatSourceValue')
```

#### Post-processing

We need temperature on the domain as post-processings

```python
    A = (q * l - g) / k
    T = Ti + A * x - (q / (2 * k)) * x * x
```

#### Run simulation

Finally, we can initialize and run the simulation

```python
                                               'fieldType': 'ipField', 'material': 'bar', 'quadratureOrder': 2}},
                               {'AbsoluteDistance': {'firstField': 'Temperature', 'secondField': 'ReferenceSolution',
                                                     'fieldType': 'nodeField', 'material': 'bar'}},
                               {'AbsoluteDistance': {'firstField': 'Temperature', 'secondField': 'ReferenceSolution',
                                                     'fieldType': 'ipField', 'material': 'bar', 'quadratureOrder': 2}}])
```
