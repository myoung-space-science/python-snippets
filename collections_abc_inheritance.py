"""
This module demonstrates inheritance when the base class comes from
`collections.abc`. It is closely related to the `abc_hierarchy.py` example
module. Specifically, this module demonstrates that you can partially implement
a subclass of `collections.abc.Mapping` as long as subsequent subclasses
complete the implementation.
"""

import collections.abc
from typing import *


class BaseMapping(collections.abc.Mapping):
    """"""
    def __init__(self, stuff: Iterable) -> None:
        self._stuff = stuff

    def __len__(self) -> int:
        return len(self._stuff)

    def __iter__(self) -> Iterator:
        return iter(self._stuff)


class MyMapping(BaseMapping):
    """"""
    def __init__(self, stuff: Iterable) -> None:
        super().__init__(stuff)

    def __getitem__(self, k):
        return self._stuff[k]


stuff = [3, 5, 9]
cases = [BaseMapping, MyMapping]
for case in cases:
    name = case.__name__
    try:
        instance = case(stuff)
        print(f"Instantiated {name}")
    except TypeError as err:
        print(f"Couldn't instantiate {name}: {err}")

my = MyMapping(stuff)
print(f"Concrete class contains {my[0]} at index 0")
