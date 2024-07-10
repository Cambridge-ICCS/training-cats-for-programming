from typing import TypeVar, Callable
A = TypeVar('A')
B = TypeVar('B')

# list : Type -> Type

# Apply a function to every element in a list
def fmap(f : Callable[[A], B], xs : list[A]) -> list[B]:
  return list(map(f, xs))
  # return [f(x) for x in xs]

def fmapAlt(f : Callable[[A], B]) -> Callable[[list[A]], list[B]]:
  return (lambda xs: list(map(f, xs)))

import numpy as np
import numpy.typing as npt

def nparry_fmap(f : Callable[[A], B], xs : npt.NDArray[A]) -> npt.NDArray[B]:
  return np.array([f(x) for x in xs])