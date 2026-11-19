<!-- source: https://docs.salome-platform.org/latest/gui/PYHELLO/load_module.html -->

# Loading PYHELLO component

The PYHELLO_ORB module has to be imported before making a request to load the component into the container, to obtain access to methods of the component. This container is made accessible in the runPYHELLO.py by means of the **container** variable:

```python

>> import PYHELLO_ORB
>> c=container.load_impl("PYHELLO","PYHELLO")
>> c.makeBanner("Christian")
```

The last instruction returns a string "Hello Christian". Proceed as follows to see the CORBA objects created by these actions:

```python

>> clt.showNS()
```

[<< Previous](run_procedure.md)  
[>> Next](catalog_def.md)
