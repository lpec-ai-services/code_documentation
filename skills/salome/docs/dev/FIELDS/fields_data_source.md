<!-- source: https://docs.salome-platform.org/latest/dev/FIELDS/fields_data_source.html -->

# Data Source

Data Source for all presentations of Fields module is a MED file. To add Data Source into Fields module, choose
**File > Add Data Source** menu (or click **Add Data Source** [![img](https://docs.salome-platform.org/latest/dev/FIELDS/_images/image_datasource_add.png)](https://docs.salome-platform.org/latest/dev/FIELDS/_images/image_datasource_add.png) button in the *Datasource* toolbar).
This shows a standard dialog that allows browsing and choosing *.med files:

![figure](https://docs.salome-platform.org/latest/dev/FIELDS/_images/image_file_search.png)

Select a file and confirm your choice by pressing **Open** button.
As a result, Data Source representation appears in **Object Browser**:

![figure](https://docs.salome-platform.org/latest/dev/FIELDS/_images/image_data_source_representation.png)

It contains the following information:

- A path to the MED file (root Data Source item),
- A list of the meshes present in the Data Source,
- For each Mesh item - a list of the fields plus **Mesh view** presentation item.

Also, [Mesh presentation](fields_mesh_presentation.md#fields-mesh-presentation-page) is displayed in 3D Viewer.
