"""
This example simply demonstrates that a concrete implementation of an abstract
method may be a method or a property.
"""

import abc


class A(abc.ABC):
    @abc.abstractmethod
    def func(self):
        pass


class B(A):
    def func(self):
        return "method"


class C(A):
    @property
    def func(self):
        return "property"


b = B()
print(b.func()) # -> "method"
c = C()
print(c.func) # -> "property"
