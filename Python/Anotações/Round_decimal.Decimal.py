import decimal


numero_1 = 0.1
numero_2 = 0.7
numero_3 = numero_1 + numero_2

print(numero_3)
print(f'{numero_3:.2f}') # Retorna uma STRING
print(f'{round(numero_3, 2)} - ARREDONDADO') # Arredonda um número flutuante -> round(*nome da variavel*, *quantidade de casa após a vírgula*)

# Os números dentro do Decimal devem estar em STRING para funcionarem corretamente
numero_1 = decimal.Decimal('0.1')
numero_2 = decimal.Decimal('0.7')
numero_3 = numero_1 + numero_2

print(numero_3, '- DECIMAL COM STRING')

numero_1 = decimal.Decimal(0.1)
numero_2 = decimal.Decimal(0.7)
numero_3 = numero_1 + numero_2

print(numero_3, '- DECIMAL SEM STRING') # Número problemático