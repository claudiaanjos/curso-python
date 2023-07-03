import pytest
from primo import primo

@pytest.mark.parametrize("num,res",[(2,True),(6,False),(13,True),(-1,False)])
def test_primo(num,res):
  assert primo(num) == res