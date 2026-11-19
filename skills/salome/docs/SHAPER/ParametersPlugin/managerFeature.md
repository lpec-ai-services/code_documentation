<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/ParametersPlugin/managerFeature.html -->

# Parameters manager

To create/edit simultaneously a set of parameters in the active partset or part instead of calling them one by one:

1. select in the Main Menu *Part - > Parameters* item or
2. click ![paper_roll.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/paper_roll.png) **Parameters** button in the toolbar:

The following dialog box with parameter table appears:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/parameters.png)

Parameters dialog box

To edit a parameter, double-click on parameter in object browser.

**Input fields**:

- **Name** defines parameter name. Name follows the naming rules of the python language for variables;
- **Expression** allows manual input of python expression;
- **Result** evaluates expression as real number by python *eval()* function;
- **Comment** contains any text. This field is optional;
- **Add** button adds a new empty string in the end of table. Default **Name** is *<NoName>*, **Expression** is *<NoValue>*
- **Insert** button adds a new empty string before the selected parameter;
- **Delete** button removes the selected parameter from the table;
- **Import** button import parameters from .txt files. Parameters must be written in file in separate lines like example:

  **Name** **Expression** # **Comment**

  Sample.txt

  ‘’Length 36. # Length of the part’’

  ‘’Width 24 # Width of the part’’

  ‘’Height Length * Width’’
- **Modify parameter position** button moves the selected parameter

  ![param_up](https://docs.salome-platform.org/latest/gui/SHAPER/_images/parameters_up.png) one line up in the table,

  ![param_down](https://docs.salome-platform.org/latest/gui/SHAPER/_images/parameters_down.png) one line down in the table.

**TUI Command**:

model.importParameters(*Part_doc*, *filename*)
:   Parameters:
    :   - **part** – The current part object
        - **filename** – The txt file with parameters

    Returns:
    :   Created objects.

**See Also** a sample TUI Script of a [Create Parameter](TUI_parameterFeature.md#tui-parameterfeature) operation.
**See Also** [Create parameter](parameterFeature.md#parameter) operation.
