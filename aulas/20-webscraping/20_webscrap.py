# -*- coding: utf-8 -*-
"""20_WebScrap.ipynb



Prof. Fernando Amaral

www.eia.ai

# Web Scraping
"""

import pandas as pd
import urllib3
from bs4 import BeautifulSoup
def faz_requisicao(site):
  urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
  manager = urllib3.PoolManager()
  return manager.request('GET',site,headers={'User-Agent': 'Mozilla/5.0'})

def le_site(site):
  response = faz_requisicao(site)
  return BeautifulSoup(response.data,'html.parser')

bs = le_site('https://www.horariodebrasilia.org/')
tag_hora = bs.find('p',id='relogio')
tag_hora.text

bs = le_site('https://www.horariodebrasilia.org/')
tag_hora = bs.find('h3',id='dia-topo')
tag_hora.text

def func_le_paises():
  bs = le_site('https://pt.wikipedia.org/wiki/Lista_de_pa%C3%ADses_por_riqueza_total')
  table = bs.find('table', style='text-align: right')
  if (table == None):
    raise Exception("Table não encontrada")
  
  corpo = table.find("tbody")
  if (corpo == None):
    raise Exception("Corpo da tabela não encontrado")

  items = corpo.find_all('tr')

  paises = []
  for item in items:
    dados = item.find_all('td')
    item_pais = []
    for dado in dados:
      item_pais.append(dado.text.replace('\xa0',''))

    if len(item_pais)>0:
      paises.append(item_pais)
  return paises

func_le_paises()

data = pd.DataFrame(func_le_paises(), columns=['Posição','País','Riqueza Total por Bilhões (USD)'])
data.set_index('Posição')

