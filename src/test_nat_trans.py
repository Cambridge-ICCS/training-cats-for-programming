# Tests for the natural transformation module
import functor
import category
import nat_trans

# Test naturality of promote
def test_promote_natural():
  f = lambda x:x+1
  lhs = nat_trans.promote(f(1))
  rhs = functor.fmap(f)(nat_trans.promote(1))
  assert lhs == rhs

# Test naturality of promote
def test_reverse_natural():
  f = lambda x:x+1
  x = [1,2,3,34,23]
  lhs = nat_trans.reverse(functor.fmap(f)(x))
  rhs = functor.fmap(f)(nat_trans.reverse(x))
  assert lhs == rhs
