# -*- coding: utf-8 -*-
"""10_Iteradores.ipynb


Prof. Fernando Amaral

www.eia.ai

# Iteradores
"""

lista = [1,2,3,4]
iterador = iter(lista)
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))

print(type(iterador))

lista = [1,2,3,4]
iterador = iter(lista)
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))

lista = [1,2,3,4]
for item in lista:
  print(item)

lista = [1,2,3,4]
print(1 not in lista)

class ColecaoNumeros:
  def __init__(self, numero_max):
    self.max = numero_max
  def __iter__(self):
    self.numero_atual = 1
    return self

  def __next__(self):
    if self.numero_atual <= self.max:
      retorno = self.numero_atual
      self.numero_atual +=1
      return retorno
    else:
      raise StopIteration 

colecao = ColecaoNumeros(6)

for item in colecao:
  print(item)

class ColecaoNumeros:
  def __init__(self, numero_max):
    self.max = numero_max
  def __iter__(self):
    self.numero_atual = 1
    return self

  def __next__(self):
    if self.numero_atual <= self.max:
      retorno = self.numero_atual
      self.numero_atual +=1
      return retorno
    else:
      raise StopIteration

colecao = ColecaoNumeros(6)

print(2 in colecao)

class ColecaoNumeros:
  def __init__(self, numero_max):
    self.max = numero_max
  def __iter__(self):
    self.numero_atual = 1
    return self

  def __next__(self):
    if self.numero_atual <= self.max:
      retorno = self.numero_atual
      self.numero_atual +=1
      return retorno
    else:
      raise StopIteration

colecao = ColecaoNumeros(6)
iterador = iter(colecao)
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))

def ancora():
  yield 2
  yield 1
  yield 3

for item in ancora():
  print(item)

def ancora():
  yield 1
  yield 2
  yield 3

print(10 in ancora())
print(2 in ancora())

def ancora():
  yield 1
  yield 2
  yield 3

func = ancora()

print(next(func))
print(next(func))
print(next(func))

for i in range(10):
  print(i)

def meu_range(num):
  local_num = 0
  while local_num < num:
    yield local_num
    local_num += 1

for i in meu_range(10):
  print(i)

lista = ['a','b','c']

for item in enumerate(lista):
  print(item)

lista = ['a','b','c']

for indice, valor in enumerate(lista):
  print(indice, valor)

def anos():
  yield '2000'
  yield '2001'
  yield '2002'
  yield '2003'
  yield '2004'
  yield '2005'        

for indice, valor in enumerate(anos()):
  print(indice, valor)

for valor, indice in  enumerate(range(0,20,5)):
  print(valor, indice)

produtos = [
['carro', '200.000'],
['cadeira','1000'],
['moto','33000'],
['geladeira','2000'],
['armário','15000']
]

for produto, valor in produtos:
  print(produto, valor)

def gen1():
  yield [1,2]
  yield [3,4]
  yield [5,6]

for x,y in gen1():
  print(x,y)

def gen1():
  yield 1
  yield 2
  yield 3

def gen2():
  for i in gen1():
    yield i,'a'
    yield i,'b'
    yield i,'c'

for x,y in gen2():
  print(x,y)

texto1 = 'olá'
print("#".join(texto1))

lista = ['a','b','c','d']
letras = ' '.join(lista)
print(letras)

letras = '-'.join([str(i) for i in range(10)])
print(letras)

def anos():
  for i in range(2020,2030):
    yield str(i)

letras = '-'.join(anos())
print(letras)

lista =  [1,2,3]
iterador = iter(lista)
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))

lista = [1,2,3]

iterator = iter(lista)

while(True):
  try:
    print(next(iterator))
  except:
    break;

# 1 - Crie uma função iterável “meses” que retorne meses. 
# Use um laço for para mostrar os valores.

def meses():
  meses = ['janeiro','fevereiro','março','abril','maio','junho','julho',
           'agosto','setembro','outubro','novembro','dezembro']
  for i in meses:
    yield i

for mes in meses():
  print(mes)

# 2 - Cria uma função iterável que receba uma lista de números e que retorne 
# a cada iteração um item dessa lista multiplicado por dois.

def duplicado(lista):
  for i in lista:
    yield i*2

lista = [1,2,3,4,5]

for i in duplicado(lista):
  print(i)

# 3 - Crie uma classe iterável chamada “Tabuada” que calcule a tabuada da 
# multiplicação do número recebido no construtor. 
# A cada iteração ela deve retornar um resultado da tabuada. 
# Para testar use um laço for.

class Tabuada:
  def __init__(self, num):
    self.num = num
  def __iter__(self):
    self.atual = 0
    return self
  def __next__(self):
    self.atual += 1
    if(self.atual ==11):
      raise StopIteration
    return self.atual * self.num

tabuada_cal = Tabuada(2)

for i in tabuada_cal:
  print(i)

# 4 (Desafio) - Crie uma classe que retorne os fatoriais de um número no 
#  intervalo de X a Y, recebidos por parâmetro no construtor da classe.

class Fatorial:
  def __init__(self,x,y):
    self.x = x
    self.y = y
  
  def __iter__(self):
    self.atual = self.x
    return self
  
  @staticmethod
  def calcula_fatorial(num):
    result = 1
    for i in range(1, num+1):
      result *= i
    return result
  
  def __next__(self):
    if (self.atual == self.y + 1):
      raise StopIteration
    result = Fatorial.calcula_fatorial(self.atual)
    self.atual += 1
    return result

for i in Fatorial(1,10):
  print(i)

# 5 - Utilizando como base o exercício 1, retorne o número que representa o mês 
# e o próprio mês. Faça isso de duas maneiras diferentes 
# (usando enumeradores e a outra usando join).

def meses_enum():
  meses = ['janeiro','fevereiro','março','abril','maio','junho','julho',
           'agosto','setembro','outubro','novembro','dezembro']
  for i in enumerate(meses):
    yield i

for indice, mes in meses_enum():
  print(indice+1, mes)

# 6 - Crie uma função que receba uma lista de frases e junte as mesmas em uma só, 
# separados por ponto final.

def frase(lista):
  return '. '.join(lista) + '.'

textos = ['Olá, sou Carlos','Gosto de Python', 'Trabalho como dev']

print(frase(textos))

