from typing import TypeVar, List, Tuple, Union

from heroes.common.iterables import naked

IndexLike = TypeVar('IndexLike', int, List[int], Tuple[int], slice)
IndexLike = Union[int, List[int], Tuple[int], slice]

class AnyIndex:
    """A class to manage representations of indices."""
    def __init__(self, shape: Tuple[int]) -> None:
        self._shape = shape
        self._ndims = len(shape)

    def __getitem__(self, indices: IndexLike) -> Tuple[int, slice]:
        """Convert user indices into integers and slices."""
        wrapped = (indices,) if naked(indices) else indices
        if wrapped == (slice(None),):
            return tuple([slice(None)] * self._ndims)
        if Ellipsis in wrapped:
            return self.expand_ellipsis(wrapped)
        return indices

    def expand_ellipsis(self, user: IndexLike) -> tuple:
        """Expand an `Ellipsis` into one or more `slice` objects."""
        length = self._ndims - len(user) + 1
        start = user.index(Ellipsis)
        return tuple([
            *user[slice(start)],
            *([slice(None)] * length),
            *user[slice(start+length, self._ndims)],
        ])

idx = AnyIndex((3, 4, 5, 6))
print(f"{idx[1, 2, 3]=}")
print(f"{idx[...]=}")
print(f"{idx[:]=}")
print(f"{idx[:, 0, ...]=}")

