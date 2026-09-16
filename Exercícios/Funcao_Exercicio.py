# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplicador(*args):
    total = 1
    for i in args:
        total *= i
    return total

numeros = 1, 4, 5, 6
total = multiplicador(*numeros)
print("Total: ", total)

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def par_impar(numero):
    if numero % 2 == 0:
        return "Par"    
    return "Ímpar"
        
entrada = '' 
while not entrada.isdigit():
    entrada = input("Digite um número inteiro: ")
    if not entrada.isdigit():
        print("Número inválido! Digite novamente!")

# while True:
#     entrada = input("Digite um número inteiro: ")
#     try:
#         numero = int(entrada)
#         break
#     except ValueError:
#         print("Número inválido! Digite novamente!")
# print(f"Número validado: {numero}")

numero_validado = int(entrada)

resultado = par_impar(numero_validado)
print(f"O número {numero_validado} é: {resultado}")

# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def dobrar(*args):
    return [item * 2 for item in args]

def triplicar(*args):
    return [item * 3 for item in args]

def quadruplicar(*args):
    return [item * 4 for item in args]

numero = int(input("DIGITE UM NÚMERO INTEIRO: "))

print(f"\nDobro  de {numero} é igual a: {dobrar(numero)}")

print(f"\nTriplo de 2 e 3 é igual a: {triplicar(2, 3)}")

print(f"\nQuadruplo  de {numero} é igual a: {quadruplicar(numero)}")

#OU

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar


duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))

