def main():
    cantidad_positivos = 0
    cantidad_negativos = 0
    cantidad_cero = 0

    for i in range(15):
        try:
            valor = float(input(f"Ingrese el valor {i + 1}: "))
            if valor > 0:
                cantidad_positivos += 1
            elif valor < 0:
                cantidad_negativos += 1
            else:
                cantidad_cero += 1
        except ValueError:
            print("Error: Ingrese un valor numérico válido.")

    print(f"Cantidad de valores positivos: {cantidad_positivos}")
    print(f"Cantidad de valores negativos: {cantidad_negativos}")
    print(f"Cantidad de valores iguales a cero: {cantidad_cero}")

if __name__ == "__main__":
    main()