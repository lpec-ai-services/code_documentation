<!-- source: https://examples.vtk.org/site/PythonicAPI/PolyData/CellTreeLocator/ -->

# CellTreeLocator

Repository source: [CellTreeLocator](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/PolyData/CellTreeLocator.py)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/PolyData/CellTreeLocator/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**CellTreeLocator.py**

```python
#!/usr/bin/env python3

from vtkmodules.vtkCommonCore import reference
from vtkmodules.vtkCommonDataModel import (
    vtkCellTreeLocator,
    vtkGenericCell
)
from vtkmodules.vtkFiltersSources import vtkSphereSource

def main():
    sphere0 = vtkSphereSource(center=(0.0, 0.0, 0.0), radius=1.0)
    sphere0.update()

    # Create the cell locator tree.
    cell_tree = vtkCellTreeLocator(data_set=sphere0.output, automatic=True)
    cell_tree.BuildLocator()

    # These two points should not be on the sphere.
    test_inside = (0.5, 0.0, 0.0)
    test_outside = (10.0, 0.0, 0.0)

    passed = True
    pcoords = [0] * 3
    weights = [0] * 3
    tol = 0.0

    cell = vtkGenericCell()

    #  A point on the sphere.
    source_pt = [0.0] * 3
    sphere0.output.GetPoint(0, source_pt)
    cell_id = cell_tree.FindCell(source_pt, tol, cell, pcoords, weights)
    if cell_id >= 0:
        print(f'Point 0 on the sphere is in cell {cell_id}.')
        # Find the midpoint in the cell and check if it is in the same cell.
        bounds = cell.bounds
        mid_pt = list()
        for i in range(0, 6, 2):
            mid_pt.append(bounds[i] + (bounds[i + 1] - bounds[i]) / 2.0)
        cell_id_mid_pt = cell_tree.FindCell(mid_pt, tol, cell, pcoords, weights)
        if cell_id_mid_pt != cell_id:
            print('ERROR: The cell midpoint should be in the same cell.')
            passed = False
    else:
        print('ERROR: The cell corresponding to point 0 on the sphere was not found but should have been.')
        passed = False

    # Should be inside the sphere.
    cell_id = cell_tree.FindCell(test_inside, tol, cell, pcoords, weights)
    if cell_id >= 0:
        print(f'ERROR: test_inside point is in cell {cell_id} of the sphere but it should not be in the cell.')
        passed = False
    else:
        print('test_inside point is inside the sphere.')

    # Should be outside the sphere.
    cell_id = cell_tree.FindCell(test_outside, tol, cell, pcoords, weights)
    if cell_id >= 0:
        print(f'ERROR: test_outside point is in cell {cell_id} of the sphere but it should not be in the cell.')
        passed = False
    else:
        print('test_outside point is outside the sphere.')

    number_of_points = sphere0.output.number_of_points
    count_of_points = 0
    for i in range(0, number_of_points):
        source_pt = sphere0.output.GetPoint(i)
        cell_id = cell_tree.FindCell(source_pt, tol, cell, pcoords, weights)
        if cell_id:
            count_of_points += 1

    if count_of_points != number_of_points:
        num_missed = number_of_points - count_of_points
        print(f'ERROR: {num_missed} points should have been on the sphere!')
        passed = False
    else:
        print(f'Passed: A total of {count_of_points} points on the sphere were detected.')

    # This is based on [CellTreeLocator](https://gitlab.kitware.com/vtk/vtk/-/blob/master/Common/DataModel/Testing/Cxx/CellTreeLocator.cxx)
    # Kuhnan's sample code is used to test
    # vtkCellLocator::IntersectWithLine(...9 params...)

    # sphere1: The outer sphere.
    sphere1 = vtkSphereSource(theta_resolution=100, phi_resolution=100, radius=1.0)
    sphere1.update()

    # sphere2: The inner sphere.
    sphere2 = vtkSphereSource(theta_resolution=100, phi_resolution=100, radius=0.8)
    sphere2.update()

    # The normals obtained from the outer sphere.
    sphere_normals = sphere1.output.GetPointData().GetNormals()

    # Create the cell locator tree.
    locator = vtkCellTreeLocator(data_set=sphere2.output, automatic=True)
    locator.BuildLocator()

    # Initialise the counter and ray length.
    num_intersected = 0
    destin_pnt = [0] * 3
    tol = 0.0000001
    ray_len = 1.0 - 0.8 + tol  # = 1 - 0.8 + error tolerance
    param_t = reference(0.0)
    intersect = [0] * 3
    para_coord = [0] * 3
    sub_id = reference(0)
    cell_id = reference(0)

    # This loop traverses each point on the outer sphere (sphere1)
    #  and looks for an intersection on the inner sphere (sphere2).
    for i in range(0, sphere1.output.number_of_points):
        source_pnt = sphere1.output.GetPoint(i)
        normal_vec = sphere_normals.GetTuple(i)

        # Cast a ray in the negative direction toward sphere1.
        destin_pnt[0] = source_pnt[0] - ray_len * normal_vec[0]
        destin_pnt[1] = source_pnt[1] - ray_len * normal_vec[1]
        destin_pnt[2] = source_pnt[2] - ray_len * normal_vec[2]

        if locator.IntersectWithLine(source_pnt, destin_pnt, tol, param_t, intersect, para_coord, sub_id, cell_id,
                                     cell):
            num_intersected += 1

    if num_intersected != 9802:
        num_missed = 9802 - num_intersected
        print(f'ERROR: {num_missed} ray-sphere intersections missed!')
        passed = False
    else:
        print('Passed: A total of 9802 ray-sphere intersections detected.')

    if passed:
        print('All checks passed.')
    else:
        print('Some checks failed.')

if __name__ == '__main__':
    main()
```
