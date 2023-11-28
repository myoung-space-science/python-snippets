from typing import *
import numbers
import operator

# See https://docs.python.org/3/library/numbers.html for the motivation behind
# this. This implementation is specifically defined for MyType. I don't know how
# to generalize it. Passing in an arbitrary object (which would replace MyType
# below) doesn't work because the class doesn't know about itself, so I can't
# simply use _operators(MyType, ...) in the body of MyType. It may be possible
# with a metaclass...
def _operators(
    monomorphic: Callable,
    fallback: Callable,
) -> Tuple[Callable, ...]:
    """Generate forward and reverse instances of an operator.

    See https://docs.python.org/3/library/numbers.html for more info.
    """
    def forward(a, b):
        """Define the forward operation."""
        if isinstance(b, MyType):
            return monomorphic(a, b)
        elif isinstance(b, float):
            return fallback(float(a), b)
        elif isinstance(b, complex):
            return fallback(complex(a), b)
        else:
            return NotImplemented
    forward.__name__ = f"__{fallback.__name__}__"
    forward.__doc__ = monomorphic.__doc__
    def reverse(b, a):
        """Define the reverse operation."""
        if isinstance(a, MyType):
            return monomorphic(a, b)
        elif isinstance(a, numbers.Real):
            return fallback(float(a), float(b))
        elif isinstance(a, numbers.Complex):
            return fallback(complex(a), complex(b))
        else:
            return NotImplemented
    reverse.__name__ = f"__{fallback.__name__}__"
    reverse.__doc__ = monomorphic.__doc__
    return forward, reverse


class MyType:
    """A custom class."""
    def __init__(self, value) -> None:
        self.value = value

    def _add(self, other: 'MyType'):
        """Support addition between instances."""
        return self.value + other.value

    __add__, __radd__ = _operators(_add, operator.add)


