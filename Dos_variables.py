# Diseñar un algoritmo tal que dados como datos dos variables de tipo entero, obtenga el resultado de la siguiente función:
num= int(input("Ingrese numero: "))
V= int(input("Ingrese valor: "))
if num == 1:
    resp=100*V 
elif num == 2:
    resp=100**V 
elif num == 3:
    resp=100/V
else:
    resp=0 
print("La respuesta es: ",resp)
    
