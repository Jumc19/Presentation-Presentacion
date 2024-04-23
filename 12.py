def main():
    cantidad_alumnos=10
    notas_alumnos=[]

    for i in range(cantidad_alumnos):
        try:
            nota=int(input(f"ingrese la nota del alumno {i + 1} (1-10): "))
            if nota < 1 or nota >10:
                print("Error: Ingrese un nota valida entre 1 y 10.")
                return
            
            notas_alumnos.append(nota)
        except ValueError:
            print("Error: Ingrese un valor numerico valido.")
            return
        
    cantidad_aprobados = sum(1 for nota in notas_alumnos if nota >= 4)
    cantidad_desaprobados = sum(1 for nota in notas_alumnos if nota < 4)
    cantidad_superior_8 = sum(1 for nota in notas_alumnos if nota > 8)
    porcetaje_aprobados = (cantidad_aprobados/cantidad_alumnos) * 100

    print(f"cantidad de alumnos aprobados: {cantidad_aprobados}")
    print(f"cantidad de alumnos desaprobados: {cantidad_desaprobados}")
    print(f"cantidad de alumnos con nota superior a 8: {cantidad_superior_8}")
    print(f"porcentaje de alumnos aprobados: {porcetaje_aprobados:.2f}%")

if __name__ == "__main__":
    main() 