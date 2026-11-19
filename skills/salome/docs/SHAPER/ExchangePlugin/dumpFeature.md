<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/ExchangePlugin/dumpFeature.html -->

# Dump

The Dump feature allows exporting a current study to a Python script which dumps the study creation process as a sequence of Python commands.

It is possible to dump the current study state into a Python script. To dump a study:

1. select in the Main Menu *Part - > Dump* item or
2. click ![dump.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/dump.png) **Dump** button in the toolbar.

The following property panel will be opened:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Dump_panel.png)

**Dump property panel**

In this panel it is necessary to enter a file name directly or press **‘…’** button and browse it with help of dump file dialog box:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/DumpFileDlg.png)

**Dump file dialog box**

**Apply** button writes the dump file.

**Cancel** button cancels the operation.

**TUI Command**: Is not supported.

## Result

The Result of the operation is a Python file.
