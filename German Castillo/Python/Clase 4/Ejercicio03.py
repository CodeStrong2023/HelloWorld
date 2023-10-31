#Ejercicio 03: Insertar elementos y ordenarlos
#Pedir numeros y meterlos en una lista, cuando el usuario
#introduxca un numero 0, nuestro prodrama dejaria de insertar.
#Por ultimo, mostrar los numeros ordenados de mayor a menor

lista =[]
salir = False;
while not salir:
    numero = int(input('Digite un numero: '))
    if numero == 0:
        salir = True;
    else:
        lista.append(numero)
lista.sort() #Ordenamos la lista
print(f'\nLista ordenada: \n{lista}');
