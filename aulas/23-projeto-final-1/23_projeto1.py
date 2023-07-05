# -*- coding: utf-8 -*-
"""23.Projeto1.ipynb

Prof. Fernando Amaral

www.eia.ai

# Projeto Final I
"""

from numpy import cov, var, std, min, max, sqrt, mean
import matplotlib.pyplot as plt

class RegressaoLinear:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  
  def correlacao(self):
    covariacao = cov(self.x,self.y,bias=True)[0][1]
    variancia_x = var(self.x)
    variancia_y = var(self.y)
    return covariacao / sqrt(variancia_x * variancia_y)
  
  def inclinacao(self):
    stdx = std(self.x)
    stdy = std(self.y)
    return self.correlacao() * (stdy/stdx)

  def interceptacao(self):
    mediax = mean(self.x)
    mediay = mean(self.y)
    return mediay - mediax * self.inclinacao()
  
  def previsao(self,valor):
    intercepta = self.interceptacao()
    return (self.inclinacao() * valor) + intercepta

  def PlotaRegressao(self,titulo="Regressão Linear", nome_x="Eixo X", nome_y="Eixo y"):
    plt.xlabel(nome_x)
    plt.ylabel(nome_y)
    plt.title(titulo)

    plt.scatter(self.x,self.y)
    x_min = min(self.x)
    x_max = max(self.x)
    x_reta = [x_min,x_max]
    y_reta = [self.previsao(x_min), self.previsao(x_max)]
    plt.plot(x_reta, y_reta, c='r')
    plt.show()

idade = [18,23,25,33,34,43,48,51,58,63,67]
custo = [871,1100,1393,1654,1915,2100,2356,2698,2959,3000,3100]
regressao = RegressaoLinear(idade,custo)
preve = regressao.previsao(18)
print(preve)

regressao.PlotaRegressao("Plano de Saúde","Idade","Custo")

