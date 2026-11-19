<!-- source: https://docs.salome-platform.org/latest/dev/FIELDS/fields_arch_corba_services.html -->

# FIELDS module CORBA services

To manage presentations in the FIELDS module, the following CORBA components and services are implemented:

- `MED_ORB::MED_Gen` is a CORBA engine of FIELDS module; it inherits `Engine::EngineComponent` from KERNEL module. It is aimed for

  - publishing of a structure of MED file (mesh, fields and timesteps) in *SALOMEDS*,
  - registering of presentations.
- `MEDCALC::MEDFactory` is another CORBA `Engine::EngineComponent` interface (it means that it can be retrieved in the CORBA context using the `SALOME_LifeCycleCorba` registry).
  It provides access to the CORBA services, which are used to manage FIELDS presentations:

  > - `MEDCALC::MEDDataManager` - reads structure of the MED file; internally it uses *MEDCoupling* library for that purpose,
  > - `MEDCALC::MEDCommandsHistoryManager` - collects a history of Python commands which are executed in the Python console in the FIELDS module and provides access to the sequence of commands,
  > - `MEDCALC::MEDPresentationManager` - main service for creating FIELDS presentations and managing their parameters; it is used in [FIELDS GUI](fields_arch_gui.md#fields-arch-gui-page) to retrieve parameters of presentations
  >   and [medcalc](fields_arch_medcalc_py.md#fields-arch-medcacl-py-page) Python package to create and update FIELDS presentations.
