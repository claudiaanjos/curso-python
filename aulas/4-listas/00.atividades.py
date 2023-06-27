# -*- coding: utf-8 -*-
"""4_Listas.ipynb



Prof. Fernando Amaral

www.eia.ai

# Listas
## List
"""

array = []
array = list()

array_numeros = [1,2,3]
array_floats = [56.3, -2.2, 0.5]
array_str = ["A","B","C"]
array_misto = [ 2,2.3,"ABC"]
print(array)
print(array_numeros)
print(array_floats)
print(array_str)
print(array_misto)

color = [1,2,
         3,
         4,5]
print(color)

array = list([1,2,3])
print(array)
primeiro_elemento = array[0]
print(primeiro_elemento)
array[0] = 20
primeiro_elemento = array[0]
print(primeiro_elemento)
print(array[-1])
print(array)

array = [1, "texto", 3]
print(array[1:3])

array = [10,2,3]
print(array)
array.append(2)
print(array)
array.insert(2,"4")
print(array)

array  = [10,2,3,20,"3"]
array.remove(10)
print(array)
array.pop(2)
print(array)

print(len(array))

array.clear()
print(array)

array = [1, 'teste', 1.3, True]
print(1 in array)
print(False not in array)

lista = [5,6,7,2,3,4,7]
teste = lista.count(7)
print(teste)

lista = [5,6,7,2,3,4,7]
pos = lista.index(5)
print(pos)

array1 = [1,2,3]
array2 = [3,4,5]
soma = array1 + array2
print(soma)

array1 = [1,2,3]
mult = array1 * 3
print(mult)

numeros = ["um","dois","três"]
x,y,_ = numeros
print(x)
print(y)

cores = ["azul","preto","amarelo"]
for x in cores:
  print(x)

cores = ["azul","preto","amarelo"]
for i in range(0,len(cores)):
  print(cores[i])

cores = ["azul","preto","amarelo"]
indice = 0
while (indice < len(cores)):
  print(cores[indice])
  indice += 1

lista = [[1,2,3] ,[4,5,6] ]
primeira_lista =  lista[0]
segunda_lista = lista[1]
print(primeira_lista)
print(segunda_lista)
primeiro_elemento_primeira_lista = lista[1][1]
print(primeiro_elemento_primeira_lista)

"""Prof. Fernando Amaral

www.eia.ai

# Set
"""

lista_set = {}
lista2_set = {1,2,3}
lista3_set = set({1,2,3})
print(lista_set)
print(lista2_set)
print(lista3_set)

lista2_set = {1,2,3}
lista2_set[0]

lista2_set = {1,2,3}
lista2_set[0] = 2

lista_set = {1,2,3}
lista_set.add(5)
print(lista_set)
lista_set.remove(1)
print(lista_set)

lista_set = {1,2,3,4,2}
lista_set.add(1)
print(lista_set)

lista_set = {1,2,3,4}
lista_set.clear()
print(lista_set)

lista_set = {1,2,3,4}
print(len(lista_set))

lista_set = {1,2,3,4}
print(5 in lista_set)

lista_set = {0,2,3,'4', False, 6.1}
for item in lista_set:
  print(item)

set1 = {1,2,3}
set2 = {1,2,3,4}
set_unido = set1.union(set2)
print(set_unido)

set1 = {1,2,3}
set2 = {3,4,5,6}
set_unido = set1.union(set2)
print(set_unido)

set1 = {1,2,3}
set2 = {1,2,3,4}
set_inser = set1.intersection(set2)
print(set_inser)

set1 = {1,2,3}
set2 = {1,2,3,4}
set_dif = set2.difference(set1)
print(set_dif)

"""# Tuple"""

#doces = tuple(("chocolate","bom bom", "paçoca"))
doces = ('chocolate','bom bom','paçoca')
print(doces)

nums = ('1','2','3')
print(len(nums))

nums = ('1','2','3')
print(nums[2])

nums = (1,2,3,4,5,6,7,8)
sub_tupla =  nums[2:4]
print(sub_tupla)

nums = (1,2,3,4,5,6,7,8)
print(9 in nums)

tupla = tuple((10,20,40))
tupla[0] = 20

tupla = (6,7,8,9,10,6,6)
print(tupla.count(6))

tupla = (5,'3', True, 7234)
pos = tupla.index('3')
print(pos)

tupla = (5,'3', True, 7234)
for x in tupla:
  print(x)

tupla = (5,'3', True, 7234)
for i in range(0, len(tupla)):
  print(tupla[i])

tupla = (5,'3', True, 7234)
indice = 0
while (indice < len(tupla)):
  print(tupla[indice])
  indice += 1

numeros_set = (1,2,3)
numeros_lista = list(numeros_set)
numeros_lista[0] = 12
numeros_lista.append("Fim")
numeros_set = tuple(numeros_lista)
print(numeros_set)

"""# Dictionaries"""

idades = {'ana':10 ,'maria': 20, 'joão':34, 'fernando':'indefinido' }
print(idades)

nome_numeros = { 7.1: "sete virgula um", 9.8: "nove virgula oito", 10.43: "dez virgula quarenta e três"}
print(nome_numeros)

idades = {'ana':10 ,'maria': 20, 'joão':34, 'fernando':'indefinido' }
print(idades['maria'])
print(idades['fernando'])

idades.get('fernando')

nome_numeros = { 
    7.1: "sete virgula um", 
    9.8: "nove virgula oito", 
    10.43: "dez virgula quarenta e três"}
print(nome_numeros[7.1])
print(nome_numeros.get(10.43))

idades = {'ana':10 ,'maria': 20, 'joão':34, 'fernando':'indefinido' }
print("ana" in idades)
print("roberto" not in idades)

idades = {'ana':10 ,'maria': 20, 'joão':34, 'fernando':'indefinido' }
idades['maria'] = 30
idades.update({"joão":40})
print(idades)

idades = {'ana':10 ,'maria': 20, 'joão':34, 'fernando':'indefinido' }
idades['marcos'] = 90
idades.pop('ana')
print(idades)
idades.popitem()
print(idades)

idades = {'ana':10 ,'maria': 20, 'joão':34, 'fernando':'indefinido' }
lista = idades.items()
print(lista, end='\n\n')
for item in lista:
  print(item[0], item[1])

idades = {'ana':10 ,'maria': 20, 'joão':34, 'fernando':'indefinido' }
chaves = idades.keys()
valores = idades.values()
for item in chaves:
  print(item)
print("------")
for item in valores:
  print(item)

idades = {'ana':10 ,'maria': 20, 'joão':34, 'fernando':20 }
lista_nome = list(idades.values())
pessoas_com_20_anos = lista_nome.count(20)
print(pessoas_com_20_anos)

idades = {'ana':10 ,'maria': 20, 'joão':34, 'fernando':20 }
idades.clear()
print(idades)

dados_maria = {
    'sexo' : 'feminino',
    'cpf' : '12345678910',
    'rg' : '19487555'
}
dados_joao = {
    'sexo' : 'masculino',
    'cpf' : '12345678745',
    'rg' : '878164'
}
dados_ana = {
    'sexo' : 'feminino',
    'cpf' : '787846555421',
    'rg' : '820000035'
}

dados_por_nome ={
    'ana' : dados_ana,
    'maria': dados_maria,
    'joao' : dados_joao
}

print(dados_por_nome['joao']['sexo'])

dados_por_nome = {
    'ana': {  
        'sexo':'feminino',
        'cpf':'787846555421',
        'rg': '820000035'
    },
    'maria': {
        'sexo' : 'feminino',
        'cpf' : '12345678910',
        'rg' : '19487555'
    },
    'joao': {
        'sexo' : 'masculino',
        'cpf' : '12345678745',
        'rg' : '878164'
    }
}
print(dados_por_nome['ana']['rg'])

lista = [x for x in range(0,10)]
print(lista)

lista = ['1', 'zero', 'Quatro']
lista = [x for x in lista]
print(lista)

lista = [x for x in range(1,11) if x % 2 ==0  ]
print(lista)

lista_aux = [1,5,9]
lista = [x for x in range(1,11) if x not in lista_aux]
print(lista)

lista = [x for x in range(-10,20) if x <= 10 if x >=0]
print(lista)

lista =  [x*2 for x in range(0,11)]
print(lista)

lista =  [str(x)[0] for x in range(0,21)]
print(lista)

lista  = ['negativo' if x < 0 else 'positivo' for x in range(-3,4)  ]
print(lista)

lista = [ str(x) +' par' if x % 2 == 0 else str(x) + ' impar'  for x in range(2,11)  ]
print(lista)

lista = [1,2,3,4,5,6,7,8,9]
lista = list(filter(lambda x: x % 2 ==0, lista))
print(lista)

lista =  [ [x for x in range(1,5)] for y in range(1,5) ]
print(lista)

lista =  [ [str(x) + str(y) for x in range(1,5)] for y in range(1,5) ]
lista

[[str(x) + '*' + str(y ) + '=' + str(x*y) for x in range(1,8)] for y in range(1,11)]

# 1 - Crie uma lista com os seguintes números 1,10,6,7,8,10. 
# Em seguida printe a soma destes números.

tupla = (1,10,6,7,8,10)
soma = 0
for i in tupla:
  soma += i
print("Soma é: ", soma)

# 2 - Cria uma lista e preencha ela com valores de 1 a 100. 
# Em seguida printe esses valores.

lista = []
for i in range(1,101):
  lista.append(i)
print(lista)

# 3 - Crie duas listas com os seguintes valores 30,4,43,52,65,-10 e 
# 43,2,4,76,32,65,3. Agora faça a junção dessas listas, mas se houverem valores 
# repetidos entre ambas eles não podem repetir na lista unida.

lista_set1 = {30,4,43,52,65,-10}
lista_set2 = {43,2,4,76,32,65,3}
novo_set = lista_set1.union(lista_set2)
print(novo_set)

# 4 - Crie uma lista contendo o nome de todos os meses do ano. 
# Em seguida receba por input o mês (número) em que você nasceu 
# e mostre qual o nome do mês que você nasceu.

meses = ('janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro',
         'outubro','novembro','dezembro')
mes_nascido = int(input("Digite o mês que você nasceu:"))
print("Você nasceu em %s " % (meses[mes_nascido - 1]))

# 5 - Crie uma lista contendo todos dias (número) do mês em que você nasceu. 
# Em seguida receba por input o dia (número) em que você nasceu e remova 
# desta lista. Ao final mostre o conteúdo da lista.

dias  = []
for i in range(1,32):
  dias.append(i)
dia_nascido = int(input("Digite o número do dia em que você nasceu: "))
dias.remove(dia_nascido)
print(dias)

# 6 - Escolha três objetos de sua escolha e em seguida cria uma lista para 
# armazenar o objeto e sua função. Agora por input receba o nome desse objeto 
# e imprima a sua função. Caso o objeto não exista, informa ao usuário.

objetos = {
    'Cadeira' : 'Serve para sentarmos',
    'Monitor' : 'Serve para visualizar o processamento',
    'Mouse'   : 'Serve para realizar operações' 
}
objeto_procurado = input("Digite o objeto: ")
if objeto_procurado in objetos:
  print(objetos[objeto_procurado])
else:
  print("Objeto não encontrado")

# 7 - Crie uma lista contendo todos os números negativos de -30 até -20. 
# Printe essa lista.

lista = [ x for x in range(-30,-19)]
print(lista)

# 8 - Percorra os números de 4 a 100 e mantenha apenas aqueles divisíveis por 4.

lista = [ x for x in range(4,101) if x % 4 ==0 ]
print(lista)

# 9 (DESAFIO) - Crie uma lista contendo todos os números de 0 a 100, mas filtre,
# mantendo apenas os números que terminam com 0.

lista = [x for x in range(0,101) if str(x)[-1] == '0']
print(lista)

# 10 - Percorra os números de 0 a 20 e crie um array, onde caso o número 
# terminar com zero o valor devera ser '0', caso contrario devera ser '-'.

lista = [ '0' if str(x)[-1] == '0' else '-' for x in range(0,21)] 
print(lista)

