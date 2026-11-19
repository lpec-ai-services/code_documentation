<!-- source: https://docs.salome-platform.org/latest/gui/PYHELLO/load_lcc.html -->

# Loading PYHELLO component via LifeCycle service

The method of loading the component is not very different from that is described above. The services of the LifeCycle module are used in this case instead of calling the container directly. The call sequence is contained in the runPYHELLO.py **test()** function.

```python

    c=test(clt)
    c.makeBanner("Christian")
```

The test function creates the LifeCycle object. It then asks for the PYHELLO component to be loaded in the FactoryServer container:

```python
def test(clt):
 """
    Test function that creates an instance of PYHELLO component
    usage : hello=test(clt)
    """
    import LifeCycleCORBA
    lcc = LifeCycleCORBA.LifeCycleCORBA(clt.orb)
    import PYHELLO_ORB
    pyhello = lcc.FindOrLoadComponent("FactoryServePy", "PYHELLO")
    return pyhello
```

[<< Previous](catalog_def.md)  
[>> Next](load_iapp.md)
