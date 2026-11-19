<!-- source: c3po/multi1D/Grid.py -->

# `c3po.multi1D.Grid`

Contain the classes `Grid`, `MEDGrid`, `CartesianGrid`, `HexagonalGrid` and `MultiLevelGrid`.

### `class c3po.multi1D.Grid.Grid  — bases: ABC`

`Grid` is an abstract class defining a 2D mesh to be used by `MEDInterface`.

Each cell is associated with an integer (correspondence) that will be used to identify a 1D object.

#### `Grid.clone(self)`

Return a clone of `self`.

## Returns

Grid  
A clone of `self`.

#### `Grid.getCorrespondence(self, cellId)`

Return the correspondence associated with the required cell.

## Parameters

cellId  
Index of the cell in the mesh.

## Returns

> Correspondence associated with the cell.

#### `Grid.getNumberOfCells(self)`

Return the number of cells in the grid.

## Returns

> The number of cells in the grid.

#### `Grid.setCorrespondences(self, correspondences)`

Set the whole table of correspondences.

<div class="note">

<div class="title">

Note

</div>

Use `c3po.multi1D.NO_CORRESPONDENCE` as correspondence value in empty positions.

</div>

## Parameters

correspondences  
Table of correspondence to be copied. `correspondences[i]` will be associated with the cell `i`.

#### `Grid.setCorrespondence(self, cellId, correspondence)`

Set one correspondence in one cell.

<div class="note">

<div class="title">

Note

</div>

Use `c3po.multi1D.NO_CORRESPONDENCE` as correspondence value in empty positions.

</div>

## Parameters

cellId  
Index of the cell in the mesh.

correspondence  
Value to set in the cell.

#### `Grid.getNodeCoordinates(self, cellId)`

Return the coordinate of the nodes of one cell.

## Parameters

cellId  
Index of the cell in the mesh.

## Returns

list  
A list with the 2D coordinates of the nodes of the cell.

#### `Grid.shift(self, xShift, yShift)`

Shift (geometric translation) the grid.

## Parameters

xShift  
Shift to be applied on x coordinate.

yShift  
Shift to be applied on y coordinate.

#### `Grid.getMEDMesh(self)`

Return a MEDCoupling mesh image of the grid (but without correspondences).

<div class="note">

<div class="title">

Note

</div>

It should be the same result than `toMED`.getMesh().

</div>

## Returns

> A MEDCoupling 2D mesh.

#### `Grid.toMED(self)`

Return a MEDCoupling field image of `self`.

## Returns

> A MEDCoupling field image of `self`.

### `class c3po.multi1D.Grid.MEDGrid(field)  — bases: Grid`

MEDGrid allows to handle a 2D grid defined with a MEDCoupling mesh or field.

#### `MEDGrid.clone(self)`

See `Grid.clone`.

#### `MEDGrid.getCorrespondence(self, cellId)`

See `Grid.getCorrespondence`.

#### `MEDGrid.getNumberOfCells(self)`

See `Grid.getNumberOfCells`.

#### `MEDGrid.setCorrespondences(self, correspondences)`

See `Grid.setCorrespondences`.

#### `MEDGrid.setCorrespondence(self, cellId, correspondence)`

See `Grid.setCorrespondence`.

#### `MEDGrid.getNodeCoordinates(self, cellId)`

See `Grid.getNodeCoordinates`.

#### `MEDGrid.shift(self, xShift, yShift)`

See `Grid.translate`.

#### `MEDGrid.getMEDMesh(self)`

### `class c3po.multi1D.Grid.CartesianGrid(xSizes, ySizes)  — bases: MEDGrid`

`CartesianGrid` allows to define and handle a cartesian 2D mesh.

Cells are numbered along the x axis first, then along the y axis ( `loop(yDim){ loop(xDim) {i++}}` ). The mesh is centered on `(0., 0.)`.

#### `CartesianGrid.clone(self)`

see `Grid.clone`

#### `CartesianGrid.setCorrespondenceCartesian(self, xIndex, yIndex, correspondence)`

Set one correspondence from the indexes of the cell in the cartesian grid.

<div class="note">

<div class="title">

Note

</div>

Use `c3po.multi1D.NO_CORRESPONDENCE` as correspondence value in empty positions.

</div>

## Parameters

xIndex  
Index of the cell along the x axis.

yIndex  
Index of the cell along the y axis.

correspondence  
Value to associate with the cell.

### `class c3po.multi1D.Grid.HexagonalGrid(numRings, pitch)  — bases: MEDGrid`

`HexagonalGrid` allows to define and handle an hexagonal 2D mesh.

Cells are numbered in a "snail" way, from inside to outside. The central cell is numbered 0. The first cell of each ring makes an angle of `-pi/6` with x axis. The mesh is centered on `(0., 0.)`.

#### `HexagonalGrid.clone(self)`

see `Grid.clone`

#### `HexagonalGrid.setCorrespondenceHexagonal(self, ringIndex, positionIndex, correspondence)`

Set one correspondence from the indexes of the cell in the hexagonal grid.

<div class="note">

<div class="title">

Note

</div>

Use `c3po.multi1D.NO_CORRESPONDENCE` as correspondence value in empty positions.

</div>

## Parameters

ringIndex  
Index of the ring.

positionIndex  
Index of the cell on the ring.

correspondence  
Value to associate with the cell.

### `class c3po.multi1D.Grid.MultiLevelGrid(rootGrid, leafGrids)  — bases: Grid`

`MultiLevelGrid` allows to define and handle grids inside other grids.

#### `MultiLevelGrid.clone(self)`

see `Grid.clone`

#### `MultiLevelGrid.getNumLevels(self)`

Return the number of level.

<div class="note">

<div class="title">

Note

</div>

`level = 0` if empty (`rootGrid` with no cells), 1 if leaf grids are not themselves `MultiLevelGrid`, and `n + 1` with `n` the level of leaf grids otherwise.

</div>

## Returns

> Number of level.

#### `MultiLevelGrid.setCurrentLevel(self, level)`

Set the current level.

<div class="note">

<div class="title">

Note

</div>

All methods inherited from `Grid` will address this level. At level 0, the `MultiLevelGrid` behaves like the `rootGrid`. At level `n > 0`, it behaves like the juxtaposition of leaf grids with current level `n - 1`. Defaut : the value returned be `getNumLevels`.

</div>

## Parameters

level  
Level New current level.

#### `MultiLevelGrid.getCurrentLevel(self)`

Return the current level (see `setCurrentLevel`).

## Returns

> The current level.

#### `MultiLevelGrid.getCorrespondence(self, cellId)`

See `Grid.getCorrespondence`

#### `MultiLevelGrid.getNumberOfCells(self)`

See `Grid.getNumberOfCells`

#### `MultiLevelGrid.setCorrespondences(self, correspondences)`

See `Grid.setCorrespondences`

#### `MultiLevelGrid.setCorrespondence(self, cellId, correspondence)`

See `Grid.setCorrespondence`

#### `MultiLevelGrid.getNodeCoordinates(self, cellId)`

See `Grid.getNodeCoordinates`

#### `MultiLevelGrid.shift(self, xShift, yShift)`

See `Grid.shift`

#### `MultiLevelGrid.getMEDMesh(self)`
