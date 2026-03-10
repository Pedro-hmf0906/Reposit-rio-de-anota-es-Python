# O fim deve ser TAMANHO + 1 para incluir o número 10
#for i in range(1, 11, 1):
#    print(f'--- Tabuada de {i} ---')
#    for j in range(1, 11, 1):
#        print(f'{i} x {j} = {i * j}')
#    print('\n')

from typing import Counter


string = input("Digite uma palavra: ")
vogais = "aeiouáéíóúâêîôûãõ"

vogais_na_string = ''
consoantes_na_string = ''
contador_vogais = 0
contador_consoantes = 0

#Conta quantidade de letras
print(f'A palavra digitada contém {len(string.replace(" ", ""))} letras !') #Ignora espaços

for letras in string.upper():
    if letras.isalpha():
        if letras in vogais.upper():
            if letras in vogais_na_string:
                continue
            else:
                contador_vogais += 1
                vogais_na_string += letras + " "
        else:
            if letras in consoantes_na_string:
                continue
            else:
                contador_consoantes +=1
                consoantes_na_string += letras + " "
            
print('Vogais:', vogais_na_string)
print('Consoantes:', consoantes_na_string)