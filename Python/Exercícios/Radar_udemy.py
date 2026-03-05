velocidade = input("Velocidade do carro: ")
local_carro = input("Localização do carro: ")

RADAR_1 = 60 #Velocidade máxima permitida pelo Radar
LOCAL_1 = 100 #Localização do radar
RADAR_RANGE = 1 #Distância onde o radar consegue pegar

velocidade_multa = velocidade < 60
#Se o carro estiver entre 99 à 101 km, o radar pega
carro_multa = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE) 

if velocidade_multa:
    print("O carro está na velocidade adequada !")
elif carro_multa:
    print("O carro foi multado !!!")
else:
    print("Está tudo certo !")