# Determinar si un número entero proporcionado por el usuario es primo. 

m= int(2);
band = "V";

numero = int(input("Ingrese el numero: "));

while((band == "V") and (m < numero)):
    if((numero % m) == 0):
        band = "F";
    else:
        m = m + 1;
if(band == "V"):
    print("El numero leido es primo");
else:
    print("El numero leido no es primo");