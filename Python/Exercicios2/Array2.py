array = [0] * 5

for i in range(len(array)):
    valores = int(input("{} - Digite os valores de cada posição: ".format(i+1)))

    array[i] = valores

maior = 0

for numeros in array:
    if maior < numeros:
        maior = numeros 

print(maior)