# Cusro R Básico
# Python – Estruturas de Controle  
# Instrutor: Lázaro Aparecido
# Instituição INPE
# Data: 17/10/25

## Manipulando arquivos

arq = open("arquivo.txt","w") 

arq.write("oi meus amigos")

arq.close()

arq = open("arquivo.txt") # Abre o arquivo somente no modo leitura

x = arq.read()

arq.close()

print(x)

## Acesso direto a arquivos

fn = input("Entre com o nome do arquivo: ") 
 
try: 
    f= open(fn, "r") 
    all = f.readlines() # Para ler todas as linhas
    f.close() 
 
    for line in all: # Para cada linha apresente o conteúdo dela
        print(line) 
except IOError as e: 
    print("error:", e) 
