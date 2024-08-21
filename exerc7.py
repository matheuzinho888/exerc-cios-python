n1= int(input("digite qual sua nota no 1° bimestre: "))
n2= int(input("digite qual sua nota no 2° bimestre: "))
n3= int(input("digite qual sua nota no 3° bimestre: "))
n4= int(input("digite qual sua nota no 4° bimestre: "))
media = (n1+n2+n3+n4)/4
materia = input("qual a sua materia?")

if (media>=7):
  print (f"você passou de ano em {materia} com a nota {media}")

elif (media>=5):
  print (f"voce ficou de recuperação em {materia} com a nota {media}")
else:
  print (f"voce reprovou em {materia} com a nota {media}")