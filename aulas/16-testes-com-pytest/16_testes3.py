# -*- coding: utf-8 -*-
"""15_testes3.ipynb


Prof. Fernando Amaral

www.eia.ai

# Testes
"""

# 1.Crie uma função que receba um nome completo e retorne apenas o primeiro nome 
# e o último sobrenome. Por exemplo: Ana da Silva Rosa deve retornar Ana Rosa. 
# Crie uma função de teste parametrizado que teste a função pelo menos 5 vezes.

from Primeiroultimo import primeiroultimo
print(primeiroultimo("Ana da Silva Rosa"))

!pytest -v

# 2. Crie uma função que receba um nome completo e retorne a abreviatura, 
# contendo a primeira letra de cada nome em maísculo. Por exemplo: Ana Rosa 
# deve retornar AR. Crie uma função de teste parametrizado que teste a função 
# pelo menos 5 vezes e aborte caso ocorra mais de 2 erros.

from abreviatura import abreviatura
print(abreviatura("Marcio antonio Silva"))

!pytest -k test_abreviatura -v --maxfail 2

