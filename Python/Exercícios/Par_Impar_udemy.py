#Execício básico para manter a prática

#Enunciado

"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

print('Verificação de par ou ímpar (Digite somente números inteiros)')

print('-' * 20)

try:
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        print("O número digitado é par !")
    else:
        print("O número digitado é impar")
except ValueError:
    print("Erro: o valor digitado não foi um número")