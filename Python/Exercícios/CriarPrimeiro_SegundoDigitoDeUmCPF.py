while True:
    
    try:
        lista_primeiros_num = []
        cpf = ''
        contador = 0
        resultado_soma_mult_cpf = 0

        while contador < 9:
            valor = int(input("Digite um número: "))
            
            if 0 <= valor <= 9:
                lista_primeiros_num.append(valor)
                contador += 1
                
                if contador == 3 or contador == 6:
                    cpf += str(valor) + "." 
                    
                else: 
                    cpf += str(valor)
                    
            else:
                print("Por favor, insira um valor de 0 à 9, tente novamente !")
        
        print(cpf)

        for i, numeros in enumerate(lista_primeiros_num):
            peso = 10 - i
            resultado_soma_mult_cpf += (peso * numeros)

        print('Resultado da soma:',resultado_soma_mult_cpf)

        resultado_soma_mult_cpf *= 10

        print("Soma multiplicada por 10:", resultado_soma_mult_cpf)

        resto_divisao = resultado_soma_mult_cpf % 11

        print("Resto da divisão por 11:", resto_divisao)

        if resto_divisao > 9:
            lista_primeiros_num.append(0)
            cpf += "-0"
        else:
            lista_primeiros_num.append(resto_divisao)
            cpf += "-" + str(resto_divisao)

        print(lista_primeiros_num)
        print(cpf)

        resultado_soma_mult_cpf = 0

        for i, numeros in enumerate(lista_primeiros_num):
            peso = 11 - i
            resultado_soma_mult_cpf += (peso * numeros)

        print('Resultado da soma:',resultado_soma_mult_cpf)

        resultado_soma_mult_cpf *= 10

        print("Soma multiplicada por 10:", resultado_soma_mult_cpf)

        resto_divisao = resultado_soma_mult_cpf % 11

        print("Resto da divisão por 11:", resto_divisao)

        if resto_divisao > 9:
            lista_primeiros_num.append(0)
            cpf += "0"
        else:
            lista_primeiros_num.append(resto_divisao)
            cpf += str(resto_divisao)

        print(lista_primeiros_num)
        print(cpf)

        break
    
    except ValueError:
        print("Por favor, digite somente números !")
        continue