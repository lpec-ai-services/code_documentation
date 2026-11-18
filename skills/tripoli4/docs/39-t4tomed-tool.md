# T4TOMED TOOL
<!-- source PDF pages 441-443 -->

<!-- page 441 -->
Chapter 39
T4TOMED TOOL
T4toMED is a tool to create a MED format file from one or several T4G input files.
More information on MED format is available on the SALOME Platform website at the following URL:
http://www.salome-platform.org/user-section/about/med.

## 39.1 STARTING WITH T4TOMED

### 39.1.1 HOW TO LAUNCH T4TOMED

In order to translate several *.general T4G input files, a file suffixed by .all must be created as input file
for T4toMED containing the list of T4G input files:
name
<datafile_1>.general
name
<datafile_2>.general
...
The syntax to run T4toMED with this data is the following:
static_medtripoli4 <listfile>.all
If a single T4G input file has to be translated, it is possible to use it as an input file for T4toMED:
static_medtripoli4 <T4Gfile>.general
The created file name is by default <listfile>.all.med or <T4Gfile>.general.med in the case of a
single T4G input file.

### 39.1.2 T4TOMED OPTIONS

When using a .all input file listing several *.general T4G input files, a mesh is created for each file with
the following parameters by default:

<!-- page 442 -->
• Mesh name: Mesh_<n>
• Field name: Field_<n>
with n the incremented index. It is possible to group several *.general files in a single mesh. In this case,
the mesh option allows the user to specify the common mesh name. As there is no check on the identity of
meshes with the same name, it is the user’s responsibility to ensure that the meshes with a common name are
the same.
The field option allows the user to specify the field name corresponding to a .general file. As there is no
check on the uniqueness of field names, it is the users’s responsibility to ensure that a field name is not used
more than once.
Example:
name
<datafile_1>.general
mesh:MyMesh field:Score
name
<datafile_2>.general
name
<datafile_3>.general
mesh:MyMesh field:Sigma
The limit size for the mesh and field names is MED_TAILLE_NOM i.e. 32 characters.

### 39.1.3 PARTICULAR DATA

Until version 9 of TRIPOLI-4, data about the frame type (CARTESIAN or TRIANGLEZ), origin and defining
vectors are not specified in T4G input files. These data are now available for meshes defined with
EXTENDED_MESH and are written as comments in the T4G input file. Example:
header = marker "Data\n"
format = ascii
field = importance
structure = scalar
type = float
dependency = connections
grid = 19 x 21 x 21
majority = column
positions = regular, regular, regular, 9.9, 5.1, -50.1, 5.1, -50.1, 5.1
end
#frame_type = TRIANGLEZ
#origine = 0, 0, 0
#vectors = 1, 0, 0, -0.45, 0.8, 0, 0, 0, 1
Data
12.0587
...
When these data are missing from the .general file, the frame parameters set by default are:
• frame_type: CARTESIAN

<!-- page 443 -->
• origine: 0, 0, 0
• vectors: 1, 0, 0, 0, 1, 0, 0, 0, 1
It is then possible to add these data manually, to describe for instance a triangular mesh when using
EXTENDED_MESH.
