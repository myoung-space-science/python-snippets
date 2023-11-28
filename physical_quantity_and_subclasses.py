import numpy as np

from heroes.common.base import Function, Variable, PhysicalQuantity


quantity = PhysicalQuantity('P', units='erg', dimensions='energy')
print(quantity)
quantity.units.to('J')
print(quantity)
variable = Variable(np.arange(10), name='V', units='m', dimensions='length')
print(variable)
print(variable[:])
variable.units.to('cm')
print(variable)
print(variable[:])
function = Function(lambda x: x**2, name='f', units='m/s', dimensions='speed')
print(function)
print(function(3))
function.units.to('cm/s')
print(function)
print(function(3))

