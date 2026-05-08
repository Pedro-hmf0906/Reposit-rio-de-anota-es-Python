#Args

def multiplicador(multiplicador):
    def multiplicar(*args):
        resultado = []

        for item in args:
            resultado.append(item*4)
        
        return resultado
    return multiplicar

lista = [1, 2, 3]
DOBRAR = multiplicador(2)
triplicar = multiplicador(3)(3, 4)
quadruplicar = multiplicador(4)(*lista)

print(f"Variável DOBRAR: {DOBRAR}") # Isso vai imprimir o ENDEREÇO da função
print(f"Chamando DOBRAR: {DOBRAR(5, 10)}") # Isso vai imprimir [10, 20]
print(f"Resultado triplicar: {triplicar}")
print(f"Resultado quadruplicar: {quadruplicar}")

#Kwargs

def infos(nome, idade, altura):
    print(f'Nome: {nome} Idade: {idade} Altura: {altura}')

def info(**pessoa):
    for chave in pessoa:
        print(f'Chave {chave}: {pessoa[chave]}')


pessoa = {
    'nome': 'Pedro',
    'idade': 18,
    'altura': 1.87
}

print(pessoa)

for chave in pessoa:
    print(f'Chave {chave}: {pessoa[chave]}')

infos(**pessoa)
info(**pessoa)