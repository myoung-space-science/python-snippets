from typing import *


KT = TypeVar('KT')
VT = TypeVar('VT')
class MyMappingType(Generic[KT, VT]):
    """"""
    def __getitem__(self, key: KT) -> VT: ...

class Variable: ...

class C:
    """"""
    def __init__(
        self,
        m: MyMappingType[str, Variable],
    ) -> None:
        self.m = m
        v = self.m['Br']


