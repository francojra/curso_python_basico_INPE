# Curso Básico de Python do INPE - 13/10/25

# Meu terceiro script

# Calculo da media 1

notas = [6, 7, 5, 8, 9]

soma = 0 
x = 0

while x < 5: 
    soma += notas[x] 

    x += 1 
 
print("Media: %5.2f" %(soma/x))

# Calculo da media 2

notas = [0, 0, 0, 0, 0] 
soma = 0 
 
x = 0

while x < 5: 
    notas[x] = float(input("Nota %d:" %x)) 
    soma += notas[x] 
    x += 1 
 
x = 0 
 
while x < 5: 
    print("Nota %d: %6.2f" %(x,notas[x])) 
    x += 1 
 
print("Media: %5.2f" %(soma/x))

# Trabalhando com índices

numeros = [0, 0, 0, 0, 0] 
x = 0 
 
while x < 5: 
    numeros[x] = int(input("Numero %d: " % (x+1))) 
    x += 1 
 
while True: 
    escolhido = int(input("Que posicao voce quer imprimir (0 para sair):"))  # Qual a posição dos números acima voce quer saber?
    if escolhido == 0: 
        break 
    print("Voce escolheu o numero: %d" %(numeros[escolhido-1])) 
 

