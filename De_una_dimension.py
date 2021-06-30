# Aplicar las fases  para  la resolución de un problema para leer un vector de 20 números enteros y a continuación escribir en un vector A todos los números negativos y en un vector B todos los positivos o iguales a cero. Imprimir dichos vectores.
# Escoja solo 20 numeros
i=1
Arreglo=[]
nelementos=20
while i<=nelementos:
	elemento=int(input("Ingrese un numero: "))
	Arreglo.append(elemento)
	i=i+1
	
print("El arreglo es: "+str(Arreglo))
positivo=[]
for elemento in (Arreglo):
	if elemento>=0:
		positivo.append(elemento)
print ("Los numeros positivos de este arreglo son : "+str(positivo))

negativo=[]
for elemento in (Arreglo):
	if elemento<0:
		negativo.append(elemento)
print ("Los numeros megativos de este arreglos son: "+str(negativo))