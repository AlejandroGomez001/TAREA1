# Una escuela aplica dos exámenes a sus aspirantes, por lo que cada uno de ellos obtiene dos calificaciones denotadas como C1 y C2. El aspirante que obtenga calificaciones mayores que 80 en ambos exámenes es aceptado; en caso contrario es rechazado.
C1=int(input("Ingrese califiacion numero uno: "))
C2=int(input("Ingrese califiacion numero dos: "))
if((C1 >= 80) and (C2 >= 80)):
     print("aceptado")
else:
     print("rechazo")