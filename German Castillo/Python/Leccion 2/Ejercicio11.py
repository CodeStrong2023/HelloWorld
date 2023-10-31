'''
Suponga que se tiene  un conjunto de calificaciones de un grupo de 10 alumnos,
Realizar un algoritmo para calcular la calificacion promedio  y la calificacion
mas baja de todo el grupo
'''


calificacion_baja = 99999;
calificacion = 0;
suma = 0;

for i in range(0,10):
    calificacion = int(input(f'Ingresar la nota del  {i+1}º alumno :'))
    if calificacion< calificacion_baja:
        calificacion_baja = calificacion
    
    suma += calificacion
calificacion_promedio = suma /10;
print(f'la calificacion promedio es: {calificacion_promedio}' )
print(f'la califiacaion mas baja es: {calificacion_baja}')

