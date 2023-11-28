def update(method):
    """"""
    def wrapper(obj, *args, **kwargs):
        if isinstance(obj, A):
            print(obj.info)
        print(args)
        print(kwargs)
        return
    return wrapper


class A:
    def __init__(self, info) -> None:
        self.info = info
    @update
    def add(self, x, y):
        return x + y


a = A({'message': 'Hello'})
r = a.add(2, 3)
print(r)
