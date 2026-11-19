<!-- source: https://docs.salome-platform.org/latest/gui/HELLO/load_iapp.html -->

# Loading from the GUI (IAPP)

In order to activate HELLO module in the SALOME GUI desktop, the user should press the HELLO module's button on the *Modules* toolbar or select the name of the module in the combo box on this toolbar.

The image file to be used as an icon of a module should be exported by the module build procedure. The icon file name is defined in `SalomeApp.xml:`

```python
<section name="HELLO">
  <parameter name="name" value="Hello"/>
  <parameter name="icon" value="HELLO.png"/>
</section>
```

[<< Previous](load_lcc.md)
