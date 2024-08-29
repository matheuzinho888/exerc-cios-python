qt_par = 0
qt_imp = 0 
for b in range (10):
  num = int(input (f"digite o {b+1}° numero "))
  if (num%2==0):
   qt_par += 1
  else :
   qt_imp += 1 
    
print (f"a quatidade de par {qt_par} e de impares {qt_imp}")