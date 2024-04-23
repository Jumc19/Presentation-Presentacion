def main():
    cantidad_positivos = 0

    for i in range(10):
        try:
            dato = float(input(f"Ingrese el dato {i + 1}: "))
            if dato > 0:
                cantidad_positivos += 1
        except ValueError:
            print("Error: Ingrese un valor numérico válido.")

    print(f"La cantidad de datos positivos es: {cantidad_positivos}")

if __name__ == "__main__":
    main()