<!-- source: https://docs.salome-platform.org/latest/gui/PYHELLO/run_procedure.html -->

# Running SALOME

Go to the the <PYHELLO_module_installation_dir> directory and type:

```python

[bash% ] ./bin/salome/runPYHELLO
```

This command runs SALOME session configured for KERNEL and the PYHELLO module. At the end of running, the user will be prompted by the Python interpreter command line configured for SALOME that provides access to SALOME Python API (including CORBA interfaces).

The runPYHELLO file is a shell script that executes a Python commands running SALOME session by passing arguments to it in a command line:

```python

${KERNEL_ROOT_DIR}/bin/salome/envSalome.py python -i $PYHELLO_ROOT_DIR/bin/salome/runPYHELLO.py --modules=PYHELLO --killall
```

These arguments state that the runPYHELLO.py script located in the PYHELLO module will be used, that the PYHELLO component will be activated and all previously running SALOME sessions should be shutdowned.

This command will not function unless the following environment variables have previously been set:

```python

export KERNEL_ROOT_DIR=<KERNEL_module_installation_dir>
export PYHELLO_ROOT_DIR=<PYHELLO_module_installation_dir>
```

Warning
:   It is possible that the SALOME run will not reach the end. In some circumstances, the time to start CORBA servers may be long and could exceed the timeout. If the reasons is that the time to load dynamic libraries is long, it is possible that a second run immediately afterwards will be successful.

[<< Previous](build_procedure.md)  
[>> Next](load_module.md)
