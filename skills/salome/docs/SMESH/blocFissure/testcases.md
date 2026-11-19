<!-- source: https://docs.salome-platform.org/latest/gui/SMESH/blocFissure/testcases.html -->

# Test cases

A base of 28 test cases guarantees the correct functioning of « Bloc Fissure ». 12 cases are dedicated to [cracked bended pipes](#pipetc) and the others 16 are for other [generic geometries](#generictc). They are shown here in order to illustrate cases on which « Bloc Fissure » works.

## Generic cases

All 16 cases are shown Table 2. Two views show the whole cracked structure and a zoom onto the crack with its tore.

|  |  |
| --- | --- |
| CubeAngle | |
| [figure](https://docs.salome-platform.org/latest/gui/SMESH/blocFissure/_images/01_CubeAngle.png) | [figure](https://docs.salome-platform.org/latest/gui/SMESH/blocFissure/_images/01_CubeAngle_a.png) |
| CubeAngle_2 | |
| [figure](https://docs.salome-platform.org/latest/gui/SMESH/blocFissure/_images/02_CubeAngle_2.png) | [figure](https://docs.salome-platform.org/latest/gui/SMESH/blocFissure/_images/02_CubeAngle_2_a.png) |
| cubeCoin | |
| cubeMilieu | |
| cubeTransverse | |
| cylindre | |
| [figure](https://docs.salome-platform.org/latest/gui/SMESH/blocFissure/_images/03_cylindre.png) | [figure](https://docs.salome-platform.org/latest/gui/SMESH/blocFissure/_images/03_cylindre_a.png) |
| cylindre_2 | |
| [figure](https://docs.salome-platform.org/latest/gui/SMESH/blocFissure/_images/04_cylindre_2.png) | [figure](https://docs.salome-platform.org/latest/gui/SMESH/blocFissure/_images/04_cylindre_2_a.png) |
| disquePerce | |
| [figure](https://docs.salome-platform.org/latest/gui/SMESH/blocFissure/_images/05_disque.png) | [figure](https://docs.salome-platform.org/latest/gui/SMESH/blocFissure/_images/05_disque_a.png) |
| ellipse_1 | |
| [figure](https://docs.salome-platform.org/latest/gui/SMESH/blocFissure/_images/06_ellipse_1.png) | [figure](https://docs.salome-platform.org/latest/gui/SMESH/blocFissure/_images/06_ellipse_1_a.png) |
| ellipse_2 (tilted crack) | |
| [figure](https://docs.salome-platform.org/latest/gui/SMESH/blocFissure/_images/07_ellipse_2.png) | [figure](https://docs.salome-platform.org/latest/gui/SMESH/blocFissure/_images/07_ellipse_2_a.png) |
| eprouvetteCourbe | |
| [figure](https://docs.salome-platform.org/latest/gui/SMESH/blocFissure/_images/08_eprouvetteCourbe.png) | [figure](https://docs.salome-platform.org/latest/gui/SMESH/blocFissure/_images/08_eprouvetteCourbe_a.png) |
| eprouvetteDroite | |
| [figure](https://docs.salome-platform.org/latest/gui/SMESH/blocFissure/_images/09_eprouvetteDroite.png) | [figure](https://docs.salome-platform.org/latest/gui/SMESH/blocFissure/_images/09_eprouvetteDroite_a.png) |
| eprouvetteDroite_2 | |
| [figure](https://docs.salome-platform.org/latest/gui/SMESH/blocFissure/_images/10_eprouvetteDroite_2.png) | [figure](https://docs.salome-platform.org/latest/gui/SMESH/blocFissure/_images/10_eprouvetteDroite_2_a.png) |
| faceGauche | |
| [figure](https://docs.salome-platform.org/latest/gui/SMESH/blocFissure/_images/11_faceGauche.png) | [figure](https://docs.salome-platform.org/latest/gui/SMESH/blocFissure/_images/11_faceGauche_2.png) |
| faceGauche_2 | |
| [figure](https://docs.salome-platform.org/latest/gui/SMESH/blocFissure/_images/12_faceGauche_2.png) | [figure](https://docs.salome-platform.org/latest/gui/SMESH/blocFissure/_images/12_faceGauche_2_a.png) |
| vis (Crack is in the radius filet between the screw head and the screw shank) | |
| [figure](https://docs.salome-platform.org/latest/gui/SMESH/blocFissure/_images/13_vis_1.png) | [figure](https://docs.salome-platform.org/latest/gui/SMESH/blocFissure/_images/13_vis_1_2.png) |
| tube | |

## Cracked bended pipes

All 12 bended pipe test cases are not shown here because they are relatively similars with each others. Only test case cas coude_0 et coude_3 are presented, those two tests being based on the same geometry and having a crack on the internal and on the external surface.

|  |  |
| --- | --- |
| [figure](https://docs.salome-platform.org/latest/gui/SMESH/blocFissure/_images/coude_0.png) | [figure](https://docs.salome-platform.org/latest/gui/SMESH/blocFissure/_images/coude_0_2.png) |
| View of the external crack of test_coude_0 |
| [figure](https://docs.salome-platform.org/latest/gui/SMESH/blocFissure/_images/coude_3.png) |
| Bended pipe test case coude_0 with an external crack | View of the internal crack of test_coude_3 |

coude_0 can be computed using this file for the data:

> - [`data for a bended puipe`](https://docs.salome-platform.org/latest/gui/SMESH/blocFissure/_downloads/87ca25f0d2d2d949c2d4a127f373f86a/dialogFissureCoude.dic)

« Bloc Fissure » is very efficient for the case of bended pipes. The generation of the geometry and the crack insertion takes only around 15s.

## Data for the test cases

All the files for these test cases are stored in the directory of the installation of SALOME:

`Salome-VXXXX_package-YY/modules/SMESH_VXXXX/lib/python3.6/site-packages/salome/blocFissure`

The set of the med, xao and brep files can be created by the following importation:

> from blocFissure.materielCasTests import genereMateriel

Once the files are generated, they are saved into the directory of the installation of SALOME:

`Salome-VXXXX_package-YY/modules/SMESH_VXXXX/lib/python3.6/site-packages/salome/blocFissure/materielCasTests`

There is no need to generate them again.

To check the installation of salome, the test cases can be computed by the salome test process:

```python
salome -test blocFissure
```

## Running test cases

The test cases can be executed via the following instructions:

```python
from blocFissure.CasTests.blocFissureTest import blocFissureTest
BLOCFISSURE_TEST = blocFissureTest(list_of_cases)
MESSAGE_ERREUR = BLOCFISSURE_TEST.lancement()
sys.stdout.write(MESSAGE_ERREUR)
del BLOCFISSURE_TEST
```

If `list_of_cases` is an empty list, all the cases are computed.

If not, `list_of_cases` is made of the list of the numbers and/or the name of the requested case. The index of each test is the position of the test in the following table, from 0 for cubeAngle, 1 for cubeAngle_2, 2 for cubeCoin… from top to bottom, then from left to right.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| cubeAngle | cylindre_2 | eprouvetteDroite_2 | fissureCoude_3 | fissureCoude_9 |
| cubeAngle_2 | disquePerce | faceGauche | fissureCoude_4 | fissure_Coude |
| cubeCoin | ellipse_1 | faceGauche_2 | fissureCoude_5 | fissure_Coude_4 |
| cubeMilieu | ellipse_2 | fissureCoude_1 | fissureCoude_6 | vis_1 |
| cubeTransverse | eprouvetteCourbe | fissureCoude_10 | fissureCoude_7 |  |
| cylindre | eprouvetteDroite | fissureCoude_2 | fissureCoude_8 |  |
