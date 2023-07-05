# -*- coding: utf-8 -*-
"""22_MachineLearning.ipynb



Prof. Fernando Amaral

www.eia.ai

# Machine Learning
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.ensemble import RandomForestClassifier

credito = pd.read_csv('Credit.csv')
credito.head()

labelencoder = LabelEncoder()
for i in credito.select_dtypes(include='object'):
  if i != 'class':
    credito[i] = labelencoder.fit_transform(credito[i])

credito.head()

previsores = credito.iloc[:,0:20].values
classe = credito.iloc[:,20].values

previsores

print(type(classe))

X_treinamento, X_teste, y_treinamento, y_teste = train_test_split(previsores, classe, test_size=0.3, random_state=0)

print(X_treinamento.shape)
print(X_teste.shape)
print(y_treinamento.shape)
print(y_teste.shape)

floresta = RandomForestClassifier(n_estimators = 500,random_state=0)
floresta.fit(X_treinamento,y_treinamento)

previsoes = floresta.predict(X_teste)
print(previsoes)

confusao = confusion_matrix(y_teste,previsoes)
print(confusao)

taxa_acerto = accuracy_score(y_teste,previsoes)
print(taxa_acerto)

