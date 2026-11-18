<!-- source: reference/interpolation/NatureOfField.dox -->

# Nature of a field

## Overview: intensive and extensive field

`NatureOfField` is an enum which helps in determining some physical significance of the field and affects the choice of the interpolation formula (see [Summary](interptheory.md)).
It has five possible values:
-      "NoNature", the default value, does not allow the use of any interpolation tools

For intensive fields:
-      [IntensiveMaximum](interptheory.md), for intensive field with the maximum principle favored over conservativity. Relevant for temperature, pressure fields.

-      [IntensiveConservation](interptheory.md), for intensive field with the conservativity favored over maximum principle. Relevant for power density fields.

For extensive fields:
-      [ExtensiveMaximum](interptheory.md), for extensive field with the maximum principle favored over conservativity. Relevant for power fields.

-      [ExtensiveConservation](interptheory.md), for extensive fields with conservativity favored over the maximum principle. Relevant for power fields.

  

By intensive field we mean a field that represents an intensive physical variable such as density ($kg.m^{-3}$), power density ($W.m^{-3}$), temperature ($K$) or pressure ($Pa$). Typically the physical value doesn't scale with the size of the underlying geometry.  

By extensive (or integral) field we mean a field that represents an extensive physical quantity such as mass ($kg$), volume ($m^3$), a momentum ($kg.m.s^{-1}$) or power $(W$).
Typically the field value scales linearly with respect to the underlying geometry size.
For fields with a P0 representation (cell based), conservativity formulas are different depending on whether the field is extensive or intensive (see [cell-cell (P0->P0) conservative remapping of intensive fields](interptheory.md) and [cell-cell (P0->P0) conservative remapping of extensive fields](interptheory.md)).  

These two notions are themselves split into two sub-categories.
Indeed in some cases (e.g. non [overlapping meshes](interptheory.md)), it is impossible to fulfill both the conservation principle and the maximum principle during the interpolation. The nature of the fields determines the formula to be used for non overlapping cells and thus the property that we will be satisfied.

<b>Finally we consider that fields with P1 or P2 representations are necessarily intensive.</b>

## Usage

In order to use the various [interpolations](intro-interp.md), you have to specify the nature of your field.
When the source and target meshes do not overlap, different treatments will be employed depending on the nature of the source and target fields.
You can specify the nature of the field when you create a [MEDCoupling field](reference/fields/fields.md)
with the following constructor:

```
MEDCouplingFieldDouble(NatureOfField n, MEDCouplingTimeDiscretization *td, MEDCouplingFieldDiscretization *type);
```

If you read or copy an already existing field, or later after its creation, you may want to change/set its nature.
In order to do so, you can use the function

```
void setNature(NatureOfField nat);
```

Here is an example

```
...
const char sourceFileName[]="source.med";
MEDCouplingFieldDouble *sourceField=MEDLoader::ReadFieldCell(sourceFileName,"Source_Mesh",0,"Density",/*iteration0,/*order0);
const char targetFileName[]="target.med";
MEDCouplingUMesh *med_target_mesh=MEDLoader::ReadUMeshFromFile(targetFileName,"Target_Mesh",0);
//
sourceField->setNature(IntensiveMaximum);
...
```
