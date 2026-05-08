#Essa parte é só uma contextualizada rápida sobre Try e Except

numero_str = input("Vou dobrar o número que você digitar: ")

"""
OBSERVAÇÃO: Se não converter o valor para números, a parte da multiplicação acaba cocatenando a quantidade de vezes *multiplicada*
Ex.:
    numero_str = input("Vou dobrar o número que você digitar: ") => Entrada: 2
    print(f'Dobro: {numero_str * 2}') => Saída: 22
"""

# Utilizando '.isdigit()'
"""
if numero_str.isdigit():
    numero_float = float(numero_str)
    print(f"O dobro de {numero_float} é {numero_float * 2}")
else: 
    print("Isso não é um número")
"""
# isdigit() é uma ferramenta para analisar se há números inteiros em uma string, retornando um resultado boolean
# True - Números Inteiros /// False - Sem/Com espaços, Números negativos, float, caracteres especiais e letras

#-------------------------------

# Utilizando Try e Except

try:
    print("STR: ",numero_str)
    numero_float = float(numero_str)
    print("FLOAT: ",numero_float)
    print(f"O dobro de {numero_float} é {numero_float * 2}")
except:
    print("Isso não é um número")
    