# lista para almacenar los productos
productos_por_5 = []


# solicitar al usuario ingresar los 10 numeros uno por uno
for i in range(10):
    numero=float(input(f"ingrese el numero {i+1}: "))
    producto_por_5=numero*5
    productos_por_5.append(producto_por_5)

# mostrar los productos por 5 dee cada numero ingresado
print("productos por 5 de los numero ingresados:" )
for i, producto in enumerate(productos_por_5):
    print(f"numero { i + 1 }: { producto }")