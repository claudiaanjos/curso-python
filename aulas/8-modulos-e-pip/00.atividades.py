# -*- coding: utf-8 -*-
"""8_Modulos.ipynb


Prof. Fernando Amaral

www.eia.ai

# Módulos
"""

import datetime
print(type(datetime))
data = datetime.datetime(2022,5,15,10,4,5)
print(data)

import datetime as tempo
data = tempo.datetime(2022,5,15,10,4,5)
print(data)

import random
print(random.randrange(10,100))

from random import randrange
print(randrange(10,100))

from random import randrange as num_aleatorio
print(num_aleatorio(10,100))

from random import randrange, randint
print(randrange(10,100))

from random import *
print(randrange(10,100))

import random
dir(random)

import random
dir(random.randrange)

import random
print(random.__name__)
print(random.__file__)
print(random.__doc__)

from random import randrange
print(randrange.__name__)
print(randrange.__doc__)

print(__name__)
print(__doc__)

!pip list

!pip install pmdarima

import pmdarima as arima

!pip uninstall pmdarima

!pip install pmdarima==1.1.1

import teste
dir(teste)

import teste
print(teste.PI)
var = teste.Teste()
teste.MyFunc(10)

from teste import PI
print(PI)

from teste import MyFunc
MyFunc("Teste")

from teste import PI as NUMERO_PI
print(NUMERO_PI)

print(__name__)

import teste
print(teste.__name__)

import teste
print(teste.__file__)

def main():
  print("Aqui inicia o programa")

if (__name__ == '__main__'):
  main()

import sys
if(__name__=='__main__'):
  print("Número de argumentos é ", len(sys.argv))
  print("Argumento são ", sys.argv)

if (__name__=='__main__'):
  exit(1)

import sys
print(sys.__doc__)

print(print.__doc__)

'''
Este é o arquivo principal contendo uma variável chamada euler
e uma função chamada soma
'''

euler = 2.71828

def soma(num1,num2):
  '''Função que soma dois números recebebidos por entrada'''
  return num1 + num2

print(__doc__)
print(soma.__doc__)

def soma(num1,num2):
  '''Função que soma dois números recebebidos por entrada'''
  return num1 + num2

help(soma)

import teste

print(teste.__doc__)
print(teste.Teste.__doc__)
print(teste.MyFunc.__doc__)
help(teste)

# 1 - Importe do modulo random a função randrange e crie um programa que gere 
# um único número aleatório entre 2 e 100. Em seguida diga se esse número é 
# par ou impar.

from random import randrange
numero = randrange(2,100)
resto = numero % 2
if resto == 0:
  print("O número %d é par" % (numero))
else:
  print("O número %d é impar" % (numero))

# 2 - Da mesma forma que o exercício anterior, gere a soma de 100 números 
# aleatórios e mostre o resultado final.

from random import randrange
soma = 0

for i in range(0,100):
  soma += randrange(1,100)

print(soma)

# 3 - Crie um modulo que dispõem de duas funções, uma que subtrai dois números 
# e outra que soma dois números. Importe essas funções e as use. 
# Não se esqueça de gerar a documentação destas funções e do modulo e mostrar 
# na saída de seu programa. Chame o modulo de “calc_python”

import calc_python
#print(calc_python.__doc__)
#help(calc_python)
#print(calc_python.soma.__doc__)
resultado = calc_python.soma(10,20)
print(resultado)

# 4 - Cria um modulo para retornar uma lista de números aleatórios. 
# Esse modulo deve ter a seguinte funcionalidade:
# - Uma função que retorna uma lista de números randômicos chamada de 
# get_random_lista(inicial, final, tam), onde “inicial” é o número mínimo 
# que pode aparecer na lista e “final” é o número máximo que pode aparecer. 
# Por fim “tam” deve ser o número de elementos na lista. 
# Chame o modulo de “meu_random”

from meu_random import get_random_lista
print(get_random_lista(1,100,10))

# 5 - Crie um programa que tenha a entrada na função e modulo main(). 
# Ele deve receber dois números via parâmetro do programa e mostrar sua soma. 
# Mas com uma condição: Verificar se possui dois parâmetros de entrada. 
# Caso contrario parar a execução do programa e avisar qual o problema.

import sys

if(__name__== '__main__'):
  if len(sys.argv) !=3:
    print("Número de argumentos incorretos")
    sys.exit(1)
  numero1 = float(sys.argv[1])
  numero2 = float(sys.argv[2])
  print(numero1 + numero2)

!python3 teste_programa.py 10 20

