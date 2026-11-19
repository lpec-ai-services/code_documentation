<!-- source: https://docs.salome-platform.org/latest/gui/HOMARD/en/tutorials.html -->

# Examples

One will find here the instructions python for some characteristic configurations. The associated data files are downloadable. It is necessary to think of adapting the value of the variable `data_dir`: it is the directory in which the files med will have been recorded.
It is in the directory `dircase` that the files will be written resulting from the successive adaptations. This directory is created by default in `/tmp`.

## Loading of the module HOMARD

The loading of the module HOMARD is done in a way similar to the other modules.

> ```python
> import HOMARD
> homard = salome.lcc.FindOrLoadComponent('FactoryServer','HOMARD')
> homard.UpdateStudy()
> ```

To use the module HOMARD within a distributed scheme YACS, the loading is made as follows:

> ```python
> import HOMARD
> my_container.load_component_Library('HOMARD')
> homard = my_container.create_component_instance('HOMARD',0)
> homard.UpdateStudy()
> ```

## Uniform refinement

One will make here three successive uniform refinements of the mesh contained in the file `tutorial_1.00.med`. Some notes:
:   - the same hypothesis is used with each iteration
    - the produced mesh always bears the same name. That does not pose a problem because it is stored in different files.

```python
#
# Hypotheses
# ==========
l_hypothese = homard.CreateHypothesis('hypo_1')
l_hypothese.SetUnifRefinUnRef(1)
#
# Cas
# ===
le_cas = homard.CreateCase('Case_1', 'MAILL', os.path.join(DATA_TUTORIAL, "tutorial_1.00.med"))
le_cas.SetDirName(DIRCASE)
#
# Iterations
# ==========
# Iteration "iter_1_1"
iter_1_1 = le_cas.NextIteration('iter_1_1')
iter_1_1.SetMeshName('MESH')
iter_1_1.SetMeshFile(os.path.join(DIRCASE, "maill.01.med"))
iter_1_1.AssociateHypo('hypo_1')
erreur = iter_1_1.Compute(1, 2)

# Iteration "iter_1_2"
iter_1_2 = iter_1_1.NextIteration('iter_1_2')
iter_1_2.SetMeshName('MESH')
iter_1_2.SetMeshFile(os.path.join(DIRCASE, "maill.02.med"))
iter_1_2.AssociateHypo('hypo_1')
erreur = iter_1_2.Compute(1, 2)

# Iteration "iter_1_3"
iter_1_3 = iter_1_2.NextIteration('iter_1_3')
iter_1_3.SetMeshName('MESH')
iter_1_3.SetMeshFile(os.path.join(DIRCASE, "maill.03.med"))
iter_1_3.AssociateHypo('hypo_1')
erreur = iter_1_3.Compute(1, 2)
#
```

Note

Download the files

- [`initial mesh`](https://docs.salome-platform.org/latest/gui/HOMARD/en/_downloads/427aafdf4942483877e694d39d51ea7e/tutorial_1.00.med)
- [`python script`](https://docs.salome-platform.org/latest/gui/HOMARD/en/_downloads/c84ed40f43568f90bc85e5ce9b112f77/tutorial_1.py)
- [`python script for the creation of the test directory`](https://docs.salome-platform.org/latest/gui/HOMARD/en/_downloads/e4fc571d2017c49bb4e76c5f80012d9b/tutorial_util.py)

## Refinement by zones

One proceeds here to refinement according to zones. To pass from the initial mesh to the mesh ‘M_1’, one uses a box framing the z=1 plane and a sphere centered on the origin with radius 1.05. Then to pass from the mesh ‘M_1’ to the mesh ‘M_2’, one replaces the sphere by a box framing the cube on side 0.5, pointing on the origin and the meshes in the very first zone are unrefined.

```python
#
# Creation des zones
# ==================
# Box "Zone_0"
Zone_0 = homard.CreateZoneBox ('Zone_0', -0.1, 1.1, -0.1, 1.1, 0.9, 1.1)
#
# Sphere "Zone_1"
Zone_1 = homard.CreateZoneSphere ('Zone_1', 0., 0., 0., 1.05)
#
# Box "Zone_2"
Zone_2 = homard.CreateZoneBox ('Zone_2', -0.1, 0.51, -0.1, 0.51, -0.1, 0.51)
#
# Hypothese "hypo_2"
# ==================
l_hypothese = homard.CreateHypothesis('hypo_2')
l_hypothese.AddZone('Zone_1', 1)
l_hypothese.AddZone('Zone_0', 1)
#
# Hypothese "hypo_2_bis"
# ======================
l_hypothese_bis = homard.CreateHypothesis('hypo_2_bis')
l_hypothese_bis.AddZone('Zone_0', -1)
l_hypothese_bis.AddZone('Zone_2', 1)
#
# Cas
# ===
le_cas = homard.CreateCase('Case_2', 'MZERO', os.path.join(DATA_TUTORIAL, "tutorial_2.00.med"))
le_cas.SetDirName(DIRCASE)
#
# Iteration "iter_2_1"
# ====================
iter_2_1 = le_cas.NextIteration('iter_2_1')
iter_2_1.SetMeshName('M_1')
iter_2_1.SetMeshFile(os.path.join(DIRCASE, "maill.01.med"))
iter_2_1.AssociateHypo('hypo_2')
erreur = iter_2_1.Compute(1, 2)
#
# Iteration "iter_2_2"
# ====================
iter_2_2 = iter_2_1.NextIteration('iter_2_2')
iter_2_2.SetMeshName('M_2')
iter_2_2.SetMeshFile(os.path.join(DIRCASE, "maill.02.med"))
iter_2_2.AssociateHypo('hypo_2_bis')
erreur = iter_2_2.Compute(1, 2)
#
```

Note

Download the files

- [`initial mesh`](https://docs.salome-platform.org/latest/gui/HOMARD/en/_downloads/0d0a799f67b0513cad9efc3a80dd3a36/tutorial_2.00.med)
- [`python script`](https://docs.salome-platform.org/latest/gui/HOMARD/en/_downloads/944579f29a55ed4b2c1c46556066237a/tutorial_2.py)
- [`python script for the creation of the test directory`](https://docs.salome-platform.org/latest/gui/HOMARD/en/_downloads/e4fc571d2017c49bb4e76c5f80012d9b/tutorial_util.py)

## Refinement driven by a field

One proceeds here to refinement according to a field. The hypotheses are used to define the name of the field and the thresholds of refinement/unrefinement. The input of the file and the instants is made in the iteration. Fields on the nodes or the elements are interpolated.
To adapt the H_1 mesh resulting from the Iter_1 iteration, two alternatives are applied. In the first, Iter_2, the field is a scalar field of indicators of error and one cuts out the 1.5% of elements where the error is largest. In the second alternative, Iter_2_bis, one is based on a vector field and one examines the jump of this vector between an element and its neighbors: one will cut out where the infinite standard of this jump is higher than the absolute threshold of 0.0001.

```python
#
# Hypothese "hypo_0vers1"
# =======================
hypo_0vers1 = homard.CreateHypothesis('hypo_0vers1')
# Characterization of the field
hypo_0vers1.SetField('SOLU_0__QIRE_ELEM_SIGM__________')
hypo_0vers1.SetUseComp(0)
hypo_0vers1.AddComp('ERREST          ')
hypo_0vers1.SetRefinThr(3, 1.0)
hypo_0vers1.SetTypeFieldInterp(2)
hypo_0vers1.AddFieldInterp('SOLU_0__DEPL____________________')
hypo_0vers1.AddFieldInterp('SOLU_0__ERRE_ELEM_SIGM__________')
#
# Hypothese "hypo_1vers2"
# =======================
hypo_1vers2 = homard.CreateHypothesis('hypo_1vers2')
# Characterization of the field
hypo_1vers2.SetField('SOLU_1__QIRE_ELEM_SIGM__________')
hypo_1vers2.SetUseComp(0)
hypo_1vers2.AddComp('ERREST          ')
hypo_1vers2.SetRefinThr(3, 1.5)
hypo_1vers2.SetUnRefThr(3, 6.)
hypo_1vers2.SetTypeFieldInterp(2)
hypo_1vers2.AddFieldInterp('SOLU_1__DEPL____________________')
hypo_1vers2.AddFieldInterp('SOLU_1__QIRE_ELEM_SIGM__________')
#
# Hypothese "hypo_1vers2_bis"
# ===========================
hypo_1vers2_bis = homard.CreateHypothesis('hypo_1vers2_bis')
# Characterization of the field
hypo_1vers2_bis.SetField('SOLU_1__DEPL____________________')
hypo_1vers2_bis.SetUseComp(1)
hypo_1vers2_bis.AddComp('DX')
hypo_1vers2_bis.AddComp('DY')
hypo_1vers2_bis.AddComp('DZ')
hypo_1vers2_bis.SetRefinThr(1, 0.0001)
hypo_1vers2_bis.SetUnRefThr(1, 0.000001)
hypo_1vers2_bis.SetTypeFieldInterp(0)
#
# Cas
# ===
le_cas = homard.CreateCase('Case_3', 'G_0', os.path.join(DATA_TUTORIAL, "tutorial_3.00.med"))
le_cas.SetDirName(DIRCASE)
#
# Iteration "iter_3_1"
# ====================
iter_3_1 = le_cas.NextIteration('iter_3_1')
iter_3_1.SetMeshName('H_1')
iter_3_1.SetMeshFile(os.path.join(DIRCASE, "maill.01.med"))
iter_3_1.SetFieldFile(os.path.join(DATA_TUTORIAL, "tutorial_3.00.med"))
iter_3_1.SetTimeStepRank( 1, 1)
iter_3_1.AssociateHypo('hypo_0vers1')
erreur = iter_3_1.Compute(1, 2)
#
# Iteration "iter_3_2"
# ====================
iter_3_2 = iter_3_1.NextIteration('iter_3_2')
iter_3_2.SetMeshName('H_2')
iter_3_2.SetMeshFile(os.path.join(DIRCASE, "maill.02.med"))
iter_3_2.SetFieldFile(os.path.join(DATA_TUTORIAL, "tutorial_3.01.med"))
iter_3_2.SetTimeStepRank(1, 1)
iter_3_2.AssociateHypo('hypo_1vers2')
erreur = iter_3_2.Compute(1, 2)
#
# Iteration "iter_3_2_bis"
# ========================
iter_3_2_bis = iter_3_1.NextIteration('iter_3_2_bis')
iter_3_2_bis.SetMeshName('H_2_bis')
iter_3_2_bis.SetMeshFile(os.path.join(DIRCASE, "maill.02.bis.med"))
iter_3_2_bis.SetFieldFile(os.path.join(DATA_TUTORIAL, "tutorial_3.01.med"))
iter_3_2_bis.SetTimeStepRank(1, 1)
iter_3_2_bis.AssociateHypo('hypo_1vers2_bis')
erreur = iter_3_2_bis.Compute(1, 2)
#
```

Note

Download the files

- [`mesh and field stage 0`](https://docs.salome-platform.org/latest/gui/HOMARD/en/_downloads/829f1788bee0e20ef0cc7d5cf4c29346/tutorial_3.00.med)
- [`mesh and field stage 1`](https://docs.salome-platform.org/latest/gui/HOMARD/en/_downloads/20f3b35d9111d46babb6181c531e3b59/tutorial_3.01.med)
- [`python script`](https://docs.salome-platform.org/latest/gui/HOMARD/en/_downloads/72b3431903ca84cacd4dd0db7fc53a7d/tutorial_3.py)
- [`python script for the creation of the test directory`](https://docs.salome-platform.org/latest/gui/HOMARD/en/_downloads/e4fc571d2017c49bb4e76c5f80012d9b/tutorial_util.py)

## Non plane boundaries

One tests the follow-up of the curved borders here, giving the representation of the domain by its CAO. That CAO is given in a XAO format file.
The driving of refinement is the following: uniform refinement of all the elements contained in indicated groups. One starts by refining the inner faces with the pipes; then, one refines continuation twice the external faces with the pipes.
Scheme YACS carrying out this adaptation is downloadable.

```python
#
# Frontières
# ==========
boun_4 = homard.CreateBoundaryCAO("PIQUAGE", os.path.join(DATA_TUTORIAL, "tutorial_4.xao"))
#
# Cas
# ===
le_cas = homard.CreateCase('Case_4', "PIQUAGE", os.path.join(DATA_TUTORIAL, "tutorial_4.00.med"))
le_cas.SetDirName(DIRCASE)
le_cas.AddBoundary( "PIQUAGE" )
#
# Hypotheses
# ==========
# Creation of the hypothesis hypo_4
l_hypothese = homard.CreateHypothesis('hypo_4')
l_hypothese.SetUnifRefinUnRef(1)
l_hypothese.AddGroup('T1_INT_I')
l_hypothese.AddGroup('T1_INT_O')
l_hypothese.AddGroup('T2_INT')
# Creation of the hypothesis hypo_4_bis
l_hypothese_bis = homard.CreateHypothesis('hypo_4_bis')
l_hypothese_bis.SetUnifRefinUnRef(1)
l_hypothese_bis.AddGroup('T1_EXT_I')
l_hypothese_bis.AddGroup('T1_EXT_O')
l_hypothese_bis.AddGroup('T2_EXT')
#
# Iterations
# ==========
# Iteration iter_4_1 : raffinement selon les faces internes
iter_4_1 = le_cas.NextIteration('iter_4_1')
iter_4_1.SetMeshName('PIQUAGE_1')
iter_4_1.SetMeshFile(os.path.join(DIRCASE, "maill.01.med"))
iter_4_1.AssociateHypo('hypo_4')
erreur = iter_4_1.Compute(1, 2)
# Iteration iter_4_2 : raffinement selon les faces externes
iter_4_2 = iter_4_1.NextIteration('iter_4_2')
iter_4_2.SetMeshName('PIQUAGE_2')
iter_4_2.SetMeshFile(os.path.join(DIRCASE, "maill.02.med"))
iter_4_2.AssociateHypo('hypo_4_bis')
erreur = iter_4_2.Compute(1, 2)
# Iteration iter_4_3 : second raffinement selon les faces externes
iter_4_3 = iter_4_2.NextIteration('iter_4_3')
iter_4_3.SetMeshName('PIQUAGE_3')
iter_4_3.SetMeshFile(os.path.join(DIRCASE, "maill.03.med"))
iter_4_3.AssociateHypo('hypo_4_bis')
erreur = iter_4_3.Compute(1, 2)
#
```

Note

Téléchargement des fichiers

- [`initial mesh`](https://docs.salome-platform.org/latest/gui/HOMARD/en/_downloads/c15d5f658cdd7bc6f77349e562d0c74c/tutorial_4.00.med)
- [`CAO`](https://docs.salome-platform.org/latest/gui/HOMARD/en/_downloads/3ad21fdd14c2f5c78145f4b9ce873840/tutorial_4.xao)
- [`python scrip`](https://docs.salome-platform.org/latest/gui/HOMARD/en/_downloads/7dd3fb133845b49e9ca21fac1996261d/tutorial_4.py)
- [`python script for the creation of the test directory`](https://docs.salome-platform.org/latest/gui/HOMARD/en/_downloads/e4fc571d2017c49bb4e76c5f80012d9b/tutorial_util.py)
- [`YACS scheme`](https://docs.salome-platform.org/latest/gui/HOMARD/en/_downloads/66b8adca356e30124744e13a759d2162/tutorial_4.xml)

If the CAO is not available, the boundaries can be approximated: analytical borders to describe various surfaces of the pipes and a discrete border to describe the intersecting lines of the two pipes. Only the definition of the boundaries has to be modified.

```python
#
# Frontières
# ==========
boun_6_1 = homard.CreateBoundaryDi('intersection', 'COURBES', os.path.join(DATA_TUTORIAL, "tutorial_6.fr.med"))
#
boun_6_2 = homard.CreateBoundaryCylinder('cyl_1_ext', 0.0, 25., -25., 25., 50., 75., 100.)
#
boun_6_3 = homard.CreateBoundaryCylinder('cyl_2_ext', 17.5, -2.5, -12.5, -100., -75., -25., 50.)
#
boun_6_4 = homard.CreateBoundaryCylinder('cyl_1_int', 0.0, 25., -25., 25., 50., 75., 75.)
#
boun_6_5 = homard.CreateBoundaryCylinder('cyl_2_int', 17.5, -2.5, -12.5, -100., -75., -25., 25.)
#
# Cas
# ===
le_cas = homard.CreateCase('Case_6', 'PIQUAGE', os.path.join(DATA_TUTORIAL, "tutorial_4.00.med"))
le_cas.SetDirName(DIRCASE)
le_cas.AddBoundary( 'intersection' )
le_cas.AddBoundaryGroup( 'cyl_1_int', 'T1_INT_I' )
le_cas.AddBoundaryGroup( 'cyl_1_ext', 'T1_EXT_I' )
le_cas.AddBoundaryGroup( 'cyl_1_int', 'T1_INT_O' )
le_cas.AddBoundaryGroup( 'cyl_1_ext', 'T1_EXT_O' )
le_cas.AddBoundaryGroup( 'cyl_2_int', 'T2_INT' )
le_cas.AddBoundaryGroup( 'cyl_2_ext', 'T2_EXT' )
#
```

Note

Download the files

- [`initial mesh`](https://docs.salome-platform.org/latest/gui/HOMARD/en/_downloads/c15d5f658cdd7bc6f77349e562d0c74c/tutorial_4.00.med)
- [`mesh of the discrete boundary`](https://docs.salome-platform.org/latest/gui/HOMARD/en/_downloads/06f1f89fd3367990e0dfebaf216e5c52/tutorial_6.fr.med)
- [`python script`](https://docs.salome-platform.org/latest/gui/HOMARD/en/_downloads/c67c8dd9d791652c24eaa441fb58135c/tutorial_6.py)
- [`python script for the creation of the test directory`](https://docs.salome-platform.org/latest/gui/HOMARD/en/_downloads/e4fc571d2017c49bb4e76c5f80012d9b/tutorial_util.py)
- [`YACS scheme`](https://docs.salome-platform.org/latest/gui/HOMARD/en/_downloads/067db222e0a8d168e71230bbb5927fe6/tutorial_6.xml)

## Specific instructions for a 2D mesh

The instructions to adapt a 2D mesh are exactly identical to those necessary to the adaptation of a 3D mesh. The only exception relates to refinement according to geometrical zones: different functions are used to be able to define 2D zones. One gives the 2D coordinates zones, by specifying the orientation of the plane of the mesh.
In the case presented here, one for the first time refines all the elements contained in a bored disk, then in one second iteration, all the elements contained in a rectangle. One will note the use of the follow-up of the circular borders of the field.

```python
#
# Frontière
# =========
# Creation of the discrete boundary boun_5_1
boun_5_1 = homard.CreateBoundaryDi('boun_5_1', 'MAIL_EXT', os.path.join(DATA_TUTORIAL, "tutorial_5.fr.med"))
#
# Creation des zones
# ==================
# Creation of the disk with hole enveloppe
enveloppe = homard.CreateZoneDiskWithHole( 'enveloppe', 0., 0., 250., 193., 1 )
# Creation of the rectangle quart_sup
quart_sup = homard.CreateZoneBox2D( 'quart_sup', 0., 250., 0., 250., 1 )
#
# Hypotheses
# ==========
# Creation of the hypothesis hypo_5
l_hypothese = homard.CreateHypothesis('hypo_5')
l_hypothese.AddZone('enveloppe', 1)
# Creation of the hypothesis l_hypothese_bis
l_hypothese_bis = homard.CreateHypothesis('hypo_5_bis')
l_hypothese_bis.AddZone('quart_sup', 1)
#
# Cas
# ===
le_cas = homard.CreateCase('Case_5', 'COEUR_2D', os.path.join(DATA_TUTORIAL, "tutorial_5.00.med"))
le_cas.SetDirName(DIRCASE)
le_cas.SetConfType(1)
le_cas.AddBoundary('boun_5_1')
#
# Iteration "iter_5_1"
# ====================
iter_5_1 = le_cas.NextIteration('iter_5_1')
iter_5_1.SetMeshName('COEUR_2D_01')
iter_5_1.SetMeshFile(os.path.join(DIRCASE, "maill.01.med"))
iter_5_1.AssociateHypo('hypo_5')
erreur = iter_5_1.Compute(1, 2)
#
# Iteration "iter_5_2"
# ====================
iter_5_2 = iter_5_1.NextIteration('iter_5_2')
iter_5_2.SetMeshName('COEUR_2D_02')
iter_5_2.SetMeshFile(os.path.join(DIRCASE, "maill.02.med"))
iter_5_2.AssociateHypo('hypo_5_bis')
erreur = iter_5_2.Compute(1, 2)
#
```

Note

Download the files

- [`initial mesh`](https://docs.salome-platform.org/latest/gui/HOMARD/en/_downloads/a30171aba996b8c91b2fd1f8c7165d4c/tutorial_5.00.med)
- [`mesh of the discrete boundary`](https://docs.salome-platform.org/latest/gui/HOMARD/en/_downloads/d838ec8263e956812ea0bce983cce03f/tutorial_5.fr.med)
- [`python script`](https://docs.salome-platform.org/latest/gui/HOMARD/en/_downloads/718bf8aacd7f0c218e8d5ba091f0837f/tutorial_5.py)
- [`python script for the creation of the test directory`](https://docs.salome-platform.org/latest/gui/HOMARD/en/_downloads/e4fc571d2017c49bb4e76c5f80012d9b/tutorial_util.py)
