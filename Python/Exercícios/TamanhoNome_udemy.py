#Execício básico para manter a prática

#Enunciado
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input("Digite seu nome: ")
if len(nome) > 1:
    if len(nome) <= 4:
        print("Seu nome é curto !")
    elif len(nome) >= 5 and len(nome) <= 6:
        print("Seu nome tem uma quantidade normal de caracteres !")
    else:
        print("Seu nome é muito grande !")
else:
    print("Seu nome está vazio, digite mais de uma letra !")