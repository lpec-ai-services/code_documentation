<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/ExchangePlugin/importFeature.html -->

# Import

The Import feature allows importing an external file into the current study.

## Import PartSet

To open a study previously saved in SHAPER native format, select in the Main Menu *File -> Import -> Part Set…* item.
The current study will be closed, so the action dialog will be opened to choose whether the changes should be saved.
After that the following open file dialog will be opened:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/ImportPartFileDlg.png)

**Dialog box to open SHAPER native file**

Select file and press **Open** button to load the file. **Cancel** button cancels the operation.

## Import Part

To import the previously stored file in the current part, select in the Main Menu *File -> Import -> Part…* item.

The following property panel will be opened:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/ImportPart_panel.png)

**Import Part property panel**

In this panel it is possible to enter a file name directly or press **‘…’** button and browse it with help of import file dialog box:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/ImportPartFileDlg.png)

**Dialog box to import Part**

The import will be performed within the active part. If no part is active, the possible targets to import will be proposed in **Import to** combobox, which contains the list of existing parts, PartSet or a new part creation option.

**Apply** button imports the file.

**Cancel** button cancels the operation.

**TUI Command**:

model.importPart(*Part_doc*, *FileNameString*[, *PrevFeature*])
:   Parameters:
    :   - **Part_doc** – The target part document, where to import the data
        - **string** – The file name string
        - **reference** – The feature after which the imported entities should be inserted

## Import from CAD formats

It is possible to import files in the following CAD-neutral formats: BREP, STEP, IGES, XAO, STL.
To import a file into active part select in the Main Menu *File -> Import -> From CAD format…* item.

The following property panel will be opened:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Import_panel.png)

**Import property panel**

The first combobox provides the list of formats avalables (BREP, XAO, IGES or STEP).
The **Import to** combobox provides the list of destinations (one of existing Parts or a new Part).

In this panel it is possible to enter a file name directly or press **‘…’** button and browse it with help of import file dialog box:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/OpenFileDlg.png)

**Dialog box to import CAD-neutral format**

### Import BREP, XAO, IGES

In case of first choice the format of imported file will be defined according to file extension.

**Apply** button imports the file.

**Cancel** button cancels the operation.

**TUI Command**:

model.addImport(*Part_doc*, *FileNameString*)
:   Parameters:
    :   - **Part_doc** – The target part document, where to import the data
        - **string** – A file name string.

model.addImportXAOMem(*Part_doc*, *aBuffer*)
:   This function allows importing data in XAO format from GEOM through a memory buffer (bytes array), without creation of real file on disk.

    Parameters:
    :   - **Part_doc** – The target part document, where to import the data
        - **aBuffer** – A byte array with data in XAO format.

### Result

The Result of the operation depends on the imported file content.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/FileImported.png)

Import of BREP file.

**See Also** a sample TUI Script of [Import File](TUI_importFeature.md#tui-import-file) operation.

### Import STEP

In this case, the following property panel will be opened:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/ImportSTEP.png)

**Dialog box to import file in STEP format**

The file name and path can be defined in **Import file** field by direct input or browsing with ‘…’ button, which opens **Import file** dialog box.
The **Import to** combobox provides the list of destinations (one of existing Parts or a new Part).
**STEP options** provide the possibility to **Scale to International System Units** as well as to create groups from **Materials** and/or **Colors** if defined in assemblies of the file to import.

**Apply** button imports the file.

**Cancel** button cancels the operation.

**TUI Command**:

model.addImportSTEP(*Part_doc*, *FileNameString*, *scalInterUnits*, *materials*, *colors*)
:   Parameters:
    :   - **Part_doc** – The target part document, where to import the data
        - **string** – A file name string.
        - **boolean** – True if scale to UIS
        - **boolean** – True to create groups from materials
        - **boolean** – True to create groups from colors

### Result

The Result of the operation depends on the imported file content.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/FileImportedSTEP.png)

Import of STEP file.

**See Also** a sample TUI Script of [Import STEP File](TUI_importFeature.md#tui-import-file-step) operation.

### Import pictures

It is possible to import pictures in the following image formats: GIF, TIFF, PNG, JPG, JPEG, BMP, PPM, JPE.
To import a file into active part select in the Main Menu *File -> Import -> Picture…* item.

### Result

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/imageImported.png)

Import of PNG image file.

**See Also** a sample TUI Script of [Import File](TUI_importFeature.md#tui-import-file) operation.
