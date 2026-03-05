"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""
#        +01234
#        -54321
string = 'ABCDE'  # 5 caracteres (len)
# print(bool([]))  # falsy
# print(lista, type(lista))

#        0    1      2              3    4
#       -5   -4     -3             -2   -1
lista = [123, True, 'Luiz Otávio',  1.2, []]
lista[-3] = 'Maria'
print(lista)
print(lista[2], type(lista[2]))

"""
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove o índice final ou o índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista - 'nome da lista'.extend([valores inserido 1, valor inserido 2])
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

#        0   1   2   3
lista = [10, 20, 30, 40]
lista.append('Luiz')
nome = lista.pop()
lista.append(1233)
del lista[-1]
# lista.clear()
lista.insert(100, 5)
print(lista[4])

#Cocatenar
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b)
print(lista_a)

"""
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""

#Duas listas com ips diferentes
lista_a = ['Luiz', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy() #Cria uma nova IP para lista_b apontando apenas para os mesmos endereços que possuem os mesmos valores da lista_a - LISTA INDEPENDENTE

#OBS: Se lista_b = lista_a, ambas apontariam para os mesmo endereços da memória, caso houvesse mundança em algum índice de qualquer lista, as duas continuariam iguais

lista_a[0] = 'Qualquer coisa' #Como mudou o primeiro endereço da lista_a, a lista_b possui um endereço diferenta no índice 0 em relação a lista_a
print(lista_a)
print(lista_b)