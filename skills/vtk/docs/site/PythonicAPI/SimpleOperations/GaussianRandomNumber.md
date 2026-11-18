<!-- source: https://examples.vtk.org/site/PythonicAPI/SimpleOperations/GaussianRandomNumber/ -->

# GaussianRandomNumber

Repository source: [GaussianRandomNumber](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/SimpleOperations/GaussianRandomNumber.py)

### Description

This example generates three random numbers from a Gaussian distribution with mean 0.0 and standard deviation 2.0.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/SimpleOperations/GaussianRandomNumber/)), ([CSharp](https://examples.vtk.org/site/CSharp/SimpleOperations/GaussianRandomNumber/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**GaussianRandomNumber.py**

```python
#!/usr/bin/env python3

from vtkmodules.vtkCommonCore import vtkBoxMuellerRandomSequence

def main():
    # Generate three random numbers from a Gaussian distribution with mean 0.0 and standard deviation 2.0
    num_rand = 3
    mean = 0.0
    standard_deviation = 2.0
    random_sequence = vtkBoxMuellerRandomSequence()
    for i in range(0, num_rand):
        a = random_sequence.GetScaledValue(mean, standard_deviation)
        random_sequence.Next()
        print(f'{a:9.6f}')

if __name__ == '__main__':
    main()
```
