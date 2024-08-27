altura = float(input("qual a sua altura: "))
sexo = input("qual é o seu sexo: ")[0]
masc = (72.7*altura) - 58
fem = (62.1*altura) - 44.7
if (sexo== 'm' or sexo== 'M'):
   print (f"seu peso ideal é {masc}")
elif (sexo== 'f' or sexo== 'F'):
  print (f"seu peso ideal é {fem}")
else :
  print("seu genero é invalido")