from typing import TypeVar, Callable
A = TypeVar('A')

# A 'natural transformation' from the identity functor
# to the list functor.
def promote(x : A) -> list[A]:
    return [x]

# A natural transformation from a list functor to a list
# functor
def reverse(x : list[A]) -> list[A]:
    y = x.copy()
    y.reverse()
    return (y)

# A version of reverse which is _not_ natural
# because it uses global state to change its
# behaviour
g = 0
def reverse_bad(x : list[A]) -> list[A]:
    global g
    g += 1
    y = x.copy()
    for _i in range(1, g):
      y.reverse()
    return (y)



