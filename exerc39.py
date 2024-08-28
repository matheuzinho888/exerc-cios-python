import math
n1 = int(input("digite um numero inteiro menor que mil: "))
uni = n1/1
dez = n1/10
cen = n1/100
uni1 = math.ceil(int(uni))
dez1 = math.ceil(int(dez))
cen = math.ceil(int(cen))
print (f"seu numero tem {uni} unidades, {dez} dezenas e {cen} centenas")