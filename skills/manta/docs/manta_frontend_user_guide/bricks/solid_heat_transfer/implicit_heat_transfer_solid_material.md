<!-- source: https://manta-project.gitlab.io/manta/manta_frontend_user_guide/bricks/solid_heat_transfer/implicit_heat_transfer_solid_material.html -->

# The `ImplicitHeatTransferSolidMaterial` brick

Note

This brick relies on an **external** MFront behavior to work.
Please read Sections [Generalities on bricks based on MFront behaviors](../../miscellaneous/mfront_behaviors_bricks.md#mfront-behaviors-bricks) and
[Advices on the management of MFront material knowledge](../../miscellaneous/mfront_material_knowledge_management.md#mfront-material-knowledge-management) for addtional details
and advices.

## About the behavior

The behaviour must have been generated using MFront generic
interface.

The requirements of the behavior, corresponding to its material
properties and external state variables respectively, are automatically
declared by the brick and treated by the dependency management
algorithm. In the case of orthotropic behaviors, a dependency to the
rotation matrix (expressed in the reference configuration) is
automatically declared.

The state variables of the behavior are automatically used to fulfill
dependencies of other models or post-processing by the dependency
management algorithm.

### Example of usage

The following code adds the an *ImplicitHeatTransferSolidMaterial*
brick to a mechanical model:

```c++
heat_transfer_model->add(
    ctx, "ImplicitHeatTransferSolidMaterial",
    Parameters{{"domain", "cube"},
               {"library", "./libHeatTransferBehaviours-generic.so"},
               {"behavior", "IsotropicStationaryLinearHeatTransfer"}});
```

```python
heat_transfer_model.add('ImplicitHeatTransferSolidMaterial',
                        material = 'cube',
                        # or equivalently: domain = 'cube'
                        library = './libHeatTransferBehaviours-generic.so',
                        behavior = 'IsotropicStationaryLinearHeatTransfer')
```

### Main parameters

The main parameters used to initialize the brick are:

- `domain` (which must be a string) or `domains` (which must
  be an array of strings). Each of those strings are interpreted as
  regular expressions.
- `library` (which must be a string), which indicates in which
  library the MFront behavior must be loaded.
- `behavior` (which must be a string), which indicates which
  behavior must be loaded in the library.
- `hypothesis` (which must be a string), which indicated which
  structural hypothesis shall be used. This is only useful in 2D under the
  inPlane geometric hypothesis:

  - In 3D, the Tridimensional structural hypothesis is automatically selected.
  - In 2D, the Axisymmetrical structural hypothesis is automatically
    selected if the corresponding geometric hypothesis is set.
- exportTemperatureGradient: boolean stating if the temperature
  gradient shall be exported (`true` by default).
- exportHeatFlux: boolean stating if the heat flux shall be exported
  (`true` by default).
- `quadratureOrder` (which must be a positive integer). This
  parameter is *optional* and allows to select the quadrature order.
- `integrationScheme` (which must be a string). This
  parameter is *optional* and defaults to default. It allows to select
  an integration scheme, as an identifier for specific formulation. This
  parameter is only useful when using user-defined formulations
  (see [User-defined extensions](#implicit-heat-transfer-user-defined-extensions)).

### Description

The *ImplicitHeatTransferSolidMaterial* brick` computes
the jacobian and the residual associated with the following
variational operator:

(10)\[\int_{\Omega_{r}}\v{j}\,\cdot\,\vGradient\paren{\var{T}} \d\,V\]

where:

- \(\Omega_{r}\) is the domain on which the brick is defined, in the
  reference configuration,
- \(\var{T}\) is a kinematically admissible virtual variation of
  the temperature field,
- \(\v{j}\) is the heat flux,
- \(\vGradient\paren{\var{T}}\) is the gradient of virtual variation
  of the temperature in the reference configuration.

Note

The *ImplicitHeatTransferSolidMaterial* brick deleguates the
computation of the inner heat flux and conductivity matrix to the
`ImplicitHeatTransferSolidMaterialFormulation` class. This class
can be used directly by advanced users.

### Supported structural hypotheses and elements

The following table summarizes the list of supported structural
hypotheses and, for each hypothesis, the list of elements.

| Structural hypothesis | Supported elements |
| --- | --- |
| *Tridimensional* | *tet4*, *tet10*, *hex8*, *hex20*, *pyr5* |
| *PlaneStrain* | *tri3*, *tri6*, *tri10*, *qua4*, *qua8* |
| *PlaneStress* | *tri3*, *tri6*, *tri10*, *qua4*, *qua8* |
| *Axisymmetrical* | *tri3*, *tri6*, *tri10*, *qua4*, *qua8* |

### User-defined extensions

User can register variants of the previous built-in formulations by registring new
generators to the cxx:ImplicitHeatTransferSolidMaterialFormulationsFactory class.

### Compatible models

This brick is compatible with the following models:

- [Implicit heat transfer](../../models/solid_heat_transfer/implicit_heat_transfer.md#implicit-heat-transfer-model)
