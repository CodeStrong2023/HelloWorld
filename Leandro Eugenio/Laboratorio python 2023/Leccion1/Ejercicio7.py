'''
    Ejercicio 5: Sistema de Calificaciones

El objetivo del programa sera crear un sitema
de calificaciones de la siguiente manera:
Le pedimos al usuario que ingrese un valor del 0 al 10

Luego si ingreso 9 o 10 imprimimos A
Entre 8 y menor a 9 imprimimos B
entre 7 y menor a 8 imprimimos C
entre 6 y menor a 7 imprimimos D
entre 0 y menor a 8 imprimimos F
De lo contrario al valor ingresado es correcto
'''
calificacion = int(input('Digite la calificacion entre 0 a 10: '))
if 9 <= calificacion <= 10:
    print('A')
elif 8 <= calificacion < 9:
    print('B')
elif 7 <= calificacion < 8:
    print('C')
elif 6 <= calificacion < 7:
    print('D')
elif 0 <= calificacion < 6:
    print('F')
else:
    print('VALOR INCORRECTO')
