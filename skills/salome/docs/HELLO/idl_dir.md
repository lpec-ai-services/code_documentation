<!-- source: https://docs.salome-platform.org/latest/gui/HELLO/idl_dir.html -->

# The idl directory

The `idl` directory requires a `CMakeLists.txt` that must make the compilation of the CORBA IDL `HELLO_Gen.idl` file and install all the generated files into the correct module installation directories. This is done by using `OMNIORB_ADD_MODULE()` CMake macro:

```python
OMNIORB_ADD_MODULE(SalomeIDLHELLO HELLO_Gen.idl ${KERNEL_ROOT_DIR}/idl/salome ${KERNEL_SalomeIDLKernel})
INSTALL(TARGETS SalomeIDLHELLO EXPORT ${PROJECT_NAME}TargetGroup DESTINATION ${SALOME_INSTALL_LIBS})
```

The IDL file itself must define a CORBA component for which the name must be different from the module name to avoid name conflicts and define a CORBA interface that is derived at least from the *EngineComponent* interface   
of the *Engines* module. In case of HELLO module, the name of the CORBA component is **HELLO_ORB** and the name of the interface is **HELLO_Gen**.

[<< Previous](build_proc_files.md)  
[>> Next](src_dir.md)
