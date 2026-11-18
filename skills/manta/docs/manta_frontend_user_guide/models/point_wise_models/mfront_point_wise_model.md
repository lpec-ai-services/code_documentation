<!-- source: https://manta-project.gitlab.io/manta/manta_frontend_user_guide/models/point_wise_models/mfront_point_wise_model.html -->

# The `MFrontPointWiseModel` model

The `MFrontPointWiseModel` model interfaces an external MFront
model. This model is mostly a wrapper around the
[MFrontPointWiseModel model
brick](../../bricks/point_wise/mfront_point_wise_model_brick.md#manta-frontend-user-guide-mfront-point-wise-model-brick). As a
consequence, no other brick can be added to this model.

Note

Inline information about the `MFrontPointWiseModel` model
can be retrieved as follows:

PYTHON

```python
manta.info('Models', 'MFrontPointWiseModel')
```

SH

```sh
manta-info Models:MFrontPointWiseModel
```

## Example of usage

PYTHON

```python
ps.setModel('MFrontPointWiseModel',
            material = 'cube',
            library = 'src/libBehaviour.so',
            model ='ChemicalReaction5',
            hypothesis = 'planeStrain',
            quadratureOrder = 2)
```

C++

```c++
const auto m = Parameters{{"material", "mesh"},
                          {"library", "src/libBehaviour.so"},
                          {"model", "ChemicalReaction5"},
                          {"hypothesis", "planeStrain"},
                          {"quadratureOrder", 2}};
ps->setModel(ctx, "MFrontPointWiseModel", m);
```

## Available parameters

The following parameters are avaiable:

- `model`: name of the point wise model.
- `material`: material name (regular expression) (equivalent to
  `domain`).
- `materials`: materials names (regular expressions) (equivalent
  to `domains`).
- `domain`: domain name (regular expression) (equivalent to
  `material`).
- `domains`: domains names (regular expressions) (equivalent to
  `materials`).
- `library`: path to the MFront library (string).
- `hypothesis`: structural hypothesis (string). Valid values
  are: `PlaneStrain`, `PlaneStress`, `Tridimensional`, etc.
- `quadratureOrder`: order of quadrature (optional).
- `logFile`: log file.
- `verbosityLevel`: verbosity level
