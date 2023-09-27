#Ejercicio 01 : crear una funcion pàra sumar los valores recibidos de tio
#numericos, utilizando argumentos variables *args como parametor de la
#funcion y agregar como resultado la suma de todos los valores pasados
#como argumentos.
#Definimos una funcion

def sumarValor(*args):#Recibimos una cantidad de parametros indefinidos
    resultado = 0;
    for valor in args:
        resultado += valor;
    return resultado

#LLmamaos a la funcion
print(sumarValor(3,5,9))
    
