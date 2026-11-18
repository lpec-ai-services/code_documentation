<!-- source: https://manta-project.gitlab.io/manta/manta_frontend_user_guide/bricks/solid_mechanics/nodal/nodal_mass_brick.html -->

# The `NodalMass` brick

The `NodalMass` brick implements concentrated mass for nodal elements.

It corresponds to the [NodalMassMatrixFormulation](../../../../manta_components_user_guide/formulations/solid_mechanics/beams_and_shells/nodal/nodal_mass_matrix_formulation.md#formulation-nodal-mass) found
in MANTA's components.

## Example of usage

The following code adds the a `NodalMass` brick to a mechanical model:

```python
        model.add(
            'NodalMass',
            domain     = 'right', 
            hypothesis = 'tridimensional', 
            mass       = CONCENTRATED_MASS,
        )
```

## Main parameters

The main parameters used to initialize the brick are:

- `material` or `domain`:
  mesh set over which the brick is defined
- `materials` or `domains`:
  list of mesh set over which the brick is defined
- `hypothesis`:
  structural hypothesis
- `mass`:
  value of the mass to be added to each 1-node element

## Physical description

This brick implements **translational nodal masses**, or **concentrated masses**.

Masses are added at each 1-node element, the given value for the mass **is not
distributed** over the whole `MeshSet`.

Masses are by default translational only and do not integrate any rotational inertias.

The added concentrated masses are isotropic, i.e. the translational inertias
are equal in each direction.

## Supported structural hypotheses and elements

The following table summarizes the list of supported structural
hypotheses and, for each hypothesis, the list of elements.

| Structural hypothesis | Supported elements |
| --- | --- |
| *Tridimensional* | *poi1* |
| *PlaneStrain* | *poi1* |
| *PlaneStress* | *poi1* |
| *Axisymmetrical* | *poi1* |

## Compatible models

This brick is compatible with the following models:

- [The ExplicitMechanics model](../../../models/solid_mechanics/explicit_solid_mechanics.md#explicit-mechanics-model)
