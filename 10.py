def main():
    cantidad_impares = 0
    for i in range(20):
        try:
            numero=int(input(f"ingrese el numero {i + 1}: "))
            if numero % 2 !=0:
                cantidad_impares += 1
        except ValueError:
            print("Error: ingrese un valor numerico valido.")


    total_numeros = 20
    porcentaje_impares = (cantidad_impares / total_numeros) * 100

    print(f"porcentaje de numeros impares: {porcentaje_impares:.2f}%")

if __name__ == "__main__":
    main()