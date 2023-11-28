"""
This module demonstrates declaring abstract properties on an abstract meta
class, causing those properties to behave as class attributes on subclasses. It
further demonstrates that the requirement to implement abstract
properties/methods will pass through to the highest level class that the user
attempts to instantiate, which is consistent with the behavior of other abstract
attributes.
"""

import abc


class Meta(metaclass=abc.ABCMeta):
    """"""
    def __init__(self) -> None:
        self._d = 11111

    @property
    @abc.abstractmethod
    def a(self):
        pass

    @property
    def d(self):
        return self._d


class Base(Meta):
    """"""


class Class(Base):
    """"""
    a = -1
    d = 99999

c = Class()
print(c.a)
print(c.d)
