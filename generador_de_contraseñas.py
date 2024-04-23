import random
import string

def generar_contrasena(longitud, caracteres):
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

def main():
    longitud = int(input("Longitud de la contraseña: "))
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    print("Caracteres permitidos: ")
    print("1. Letras mayúsculas (A-Z)")
    print("2. Letras minúsculas (a-z)")
    print("3. Dígitos (0-9)")
    print("4. Símbolos de puntuación")
    
    opcion = input("Elija los tipos de caracteres permitidos (separados por comas): ")
    opcion = opcion.split(",")
    
    caracteres_permitidos = ""
    for op in opcion:
        if op == "1":
            caracteres_permitidos += string.ascii_uppercase
        elif op == "2":
            caracteres_permitidos += string.ascii_lowercase
        elif op == "3":
            caracteres_permitidos += string.digits
        elif op == "4":
            caracteres_permitidos += string.punctuation
    
    contrasena_generada = generar_contrasena(longitud, caracteres_permitidos)
    print("Contraseña generada: ", contrasena_generada)

if __name__ == "__main__":
    main()
    