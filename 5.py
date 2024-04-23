# solicitar al usuario los tres numeros
A=float(input("Ingrese el valor de A: "))
B=float(input("Ingrese el valor de B: "))
C=float(input("Ingrese el valor de C: "))

# realizar los calculos segun las condiciones
if A==B:
    resultado=A*B+C
elif A>B:
    resultado=A/B
else:
    resultado=(A+C)/B

# mostrar el resultado
print("el resutlado es: ",resultado)