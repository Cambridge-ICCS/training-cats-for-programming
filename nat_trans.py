from typing import TypeVar, Callable
A = TypeVar('A')

def promote(x : A) -> list[A]:
    return [x]

def reverse(x : list[A]) -> list[A]:
    y = x.copy()
    y.reverse()
    return (y)

# A version of reverse which is not natural
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



