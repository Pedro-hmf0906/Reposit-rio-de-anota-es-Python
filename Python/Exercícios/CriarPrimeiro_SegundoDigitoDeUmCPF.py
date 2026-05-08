import random


while True:
    try:
        numeros = []

        for _ in range(9):
            numeros.append(random.randint(0,9))

        # Função
        def calcula_digito(lista, peso_inicial):
            soma = 0

            for i, numero in enumerate(lista):
                soma += numero * (peso_inicial - i)
            print("Soma:",soma)

            resultado = (soma * 10) % 11
            print('Resultado divisão:',resultado)
            
            return 0 if resultado > 9 else resultado

        digito1 = calcula_digito(numeros, 10)
        numeros.append(digito1)

        digito2 = calcula_digito(numeros, 11)
        numeros.append(digito2)

        cpf = "{}{}{}.{}{}{}.{}{}{}-{}{}".format(*numeros) #Legal !

        print("CPF gerado:", cpf)

        break

    except ValueError:
        print("Digite apenas números!")