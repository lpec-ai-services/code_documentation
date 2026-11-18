<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/manta_components_user_guide.html -->

# User guide of the MANTA components

The MANTA components target researchers in the field of numerical methods which would like to implement and test various algorithms.
Those libraries provides a generic and flexible way to implement a new unstructured-mesh-based numerical method dealing with a
given set of Partial Differential Equations (PDE).

The MANTA components can be used to create:

- Standalone executables,
- Extensions for the MANTA and PyManta frontends.

This section aims at explaining the creation of a MANTA C++ script at this layer.
Furthermore a list of all formulations/solver/algorithms/tools of this layer is also available here.
For further description about the implementation details of MANTA we redirect interested readers to the [developer guide](../developer_guide/developer_guide.md#developer).
For readers interested in solving PDE's not yet available in MANTA, we specifically redirect readers to the [pipeline description](../developer_guide/pipeline/pipeline.md#pipeline).

Contents

- [Catalogs for components](components_catalogs/components_catalogs.md)
- [Main c++ User Concepts](main_user_concepts/general_outline/cpp_user_guide.md)
- [The "module" system](the_module_system/the_module_system.md)
- [User-defined extensions](user_defined_extensions/user_defined_ext.md)
