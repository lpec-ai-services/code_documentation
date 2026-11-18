<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/user_defined_extensions/plugins.html -->

# Plug-ins usage

## The `loadPlugin` function

The `loadPlugin` allows to load a shared library. After loading the
library, it automatically calls a function named
`manta_plugin_init`.

PYTHON

```python
manta.core.loadPlugin('libmanta_plugin.so')
```

C++

```c++
auto success = loadPlugin("libmanta_plugin.so");
```

The `manta_plugin_init` function is usually used to register user
defined extensions in the various factories provided by MANTA (see
Section [Factory functions and abstract factories](../../developer_guide/dev_guidelines/patterns.md#abstract-factories)).

### Available factories

The following abstract factories are available currently:
`CurveFactory`, `PostProcessingFactory`,
`ModelBrickFactory`, `ModelFactory`, `LoadingFactory`,
`PropertyFactory`, `CouplingSchemeFactory`,
`CompressibleInviscidFluidSolverFactory`,
`ImplicitMechanicsSolidMaterialFormulationsFactory`.

### Example

The following implementation of the `manta_init_plugin` function
registers a new brick implemented by the
UserDefinedLinearConvectionBrick class in the `ModelBrick` class:

```c++
extern "C" {

MANTA_VISIBILITY_EXPORT bool manta_plugin_init(Context *const ctx)
{
  using namespace manta;
  auto &f = ModelBrickFactory::get();
  auto g  = makeStandardModelBrickGenerator<UserDefinedLinearConvectionBrick>();
  if (!f.registerGenerator(*ctx, "UserDefinedLinearConvection", g)) {
    return ExitStatus::failure;
  }
  return ExitStatus::success;
}

} // end of extern "C"
```
