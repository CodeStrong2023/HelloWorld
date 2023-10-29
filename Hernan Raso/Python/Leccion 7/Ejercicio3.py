# Ejercicio 3: Funcion recursiva
# Imprimir numeros de 6 a 1 de manera descemdente usando funciones recursivas puede ser cualquier valor positivo,
# por ejemplo, si pasamos el valor de 5 debe imprimir 5, 4, 3, 2, 1, si se ingresan numeros negativos no imprime nada

def imprimir_numeros_recursivos(numero):
    if numero >= 1:
        print(numero)
        imprimir_numeros_recursivos(numero-1)
    elif numero == 0:
        return
    elif numero <= 0:
        print('El valor ingresado es incorrecto...')

imprimir_numeros_recursivos(1)

# Tarea: que el numero lo ingrese el usuario

numeroIngreso = int(input('Ingrese un numero: '))
def imprimir_numeros_recursivos(numero):
    if numero >= 1:
        print(numero)
        imprimir_numeros_recursivos(numero-1)
    elif numero == 0:
        return
    elif numero <= 0:
        print('El valor ingresado es incorrecto...')

imprimir_numeros_recursivos(numeroIngreso)