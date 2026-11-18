<!-- source: https://manta-project.gitlab.io/manta/manta_frontend_user_guide/physical_system/geometric_hypothesis.html -->

# Definining the geometric hypothesis and the default structural hypothesis

In many cases, the knowledge of the space dimension as
defined by the mesh, is not enough. Two additional informations may be
defined at the physical system level:

- the geometric hypothesis,
- the default structural hypothesis.

## Geometric hypothesis

The geometric hypothesis is mostly used in \(2D\) to distinguish
axisymmetrical computations from in plane computations.

The following geometric hypotheses are available:

- `default` in \(1D\),
- `inPlane` (or equivalently `default`) in \(2D\),
- `axisymmetrical` in \(2D\)
- `tridimensional` (or equivalently
  `default`) in \(3D\).

For each parameters, both synthax, `default` and `Default`
(with an uppercase on the first letter) would be accepted. This is true for every listed keywords,
*e.g.* `inPlane` and `InPlane` or `tridimensional` and `Tridimensional`.
The geometric hypothesis does not need to be explicitly specified in
\(1D\) or in \(3D\).

### Example

PYTHON

```python

ps = manta.PhysicalSystem(mesh = {'file': 'mesh.med',
                                  'meshName': 'MESH',
                                  'domains': ['nameOfDomain'],
                                  'boundaries': ['nameOfBoundary1',
                                                 'nameOfBoundary2',
                                                 'nameOfBoundary3'],
                                  'nodes': ['nameOfNode1'], 
                                  'edges': ['nameOfEdge1', 'nameOfEdge2']}, 
                          geometricHypothesis = 'inPlane')
```

C++

```c++
const auto mesh_parameters = Parameters{{"file", "mesh.med"},{"meshName", "nameOfMesh"},
{"domains", "nameOfDomain"}, {"boundaries", {"nameOfBoundary1", "nameOfBoundary2", "nameOfBoundary3"}}, {"nodes", {"nameOfNode1"}}, {"edges", {"nameOfEdge1", "nameOfEdge2"}}};
auto ps = construct<PhysicalSystem>(ctx, Parameters{{"mesh", mesh_parameters}, {"geometricHypothesis", "inPlane"}});
```

Note

`inPlane` 2D modeling supposes that
all quantities which would be integrated along the third dimension
(forces, section of beam, ... e.g.) in 3D modeling
are defined **by length along the third dimension**.
Hence, 2D forces are expressed in N/m
and a beam cross section geometric area is in m 2/m.

## Default structural hypothesis

The following structural hypotheses are available:

- `planeStress` and
  `planeStrain`. This structural
  hypothesis is only compatible with the `inPlane` geometric
  hypothesis.
- `axisymmetrical`. This structural
  hypothesis is only compatible with the `axisymmetrical` geometric
  hypothesis.
- `tridimensional`.

For each parameters, both synthax, `planeStress` and `PlaneStress`
(with an uppercase on the first letter) would be accepted.

In practice, the structural hypothesis can be deduced automatically by
the physical system from the geometric hypothesis, except when the
geometric hypothesis is `inPlane`.

Note also that, in most cases, it seems more meaningful to define the
structural hypothesis at the brick level. This is why a default
structural hypothesis is rarely defined at the physical system level in
the examples.
