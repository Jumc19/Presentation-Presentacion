def sumar(a,b):
    return a+b


def restar(a,b):
    return a-b


def multiplicacion(a,b):
    return a*b


def dividir(a,b):
    return a/b
    if b==0:
        raise ValueError("no es posible dividir entre cero")
    return a/b


if __name__=="__main__":
    try:
        num1=float(input("ingrese el primer numero "))
        num2=float(input("ingrese el segundo numero "))
        suma=sumar(num1,num2 )
        resta=restar(num1,num2 )
        producto=multiplicacion(num1,num2 )
        division=dividir(num1,num2 )
        print(f"suma: {suma}")
        print(f"resta: {resta}")
        print(f"multiplicacion: {producto}")
        print(f"division: {division}")

    except ValueError as e:
        print("Error: ingrese valores numericos validos")
    except Exception as e:
        print(f"error{e}")