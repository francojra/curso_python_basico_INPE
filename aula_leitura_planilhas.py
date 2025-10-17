# Cusro R Básico
# Python – Estruturas de Controle  
# Instrutor: Lázaro Aparecido
# Instituição INPE
# Data: 17/10/25

## Lendo planilhas

## Mostrando as folhas de uma planilha 

import openpyxl 

wb = openpyxl.load_workbook('medidas_satelite.xlsx') 
print(wb.sheetnames) 

wb.close() 
