from typing import *

class Test:
    """"""
    def __init__(self, values) -> None:
        self.values = values
        self._count = None

    def __iter__(self) -> Iterator:
        """"""
        self._count = 0
        return self

    def __next__(self):
        """"""
        try:
            this = self.values[self._count]
            self._count += 1
            return this
        except IndexError:
            raise StopIteration

tester = Test([1, 3, 6, 77, 909])
new = [t + 2 for t in tester]
print(new)
