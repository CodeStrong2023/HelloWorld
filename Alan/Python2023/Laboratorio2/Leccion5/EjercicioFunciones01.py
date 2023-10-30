#Ejercicio 01: crear una funcion para sumar los valores recibidos de tipo
#numericos, utilizando los argumentos variables *args como parametro de la
#funcion y agregar como resultado la suma de todos los valores pasados como argumentos

#definimos funcion
def sumarValor(*args):  # recibimos una cantidad de parametros indefinidos
    resultado = 0
    #iteramos cada elemento
    for valor in args:
        resultado+=valor
    return resultado

print(sumarValor(3, 5, 9,2,1))
