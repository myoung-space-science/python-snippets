from typing import *


class KeyedSingleton:
    """For creating singletons only in certain cases."""
    _instances = {}
    _singletons = []
    def __new__(cls, key: str) -> Any:
        """"""
        if key in cls._instances:
            return cls._instances[key]
        new = super(KeyedSingleton, cls).__new__(cls)
        if key in cls._singletons:
            cls._instances[key] = new
        return new


class TestClass(KeyedSingleton):
    """"""
    _singletons = ['special', 'only']


old_special = TestClass('special')
old_only = TestClass('only')
old_other = TestClass('other')

new_special = TestClass('special')
new_only = TestClass('only')
new_other = TestClass('other')

assert new_special is old_special
assert new_only is old_only
assert old_special is not old_only
assert new_special is not new_only
assert new_other is not old_other

