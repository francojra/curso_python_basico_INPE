# Cusro R Básico
# Python – Estruturas de Controle  
# Instrutor: Lázaro Aparecido
# Instituição INPE
# Data: 17/10/25

## Lendo arquivos da internet

from urllib.request import urlopen 

url = "https://raw.githubusercontent.com/FinYang/tsdl/master/data-raw/ecology1/hopedale.dat" 

web_page = urlopen(url) 

for i in range(1,4): 
    linha = web_page.readline() 

tabela = []

for line in web_page: 
    line = line.strip() 
    line = str(line,'utf-8') 
    dados = float(line) 
    tabela.append(dados) 
    print(dados) 
 
web_page.close()

## No terminal colocar 'python -m pip install matplotlib'

from matplotlib import pyplot as plt

plt.plot(tabela) 
plt.show() 
