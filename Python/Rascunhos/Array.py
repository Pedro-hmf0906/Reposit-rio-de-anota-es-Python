#RASCUNHOS

array = [0] * 10
soma = 0

for i in range(len(array)):
    valores = int(input('Informe o valor desejado na posição: {} '.format(i) ))

    array[i] = valores

for numeros in array:
    soma += numeros

print('A soma de todos os valores é: ', soma)