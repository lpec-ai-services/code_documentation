<!-- source: https://docs.salome-platform.org/latest/gui/PYHELLO/load_iapp.html -->

# Loading from the GUI (IAPP)

In order to activate PYHELLO module in the SALOME GUI desktop, the user should press the PYHELLO module's button on the "Modules" toolbar or select the name of the module in the combo box on this toolbar.

The image file to be used as an icon of a module should be exported by the module build procedure. The icon file name is defined in the corresponding SalomeApp.xml configuration file:

```python
<section name="PYHELLO">
  <parameter name="name" value="Hello"/>
  <parameter name="icon" value="PYHELLO.png"/>
  <parameter name="library" value="SalomePyQtGUI"/>
</section>
```

[<< Previous](load_lcc.md)
