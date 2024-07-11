# Tests for the functor module and the fmap operation
import functor
import category

# Test fmap's behaviour on identity functions
def test_identity():
  assert functor.fmap(category.id)([1, 2, 3]) == category.id([1, 2, 3])
  assert functor.fmap(category.id)([]) == category.id([])

# Test fmap's functor composition property
def test_composition():
  f = lambda x: x + 1
  g = lambda x: x * 2
  lhs = functor.fmap(category.compose(f, g))([1, 2, 3])
  rhs = functor.fmap(g)(functor.fmap(f)([1, 2, 3]))
  assert lhs == rhs

####################
# # Test nparray_fmap on identity functions
def test_nparray_identity():
  import numpy as np
  assert np.array_equal(functor.nparry_fmap(lambda x: x, np.array([1, 2, 3])), np.array([1, 2, 3]))
  assert np.array_equal(functor.nparry_fmap(lambda x: x, np.array([])), np.array([]))

# # Test nparray_fmap's functor composition property
def test_nparray_composition():
  import numpy as np
  f = lambda x: x + 1
  g = lambda x: x * 2
  lhs = functor.nparry_fmap(category.compose(f, g), np.array([1, 2, 3]))
  rhs = functor.nparry_fmap(g, functor.nparry_fmap(f, np.array([1, 2, 3])))
  assert np.array_equal(lhs, rhs)
