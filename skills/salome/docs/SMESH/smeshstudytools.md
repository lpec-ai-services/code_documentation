<!-- source: https://docs.salome-platform.org/latest/gui/SMESH/smeshstudytools.html -->

# smeshstudytools module

This module provides a class [`SMeshStudyTools`](#smeshstudytools.SMeshStudyTools) to facilitate the
use of mesh objects in Salome study.

*class* smeshstudytools.SMeshStudyTools(*studyEditor=None*)
:   This class provides several methods to manipulate mesh objects in Salome
    study. The parameter studyEditor defines a
    `StudyEditor` object used to access the study. If
    `None`, the method returns a `StudyEditor`
    object on the current study.

    editor
    :   This instance attribute contains the underlying
        `StudyEditor` object. It can be used to access
        the study but the attribute itself should not be modified.

    displayMeshObjectFromEntry(*entry*)
    :   Display the SMESH object associated to the specified entry
        (the entry is the identifier of an item in the objects browser).

    getMeshFromGroup(*meshGroupItem*)
    :   Get the mesh item owning the mesh group meshGroupItem.

        Parameters:
        :   **meshGroupItem** (*SObject*) – Mesh group belonging to the searched mesh.

        Returns:
        :   The SObject corresponding to the mesh, or None if it was not
            found.

    getMeshObjectFromEntry(*entry*)
    :   Returns the MESH object associated to the specified entry,
        (the entry is the identifier of an item in the objects browser).

    getMeshObjectFromSObject(*sobject*)
    :   Returns the SMESH object associated to the specified SObject,
        (the SObject is an item in the objects browser).

    getMeshObjectSelected()
    :   Returns the MESH object currently selected in the active study.

    updateStudy()
    :   This function updates the tools so that it works on the
        specified study.
