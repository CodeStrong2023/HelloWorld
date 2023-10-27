import math;
#Dada la siguiente tupla
tupla = (13, 1, 8, 3, 2, 5, 8) #Definimos la tupla
#Crear una lista que solo incluya los numeros menores a 5
#e imprima por consola [1,2,3]
lista = []

for n in tupla:
    if n < 5:
        lista.append(n)

print(lista)


#Ejercicio de Matematicas
#Para sacar la raiz cuadrad de un numero positivo
numero = int(input('Digite un numero positivo :'))
while numero < 0:
    print('Error -> Deberia ser un numero positivo')
    numero = int(input('Digite un numero positivo'))

print(f'\nSu raiz cuadrada es: {math.sqrt(numero):.2f}') 
