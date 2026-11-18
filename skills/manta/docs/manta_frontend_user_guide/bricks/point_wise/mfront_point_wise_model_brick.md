<!-- source: https://manta-project.gitlab.io/manta/manta_frontend_user_guide/bricks/point_wise/mfront_point_wise_model_brick.html -->

# The `MFrontPointWiseModel` model brick

The `MFrontPointWiseModel` model brick calls an MFront model on
one or several materials.

See also the following sections:

- [Generalities on bricks based on MFront behaviors](../../miscellaneous/mfront_behaviors_bricks.md#mfront-behaviors-bricks),
- [Advices on the management of MFront material knowledge](../../miscellaneous/mfront_material_knowledge_management.md#mfront-material-knowledge-management).

Note

Inline information about the `MFrontPointWiseModel` model
can be retrieved as follows:

PYTHON

```python
manta.info('Model bricks', 'MFrontPointWiseModel')
```

SH

```sh
manta-info "Model bricks:MFrontPointWiseModel"
```

## Example of usage

PYTHON

```python
m.add('MFrontPointWiseModel',
      material = 'cube',
      library = 'src/libBehaviour.so',
      model ='ChemicalReaction5',
      hypothesis = 'planeStrain',
      quadratureOrder = 2)
```

C++

```c++
const auto params = Parameters{{"material", "mesh"},
                               {"library", "src/libBehaviour.so"},
                               {"model", "ChemicalReaction5"},
                               {"hypothesis", "planeStrain"},
                               {"quadratureOrder", 2}};
m->add(ctx, "MFrontPointWiseModel", params);
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
- `quadratureOrder`: order of quadrature.

## Compatible models

This brick is compatible with the following models:

- [The MFrontPointWiseModel model](../../models/point_wise_models/mfront_point_wise_model.md#mfront-pointwise-model)
