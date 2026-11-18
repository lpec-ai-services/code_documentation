<!-- source: https://tripoli5.asnr.dev/documentation/latest-release/examples/features/physical_quantities.html -->

# Physical quantities in TRIPOLI-5

TRIPOLI-5 relies on the use of several classes to describe physical quantities including `Energy`, `Density`, `Temperature`, `Mass`, instead of simple `double`s. The corresponding classes are defined in the `tripoli5.core.physics` module.

This allows to:

- enforce constraints on the physical quantity that is defined (e.g., an `Energy` cannot be negative),
- make the units explicit in the user input,
- have safer interfaces by avoiding mixup in the arguments order (e.g., the position of two floating point arguments can be switched without warning whereas an `Energy` cannot be mistaken for a `Temperature`).

The example below shows how to create an `Energy` object, and how it is possible to retrieve its value as a `double` for different units. For more info on other classes available, refer to the [API documentation of the Core module](../../api/core-api.md).

```ipython3
from tripoli5.core.physics import Energy
```

```ipython3
# the energy object is defined with a given unit
one_mev_energy = Energy(1.0, Energy.Units.MeV)

# it is then possible to retrieve the value of the energy for different units
print(f"Energy in MeV = {one_mev_energy.MeV:.1e}")
print(f"Energy in keV = {one_mev_energy.keV:.1e}")
print(f"Energy in eV = {one_mev_energy.eV:.1e}")
```

```

Energy in MeV = 1.0e+00
Energy in keV = 1.0e+03
Energy in eV = 1.0e+06
```

You can also compare two objects of the same type even if they were not created using the same unit

```ipython3
Energy(0.1, Energy.Units.MeV) == Energy(100, Energy.Units.keV)
```

```

True
```

However, the syntax shown above is a bit verbose. To simplify the use of these objects, TRIPOLI-5 allows to use *literals* as shown below.

## TRIPOLI-5 literals in the Python API

It is possible to simplify the syntax for creating the above mentioned objects using these *literals*.

Basically, one can create a `Energy` with value `e` (of type `double`) in MeV by writing `energy = e * MeV` instead of the syntax above.

To do so, one must import the necessary literals from the `tripoli5.core.literals` module.

```ipython3
from tripoli5.core.literals import MeV

one_mev_energy_with_literal = 1.0 * MeV
print(type(one_mev_energy_with_literal), f"in MeV : {one_mev_energy_with_literal.MeV}")

one_mev_energy_without_literal = Energy(1.0, Energy.Units.MeV)

print(one_mev_energy_with_literal == one_mev_energy_with_literal)
```

```

<class 'tripoli5.core.physics.Energy'> in MeV : 1.0
True
```

Currently available literals for `tripoli5.core.physics` objects include

| Physical quantity | Literal | Corresponding TRIPOLI-5 unit |
| --- | --- | --- |
| Mass | g neutronMass massMeV | Mass.Unit.g Mass.Unit.NeutronMass Mass.Unit.MeV |
| Energy | eV keV MeV | Energy.Unit.eV Energy.Unit.keV Energy.Unit.MeV |
| Density | gPerCm3 | Density.Unit.gPerCm3 |
| Temperature | K tempMeV | Temperature.Unit.K Temperature.unit.MeV |
