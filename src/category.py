from typing import TypeVar, Callable
A = TypeVar('A')
B = TypeVar('B')
C = TypeVar('C')

# Objects: A, B, C, Int, Float, String, etc.
# Morphisms: float : Int -> Float, ....

# Function composition as we know and love it
# f : A -> B
# g : B -> C
# compose(f, g) : A -> C
def compose(f : Callable[[A], B], g : Callable[[B], C]) -> Callable[[A], C]:
    return lambda x: g(f(x))

# Identity function
def id(x : A) -> A:
    return x