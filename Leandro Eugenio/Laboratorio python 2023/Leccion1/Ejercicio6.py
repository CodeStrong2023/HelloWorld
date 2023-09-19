'''
Ejercicio: Etapas de vida
haremos un programa que cuando el usuario ingrese su edad
le diga, o imprima la etapa de su vida en una breve oracion

0 a 10 = la infancia es increible y bella
10 a 19 = Tienes muchos cambios, mucho que estudiar
20 a 29 = Amor y comienza el trabajo
para las siguientes etapas, deberas completarlo
'''

edad = int(input('Digite su edad: '))
mensaje = None

if 0 <= edad < 10 :
    mensaje = 'La infancia es increible y bella'
elif 10 <= edad < 20:
    mensaje = 'Tienes muchos cambios, mucho que estudiar'
elif 20 <= edad < 30:
    mensaje = 'Amor y comienza el trabajo'
elif 30 <= edad < 40:
    mensaje = 'Disfrute en Familia'
elif 40 <= edad < 50:
    mensaje = 'Trayeco final del trabajo'
elif 50 <= edad < 60:
    mensaje = 'Jubilacion y tiempo libre'
elif 60 <= edad < 70:
    mensaje = 'Dolores y remedios'
else:
    mensaje = 'Etapa final'

print(f'Su etapa de vida es: {mensaje}')