# --".strip()"-- é uma ferramenta fundamental para manipulação de strings, usada para remover caracteres indesejados
nome = input("Digite seu nome: ").strip() 
idade = input("Digite sua idade: ")
print() #/r/n

if nome and idade :
    print(f'Seu nome é: "{nome}"')
    print(f'Sua idade é: {idade}')

    print(10 * '-')

    print(f'Seu nome invertido é: "{nome[::-1]}"')

    print(10 * '-')

    if ' ' in nome :
        print("Seu nome contém espaços !")
    else :
        print('Seu nome não contém espaços !')
    
    print(10 * '-')
    
    print(f'Seu nome tem {len(nome.replace(" ", ""))} letras')
    
    print(10 * '-')
    
    print(f'A primeira letra do seu nome é: "{nome[0]}"')
    print(f'A ultima letra do seu nome é: "{nome[-1]}"')
    
    print()
else :
    print('Desculpa, você deixou campos vazios...')
    print()