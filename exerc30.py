n1=float(input("digite o 1° numero "))
n2=float(input("digite o 2° numero "))
sinal=(input("digite o sinal de calculo desejado "))

if (sinal=='+'):
  resultado=n1+n2
  print(f"o resultado foi de {resultado}")

elif (sinal=='-'):
  resultado=n1-n2
  print(f"o resultado foi de {resultado}")

elif(sinal=='*'):
  resultado=n1*n2
  print (f"o resultado foi {resultado}")

elif (sinal=='/'):
  resultado=n1/n2
  print (f"o resultado foi {resultado}")

else:
  print ("seu operador é invalido digite - ou +")