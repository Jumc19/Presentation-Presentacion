def main():
    cantidad_pares = 0
    cantidad_impares = 0

    for i in range(10):
        try:
            numero = int(input(f"Ingrese el número {i + 1}: "))
            if numero % 2 == 0:
                cantidad_pares += 1
            else:
                cantidad_impares += 1
        except ValueError:
            print("Error: Ingrese un valor numérico válido.")

    print(f"Cantidad de números pares: {cantidad_pares}")
    print(f"Cantidad de números impares: {cantidad_impares}")

if __name__ == "__main__":
    main()