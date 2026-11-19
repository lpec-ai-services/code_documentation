<!-- source: https://docs.salome-platform.org/latest/gui/HOMARD/en/tui_create_case.html -->

# The case

The variables are described in [The creation of a case](gui_create_case.md).

## Methods of the class homard

### Creation of a case

|  |
| --- |
|  |
| **CreateCase(case_name, mesh_name, mesh_file)**  Returns an instance of the class `cas` after its creation   - `case_name`: the name of the case - `mesh_name`: the name of the initial mesh - `mesh_file`: the name of the MED file of this mesh  Default:  - the directory for the results is `/tmp` - the adaptation is conformal |
| **GetCase(case_name)**  Returns an instance of the class `cas` known by its name   - `case_name`: the name of the case |
| **GetAllCasesName()**  Returns the liste of the name of all the existing cases |

### Creation of a case by pursuit of a computed iteration

|  |
| --- |
|  |
| **CreateCaseFromIteration(case_name, dir_name)**  Returns an instance of the class `cas` after its creation   - `case_name`: the name of the case - `dir_name`: the name of the directory that contains   the iteration |
| **CreateCaseFromCaseLastIteration(case_name, dir_name)**  Returns an instance of the class `cas` after its creation   - `case_name`: the name of the case - `dir_name`: the name of the directory that contains   the case |
| **CreateCaseFromCaseIteration(case_name, dir_name, number)**  Returns an instance of the class `cas` after its creation   - `case_name`: the name of the case - `dir_name`: the name of the directory that contains   the case - `number`: the number of the iteration of the case |

## Methods of the class cas

|  |
| --- |
|  |
| **GetName()**  Returns the name of the case |
| **SetDirName(dirname)**  Gives a directory for the results of the case. It can be done only after the creation of the case and before the first computation.   - `dirname`: the name of the directory of the results |
| **GetDirName()**  Returns the name of the directory of the results of the case |
| **SetConfType(conf_type)**  Defines the type of conformity for the case   - `conf_type`: integer as follows:  - 0: conformal (default)   - 1: non conformal with at max 2 cut edges per element   - 2: non conformal with one hanging node per edge of     element   - 3: non conformal without any constraint   - -1: conformal with boxes (no staircases)   - -2: non-conformal with boxes (no staircases) |
| **GetConfType()**  Returns the type of conformity |
| **SetExtType(ext_type)**  Defines the external type for the case   - `ext_type` : integer as follows:  - 0 : Standard MED (default)   - 1 : Saturne MED   - 2 : Saturne 2D MED |
| **GetExtType()**  Returns the external type for the case |
| **GetIter0()**  Returns the iteration linked to the initial mesh. This iteration is automatically created by the module HOMARD. It is used to connect the iterations. It is connected to an initial mesh or to the iteration of a previous case. |
| **AddBoundary(boundary)**  Add a boundary to the definition of a case   - `boundary`: name of the curved boundary |
| **AddBoundaryGroup(boundary, group)**  Add a boundary to the definition of a case   - `boundary`: name of the curved boundary   Discrete boundary:  . if all the curved lines are involved, the second argument is an empty string. . if only some curved lines are involved, `group` is the name of the group of segments  Analytical boundary:   - `group`: name of the group of faces located on the   boundary |
| **Delete(option)**  Deletes the case and all the connected iterations. The MED file of the first mesh is kept.   - `option`: an integer to define what to do with the   MED file of the associated meshes  - 0: the files are kept   - 1: the files are removed   Returns an integer:  - 0: the destruction is done - other value: problem |
| **GetState()**  Returns the state of the case:  - 0: corresponds to an initial mesh - other value: pursuit of an iteration with number n |
| **WriteYACSSchema(ScriptFile, DirName, MeshFile)**  Writes a schema YACS relative to the case.   - `ScriptFile` : name of the file that contains the   script to launch the computation - `DirName` : the directory for the computation - `MeshFile` : name of the file that contains the mesh   for the very first computation |

## Advanced options

|  |
| --- |
|  |
| **SetPyram(option)**  Defines the status of the pyramids in this case   - `option`: integer that defines the status of the   pyramids that could belongs to the initial mesh  - 0: rejected pyramids (default)   - 1: authorized pyramids |
| **GetPyram()**  Returns the status of the pyramids in this case |

## Informations for the initial mesh

|  |
| --- |
|  |
| **MeshInfo(Qual, Diam, Conn, Tail, Inte)**  Gives information about the current mesh. For every option, the choice #0 corresponds to ‘no action’, while the choice #1 launches the option.   - `Qual`: quality of the elements - `Diam`: diametre of the elements - `Conn`: connexity of the domain; a single block, how   many holes, etc. - `Tail`: size of the parts of the domain, group by   group - `Inte`: staggered elements, by dimension |

## Example

The creation of the object case_1 is done as follows:

```python
case_name = "CAS_1"
mesh_name = "MAILL"
mesh_file = "/scratch/Salome/Adapt/m0.med"
case_1 = homard.CreateCase(case_name, mesh_name, mesh_file)
dirname = "/scratch/Salome/Adapt/resu"
case_1.SetDirName(dirname)
case_1.SetConfType(1)
case_1.AddBoundaryGroup( 'intersection', '' )
case_1.AddBoundaryGroup( 'cyl_1', 'T1_EXT' )
case_1.AddBoundaryGroup( 'cyl_1', 'T2_EXT' )
case_1.AddBoundaryGroup( 'cyl_2', 'T_INT' )
```

## Similar graphical input

Look at [The creation of a case](gui_create_case.md)
