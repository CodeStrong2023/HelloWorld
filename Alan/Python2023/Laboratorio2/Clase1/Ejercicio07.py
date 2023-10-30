#Ejercicio 7: Juego adivina el numero
#realizar un juego para adivinar un numero. para ello se debe generar un numero aleatorio entre 1 - 100
#y luego ir pidiendo al usuario que adivine, si ingresa uno menor se le avisa que ingrese uno mayor,
#si ingresa uno mayor se le avisa que ingrese uno menor, cuando adivine, mostrar el numero que adivino y la cantidad
#de intentos realizados.

import random
print(f"Juego adivina el numero")
aleatorio = random.randint(0,100) #genera numero aleatorio de 0 a 100
contador = 0 #contador para mostrar los intentos del jugador

while True:
    numero = int(input("Digite un numero: ")) #pedimos el numero
    contador+= 1 #contador en aumento
    if numero > aleatorio:
        print("No es el numero, ingrese un numero menor")
    elif numero < aleatorio:
        print("No es el numero, ingrese un numero mayor")
    else:
        print(f"Felicidades, adivinaste, el numero era: {aleatorio}")
        break
print(f"La cantidad de intentos fue: {contador}")