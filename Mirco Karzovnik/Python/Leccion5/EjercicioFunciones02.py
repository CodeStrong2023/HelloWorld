# Ejercicio 2: Funcion con *args para multiplicar
# Crear una funcion para multiplicar los valores recibidos
# de tipo numerico , utilizandop argunemtnos variables *args
# como parametro de la funcion y regresar como resultado
# la multiplicacion de todos los valroes pasados como argumentos

#Definimos la funcion para multiplicar
def multiplicar_valores(*args):
    resultado = 1
    for numero in args:
        resultado *= numero

print(multiplicar_valores(3, 5, 15))

