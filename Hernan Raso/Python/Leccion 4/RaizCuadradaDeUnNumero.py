import math  # Importamos la clase math para hacer uso de la funcion sqrt (Raiz Cuadrada)
# Ejercicio de Matematicasd
# Para sacar la Raiz cuadrada de un numero Positivo


numero = int(input("Ingrese un numero Positivo: "))
while numero < 0:
    print("Error -> deberia ser un numero positivo")
    numero = int(input("Ingrese un numero positivo: "))
print(f'\nSu raiz cuadrada es: {math.sqrt(numero):.2f}')

