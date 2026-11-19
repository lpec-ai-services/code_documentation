<!-- source: https://docs.salome-platform.org/latest/gui/HELLO/bin_dir.html -->

# The bin directory

The file `VERSION.in` is used to document the module, it must define its version and (optionally) its compatibilities or incompatibilities with other modules. Therefore, it is strongly recommended but is not essential for correct operation of the module.

The `runHELLO.in` file is the equivalent of the `runSalome` script distributed by the KERNEL module but configured to start SALOME session with HELLO module only.

The `runHELLO.py` file reuses part of functionality provided by the KERNEL's `runSalome.py` script. It is used to run SALOME session and start HELLO module in this session.

[<< Previous](src_dir.md)  
[>> Next](doc_dir.md)
