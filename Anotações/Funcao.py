def saudacao(nome):
    print(f"Olá, {nome}!")

# def soma(a,b):
#     print(a+b)

# saudacao("Pedro")
# soma(2,3)

def soma(*args):
    total = 0
    for numero in args:
        print("Índice:", numero)
        total += numero
    print(total)
    
soma(1, 2, 3, 4) #Espaçamento entre os elementos