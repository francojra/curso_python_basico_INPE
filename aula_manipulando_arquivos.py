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

## Exemplo 1

fn = input("Entre com o nome do arquivo: ") 
 
try: 
    f= open(fn, "r") 
    all = f.readlines() # Para ler todas as linhas
    f.close() 
 
    for line in all: # Para cada linha apresente o conteúdo dela
        print(line) 
except IOError as e: 
    print("error:", e) # Caso o sistema não possa parar, esse código emite o erro, mas continua nas próximas linhas de código

## Exemplo 2

infile = open('temperatura.txt','r') 

numbers = [float(line) for line in infile.readlines()] 

infile.close() 
  
for x in numbers: 
    print(x)

media = sum(numbers)/len(numbers)

## Exemplo 3

nome = input('nome do arquivo: ') 

arquivo = open(nome,'r')

contador = 0 
for linha in arquivo: 
 contador = contador + 1 # contador += 1
 
arquivo.close() 
print(contador) 

## Exemplo 4

## Ler o arquivo vendas.txt e mostrar na tela 

arquivo_entrada = open("vendas_python.txt","r") 

for linha in arquivo_entrada: 
    linha = linha.strip() 
    print(linha) 

arquivo_entrada.close() 

## Exemplo 5

f = open('tabela.txt','w') 

for i in range(1,51): 
    f.write(str(i)+'  '+str(i**2)+ '\n') 

f.close()
