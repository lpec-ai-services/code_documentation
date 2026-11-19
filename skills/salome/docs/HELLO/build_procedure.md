<!-- source: https://docs.salome-platform.org/latest/gui/HELLO/build_procedure.html -->

# Construction, installation

Before building HELLO module, please ensure that SALOME environment is set properly. Assume that SALOME environment is set in env_products.sh script. In order to build and install HELLO module, you have to perform several steps:

```python

[bash% ] source env_products.sh
[bash% ] mkdir HELLO_BUILD
[bash% ] cd HELLO_BUILD
[bash% ] cmake -DCMAKE_BUILD_TYPE=<Mode> -DCMAKE_INSTALL_PREFIX=<HELLO_module_installation_dir> ../HELLO1_SRC
[bash% ] make
[bash% ] make install
```

The first command sets environment for building project.

Second command creates a build directory for the HELLO module. Then next step is to cd to this build directory. From this directory you invoke cmake command, where <Mode> is build mode (Release or Debug), <HELLO_module_installation_dir> is a destination folder to install HELLO module of SALOME. By default (if CMAKE_INSTALL_PREFIX option is not given), HELLO module will be configured for installation to the /usr directory that requires root permissions to complete the installation.

Next steps - build the package (`make`) and install it (`make` install).

On each step, you have to ensure that the operation is finished correctly (no errors raised). After the last step is finished, the HELLO module is built and installed to the `<HELLO_module_installation_dir>` directory.

[<< Previous](doc_dir.md)  
[>> Next](run_procedure.md)
