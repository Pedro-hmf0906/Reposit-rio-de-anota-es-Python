"""
Faça uma lista de compras
O usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com erros de índices inexistentes na lista
"""

import os

carrinho_de_compras = [] #Inicialmente vazia

#AVISO !!!!!
#Sim, eu sei que eu poderia utilizar switch, mas ainda não fui atrás de como é a sintaxe dele, fora que eu tô treinando if/elif/else

while True:
    lowercase = input("Selecione uma opção: \n [i]nserir [a]pagar [l]istar [s]air: ")
    opcao = lowercase.lower()

    print()
    
    if opcao == 'i':
        
        while True:
            item = input("Por favor, selecione um item para suas compras !\nItem: ")
        
            if item == '':
                print("\nNada foi digitado. Digite novamente !\n")
                continue
        
            carrinho_de_compras.append(item)
            print()
            print(f'O item {item} foi adicionado ao carrinho\n')
            break
        
        continue
    
    elif opcao == 'a':

        if not carrinho_de_compras: # Verifica se a lista está vazia
            print("O seu carrinho está vázio, insira algo, por gentileza !")
            continue
        else:    
        
            print("Selecione um índice para remover:\n")
        
            while True:
                try:   
                    for i, nome in enumerate(carrinho_de_compras):
                        print(i, nome)
                    print()
                    indice = int(input('Índice: '))
                    del carrinho_de_compras[indice]
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break    
                except ValueError:
                    print("\nInsira um número inteiro !\n")
                
                except IndexError:
                    print("\nÍndice inexistente na lista\n")
                
                except Exception:
                    print('\nErro desconhecido\n')
                
        continue
    
    elif opcao == 'l':
        
        os.system('cls' if os.name == 'nt' else 'clear')

        if not carrinho_de_compras:
            print("Nada foi inserido ainda, insira alguma coisa !\n")
            continue
        
        for indice, nome in enumerate(carrinho_de_compras):
            print(indice, nome)
        print()
    
    elif opcao == 's':
        print("Saindo...")
        break

    else:
        
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Opção inexistente. Por favor, selecione uma das opção sugeridas: i, a, l ou s\n")
        print()
        continue
