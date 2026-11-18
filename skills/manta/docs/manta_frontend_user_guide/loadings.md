<!-- source: https://manta-project.gitlab.io/manta/manta_frontend_user_guide/loadings.html -->

# Loadings

Loadings is a generic concept that is used, generally by boundary
conditions, to describe the action of the rest of the universe on some
part of the physical system of interest.

For instance, loadings may describe the spatio-temporal evolution of the
pressure of an external gas on the outer boundary of a pipe. This
evolution is used by the `ImposedPressure` brick to define the
appropriate boundary condition in the `ImplicitMechanics` model.

See also

Further help about available loadings can be found in the
`Loadings` section of the online help which is accessible in
python through the manta.info function or through the manta-info
utility (see Section [The manta-info utility](miscellaneous/tools.md#manta-info-utility)).

PYTHON

```python
manta.info('Loadings')
```

SH

```sh
manta-info Loadings
```

## Available loadings

### ConstantUniform

This loading describes a constant (in time) and uniform (in space) loading

C++

```c++
const auto r = Vector<Parameter>{Vector<Parameter>{0, 1, 0},
                                 Vector<Parameter>{1, 0, 0},
                                 Vector<Parameter>{0, 0, 1}};
ps.addLoading(ctx, "ConstantUniform",
              Parameters{{"material", "cube"},
                         {"name", "RotationMatrixToMaterialFrame"},
                         {"value", r}});
```

#### Parameters

The following parameters are allowed:

- `value`: value of the loading.
- `boundaries`: names of boundaries (regular expressions).
- `materials`: materials names (regular expressions) (equivalent
  to domains).
- `name`: name of the loading.
- `boundary`: name of a boundary (regular expression).
- `domains`: domains names (regular expressions) (equivalent to
  materials).
- `material`: material name (regular expression) (equivalent to
  domain).
- `domain`: domain name (regular expression) (equivalent to material).

### ConstantUniformScalar

This loading describes a constant (in time) and uniform (in space) scalar loading

#### Example of usage

```python
ps.addLoading('ConstantUniformScalar',
              name = 'Temperature',
              material = 'cube',
              value = 293.15)
```

#### Parameters

The following parameters are allowed:

- `name`: name of the loading.
- `value`: value of the loading.
- `boundaries`: names of boundaries (regular expressions).
- `materials`: materials names (regular expressions) (equivalent
  to domains).
- `boundary`: name of a boundary (regular expression).
- `domains`: domains names (regular expressions) (equivalent to
  materials).
- `material`: material name (regular expression) (equivalent to
  domain).
- `domain`: domain name (regular expression) (equivalent to material).

## Defining spatiotemporal loadings in Python

The `addScalarSpatiotemporalLoading` method of the PhysicalSystem
class allows to define a loading as a function of the time \(t\) and/or
space, with the coordinates.

The function must have 2 arguments in \(1D\), 3 arguments in
\(2D\) and 4 arguments in \(3D\).

### Example of usage

The following code adds a loading named `testLoading` on a
material named `cube` in \(2D\) defined by the following
spatiotemporal function \(f(t, x, y) = x + y\) (the time variable is
unused):

```python
def f(t, x, y):
 return x + y

ps.addScalarSpatiotemporalLoading(f, name = "testLoading",
                                  material = "cube")
```

Usage of a unnamed function (called lambda function in Python) allows
to shorten this example as follows:

```python
ps.addScalarSpatiotemporalLoading(lambda t, x, y : x + y,
                                  name = "testLoading",
                                  material = "cube")
```

### Parameters

The following parameters are allowed:

- `name`: name of the loading.
- `boundaries`: names of boundaries (regular expressions).
- `materials`: materials names (regular expressions) (equivalent
  to domains).
- `boundary`: name of a boundary (regular expression).
- `domains`: domains names (regular expressions) (equivalent to
  materials).
- `material`: material name (regular expression) (equivalent to
  domain).
- `domain`: domain name (regular expression) (equivalent to material).
- `configurationTime`: the configuration on which the function is
  evaluated. This parameter can be `initial` or `current`
  (`Initial` or `Current` are also accepted).
