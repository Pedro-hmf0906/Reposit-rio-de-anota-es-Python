#Código com problema !!!! Resolver

'''
Problemas:

1-Analisa um único caractere varias vezes caso houver repetição de caractere - PROBLEMA DE OTIMIZAÇÃO
2-Armazena apenas um caractere para empate, não para caso de haver 3 ou mais iguais
3-A impressão final de repetição não está correta !
'''

#Depois eu corrigo ! Ainda há coisas para aprender em python que otimizaria muito o funcionamento desse programa
#21/02/2026

string = input('Digite qualquer coisa !')

i = 0
contador = 0
mais_apareceu = ""
letra_repetida = "" #Problema

#Analisa indice por indice
while i < len(string):
    letra = string[i]

    #Verifica existencia do espaçamento e nao conta no contador
    if letra == " ":
        i += 1 
        continue

    #Conta a quantidade de caracteres da letra atual
    quant_letra_atual = string.count(letra) #Vai contar a quantidade de letras no indicie I

    #Recebe o valor do caractere que mais aparece

    #Problema
    if contador == quant_letra_atual: #Caso teste de repetição de DUAS letras, mas e se houver mais letras com a mesma quantidade ?
      letra_repetida = letra
    elif contador < quant_letra_atual:
      contador = quant_letra_atual
      mais_apareceu = letra

    i += 1
    
if mais_apareceu == letra_repetida: #Problema
    print(f'A letra {mais_apareceu} possui a mesma quantidade de caracteres que a letra {letra_repetida} \
         \n Quantidade: {contador}')
else:
    print(f'O que mais apareceu foi: {mais_apareceu}')
    print(f'Sua quantidade foi: {contador}')

