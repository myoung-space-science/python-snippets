"""
A possible (but probably un-pythonic) way to add a type annotation that
indicates that the object returned from a function is a subtype of the object
passed into the function.
"""

import typing


T = typing.TypeVar('T')


class Parent:
    """Some class that does something."""

    def __init__(self, *args, **kwargs) -> None:
        pass


class Subtype(typing.Generic[T]):
    """Generic type to indicate a subclass in type hints."""


def create_subtype(base: typing.Type[T], *args, **kwargs) -> Subtype[T]:
    """Instantiate a subtype of `t`."""
    New = type('New', (base,), {})
    return New(*args, **kwargs)


new = create_subtype(Parent, 1, v=2)
# Hovering over new shows `new: Subtype[Parent]`
