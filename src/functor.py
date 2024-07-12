from typing import TypeVar, Callable

# List are functors, with:
#   - object mapping:
#      list : Type -> Type

A = TypeVar('A')
B = TypeVar('B')

#    - morphism mapping:
#        lift an   A -> B             function
#        to   a    list(A) -> list(B) function
#      provided by the following function:

def fmap(f : Callable[[A], B]) -> Callable[[list[A]], list[B]]:
  # Apply a function to every element in a list
  return (lambda xs : list(map(f, xs)))


# Alternate version with fmap as a function of arity 2
def fmapAlt(f : Callable[[A], B], xs : list[A]) -> list[B]:
  # Apply a function to every element in a list
  return list(map(f, xs))
  # Alternate implementation
  # return [f(x) for x in xs]

# Numypy arrays are also functos

import numpy as np
import numpy.typing as npt

def nparry_fmap(f : Callable[[A], B], xs : npt.NDArray[A]) -> npt.NDArray[B]:
  return np.array([f(x) for x in xs])