deposito = int(input("qual o valor do deposito: "))
juros = int(input("qual a taxa de juros a ser paga: "))
pag = deposito+(deposito*juros/100)
vltd = pag+deposito
print (f"seu rendimento com o juros foi de {pag}")
print (f"seu rendimento total foi de {vltd}")