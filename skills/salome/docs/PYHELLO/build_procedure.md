<!-- source: https://docs.salome-platform.org/latest/gui/PYHELLO/build_procedure.html -->

# Construction, installation

Before building PYHELLO module, please ensure that SALOME environment is set properly. Assume that SALOME environment is set in env_products.sh script. In order to build and install PYHELLO module, you have to perform several steps:

```python

[bash% ] source env_products.sh
[bash% ] mkdir PYHELLO_BUILD
[bash% ] cd PYHELLO_BUILD
[bash% ] cmake -DCMAKE_BUILD_TYPE=<Mode> -DCMAKE_INSTALL_PREFIX=<PYHELLO_module_installation_dir> ../PYHELLO1_SRC
[bash% ] make
[bash% ] make install
```

The first command sets environment for building project.

Second command creates a build directory for the PYHELLO module. Then next step is to cd to this build directory. From this directory you invoke cmake command, where <Mode> is build mode (Release or Debug), <PYHELLO_module_installation_dir> is a destination folder to install PYHELLO module of SALOME. By default (if CMAKE_INSTALL_PREFIX option is not given), PYHELLO module will be configured for installation to the /usr directory that requires root permissions to complete the installation.

Next steps - build the package (`make`) and install it (`make` install).

On each step, you have to ensure that the operation is finished correctly (no errors raised). After the last step is finished, the PYHELLO module is built and installed to the `<PYHELLO_module_installation_dir>` directory.

[<< Previous](doc_dir.md)  
[>> Next](run_procedure.md)
