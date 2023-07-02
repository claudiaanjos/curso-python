# -*- coding: utf-8 -*-
"""15_Matplotlib.ipynb


Prof. Fernando Amaral

www.eia.ai

# Matplotlib
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4,5])
y = np.array([2,4,6,8,10])

plt.plot(x,y)
plt.show()

import matplotlib.pyplot as plt
import numpy as np

x = np.array([0,1,2,3,4,5])
y = x * 2

plt.plot(x,y)
plt.show()

import matplotlib.pyplot as plt
import numpy as np
y = np.array([-2,2,10,4,5])
x = np.array(["segunda","terça","quarta","quinta","sexta"])
plt.plot(x,y)
plt.show()

import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([1,2,3,4,5])
y1 = x1 * 2

x2 = np.array([5,10,15])
y2 = x2 + 2

plt.plot(x1,y1)
plt.plot(x2,y2)
plt.show()

import matplotlib.pyplot as plt
import numpy 

x1 = numpy.arange(1,10)
y1 = x1 * 2

x2 = numpy.arange(1,10)
y2 = x2 ** 2

plt.plot(x1,y1)
plt.plot(x2,y2)
plt.axis([0,10,-1,50])
plt.show()

import matplotlib.pyplot as plt
import numpy 

x1 = numpy.arange(1,10)
y1 = x1 * 2

x2 = numpy.arange(1,10)
y2 = x2**2

plt.plot(x1,y1)
plt.plot(x2,y2)
plt.xlim(0,10)
plt.ylim(-1,50)
plt.show()

import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4,5])
y = x*2

plt.xlabel("Vendas")
plt.ylabel("Temperatura")

plt.plot(x,y)
plt.show()

import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4,5])
y = x*2

plt.xlabel("Vendas")
plt.ylabel("Temperatura")
plt.title("Gráfico de Vendas")

plt.plot(x,y)
plt.show()

import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4,5])
y = x*2

plt.xlabel("Vendas")
plt.ylabel("Temperatura")
plt.title("Gráfico de Vendas", y= 1.1)

plt.plot(x,y)
plt.show()

import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4,5])
y = x*2

plt.xlabel("Vendas")
plt.ylabel("Temperatura")
plt.title("Gráfico de Vendas", y= 0.9, loc="left", x=0.01)

plt.plot(x,y)
plt.show()

import matplotlib.pyplot as plt
import numpy as np

font_props = {
    'family': 'cmb10',
    'color' : 'blue',
    'weight': 'bold',
    'size'  : 18,
}
x = np.arange(0,20,0.5)
y = x**6

plt.xlabel("Vendas", fontdict = font_props)
plt.ylabel("Temperatura", fontdict = font_props)
plt.title("Vendas", fontdict = font_props)

plt.plot(x,y)
plt.show()

import matplotlib.pyplot as plt
import numpy as np

font_props = {
    'family': 'DejaVu Sans',
    'color' : 'blue',
    'weight': 'bold',
    'size'  : 16,
}

font_props2 = {
    'family': 'DejaVu Sans',
    'color' : 'green',
    'weight': 'normal',
    'size'  : 18,
}
x = np.arange(-10,10,0.1)
y = x**2

plt.text(-5,50, "É uma parábola", fontdict = font_props2)

plt.xlabel("Vendas", fontdict = font_props)
plt.ylabel("Temperatura", fontdict = font_props)
plt.title("Vendas", fontdict = font_props)

plt.plot(x,y)
plt.show()

import matplotlib.pyplot as plt
import numpy as np

font_props = {
    'family': 'DejaVu Sans',
    'color' : 'blue',
    'weight': 'bold',
    'size'  : 16,
}

font_props2 = {
    'family': 'DejaVu Sans',
    'color' : 'green',
    'weight': 'normal',
    'size'  : 10,
}
x = np.arange(-10,10,0.1)
y = x**2


plt.figure(figsize=(10,10))

plt.text(-5,50, "É uma parábola", fontdict = font_props2)

plt.xlabel("Vendas", fontdict = font_props)
plt.ylabel("Temperatura", fontdict = font_props)
plt.title("Vendas", fontdict = font_props)

plt.plot(x,y)
plt.show()

import matplotlib.pyplot as plt
import numpy

x = numpy.arange(0,10,0.5)
y = x**6

plt.plot(x,y, c='Red')

plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.title("A função y = x**6")
plt.show()

import matplotlib.pyplot as plt
import numpy

x = numpy.arange(0,10,0.5)
y = x**6

plt.plot(x,y, color='y')

plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.title("A função y = x**6")
plt.show()

import matplotlib.pyplot as plt
import numpy

x = numpy.arange(0,10,0.5)
y = x**6

plt.plot(x,y, c='#e7044c')

plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.title("A função y = x**6")
plt.show()

import matplotlib.pyplot as plt
import numpy
x = numpy.arange(0,10)
y = 2*x + 1

plt.xlabel("Vendas")
plt.ylabel("Temperatura")
plt.title("Gráfico de Vendas")

plt.plot(x,y,c='b', linewidth= '5.5')
plt.show()

import matplotlib.pyplot as plt
import numpy
x = numpy.arange(0,10)
y = 5*x + 1

plt.xlabel("Vendas")
plt.ylabel("Temperatura")
plt.title("Gráfico de Vendas")
#solid, dashed, dotted, dashdot
plt.plot(x,y,c='g', linewidth= '6.5', linestyle='dashdot')
plt.show()

import matplotlib.pyplot as plt
import numpy

x1 = numpy.arange(0,20,0.5)
y1 = numpy.cos(x1)

x2 = numpy.arange(0,20,0.5)
y2 = numpy.cos(x2)*2

plt.xlabel("Vendas")
plt.ylabel("Temperatura")
plt.title("Gráfico de Vendas")

plt.plot(x1,y1, c='g', lw='6.5', ls='dashed', label="Vendas")
plt.plot(x2,y2, c='b', lw='3.5', ls='solid', label="Temperatura")
plt.legend(loc='upper right')
plt.show()

import matplotlib.pyplot as plt
import numpy

x1 = numpy.arange(0,20,0.5)
y1 = numpy.cos(x1)

x2 = numpy.arange(0,20,0.5)
y2 = numpy.cos(x2)*2

plt.xlabel("Vendas")
plt.ylabel("Temperatura")
plt.title("Gráfico de Vendas")

plt.plot(x1,y1, c='g', lw='6.5', ls='dashed', label="Vendas", alpha=0.3)
plt.plot(x2,y2, c='b', lw='3.5', ls='solid', label="Temperatura")
plt.legend(loc='upper right')
plt.show()

import matplotlib.pyplot as plt
import numpy

x = numpy.arange(0,19)
y = -x ** 4
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.title("Gráfico da função y = -x**4")
plt.plot(x,y, c='orange', lw='1.5', marker = '|')
plt.show()

import matplotlib.pyplot as plt
import numpy

x1 = numpy.arange(0,20,0.5)
y1 = numpy.cos(x1)

x2 = numpy.arange(0,20,0.5)
y2 = numpy.cos(x2)*2

plt.xlabel("Vendas")
plt.ylabel("Temperatura")
plt.title("Gráfico de Vendas")

plt.plot(x1,y1, c='g', lw='1.5', ls='dashed', label="Vendas", marker='+')
plt.plot(x2,y2, c='b', lw='1', ls='solid', label="Temperatura", marker='D', 
         markersize='8', markerfacecolor = 'red', markeredgecolor='green' )
plt.legend(loc='upper right')
plt.show()

import matplotlib.pyplot as plt
import numpy

x1 = numpy.arange(1,100)
y1 = x1**2

plt.plot(x1,y1)
plt.grid()
plt.show()

import matplotlib.pyplot as plt
import numpy

x1 = numpy.arange(1,100)
y1 = x1**2

plt.plot(x1,y1)
plt.grid(
    c ='b',
    ls = 'dotted',
    lw = 1.5, 
    alpha = 0.5
)
plt.show()

import matplotlib.pyplot as plt
import numpy

x1 = numpy.arange(1,100)
y1 = x1**2
plt.plot(x1,y1, color='r')
plt.grid(c='b', ls = 'dotted', lw = 1.5)
plt.xticks([1,2,3,4,10,20,40,80,120,180])
plt.show()

import matplotlib.pyplot as plt
print(plt.style.available)

import matplotlib.pyplot as plt
import numpy
x1 = numpy.arange(1,100)
y1 = x1**2
plt.style.use("classic")
plt.grid(c='gray')
plt.plot(x1,y1)
plt.show()

import matplotlib.pyplot as plt
import numpy
x1 = numpy.arange(0,20,0.5)
y1 = x1*2

x2 = numpy.arange(0,20,0.5)
y2 = numpy.sin(x2)

plt.subplot(1,2,1)
plt.title("A primeira função")
plt.plot(x1,y1, c='g', lw = '6.5', ls='dashed')

plt.subplot(1,2,2)
plt.title("A segunda função")
plt.plot(x2,y2, c='r', lw= '3.5', ls='solid')

plt.show()

import matplotlib.pyplot as plt
import numpy

x1 = numpy.arange(0,20,0.5)
y1 = numpy.cos(x1)

x2 = numpy.arange(0,20,0.5)
y2 = numpy.cos(x1)*2

plt.subplot(1,2,1)
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.title("A primeira função coseno")
plt.plot(x1,y1, c='g', lw='6.5', ls='dashed', label='y=cos(x)')
plt.legend(loc='lower right')
plt.ylim(-3, 2)


plt.subplot(1,2,2)
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.title("A segunda função coseno")
plt.plot(x2,y2, c='b', lw='3.5', ls='solid', label='y=cos(x)*2')
plt.legend(loc='lower right')
plt.ylim(-3, 2)

plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt
import numpy

x1 = numpy.arange(0,20,0.5)
y1 = numpy.cos(x1)

x2 = numpy.arange(0,20,0.5)
y2 = numpy.cos(x1)*2

plt.subplot(2,2,1)
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.title("A primeira função coseno")
plt.plot(x1,y1, c='g', lw='6.5', ls='dashed', label='y=cos(x)')
plt.legend(loc='lower right')
plt.ylim(-3, 2)

plt.subplot(2,2,2)
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.title("A primeira função coseno")
plt.plot(x1,y1, c='r', lw='6.5', ls='dashed', label='y=cos(x)')
plt.legend(loc='lower right')
plt.ylim(-3, 2)


plt.subplot(2,2,3)
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.title("A segunda função coseno")
plt.plot(x2,y2, c='b', lw='3.5', ls='solid', label='y=cos(x)*2')
plt.legend(loc='lower right')
plt.ylim(-3, 2)

plt.subplot(2,2,4)
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.title("A segunda função coseno")
plt.plot(x2,y2, c='y', lw='3.5', ls='solid', label='y=cos(x)*2')
plt.legend(loc='lower right')
plt.ylim(-3, 2)

plt.subplots_adjust(hspace=0.8, wspace=0.4)
plt.suptitle("Meus gráficos",y=1.03 )

plt.show()

import matplotlib.pyplot as plt
import numpy
x = numpy.array([1,2,3,4,5])
y = numpy.array([2,4,6,8,10])

plt.bar(x,y, color='g', width=0.3)
plt.show()

import matplotlib.pyplot as plt
import numpy

y = numpy.array([1,2,3])
x = numpy.array(['Um','Dois','Três'])
plt.barh(x,y, color='r' , height=0.4)

plt.title("Gráfico de Barras")
plt.ylabel("Números")
plt.xlabel("Valores")
plt.show()

import matplotlib.pyplot as plt
import numpy

valores_esquerda = numpy.arange(0,6)
valores_direita = numpy.arange(6,0,-1)
ys = numpy.arange(6)

plt.barh(ys,valores_esquerda, color='y')
plt.barh(ys, -valores_direita, color='c')

plt.legend(['a','b'])

plt.title("Gráfico de barras dividido")
plt.ylabel("Valores de Y")
plt.xlabel("Valores esquerda vs direita")
plt.show()

import matplotlib.pyplot as plt
import numpy

valores_esquerda = numpy.arange(0,6)
valores_direita = numpy.arange(6,0,-1)
xs = numpy.arange(6)

plt.bar(xs,valores_esquerda, color='y')
plt.bar(xs, -valores_direita, color='c')

plt.legend(['a','b'])

plt.title("Gráfico de barras dividido")
plt.ylabel("Valores de Y")
plt.xlabel("Valores esquerda vs direita")
plt.show()

import matplotlib.pyplot as plt
import numpy as np

xs = np.array(['Janeiro','Fevereiro','Março','Abril'])
time1 = np.array([5,10,15,20])
time2 = np.array([1,2,4,9])
time3 = np.array([5,8,2,2])
time4 = np.array([6,7,2,1])

plt.bar(xs,time1, color='red', width =0.5)
plt.bar(xs,time2,bottom=time1, color='yellow', width =0.5)
plt.bar(xs,time3,bottom=time2+time1  ,color='orange', width =0.5)
plt.bar(xs,time4,bottom=time1+time2+time3 , color='green', width =0.5)

plt.title("Rendimento no Esporte")
plt.xlabel("Meses")
plt.ylabel("Gols")
plt.legend(['Time1','Time2','Time3','Time4'])
plt.show()

import matplotlib.pyplot as plt
import numpy as np

xs = np.array(['Janeiro','Fevereiro','Março','Abril'])
time1 = np.array([5,10,15,20])
time2 = np.array([1,2,4,9])
time3 = np.array([5,8,2,2])
time4 = np.array([6,7,2,1])

plt.barh(xs,time1, color='red')
plt.barh(xs,time2,left=time1, color='yellow')
plt.barh(xs,time3,left=time2+time1  ,color='orange')
plt.barh(xs,time4,left=time1+time2+time3 , color='green')
plt.xlim(0,40)
plt.title("Rendimento no Esporte")
plt.xlabel("Meses")
plt.ylabel("Gols")
plt.legend(['Time1','Time2','Time3','Time4'])
plt.show()

import matplotlib.pyplot as plt
import numpy as np

alturas = np.array([1.75, 1.50, 1.46, 1.65, 1.74, 1.76, 1.80, 1.73, 1.89, 1.90, 1.61])
plt.hist(alturas, color='r', edgeColor='b', bins = [1.40, 1.50, 1.60, 1.70, 1.80, 1.90,2])
plt.xlabel("Alturas")
plt.ylabel("Ocorrências")
plt.title("Distribuição das alturas")
plt.show()

import matplotlib.pyplot as plt
import numpy as np

alturas = np.array([1.75, 1.50, 1.46, 1.65, 1.74, 1.76, 1.80, 1.73, 1.89, 1.90, 1.61])
plt.hist(alturas, color='r', edgeColor='b', bins = 7)
plt.xlabel("Alturas")
plt.ylabel("Ocorrências")
plt.title("Distribuição das alturas")
plt.show()

import matplotlib.pyplot as plt
import numpy as np

alturas = np.array([1.75, 1.50, 1.46, 1.65, 1.74, 1.76, 1.80, 1.73, 1.89, 1.90, 1.61])
plt.hist(alturas, color='r', edgeColor='b')
plt.xlabel("Alturas")
plt.ylabel("Ocorrências")
plt.title("Distribuição das alturas")
plt.show()

import matplotlib.pyplot as plt
import numpy as np

alturas_mundiais = np.random.normal(loc=175, scale=11, size=1000)/100
alturas_brasil = np.random.normal(loc=185, scale=9, size=1000)/100

plt.hist(alturas_mundiais, bins=7, color='b', edgeColor='g', alpha=0.5)
plt.hist(alturas_brasil, bins=7, color='y', edgeColor= 'r', alpha=0.5)
plt.legend(["Altura Mundial","Altura Brasil"])
plt.xlabel("Alturas")
plt.ylabel("Ocorrências")
plt.title("Distriubição de alturas")
plt.show()

import matplotlib.pyplot as plt
import numpy as np

classes = np.array(['Classe baixa','Classe média','Classe alta'])
dados = np.array([10,30,80])
cores = np.array(['r','g','y'])
plt.pie(dados, labels=classes, colors=cores)
plt.title("Distribuição de Classes")
plt.legend(classes, loc='upper right')
plt.show()

import matplotlib.pyplot as plt
import numpy as np

classes = np.array(['Classe baixa','Classe média','Classe alta'])
dados = np.array([10,30,80])
cores = np.array(['r','g','y'])

plt.figure(figsize=(7,7))
plt.pie(dados, labels=classes, colors=cores, shadow=True, startangle=90)
plt.title("Distribuição de Classes")
plt.legend(classes, loc='upper right')
plt.show()

import matplotlib.pyplot as plt
import numpy as np

classes = np.array(['Classe baixa','Classe média','Classe alta'])
dados = np.array([10,30,80])
cores = np.array(['r','g','y'])
offsets = np.array([0.2,0.03,0.03])

plt.figure(figsize=(7,7))
plt.pie(dados, labels=classes, colors=cores, shadow=True, startangle=90, radius=0.8, explode=offsets)
plt.title("Distribuição de Classes")
plt.legend(classes, loc='upper right')
plt.show()

import matplotlib.pyplot as plt
import numpy as np

classes = np.array(['Classe baixa','Classe média','Classe alta'])
dados = np.array([10,30,80])
cores = np.array(['r','g','y'])
offsets = np.array([0.2,0.03,0.03])

edge_props = {
    'linewidth' : 1,
    'edgecolor' : 'black' ,
    'linestyle' : 'solid'
}

plt.figure(figsize=(7,7))
plt.pie(dados, labels=classes, colors=cores, shadow=True, startangle=90, radius=0.8, explode=offsets, wedgeprops=edge_props)
plt.title("Distribuição de Classes")
plt.legend(classes, loc='upper right')
plt.show()

import matplotlib.pyplot as plt
import numpy as np

classes = np.array(['Classe baixa','Classe média','Classe alta'])
dados = np.array([10,30,80])
cores = np.array(['r','g','y'])
offsets = np.array([0.2,0.03,0.03])

edge_props = {
    'linewidth' : 1,
    'edgecolor' : 'black' ,
    'linestyle' : 'solid'
}

text_props = {
    'color' : 'black',
    'style' : 'oblique' ,
    'size' : 8
}

plt.figure(figsize=(7,7))
plt.pie(dados, labels=classes, colors=cores, shadow=True, startangle=90, 
        radius=0.8, explode=offsets, wedgeprops=edge_props, textprops = text_props, autopct= lambda value: '%.2f %s' % (value, '%') )


plt.title("Distribuição de Classes")
plt.legend(classes, loc='upper right')
plt.show()

import matplotlib.pyplot as plt
import numpy as np


x = numpy.arange(0,10)
y = numpy.array([1,4,9,12,4,7,4,9,2,1])

plt.scatter(x,y)
plt.title("Gráfico de Dispersão")
plt.show()

import matplotlib.pyplot as plt
import numpy 

plt.style.use('bmh')
x = numpy.arange(0,10)
y = numpy.array([1,4,9,12,4,7,4,9,2,1])

cores = numpy.array(['r','r','g','b','b','r','y','brown','pink','gray'])

plt.scatter(x,y, c=cores, marker='o', s=200)
plt.title("Gráfico de Dispersão")
plt.show()

import matplotlib.pyplot as plt
import numpy 

plt.style.use('bmh')
x = numpy.arange(0,10)
y = numpy.array([1,4,9,12,4,7,4,9,2,1])
z = numpy.array([100,50,150,200,100,120,130,80,90,144])

cores = numpy.array(['r','r','g','b','b','r','y','brown','pink','gray'])

plt.scatter(x,y, c=cores, marker='o', s=z)
plt.title("Gráfico de Dispersão")
plt.show()

import matplotlib.pyplot as plt
import numpy

plt.style.use('bmh')
x = numpy.arange(0,10)
y = numpy.array([1,4,9,12,4,7,4,9,2,1])

z = numpy.array([25,50,75])
z_indices = numpy.array([0,2,1,1,1,0,2,1,1,0])

cores = numpy.array(['r','g','b'])
z_cores = numpy.array([0,1,1,0,1,2,2,0,1,0])

plt.scatter(x,y, c=cores[z_cores], marker='o', s=z[z_indices])
plt.title("Gráfico de Dispersão")
plt.show()

import matplotlib.pyplot as plt
import numpy 

plt.style.use('bmh')
x = numpy.arange(0,10)
y = numpy.array([1,4,9,12,4,7,4,9,2,1])

z = numpy.array([125,250,375])
z_indices = numpy.array([0,2,1,1,1,0,2,1,1,0])

cores = numpy.array(['r','g','b'])
z_cores = numpy.array([0,1,1,0,1,2,2,0,1,0])

z_bordas = numpy.array([2,0,0,1,2,1,1,1,2,1])

plt.scatter(x,y, c=cores[z_cores], marker='^', s=z[z_indices], edgecolors=cores[z_bordas], linewidth=2)
plt.title("Gráfico de Dispersão")
plt.show()

import matplotlib.pyplot as plt
import numpy 

plt.style.use('bmh')
x = numpy.arange(0,10)
y = numpy.array([1,4,9,12,4,7,4,9,2,1])

x1 = numpy.arange(3,13)
y1 = numpy.array([4,4,5,12,4,7,7,9,9,1])


z = numpy.array([125,250,375])
z_indices = numpy.array([0,2,1,1,1,0,2,1,1,0])

cores = numpy.array(['r','g','b'])
z_cores = numpy.array([0,1,1,0,1,2,2,0,1,0])

z_bordas = numpy.array([2,0,0,1,2,1,1,1,2,1])

plt.scatter(x,y, c=cores[z_cores], marker='^', s=z[z_indices], edgecolors=cores[z_bordas], linewidth=2)

plt.scatter(x1,y1, c=cores[z_cores], marker='o', s=z[z_indices], edgecolors=cores[z_bordas], linewidth=2)


plt.title("Gráfico de Dispersão")
plt.show()

import matplotlib.pyplot as plt
import numpy 
plt.style.use("default")

x = np.random.randint(10,size=10)
y = np.random.randint(10,size=10)
x2 = np.random.randint(10,size=10)
y2 = np.random.randint(10,size=10)

plt.scatter(x,y, label='Meninos')
plt.scatter(x2,y2, label='Meninas')
plt.title("Gráfico de Dispersão")
plt.legend()
plt.show()

# 1 - Plote a função y = 5x + 1. Onde x vai de 0 até 10. Use marcadores do tipo 
# quadrado. Informe o título do gráfico e  eixos x e y. 
# De as cores  vermelho aos marcadores e azul a reta.

import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0,11)
y = 5*x + 1

plt.title("Função y = 5x + 1")
plt.ylabel("Eixo y")
plt.xlabel("Eixo x")

plt.plot(x,y,c='b',mfc='r',marker='s')
plt.show()

# 2 - Plote os dados a seguir em um gráfico com linhas:
# Valor do real em relação ao dólar (dados fictícios):
# 2016: 3,15
# 2017: 3,26
# 2018: 3,88
# 2019: 4,30
# 2020: 5,33
# 2021: 5,45
# 2022: 5,39

import matplotlib.pyplot as plt
import numpy as np
x = np.arange(2016,2023)
y = np.array([3.15,3.26,3.88,4.3,5.33,5.45,5.39])
plt.xlabel("Ano")
plt.ylabel("Valor do real (R$)")
plt.title("Variação Dolar vs Real")
plt.plot(x,y,c='b', mfc='b', marker='o')

plt.show()

#  3 - Faça o mesmo exercício anterior em um gráfico de barras, 
# compare os resultados.

import matplotlib.pyplot as plt
import numpy as np
x = np.arange(2016,2023)
y = np.array([3.15,3.26,3.88,4.3,5.33,5.45,5.39])
plt.xlabel("Ano")
plt.ylabel("Valor do real (R$)")
plt.title("Variação Dolar vs Real")
plt.bar(x,y,color='b')

plt.show()

# 4 - Com base nos dados do exercício anterior. 
# Plote dois gráficos separados (um no lado do outro). 
# Em um você ira plotar o gráfico da variação dólar X real. 
# E no outro ira plotar o PIB per Capita do Brasil, nos mesmo anos. 
# Escolha o tipo de gráfico que preferir.
# Dados do PIB (dados fictícios):
# 2016: 8710,50 USD
# 2017: 9928,50
# 2018: 9151,58
# 2019: 8897,29
# 2020: 6795,32
# 2021: 7500,21
# 2022: 7542,34

import matplotlib.pyplot as plt
import numpy as np
x = np.arange(2016,2023)
y1 = np.array([3.15,3.26,3.88,4.3,5.33,5.45,5.39])
y2 = np.array([8710.5,9928.5,9151.58,8897.29,6795.32,7500.21,7542.34])

plt.subplot(1,2,1)
plt.xlabel("Ano")
plt.ylabel("Valor do Real (R$)")
plt.title("Variação Dolar X Real")
plt.bar(x,y1,color='b', width=0.7)

plt.subplot(1,2,2)
plt.xlabel("Ano")
plt.ylabel("Pib per Capita")
plt.title("Variação do Pib per Capita")
plt.plot(x,y2,c='y', lw='3.5', ls='solid', marker='s', mfc='g')

plt.suptitle("Situação Econômica do Brasil", y=1.05)
plt.tight_layout()
plt.show()

# 5 - Crie um gráfico de pizza para representar os seguintes dados:
# Destino de exportações do Brasil:
# 	China: 30% Estados Unidos: 40% Europa: 20% Outros: 10%

import matplotlib.pyplot as plt
import numpy as np

paises = np.array(['China','Estados Unidos','Europa','Outros'])
dados = np.array([30,40,20,10])
cores = np.array(['blue','y','g','brown'])

edge_props ={
    'linewidth' : 1,
    'edgecolor' : 'black',
    'linestyle' : 'dashed'
}

text_props = {
    'color': 'black',
    'style': 'oblique',
    'size' : 13,
    'family' : 'sans'
}

plt.figure(figsize=(7,7))
plt.pie(dados,labels=paises,colors = cores, shadow=True, radius=0.8, startangle=90, autopct = lambda value : '%.2f %s' % (value,'%'), 
        textprops = text_props)
plt.legend(paises, loc="lower right")
plt.tight_layout()
plt.show()

# 6 - Crie um gráfico de dispersão mostrando a relação entre peso e altura 
# de algumas pessoas. Analise os resultados
#	Dados altura = [1.60, 1.62, 1.65, 1.65, 1.70, 1.70, 1.75, 1.80. 1.85, 
  1.90, 1.90, 1.95, 2.00] 
#	Dados peso = [60, 61, 64, 67, 70, 73, 75, 80. 85, 90, 85, 1.95, 2.00]

import matplotlib.pyplot as plt
import numpy as np
x = np.array([1.60, 1.62, 1.65, 1.65, 1.70, 1.70, 1.75, 1.80, 1.85,1.90, 1.90, 1.95, 2.00])
y = np.array([60, 61, 64, 67, 70, 73, 75, 80, 85, 90, 85, 95, 100])

ax = plt.scatter(x,y)
plt.title("Relação Peso e Altura")
plt.xlabel("Altura")
plt.ylabel("Peso")
plt.show()

