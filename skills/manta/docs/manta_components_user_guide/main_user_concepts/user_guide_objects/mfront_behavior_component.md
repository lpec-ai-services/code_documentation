<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/main_user_concepts/user_guide_objects/mfront_behavior_component.html -->

# `MFrontBehaviorComponent`

Non-linear behaviors of solid materials can be hard coded in MANTA formulations,
or they can be computed externally through an MFront behavior.
Details on MFront and its use can be found in this
[section of the frontend](../../../manta_frontend_user_guide/miscellaneous/mfront_material_knowledge_management.md#mfront-material-knowledge-management).

This page describes the declaration, in MANTA components, of behaviors based on
externally compiled MFront sources through the `MFrontBehaviorComponent` class.

Note that this is a sibling class to the frontend behavior counterpart `MFrontBehavior`.

## Example of usage

`MFrontBehaviorComponent` requires the following include:

```c++
#include "manta/components-behavior/mfront_behavior_component.h"
```

It is constructed with:

```c++
    auto behavior =
        MFrontBehaviorComponent(spec, GeoType::hex8, QuadId::hex8, behaviorLibPath, behaviorName, "Tridimensional", matp);
```

## Parameters

`MFrontBehaviorComponent` has seven parameters:

- `spec`, the meshSet on which the behavior is integrated,
- `GeoType::hex8`, the geometric type of the cells of that meshSet,
- `QuadId::hex8`, the quadrature rule used to integrate the behavior,
- `behaviorLibPath`, a `std::string` of the path to the compiled library,
- `behaviorName`, a `std::string` of the name of the MFront behavior,
- `"Tridimensional"`, a `std::string` of the geometric hypothesis,
- `matp`, an `OMap<std::string, Vector<Real>>` gathering the material parameters.

Note

To import a behavior one has to specify the path to the binary implementing the law.
In the elasto-plastic example above this binary is `libCharpyBehaviours-generic.so`.
Note that here, in order to look inside the working directory, this path is given
preceded by `./`. If this prefix is not used, the working directory is not checked,
and environment-variable-defined paths such as `LD_LIBRARY_PATH` are checked instead.

The number of material parameters depends on the specific behavior. Here is the
declaration of `matp` for an elastic damage model:

```c++
    OMap<std::string, Vector<Real>> matp;
    matp["YoungModulus"] = {YoungModulus};
    matp["PoissonRatio"] = {PoissonRatio};
```

and for an elasto-plastic model:

```c++
    // > create the behavior
    OMap<std::string, Vector<Real>> matp;

    matp["YoungModulus"]   = {YoungModulusCharpy};
    matp["PoissonRatio"]   = {PoissonRatioCharpy};
    matp["HardeningSlope"] = {HCharpy};
    matp["YieldStrength"]  = {sy0Charpy};
    matp["H"]              = {HCharpy};
    matp["sy0"]            = {sy0Charpy};
    MFrontBehaviorComponent behaviorCharpy(
        charpy, GeoType::hex8, QuadId::hex8, "./libCharpyBehaviours-generic.so", behaviorCharpyName, "Tridimensional", matp);
    // <
```

## State variables and time stepping

`MFrontBehaviorComponent` keeps two copies of the state variables, one at the
beginning of the time step (`bts`) and one at its end (`ets`). Formulations owning behaviors
can call `update()` or `revert()` to pour (`ets`) into (`bts`) and vice versa.
For instance, consider the non-linear resolution of a structural mechanics problem with a newton algorithm.
In such a case, there is a need to call for `solidImplicitForm.update()` at the end of a time-step.

The internal and external state variable fields can be read back as an `IPFieldView`
through `getInternalVariablesField()` and `getExternalVariablesField()`; the
`getInternalVarNames()` / `getInternalVarOffset()` accessors (and their
`External` counterparts) give the layout of these fields.

## List of examples and tests

- `MFrontBehaviorComponent` is used in most implicit and explicit solid-mechanics
  examples (`examples/implicit/*`, `examples/beam`, `examples/cook`,
  `examples/contact/*`, `examples/phasefield/*`),
- in the phase-field component tests
  (`src/components/fem_phasefield_damage/tests/nr`),
- in `src/components/modeling/tests/e2e/nr` (`plasticube`, `rev`, `strip2D`, ...).
- one can check the `PhaseFieldDamageImplicitFormulation` implementation to see a formulation
  that performs a coupling with a solid mechanics formulation by reading/updating the state variables of the behavior.

## Current limitations

The behaviour called through a `MFrontBehaviorComponent` currently is limited to:

- Material properties uniform in space.
- External variables that are scalars.

Users of the components may find those restrictions unsuitable for their use case.
In this case, they may either derive their own implementation by inheriting from `MFrontBehaviorBase`.
For example, they make take inspiration from the `MFrontBehavior` class which heavily relies on evaluators.
