# -*- coding: utf-8 -*-
"""13_Numpy.ipynb


Prof. Fernando Amaral

www.eia.ai

# Numpy
"""

import numpy
boolean = numpy.bool_(True)
print(boolean, type(boolean))

import numpy
string = numpy.string_("este e um texto")
print(string, type(string))

import numpy
string = numpy.unicode_("este é um texto")
print(string, type(string))

import numpy
#inteiro de 32 bits
inteiro = numpy.intc(-102)
#inteiro de 32 bits sem sinal
uinteiro = numpy.uintc(102)
#inteiro de 64 bits
long = numpy.int_(84848484)
#inteiro de 64 bits sem sinal
ulong = numpy.uint(34353434)

print(inteiro, type(inteiro))
print(uinteiro, type(uinteiro))
print(long, type(long))
print(ulong, type(ulong))

from numpy.core.fromnumeric import ptp
import numpy
#64 bits
ponto_flutuante = numpy.float_(10002.34)
#32 bits
ponto_flutuante2 = numpy.float32(3994.34)
print(ponto_flutuante, type(ponto_flutuante))
print(ponto_flutuante2, type(ponto_flutuante2))

int8 = numpy.int8(20)
int16 = numpy.int16(1000)
uint8 = numpy.uint8(34)
uint16 = numpy.uint16(344)
float16 = numpy.float16(16)
print(int8, type(int8))
print(int16, type(int16))
print(uint8, type(uint8))
print(uint16, type(uint16))
print(float16, type(float16))

import numpy
array = numpy.array([1,2,3,4,5,6,7,8,9,0])
print(array)
print(type(array))
print(array.dtype)

import numpy
array = numpy.array([1,2,3,4,5,6,7,8,9,0], dtype= numpy.int8)
print(array)
print(type(array))
print(array.dtype)

import numpy
array = numpy.array(["1","234","1"], dtype= numpy.string_)
print(array)
print(type(array))
print(array.dtype)

"""i = inteiro
b = booleano
u = inteiro sem sinal
f = ponto flutuante
S = String (bytes)
U = String Unicode
"""

import numpy
array = numpy.array(["abc","def","ghi"], dtype= 'S3')
print(array)
print(array.dtype)
print(array.itemsize)
print(array.nbytes)

import numpy
array = numpy.array([1,2,3], dtype= 'i2')
print(array)
print(array.dtype)
print(array.itemsize)
print(array.nbytes)

import numpy
class Pessoa:
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade

array = numpy.array([Pessoa("Fernando",45),Pessoa("Rodrigo",23)])
print(array)
print(type(array))
print(array.dtype,  end='\n\n')

print(array[0].nome, array[1].idade)

import numpy

tipo_pessoa = numpy.dtype([ ('nome','S10'),('idade','i4')  ] )  

array = numpy.array([ ('Rodrigo',24), ('fernando',45) ], dtype= tipo_pessoa)

print(array)
print(type(array))
print(array.dtype)

import numpy as np
array = np.array([1,2,3,4,5,6,7,8,9,0])
print(array)
print(array.ndim)
print(array.size)
print(len(array))
print(array.shape)
print(array.dtype)
print(array.itemsize )
print(array.nbytes)

import numpy as np
array = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(array)
print(array.ndim)
print(array.size)
print(len(array))
print(array.shape)
print(array.dtype)
print(array.itemsize )
print(array.nbytes)

import numpy
tipo_pessoa = numpy.dtype([ ('nome','S10'),('idade','i4')  ] )  
array = numpy.array([ ('Rodrigo',24), ('fernando',45) ], dtype= tipo_pessoa)
print(array)
print(array.ndim)
print(array.size)
print(array.shape)
print(array.dtype)
print(array.itemsize )
print(array.nbytes)

import numpy

array1 = numpy.zeros(9)
array2 = numpy.ones(3)
array3 = numpy.empty(6)
array4 = numpy.identity(4)

print(array1, end='\n\n')
print(array2, end='\n\n')
print(array3, end='\n\n')
print(array4, end='\n\n')

import numpy

array1 = numpy.zeros((3,3))
array2 = numpy.ones((4,4))
print(array1, end='\n\n')
print(array2, end='\n\n')

import numpy

array1 = numpy.arange(9)
array2 = numpy.arange(4,16)
print(array1)
print(array2)

import numpy

array1 = numpy.arange(2,16+1,2)

print(array1)

import numpy
array = numpy.full((4,4), 10)
print(array)

import numpy
array_float = numpy.random.rand(4,4)
array_int = numpy.random.randint(5,11, (5,5))
print(array_float)
print(array_int)

import numpy
array = numpy.array([i for i in range(0,10)])
print(array)

import numpy
array = numpy.array([
    [i for i in range(0,3)],
    [i for i in range(3,6)],
    [i for i in range(6,9)]]
    )
print(array)

import numpy as np
array = np.array([1,2,3,4,5,6,7,8,9,10])
print(array[2])
print(array[2:4])

import numpy as np
array = np.array([[1,2,3],[4,5,6],[7,8,9]]) 
print(array, end='\n\n')

print(array[2])
print(array[2][2])
print(array[2,2])
print(array[1:3])
print(array[2,1:3])

import numpy as np
array = np.array([[1,2,3],[4,5,6],[7,8,9]]) 
print(array, end='\n\n')
print(array[2, :])
print(array[:,2])

import numpy as np
array = np.array([[1,2,3,4],[5,6,7,8]]) 
print(array, end='\n\n')
print(array[1, :])
print(array[:,1])

import numpy as np
array = np.array([[1,2,3,4,5,6,7,8,9],[10,11,12,13,14,15,16,17,18],
                  [19,20,21,22,23,24,25,26,27]]) 
print(array, end='\n\n')
print(array[1, ::2])

import numpy as np
array = np.array([1,2,3,4])
for i in array:
  print(i)

import numpy as np
array = np.array([[1,2,3,4],[5,6,7,8]])
for i in array:
  for j in i:
    print(j)

import numpy as np
array = np.array([[1,2,3,4],[5,6,7,8]])

for x in np.nditer(array, order='F'):
  print(x)

import numpy as np
array = np.array([[1,2,3],[5,6,7],[7,8,9]])
array[0] = [1,2,4]
array[1,1:3] = [0,0]
array[0,0] = 10
print(array)

import numpy as np
array = np.array([[1,2,3],[5,6,7],[7,8,9]])
array[:,2] =[0,0,0]
print(array)

import numpy as np
array = np.array([1,2,3,4])
array2 = np.append(array, [5,6,7,8])
print(array2)

import numpy as np
array = np.array([[1,2,3],[5,6,7],[7,8,9]])
print(array, end='\n\n')
array2 = np.append(array, [5,6,7])
print(array2)

import numpy as np
array = np.array([[1,2,3],[4,5,6],[7,8,9]])
array1 = np.append(array,[[10,11,12]], axis=0) #linha
array2 = np.append(array,[[10],[11],[12]], axis = 1) #adicionado por coluna
print(array, end='\n\n')
print(array1, end='\n\n')
print(array2, end='\n\n')

import numpy as np
array = np.array([1,2,3])
array = np.insert(array, 1,10)
print(array)

import numpy as np
array = np.array([[1,2,3],[7,8,9],[10,11,12]])
array1 = np.insert(array,1,[4,5,6], axis = 0)
array2 = np.insert(array,1,[4,5,6], axis = 1)
print(array1, end='\n\n')
print(array2, end='\n\n')

import numpy as np
array = np.array([[1,2,3],[7,8,9],[10,11,12]])
array1 = np.delete(array,1, axis = 0)
array2 = np.delete(array,1, axis = 1)
print(array1, end='\n\n')
print(array2, end='\n\n')

import numpy as np
array = np.array([1,2,3])
copy_array = array
copy_array[0] = 0
print(array)

import numpy as np
array = np.array([1,2,3])
copy_array = array.copy()
copy_array[0] = 0
print(array)

import numpy as np
array = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(array)
array = array.reshape(9)
print(array)

import numpy as np
array = np.array([i for i in range(0,27)])
print(array)
array = array.reshape(3,9)
print(array)
array = array.reshape(9,3)
print(array)
array = array.reshape(3,3,3)
print(array)

import numpy as np
array = np.array([[1,2,3],[4,5,6],[7,8,9]])
array = array.flatten()
print(array)

import numpy as np
array1 = np.array([1,2,3])
array2 = np.array([2,4,6])

print(array1 + array2)
print(array1 - array2)
print(array1 / array2)
print(array1 * array2)
print(array1 ** array2)
print(array1 // array2)

import numpy as np
array1 = np.array([1,1,1])
array2 = np.array([[2,4,6],[1,2,3]])
array3 = np.array([[2,4,6],[1,2,3],[3,4,5]])
print(array1 + array2)
print(array1 + array3)

import numpy as np
array1 = np.array([1,2,3])
print(array1 + 2)
print(array1 - 2)

import numpy as np
array1 = np.array([10,20,30,5])
array2 = np.array([20,40,10,5])

print(array1 > array2)
print(array1 == array2)
print(array1 != array2)

import numpy as np
array1 = np.array([10,20,30,5])
array2 = np.array([20,40,10,5])
array3 = np.array([10,20,30,5])
print(np.array_equal(array1,array2))
print(np.array_equal(array1,array3))

import numpy as np
array1 = np.array([10,20,30,5])
array2 = np.array([20,40,10,5])
array12 = np.concatenate((array1,array2),axis=0)
print(array12)

import numpy as np
array1 = np.array([[1,2,3],[4,5,6]])
array2 = np.array([[7,8,9],[10,11,12]])
array12 = np.concatenate((array1,array2),axis=0) 
print(array12)
array12 = np.concatenate((array1,array2),axis=1) 
print(array12)

import numpy as np
array1 = np.array([1,2,3])
array2 = np.array([4,5,6])

array12r = np.vstack((array1,array2))
array12c = np.hstack((array1,array2))
print(array12r)
print(array12c)

import numpy as np
array1 = np.array([[1,2,3],[4,5,6]])
array2 = np.array([[7,8,9],[10,11,12]])
array12r = np.vstack((array1,array2))
array12c = np.hstack((array1,array2))
print(array12r)
print(array12c)

import numpy as np
array = np.array([1,2,3,4,5,6])
print(np.split(array,1))
print(np.split(array,2))
print(np.split(array,3))

import numpy 
array = numpy.array([[1,2,3,4],[4,5,6,7]])
print(np.split(array,2))

import numpy 
array = numpy.array([1,2,3,4,5,6])
array1 = numpy.array_split(array,2)
array2 = numpy.array_split(array,3)
array3 = numpy.array_split(array,4)
print(array1)
print(array2)
print(array3)

import numpy 
array = numpy.array([[1,2,3],[4,5,6]])
array1 = numpy.array_split(array,2)
array2 = numpy.array_split(array,3)
array3 = numpy.array_split(array,4)
print(array1)
print(array2)
print(array3)

import numpy 
array = numpy.array([[1,2,3],[4,5,6],[7,8,9]])
array1 = numpy.hsplit(array,3)
print(array1)

import numpy
array = numpy.array([1,3,4,2,7,4])
array_find = numpy.where(array >= 4 ) 
print(array_find)

import numpy
array = numpy.array([1,3,4,2,7,4])
array_find = numpy.where( (array == 4) | (array == 7) ) 
print(array_find)

import numpy
array = numpy.array([1,-1,-3,0,6,3,-78])
array_find = numpy.where( (array > 0) & (array < 10) ) 
print(array_find)

import numpy
array = numpy.array([1,3,4,2,7,4])
array_find = numpy.any(array ==1)
print(array_find)

import numpy
array = numpy.array([1,3,4,2,7,4])
array_find = numpy.any((array>0) & (array<10))
print(array_find)

import numpy
array = numpy.array([1,3,4,2,7,4])
array_find = numpy.all(array>0)
print(array_find)

import numpy
array = numpy.array([1,0,1,1,1,0,0])
filter = array ==1
filter_array = array[filter]
print(filter_array)

import numpy
array = numpy.array([1,0,1,1,1,0,2])
filter = (array ==1) | (array ==2)
filter_array = array[filter]
print(filter_array)

import numpy
array = numpy.array([1,0,1,1,1,0,2])
filtered_array = numpy.array([i for i in array if i ==0 ])
print(filtered_array)

import numpy
array = numpy.array([4,1,3,2])
print(numpy.sort(array, kind='quicksort'))

import numpy
array = numpy.array([[38,2,1],[5,5,4]])
print(numpy.sort(array, axis = 0 ))
print(numpy.sort(array, axis = 1 ))

import numpy
arr1 = numpy.array([1,2,3,4,5,6,18])
arr2 = numpy.array([1,2,3,4,5,6,3])

array1 = numpy.add(arr1, arr2)
array2 = numpy.subtract(arr1, arr2)
array3 = numpy.multiply(arr1, arr2)
array4 = numpy.divide(arr1, arr2)

print(array1)
print(array2)
print(array3)
print(array4)

import numpy
arr1 = numpy.array([[1,2,3],[4,5,6],[7,8,9]])
arr2 = numpy.array([[1,2,3],[4,5,6],[7,8,9]])

array = numpy.add(arr1, arr2)
print(array)

import numpy
arr1 = numpy.array([1,2,3,4,5,6,18])
arr2 = numpy.array([1,2,3,4,5,6,3])

array1 = numpy.divide(arr1, arr2)
array2 = numpy.floor_divide(arr1, arr2)
print(array1)
print(array2)

import numpy
arr1 = numpy.array([1,2])
arr2 = numpy.array([2,4])

array1 = numpy.power(arr1, arr2)
print(array1)

import numpy
arr1 = numpy.array([2,2,100])
arr2 = numpy.array([2,3,31])

array1 = numpy.mod(arr1, arr2)
print(array1)

import numpy
arr1 = numpy.array([2,2,100])
arr2 = numpy.array([2,3,31])

array1 = numpy.divmod(arr1, arr2)
print(array1)

import numpy
arr1 = numpy.array([4,25,100])

array1 = numpy.sqrt(arr1)
print(array1)

import numpy
arr1 = numpy.array([3.14159, 2.71])
array = numpy.around(arr1,2)
print(array)

import numpy
arr1 = numpy.array([3.14159, 2.71])
array = numpy.floor(arr1)
print(array)

import numpy
arr1 = numpy.array([3.14159, 2.71])
array = numpy.ceil(arr1)
print(array)

import numpy
array = numpy.array([[1,2,3],[4,5,6]])
array_sum = numpy.sum(array)
print(array_sum)

import numpy
array = numpy.array([[1,2,3],[4,5,6]])
array_sum = numpy.sum(array, axis = 1)
print(array_sum)

import numpy
array = numpy.array([[1,2,3],[4,5,6]])
array_sum = numpy.cumsum(array)
print(array_sum)

import numpy
array = numpy.array([[1,2,3],[4,5,6]])
array_sum = numpy.cumprod(array)
print(array_sum)

import numpy
array = numpy.array([[1,2,3],[4,5,6]])
array1 = numpy.cumprod(array, axis =0)
array2 = numpy.cumprod(array, axis =1)
print(array1)
print(array2)

import numpy
array = numpy.array([[1,2,3,4,5,6]])
print(numpy.amin(array))
print(numpy.amax(array))

import numpy
array = numpy.array([[1,-2,-3,-4,5,6]])
print(numpy.abs(array))

import numpy
array = numpy.array([[1,4,8],[4,3,6]])
print(array)
print(numpy.amin(array))
print(numpy.amin(array, axis = 1))
print(numpy.amin(array, axis = 0))

import numpy
arr1 = numpy.array([1,2,3,4])
arr2 = numpy.array([3,4,5,6,7])
newarr = numpy.union1d(arr1,arr2)
print(newarr)

import numpy
arr1 = numpy.array([1,2,3,4])
arr2 = numpy.array([3,4,5,6,7])
newarr = numpy.intersect1d(arr1,arr2)
print(newarr)

import numpy
arr1 = numpy.array([1,2,2,3,4,3,5,5,5,4])
newarr = numpy.unique(arr1)
print(newarr)

# 1.Crie um array com os números de 0 a 9, utilize somente 1 dimensão.

import numpy
array = numpy.arange(10)
print(array)

# 2.Crie um array com os números de 0 a 9 como o exercício anterior, 
# mas utilize List Compreensions.

import numpy
array = numpy.array([i for i in range(0,10)])
print(array)

# 3.Crie um array com os números de 0 a 8, utilize 2 dimensões, ou seja, 
# com 3 linhas (3x3)

import numpy
array = numpy.arange(9).reshape((3,3))
print(array)

# 4.Crie um array do tipo float, com 10 número de sua escolha, 
# mas utilize 32 bits/4 bytes.

import numpy
array = numpy.arange(0,9, dtype='f4')
print(array)

# 5.Crie um array com os números de 1 a 20, escolhendo o tipo de dado que 
# ocupara o menor espaço da memoria. Em seguida imprima o quanto 
# ele ocupou em bytes.

import numpy
array = numpy.arange(1,21, dtype=numpy.int8)
print(array)
print(array.nbytes)

# 6.Crie uma matriz 2x2 e imprima o primeiro elemento da primeira linha, 
# e o último elemento da última linha.

import numpy
array = numpy.random.randint(1,5,(2,2))
print(array)
print(array[0,0])
print(array[1,1])

# 7.Gere uma array 3x3 com números inteiros aleatórios entre 5 e 20. 
# Então imprima a primeira coluna e última linha

import numpy
array = numpy.random.randint(5,20,(3,3))
print(array)
print(array[:,0])
print(array[2,:])

# 8. Crie uma matriz 3x3 aleatória. Percorra linha por linha com um laço e 
# imprima a soma de cada linha.

import numpy
array = numpy.random.randint(1,50,(3,3))
print(array)
for linha in array:
  print(numpy.sum(linha))

# 9.Gere um array com os valores pares de 0 a 100 com list comprehension.

import numpy
array = numpy.array([i for i in range(0,101) if i % 2 ==0 ])
print(array)

# 10.Crie uma array 4x9 com valores quaisquer, redimensione para as 
# dimensões 36, e 6x6

import numpy
array = numpy.random.randint(0,10,(4,9))
print(array.reshape((36)))
print(array.reshape((6,6)))

# 11. Crie uma função que receba três arrays de mesmo formato, então retorne 
# elas concatenadas em uma só. Se as matrizes recebidas não forem do 
# mesmo formato gere uma exceção.

import numpy

def combina(arr1,arr2,arr3):
  if arr1.shape != arr2.shape or arr1.shape != arr3.shape:
    raise Exception("Formatos são diferentes")
  
  return numpy.concatenate((arr1,arr2,arr3))

array1 = numpy.array([1,2,3])
array2 = numpy.array([4,5,6])
array3 = numpy.array([7,8,9])

print(combina(array1,array2,array3))

# 12.Crie uma função que divida um array em N pedaços, mas mantenha so os 
# valores absolutos dos valores deste array.

import numpy
def divide_abs(arr,n):
  arr = numpy.array_split(arr,n)
  arr = numpy.abs(arr)
  return arr

array1 = numpy.array([1,2,3,-4,5,-7])
print(divide_abs(array1,2))

# 13.Crie uma função que receba um array e retorne quantos números positivos ela 
# contêm.

import numpy

def conta_positivos(arr):
  return len(numpy.where(arr>0)[0])

array = numpy.array([1,2,3,4,5,-7])
print(conta_positivos(array))

#14.Crie uma função que receba uma matriz e retorne os índices dos números que 
# são divisíveis por 3.

import numpy

def divisiveis_por_3(arr):
  return numpy.where(arr % 3 == 0)[0]

array = numpy.array([4,5,6,7,8,9])
print(divisiveis_por_3(array))

# 15.Crie uma função que diga se um array possui números negativos

import numpy

def tem_negativo(arr):
  return numpy.any(arr <0)

array = numpy.array([4,-5,6,7,8])
print(tem_negativo(array))

# 16.Crie uma função que remova os números negativos de uma array.

import numpy
def tira_negativo(arr):
  filter = arr >=0
  return arr[filter]

array = numpy.array([1,-5,5,4,3,-2,-1])
print(tira_negativo(array))

# 17.Crie uma função que receba um número inicial e final, e uma array. 
# A função deve retornar uma nova array somente com os números 
# dentro deste intervalo.

import numpy

def remove_valores(arr, inicial, final):
  filter = (arr >= inicial) & (arr <= final)
  return arr[filter]

array = numpy.array([i for i in range(-10,11)])
print(array)
print(remove_valores(array,0,7))

# 18.Crie uma função que ordene uma matriz e remova todos os números impares.

import numpy

def ordena_pares(arr):
  arr = numpy.sort(arr)
  filter = arr % 2 == 1
  return arr[filter]

array = numpy.random.randint(0,10,(100))  
print(ordena_pares(array))

# 19.Realize o mesmo exercício anterior, mas remova valores duplicados.

import numpy

def ordena_pares_unicos(arr):
  arr = numpy.sort(arr)
  filter = arr % 2 == 1
  return numpy.unique( arr[filter])

array = numpy.random.randint(0,10,(100))  
print(ordena_pares_unicos(array))

