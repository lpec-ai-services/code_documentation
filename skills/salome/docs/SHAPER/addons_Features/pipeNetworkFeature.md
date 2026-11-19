<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/addons_Features/pipeNetworkFeature.html -->

# Réseau de tuyaux

Cette macro crée les objets SHAPER correspondant à un réseau de tuyauteries décrit dans un fichier texte.

Pour créer l’objet de la tuyauterie :

1. Choisir dans le menu principal *Macros - > Réseau de tuyaux* ou
2. Cliquer le bouton ![pipeNetwork.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/pipeNetwork.png) **Réseau de tuyaux** dans la barre des macros.

Le menu suivant apparaît :

![Menu de création du réseau](https://docs.salome-platform.org/latest/gui/SHAPER/_images/pipeNetworkPanel.png)

Menu de création du réseau de tuyaux

On doit fournir le fichier de type texte qui contient le réseau. Sa syntaxe est décrite plus bas.

## Syntaxe du fichier de données

### Règles générales

- Chaque ligne commençant par # est ignorée
- Une information par ligne
- Sur une ligne, les données sont séparés par des blancs
- Les données sont regroupées en 3 sections : les noeuds, la connectivité, les raccordements
- Une section débute par **mot-clé section**

### Les noeuds

- Repérage avec **nodes section**
- Pour un noeud dont on donne les coordonnées en absolu :

`Identifiant du noeud, le signe -, les 3 coordonnées`

- Pour un noeud défini par rapport à un autre :

`Identifiant du noeud, identifiant du noeud de départ, les 3 coordonnées de la translation`

### La connectivité

- Repérage avec **connectivity section**
- Choix de la méthode de description avec **method=par_ligne** ou **method=2par2**
- Pour la méthode en ligne :

Chaque ligne est décrite par la suite de ses noeuds repérés par leurs identifiants :

`Identifiant du noeud n°1, identifiant du noeud n°2, ..., identifiant du dernier noeud`

- Pour la méthode 2 par 2 :

Chaque tronçon est décrit par les 2 noeuds repérés par leurs identifiants :

`Identifiant du noeud n°1 , identifiant du noeud n°2`

### Le raccordement entre tuyaux

- Repérage avec **fillets section**
- Pour chaque noeud à la jonction de 2 tuyaux :

Si la jonction est directe : `Identifiant du noeud, angular_connection`

Si la jonction est courbe : `Identifiant du noeud, radius=xxx` où xxx est le rayon de courbure.

Note

Par défaut, la jonction entre deux tuyaux est directe, sans rayon de courbure. On peut donc se passer de l’information `angular_connection`. Si toutes les jonctions sont directes, on peut se passer totalement de la rubrique **fillets section**.

Note

Une jonction avec un rayon de courbure ne peut avoir lieu que sur un noeud auquel aboutit exactement 2 tuyaux. L’arc de cercle est tracé dans le plan formé par les deux tuyaux. Les deux tuyaux ne doivent donc pas être colinéaires.

### Exemple

```text
# Positions des noeuds :
nodes section
# Le tuyau principal
id_noeud1 - 0 0 0
id_noeud2 - 10 -10 0
id_noeud3 - 15 -15 0
id_noeud4 - 20 -20 0
id_noeud5 - 21 -21 10
id_noeud6 - 30 -21 10
id_noeud7 - 30 -10 10
id_noeud8 - 30 -5 10
id_noeud9 - 30 0 10
# Les deux piquages
id_noeudA id_noeud2 -5 -5 10
id_noeudB id_noeudA 0 5 10
id_noeudC - 30 -10 20
id_noeudD id_noeudC 5 5 5
id_noeudE id_noeudD 5 5 5

# Connectivité :
connectivity section
# Choix entre 2 méthodes=soit 2par2 soit par_ligne
method=par_ligne
id_noeud1 id_noeud2 id_noeud3 id_noeud4 id_noeud5 id_noeud6 id_noeud7 id_noeud8 id_noeud9
id_noeudB id_noeudA id_noeud2
id_noeud7 id_noeudC id_noeudD id_noeudE

# Congés de raccordement :
fillets section
id_noeud2 angular_connection
id_noeud4 radius=1
id_noeud5 angular_connection
id_noeud6 radius=2
```

![Exemple de réseau](https://docs.salome-platform.org/latest/gui/SHAPER/_images/pipeNetworkExemple.png)

Exemple de réseau

[`Téléchargement des données de cet exemple`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/e5ef076a4afed3db94b434e78a583888/pipeNetwork_ligne.txt)

Le pilotage en TUI se fait ainsi :

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Exemple de création d'un objet SHAPER tuyauterie à partir d'une description dans un fichier txte

Copyright 2022 EDF
"""

__revision__ = "V02.01"

#=================================================================================
# theFile = fichier texte de la description du réseau
theFile = "/home/D68518/pipeNetwork_ligne.txt"
#=================================================================================

import salome
salome.standalone()
salome.salome_init()

from ModelAPI import *

aSession = ModelAPI_Session.get()

# Création de la part pour accueillir le réseau
aSession.startOperation("Create part for pipe network")
aPartFeature = aSession.moduleDocument().addFeature("Part")
aSession.finishOperation()
aPart = aSession.activeDocument()

# Importation et traitement du fichier
aSession.startOperation("Import file")
aFeatureKind = "pipeNetwork"
anImportFeature = aPart.addFeature(aFeatureKind)
aFieldName = "file_path"
aFile = anImportFeature.string(aFieldName)
aFile.setValue(theFile)
aSession.finishOperation()

if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
```

[`Téléchargement du pilotage en TUI`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/a9b8ef8526ac952bfdb8eb4dc98c2947/pipeNetwork.py)
