<!-- source: https://manta-project.gitlab.io/manta/manta_frontend_user_guide/miscellaneous/utilities.html -->

# Miscellaneous utility features

This section is devoted to describe various utility features.

## Fields

### The `computeIntegral` functions

The `computeIntegral` functions allow to compute the integral of a
field on integration points or the integral of a set of fields on
integration points.

Those functions takes three arguments:

1. the field or the set of fields,
2. the geometric hypothesis,
3. the configuration time.

Warning

For all geometric hypotheses, the `computeIntegral` function
requires the jacobian determinants in the considered configuration to be
available, i.e. that the `PhysicalSystem::requestJacobiansDeterminants`
method (or `ResourcesManager::requestJacobiansDeterminants`) has been
called **before** `PhysicalSystem::initialize` (or `ResourcesManager::init`).

In the axisymmetrical case, the position of the integration points in
the considered configuration to be available, i.e. that the
`PhysicalSystem::requestIntegrationPointsCoordinates` method (or
`ResourcesManager::requestIntegrationPointsCoordinates`) has been
called **before** `PhysicalSystem::initialize` (or `ResourcesManager::init`).

#### Example of usage

```
auto i = computeIntegral(f, ps.getGeometricHypothesis(), ConfigurationTime::initial);
```

### The `computeMeanValue` functions

The `computeMeanValue` functions allow to compute the integral of a
field \(f\) on integration points or the integral of a set of fields
on integration points using the following formula:

\[\left(\frac{1}{\displaystyle\int_{\Omega}\d\,V}\right) \int_{\Omega}f\,\d\,V\]

The `computeMeanValue` functions have the same interfaces and restrictions than the `computeIntegral` functions.

#### Example of usage

```
auto i = computeMeanValue(f, ps.getGeometricHypothesis(), ConfigurationTime::initial);
```
