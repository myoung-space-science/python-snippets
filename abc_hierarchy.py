"""
This module demonstrates creating a class hierarchy based on the `abc` (abstract
base class) module. Specifically, it illustrates the difference between defining
and implementing abstract methods, as well as when you can and can't instantiate
a class in such a hierarchy.
"""

import abc
from typing import *


class Base(abc.ABC):
    """"""
    @abc.abstractmethod
    def base_method(self):
        """"""
        pass


class Main(Base):
    """"""
    def base_method(self):
        """"""
        return print("I am base_method")

    @abc.abstractmethod
    def main_method(self):
        """"""
        pass


class SubClass(Main):
    """"""
    def main_method(self):
        """"""
        return print("I am main_method")


cases = [Base, Main, SubClass]
for case in cases:
    name = case.__name__
    try:
        instance = case()
        print(f"Instantiated {name}")
    except TypeError as err:
        print(f"Couldn't instantiate {name}: {err}")

subclass = SubClass()
subclass.base_method()
subclass.main_method()