# Leer tres números enteros diferentes entre sí y determinar el número mayor de los tres.
n1 = float(input("Ingrese el primer numero: "))
n2 = float(input("Ingrese el segundo numero: "))
n3 = float(input("Ingrese el tercer numero: "))

if n2 < n1 >n3:
    print("El numero mayor es el primer numero. Numero: ",n1)
if n1 < n2 >n3:
    print("El numero mayor es el segundo numero. Numero: ",n2)
if n1 < n3 >n2:
    print("El numero mayor es el tercer numero. Numero: ",n3)
else:
    print("Todos los numeros son iguales.")