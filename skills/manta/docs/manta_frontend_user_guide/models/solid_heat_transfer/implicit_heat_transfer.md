<!-- source: https://manta-project.gitlab.io/manta/manta_frontend_user_guide/models/solid_heat_transfer/implicit_heat_transfer.html -->

# Implicit heat transfer

This page describes the *ImplicitHeatTransfer* model.

## Description

This model aims at determining the temperature field
\(\ets{T}\) (denoted \(T\) in the following, when no
confusion is possible) at the end of a time step by solving a non
linear system of the form:

(5)\[ \mathbb{R}\paren{\ets{T}} = 0\]

In MANTA, the residual \(\mathbb{R}\) is computed by summing the
contributions of bricks (see Paragraph
[Available algorithms](#manta-user-guide-implicit-heat-transfer-bricks)) with the
convention that the residual is the difference bewteen internal heat flux
(see Section [The ImplicitHeatTransferSolidMaterial brick](../../bricks/solid_heat_transfer/implicit_heat_transfer_solid_material.md#implicit-heat-transfer-solid-material-brick) for
example) and external heat flux (see Section
[The HeatSource brick](../../bricks/solid_heat_transfer/implicit_heat_transfer_heat_source.md#implicit-heat-transfer-heat-source-brick) for example).

## Available algorithms

Currently, only the basic Newton algorithm is available to solve
Equation [(5)](#equation-manta-user-guide-implicit-heat-transfer-residual).
