# -*- coding: utf-8 -*-
"""17.cliente.ipynb



Prof. Fernando Amaral

www.eia.ai

# Criando uma API
"""

import requests
x = requests.get('http://363e-35-204-114-93.ngrok.io/cotacao/')
print(x.text)
print(x)

import requests
x = requests.get('http://91b3-35-204-114-93.ngrok.io')
print(x.text)

import requests
x = requests.get('http://8589-35-204-114-93.ngrok.io/conversao/200.2')
print(x.text)

import requests
x = requests.get('http://bc6f-35-204-114-93.ngrok.io/cotacaocompleta?valor=200&mes=Marco')
print(x.text)

import requests
x = requests.get('http://ff8e-35-204-114-93.ngrok.io/tabela/')
print(x.text)

