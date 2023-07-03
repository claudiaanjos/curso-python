import pytest
from Primeiroultimo import primeiroultimo

@pytest.mark.parametrize("nomecompleto,resultado",[("Fernando Amaral","Fernando Amaral"),
                                  ("José Carlos Teixeira","José Teixeira"),
                                  ("Ana Maria da Silva Soares","Ana Soares"),
                                  ("Ana Rosa","Ana Rosa"),("  Maria da Silva Amaral    ","Maria Amaral")])
def test_nomesprimeiroultimo(nomecompleto,resultado):
  assert primeiroultimo(nomecompleto) == resultado
