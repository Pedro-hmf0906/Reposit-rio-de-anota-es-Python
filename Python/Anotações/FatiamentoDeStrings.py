"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [início:final:passo] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""
#Inicio - Começo da contagem
#Final - Onde para a contagem
#Passo - Quantidade de caracteres que vão ser contados até o próximo

#Exemplo passo: v = Olá mundo
#                   123456789
#print(v[::2]) -> Saída: Oámno
#print(v[::3]) -> Saída: O n

variavel = 'Olá mundo'

print(variavel[3:7]) #Conta a partir do caractere da posicao 3 e encerra na caractere 7
print(variavel[::-1]) #Inverte a string