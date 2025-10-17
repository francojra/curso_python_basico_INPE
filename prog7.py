# lendo_csv_4.py 
 
import pandas as pd 
     
df1 = pd.read_csv("https://datahub.io/core/gold-prices/_r/-/data/annual.csv") 
 
print(df1)

import matplotlib.pyplot as plt 
 
plt.plot(df1.Date, df1.Price) 
 
plt.show() 

# lendo_csv_3.py

import pandas as pd

df1 = pd.read_csv("amostras_ar.csv") 
print(df1)

# cria o arquivo saida.csv 
# sem a primeira linha 
# com index = True, insere em cada linha, um indice

df2 = df1.to_csv('saida.csv', index = True, header = False) 
 
