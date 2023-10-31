""" Ejercicio 4: Área y longitud de un circulo
Hacer un programa para ingresar el radio de un circulo y se reporte su área y la longitud de la circunferencia.

Área = Pi * r2
Longitud = 2 * Pi * r
En este ejercicio vamos a necesitar importar el modulo math porque tiene el valor de Pi
Se escribe:   import math
 """

import math;

radio = float(input('ingresa el valor del radio'))

area = math.pi * (radio**2)
Longitud = 2 * math.pi * radio

print(f'\n El area del circulo es igual a = {area} \n la Longitud del circulo es igual a = {Longitud}')
