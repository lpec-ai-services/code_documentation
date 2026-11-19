<!-- source: https://docs.salome-platform.org/latest/gui/SMESH/tui_adaptation.html -->

# Adaptation

## HOMARD

```python
import inspect
import os
import os.path as osp
import shutil
import tempfile

import salome
salome.salome_init_without_session()

from salome.smesh import smeshBuilder
import SMESHHOMARD

smesh = smeshBuilder.New()

data_dir = osp.abspath(osp.join(osp.dirname(inspect.getfile(lambda: None)), 'data'))
working_dir = tempfile.mkdtemp()

input_med_1 = osp.join(data_dir, "tutorial_4.00.med")
input_xao_1 = osp.join(data_dir, "tutorial_4.xao")
output_med_1 = osp.join(working_dir, "tutorial_4.00_Uniform_R.med")
log_file_1 = osp.join(working_dir, "tutorial_4.00_Uniform_R.log")

# Case 1: input: med file
#         output: med file, log file, published mesh
if osp.isfile(output_med_1):
  os.remove(output_med_1)
if osp.isfile(log_file_1):
  os.remove(log_file_1)

cao_name = "CAO_PIQUAGE"
smeshhomard = smesh.Adaptation("Uniform")
smeshhomard.CreateBoundaryCAO(cao_name, input_xao_1)
smeshhomard.CreateCase("PIQUAGE", input_med_1, working_dir)
smeshhomard.AddBoundary(cao_name)
smeshhomard.SetConfType(0)
smeshhomard.SetKeepMedOUT(True)
smeshhomard.SetPublishMeshOUT(True)
smeshhomard.SetMeshNameOUT("PIQUAGE_Uniform_R_01")
smeshhomard.SetMeshFileOUT(output_med_1)
smeshhomard.SetKeepWorkingFiles(False)
smeshhomard.SetLogInFile(True)
smeshhomard.SetLogFile(log_file_1)
smeshhomard.SetRemoveLogOnSuccess(False)
smeshhomard.SetVerboseLevel(3)
if smeshhomard.Compute() != 0: raise Exception("Error when computing Mesh")

if osp.isfile(output_med_1):
  os.remove(output_med_1)
else:
  print("Test Uniform refinement Case 1: Error: no output med file")
  assert(False)

if osp.isfile(log_file_1):
  os.remove(log_file_1)
else:
  print("Test Uniform refinement Case 1: Error: no log file")
  assert(False)

# Case 2: input: mesh, boundaries
#         output: published mesh
input_med_2 = osp.join(data_dir, "tutorial_5.00.med")
input_fr    = osp.join(data_dir, "tutorial_5.fr.med")
output_med_2 = osp.join(working_dir, "tutorial_5.00_Uniform_R.med")
log_file_2 = osp.join(working_dir, "tutorial_5.00_Uniform_R.log")

if osp.isfile(output_med_2):
  os.remove(output_med_2)
if osp.isfile(log_file_2):
  os.remove(log_file_2)

# prepare input mesh
([MAILL], status) = smesh.CreateMeshesFromMED( input_med_2 )

smeshhomard = smesh.Adaptation("Uniform")
smeshhomard.CreateBoundaryDi("Boun_5_1", "MAIL_EXT", input_fr)
smeshhomard.CreateCaseOnMesh("COEUR_2D", MAILL.GetMesh(), working_dir)
smeshhomard.AddBoundary("Boun_5_1")
smeshhomard.SetConfType(1)
smeshhomard.SetKeepMedOUT(False)
smeshhomard.SetPublishMeshOUT(True)
smeshhomard.SetMeshNameOUT("COEUR_2D_Uniform_R")
smeshhomard.SetMeshFileOUT(output_med_2)
smeshhomard.SetKeepWorkingFiles(False)
smeshhomard.SetLogInFile(True)
smeshhomard.SetLogFile(log_file_2)
smeshhomard.SetRemoveLogOnSuccess(True)
smeshhomard.SetVerboseLevel(0)
if smeshhomard.Compute() != 0: raise Exception("Error when computing Mesh")

if osp.isfile(output_med_2):
  print("Test Uniform refinement Case 2: Error: output med file has not been removed")
  assert(False)

if osp.isfile(log_file_2):
  print("Test Uniform refinement Case 2: Error: log file has not been removed")
  assert(False)

shutil.rmtree(working_dir)

if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/2c6e5ffbc8133852b718447baaeef4f5/test_uniform_refinement.py)

```python
import inspect
import os
import os.path as osp
import shutil
import tempfile

import salome
salome.salome_init_without_session()

from salome.smesh import smeshBuilder
import SMESHHOMARD

smesh = smeshBuilder.New()

data_dir = osp.abspath(osp.join(osp.dirname(inspect.getfile(lambda: None)), 'data'))
working_dir = tempfile.mkdtemp()

input_med = osp.join (data_dir, "test_homard_adapt.med")
output_med_1 = osp.join (working_dir, "test_1.00_Uniform_R_01.med")
output_med_2 = osp.join (working_dir, "test_1.00_Uniform_R_02.med")
log_file_1 = osp.join (working_dir, "test_1.00_Uniform_R_01.med.log")
log_file_2 = osp.join (working_dir, "test_1.00_Uniform_R_02.med.log")

# Case 1: input: med file
#         output: med file, log file, published mesh
if osp.isfile(output_med_1):
  os.remove(output_med_1)
if osp.isfile(log_file_1):
  os.remove(log_file_1)

smeshhomard = smesh.Adaptation("Uniform")
smeshhomard.CreateCase("MAILL", input_med, working_dir)
smeshhomard.SetConfType(0)
smeshhomard.SetKeepMedOUT(True)
smeshhomard.SetPublishMeshOUT(True)
smeshhomard.SetMeshNameOUT("MAILL_Uniform_R_01")
smeshhomard.SetMeshFileOUT(output_med_1)
smeshhomard.SetKeepWorkingFiles(False)
smeshhomard.SetLogInFile(True)
smeshhomard.SetLogFile(log_file_1)
smeshhomard.SetRemoveLogOnSuccess(False)
smeshhomard.SetVerboseLevel(3)
if smeshhomard.Compute() != 0: raise Exception("Error when computing Mesh")

if osp.isfile(output_med_1):
  os.remove(output_med_1)
else:
  print("Test Uniform refinement Case 1: Error: no output med file")
  assert(False)

if osp.isfile(log_file_1):
  os.remove(log_file_1)
else:
  print("Test Uniform refinement Case 1: Error: no log file")
  assert(False)

# Case 2: input: mesh, boundaries
#         output: published mesh
if osp.isfile(output_med_2):
  os.remove(output_med_2)
if osp.isfile(log_file_2):
  os.remove(log_file_2)

# prepare input mesh
([MAILL], status) = smesh.CreateMeshesFromMED( input_med )

#smeshhomard = smesh.Adaptation("Uniform")
Boun_1 = smeshhomard.CreateBoundaryCylinder("Boun_1", 0.5, 0.5, 0.5, 0, 0, 1, 0.25)
smeshhomard.CreateCaseOnMesh("MAILL", MAILL.GetMesh(), working_dir)
smeshhomard.SetConfType(0)
smeshhomard.AddBoundaryGroup("Boun_1", "BORD_EXT")
smeshhomard.AddBoundaryGroup("Boun_1", "MOITIE1")
smeshhomard.SetKeepMedOUT(False)
smeshhomard.SetPublishMeshOUT(True)
smeshhomard.SetMeshNameOUT("MAILL_Uniform_R_02")
smeshhomard.SetMeshFileOUT(output_med_2)
smeshhomard.SetKeepWorkingFiles(False)
smeshhomard.SetLogInFile(True)
smeshhomard.SetLogFile(log_file_2)
smeshhomard.SetRemoveLogOnSuccess(True)
smeshhomard.SetVerboseLevel(0)
if smeshhomard.Compute() != 0: raise Exception("Error when computing Mesh")

if osp.isfile(output_med_2):
  print("Test Uniform refinement Case 2: Error: output med file has not been removed")
  assert(False)

if osp.isfile(log_file_2):
  print("Test Uniform refinement Case 2: Error: log file has not been removed")
  assert(False)

shutil.rmtree(working_dir)

if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/139b82e07db3a29b13520aad96698a2b/test_homard_adapt.py)

## MG_Adapt

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests des adaptations par MGAdapt en standalone

Copyright 2021 EDF
Gérald NICOLAS
+33.1.78.19.43.52
"""

__revision__ = "V04.04"

#========================= Les imports - Début ===================================

import inspect
import sys
import os
import tempfile
import shutil
import salome

salome.standalone()
salome.salome_init_without_session()

import SMESH
from salome.smesh import smeshBuilder
smesh = smeshBuilder.New()

#========================== Les imports - Fin ====================================

#========================= Paramétrage - Début ===================================
# 1. REPDATA = répertoire du cas
#REPDATA = os.path.abspath(os.path.join(os.path.dirname(inspect.getfile(lambda: None)), 'data'))
REPDATA = os.path.abspath(os.path.join(os.getenv("SMESH_ROOT_DIR"),'share','doc','salome','examples','SMESH', 'data'))
print(REPDATA)
#
# 2. Repérage des données
D_DATA = dict()
D_DATA["01"] = "01" # 2D plan ; carte locale
D_DATA["02"] = "02" # 2D plan ; carte en arrière-plan
D_DATA["03"] = "01" # 2D plan ; taille constante
D_DATA["04"] = "04" # 3D ; carte locale et dernier pas de temps
D_DATA["05"] = "04" # 3D ; carte locale et pas de temps n°1
D_DATA["06"] = "06" # 2D non plan; carte locale
D_DATA["07"] = "07" # 2D plan ; carte locale anisotrope
D_DATA["08"] = "08" # 3D ; carte en arrière-plan anisotrope
D_DATA["10"] = "10" # 2D plan ; carte locale et maillage initial quadratique
D_DATA["11"] = "11" # 2D plan ; carte locale et maillage initial en quadrangles
D_DATA["13"] = "13" # 3D ; carte locale en simple précision et dernier pas de temps
#========================== Paramétrage - Fin ====================================

class MGAdaptTest (object):

  """Test de l'adaptation par MGAdapt

Options facultatives
********************
Le(s) nom du/des tests à passer. Si aucun n'est donné, tous les cas sont passés.
  """

# A. La base

  message_info = ""
  _verbose = 0
  _verbose_max = 0
  affiche_aide_globale = 0

# B. Les variables

  l_cas = None
  rep_test = None
  nro_cas = None
  cas = None

#=========================== Début de la méthode =================================

  def __init__ ( self, liste_option ):

    """Le constructeur de la classe MGAdaptTest"""

    self.l_cas = list()
    self.repout = None

    for option in liste_option :

      #print (option)
      saux = option.upper()
      #print (saux)
      if saux in ( "-H", "-HELP" ):
        self.affiche_aide_globale = 1
      elif saux == "-V" :
        self._verbose = 1
      elif saux == "-VMAX" :
        self._verbose = 1
        self._verbose_max = 1
      else :
        self.l_cas.append(option)

    if not self.l_cas:
      for cle in D_DATA:
        self.l_cas.append(cle)
    self.l_cas.sort()

    if self._verbose_max:
      print ("Liste des cas : {}".format(self.l_cas))

#===========================  Fin de la méthode ==================================

#=========================== Début de la méthode =================================

  def __del__(self):
    """A la suppression de l'instance de classe"""
    if self._verbose_max:
      print ("Suppression de l'instance de la classe.")

#===========================  Fin de la méthode ==================================

#=========================== Début de la méthode =================================

  def _add_file_in (self, objet_adapt):
    """Ajout du fichier med d'entrée

Entrées/Sorties :
  :objet_adapt: l'objet du module
    """
    if self._verbose_max:
      print ("_add_file_in pour {}".format(self.nro_cas))

    ficmed = os.path.join (REPDATA, "test_{}.med".format(D_DATA[self.nro_cas]))
    if self._verbose_max:
      print ("Fichier {}".format(ficmed))
    if not os.path.isfile(ficmed):
      erreur = 1
      message = "Le fichier {} est inconnu.".format(ficmed)
    else:
      objet_adapt.setMEDFileIn(ficmed)
      erreur = 0
      message = ""

    return erreur, message

#===========================  Fin de la méthode ==================================

#=========================== Début de la méthode =================================

  def _add_file_out (self, objet_adapt):
    """Ajout du fichier de sortie

Entrées/Sorties :
  :objet_adapt: l'objet du module
    """
    if self._verbose_max:
      print ("_add_file_out pour {}".format(self.nro_cas))

    if not self.repout:
      self.repout = tempfile.mkdtemp()

    ficmed = os.path.join (self.repout, "test_{}.adapt.tui.med".format(self.nro_cas))
    if os.path.isfile(ficmed):
      os.remove(ficmed)

    objet_adapt.setMEDFileOut(ficmed)

    if self._verbose:
      print (". Maillage adapté dans le fichier {}".format(ficmed))

    return

#===========================  Fin de la méthode ==================================

#=========================== Début de la méthode =================================

  def  _add_file_bkg (self, objet_adapt):
    """Ajout du fichier med de fond

Entrées/Sorties :
  :objet_adapt: l'objet du module
    """
    if self._verbose_max:
      print ("_add_file_bkg pour {}".format(self.nro_cas))

    ficmed = os.path.join (REPDATA, "test_{}_bg.med".format(D_DATA[self.nro_cas]))
    if self._verbose_max:
      print ("Fichier {}".format(ficmed))
    if not os.path.isfile(ficmed):
      erreur = 1
      message = "Le fichier {} est inconnu.".format(ficmed)
    else:
      objet_adapt.setMEDFileBackground(ficmed)
      erreur = 0
      message = ""

    return erreur, message

#===========================  Fin de la méthode ==================================

#=========================== Début de la méthode =================================

  def _hypo_creation (self, maptype, option, niveau=3):
    """Création d'une hypothèse

Entrées :
  :maptype: type de carte : "Local", "Background", "Constant"
  :option: nom du champ si "Local" ou "Background", valeur si "Constant"
  :niveau: niveau de verbosité

Sortie :
  :hypo: l'objet hypothèse
    """
    if self._verbose_max:
      print ("_hypo_creation pour {} avec {}".format(maptype,option))

    erreur = 0
    message = ""

    while not erreur :

      #--- Création de l'hypothèse ---
      hypo = smesh.CreateAdaptationHypothesis()

      # Type de données
      if ( maptype in ("Local", "Background", "Constant") ):
        hypo.setSizeMapType(maptype)
      else:
        message = "Le type de carte {} est inconnu.".format(maptype)
        erreur = 2
        break

      # Valeur
      if ( maptype in ("Local", "Background") ):
        hypo.setSizeMapFieldName(option)
      else:
        hypo.setConstantSize(option)

      # Verbosité
      self._hypo_verbose (hypo, niveau)

      break

    return erreur, message, hypo
#===========================  Fin de la méthode ==================================

#=========================== Début de la méthode =================================

  def _hypo_verbose (self, hypo, niveau=10):
    """Débogage des hypothèses

Entrées :
  :niveau: niveau de verbosité

Entrées/Sorties :
  :hypo: l'objet hypothèse
    """

    hypo.setVerbosityLevel(niveau)

    if self._verbose_max:

      hypo.setPrintLogInFile(True)
      hypo.setKeepWorkingFiles(True)
      hypo.setRemoveOnSuccess(False)

    return
#===========================  Fin de la méthode ==================================

#=========================== Début de la méthode =================================

  def _calcul (self, objet_adapt, hypo):
    """Calcul

Entrées :
  :objet_adapt: l'objet du module
  :hypo: l'objet hypothèse
    """

    #--- association de l'hypothese à l'objet de l'adaptation
    objet_adapt.AddHypothesis(hypo)

    #-- Calcul
    if self._verbose_max:
      print (hypo.getCommandToRun())
    erreur = objet_adapt.Compute(False)
    if erreur:
      message = "Echec dans l'adaptation."
    else:
      message = ""

    return erreur, message

#===========================  Fin de la méthode ==================================

#=========================== Début de la méthode =================================

  def _test_00 (self, objet_adapt):
    """Test générique

Entrées/Sorties :
  :objet_adapt: l'objet du module
    """

    erreur = 0
    message = ""

    while not erreur :

      #--- les fichiers MED ---#
      erreur, message = self._add_file_in (objet_adapt)
      if erreur:
        break
      self._add_file_out (objet_adapt)
      if self.nro_cas in ("02", "08"):
        erreur, message = self._add_file_bkg (objet_adapt)
        if erreur:
          break

      #--- Création de l'hypothèse ---
      if self.nro_cas in ("01", "04", "05", "06", "07", "10", "11", "13"):
        maptype = "Local"
        if self.nro_cas in ("01", "04", "05", "06", "07", "10"):
          option = "TAILLE"
        elif self.nro_cas in ("11",):
          option = "Taille de maille"
        elif self.nro_cas in ("13",):
          option = "Elevation"
      elif self.nro_cas in ("02", "08"):
        maptype = "Background"
        option = "TAILLE"
      elif self.nro_cas in ("03",):
        maptype = "Constant"
        option = 0.5

      if self._verbose:
        niveau = 3
      elif self._verbose_max:
        niveau = 10
      else:
        niveau = 0
      erreur, message, hypo = self._hypo_creation(maptype, option, niveau)
      if erreur:
        break

      #-- Ajout des options
      if self.nro_cas in ("04", "06", "07", "08", "10", "11"):
        hypo.setTimeStepRankLast()
      elif self.nro_cas in ("05",):
        hypo.setTimeStepRank(1,1)
      elif self.nro_cas in ("13",):
        hypo.setTimeStepRank(0,0)

      # options facultatives
      if self.nro_cas in ("03",):
        hypo.setOptionValue("adaptation", "surface")

      #-- Calcul
      try :
        erreur, message = self._calcul (objet_adapt, hypo)
      except :
        erreur = 1871
        message = "Erreur dans le calcul par SMESH"

      break

    return erreur, message

#===========================  Fin de la méthode ==================================

#=========================== Début de la méthode =================================

  def _traitement_cas (self ):
    """Traitement d'un cas

Sorties :
  :erreur: code d'erreur
  :message: message d'erreur
    """

    nom_fonction = __name__ + "/_traitement_cas"
    blabla = "\nDans {} :".format(nom_fonction)

    if self._verbose_max:
      print (blabla)

# 1. Préalables

    erreur = 0
    message = ""
    if self._verbose:
      print ("Passage du cas '{}'".format(self.nro_cas))

    if ( self.nro_cas in ("01", "02", "03", "04", "05", "06", "07", "08", "10" ,"11" ,"13") ):
      objet_adapt = smesh.Adaptation('MG_Adapt')
      erreur, message = self._test_00 (objet_adapt)
      del objet_adapt

    else:
      erreur = 1
      message = "Le cas '{}' est inconnu.".format(self.nro_cas)

    return erreur, message

#===========================  Fin de la méthode ==================================

#=========================== Début de la méthode =================================

  def lancement (self):

    """Lancement

Sorties :
  :erreur: code d'erreur
  :message: message d'erreur
    """

    nom_fonction = __name__ + "/lancement"
    blabla = "\nDans {} :".format(nom_fonction)

    erreur = 0
    message = ""

    if self._verbose_max:
      print (blabla)

    for nom_cas in self.l_cas:
      self.nro_cas = nom_cas
      erreur_t, message_t = self._traitement_cas ()
      if erreur_t:
        erreur += 1
        message += "\nErreur n° {} pour le cas {} :\n".format(erreur_t,nom_cas)
        message += message_t

    if ( erreur and self._verbose_max ):
      print (blabla, message)

    if self.repout:
      shutil.rmtree(self.repout)

    return erreur, message

#===========================  Fin de la méthode ==================================

#==========================  Fin de la classe ====================================

#==================================================================================
# Lancement
#==================================================================================

if __name__ == "__main__" :

# 1. Options

  L_OPTIONS = list()
  #L_OPTIONS.append("-h")
  #L_OPTIONS.append("-v")
  #L_OPTIONS.append("-vmax")
  L_OPTIONS.append("01")
  L_OPTIONS.append("02")
  L_OPTIONS.append("03")
  L_OPTIONS.append("07")
  L_OPTIONS.append("10")
  L_OPTIONS.append("11")
  L_OPTIONS.append("04")
  L_OPTIONS.append("05")
  L_OPTIONS.append("06")
  L_OPTIONS.append("08")
  L_OPTIONS.append("13")

# 2. Lancement de la classe

  #print ("L_OPTIONS :", L_OPTIONS)
  MGADAPT_TEST = MGAdaptTest(L_OPTIONS)
  if MGADAPT_TEST.affiche_aide_globale:
    sys.stdout.write(MGADAPT_TEST.__doc__+"\n")
  else:
    ERREUR, MESSAGE_ERREUR = MGADAPT_TEST.lancement()
    if ERREUR:
      sys.stdout.write(MGADAPT_TEST.__doc__+"\n")
      MESSAGE_ERREUR += "\n {} erreur(s)\n".format(ERREUR)
      sys.stderr.write(MESSAGE_ERREUR)
      #raise Exception(MESSAGE_ERREUR)
      assert(False)

  del MGADAPT_TEST

  #sys.exit(0)
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/e9d676129ab10b6270689d36dc35bb60/MGAdaptTests_without_session.py)

**See Also** the GUI [Adaptation](adaptation.md#adaptation-page).
