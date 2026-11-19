<!-- source: https://docs.salome-platform.org/latest/gui/HOMARD/en/glossaire.html -->

# Glossary

case
:   A case is defined with an initial mesh and a list of adaptations.

error indicator
:   The error indicator is a field that is expressed over the elements. It represents an estimation of the error between the real solution and the computed solution.

field
:   A field is expressed over a mesh, onto node or element, with 1 or more components.

hypothesis
:   A hypothesis describes the conditions that governs the modification from a mesh to another one: refinement and/or unrefinement, etc. A hypothesis is referenced by 1 or more iterations.

iteration
:   An iteration is the process that transform a mesh to another one into a case. An iteration implies refinement and/or unrefinement, following the associated hypothesis.

level
:   The level of an element corresponds to the number of splitting that were done to obtain it. The levem of the elements in the initial mesh is 0.

MED
:   It is the excange format for the meshes and the fields in SALOME.

refinement
:   The refinement is an operation that consists in splitting the selected elements.

unrefinement
:   The unrefinement is an operation that consists in removing the selected elements. In fact, the objective is to cancel a previous splitting: a ‘higher’ level than the initial mesh cannot be obtained.

zone
:   A zone is a region that may govern the adaptation: every element with at least 2 nodes inside the zone is split or removed, depending on the choice.
