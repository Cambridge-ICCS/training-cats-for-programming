from typing import TypeVar, Callable, Generic
A = TypeVar('A', bound=np.generic)
B = TypeVar('B', bound=np.generic)

import numpy as np
import numpy.typing as npt

# Structure to hold an array and a cursor (index) into
# that array
class ArrayComonad(Generic[A]):
    def __init__(self, array : npt.NDArray[A], cursor : int):
        self.array  = array
        self.cursor = cursor

# Extend operation over the array comonad
# which take a function D A -> B
# which computes a stencil in a local context
# and lifts it to work globally, as a function
# D A -> D B to compute over the whole array
def extend(f : Callable[[ArrayComonad[A]], B], w : ArrayComonad[A]) -> ArrayComonad[B]:
    new_array = np.array([f(ArrayComonad(w.array, i)) for i in range(len(w.array))])
    return ArrayComonad(new_array, w.cursor)
