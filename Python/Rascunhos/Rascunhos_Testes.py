'''Tabuada'''
# O fim deve ser TAMANHO + 1 para incluir o número 10
#for i in range(1, 11, 1):
#    print(f'--- Tabuada de {i} ---')
#    for j in range(1, 11, 1):
#        print(f'{i} x {j} = {i * j}')
#    print('\n')

# from typing import Counter

'''Contador de vogais e consoantes'''
# string = input("Digite uma palavra: ")
# vogais = "aeiouáéíóúâêîôûãõ"

# vogais_na_string = ''
# consoantes_na_string = ''
# contador_vogais = 0
# contador_consoantes = 0

# #Conta quantidade de letras
# print(f'A palavra digitada contém {len(string.replace(" ", ""))} letras !') #Ignora espaços

# for letras in string.upper():
#     if letras.isalpha():
#         if letras in vogais.upper():
#             if letras in vogais_na_string:
#                 continue
#             else:
                # contador_vogais += 1
#                 vogais_na_string += letras + " "
#         else:
#             if letras in consoantes_na_string:
#                 continue
#             else:
#                 contador_consoantes +=1
#                 consoantes_na_string += letras + " "
            
# print('Vogais:', vogais_na_string)
# print('Consoantes:', consoantes_na_string)

'''Impressão de números pares e impares'''

# pares = []
# impares = []

# for i in range(20):
#     pares.append(i if i % 2 == 0 else impares.append(i))

# pares = [item for item in pares if item is not None] 
# print(*pares,"\n---------\n", *impares)

'''Somatória de Listas'''

# notas = [8.5, 7.0, 9.2, 5.5, 6.8]
# soma = 0

# for nota in notas:
#     soma += nota

# soma /= 5
# print(soma)

'''Maior e Menor'''

# import random

# numeros = []

# maior = 0

# for i in range(20):
#     numeros.append(random.randint(0,100))

# print(*numeros)
# menor = numeros[0]

# for tamanho in numeros:

#     if tamanho > maior:
#         maior = tamanho
#     if menor > tamanho:
#         menor = tamanho

# print('Maior:',maior)
# print('Menor:',menor)