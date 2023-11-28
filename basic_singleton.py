class Singleton:
    """A simple base class for creating singletons."""
    _exists = False
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._exists:
            return cls._instance
        new = super(Singleton, cls).__new__(cls, *args, **kwargs)
        cls._exists = True
        cls._instance = new
        return new

class GuyNamedSteve(Singleton): ...
Steve = GuyNamedSteve()
he = GuyNamedSteve()

if he is Steve:
    print("This is Steve")

class Whoever: ...
Paul = Whoever()
Tom = Whoever()

if Tom is not Paul:
    print("Tom and Paul are different people")


