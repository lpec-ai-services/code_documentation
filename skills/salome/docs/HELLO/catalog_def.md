<!-- source: https://docs.salome-platform.org/latest/gui/HELLO/catalog_def.html -->

# HELLO module catalog definition

In the example from the previous chapter, the HELLO component was loaded by making a direct request to the SALOME container. This is not the standard method for loading of a component. The normal way uses the SALOME LifeCycle service that invokes SALOME Module Catalog services to identify the component and its properties and then calls the requested container to load the component.

Before this method can be used, the component must be declared in a catalog in the XML format, for which the name must be `<MODULE>Catalog.xml`. In our case, it will be `HELLOCatalog.xml`. Usually this catalog is put to the resources sub-directory of the directory tree. The simplest way to create this file is to use Catalog Generator utility provided by the SALOME KERNEL module, that can automatically generate XML description file from the IDL file.

[<< Previous](load_module.md)  
[>> Next](load_lcc.md)
