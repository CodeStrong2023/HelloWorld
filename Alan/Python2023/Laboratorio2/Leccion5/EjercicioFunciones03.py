#Ejercicio 03: funcion rescursiva
#imprimir numeros de 5 a 1 de manera descendente usando funciones recursivas
#puede ser cualquier valor positivo, por ejemplo, si pasamos el valor de 5, debe imprimir:
#5 4 3 2 1
#si se ingresan numeros negativos no imprime nada

def imprimir_numeros_recursivos(numero):
    if numero >=1:
        print(numero)
        imprimir_numeros_recursivos(numero-1)
    elif numero == 0:
        return
    elif numero <= 0:
        print("Valor ingresado incorrecto")

numEleccion = int(input("Ingrese un numero: "))
imprimir_numeros_recursivos(numEleccion)