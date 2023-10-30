import math #importamos la clase math para hacer uso de la funcion sqrt(raiz cuadrada)

#dada la siguiente tupla
tupla = (13, 1, 8, 3, 2, 5, 8) #definir la tupla
#crear una lista que solo incluya numeros menores a 5
#e imprima por consola [1, 3, 2]
lista = []
for elemento in tupla:
    if elemento <5:
        lista.append(elemento)
print(lista)

#ejercicio matematicas
#para sacar la raiz cuadrada de un numero positivo
numero = int(input("Digite un numero positivo"))
while numero < 0:
    print("error -> deberia ser un numero positivo")
    numero = int(input("Digite un numero positivo"))
print(f"su raiz cuadrada es: {math.sqrt(numero):.2f}")