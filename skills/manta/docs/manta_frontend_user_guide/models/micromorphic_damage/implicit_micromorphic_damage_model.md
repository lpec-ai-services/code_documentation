<!-- source: https://manta-project.gitlab.io/manta/manta_frontend_user_guide/models/micromorphic_damage/implicit_micromorphic_damage_model.html -->

# Implicit micromorphic damage model

The micromorphic damage approach to fracture has been introduced by
Siedel et al. (see [[FHS+22](../../../references/references.md#id26), [Sie23](../../../references/references.md#id24)],
and the references therein), following the seminal work of Forest
[[For09](../../../references/references.md#id25)], as a variational regularization of
classical phase-field approaches to brittle fracture.

The micromorphic approach to fracture is however quite general and can
be used to implement a wide range of models describing both brittle and
ductile failure.

The main advantage of the micromorphic damage approach is that the
damage irreversibility is treated locally, at the integration points.
The main drawback is that a penalization parameter enters the
formulation. However, as shown by [[FHS+22](../../../references/references.md#id26)], this
parameter can be choosen in a straight forward manner, independently of
the problem treated, so it is not an issue in practice.

The ImplicitMicromorphicDamageResourcesManager described in
[this section](../../bricks/micromorphic_damage/implicit_micromorphic_damage_brick.md#implicit-micromorphic-damage-solid-material-brick) is only
meant to describe the evolution of a (scalar) micromorphic degree of freedom,
name the micromorphic damage and denoted \(d_{\chi}\) in the
following. This model is meant to be coupled with a mechanical model in
a staggered approach.
