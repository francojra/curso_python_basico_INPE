# Cusro R Básico
# Python – Estruturas de Controle  
# Instrutor: Lázaro Aparecido
# Instituição INPE
# Data: 15/10/25

## Exemplo 1

a = 2 
b = 12 
if a < 5 and b * a > 0 : 
   print("ok")

## Exemplo 2

a = 10 
b = 12 
if a < 5 and b * a > 0 : 
   print("ok") 
else: 
   print("nada bom") 

## Exemplo 3

nome = "pedro" 
 
if nome == "pedro": 
    idade = 21 
     
elif nome == "jose": 
     
    idade = 83 
 
else: 
 
    idade = 0 
 
print(idade) 

## Exemplo 4

x = int(input("Por favor, entre com um numero: ")) 
 
if x < 0: 
 
    x = 0 
    print('Numero negativo') 
 
elif x == 0: 
 
    print('Zero') 
 
elif x == 1: 
 
    print("Um") 
 
else: 
 
    print('Mais') 

## Exemplo 5

data = input("Entre 'y' ou 'n': ") 

if data[0] == 'y': 
    print("Voce digitou 'y'.")           # tecla 'y' 
 
elif data[0] == 'n': 
    print("Voce digitou 'n'.")           # tecla 'n' 
 
else: 
    print('tecla invalida!!!')           # outra tecla 

## Exemplo 6

letra = input("Digite uma letra minuscula: ") 
 
if letra <= 'k': 
    print('E uma das primeiras letras do alfabeto') 
 
if letra >= 'l': 
    print('E uma das ultimas letras do alfabeto') 

## Usando a biblioteca math

from math import sin, cos, pi 
 
graus = float(input('Digite um angulo (em graus): ')) 
 
angulo = graus * pi /180   # converte para radianos 
 
valor_cosseno = cos(angulo) 
print('cosseno do angulo e: %f' %valor_cosseno) 
 
valor_seno = sin(angulo) 
print('seno do angulo e: %f' %valor_seno)

print(pi)

## Instrução for

## Exemplo 1

jan_ken_pon = ["pedra","papel","cenoura"] 

for item in jan_ken_pon:
  print(item) 

## Exemplo 2

for i in range(1,4): 
  print("%da volta" % i) 
 
for i in range(1,10): 
  print("%da volta" % i) 

## Exemplo 3 - Medindo algumas strings: 
 
a = ['gato', 'janela', 'defenestrar'] 
  
for x in a: 
 
 print(x, len(x)) 
 
## Exemplo 4

principal = 1000.0 
taxa = 0.05         # taxa de juros 

print("Ano %21s" % "Valor depositado") 
 
for ano in range( 1, 11 ): 
    depositado = principal * (1.0 + taxa) ** ano 
    print("%4d%21.2f" % (ano, depositado)) 

## Exemplo 5

for x in range (1,11): 
 
 if x == 7: 
  break 
 print(x)

print("\n parou o loop em x = ", x) 

## Exemplo 6

for x in range (1,11): 
 
 if x == 5: 
  continue  # Pula o valor 5 e continua nos próximos valores do conjunto de 1,11
 print(x) 
 
print("\n 'continue' do Python foi usado para pular o valor 5")
