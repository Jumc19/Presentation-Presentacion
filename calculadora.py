print("Bienvenidos a la calcualdora")
print("Para salir escribe Salir")
print("Las operaciones que se pueden realizar son suma, resta, multiplicacion y division")

resultado=""

while True:

    if not resultado:
        resultado=input("ingrese número: ")
        if resultado.lower()=="salir":
            break
        resultado=int(resultado)
    op=input("ingresa operacíon: ")
    if op.lower()=="salir":
        break 
    n2=input("ingresa el siguiente numero: ")
    if n2.lower()=="salir":
        break
    n2=int(n2)

    if op.lower()=="suma":
        resultado += n2
    elif op.lower()=="resta":
        resultado -= n2
    elif op.lower()=="multi":
        resultado *= n2
    elif op.lower()=="div":
        resultado /= n2

    else:
        print("operacion no valida")
        break
    print (f"El resultado es: {resultado}")