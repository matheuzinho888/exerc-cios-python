seq = int(input("qual a sequencia de numeros fibonnaci desejado: "))
n1=1
n2=1
n3=0
i=3
while i<=seq:
  n3=n1+n2
  n1=n2
  n2=n3
  i=i+1

print(n3)