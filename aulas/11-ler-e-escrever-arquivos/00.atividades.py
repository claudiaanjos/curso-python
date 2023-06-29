# -*- coding: utf-8 -*-
"""11_Arquivos.ipynb



Prof. Fernando Amaral

www.eia.ai

# Arquivos
"""

arquivo = open("exemplo.txt","wt")
arquivo.write("Olá estou escrevendo no arquivo\n")
arquivo.write("Está é a segunda linha do arquivo")
arquivo.close()

lista = ["Ana","Fernando", "João", "Maria"]
arquivo = open("nomes.txt","wt")
for i in lista:
  arquivo.write(i + '\n')
arquivo.close()

texto = "Ana\nFernando\nJoão\nMaria"
arquivo = open("nomes2.txt","wt")
arquivo.writelines(texto)
arquivo.close()

lista = [str(i) + '\n' for i in range(0,20)]
arquivo = open('numeros_3.txt','wt')
arquivo.writelines(lista)
arquivo.close()

with open("exemplo_with.txt","wt") as arquivo:
  arquivo.write("Olá estou escrevendo no arquivo\n")
  arquivo.write("Está é a segunda linha do arquivo")

arquivo = open("exemplo.txt","rt")
lido = arquivo.read()
print(lido)
arquivo.close()

arquivo = open("exemplo.txt","rt")
lido = arquivo.read(10)
print(lido)
arquivo.close()

arquivo = open("exemplo.txt","rt")
primeira_linha = arquivo.readline()
segunda_linha = arquivo.readline()

print(primeira_linha)
print(segunda_linha)

arquivo.close()

arquivo = open("exemplo.txt","rt")
for linha in arquivo:
  print(linha)

arquivo.close()

with open("exemplo.txt","rt") as arquivo:
  for linha in arquivo:
    print(linha)

from os import path
arquivo_existe = path.exists("sample_data/README.md")

if arquivo_existe:
  print("O arquivo existe")
else:
  print("O arquivo não existe")

import os
os.remove('exemplo.txt')

file = open('teste','w')
try:
  file.write('hello world')
finally:
  file.close()

import os
try:
  os.remove("errerere.txt")
except Exception as error:
  print("Ocorreu um erro: " + str(error))

import os
os.mkdir('pasta')

import os
os.rmdir('pasta') #a pasta deve estar vazia

import os
os.mkdir('/content/pasta') #a pasta deve estar vazia

import os
os.mkdir('/content/pasta/pasta') #a pasta deve estar vazia

import os
os.rmdir('/content/pasta')

import os
for i in range(0,10):
  nome_pasta = 'pasta' + str(i)
  try:
    os.mkdir(nome_pasta)
  except:
    pass

  try:
    open(nome_pasta + '/texto.txt','wt').close()
  except:
    pass

import os
for i in range(0,10):
  nome_pasta = 'pasta' + str(i)
  try:
    os.remove(nome_pasta + '/texto.txt')
  except:
    pass

  try:
    os.rmdir(nome_pasta)
  except:
    print("Falha ao excluir a pasta", nome_pasta)

import shutil
for i in range(0,10):
  nome_pasta = 'pasta' + str(i)
  try:
    shutil.rmtree(nome_pasta)
  except:
    print("Falha ao excluir a pasta", nome_pasta)

import os
files = os.listdir("/content/sample_data")
print(files)

import csv
with open("pessoas.csv",'w') as arquivo:
  escritorCsv = csv.writer(arquivo,delimiter=',')
  escritorCsv.writerow(["id","nome", "profissão"])
  escritorCsv.writerow(["1","Fernando", "Eng. de Dados"])
  escritorCsv.writerow(["2","Maria", "Professora"])
  escritorCsv.writerow(["3","Rodrigo", "Dev"])
  escritorCsv.writerow(["4","Irene", "Tec. Informática"])

import csv
linhas = [["id","nome", "profissão"],["1","Fernando", "Eng. de Dados"],
          ["2","Maria", "Professora"],["3","Rodrigo", "Dev"]]

with open('pessoas2.csv','w') as file:
  escritorCsv = csv.writer(file)
  escritorCsv.writerows(linhas)

import csv
with open('pessoas.csv','r') as arquivo:
  leitor = csv.reader(arquivo, delimiter=',')
  for linha in leitor:
    print(linha)

import csv
class Pessoa:
  def __init__(self, id, nome, profissao):
    self.id = id
    self.nome = nome
    self.profissao = profissao
  
  @staticmethod
  def le_pessoas():
    pessoas = []
    with open('pessoas.csv','r') as arquivo:
      leitor = csv.reader(arquivo, delimiter=',')
      for linha in leitor:
        pessoa = Pessoa(linha[0], linha[1], linha[2])
        pessoas.append(pessoa)
    return pessoas
  
  @staticmethod
  def salva_pessoas(*pessoas):
    with open('pessoas.csv','w') as arquivo:
      escritorCsv = csv.writer(arquivo, delimiter=',')
      for pessoa in pessoas:
        escritorCsv.writerow([pessoa.id,pessoa.nome, pessoa.profissao])

pessoa1 = Pessoa(23,"José","Engenheiro")
pessoa2 = Pessoa(12,"Maria","Arquiteta")
pessoa3 = Pessoa(44,"Ana","Cientista de Dados")

Pessoa.salva_pessoas(pessoa1, pessoa2, pessoa3)

lista_pessoa = Pessoa.le_pessoas()

for pessoa in lista_pessoa:
  print(pessoa.id, pessoa.nome, pessoa.profissao)

import json
idades = {
    'Rogério': 20,
    'Maria':34,
    'Pedro':18
}

print(json.dumps(idades,ensure_ascii=False))
print(json.dumps(23))
print(json.dumps(3.14))
print(json.dumps([1,2,3,4,5]))
print(json.dumps(True))
print(json.dumps(None))

import json
DadosPessoas = {
    'Rodrigo' : {
        'CPF': '123456788',
        'Sexo': 'Masculino',
        'Endereco':'Casa 345',
        'Idade': 23
    },
    'Fernando': {
        'CPF': '4545454',
        'Sexo': 'Masculino',
        'Endereco':'Rua y',
        'Idade': 23,
        'Filhos': ["Rodrigo","lucas"]
    }
}

texto = json.dumps(DadosPessoas, indent=4)
print(texto)

with open('exemplo.json','wt') as arquivo:
  arquivo.write(texto)

import json
dicionario = None
with open("exemplo.json",'rt') as arquivo:
  arquivo_lido = arquivo.read()
  dicionario = json.loads(arquivo_lido)

print(dicionario)
print(type(dicionario))
print(dicionario['Rodrigo']['Idade'])

import json

class Carro:
  def __init__(self, nome, potencia):
    self.nome = nome
    self.potencia = potencia

  @staticmethod
  def salva_carros(*carros):
    dicionario = dict()
    for carro in carros:
      dicionario[carro.nome] = carro.potencia
    texto = json.dumps(dicionario, indent=4)
    with open('carros.json','w') as arquivo:
      arquivo.write(texto)
  @staticmethod
  def le_carros():
    lista = []
    texto = None
    with open('carros.json','r') as arquivo:
      texto = arquivo.read()
    dicionario = json.loads(texto)
    for chave in dicionario:
      carro = Carro(chave, dicionario[chave])
      lista.append(carro)
    return lista

carro1 = Carro('Fusca',40)
carro2 = Carro('Nivus', 450)
carro3 = Carro("Focus", 290)

Carro.salva_carros(carro1,carro2,carro3)
lista_carros = Carro.le_carros()

for carro in lista_carros:
  print(carro.nome, carro.potencia)

import xml.etree.ElementTree as xml
import os

no_raiz = xml.Element("DadosPessoais")
no_pessoa = xml.Element("Pessoa", attrib={'Nome':'Rodrigo'})
no_cpf = xml.SubElement(no_pessoa, 'CPF')
no_cpf.text = '123456789'

no_sexo = xml.SubElement(no_pessoa, 'Sexo')
no_sexo.text = 'Masculino'

no_endereco = xml.SubElement(no_pessoa, 'Endereco')
no_endereco.text = 'Rua XYZ'

no_raiz.append(no_pessoa)

arvore = xml.ElementTree(no_raiz)

with open('dados_exemplo.xml','wb') as files:
  arvore.write(files)

import xml.etree.ElementTree as xml
import os

def criaTagPessoa(nome, cpf, sexo, endereco):
  no_pessoa = xml.Element("Pessoa", attrib={'Nome':nome})
  no_cpf = xml.SubElement(no_pessoa, 'CPF')
  no_cpf.text = cpf

  no_sexo = xml.SubElement(no_pessoa, 'Sexo')
  no_sexo.text = sexo

  no_endereco = xml.SubElement(no_pessoa, 'Endereco')
  no_endereco.text = endereco

  return no_pessoa

raiz = xml.Element("DadosPessoais")
pessoa1 = criaTagPessoa("Rodrigo","1234545","Masculino","Rua abc")
pessoa2 = criaTagPessoa("Maria","432324","Feminino","Rua 123")
pessoa3 = criaTagPessoa("Ana","565677","Feminino","Rua 456")

raiz.append(pessoa1)
raiz.append(pessoa2)
raiz.append(pessoa3)

arvore = xml.ElementTree(raiz)

with open('dados_exemplo2.xml','wb') as files:
  arvore.write(files)

import xml.etree.ElementTree as xml
import os

def criaTagPessoa(nome, cpf, sexo, endereco):
  no_pessoa = xml.Element("Pessoa", attrib={'Nome':nome})
  no_cpf = xml.SubElement(no_pessoa, 'CPF')
  no_cpf.text = cpf

  no_sexo = xml.SubElement(no_pessoa, 'Sexo')
  no_sexo.text = sexo

  no_endereco = xml.SubElement(no_pessoa, 'Endereco')
  no_endereco.text = endereco

  return no_pessoa

dados = {
    'Rodrigo' : {
        'CPF': '123456788',
        'Sexo': 'Masculino',
        'Endereco':'Casa 345',
        'Idade': 23
    },
    'Fernando': {
        'CPF': '4545454',
        'Sexo': 'Masculino',
        'Endereco':'Rua y',
        'Idade': 23,
        'Filhos': ["Rodrigo","lucas"]
    },
       'Ana' : {
        'CPF': 'dafdfadf',
        'Sexo': 'Feminino',
        'Endereco':'Casa 345',
        'Idade': 28
    }
}

raiz = xml.Element("DadosPessoais")

for key in dados:
  nome = key
  dados_pessoa = dados[nome]
  cpf = dados_pessoa['CPF']
  sexo = dados_pessoa['Sexo']
  endereco = dados_pessoa['Endereco']
  #idade = dados_pessoa['Idade']
  pessoa = criaTagPessoa(nome, cpf, sexo, endereco)
  if 'Filhos' in dados_pessoa:
    filhos = xml.SubElement(pessoa,'Filhos')
    for filho in dados_pessoa['Filhos']:
      pessoa_filho = xml.SubElement(filhos, 'Pessoa', attrib={'nome': filho})
  raiz.append(pessoa)

arvore = xml.ElementTree(raiz)
with open('dados_pessoais_3.xml','wb') as files:
  arvore.write(files)

import xml.etree.ElementTree as xml
tree = xml.parse("dados_pessoais_3.xml")
root = tree.getroot()
print(root.tag)
for pessoa in root:
  print('  ', pessoa.tag, pessoa.attrib['Nome'])
  for dado in pessoa:
    if (dado.tag == 'Filhos'):
      for filho in dado:
        print('   ', filho.tag, filho.attrib['nome'])
    else:
      print('   ', dado.tag, dado.text)

import xml.etree.ElementTree as xml
import os

class Carro:
  def __init__(self, nome, potencia):
    self.nome = nome
    self.potencia = potencia
  
  @staticmethod
  def salva_carros(*carros):
    raiz = xml.Element("Raiz")

    for carro in carros:
      no_carro = xml.Element('Carro')
      no_nome = xml.SubElement(no_carro, 'Nome')
      no_nome.text = carro.nome

      no_potencia = xml.SubElement(no_carro, 'Potencia')
      no_potencia.text = str(carro.potencia)

      raiz.append(no_carro)
    arvore = xml.ElementTree(raiz)
    with open('carros_exemplo.xml','wb') as files:
      arvore.write(files)

  @staticmethod
  def le_carros():
    lista =[]
    tree = xml.parse('carros_exemplo.xml')
    root = tree.getroot()
    for carro in root:
      nome = None
      potencia = None

      for dado in carro:
        if (dado.tag == 'Nome'):
          nome = dado.text
        if (dado.tag == 'Potencia'):
          potencia = dado.text
      carro = Carro(nome, potencia)
      lista.append(carro)
    return lista

carro1 = Carro('Maverik',330)
carro2 = Carro('Nivus',200)
carro3 = Carro('Monza',180)

Carro.salva_carros(carro1,carro2,carro3)

lista_carros = Carro.le_carros()

for carro in lista_carros:
  print(carro.nome, carro.potencia)

!pip install -U PyYAML

from yaml.loader import Loader
import yaml
dtname = None
with open("config.yaml") as f:
  data = yaml.load(f,Loader=yaml.FullLoader)
  dtname = data['cloud']['provider']
print(dtname)

# 1 - Leia o seguinte arquivo (“exercicio1.txt”) e transforme em uma lista.

lista = []
with open('exercicio1.txt', 'rt') as arquivo:
  for linha in arquivo:
    lista.append(linha)

print(lista)

# 2 - Leia o seguinte arquivo (“exercicio2.txt”), onde cada linha tem um 
# produto e seu valor. Crie uma classe chamada Produto, para representar cada 
# item do arquivo, com nome e valor. Salve todos produtos em uma lista, 
# ao final imprima a lista item por item, mostrando nome e valor.

class Produto:
  def __init__(self, nome, valor):
    self.nome = nome
    self.valor = valor

produtos = []

with open('exercicio2.txt','rt') as arquivo:
  for linha in arquivo:
    indice_separa = linha.index("R$")

    nome = linha[:indice_separa-1]
    valor = linha[indice_separa:len(linha)-1]
    produto = Produto(nome, valor)
    produtos.append(produto)

for produto in produtos:
  print(produto.nome, produto.valor)

# 3 - Escreva num arquivo os números de 0 até 100. Uma linha para cada número.

with open('exercicio3.txt','wt') as arquivo:
  for i in range(0,101):
    arquivo.write(str(i) + '\n')

# 4 - Escreva num arquivo todos números positivos e menores que 100 
# que são divisíveis por 3.

with open('exercicio4.txt','wt') as arquivo:
  for i in range(0,101):
    if i % 3 == 0:
      arquivo.write(str(i) + '\n')

# 5 - Crie um arquivo CSV separado por virgula para guardar informações 
# de sua família. Nesse arquivo deve constar em cada linha o nome de um membro 
# da família e o grau de parentesco(Ex: pai). Escreva 5 membros da 
# família no arquivo. Faça uma função que ira escrever no arquivo, 
# e outra que ira ler o arquivo.

import csv

def escreve_arquivo():
  with open('exercicio5.csv','w') as arquivo:
    escritorCSV = csv.writer(arquivo, delimiter=',')
    escritorCSV.writerow(["Nome","Parentesco"])
    escritorCSV.writerow(["Pedro","Avô"])
    escritorCSV.writerow(["Maria","Avó"])
    escritorCSV.writerow(["José","Pai"])
    escritorCSV.writerow(["Ana","Mãe"])
    escritorCSV.writerow(["Amanda","Filha"])

def le_arquivo():
  with open('exercicio5.csv','r') as arquivo:
    leitor = csv.reader(arquivo, delimiter = ',')
    for linha in leitor:
      print(linha)
escreve_arquivo()
le_arquivo()

# 6 - Faça um programa que leia um arquivo CSV separado por virgula 
# “exercicio6.csv”, onde cada linha tem os seguintes valores 
# (id_empresa, nome_empresa, numero_funcionarios, lucro). 
# Modele uma classe empresa que será usada para guardar os valores do arquivo. 
# Imprima o resultado.

import csv
class Empresa:
  def __init__(self,id,nome, numero_funcionarios, lucro):
    self.id = id
    self.nome = nome
    self.numero_funcionarios = numero_funcionarios
    self.lucro = lucro

empresas = []

with open('exercicio6.csv','r') as arquivo:
  leitor = csv.reader(arquivo, delimiter=',')
  for linha in leitor:
    emp = Empresa(linha[0], linha[1], linha[2], linha[3])
    empresas.append(emp)

for emp in empresas:
  print(emp.id, emp.nome, emp.numero_funcionarios, emp.lucro)

# 7 - Crie uma classe que represente uma pessoa, com nome e idade. 
# Após criar pelo menos 3 instâncias da classe, crie um método que 
# transforme essas instâncias em um dicionário, para pode-las salvar 
# em um arquivo em formato JSON, com nome de “exercicio7.json”. 
# Este método devem ser um tipo estático da classe. 
# Leia o arquivo depois de salvo.

import json
class Pessoa: 
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade

  @staticmethod
  def transforma_dict(*args):
    dicionario = dict()
    for pessoa in args:
      dicionario[pessoa.nome] = pessoa.idade
    return dicionario

pessoa1 = Pessoa("Carlos", 45)
pessoa2 = Pessoa("Maria", 67)
pessoa3 = Pessoa("Pedro", 23)

dictionario_pessoas = Pessoa.transforma_dict(pessoa1,pessoa2,pessoa3)
texto = json.dumps(dictionario_pessoas, indent=4)
print(texto)
with open('exercicio7.json','wt') as arquivo:
  arquivo.write(texto)

# 8 - Com base no exercício anterior, agora crie uma função do tipo da classe 
# que leia o arquivo gerado e retorne as instâncias de classes de 
# volta em uma lista.

import json
class Pessoa: 
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade

  @staticmethod
  def transforma_para_pessoa():
    pessoas = []
    with open('exercicio7.json','rt') as arquivo:
      arquivo_lido = arquivo.read()
      dicionario = json.loads(arquivo_lido)
      for key in dicionario:
        pessoa = Pessoa(key,dicionario[key] )
        pessoas.append(pessoa)
    return pessoas

pessoas = Pessoa.transforma_para_pessoa()

for pessoa in pessoas:
  print(pessoa.nome, pessoa.idade)

# 9 - Crie um arquivo XML, nesse arquivo XML haverá a tag raiz Root. 
# Dentro dessa raiz podem haver varias tags Estado com atributo nome. 
# Dentro de cada estado pode haver a tag Cidade mas nesse caso o valor da tag 
# (texto) devera ser o nome da cidade. 
# Crie um programa que gere esse arquivo com alguns estados e municípios.

import xml.etree.ElementTree as xml
import os

def cria_estado(nome, cidades):
  element_estado = xml.Element("Estado", attrib={'nome' : nome})
  for cidade in cidades:
    elemento_cidade = xml.SubElement(element_estado,'Cidade')
    elemento_cidade.text = cidade
  return element_estado

raiz = xml.Element("Root")
no_estado = cria_estado('Rio Grande do Sul',['Santa Maria','Porto Alegre','Novo Hamburgo'])
no_estado2 = cria_estado('São Paulo',['Sorocaba','Campinas'])
raiz.append(no_estado)
raiz.append(no_estado2)

arvore = xml.ElementTree(raiz)

with open('exercicio9.xml','wb') as files:
  arvore.write(files)

