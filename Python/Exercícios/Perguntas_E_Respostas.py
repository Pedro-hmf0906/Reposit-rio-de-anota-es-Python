perguntas = [
    {
        'Pergunta': 'Quanto é 2+2 ?',
        'Opções': ['1','2','3','4'],
        'Resposta': '4'
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
acertos = 0

for pergunta in perguntas:
    print(pergunta['Pergunta'])

    for i, opcao in enumerate(pergunta['Opções']):

        print(f'{i} - {opcao}')

    resposta_usuario = input('Digite a opção da resposta correta: ')

    acerto = False
    resposta_correta = pergunta['Resposta']
    qtd_opcoes = len(pergunta['Opções'])

    if resposta_usuario.isdigit():
        resposta_usuario = int(resposta_usuario)

        if resposta_usuario >= 0 and resposta_usuario < qtd_opcoes:
            if pergunta['Opções'][resposta_usuario] == resposta_correta:
                acerto = True


    if acerto:
        acertos += 1
        print('Parabéns, você acertou !')
    else:
        print('Você errou !')

print(f'Você acertou {acertos} de {len(perguntas)} perguntas.')