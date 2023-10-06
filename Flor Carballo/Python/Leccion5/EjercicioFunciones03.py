# Ejercicio 3: Funcion Recursiva. Imprimi números de 5 a 1 de manera descendente usando funciones recursivas. Puede ser cualquier valor positivo.
def imprimir_numeros_recursivos(numero):
    if numero >= 1: # Caso Base
        print(numero)
        imprimir_numeros_recursivos(numero-1) # Caso recursivo
    elif numero == 0:
        return
    elif numero <= 0:
        print("Valor ingresado incorrecto...")

# Tarea: que el número lo ingrese el usuario
try:
    numero_ingresado = int(input("Ingrese un número positivo: "))
    imprimir_numeros_recursivos(numero_ingresado)
except ValueError:
    print("Valor ingresado incorrecto. Debe ser un número entero positivo.")


