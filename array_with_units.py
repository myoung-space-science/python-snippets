from typing import *

import numpy as np

from heroes.common.units import Units


class ArrayWithUnits:
    """A class demonstrating array-value scaling with units.

    This class uses an instance of the ``units.Units`` class to provide a
    dynamic object representing the units associated with the given numerical
    values. Updating the units will self-consistently rescale the numerical
    values.

    NB: This implementation allows the user to access all the values via the
    `values` property, or a subset of values via `__getitem__`. Alternative
    implementations could force the user to only use `__getitem__` by obscuring
    the `values` property through renaming (e.g., `_scaled_values`) or
    converting it to a method.
    """
    def __init__(self, values: Iterable, units: Union[str, Units]=None) -> None:
        self._values = values
        self._units = Units(units or '')
        self._base = self.units.copy()

    def __getitem__(self, index) -> np.ndarray:
        """Access array values via index notation."""
        return self.values[index]

    @property
    def values(self) -> np.ndarray:
        """The scaled numerical values."""
        return self._scale * np.array(self._values)

    @property
    def _scale(self) -> float:
        """Update the numerical scale factor."""
        reference = self._base.copy()
        return reference.to(self.units)

    @property
    def units(self) -> Units:
        """A dynamic object representing this observation's units."""
        return self._units


# Set the initial units to 'cm'/'centimeters' and store it in a variable to use
# later.
cm = 'cm'

# Create an instance of the array class.
test = ArrayWithUnits(np.array([1.0, 1.5, 2.0]), cm)

# Print the original values.
print(f"The original values are {test.values}")
print(f"The original units are {test.units}")

# Demonstrate changing units with self-consistent scaling. This print the values
# accessed by property and by slice (via __getitem__), and a single value
# accessed by index. It converts back to the original units to demonstrate that
# the scaling is reversible. The final conversion will fail because 'J'/'joules'
# is a unit of energy, which is incommensurate with units of length.
for new in ['m', cm, 'km', 'J']:
    test.units.to(new)
    print(f"The new units are {test.units}")
    print(f"The values (via property) are {test.values}")
    print(f"The values (via slice) are {test[:]}")
    print(f"The value at index 0 is {test[0]}")
