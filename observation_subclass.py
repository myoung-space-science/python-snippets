from typing import *

import numpy as np

from heroes.common.base import Observation


class Test(Observation):
    def _get_from_context(self, key: str) -> Any:
        return self._context.get(key)

obs = Test(
    np.array([1.0, 1.5, 2.0]),
    units='cm',
    context={'thing': 4.56},
    name="Observation",
)
print(obs.units)
print(np.array(obs))
obs.units.to('m')
print(obs.units)
print(np.array(obs))
print(obs['thing'])
print(obs['nothing'])