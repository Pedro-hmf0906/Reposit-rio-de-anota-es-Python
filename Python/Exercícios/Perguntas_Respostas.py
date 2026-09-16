# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

qtd_acertos = 0

for pergunta in perguntas:
    print('Pegunta: ', pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']
    for i, value in enumerate(opcoes):
        print(f'{i}) {value}')
    print()

    escolha = input("Digite sua resposta: ")

    quantidade_opcoes = len(opcoes)
    acertou = False
    resposta = None

    
    if escolha.isdigit():
        resposta = int(escolha)
    
    if resposta is not None:
        if resposta >= 0 and resposta < quantidade_opcoes:
            if opcoes[resposta] == pergunta['Resposta']:
                acertou = True

    print()
    if acertou:
        qtd_acertos += 1
        print("Acertou !!!")
    else:
        print("Errou...")

print()

print('Quantidade de acertos:', qtd_acertos)
print(" de ", len(perguntas), " perguntas" )