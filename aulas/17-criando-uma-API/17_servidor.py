# -*- coding: utf-8 -*-
"""17.servidor.ipynb



Prof. Fernando Amaral

www.eia.ai

# Criando uma API
"""

!pip install flask_ngrok

!pip install pyngrok

!ngrok authtoken 'XXX'

from flask import jsonify, Flask, request
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)

@app.route('/')
def padrao():
  return "Escolha um dos métodos"

@app.route('/cotacao/')
def cotacao():
  return '5.34'

@app.route('/conversao/<float:val>')  
def conversao(val):
  return str(val * 5.34)

@app.route('/cotacaocompleta', methods=['GET'])
def cotacaocompleta():
  argumentos = request.args
  valor = float(argumentos.get('valor'))
  mes = argumentos.get('mes')

  total = 0.0
  if mes == 'Janeiro':
    total = valor * 5.34
  elif mes == 'Fevereiro':
    total = valor * 5.22
  elif mes == 'Marco':
    total = valor * 5.19

  return str(total)

@app.route('/tabela/')
def tabela():
  return jsonify(Janeiro='5.34',Fevereiro='5.22', Marco='5.33')


app.run()

