while True:
    try:
        numeros = []

        while len(numeros) < 9:
            valor = int(input("Digite um número (0-9): "))

            if 0 <= valor <= 9:
                numeros.append(valor)
            else:
                print("Digite um número entre 0 e 9")

        def calcula_digito(lista, peso_inicial):
            soma = 0

            for i, numero in enumerate(lista):
                soma += numero * (peso_inicial - i)

            resultado = (soma * 10) % 11
            return 0 if resultado > 9 else resultado

        digito1 = calcula_digito(numeros, 10)
        numeros.append(digito1)

        digito2 = calcula_digito(numeros, 11)
        numeros.append(digito2)

        cpf = "{}{}{}.{}{}{}.{}{}{}-{}{}".format(*numeros)

        print("CPF gerado:", cpf)

        break

    except ValueError:
        print("Digite apenas números!")