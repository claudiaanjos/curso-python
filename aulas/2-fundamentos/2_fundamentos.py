# -*- coding: utf-8 -*-
"""2_Fundamentos.ipynb



Prof. Fernando Amaral

www.eia.ai

# Fundamentos
## Comentários
"""

# isto é um comentário
# isto é outro comentário
print("olá mundo") # isto é um comentário

''' Este é um comentário
o comentário continua aqui
aqui ainda continua
e aqui termina '''

print('olá mundo')
print(10)
print(20.5)

print("Maça", 20, 30.45)

print("Maça", "Pera", "Uva", sep=' - ')

print("Maça","Pera", end = ' Fim', sep=' ')

print("Este é um texto longo, \n eu quero quebrar a linha")

print("Maça","Pera", sep='\n')

print("A pontuação total de %s foi %s pontos" % ("Fernando","10") )

print("A pontuação total de {} foi {} pontos".format("Fernando","10"))

print("A pontuação total de" + " Fernando" + " foi" + " 10 " + "pontos")

#1 - Realize o print do seu nome completo, sua idade e sua 
# altura utilizando um print para cada valor.

print("Fernando")
print("30")
print("1,92")

#2 - Realize o print do seu nome completo, sua idade e sua altura 
# utilizando apenas um print para todos valores.

print("Nome: {}, idade:{}, altura:{}".format("Fernando", "30", "1,90"))

#3 - Realize o print de 3 números de sua escolha em um mesmo print, 
# mas separados pelo caracter '-'.

print(1,2,3, sep="-")

"""# Variáveis"""

_numero = 1
Numero = 2
numero = 3
numero123 = 4
print(_numero, Numero, numero, numero123)

numero = 10
print(numero)
numero = 20
print(numero)

texto = 'Olá mundo!'
print(texto)

"""# Tipos Primitivos"""

variavel = None
print(variavel)

inteiro = 10
print(inteiro)

decimal = 1.53
print(decimal)

texto = "olá, isto é um texto"
print(texto)

var = True
print(var)
var = False
print(var)

var1 = 10
var2 = var1
print(var2)

var = None
print(var)
var = 1
print(var)
var = "Texto"
print(var)

saldoBancario = 100
SaldoBancario = 100
saldo_bancario = 100

#1 - Crie uma variável de cada tipo e ponha alguma valor escolhido. 
#Em seguida, printe todos esses valores.

inteiro = 750
decimal = 3.1415
text = "Maça"
booleano = True
print(inteiro)
print(decimal)
print(text)
print(booleano)

#2 - Crie variáveis para guardar seu nome, CPF e uma que indique 
# se você esta casado, em seguida printe esses valores separadamente, 
# mas não esqueça de printar junto o que eles significam.

nome = "Fernando Amaral"
CPF = "123.456.789-10"
casado = True
print("Nome: ", nome)
print("CPF: ", CPF)
print("Casado: ", casado)

"""# Formatação"""

# %s texto
# %d inteiro
# %f real

nome = "Ana"
texto_formatado = "O nome dela é %s " % (nome)
print(texto_formatado)

nome = "Rodrigo"
idade = 23
altura = 1.73
texto = "Meu nome é %s. tenho %d anos e tenho %f metros de altura" % (nome, idade, altura)
print(texto)

numero_gigante = 1.123456789
print("Número gigante formatado: %.2f" % (numero_gigante))

valor = False
print("O valor é %s" % (valor))
print("O valor é %d" % (valor))

decimal = 23.4566
print("A parte inteira é %d" % (decimal))

texto = "Olá, assim se quebra uma linha,\n\tentendeu como quebra a linha?\n\t\tfim"
print(texto)

texto = 'Deixa a \'palavra\' entre aspas'
print(texto)

# 1 - Escreva e formate a data em que você nasceu no formato dia/mês/ano. 
# Não esqueça de criar 3 variáveis para guardar o dia, mês e ano.

dia, mes, ano = 4, 12, 1980
data = "Eu nasci em %d/%d/%d" % (dia, mes, ano)
print(data)

# 2 - Escreva e formate a hora e minuto atual. 
# Não esqueça de criar duas variáveis para guardar a hora e minuto.

horas = 21
minutos = 53
print("Agora são %d horas e %d minutos" % (horas, minutos))

# 3 - Escreva um programa que contêm o número PI, que deve ter o valor exato 
# de 3.14159265359. Agora formate esse número para ter apenas cinco casas decimais.

pi = 3.14159265359
pi_formatado = 'O PI é normalmente exibido com %.5f' % (pi)
print(pi_formatado)

"""# Operadores Aritméticos"""

print(10 + 20)

numero = 10 + 10.5
print(numero)

outro_numero = 30 + numero
print(outro_numero)

numero = 20 -10
print(numero)

numero = 10 * 2
print(numero)

numero = 10 / 3
print(numero)

numero = 10 // 3
print(numero)

numero = 2 ** 4
print(numero)

numero = 4 % 3
print(numero)

nume1 = 10 * 2 + 1
print(nume1)

nume1 = 10 * (2 + 1)
print(nume1)

nume1 = 3 * 3 - 9
print(nume1)

nume1 = 3 * (3 - 9)
print(nume1)

nume1 = 20
nume2 = 40
nume3 = 60
resultado = nume1 + nume2 + nume3
print(resultado)

resultado = resultado * 2
print(resultado)

a = 1
a += 1
print(a)

# 1 - Crie um programa que possui duas variáveis, uma recebe o ano 
# em que estamos e a outra o ano em que você nasceu. 
# Em seguida subtraia ambas para receber uma estimativa de quantos anos você tem. 
# Mostre esse valor na saída do programa.

ano_atual = 2022
ano_nascimento = 1998
estimativa_idade = ano_atual - ano_nascimento
print("Devo ter em torno de %d anos" % (estimativa_idade))

# 2 - Crie um programa que faz a média aritmética entre três números. 
# Estes números devem ser salvos em uma variável. 
# Mostre esse valor na saída do programa.

num1 = 10
num2 = 15
num3 = 6
media = (num1 + num2 + num3) / 3
print("A média é %f " % (media))

# 3 - Crie um programa que calcule o IMC (índice de massa corporal).
# O IMC é dado pelo peso em KG divido pela altura em metros elevado ao quadrado. 
# Salvar esses valores em uma variável. Mostre esse valor na saída do programa.

peso = 80.5
altura = 1.72
imc = peso // altura ** 2
print('O IMC é ', imc)

# 4 (Desafio) - Você tem um determinado números de ovos de páscoa para dividir 
# entre um determinado número de pessoas (duas variáveis iniciais). 
# Determine quantos ovos ficarão por pessoa e quantos ovos sobrarão 
# pois não puderam ser divido igualmente. 
# Lembre que o número de ovos por pessoa é um número inteiro

ovos = 56
pessoas = 3
print("Tenho inicialmente %d ovos para %d pessoas " % (ovos, pessoas))
ovos_por_pessoas = ovos // pessoas
ovos_restantes = ovos % pessoas
print("Cada uma das %d pessoas terá %d ovo(s) " % (pessoas, ovos_por_pessoas))
print("Restou %d ovo(s) que não puderam ser divididos" % (ovos_restantes))

"""# Operadores Lógicos"""

resultado1 = True and False
print(resultado1)

resultado2 = True and True
print(resultado2)

var1 = True
var2 = True
var3 = False
print(var1 and var2 and var3)

clima_bom = True
estou_disposto = True
vou_ao_mercado = clima_bom and estou_disposto
print("Vou ao mercado? ", vou_ao_mercado)

resultado = True or False
print(resultado)

resultado = True or True
print(resultado)

resultado = False or False
print(resultado)

sei_programar = True
sei_investir = False
ganho_bom_salario = sei_programar or sei_investir
print("Terei um bom salário? ", ganho_bom_salario)

resultado = False
print(not resultado)

porta_aberta = False
tem_chave = False
print("Estou trancado? ", not porta_aberta and not tem_chave)

# Prioridade
# NOT , AND, OR

bool1 = True or False and True
print(bool1)

bool2 = True or not False
print(bool2)

bool3 = True and not (True or False)
print(bool3)

# 1 - Crie um programa que diga “se você precisar ir ao mercado”. 
# Você precisa ir ao mercado se “faltar comida” ou “se for sábado”. 
# Mostre na saída do programa o valor lógico, indicando sim ou não.

falta_comida = False
e_sabado = True
vou_ao_mercado = falta_comida or e_sabado
print("Preciso ir ao mercado? ", vou_ao_mercado)

# 2 - Crie um programa que responda “se você pode atravessar a rua” 
# na faixa de pedestres. Você pode atravessar a rua se o “sinal estiver  
# vermelho” e “se não houver nenhum carro vindo da direita” E “nem da esquerda”. 
# Altere as variáveis para verificar se o programa esta correto.
# Mostre na saída do programa o valor lógico.

sinal_vermelho = True
carro_vindo_direita = False
carro_vindo_esquerda = False
pode_atravessar = sinal_vermelho and not carro_vindo_direita and not carro_vindo_esquerda
print("Posso atravessar? ", pode_atravessar)

# 3 - Agora faça a mesma coisa que o exercício anterior, mas desta vez você 
# esta com pressa e para atravessar a rua basta que o sinal esteja vermelho 
# "OU" que não venha carro da esquerda e direita. Altere as variáveis 
# para verificar a resposta em comparação com ao exercício anterior. 
# Mostre na saída do programa o valor lógico.

sinal_vermelho = False
carro_vindo_direita = True
carro_vindo_esquerda = True
pode_atravessar = sinal_vermelho or not carro_vindo_direita and not carro_vindo_esquerda
print("Posso atravessar? ", pode_atravessar)

"""# Casting"""

texto = "olá"
numero = 2
decimal = 1.5
booleano = True
print(type(texto))
print(type(numero))
print(type(decimal))
print(type(booleano))

texto1 = "2"
texto2 = "1.5"
numero1 = int(texto1)
numero2 = float(texto2)
print(type(texto1))
print(type(numero1))
print(type(numero2))
print(numero1 + numero2)

num = 21.45646
inteira = int(num)
print("A parte inteira de %f é %d" % (num, inteira))

texto = "O número é: "
numero = 10.3
numero_em_string = str(numero)
print(texto, numero_em_string)
print(type(numero_em_string))

numero = 123
texto = str(numero)
numero_de_digitos = len(texto)
print("O número %s tem %d digitos " % (texto, numero_de_digitos))

vazio = None
numero_um = 15
numero_zero = 0
texto = "Texto"
texto_vazio = ""
decimal_zero = 0.0
decimal = 3.5

print("Variável tem valor: ", bool(vazio))

print("Número tem valor: ", bool(numero_um))
print("Número tem valor: ", bool(numero_zero))

print("String tem conteúdo: ", bool(texto))
print("String tem conteúdo: ", bool(texto_vazio))

print("Float tem valor: ", bool(decimal_zero))
print("Float tem valor: ", bool(decimal))

# 1 - Crie um programa que possui uma variável do “tipo string” 
# contendo um número que indique quanto você tem no banco. 
# Em seguida desconte mil deste valor e mostre na saída do programa.

saldo_em_texto = "4500.45"
saldo = float(saldo_em_texto)
total = saldo - 1000
print("Tenho no banco R$ %.2f " % (total))

# 2 - Crie um programa que indique se seu saldo bancário esta zerado 
# (valor lógico). Declare uma variável para guardar seu saldo bancário.

saldo = 0.0
esta_zerado = not bool(saldo)
print("Saldo zerado: ", esta_zerado)

# 3 - Crie um programa que contenha sua altura, mas deve somente mostrar 
# a parte inteira de sua altura na saída do programa, 
# pois queremos uma estimativa.

altura = 1.73
altura_inteira = int(altura)
print("Tenho pelo menos %i metros de altura " % (altura_inteira))

"""# Input"""

valor_escrito = input()
print(type(valor_escrito))
print(valor_escrito)

meu_nome = input()
print("Eu me chamo %s " % (meu_nome))

dia = input("Insira o dia: ")
mes = input("Insira o mês: ")
ano = input("Insira o ano: ")
print("A data inserida for %s/%s/%s " % (dia, mes, ano))

entrada_usuario = input("Digite 1 para verdadeiro e 0 para falso: ")
valor_inteiro = int(entrada_usuario)
valor_logico = bool(valor_inteiro)
print("Você escolheu: %s " % valor_logico)
print("ou ainda, você escolheu: %i " % (valor_inteiro))

# 1 - Crie um programa que leia por input dois números e realize
# a divisão entre ambos. Formate o print para mostrar o cálculo completo.

num1 = input("Insira o primeiro número: ")
num2 = input("Insira o segundo número: ")
divisao =  float(num1) / float(num2)
print("%s dividido por %s é %.2f" % (num1, num2, divisao) )

# 2 - Crie um programa que mostre o dia, mês, ano, hora, 
# minuto e segundos inseridos pelo usuário. Formate o valor.

dia = input("Insira o dia: ")
 mes = input("Insira o mês: ")
 ano = input("Insira o ano: ")
 hora = input("Insira a hora: ")
 minuto = input("Insira o minuto: ")
 segundo = input("Insira o segundo: ")
 print("%s/%s/%s %s:%s:%s" % (dia, mes, ano, hora, minuto, segundo))

"""# Operadores de Atribuição e Combinação de Operadores Lógicos"""

numero = 1 
numero = numero + 1
print(numero)

numero = 1
numero += 1
print(numero)

numero = 10 
numero = numero / 2
print(numero)

numero = 10 
numero /= 2
print(numero)

num = 10
booleana = (num == 10)
print(booleana)

num = 10
booleana = (num != 10)
print(booleana)

num1 = 10
num2 = 20
e_maior = num1 < num2
print(e_maior)

num1 = 21
num2 = 20
e_maior = num1 <= num2
print(e_maior)

num = 11
boolean = num > 0 and num < 10 
print(boolean)

#ver. se é tipo float e igual a 10.1. ou 20.2
num = 10.1
boolean = type(num) == float and (num == 10.1 or num == 20.2)
print(boolean)

# 1 - Crie um programa que responda se você foi aprovado numa prova. 
# Você somente foi aprovado numa prova se sua média for maior ou igual que 7 
# ou se sua nota no exame for maior ou igual a 5. Leia esses valores por input.

media_input = input("Digite sua média nas provas: ")
exame_input = input("Digite sua nota no exame: ")
media_prova = int(media_input)
nota_exame = int(exame_input)
aprovado = (media_prova >=7) or (nota_exame >= 5)
print("Aprovação: ", aprovado)

# 2 - Crie  um programa que diga se a senha esta correta e portanto você tem 
# acesso ao sistema. A senha devera ser salva no código, e a tentativa deve ser 
# lida por input.

senha_tentativa = input("Digite a senha: ")
senha_padrao = "1234"
print("Senha está correta? ", senha_tentativa == senha_padrao)

"""# Operadores sobre string"""

texto1 = "olá"
texto2 = ", "
texto3 = "tudo bem?"
texto_completo = texto1 + texto2 + texto3
print(texto_completo)

texto1 = "olá"
texto1 += " mundo"
print(texto1)

texto = "Python é bem produtivo,"
texto_repetido = texto * 3
print(texto_repetido)

texto = "exemplo"
print(texto[0])
print(texto[1])

texto = "exemplo"
print(texto[1:4])
print(texto[3:])''
print(texto[:5])

texto = "carro"
print(texto[-4])
print(texto[-4:])
print(texto[:-1])
print(texto[-5:-2])

texto = "metro"
print(texto[::-1])
print(texto[3::-1])
print(texto[3:1:-1])

texto = "023"
texto = "1" + texto[1:]
print(texto)

texto = "abcdefg"
texto = texto[:3] + texto[4:]
print(texto)

texto1 = "Olá"
texto2 = "Olá"
igual = texto1 == texto2
print("Textos são iguais? ", igual)

print("a" != "b")

texto = "Programação"
print("a" in texto)
print("e" in texto)
print("Programa" in texto)
print("Programa" not in texto)
print("Vinte" not in texto)

tamanho = len(texto)
print(tamanho)

# 1 - Crie um única string que contêm seu nome e sobrenome, em seguida use o 
# slicing para separar o nome em uma variável e o seu sobrenome em outra. 
# Printe esses valores.

nome_completo = "Carlos Silva"
nome = nome_completo[:6]
sobrenome = nome_completo[7:]
print("Nome: ", nome)
print("Sobrenome", sobrenome)

# 2 - Leia uma string através do input e retire o ultimo caractere.
string = input("Digite um texto qualquer: ")
string = string[:-1]
print(string)

# 3 - Faça um programa que leia uma string através do input e diga se 
# ela possui uma vogal.

texto = input("Digite uma palavra: ")
possui_vogal = ("a" in texto) or ("e" in texto) or ("i" in texto) or ("o" in texto)  or   ("u" in texto) 
print("Possui vogal? ", possui_vogal)

# 4 - Faça um programa que insira a palavra 'ABC' na primeira posição 
# de uma string lida por input.

texto = input("Digite uma palavra: ")
texto = "ABC" + texto[0:]
print(texto)

