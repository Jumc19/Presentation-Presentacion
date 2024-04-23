def calcular_cambio(costo, dinero_entregado):
    if dinero_entregado< costo:
        return "el dinero entregado es insuficiente, Transacciòn cancelada."
    else:
        cambio=dinero_entregado-costo
        return f"cambio a entregar: {cambio}"    
    
if __name__=="__main__":
    try:
        costo=float(input("Ingrese el costo del articulo vendido: "))
        dinero_entregado=float(input("ingrese la cantidad de dinero entregado por el cliente "))
        resultado=calcular_cambio(costo,dinero_entregado)
        print(resultado)
    except ValueError:
        print("Error: Ingrese valores numericos validos.")