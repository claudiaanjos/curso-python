# -*- coding: utf-8 -*-
"""15_Teste2.ipynb



Prof. Fernando Amaral

www.eia.ai

# Testes
"""

from primo import primo
print(primo(7))
print(primo(8))

!pytest -v

from primo import primo
print(primo(2))
print(primo(-1))
print(primo(7))
print(primo(8))

!pytest -v

