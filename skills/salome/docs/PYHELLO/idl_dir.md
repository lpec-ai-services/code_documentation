<!-- source: https://docs.salome-platform.org/latest/gui/PYHELLO/idl_dir.html -->

# The idl directory

The `idl` directory requires a `CMakeLists.txt` that must make the compilation of the CORBA IDL `PYHELLO_Gen.idl` file and install all the generated files into the correct module installation directories. This is done by using `OMNIORB_ADD_MODULE()` CMake macro:

```python
OMNIORB_ADD_MODULE(SalomeIDLPYHELLO PYHELLO_Gen.idl ${KERNEL_ROOT_DIR}/idl/salome ${KERNEL_SalomeIDLKernel})
INSTALL(TARGETS SalomeIDLPYHELLO EXPORT ${PROJECT_NAME}TargetGroup DESTINATION ${SALOME_INSTALL_LIBS})
```

The idl file itself must define a CORBA module for which the name must be different from the module name to avoid name conflicts and define a CORBA interface that is derived at least from the EngineComponent interface   
of the Engines module. The name of the CORBA module will be **PYHELLO_ORB** and the name of the interface will be **PYHELLO_Gen**.

[<< Previous](build_proc_files.md)  
[>> Next](src_dir.md)
