#Basicamente é pra fazer que a variável nome seja impressa entre asteriscos indice por indice em um while 

nome = input("Digite seu nome: ")

i = 0 #índice
novo_nome = '' #Iniciar uma variável vazia fora do loop, assim toda vez que o loop reiniciar, ela não zera
while i < len(nome):
    letra = nome[i]
    novo_nome += f'*{letra}'
    i += 1

novo_nome += '*' #Só pra encerrar com um asterisco no final do nome
print(novo_nome)