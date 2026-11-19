<!-- source: https://docs.salome-platform.org/latest/gui/HELLO/load_module.html -->

# Loading HELLO component

The *HELLO_ORB* module has to be imported before making a request to load the component into the container, to obtain access to methods of the component. This container is made accessible in the `runHELLO.py` by means of the *container* variable:

```python

>> import salome
>> salome.salome_init()
>> import HELLO_ORB
>> c = container.load_impl("HELLO", "HELLO")
>> c.hello("Christian")
```

The last instruction invokes HELLO module's service *hello()*. Proceed as follows to see the CORBA objects created by these actions:

```python

>> clt.showNS()
```

[<< Previous](run_procedure.md)  
[>> Next](catalog_def.md)
