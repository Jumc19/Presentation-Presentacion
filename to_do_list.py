def mostrar_tareas(tareas):
    if not tareas:
        print("No hay tareas pendientes.")
    else:
        print("Tareas pendientes:")
        for i, tarea in enumerate(tareas, 1):
            print(f"{i}. {tarea}")

def agregar_tarea(tareas, tarea):
    tareas.append(tarea)
    print("Tarea agregada con éxito.")

def eliminar_tarea(tareas, numero_tarea):
    if numero_tarea < 1 or numero_tarea > len(tareas):
        print("Número de tarea inválido.")
    else:
        tarea_eliminada = tareas.pop(numero_tarea - 1)
        print(f"Tarea '{tarea_eliminada}' eliminada con éxito.")

def main():
    tareas = []
    while True:
        print("\n== Aplicación de Lista de Tareas ==")
        print("1. Mostrar tareas")
        print("2. Agregar tarea")
        print("3. Eliminar tarea")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_tareas(tareas)
        elif opcion == "2":
            tarea = input("Ingrese la nueva tarea: ")
            agregar_tarea(tareas, tarea)
        elif opcion == "3":
            mostrar_tareas(tareas)
            numero_tarea = int(input("Ingrese el número de la tarea a eliminar: "))
            eliminar_tarea(tareas, numero_tarea)
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
