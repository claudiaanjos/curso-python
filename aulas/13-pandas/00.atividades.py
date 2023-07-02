# -*- coding: utf-8 -*-
"""14_Pandas_.ipynb



Prof. Fernando Amaral

www.eia.ai

# Pandas
"""

import pandas as pd
pd.Series([1,2,3,4,5])

import pandas as pd
pd.Series([1,2,3,4,5], dtype='i4')

import pandas as pd
pd.Series([1,2,3,4,5], dtype='i4', name="Meus números")

import pandas as pd
minha_serie = pd.Series([1,2,3,4,5], dtype='i4', name="Meus números", index=["Um","Dois","Três","Quatro","Cinco"])
print(minha_serie['Um'])
print(minha_serie['Quatro'])
print(minha_serie.shape)

import pandas as pd
minha_serie = pd.Series([1,2,3,4,5], dtype='i4', name="Meus números", index=["Um","Dois","Três","Quatro","Cinco"])
minha_serie['Seis'] = 6
print(minha_serie)

import pandas as pd
import numpy as np
array = np.array([45.4,50.5, 65.7, 98.7])
pesos = pd.Series(array, index=['Carlos',"josé","Maria","Fernanda"])
print(pesos)
print(type(pesos))

import pandas as pd
data_frame = pd.DataFrame()
data_frame

import pandas as pd
nomes = ['Roger','Lucas','Cristiano','Maria']
data_frame = pd.DataFrame(nomes)
data_frame

print(data_frame)

import pandas as pd
numeros = [
          ['11','12','13','14'],   
          ['11','12','13','14'],   
          ['11','12','13','14'],   
          ['11','12','13','14']   
          ]

data_frame = pd.DataFrame(numeros)
data_frame

import pandas as pd
numeros = [
          ['11','12','13','14'],   
          ['11','12','13','14'],   
          ['11','12','13','14'],   
          ['11','12','13','14']   
          ]
data_frame = pd.DataFrame(numeros, columns=['a','b','c','d'],index=['x','y','z','w'])
data_frame

import pandas as pd
dados = {
        'Nome': ['Roger','Cristiano','Diego','Carla'],
        'Idade': [45,34,56,21],
        'Profissão': ['Engeheiro','Desenvolvedor','Metalurgico','Médica']
        }

data_frame = pd.DataFrame(dados)
data_frame

import pandas as pd
dados = {
        'Idade': [45,34,56,21],
        'Profissão': ['Engeheiro','Desenvolvedor','Metalurgico','Médica']
        }
data_frame = pd.DataFrame(dados, index=['Roger','Cristiano','Diego','Carla'])
data_frame

data_frame.loc['Roger']

import pandas as pd
data = pd.read_csv('pessoas.csv', index_col='Nome')
data

data.loc['Roger']

len(data.columns)

data.columns

len(data.index)

data.index

data.shape

for indice, linha in data.iterrows():
  print(indice, linha[0], linha[1], linha[2])

for coluna in data:
  print(coluna)

data['Altura']

for coluna in data:
  print(data[coluna])

data

print(data.loc['Roger']['Idade'])
print(data.loc['Roger'][0])

print(data.iloc[0]['Idade'])
print(data.iloc[0][0])

print(data.loc['Roger'])
print(type(data.loc['Roger']))

print(data.iloc[0])

data.loc['Cristiano':'Jeferson']

data.iloc[1:4]

print(data['Idade'])

idade = data['Idade']
print(idade[3])
print(idade['Diego'])

data[['Idade','Altura']]

colunas = data[['Idade','Altura']]
print(type(colunas))

data

colunas = data.iloc[:,1:3]
colunas

colunas = data.loc[:,"Idade":"Profissão"]
colunas

mask = data['Idade'] < 50
mask

nova_dframe = data[mask]
nova_dframe

nova_dframe = data[(data['Idade']>40) & (data['Altura']>1.75) ]
nova_dframe

data

data.at['Roger','Idade'] = 56
data

data.iat[2,0] = 100
data

data.loc['Cristiano','Idade':'Profissão'] = (45,'Dev')
data

data.loc['José',['Idade','Altura']] = (65,1.72)
data

data.iloc[0,2] = 1.94
data

data.loc[:,'Idade'] = 76
data

data.loc[:,'Idade':'Profissão'] = None
data

data.loc[:,['Idade','Altura']] = (23,1.8)
data

data = pd.read_csv('pessoas.csv', index_col='Nome')
data

data.loc[(data['Idade']<40),'Altura'] = 1.99
data

data.loc[(data['Idade'] == 34) & (data['Profissão']=='Programador'),['Idade','Altura']]= (80,1.00)
data

data = pd.read_csv('pessoas.csv', index_col='Nome')
data

data.loc['Carlos'] = (56,'Engenheiro',1.76)
data

data_adicional = pd.DataFrame({'Idade':[34,21,54],
                               'Profissão': ['Paraquedista','Professor','Cozinheiro'],
                               'Altura': [1.79, 1.76, 1.90]},
                              index = ['Julia','Roberto','Jack']                              
                               )
data_adicional.index.name = 'Nomes'
data_adicional

data = data.append(data_adicional)
data

data = pd.read_csv('pessoas.csv', index_col='Nome')
data

data['Sobrenome'] = None
data

data['Sobrenome'] = ['Silva','Sagan','','','','']
data

data.insert(loc=1,column='Data Nascimento', value=['30/09/2000' for i in range(6)])
data

data = pd.read_csv('pessoas.csv', index_col='Nome')
data

data2 = data.drop(index = ['Roger','Diego'])
data2

data.drop(index = ['Roger','Diego'], inplace=True)
data

data.drop(index=data.index[[0,1]], inplace=False)

data

data = pd.read_csv('pessoas.csv', index_col='Nome')
data

data.drop(index=data[data['Altura']>= 1.7].index, inplace=True)
data

data = pd.read_csv('pessoas.csv', index_col='Nome')
data

data.drop(columns=['Idade'], inplace=True)
data

data.columns

data.drop(columns=data.columns[[0,1]], axis=1, inplace=True)
data

data = pd.read_csv('pessoas.csv', index_col='Nome')
data

data.loc['Roger','Idade'] = None
data

data.isnull()

pd.isnull(data['Idade'])

data.notnull()

mask = pd.notnull(data['Idade'])
mask

data[mask]

copy = data.sort_values("Idade", ascending=False, inplace=False)
copy

copy = data.sort_values("Idade", ascending=True, inplace=False, na_position='last')
copy

data.loc['Maria','Idade'] = 34
data

copy = data.sort_values(['Idade','Altura'], ascending = [True,False], inplace=False, na_position='first')
copy

data = pd.read_csv('pessoas.csv', index_col='Nome')
data

data.loc['Willian'] = (25 ,'Programador' ,1.75 )
data.loc['Lando'] = (22 ,'Programador' , 1.65)
data.loc['Max'] = (45 ,'Médico' ,1.68 )
data.loc['Sebastian'] = (35 ,'Médico' ,1.74 )
data.loc['Ana'] = (23 ,'Médico' ,1.7 )
data

grupos = data.groupby('Profissão')

for indice, grupo in grupos:
  print(indice)
  print(grupo)

grupos.get_group('Programador')

grupos = data.groupby(['Profissão','Idade'])
grupos.describe()

# 1.Crie um dataframe com a estrutura abaixo. Os índices devem ser as 
# Equipes “X Racing”, “Equatorial”, “Typo”, “Blue Race”,”Capa Racing”. 
# Utilize um dicionário.

import pandas as pd
dados = {
        'Sede' : ['Nova Iorque','São Paulo','Nova Iorque','Londres','Londres'],
        'Piloto': ['Mike Ross','Sebastian Thomas','Glen Are','Michael Schum','Luiz da Silva'],
        'Mundiais': [10,11,0,3,44],
        'Vitorias': [321,229,12,44,1023]
        }
data_frame = pd.DataFrame(dados, index=['X Racing','Equatorial','Type','Blue Race','Capa Racing'])
data_frame

# 2.Mostre todas as informações da equipe Blue Race

data_frame.loc['Blue Race']

# 3.Mostre o número de mundiais da equipe Capa Racing

print(data_frame.loc['Capa Racing']['Mundiais'])
print(data_frame.loc['Capa Racing'][2])

# 4.Mostre apenas as equipes que tem 10 ou mais mundiais

mask = data_frame['Mundiais'] >= 10
data_frame[mask]

# 5.Mostre apenas as equipes que tem 10 ou mais mundiais e mais de 300 vitórias

data_frame[ (data_frame['Mundiais']>=10) & (data_frame['Vitorias'] > 300)]

# 6.Atualize o nome do piloto da Equipe Equatorial para Antônio Racer

data_frame

data_frame.at['Equatorial','Piloto'] = 'Antônio Racer'
data_frame

# 7. Atualize em um mesmo comando a equipe X Racing, definindo sede como 
# São Paulo e Vitórias com 322

data_frame.loc['X Racing',['Sede','Vitorias']] = ('São Paulo',322)
data_frame

# 8.Inclua uma nova equipe Red Cow, com sede em São Paulo, 
# Pitolo Fernando Vetel, Mundiais zero e Vitórias zero

data_frame.loc['Red Cow'] = ("São Paulo", "Fernando Vetel",0,0)
data_frame

# 9. Ordene o dataframe de forma decrescente pelo número de vitórias

data = data_frame.sort_values("Vitorias", ascending=False, inplace=False)
data

