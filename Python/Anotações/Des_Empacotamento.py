"""
Empacotamento e Desempacotamento
"""
_, _, nome, *resto = ['Maria', 'Helena', 'Luiz']
#print(nome)

#O "_" normalmente refência uma variável que não será usada

# Desempacotamento em chamadas
# de métodos e funções
string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'
salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', ],  # 2
]

# p, b, *_, ap, u = lista
# print(p, u, ap)

# print('Maria', 'Helena', 1, 2, 3, 'Eduarda')
# print(*lista) - Saída: Maria Helena 1 2 3 Eduarda
# print(*string) - Saída: A B C D
# print(*tupla) - Saída: Python é legal

print(*salas, end='\n\nLeruleruleruleru\n', sep='\n\nPulou linha\n\n')

# O *salas/*string/*lista/*tupla desempacota todos os elementos dentro de cada apelido