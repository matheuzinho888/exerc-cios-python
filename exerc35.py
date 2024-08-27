import math
met = float(input("quantos metros quadrados quadrados voce quer pintar: "))
lata = 18
preco = 80
latapre = math.ceil(float(met/lata))
quati = latapre*preco 
print (f"voce vai precisar de {latapre} latas")
print (f"o preco ao total vai ser de {quati} reais")