"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

import os


string = 'Termo'
palavra_secreta = string.lower()
texto = ''
contador = 0

while True:
    try:
        #Pega apenas o primeiro caractere digitado pelo usuário
        palavra_adivinhada = input("Digite a letra desejada: ")[0] 
        contador += 1

        #Caso o usuário digite caracteres maiúsculo
        lowercase = palavra_adivinhada.lower()
        print('-' * 10)

        #Verifica se o caractere digitado pelo usuário está na palavra secreta
        if lowercase in palavra_secreta:
            print("A palavra está na palavra secreta !")
            texto += lowercase
        else:
            print("A palavra não está na palavra secreta !")
            print('-' * 10)
            continue
        
        palavra_formada = ''

        #Posiciona exatamente na posição em que se encontra o caractere digitado pelo usuário
        for letra_secreta in palavra_secreta:
            if letra_secreta in texto:
                palavra_formada += letra_secreta
            else:
                palavra_formada += '*' 

        print('-' * 10)

        print(palavra_formada)

        if palavra_formada == palavra_secreta:
          os.system('cls' if os.name == 'nt' else 'clear') #Limpa o terminal, 'nt' para windows e 'posix' para UNIX
          #Só para Windows: os.system('cls')
          #Unix: os.system('clear')

          print("Parabéns, você adivinhou a palavra secreta !!!")
          break
        
    except IndexError:
        print("Por favor, insira algum caractere !")
        continue

print(f"A palavra secreta era: {palavra_secreta}")
print(f'Quantidade de tentativas: {contador}')
