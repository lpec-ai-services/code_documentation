<!-- source: https://manta-project.gitlab.io/manta/manta_frontend_user_guide/simulation/time_increment_computers.html -->

# Time increment computers

Time increment computers are helper objects that can be used by a
simulation object to determine the next time increment.

## Example of usage

The following snipppet adds the `MaximumFieldIncrement` time
increment computer to a simulation to adapt the time step. This time
increment computer will try to calculate a time increment such that the
increment of the equivalent plastic strain in the material `cube`
would remain below a threshold value of \(10^{-4}\):

```python
s.addTimeIncrementComputer("MaximumFieldIncrement",
                           field = 'EquivalentPlasticStrain', fieldType = 'ipField', material = 'cube',
                           maximumIncrementValue=1e-4)
```

## List of available time increment computers

### `MaximumFieldIncrement`

The `MaximumFieldIncrement` time increment computer tries to
calculate the next time step such that the increment of a given scalar
value \(x\) remains below a given threshold
\(\varepsilon_{\Delta\, x}\). Note that \(\varepsilon_{\Delta\,
x}\) must be positive and the `MaximumFieldIncrement` time
increment computer only works for increasing quantities, such as the
porosity in ductile failure.

Let \(\Delta x_{c}\) be the increment of the \(x\) at the end of
the current time step and \(\Delta t_{c}\) the current time
increment. The next time increment \(\Delta t_{e}\) is estimated as
follows:

\[\Delta t_{e} =
\frac{\varepsilon_{\Delta\, x}}
{\max\left(\Delta x_{c}, 10^{-2}\,\cdot\, \varepsilon_{\Delta\, x}\right)}
\,\cdot\,\Delta t_{c}\]

Note

With this formula, \(\Delta t_{e}\) may be at most 100 greater
than \(\Delta t_{c}\).

This is generally not an issue as the next time increment also depends
from other time increment computers. In particular, a default
time step increment computer is always declared by the
`Simulation` class which proposes the distance to the end
of the current temporal sequence as the next time step. Moreover,
the `Simulation` class also has optional parameters which
controls (limits) the increase (or decrease) of the time increment
(with respect to the previous one)

#### Parameters

The `MaximumFieldIncrement` inherits the parameters of the
`MaximumIncrement` curve (see Section
[The Maximum, Minimum and MaximumIncrement curves](../post_processings/curves.md#maximum-increment-curve) for details) plus one parameter,
`maximumIncrementValue`, which gives the value of the threshold
\(\varepsilon_{\Delta\, x}\)
