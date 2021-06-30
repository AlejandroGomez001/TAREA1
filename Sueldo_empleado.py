# Dado el sueldo de un empleado, encontrar el nuevo sueldo si obtiene un aumento del 10% si su sueldo es inferior a $600, en caso contrario no tendrá aumento.
s= float(input("Ingese sueldo: "))
if s < 600:
    ns= s + s*0.1
elif s:
    ns= s 
print("El sueldo del empleado es: ",ns)