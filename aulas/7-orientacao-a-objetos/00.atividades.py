# -*- coding: utf-8 -*-
"""7_OrientacaoObjetos.ipynb

Prof. Fernando Amaral

www.eia.ai

# Orientação a Objetos
"""

class Teste:
  pass

minha_classe = Teste()
print(type(minha_classe))

class NossaClasse:
  def __init__(self):
      print("Eu existo")

var = NossaClasse()
print(type(var))

class Pessoa:
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade  = idade
    print("Pessoa com nome %s e idade %d criada" % (nome,idade))

pessoa1 = Pessoa('Rodrigo',34)
pessoa2 = Pessoa("Lucas",21)

print(pessoa1.nome)
print(pessoa2.idade)

class Pessoa:
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade  = idade
    print("Pessoa com nome %s e idade %d criada" % (nome,idade))

pessoa1 = Pessoa('Rodrigo',34)

pessoa1.nome = "Marcelo"
print(pessoa1.nome)

class Pessoa:
  especie = "Homo Sapiens"
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade  = idade
    print("Pessoa com nome %s e idade %d criada" % (nome,idade))

pessoa1 = Pessoa('Rodrigo',34)
pessoa2 = Pessoa("Lucas",21)

print(pessoa1.especie)
print(pessoa2.especie)

class Pessoa:
  especie = "Homo Sapiens"
  num_pessoas = 0
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade  = idade
    Pessoa.num_pessoas += 1

pessoa1 = Pessoa('Rodrigo',34)
print(Pessoa.num_pessoas)
pessoa2 = Pessoa("Lucas",21)
print(Pessoa.num_pessoas)
pessoa3 = Pessoa("Maria",22)
print(Pessoa.num_pessoas)

class Pessoa:
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade  = idade
  def print_nome(self):
    print("Meu nome é %s " % (self.nome))

pessoa1 = Pessoa("Rodrigo","34")
pessoa2 = Pessoa("Maria","22")

pessoa1.print_nome()
pessoa2.print_nome()

class Pessoa:
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade  = idade
  
  def print_string(self, nome):
    print("Meu nome é %s " % (nome))
  
  def print_nome(self):
    self.print_string(self.nome)

pessoa1 = Pessoa("Rodrigo","34")
pessoa2 = Pessoa("Maria","22")

pessoa1.print_nome()
pessoa2.print_nome()

class Pessoa:
  def __init__(self, nome):
    self.nome = nome
  def insere_idade(self,idade):
    self.idade = idade

rodrigo = Pessoa("Rodrigo")
rodrigo.insere_idade(34)

print(rodrigo.idade)

class Tipo1:
  def __init__(self, outra_classe):
    self.outra = outra_classe

class Tipo2:
  numero = 10

classe2 = Tipo2()
classe1 = Tipo1(classe2)

print(classe1.outra.numero)

class Exemplo:
  def __init__(self):
    pass

lista = []
ex1 = Exemplo
ex2 = Exemplo

lista.append(ex1)
lista.append(ex2)

print(lista[1])

class FormaGeometrica:
  def __init__(self,altura,largura):
    self.altura = altura
    self.largura = largura

class Quadrado(FormaGeometrica):
  pass

class Triangulo(FormaGeometrica):
  pass

quadrado = Quadrado(100,50)
triangulo = Triangulo(10,30)

print(quadrado.altura)
print(triangulo.largura)

class FormaGeometrica:
  def __init__(self,altura,largura):
    self.altura = altura
    self.largura = largura

class Quadrado(FormaGeometrica):
  lado = 10

class Triangulo(FormaGeometrica):
  angulo = 30

quadrado = Quadrado(100,50)
triangulo = Triangulo(10,30)

print(quadrado.altura)
print(quadrado.largura)
print(quadrado.lado)

print(triangulo.angulo)

class FormaGeometrica:
  def __init__(self,altura,largura):
    self.altura = altura
    self.largura = largura
  def funcao_herdada(self):
    print("Sou herdado")

class Quadrado(FormaGeometrica):
  pass

class Triangulo(FormaGeometrica):
  pass

quadrado = Quadrado(100,50)
triangulo = Triangulo(10,30)

quadrado.funcao_herdada()
triangulo.funcao_herdada()

class ClassePai:
  def __init__(self):
    print("sou a classe pai")

class ClasseFilha1(ClassePai):
  def __init__(self):
    print("sou a classe filha 1")

class ClasseFilha2(ClassePai):
  def __init__(self):
    print("sou a classe filha 2")

pai = ClassePai()
filha1 = ClasseFilha1()
filha2 = ClasseFilha2()

class FormaGeometrica:
  def __init__(self, altura, largura):
    self.altura = altura
    self.largura = largura

class Quadrado(FormaGeometrica):
  def __init__(self,altura, largura, atributo_quadrado):
    FormaGeometrica.__init__(self, altura, largura)
    self.atributo_quadrado = atributo_quadrado

class Triangulo(FormaGeometrica):
  def __init__(self,altura, largura, atributo_triangulo):
    FormaGeometrica.__init__(self, altura, largura)
    self.atributo_triangulo = atributo_triangulo

quadrado = Quadrado(100,200, 'quadrado')
triangulo = Triangulo(100,200, 'triangulo')

print(quadrado.altura)
print(quadrado.atributo_quadrado)

print(triangulo.largura)
print(triangulo.atributo_triangulo)

class FormaGeometrica:
  def __init__(self,altura,largura):
    self.altura = altura
    self.largura = largura
  def calcula_area(self):
    pass

class Quadrado(FormaGeometrica):
  def calcula_area(self):
    return self.altura * self.largura

class Triangulo(FormaGeometrica):
  def calcula_area(self):
    return (self.altura * self.largura)/2

quadrado = Quadrado(200,200)
triangulo = Triangulo(200,200)

print(quadrado.calcula_area())
print(triangulo.calcula_area())

class Veiculo:
  def __init__(self, marcha):
    self.marcha = marcha
  def aumenta_marcha(self):
    self.marcha +=1
    self.marcha = min(self.marcha,5)
  def diminui_marcha(self):
    self.marcha -= 1
    self.marcha = max(self.marcha,1)

class Palio(Veiculo):
  def __init__(self, marcha):
    Veiculo.__init__(self,marcha)

class EcoSport(Veiculo):
  def __init__(self, marcha):
    Veiculo.__init__(self,marcha)
  def aumenta_marcha(self):
    self.marcha +=1
    self.marcha = min(self.marcha,6)

carro = EcoSport(5)
carro.aumenta_marcha()
print(carro.marcha)
carro.aumenta_marcha()
print(carro.marcha)

class Base1:
  def __init__(self, atributo1):
    self.atributo1 = atributo1
  def Base1_print(self):
    print("Base1")

class Base2:
  def __init__(self, atributo2):
    self.atributo2 = atributo2
  def Base2_print(self):
    print("Base2")

class MinhaClasse(Base1,Base2):
  def __init__(self):
    Base1.__init__(self,10)
    Base2.__init__(self,20)

var = MinhaClasse()
print(var.atributo1)    
print(var.atributo2)    
var.Base1_print()
var.Base2_print()

class Segredo:
  def __init__(self):
    self.__segredo = 'Senha123'

seg = Segredo()
print(seg.__segredo)

class Segredo:
  def __init__(self):
    self.__segredo = 'Senha123'

  def __printa_segredo(self):
    print(self.__segredo)

  def printa_segredo(self):
    self.__printa_segredo()
  

seg = Segredo()
seg.__printa_segredo()

class Base:
  def __base__privada(self):
    print('Pertenco somente a base')
  def _baseprotegida(self):
    print("Pertenco a Base e a quem me herdar")

class Filha(Base):
  def acessa_protegida(self):
    self._baseprotegida()

filha = Filha()
filha.acessa_protegida()
filha._baseprotegida()

class Veiculo:
  def __init__(self):
    self.__marcha =1
  def aumenta_marcha(self):
    self.__marcha +=1
    self.__marcha = min(self.__marcha,5)
  def diminui_marcha(self):
    self.__marcha -=1
    self.__marcha = max(self.__marcha,1)
  def marcha_atual(self):
    return self.__marcha

carro = Veiculo()
carro.aumenta_marcha()
carro.aumenta_marcha()
carro.aumenta_marcha()
carro.aumenta_marcha()
carro.aumenta_marcha()
print(carro.marcha_atual())  
carro.diminui_marcha() 
carro.diminui_marcha() 
print(carro.marcha_atual()) 
carro.diminui_marcha() 
carro.diminui_marcha() 
print(carro.marcha_atual()) 
carro.diminui_marcha() 
print(carro.marcha_atual())

class Pessoa:
  def __init__(self, nome):
    self.__nome = nome

  def get_nome(self):
    print("pegando nome")
    return self.__nome

  nome = property(get_nome) 

instancia = Pessoa("Maria")
print(instancia.nome)

class Pessoa:
  def __init__(self, nome):
    self.__nome = nome

  def get_nome(self):
    print("pegando nome")
    return self.__nome
  
  def set_nome(self,nome):
    if len(nome)> 0:
      print("Setando nome") 
      self.__nome = nome

  nome = property(get_nome, set_nome) 

instancia = Pessoa("Maria")
print(instancia.nome)
instancia.nome = "Marcos"
print(instancia.nome)

class Pessoa:
  def __init__(self, nome):
    self.__nome = nome
  
  def set_nome(self,nome):
    if len(nome)> 0:
      print("Setando nome") 
      self.__nome = nome

  nome = property(fset = set_nome) 

instancia = Pessoa("Maria")
instancia.nome = "Marcos"
#fset, fget, fdel

class Natural:
  def __init__(self,numero):
    self.__numero = numero 
  @property
  def numero(self):
    print("pegando numero")
    return self.__numero
  @numero.setter
  def numero(self, value):
    if value >=0:
      self.__numero = value
      print('setando numero para ', value)

numero = Natural(10)
numero.numero = -10
print(numero.numero)

class Pessoa:
  def __init__(self, nome):
    self.__nome = nome
  @property
  def nome(self):
    return self.__nome.capitalize()
  @nome.setter
  def nome(self, value):
    if (len(value)!=0):
      self.__nome = value

pessoa = Pessoa("rodrigo")
print(pessoa.nome)
pessoa.nome = 'fernando'
print(pessoa.nome)
pessoa.nome = ''
print(pessoa.nome)

class Teste:
  def __init__(self,gasolina):
    pass
  @classmethod
  def class_method(cls):
    print(cls)
  @staticmethod
  def static_method():
    print("static method")

Teste.class_method()
Teste.static_method()

testando = Teste("aditivada")
testando.class_method()

class Veiculo:
  def __init__(self,nome, gasolina, potencia):
    self.nome = nome
    self.gasolina = gasolina
    self.potencia = potencia    
  @classmethod
  def cria_carro(cls):
    return cls('carro','comum',200)
  @classmethod
  def cria_trator(cls):
    return cls('trator','aditivada',500)

veiculo1 = Veiculo.cria_carro()
veiculo2 = Veiculo.cria_trator()

print(veiculo1.nome)
print(veiculo1.gasolina)
print(veiculo1.potencia)
print(veiculo2.nome)

class Veiculo:
  __numero_veiculos = 0
  def __init__(self,nome, gasolina, potencia):
    self.nome = nome
    self.gasolina = gasolina
    self.potencia = potencia    
    Veiculo.__numero_veiculos += 1
  @staticmethod
  def get_numero_carros():
    return Veiculo.__numero_veiculos

carro =  Veiculo("carro","aditivada",200)
carro2 =  Veiculo("caminhao","aditivada",1000)
print(Veiculo.get_numero_carros())
print(carro.get_numero_carros())

lst1 = 10
lst2 = lst1
lst2 = 20
print(lst1)

lst1 = [1,2,3]
lst2 = lst1
lst2.append(10)
print(lst1)

class Classe:
  def __init__(self):
    self.num = 10

class1 = Classe()
class2 = class1
class1.num = 20
print(class2.num)

from copy import copy
lst1 = [1,2,3]
lst2 = copy(lst1)
lst2.append(10)
print(lst1)

from copy import copy
class Classe:
  def __init__(self):
    self.num = 10

class1 = Classe()
class2 = copy(class1)
class1.num = 20
print(class2.num)

class Classe:
  def __init__(self):
    self.num = 10

class1 = Classe()
class2 = class1
print(class2 is class1)

from copy import copy
class Classe:
  def __init__(self):
    self.num = 10

class1 = Classe()
class2 = copy(class1)
print(class2 is class1)

numero = 10
del numero
print(numero)

arr = [1,2,3]
del arr
print(arr)

arr = [1,2,3]
del arr[0]
print(arr)

class Teste:
  def __init__(self):
    pass

varivel = Teste()
del variavel

class Teste:
  def __init__(self, num):
    self.num = num

variavel = Teste(10)
print(variavel.num)

del variavel.num

print(variavel.num)

class Teste:
  def __init__(self):
    self.lista = [1,2,3]
  def __del__(self):
    print("Fui deletado")

teste = Teste()
del teste

class Pessoa:
  def __init__(self, nome):
    self.__nome = nome

  def get_nome(self):
    print("pegando nome")
    return self.__nome
  
  def set_nome(self, nome):
    print("setando nome")
    self.__nome = nome

  def del_nome(self):
    print("deletando nome")
    del self.__nome

  nome = property(get_nome, set_nome, del_nome)

instancia = Pessoa("Larissa")

del instancia.nome

class Pessoa:
  def __init__(self, nome):
    self.__nome = nome
  
  @property
  def nome(self):
    return self
  
  @nome.deleter
  def nome(self):
    print("deletando nome")
    del self.__nome

instancia = Pessoa("Larissa")
del instancia.nome

e_inteiro = isinstance(5, int)
print(e_inteiro)

e_inteiro = isinstance(5, (int, float, str))
print(e_inteiro)

class Base:
  def __init__(self):
    pass

classe = Base()
e_base = isinstance(classe, Base)
print(e_base)

class Base:
  def __init__(self):
    pass

class Herdeiro(Base):
  def __init__(self):
    pass

classe = Herdeiro()

e_base = isinstance(classe, Base)
e_herdeiro = isinstance(classe, Herdeiro)

print(e_base)
print(e_herdeiro)

class Base:
  def __init__(self):
    pass

class Herdeiro(Base):
  def __init__(self):
    pass

classe = Base()

e_base = isinstance(classe, Base)
e_herdeiro = isinstance(classe, Herdeiro)

print(e_base)
print(e_herdeiro)

class Base:
  def __init__(self):
    pass

class Herdeiro(Base):
  def __init__(self):
    pass


e_base = issubclass(Base, Herdeiro)
e_herdeiro = issubclass(Herdeiro, Base)

print(e_base)
print(e_herdeiro)

def soma(num1, num2):
  if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
    return num1 + num2
  else:
    return None

print(soma(1,34.3))
print(soma(True, "texto"))

class Veiculo:
  def __init__(self):
    pass
  def acelera(self):
    pass

class Moto(Veiculo):
  def __init__(self):
    pass

class Carro(Veiculo):
  def __init__(self):
    pass
  def re(self):
    print("Dando ré")

def faz_re(var):
  if isinstance(var, Carro):
    var.re()
  else:
    print("não tem ré")

motinho = Moto()
carrinho = Carro()

faz_re(motinho)
faz_re(carrinho)

class Lista():
  def __init__(self):
    pass

  def __enter__(self):
    print("Memória Iniciada")
    self.lista = [ i for i in range(0,10)]
    return self.lista

  def __exit__(self, *args, **kwargs):
    print("Memória Liberada")
    del self.lista 

with Lista() as temp_lista:
  for i in temp_lista:
    print(i)

print("Aqui o objeto já não existe mais")

class Lista():
  def __init__(self):
    pass

  def __enter__(self):
    print("Memória Iniciada")
    self.lista = [ i for i in range(0,10)]
    return self.lista

  def __exit__(self, *args, **kwargs):
    print("Memória Liberada")
    del self.lista 

minha_lista = Lista()

with minha_lista as temp_lista:
  for i in temp_lista:
    print(i)

print("Aqui o objeto já não existe mais")

class MeuNumero:
  def __init__(self,numero):
    self.numero = numero
  def __add__(self, outro):
    return self.numero + outro.numero

num1 = MeuNumero(10)
num2 = MeuNumero(20.5)

print(num1 + num2)

class MeuNumero:
  def __init__(self,numero):
    self.numero = numero
  def __add__(self, outro):
    soma = self.numero + outro.numero
    return MeuNumero(soma)

num1 = MeuNumero(10)
num2 = MeuNumero(20.5)
num3 = num1 + num2
print(num3.numero)

class MeuNumero:
  def __init__(self,numero):
    self.numero = numero
  def __sub__(self, outro):
    return self.numero - outro.numero

num1 = MeuNumero(20.5)
num2 = MeuNumero(10)

print(num1 - num2)

# 1 - Crie uma classe para representar um carro. Ele deve ter um atributo que 
# diga sua potência em cavalos. Outro atributo deve dizer quanto de gasolina 
# por quilômetros ele consome. Cria duas instâncias e mostre os valores.

class Carro:
  def __init__(self, potencia, alcance):
    self.potencia = potencia
    self.alcance = alcance

carro1 = Carro(100,200)
carro2 = Carro(200,350.5)

print("Potência do carro 1: ", carro1.potencia, " cavalos")
print("Alcance do carro 1: ", carro1.alcance, " Km/l")

print("Potência do carro 2: ", carro2.potencia, " cavalos")
print("Alcance do carro 2: ", carro2.alcance, " Km/l")

# 2 - Cria uma classe que represente uma pessoa. Ela deve possuir um nome, 
# CPF e um dependente, onde o dependente é outra pessoa. 
# Dependente não é obrigatório. Crie duas instâncias: pai e filho, 
# e imprima as saídas.

class Pessoa:
  def __init__(self, nome, cpf, dependente=None):
    self.nome = nome
    self.cpf = cpf
    self.dependente = dependente

filho = Pessoa("Rodrigo","200.300.400-45")
pai = Pessoa("Fernando","100.200.300-34",filho)

print("Nome ", filho.nome, " CPF: ", filho.cpf, " Dependente: " , filho.dependente )
print("Nome ", pai.nome, " CPF: ", pai.cpf, " Dependente: " , pai.dependente.nome )

# 3 - Crie uma classe base que represente um veículo. 
# Os atributos devem ser peso do veiculo, número de rodas e potência. 
# Em seguida crie três classes que herdam esse veículo: ônibus, carro e moto. 
# Crie uma instância de cada tipo e imprima as instâncias

class Veiculo:
   def __init__(self, peso, potencia, rodas):
     self.peso = peso
     self.potencia = potencia
     self.rodas = rodas

class Moto(Veiculo):
  def __init__(self, peso, potencia, rodas):
    Veiculo.__init__(self, peso, potencia, rodas)

class Carro(Veiculo):
  def __init__(self, peso, potencia, rodas):
    Veiculo.__init__(self, peso, potencia, rodas)

class Onibus(Veiculo):
  def __init__(self, peso, potencia, rodas):
    Veiculo.__init__(self, peso, potencia, rodas)

onibus = Onibus(1000,400, 6)
carro = Carro(300, 100, 4)
moto = Moto(100,50,2)

print("Onibus, Peso: ", onibus.peso, " Potência: ", onibus.potencia, " Rodas ", onibus.rodas)
print("Carro, Peso: ", carro.peso, " Potência: ", carro.potencia, " Rodas ", carro.rodas)
print("Moto, Peso: ", moto.peso, " Potência: ", moto.potencia, " Rodas ", moto.rodas)

# 4 - Baseado no exercício anterior, cria uma função na classe base que diga 
# a distância percorrida. Vamos supor que esse valor é dado pela peso do veículo
# dividido pela potência do veículo vezes mil. Crie uma moto, carro e um ônibus. 
# Mostre esses valores.

class Veiculo:
   def __init__(self, peso, potencia, rodas):
     self.peso = peso
     self.potencia = potencia
     self.rodas = rodas
   def distancia_percorrida(self):
     return (self.potencia / self.peso ) * 1000

class Moto(Veiculo):
  def __init__(self, peso, potencia, rodas):
    Veiculo.__init__(self, peso, potencia, rodas)

class Carro(Veiculo):
  def __init__(self, peso, potencia, rodas):
    Veiculo.__init__(self, peso, potencia, rodas)

class Onibus(Veiculo):
  def __init__(self, peso, potencia, rodas):
    Veiculo.__init__(self, peso, potencia, rodas)

onibus = Onibus(1000,400, 6)
carro = Carro(300, 100, 4)
moto = Moto(100,50,2)

print("Distancia Percorrida do onibus: ", onibus.distancia_percorrida())
print("Distancia Percorrida do carro: ", carro.distancia_percorrida())
print("Distancia Percorrida da moto: ", moto.distancia_percorrida())

# 5 - Baseado no exercício anterior, crie os operador '>' e '<' para dizer qual 
# veículo é mais potente. Compare um de cada tipo.
# Observação, sobrescreva os métodos __lt__ e __gt__

class Veiculo:
   def __init__(self, peso, potencia, rodas):
     self.peso = peso
     self.potencia = potencia
     self.rodas = rodas
   def __lt__(self,outro) :
     return self.potencia < outro.potencia
   def __gt__(self, outro):
     return self.potencia > outro.potencia

class Moto(Veiculo):
  def __init__(self, peso, potencia, rodas):
    Veiculo.__init__(self, peso, potencia, rodas)

class Carro(Veiculo):
  def __init__(self, peso, potencia, rodas):
    Veiculo.__init__(self, peso, potencia, rodas)

class Onibus(Veiculo):
  def __init__(self, peso, potencia, rodas):
    Veiculo.__init__(self, peso, potencia, rodas)

onibus = Onibus(1000,400, 6)
carro = Carro(300, 100, 4)
moto = Moto(100,50,2)

print(onibus > carro)
print(onibus < moto)
print(moto > carro)

# 6 - Cria uma classe que represente um número negativo, 
# use propriedades (@property)  para controlar o valor guardado pela classe, 
# sem deixar que ele fique positivo (0 pode). Além disso crie alguns operadores 
# para comparação e de subtração. Cuide para que nenhum valor positivo surja.

class NumeroNegativo:
  def __init__(self, numero):
    self.__numero =0
    self.numero = numero 
  @property
  def numero(self):
    return self.__numero
  @numero.setter
  def numero(self, value):
    if value <= 0:
      self.__numero = value
  def __lt__(self, outro):
    return self.__numero < outro.__numero
  def __gt__(self,outro):
    return self.numero > outro.__numero
  def __sub__(self, outro):
    sub = self.__numero - outro.__numero
    if sub > 0:
      sub = 0
    return sub

num1 = NumeroNegativo(-10)
num2 = NumeroNegativo(-20)
num3 = NumeroNegativo(10)

print(num1.numero, num2.numero, num3.numero)
print(num1 > num2)
print(num1 - num2)

# 7 - Crie uma função  que diga se um objeto é um primitivo 
# do Python, informando que é sempre passado valor Ex: [int, float, str, bool], 
# ou se é um objeto passado por referência

def testa_objeto(obj):
  if isinstance(obj, (int, float, str, bool)):
    print("Objeto por valor")
  else:
    print("Objeto por referência")

class Objeto:
  def __init__(self):
    pass

obj = Objeto()
valor = 3

testa_objeto(obj)
testa_objeto(valor)

