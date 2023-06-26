# -*- coding: utf-8 -*-
"""3_EstruturasdeProgramacao.ipynb



Prof. Fernando Amaral

www.eia.ai

# Estruturas de Programação
## IF
"""

print("Isto está fora dos ifs")
if (True):
  print("Este código vai ser executado")

print("Isto está fora dos ifs")

if (False):
  print("Esta código não vai ser executado")

print("Isto está fora dos ifs")

if (True):
  pass

valor1 = 10
valor2 = 10
sao_iguais = (valor1 == valor2)
if sao_iguais:
  print("São iguais")

valor1 = 10
valor2 = 10
if (valor1 == valor2):
  print("São iguais")
  print("São iguais parte II")

valor1 = 10
valor2 = 10
if (valor1 == valor2): print("São iguais")

if (10 != 20):
  print("São diferentes 1")

if (10 != 10):
  print("São diferentes 2")

if ("olá" != "alo"):
  print("São diferentes 3")

numero = 11
if (numero > 10):
  print("é maior que 10")

nome = input("Digite seu nome:")
if "a" in nome:
  print("Possui a letra \'a\'")

nome = input("Digite seu nome: ")
possui_vogal = ("a" in nome) or ("e" in nome) or ("i" in nome) or ("o" in nome) or ("u" in nome) 
if possui_vogal:
  print("Possui alguma vogal")

numero = 10
if (numero >= 10):
  print("É maior ou igual a 10")
  print("------")
else:
  print("É menor que 10")
  print("******")
print("Fim")

numero  = 9
if numero % 2 == 0:
  print("É par")
else:
  print("É impar")

valor = 11
if valor >=0 and valor < 10:
  print(valor)
else:
  print("Valor não aceito")

texto = "ab"
if len(texto) == 1:
  print("Tem 1 caractere")
else:
  print("não tem 1 caractere")

numero = 1
if numero ==1 or numero ==0:
  print("É 1 ou 0")

numero = -11
condicao = numero > 10 or numero < -10
if condicao:
  print("Absolutamente maior que 10")

numero = 10
if numero > 0:
  print("Número é maior que zero")
  if numero > 10:
    print("Número é maior que dez")

numero = 1001
if numero < 10:
  print("Menos que 10")
elif numero < 100:
  print("Menos que 100")
elif numero <= 1000:
  print("Menor ou igual a 1000")
else:
  print("Nenhuma anterior")

texto = 'c'
if texto == 'a':
  print("É vogal a")
elif texto == 'e':
  print("É vogal e")
elif texto == 'i':
  print("É vogal i")
elif texto == 'o':
  print("É vogal o")
elif texto == 'u':
  print("É vogal u")
else:
  print("É consoante")

numero = 11
resultado = "PAR" if numero % 2 == 0 else "IMPAR"
print(resultado)

numero = 3
resultado = "Um" if numero == 1 else "Dois" if numero == 2 else "Três"
print(resultado)

# 1 - Crie um programa que receba o seu saldo bancário e o quanto você deve. 
# Em seguida o programa deve dizer se você tem saldo positivo ou negativo.

saldo_entrada = input("Digite seu saldo: ")
valor_devido_entrada = input("Digite o quanto você deve: ")
saldo = float(saldo_entrada)
devido = float(valor_devido_entrada)
valor_total = saldo - devido
if valor_total >= 0:
  print("Seu saldo é positivo, você tem R$ %.2f" % (valor_total))
else:
  print("Seu saldo é negativo, você deve R$ %.2f" % (valor_total))

# 2 - Crie um programa que possui uma variável que guarde seu CPF e que guarde 
# uma senha de sua escolha. Em seguida receba por input uma senha do usuário. 
# Caso a senha recebida seja a correta mostre o CPF, 
# caso não diga que a senha esta incorreta.

senha = "123"
cpf = "123.456.789-10"
senha_usuario = input("Digite a senha: ")
if senha_usuario == senha:
  print("Senha correta, seu CPF é %s" % (cpf))
else:
  print("Sua senha está incorreta!")

# 3 - Crie um programa que fale sobre sua idade. As regras são as seguintes
# você deve receber por input sua idade, se você tiver ate três anos 
# printe que é um bebe, ate 13 anos uma criança, ate 18 anos adolescente, 
# até 65 adulto. Em nenhum deste casos é um idoso

idade = int(input("Digite sua idade: "))
if idade <=3:
  print("Você é um bebe!")
elif idade <= 65:
  print("Você é uma criança!")
elif idade <= 18:
  print("Você é um adolescente!")
elif idade <= 65:
  print("Você é um adulto!")
else:
  print("Você é um idoso!")

# 4 - Crie um programa que receba dois números, e também receba do usuário 
# a operação que deve ser feita, as possibilidades são soma(+), subtração (-), 
# divisão(/) e multiplicação(*). 
# Realize a operação escolhida sobre os dois números.

nume1 = float(input("Digite o primeiro número: "))
nume2 = float(input("Digite o primeiro segundo: "))
operacao = input("Digite a operação: ")

if (operacao == "+"):
  soma = nume1 + nume2
  print("A soma é: ", soma)
elif (operacao == "-"):
  subtracao = nume1 - nume2
  print("A subtração é ", subtracao)
elif (operacao == "*"):
  multiplicacao = nume1 * nume2
  print("A multiplição é ", multiplicacao)
elif (operacao == "/"):
  divisao = nume1 / nume2
  print("A divisão é ", divisao)
else:
  print("Operação Inválida!")

"""# Laços / Loops"""

while (True):
  print("Isso não vai parar!")

interacao = 10
while (interacao > 0):
  print(interacao)
  interacao -= 1
print("Encerrou!")

indice = 10
print("Programa começou")
while (indice >= 2):
  resto = (indice % 2)
  if resto == 0:
    print("O número %d é par" % (indice))
  else:
    print("O numéro %d é impar" % (indice))
  indice -= 1

print("Programa finalizou")

soma = 0
numeros_lidos = 0

while (numeros_lidos < 5):
  num_str = input("Digite um valor: ")
  num_lido = float(num_str)
  soma += num_lido
  numeros_lidos += 1

print("Soma é %.2f " % (soma))

texto = "Olá 123 _"
indice = 0
while (indice < len(texto)):
  print(texto[indice])
  indice += 1

num_atual = 0
while (True):
  if (num_atual == 5):
    break
  print(num_atual)
  num_atual +=1

print("Encerrou!")

num_atual = 0

while (num_atual < 10):
  num_atual += 1
  if (num_atual ==7):
    continue
  print(num_atual)

print("Encerrou!")

# 1 - Crie um programa que receba 5 números e retorne 
# a média aritmética entre esses números

soma_atual = 0
numeros_lidos = 0

while (numeros_lidos < 5):
  num_str = input("Digite um valor: ")
  num_lido = float(num_str)
  soma_atual += num_lido
  numeros_lidos += 1

media = soma_atual  / 5
print("A média é %.2f " % (media))

# 2 - Crie um programa que receba 5 números, realiza a soma destes números, 
# mas caso um destes números seja negativo não considere ele na soma.

soma_atual = 0
numeros_lidos = 0

while (numeros_lidos < 5):
  num_str = input("Digite um valor: ")
  num_lido = float(num_str)
  if num_lido >=0:
    soma_atual += num_lido
  numeros_lidos += 1

print("A soma é %.2f " % (soma_atual))

# 3 - Cria um programa que receba um número arbitrário (definido pelo usuário) 
# de números que serão lidos e retorne a soma de todos eles.

numeros_que_devem_ser_lidos = float(input("Digite quantos números serão lidos:"))

soma_atual = 0
numeros_lidos = 0

while (numeros_lidos < numeros_que_devem_ser_lidos):
  num_str = input("Digite um valor: ")
  num_lido = float(num_str)
  soma_atual += num_lido
  numeros_lidos += 1

print("O total é %.2f " % (soma_atual))

# 4 - Percorra os números de 2 até 10 e diga se o número é par ou impar.

num_atual =2
while (num_atual <= 10):
  resto = num_atual % 2
  if (resto ==0):
    print("O número %d é par" % (num_atual))
  else:
    print("O número %d é impar" % (num_atual))
  num_atual +=1

# 5 - Crie um programa que receba como input uma string. 
# Em seguida percorra a string e diga quantos espaços em branco essa string tem.

texto = input("Digite um texto: ")
indice =0
num_vazio =0

while (indice < len(texto)):
  if texto[indice] == " ":
    num_vazio +=1
  indice += 11

print("Número de espaços no texto é de %d " % (num_vazio))

for x in range(10):
  print(x)

for x in range(5,10):
  print(x)

for x in range(5,20,5):
  print(x)

for x in range(20,5,-5):
  print(x)

texto = "123t56789"
for x in range(0, len(texto)):
  print(texto[x])

letra = input("Digite uma letra: ")

if (len(letra) != 1):
  print("Precisa ter 1 digito!")
else:
  texto = input("Digite um texto: ")
  for i in range(0, len(texto)):
    if letra == texto[i]:
      print("Encontrei a letra %s na posição %d " % (letra, i))

texto = "Olá, eu sou iterável"
for x in texto:
  print(x)

for x in range(0,3):
  for y in range(0,5):
    print(x,y)

for x in range(1,11):
  print("------------------")
  for y in range(1,11):
    print("%d X %d = %d" % (x,y,x*y))

# 1 - Crie um programa que receba uma string por input e conte quantos 
# caracteres ela têm, não leve em conta caracteres de espaço. 
# Você não deve usar o len().

texto = input("Digite um texto:")
num_caracteres = 0

for letra in texto:
  if (letra != " "):
    num_caracteres += 1

print("Tem %d caracteres no texto: " % (num_caracteres))

# 2 - Crie um programa que faça o calculo do fatorial de um número.
# O fatorial a ser calculado deve ser recebido por input.

fatorial_str = input("Digite o fatorial desejando:")
fatorial_numero = int(fatorial_str)
resultado = 1

for i in range(1, fatorial_numero+1):
  resultado *= i

print("O fatorial de %d é %d " % (fatorial_numero, resultado))

# 3 - Crie um programa que leia um quantidade arbitraria de textos e 
# concatene eles numa string única.

numero_de_leituras = int(input("Digite o número de textos que serão lidos: "))
texto_total = ""
for i in range(numero_de_leituras):
  texto_total += input("Digite o texto: ")

print("Texto completo: ", texto_total)

# 4 - Cria um programa que printe a tabuada da divisão de um número lido 
# por input.

numero = int(input("Digite a tabuada de divisão desejada: "))
for num in range(1,11):
  print("%d / %d = %f " % (num, numero, num / numero))

# 5 (DESAFIO) - Crie um programa que percorra os números de 3 até 30 e 
# diga se o número é primo ou não.

for numero in range(3,31):
  e_primo = True

  for num_teste in range(2, numero):
    if (numero % num_teste == 0):
      e_primo = False
      break
  
  if (e_primo):
    print("O número %d é primo" % (numero))
  else:
    print("O número %d não é primo " % (numero))

