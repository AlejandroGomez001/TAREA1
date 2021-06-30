# Calcular la suma de los cuadrados de los primeros 100 enteros y escribir el resultado.

i=int(1);
suma=int(1);
for x in range (2, 100) :
    i=i+2
    suma = suma + i;
    print("El cuadrado de "+str(x)+"es:"+str(suma))
