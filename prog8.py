# Funções

def f():
    return

print(f())

def f():
    return "Oi"

print(f())

def f(nome):
    return "Oi, "+nome+ "!"

print(f("amigo"))
print(f("Jeanne"))

def imprime_prato(p): 
    print("%s ...... %10.2f" % (p["nome"],p["preco"]))
    
p1 = {"nome":"Arroz com brocolis","preco": 9.90}  # Chaves indica que é um dicionário
p2 = {"nome":"Soja com legumes",  "preco": 7.80} 
p3 = {"nome":"Lentilhas", "preco": 4.80}

lista_pratos = [p1,p2,p3] # Colchetes indica uma lista

def imprime_cardapio (pratos): 
    print("cardapio para hoje\n") 
    for p in pratos:  # Para cada tipo de prato...
        imprime_prato(p)  # Imprime a lista de pratos (lista_pratos) com respectivos preços
 
    print("\n Total de pratos: %d" % len(pratos))  # Aqui vai mostrar o númerod e pratos contidos
    # em lista_pratos (vai aparecer no final do resultado).
 
imprime_cardapio(lista_pratos) 

def teclado(): 
    data = input('Entre com "y" ou "n": ') 

    if data[0] == 'y': 
        print('Voce digitou "Y"') 
 
    elif data[0] == 'n': 
        print('Voce digitou "n"') 
 
    elif data == 'abracadabra': 
        print('parabens, voce conseguiu!!!')

    else: 
        print('Voce digitou a tecla invalida')
        
teclado()

#calculo de um polinomio

def polinomio(a, b, c, x): 
    primeiro = a * x * x 
    segundo = b * x 
    terceiro = c 
    return primeiro + segundo + terceiro 
