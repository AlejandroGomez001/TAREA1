# Leer tres números enteros diferentes entre sí y determinar el número mayor de los tres.
A=int(input("Ingrese un numero\n"))
B=int(input("Ingrese otro numero\n"))
C=int(input("Ingrese un numero\n"))
if(A > B and A > C):
 print("El numero mayor es " + str(A))
else:
 if(B > A and B > C):
  print("El numero mayor es " + str(B))
 else:
  print("El numero mayor es " + str(C))