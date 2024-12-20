<img src="https://plas4sci.github.io/assets/images/iccs-logo.jpg"  width="355" align="left">

<br><br>

# Training material for 'What can abstract mathematics tell us about programming climate models?'

![GitHub](https://img.shields.io/github/license/Cambridge-ICCS/training-cats-for-programming)

This is a short training session that gives an introduction
to basic concepts in [category theory](https://en.wikipedia.org/wiki/Category_theory) and how they can be used to structure common
programming patterns in numerical programming (e.g., in climate
mdoels), informing both testing and optimization. This training
was initially delivered at the ICCS Summer School 2024.

## Contents

The repository contains a number of examples that are then guided through via slides and blackboard.

- [src/category.py] - The analogy of a category of Python types as objects and functions as morphisms;
- [src/functor.py] - Analogy of lists and arrays as functors
- [src/nat_trans.py] - Examples of natural transformations on lists.
- [src/comonad.py] - Analogy of comonads for arrays

Alongside these files are tests based on the expected axioms
from the category theory structures being used as analogies:

- [src/test_functors.py] - Tests functor axioms
- [src/test_nat_functors.py] - Tests naturality axiom

