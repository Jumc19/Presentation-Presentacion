def calcular_promedio(nombre_alumno,calificaciones):
    #   calcular promedio
    promedio=sum(calificaciones)/len(calificaciones)

    #imprimir resultados
    print(f"nombre del alumno: {nombre_alumno} ")
    print(f"promedio de calificaciones {promedio} ")



#  Ejemplo de uso
nombre_alumno=input("ingrese el nombre del/la alumno/a ")

calificaciones=[]
for i in range (5):
    calificacion=float(input(f"ingrese la calificacion { i + 1 }: "))
    calificaciones.append(calificacion)


calcular_promedio(nombre_alumno,calificaciones)