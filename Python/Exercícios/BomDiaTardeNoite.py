#Execício básico para manter a prática

#Enunciado
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

print('-' * 10 ,"Verificação de Horário", '-' * 10)

try:
    horario = float(input("Digite seu horário atual: "))

    if horario >= 0 and horario <= 11:
        print("Bom Dia !!!")
    elif horario >= 12 and horario <= 17:
        print("Boa Tarde !!!")
    elif horario >= 18 and horario <= 23:
        print("Boa Noite !!!")
    else:
        print("O horário digitado não condiz com as 24 horas de um dia !")
except ValueError:
    print("Erro: o valor digitado não condiz com o que foi solicitado !")