import pytest
from abreviatura import abreviatura

@pytest.mark.parametrize("nome,abrev",[("Fernando Amaral","FA"),
                                   ("José Carlos Teixeira","JCT"),
                                  ("Ana Maria da Silva Soares","AMDSS"),
                                  ("Ana Rosa","AR"),("  Maria da Silva Amaral    ","MDSA")])
def test_abreviatura(nome,abrev):
  assert abreviatura(nome) == abrev