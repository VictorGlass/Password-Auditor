

'''


## Password Auditor - Version simple y educativa.

## Autor: Victor Ignacio Carrera Gutierrez.

## Uso: Local y ético (no envia datos, no accede a redes).

## Descripción:

Este script analizara las contraseñas ingresadas por el usuario
y evaluará su seguridad en funcion de distintos criterios comunes de
Ciberseguridad.

'''


import math
import sys
import re


## Esta es la lista de contraseñas mas comunes para detectar rapidamente.

common_passwords = [
    "123456", "password", "admin", "qwerty", "abc123", 
    "letmein", "welcome", "iloveyou"
]


def calculate_entropy(password: str) -> float:

    ## Calcula la entropia de una contraseña segun su longitud
    ## y el tamaño del conjunto de caracteres usado.

    if not password:
        return 0.0

    charset_size = 0
    if re.search(r"[a-z]", password): charset_size += 26
    if re.search(r"[A-Z]", password): charset_size += 26
    if re.search(r"[0-9]", password): charset_size += 10
    if re.search(r"[^a-zA-Z0-9]", password): charset_size += 32


    if charset_size == 0:
        return 0.0
    

    entropy = len(password) * math.log2(charset_size)
    return round(entropy, 2)


def check_strength(password: str ):

    ## Evaluará la contraseña y devolverá (nivel, mensaje).

    if not password:
        return ("Es debil, La contraseña esta vacia.")

    ## Revision rapida: contraseñas comunes.

    if password.lower() in common_passwords:
        return ("Es debil, muy comun, evita usarla. ")
    
    entropy = calculate_entropy(password)


    ## Clasificacion segun entropia aproximada.

    if entropy < 40:
        nivel = "Debil"
        mensaje = "Demasiado corta y predecible"
    elif entropy < 60:
        nivel = "Media"
        mensaje = "Mejorar: usa mas carcteres y simbolos"
    else:
        nivel = "Fuerte"
        mensaje = "Excelente nivel de seguridad"

    return (nivel, mensaje)
    

def analyze_password(password: str):

    ## Analiza y muestra el resultado.

    try:
        resultado = check_strength(password)

        ## Comprobar que la funcion devolvio una tupla de 2 elementos.
        if isinstance(resultado, tuple) and len(resultado) == 2:
            nivel, mensaje = resultado
            print(f"\nContraseña: {password}")
            print(f"Fortaleza: {nivel}")
            print(f"Sugerencia: {mensaje}")
        else:
            print(f"Resultado inesperado: {resultado}")
    except Exception as e:
        print(f"Error al intentar analizar la contraseña: {e}")


def main():

    ## Apartado principal del programa.

    print("Password Auditor -  Análisis Local y Ético")

    if len(sys.argv) > 1:

        ## Leer desde un archivo si se pasa como argumento.

        archivo = sys.argv[1]
        try:
            with open(archivo, "r", encoding = "utf-8") as f:
                contraseñas = [line.strip() for line in f if line.strip()]
            for pw in contraseñas:
                analyze_password(pw)
        except FileNotFoundError:
            print("Archivo no encontrado.")
    
    else:

        ## Modo interactivo

        while True:
            pwd = input("\nIntroduce una posible contraseña (o 'salir' para terminar): ")
            if pwd.lower() == "salir":
                print("\nGracias por usar Password Auditor.")
                break
            analyze_password(pwd)

if __name__ == "__main__":
    main()

