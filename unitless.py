from typing import Any


class Unitless:
    """A singleton object representing the unitless state."""
    _instance = None
    def __new__(cls) -> Any:
        if cls._instance is None:
            cls._instance = super(Unitless, cls).__new__(cls)
        return cls._instance
unitless = Unitless()


