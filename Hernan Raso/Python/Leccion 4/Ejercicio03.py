# Ejercicio 3: Insertar elementos y ordenarlos, Pedir numeros y meterlos en una lista, cuando el usuario
# intruzca un numero 0, nuestro programa dejaria de insertar. Por ultimo, mostrar los numeros ordenados
# de menos a mayor

lista = []
salir = False
while not salir:
    numero = int(input('Ingrese un numero: '))
    if numero == 0:
        salir = True
    else:
        lista.append(numero)
lista.sort() # La lista esta ordenada con esta funcion
print(f'\nLista Ordenada: \n´{lista}')
