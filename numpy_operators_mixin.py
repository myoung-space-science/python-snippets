"""
This is a place to test simple use cases of the numpy operators mixin class.
"""

import numpy


def prefer_numpy(cls: type):
    """Indicate that `method` should defer to `numpy` operators."""
    if '__array_ufunc__' in cls.__dict__:
        mixin = numpy.lib.mixins.NDArrayOperatorsMixin
        methods = {
            '__eq__',
            '__ne__',
            '__lt__',
            '__le__',
            '__gt__',
            '__ge__',
            '__abs__',
            '__pos__',
            '__neg__',
            '__add__',
            '__radd__',
            '__sub__',
            '__rsub__',
            '__mul__',
            '__rmul__',
            '__truediv__',
            '__rtruediv__',
            '__pow__',
            '__rpow__',
        }
        for method in methods:
            setattr(cls, method, getattr(mixin, method))
    return cls


@prefer_numpy # comment this to see different behavior for __add__
class Array(numpy.lib.mixins.NDArrayOperatorsMixin):
    """Some array."""

    def __init__(self, value, name: str=None) -> None:
        self.value = value
        self.name = name

    def __repr__(self) -> str:
        clsname = self.__class__.__qualname__
        if self.name:
            return f"{clsname}({self.value, self.name})"
        return f"{clsname}({self.value})"

    def __add__(self, other):
        print(f"__add__({self}, {other})")

    def __array_ufunc__(self, ufunc, method, *args, **kwargs):
        if kwargs:
            sa = ', '.join(str(arg) for arg in args)
            sk = ', '.join(f"{k}={v}" for k, v in kwargs.items())
            print(f"{ufunc}.{method}({sa}, {sk})")
        print(f"{ufunc}.{method}{args}")


a0 = Array(+2)
a1 = Array(-2)
a0 + a1
a0 + 4
4 + a0
a0 - 4
a0 % 2

