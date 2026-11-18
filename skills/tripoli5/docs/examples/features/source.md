<!-- source: https://tripoli5.asnr.dev/documentation/latest-release/examples/features/source.html -->

# Source

Source distributions in TRIPOLI-5 are defined using the `tripoli5.source` and `tripoli5.distributions` modules. These modules provide the necessary classes to define various types of source distributions, including spatial, energetic and angular distributions.

The source must be specified for the simulation. Currently, TRIPOLI-5 supports the definition of a single source per simulation. Note that the source is defined independently of the geometry.

To define a source, you can create an instance of the `tripoli5.source.FactorizedSource` class. This class allows you to combine different distributions to create a source definition.

For sources that emit particles isotropically from a single point, it is recommended to use the `tripoli5.source.PointIsotropicSource` class.

Once your `source` object is instantiated, you can use it to configure the `tripoli5.simulation.SimulationBuilder` class.

## Imports

Start by importing TRIPOLI-5 and some necessary classes.

```ipython3
import tripoli5
from tripoli5.core.literals import MeV
from tripoli5.core.euclide import Point
from tripoli5.core.physics import ParticleType
```

## Factorized Source

In TRIPOLI-5, sources are factorized. Currently, only the neutron source is available. The `FactorizedSource` class in the `tripoli5.source` module represents a particle source that is factorized into independent spatial, energy, and angular distributions. This allows for the combination of different types of distributions to model particle sources.

The `tripoli5.distributions` module is divided into three main submodules: **angular**, **energy**, and **spatial**, each focusing on a specific aspect of particle source distributions.

### Spatial distributions

The `tripoli5.distributions.spatial` submodule manages the spatial location of particle sources. It provides different types of spatial distributions: `PointDistribution`, `LineDistribution`, `BoxDistribution`, `CylinderDistribution`, `CosineDistribution` and `SphereDistribution`. Below are examples of how to create each type of distribution:

#### Point Distribution

A `PointDistribution` represents a single point in 3D space. This is the simplest form of spatial distribution, where the source is concentrated at a specific coordinate.

```ipython3
# Create a point distribution
point_distrib = tripoli5.distributions.spatial.PointDistribution(
    point=Point(0.0, 0.0, 0.0)
)
```

#### Line Distribution

A `LineDistribution` represents a line segment in 3D space. The source is distributed uniformly along the line segment defined by two endpoints.

```ipython3
# Create a linear distribution
line_distrib = tripoli5.distributions.spatial.LineDistribution(
    p0=Point(0.0, 0.0, 0.0),
    p1=Point(1.0, 1.0, 1.0),
)
```

#### Box Distribution

A `BoxDistribution` represents a 3D box in space. The source is distributed uniformly within the volume defined by two opposite corners of the box.

```ipython3
# Create a box distribution
box_distrib = tripoli5.distributions.spatial.BoxDistribution(
    lower_left=Point(0.0, 0.0, 0.0), upper_right=Point(1.0, 1.0, 1.0)
)
```

#### Cylinder Uniform Distribution

A `CylinderDistribution` represents a cylindrical volume in 3D space. The source is distributed uniformly within the cylinder defined by its center, radius, and half-height.

```ipython3
# Create a cylindrical distribution
cylinder_distrib = tripoli5.distributions.spatial.CylinderDistribution(
    center=Point(0.0, 0.0, 0.0), radius=25.0, half_height=30.0
)
```

#### Cylinder Cosine Distribution

A `CylinderCosineDistribution` represents a distribution where the source intensity follows a cosine function in a cylindrical volume, both radially and axially. This type of distribution is particularly useful for modeling sources with a directional component, such as those found in nuclear reactors.

```ipython3
# Create a cosine distribution
cosine_distrib = tripoli5.distributions.spatial.CylinderCosineDistribution(
    center=Point(0.0, 0.0, 0.0), radius=25.0, half_height=30.0
)
```

#### Sphere Distribution

A `SphereDistribution` represents a spatial distribution where source particles are uniformly distributed within a spherical volume defined by its center and radius.

```ipython3
# Create a sphere distribution centered at (0, 0, 0) with a radius of 5
sphere_distrib = tripoli5.distributions.spatial.SphereDistribution(
    center=Point(0.0, 0.0, 0.0), radius=5.0
)
```

### Energy distributions

The `tripoli5.distributions.energy` submodule handles the energy characteristics of particles. It provides different types of energy distributions: `MaxwellSpectrum`, `MonoKinetic`, and `WattSpectrum`. Below are examples of how to create each type of distribution:

#### MonoKinetic Distribution

The `MonoKinetic` distribution represents particles that all have the same energy. This type of distribution is used when the source emits particles with a single, fixed energy. It is often used in simulations where the particles are assumed to have a constant energy, such as in monoenergetic neutron sources.

```ipython3
# Monocinetic spectrum
dirac_energy = tripoli5.distributions.energy.MonoKinetic(energy=2.0 * MeV)
```

#### Watt spectrum distribution

The `WattSpectrum` distribution represents particles with an energy spectrum that follows the Watt fission spectrum. This spectrum is commonly used to model the energy distribution of neutrons emitted during nuclear fission.

The Watt spectrum is described by the following probability distribution:

\[p(E) \, dE = \frac{2 \exp\left(-\frac{a}{4c}\right)}{\sqrt{\frac{\pi a^3}{c}}} \exp\left(-\frac{E}{a}\right) \sinh\left(\sqrt{\frac{E}{c}}\right) \, dE\]

where \(a\) and \(c\) are parameters that define the shape of the spectrum.

```ipython3
# Watt spectrum distribution
watt_spectrum = tripoli5.distributions.energy.WattSpectrum(a=1.0 * MeV, c=1.0 * MeV)
```

#### MaxwellSpectrum Distribution

The `MaxwellSpectrum` distribution represents particles with an energy spectrum that follows the Maxwell-Boltzmann distribution. This spectrum is commonly used to model the energy distribution of particles in thermal equilibrium, such as in a gas.

The Maxwell-Boltzmann distribution is described by the following probability distribution:

\[p(E) \, dE = \frac{2 \sqrt{E}}{\sqrt{\pi} (k_B T)^{3/2}} \exp\left(-\frac{E}{k_B T}\right)\]

where \(k_B\) is the Boltzmann constant and \(T\) is the temperature.

```ipython3
# Maxwell spectrum distribution
maxwell_spectrum = tripoli5.distributions.energy.MaxwellSpectrum(kb_T=1.0 * MeV)
# kb_T: Thermal energy of the medium
```

### Angular distributions

The `tripoli5.distributions.angular` submodule deals with the directional properties of particle emissions. It provides different types of angular distributions: `IsotropicAngularDistribution` and `MarsagliaIsotropicAngularDistribution`. Below are examples of how to create each type of distribution:

#### IsotropicAngularDistribution

The `IsotropicAngularDistribution` class is used to define an angular distribution where the direction of particles is uniformly distributed over a sphere. This means that every direction in three-dimensional space is equally likely. This type of distribution is commonly used when the source of particles is assumed to emit particles in all directions with equal probability.

```ipython3
# Isotropic angular distribution
isotropic_distrib = tripoli5.distributions.angular.IsotropicAngularDistribution()
```

#### MarsagliaIsotropicAngularDistribution

The `MarsagliaIsotropicAngularDistribution` class is a more specialized implementation of an isotropic angular distribution. It uses a specific algorithm, known as Marsaglia’s method, to sample isotropic directions in 3D space. This method is based on a mathematical approach described by George Marsaglia in his paper “Choosing a Point from the Surface of a Sphere” (Ann. Math. Stat. 43, 645-646, 1972).

Marsaglia’s method ensures that the directions are sampled uniformly over the surface of a sphere, providing a more accurate and efficient way to generate isotropic directions compared to simpler methods. This can be particularly useful in simulations where the accuracy of the angular distribution is important.

```ipython3
# Marsaglia isotropic angular distribution
marsaglia_distrib = (
    tripoli5.distributions.angular.MarsagliaIsotropicAngularDistribution()
)
```

### Create a Factorized Source

To create a Factorized Source, use the constructor of the `FactorizedSource` class. The parameters for the constructor are:

- spatial: An instance of a spatial distribution class that defines the spatial location of the particle source.
- energy: An instance of an energy distribution class that defines the energy characteristics of the particles.
- angle: An instance of an angular distribution class that defines the directional properties of the particle emissions.
- norm: (Optional) A normalization factor (default is 1.0) that scales the overall intensity of the source.

Below is an example of a factorized source combination that models a neutron particle source. This source is distributed within a cylindrical volume, has a monokinetic incident energy of 2 MeV, and emits particles uniformly in all directions. The intensity of the source is normalized to 1.0.

```ipython3
# Create a Factorized Source
factorized_source = tripoli5.source.FactorizedSource(
    spatial=tripoli5.distributions.spatial.CylinderDistribution(
        center=Point(0.0, 0.0, 0.0), radius=26.67, half_height=28.8169
    ),
    energy=tripoli5.distributions.energy.MonoKinetic(2.0 * MeV),
    angle=tripoli5.distributions.angular.IsotropicAngularDistribution(),
    norm=1.0,
)
```

## Point Isotropic Source

The `PointIsotropicSource` class in the `tripoli5.source` module represents a particle source that emits particles isotropically from a single point in space. This source is characterized by its location, energy distribution, particle type, and normalization factor.

### Create a Point Isotropic Source

To create a Point Isotropic Source, use the constructor of the `PointIsotropicSource` class. The parameters for the constructor are:

- type: The type of particle being emitted.
- energy_dist: An instance of an energy distribution class that defines the energy characteristics of the particles.
- x, y, z: The coordinates of the point in 3D space from which the particles are emitted.
- norm: (Optional) A normalization factor (default is 1.0) that scales the overall intensity of the source.

Below is an example of source that emits neutrons isotropically from a specific point in space. The source will have a monokinetic energy of 2.0 MeV and will be located at the origin (0.0, 0.0, 0.0). The intensity of the source is normalized to 1.0.

```ipython3
# Create a Point Isotropic Source
point_source = tripoli5.source.PointIsotropicSource(
    type_=ParticleType("Neutron"),
    energy_dist=tripoli5.distributions.energy.MonoKinetic(2.0 * MeV),
    point=Point(0.0, 0.0, 0.0),
    norm=1.0,
)
```
