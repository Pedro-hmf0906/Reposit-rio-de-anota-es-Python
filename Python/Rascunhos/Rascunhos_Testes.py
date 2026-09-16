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

# numeros = []

# while True:
# 	numero_novo = input('Digite um número para adicionar: ')

# 	if numero_novo.isdigit():
# 		numero_novo = int(numero_novo)

# 	if numero_novo == 0:
# 		break
# 	numeros.append(numero_novo)
				
# print('Maior :', max(numeros))
# print('Menor :', min(numeros))
# print('Média :', sum(numeros) / (1 + len(numeros)))
# print('Soma  :' , sum(numeros))
# print(*numeros , "0")

"""VERIFICADOR DE PALÍNDROMO"""

# palavra = input('Digite uma palavra: ').upper().replace(" ", "")
# palavra_formada = ""

# for i in range(len(palavra)):
# 	if palavra[i] == palavra[-1 - i]:
# 		palavra_formada += palavra[i]
# 	else: 
# 		break

# if palavra_formada == palavra:
# 	print("Sua palavra é um palíndromo")
# else:
# 	print("Sua palavra não é um palíndromo")

"""Contagem de letras em uma palavra"""

# from collections import Counter

# texto = input("Selecione seu texto: ").replace(" ", "")

# dicionario = dict(Counter(texto))

# for chave, valor in dicionario.items():
#     print(f'Letra: {chave} - Quantidade: {valor}')

"""Filtro de números pares e ao quadrado"""

# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# lista_pares = []
# lista_ao_quadrado = []

# for numeros in lista:
#     if numeros % 2 == 0:
#         lista_pares.append(numeros)
#     lista_ao_quadrado.append(numeros ** 2)

# print("Lista original:", *lista)
# print("Números pares:", *lista_pares)
# print("Números ao quadrado:", *lista_ao_quadrado)

"""Rascunho de teste sort() e list comprehension"""

dados = [
    {'nome': 'Ana', 'idade': 17, 'status': 'pendente'},
    {'nome': 'Bruno', 'idade': 25, 'status': 'pendente'},
    {'nome': 'Carla', 'idade': 30, 'status': 'pendente'},
]

dados1 = [
    
    {**dado, 'status': 'ativo'} if dado['idade'] >= 18 else {**dado}
    for dado in dados
    
    ]

print(dados1)

dados2 = [
    
    {**dado, 'vip': True} if dado['idade'] >= 25 else {**dado, 'vip': False}
    for dado in dados
    
    ]
    
print(dados2)

#dados3 = [
    
    
#    {**dado, 'nome': 'Bruno Silva'} if dado['nome'] == 'Bruno' else {**dado}
#    for dado in dados
    
#    ]
 
dados3 = []

for dado in dados:
    if dado['nome'] == 'Bruno':
        dado['nome'] = 'Bruno Silva'
        dados3.append(dado)
    else:
        dados3.append(dado)
    
print(dados3)

listas = [1,9,5,6,2]

lista_vazia = []

for lista in listas:
    lista_vazia.append(lista)

print(*lista_vazia)

lista_vazia2 = [x for x in listas]
    
print(*lista_vazia2)    

listas.sort(reverse = True)

print(listas)

dados.append({'nome': 'Julio', 'idade': 20, 'status': 'pendente'})
dados.sort(key=lambda item: item['idade'], reverse = True)

print(*dados)