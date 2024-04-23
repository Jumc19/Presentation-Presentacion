# solicitar al usuario ingresar los datos numericos
numero1=float(input("ingrese el primer numero "))
numero2=float(input("ingrese el segundo numero "))

# comparar los numeros para determinar el mayor
if numero1>numero2:
    mayor=numero1
    igual=False
elif numero2>numero1:
    mayor=numero2
    igual=False
else:
    mayor=numero1
    igual=True


# mostrar resultado
if igual:
    print("los nuemro ingresados son iguales. ")
else:
    print("el numero mayor es :",mayor)