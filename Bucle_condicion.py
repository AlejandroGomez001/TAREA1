# Diseñe un pseudocódigo para calcular la suma y producto de N números enteros, utilizando un bucle controlado por el usuario.
n=int(input("Ingrese un numero: "));
producto=1
suma=0
respuesta=str("S")
while((respuesta!="N")and (respuesta!="n")):
	suma=suma+n
	producto=producto*n
	print("La suma es: "+str(suma))
	print("El producto es: "+str(producto))
	respuesta=str(input("¿Desea ingresar otro numero Si=ingrese la letra 'S' y si es No=Ingrese la letra'N'?"))


