import abc
from typing import *


class ReprMixin:
    """"""
    def __init__(self) -> None:
        self._name = "ReprMixin"

    @property
    def name(self) -> str:
        """"""
        # This will never return `str(self._name)` when used as a mixin, since
        # the subclass will use `Base.__init__`.
        if hasattr(self, '_name'):
            return str(self._name)
        return f"{self.__class__.__qualname__}"

    def _repr(self, arg: str=None) -> str:
        """"""
        if not arg:
            return self.name
        return f"{self.name}({arg})"

    def __repr__(self) -> str:
        """"""
        return self._repr()


class Base(abc.ABC):
    """"""
    def __init__(self, values: Iterable[float]) -> None:
        self._values = values

    def __getitem__(self, index) -> Tuple[float]:
        """"""
        values = self._update(self._values)
        return values[index]

    @abc.abstractmethod
    def _update(self, values: Iterable[float]) -> Tuple[float]:
        """"""
        pass


class DoublerPlain(Base):
    """"""
    def _update(self, values: Iterable[float]) -> Tuple[float]:
        """"""
        return tuple(2.0 * v for v in values)


class DoublerWithRepr(Base, ReprMixin):
    """"""
    def _update(self, values: Iterable[float]) -> Tuple[float]:
        """"""
        return tuple(2.0 * v for v in values)


class DoublerCustom(Base, ReprMixin):
    """"""
    def _update(self, values: Iterable[float]) -> Tuple[float]:
        """"""
        return tuple(2.0 * v for v in values)

    def __repr__(self) -> str:
        """"""
        return self._repr(', '.join(str(v) for v in self._values))


values = [1.0, 2.0, 3.0]
cases = [DoublerPlain, DoublerWithRepr, DoublerCustom]
for case in cases:
    doubler = case(values)
    print(f"2 * {values[1]} = {doubler[1]}")
    print(str(doubler))

try:
    doubler = Base(values)
except TypeError:
    print("Can't subclass an ABC")