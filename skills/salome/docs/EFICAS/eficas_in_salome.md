<!-- source: https://docs.salome-platform.org/latest/gui/EFICAS/eficas_in_salome.html -->

# EFICAS in Salome

## Launching EFICAS in Salome

first activate EFICAS module

![figure](https://docs.salome-platform.org/latest/gui/EFICAS/_images/LctDsSalome.png)

Use EFICAS. When a file is saved, Eficas will create an associated entry in the object browser.
It is possible to user the file in other modules (see appropriate module’s documentation).

![figure](https://docs.salome-platform.org/latest/gui/EFICAS/_images/ArbreSalome.png)

## Structural Element (for Aster)

Eficas is able to create “structural element” in GEOM or in SMESH in order to
validate data.

- Create your geometry

![figure](https://docs.salome-platform.org/latest/gui/EFICAS/_images/Salome_Pylone.png)

- Create your eficas JDC, and define for example a beam

![figure](https://docs.salome-platform.org/latest/gui/EFICAS/_images/Salome_Pylone-Eficas.png)

- Click on “View3D”. Eficas shows you the result in GEOM and creates “beams” .
  be aware : these “structural element” are not Geometry elements (You can’t use it)
  It’s also possible to verify normals orientation.

![figure](https://docs.salome-platform.org/latest/gui/EFICAS/_images/Salome_Pylone-SE.png)
