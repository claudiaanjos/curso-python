# -*- coding: utf-8 -*-
"""15_Testes.ipynb



Prof. Fernando Amaral

www.eia.ai

# Testes
"""

import pytest

!pytest

!pytest -v

!pytest test_2.py -v

!pytest -k im -v

!pytest -m primarios -v

!pytest -m primarios -v

!pytest -k test_par3 -v

!pytest -k test_par3 -v --maxfail 1

!pytest -k test_par3 -v --junitxml="resultadoteste.xml"

