'''
Diseñar un programa que ingresado un año, nos devuelva por consola
si es un año bisiesto o no, repetir la accion hasta que el usuario 
lo decida

'''
num = None
opcion = "S"

while opcion != "N":
    num = int(input('Digite el año '))
    if num % 4 == 0 and num % 100 == 0 or num % 480 == 0 :
        print(f'El año {num} es bisiesto')
    else:
        print('No es bisiesto')
    
    opcion = input('Desea saber si otro año es bisiesto? ingresa "S" o "N"')
    opcion = opcion.upper()

    