# -*- coding: utf-8 -*-
"""12_ExpressoeRegulares.ipynb


Prof. Fernando Amaral

www.eia.ai

# Expressões Regulares
"""

import re
texto = '00123451'
info = re.search('1',texto)
if info != None:
  print('Encontrado ocorrência em ', info.span())
  print("O que foi encontrado ", info.group())
else:
  print("Nada foi encontrado")

import re
texto = '00123451'
info = re.findall('1',texto)
print(info)

import re
texto = '001234510'
info = re.split("1",texto)
print(info)

import re
texto = '001234510'
info = re.sub("1","#", texto)
print(info)

import re
texto = 'existem 64 predios com 700 metros'
info = re.search('predios',texto)
if info != None:
  print('Encontrado ocorrência em ', info.span())
  print("O que foi encontrado ", info.group())
else:
  print("Nada foi encontrado")

import re
texto = 'ABCDefgHI123'

#[]
info1 = re.findall('[Ae3]',texto)
info2 = re.findall('[A-Z]',texto)
info3 = re.findall('[a-z]',texto)
info4 = re.findall('[0-9]',texto)
info5 = re.findall('[A-Za-z]',texto)
print(info1)
print(info2)
print(info3)
print(info4)
print(info5)

import re
texto = 'existem 64 predios com 700 metros'
# | => or
info = re.findall('predios|metros', texto)
print(info)

import re
texto = 'ABCDefgHI123'
info = re.findall('[A-Z]|[0-9]',texto)
print(info)

import re
texto = 'existem 64 predios com 700 metros'
info = re.search("^existem", texto)
if info !=None:
  print("Encontrado ocorrencia em ", info.span())
  print("O que foi encontrado: ", info.group())

import re
texto = 'existem 64 predios com 700 metros'
info = re.search("metros$", texto)
if info !=None:
  print("Encontrado ocorrencia em ", info.span())
  print("O que foi encontrado: ", info.group())

import re
texto = 'abbabb'
info = re.search('abb',texto)
if info != None:
  print('Encontrado ocorrência em ', info.span())
  print("O que foi encontrado ", info.group())
else:
  print("Nada foi encontrado")

import re
texto = 'abbabb'
info = re.search('(abb)+',texto)
if info != None:
  print('Encontrado ocorrência em ', info.span())
  print("O que foi encontrado ", info.group())
else:
  print("Nada foi encontrado")

import re
texto = 'aabbaabbbbbbaaccaa'
info = re.search('(aa|bb)+',texto)
if info != None:
  print('Encontrado ocorrência em ', info.span())
  print("O que foi encontrado ", info.group())
else:
  print("Nada foi encontrado")

import re
texto = 'aabbaabbbbbbaaccaa'
info = re.search('(aa|bb){2}',texto)
if info != None:
  print('Encontrado ocorrência em ', info.span())
  print("O que foi encontrado ", info.group())
else:
  print("Nada foi encontrado")

import re
texto = 'abc'
info = re.search('(aa|bb)*',texto)
if info != None:
  print('Encontrado ocorrência em ', info.span())
  print("O que foi encontrado ", info.group())
else:
  print("Nada foi encontrado")

import re
texto = ''
info = re.search('^(aa)?$',texto)
if info != None:
  print('Encontrado ocorrência em ', info.span())
  print("O que foi encontrado ", info.group())
else:
  print("Nada foi encontrado")

import re
texto = 'aaaaaa'
info = re.search('^(aa){2,3}$',texto)
if info != None:
  print('Encontrado ocorrência em ', info.span())
  print("O que foi encontrado ", info.group())
else:
  print("Nada foi encontrado")

import re
# {,7}  7 ou menos
# {7,}  7 ou mais 
texto = 'xxxxx'
info = re.search('^x{7,}$',texto)
if info != None:
  print('Encontrado ocorrência em ', info.span())
  print("O que foi encontrado ", info.group())
else:
  print("Nada foi encontrado")

import re
texto = 'Olá sou eu, AQUI, e nada para frente'
info = re.search('(.)*(AQUI)(.)*',texto)
if info != None:
  print('Encontrado ocorrência em ', info.span())
  print("O que foi encontrado ", info.group())
else:
  print("Nada foi encontrado")

import re

texto = '01234 ABC'

info = re.search("\d+",texto)

if info != None:
  print("Encontrada ocorrência em ", info.span())
  print("O que foi encontrado ", info.group())

import re

texto = '01234 ABC'

info = re.search("\W",texto)

if info != None:
  print("Encontrada ocorrência em ", info.span())
  print("O que foi encontrado ", info.group())

import re
texto = '0 C°'

info = re.search('^(-)?[0-9]+ C°$', texto)

if info != None:
  print("Temperatura válida")
else:
  print("Temperatura inválida")

import re
texto = '99224566'

info = re.search('^99([0-9]{6})$', texto)

if info != None:
  print("Número válido")
else:
  print("Número inválido")

import re
texto = "Texto teste"

info = re.search('(^[A-Za-z]+ +[A-Za-z]+ *$)', texto)
if info != None:
  print("Encontrada ocorrência em ", info.span())
  print("O que foi encontrado ", info.group())
else:
  print("Padrão não encontrado")

# DD/MM/AAAA
# O dia pode variar de 00 a 31
# o mês de 00 a 12
# o ano de 0000 a 9999

texto =  '28/05/1998'

info = re.search("^([0-2][0-9]|[3][0-1])/([0][1-9]|[1][0-2])/([0-9]){4}$" ,texto)
if info != None:
  print("Data válida")
else:
  print("Data Inválida")

# 1 - Faça uma expressão regular para reconhecer números de 20 até 35 apenas.
# O texto deve ser composto apenas destes números, nenhum outro caractere 
# é permitido

import re
texto = '16'
info = re.search("^([2][0-9])|([3][0-5])$", texto)
if info != None:
  print("Encontrado ocorrência em ", info.span())
  print("Número encontrado  ", info.group())
else:
  print("Valor inválido")

# 2 - Faça uma expressão regular para dizer se a palavra 'python' esta na frase.

import re
texto = 'este notebook utiliza python'
info = re.search("python", texto)
if info != None:
  print("Encontrado ocorrência em ", info.span())
  print("Número encontrado  ", info.group())
else:
  print("Valor inválido")

'''
3 - Faça uma expressão regular para validar se uma string dada é um dia da 
semana. As possibilidades são:
Segunda-Feira
Terça-Feira
Quarta-Feira
Quinta-Feira
Sexta-Feira
Sábado
Domingo
'''

import re
texto = 'Terça-Feira'
info = re.search('^(Segunda-Feira|Terça-Feira|Quarta-Feira|Quinta-Feira|Sexta-Feira|Sábado|Domingo)$', texto)
if info != None:
  print("Encontrado ocorrência em ", info.span())
  print("Número encontrado  ", info.group())
else:
  print("Valor inválido")

# 4 - Faça uma expressão regular para detectar telefones que comecem com 95. 
# Telefones que começam com 95 devem ser bloqueados. Um número de 
# telefone deve ser válido para poder ser validado, na forma XXXXXXXX onde X é 
# um número. Primeiro diga se é um número válido.
# Caso seja diga se ele foi bloqueado ou não.

import re
texto = '9645634'

info = re.search("^([0-9]{8})$", texto)

if info !=None:
  print("Número válido")
  info2 = re.search("^95([0-9]{6})$", texto)
  if info2 !=None:
    print("Telefone bloqueado")
  else:
    print("Telefone não bloqueado")
else:
  print("Número inválido")

# 5 - Faça uma expressão regular para reconhecer palavrados no gerúndio. 
# Normalmente essas palavras podem ser detectadas caso elas terminem com ando,
# sendo, indo: Exemplo: sorrindo, andando. Usa a função “find all” 
# para retornar as ocorrências.

import re
texto = "Olá, eu estou dormindo, e não sorrindo"
info = re.findall("([\w]+indo|ando|endo)+", texto)
print(info)

'''
6 - Faça um expressão regular para detectar se a hora é válida: 
O formato é de 24 horas, e é especificado da seguinte forma: HH:MM
Ex:
19:30
09:30
23:45
23:70 (inválido)
'''

import re
texto = '00:59'

info = re.search("^([0-1][0-9]|[2][0-3]):[0-5][0-9]$", texto)

if info != None:
  print("Horário válido")
else:
  print("Horário inválido")

# 7 (DESAFIO) - Faça uma expressão regular para validar se uma expressão é uma 
# conta matemática valida. Nessa conta matemática só podem haver 2 números 
# inteiros sendo somados ou subtraídos entre si. Valide se é uma expressão 
# matemática ou não.

import re

texto = '3232+4453'
info = re.search('^ *(\d+ *(-|\+) *\d+) *$', texto)
if info != None:
  print("Expressão válida")
else:
  print("Expressão inválida")

