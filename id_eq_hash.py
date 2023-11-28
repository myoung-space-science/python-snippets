"""
A note on identity, equality, and hash values.
"""

class Singleton:
    """A simple base class for creating singletons."""

    _exists = False
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._exists:
            return cls._instance
        new = super(Singleton, cls).__new__(cls)
        cls._exists = True
        cls._instance = new
        return new


class C(Singleton):
    def __init__(self, v) -> None:
        self.v = v
    def __hash__(self) -> int:
        return hash(self.v)
    def __eq__(self, other):
        return False

# True, since `C` is a singleton.
print(C(1.1) is C(1.1))
# True, since the initialization arguments are equal.
print(hash(C(1.1)) == hash(C(1.1)))
# False by definition, despite them being identical!
print(C(1.1) == C(1.1))


