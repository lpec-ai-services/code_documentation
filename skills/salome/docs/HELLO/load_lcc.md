<!-- source: https://docs.salome-platform.org/latest/gui/HELLO/load_lcc.html -->

# Loading HELLO component via LifeCycle service

The method of loading the component is not very different from that is described above. The services of the LifeCycle module are used in this case instead of calling the container directly. The call sequence is contained in the `runHELLO.py` *test()* function.

```python

    import salome
    salome.salome_init()
    c = test(clt)
    c.hello("Christian")
```

The test function creates the LifeCycle object. It then asks for the HELLO component to be loaded in the *FactoryServer* container:

```python
def test(clt):
 """
    Test function that creates an instance of HELLO component
    usage : hello=test(clt)
    """
    import LifeCycleCORBA
    lcc = LifeCycleCORBA.LifeCycleCORBA(clt.orb)
    import HELLO_ORB
    hello = lcc.FindOrLoadComponent("FactoryServer", "HELLO")
    return hello
```

[<< Previous](catalog_def.md)  
[>> Next](load_iapp.md)
