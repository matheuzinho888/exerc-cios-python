salario = int(input("qual é o seu salario atual: "))
gra = salario+ (salario*5/100)
nsala = gra- (gra*7/100)
print (f"seu salario ganhou 5% de gratificação e perdeu 7% em imposto e ficou {nsala} ao total")