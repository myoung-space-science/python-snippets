from typing import *


class KeyHashError(TypeError):
    pass


class HashedSingleton:
    """Like ``KeyedSingleton``, but with a custom hash check."""
    _instances = {}
    _singletons = []
    def __new__(cls, key: Hashable, *args, **kwargs) -> Any:
        """"""
        try:
            hash(key)
        except TypeError:
            raise KeyHashError("key must be hashable") from None
        if key in cls._instances:
            return cls._instances[key]
        new = super(HashedSingleton, cls).__new__(cls, *args, **kwargs)
        if key in cls._singletons:
            cls._instances[key] = new
        return new
