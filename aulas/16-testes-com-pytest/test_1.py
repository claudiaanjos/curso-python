import pytest

@pytest.mark.primarios
def test_par(retorna_valor):
  assert retorna_valor % 2 == 0

@pytest.mark.primarios
def test_par2(retorna_valor):
  assert retorna_valor % 3 == 0

@pytest.mark.parametrize("num1,num2",[(10,2),(3,2),(3,2),(12,4)])
def test_par3(num1,num2):
  assert num1 % num2 == 0 