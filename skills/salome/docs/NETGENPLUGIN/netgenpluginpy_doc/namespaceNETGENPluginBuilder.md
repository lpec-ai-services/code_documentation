<!-- source: https://docs.salome-platform.org/latest/gui/NETGENPLUGIN/netgenpluginpy_doc/namespaceNETGENPluginBuilder.html -->

# NETGENPluginBuilder Namespace Reference

Python API for the NETGEN meshing plug-in module.
[More...](#details)

## Detailed Description

Python API for the NETGEN meshing plug-in module.

## Variable Documentation

### noNETGENPlugin

```python
int noNETGENPlugin = 0
```

### LIBRARY

```python
string LIBRARY = "libNETGENEngine.so"
```

### NETGEN_VERSION_MAJOR

```python
NETGEN_VERSION_MAJOR = NETGENPlugin.NETGEN_VERSION_MAJOR
```

### NETGEN_3D

```python
string NETGEN_3D = "NETGEN_3D"
```

Algorithm type: Netgen tetrahedron 3D algorithm, see [NETGEN_3D_Algorithm](classNETGENPluginBuilder_1_1NETGEN__3D__Algorithm.md).

### NETGEN_3D_Remote

```python
string NETGEN_3D_Remote = "NETGEN_3D_Remote"
```

### NETGEN_1D2D3D

```python
string NETGEN_1D2D3D = "NETGEN_2D3D"
```

Algorithm type: Netgen tetrahedron 1D-2D-3D algorithm, see [NETGEN_1D2D3D_Algorithm](classNETGENPluginBuilder_1_1NETGEN__1D2D3D__Algorithm.md).

### NETGEN_1D2D

```python
string NETGEN_1D2D = "NETGEN_2D"
```

Algorithm type: Netgen triangle 1D-2D algorithm, see [NETGEN_1D2D_Algorithm](classNETGENPluginBuilder_1_1NETGEN__1D2D__Algorithm.md).

### NETGEN_2D

```python
string NETGEN_2D = "NETGEN_2D_ONLY"
```

Algorithm type: Netgen triangle 2D algorithm, see [NETGEN_2D_Only_Algorithm](classNETGENPluginBuilder_1_1NETGEN__2D__Only__Algorithm.md).

### NETGEN_2D_Remote

```python
string NETGEN_2D_Remote = "NETGEN_2D_Remote"
```

### NETGEN_FULL

```python
string NETGEN_FULL = NETGEN_1D2D3D
```

Algorithm type: Synonim of NETGEN_1D2D3D, see [NETGEN_1D2D3D_Algorithm](classNETGENPluginBuilder_1_1NETGEN__1D2D3D__Algorithm.md).

### NETGEN

```python
string NETGEN = NETGEN_3D
```

Algorithm type: Synonim of NETGEN_3D, see [NETGEN_3D_Algorithm](classNETGENPluginBuilder_1_1NETGEN__3D__Algorithm.md).

### FULL_NETGEN

```python
string FULL_NETGEN = NETGEN_FULL
```

Algorithm type: Synonim of NETGEN_1D2D3D, see [NETGEN_1D2D3D_Algorithm](classNETGENPluginBuilder_1_1NETGEN__1D2D3D__Algorithm.md).

### SOLE

```python
int SOLE = 0
```

Hypothesis type enumeration: complex hypothesis (full set of parameters can be specified), see [NETGEN_Algorithm.Parameters()](classNETGENPluginBuilder_1_1NETGEN__Algorithm.md#a9ee33d8eced270456ca7d0bbc8d09620)

### SIMPLE

```python
int SIMPLE = 1
```

Hypothesis type enumeration: simple hypothesis (only major parameters are specified), see [NETGEN_Algorithm.Parameters()](classNETGENPluginBuilder_1_1NETGEN__Algorithm.md#a9ee33d8eced270456ca7d0bbc8d09620)

### VeryCoarse

```python
int VeryCoarse = 0
```

Fineness enumeration: very coarse quality of mesh, see [NETGEN_Algorithm.SetFineness()](classNETGENPluginBuilder_1_1NETGEN__Algorithm.md#a81522617a0e5045259d3c6af83260072)

### Coarse

```python
int Coarse = 1
```

Fineness enumeration: coarse quality of mesh, see [NETGEN_Algorithm.SetFineness()](classNETGENPluginBuilder_1_1NETGEN__Algorithm.md#a81522617a0e5045259d3c6af83260072)

### Moderate

```python
int Moderate = 2
```

Fineness enumeration: moderate quality of mesh, see [NETGEN_Algorithm.SetFineness()](classNETGENPluginBuilder_1_1NETGEN__Algorithm.md#a81522617a0e5045259d3c6af83260072)

### Fine

```python
int Fine = 3
```

Fineness enumeration: fine quality of mesh, see [NETGEN_Algorithm.SetFineness()](classNETGENPluginBuilder_1_1NETGEN__Algorithm.md#a81522617a0e5045259d3c6af83260072)

### VeryFine

```python
int VeryFine = 4
```

Fineness enumeration: very fine quality of mesh, see [NETGEN_Algorithm.SetFineness()](classNETGENPluginBuilder_1_1NETGEN__Algorithm.md#a81522617a0e5045259d3c6af83260072)

### Custom

```python
int Custom = 5
```

Fineness enumeration: custom quality of mesh specified by other parameters), see [NETGEN_Algorithm.SetFineness()](classNETGENPluginBuilder_1_1NETGEN__Algorithm.md#a81522617a0e5045259d3c6af83260072)
