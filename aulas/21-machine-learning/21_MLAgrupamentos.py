# -*- coding: utf-8 -*-
"""22_MLAgrupamentos.ipynb


Prof. Fernando Amaral

www.eia.ai

# Machine Learning
"""

from sklearn import datasets
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

iris = datasets.load_iris()

print("dados: ", iris.data)

print("classe: ", iris.target)

print("nome classes: ", iris.target_names)

print("nome dos atributos ", iris.feature_names)

unicos, quantidade = np.unique(iris.target, return_counts = True)
print(unicos)
print(quantidade)

cluster = KMeans(n_clusters=3)
cluster.fit(iris.data)

agrupamentos = cluster.labels_
print(agrupamentos)

unicos, quantidade = np.unique(agrupamentos, return_counts = True)
print(unicos)
print(quantidade)

resultados = confusion_matrix(iris.target, agrupamentos)
print(resultados)

acuracia = accuracy_score(iris.target, agrupamentos)
print(acuracia)

plt.scatter(iris.data[agrupamentos ==0,0], iris.data[agrupamentos==0,1], c='green', label='Setosa')
plt.scatter(iris.data[agrupamentos ==1,0], iris.data[agrupamentos==1,1], c='red', label='Versicolor')
plt.scatter(iris.data[agrupamentos ==2,0], iris.data[agrupamentos==2,1], c='blue', label='Virginica')
plt.legend()

