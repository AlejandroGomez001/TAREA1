# Diseñe un pseudocodigo para calcular la suma y productos de N numeros enteros, ultilizando un bucle controlado por centinela
n=int(input("Ingrese un numero: "));
while(n>=0):
	suma=0
	producto=1
	suma=suma+n
	producto=producto*n
	print("La suma es: "+str(suma))
	print("El producto es: "+str(producto))
	n=int(input("Ingrese otro numero: "))
input("Ingreso un numero negativo acabo la ejecucion del algoritmo")