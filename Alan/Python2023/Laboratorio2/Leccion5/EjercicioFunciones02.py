#Ejercicio 02: funcion con *args para multiplicar
#crear una funcion para multiplicar los valores recibidos
#de tipo numerico, utilizando argumentos variables *args
#como parametro de la funcion y regresar como resultado
#la multiplicacion de todos los valores pasados como argumento

def multValor(*args): #creamos una funcion para que agregen valores infinitos
    resultado = 1 #inicializamos variable
    for valor in args:
        resultado*=valor #multiplicamos los valores ingresados
    return resultado

print(multValor(3,5,15,3)) #mostramos el resultado llamando a la funcion