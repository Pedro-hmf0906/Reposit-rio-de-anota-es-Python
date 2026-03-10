"""
split e join com list e str
split - divide uma string (list)
join - une uma string
"""
frase = '   Olha só que   , coisa interessante          '
lista_frases_cruas = frase.split(',')

lista_frases = []

for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip()) #O .strip() elimina o espaçamento que fica antes e depois da string 

print(lista_frases_cruas)
# Saída:  ['   Olha só que   ', ' coisa interessante          ']

print(lista_frases)
# Saída: ['Olha só que', 'coisa interessante']

frases_unidas = ',--- '.join(lista_frases) # A string antes de '.join()' é o caractere que vai conectar com os valores da lista

print(frases_unidas)