"""
This example provides a pattern for creating and using a metaclass that lets its
classes require that their subclasses define certain attributes at instantiation
(i.e., in `__init__`). I originally used this pattern in `common.iterables` for
`RequiredAttrMeta` to allow `CollectionMixin` to require any classes that use it
to define `self.members` before moving to a different approach that didn't
require a metaclass.
"""

import abc


class Meta(abc.ABCMeta):
    """"""
    _required = []
    def __call__(self, *args, **kwargs):
        """"""
        instance = super().__call__(*args, **kwargs)
        cls = self.__qualname__
        for attr in self._required:
            if not hasattr(instance, attr):
                raise NotImplementedError(
                    f"Can't instantiate {cls} without attribute '{attr}'"
                )
        return instance


class Base(metaclass=Meta):
    """"""
    _required = ['thing']

    @abc.abstractmethod
    def __init__(self) -> None:
        self.thing = None


class Class(Base):
    """"""
    def __init__(self) -> None:
        self.thing = "Thing"
        print("__init__")


c = Class()
print(c.thing)
