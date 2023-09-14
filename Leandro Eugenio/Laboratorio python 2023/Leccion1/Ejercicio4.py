""" Ejercicio 4: Área y longitud de un circulo
Hacer un programa para ingresar el radio de un circulo y se reporte su área y la longitud de la circunferencia.

Área = Pi * r2
Longitud = 2 * Pi * r
En este ejercicio vamos a necesitar importar el modulo math porque tiene el valor de Pi
Se escribe:   import math
 """
import math

r = float(input('Digite el radio: '))
area = math.pi * r ** 2
longitud = 2 * math.pi * r

print(f'El area del circulo es: {area}')
print(f'La longitud del circulo es: {longitud}')