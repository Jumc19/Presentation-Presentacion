def main():
    cantidad_positivos = 0
    cantidad_negativos = 0
    cantidad_cero = 0

    for i in range(10):
        try:
            num=float(input(f"ingresar el valor {i + 1}: "))
            if num > 0: 
                cantidad_positivos +=1
            elif num < 0:
                cantidad_negativos +=1
            else:
                cantidad_cero +=1
        except ValueError:
            print("Error: Ingrese un valor numerico valido.")   
    
    total_numeros = 10
    porcentaje_ceros = ( cantidad_cero / total_numeros ) * 100

    print(f"cantidad de numeros positivos: {cantidad_positivos}")
    print(f"cantidad de numeros negativos: {cantidad_negativos}")
    print(f"porcentaje de ceros: {porcentaje_ceros:.2f}%")

if __name__ == "__main__":
    main()