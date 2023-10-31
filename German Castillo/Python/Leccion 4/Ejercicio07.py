""" Ejercicio 7: Juego adivina el numero
Realizar un juego para adivinar un numero. Para ello se debe
generar un numero aleatorio entre 1 - 100 , y luego ir pidiendo
numero indicando si "es mayor" o "es menor" segun sea mayor o menor 
con respecto al N. El proceso termina cuando el usuario acierta y
alli se debe mostrar el numero de intentos """
import random;
intentos = 0;
N = random.randint(1,100);
numero = int(input("Digite un numero: "))
while N != numero:
    if(numero < N):
        print("Es mayor")
        numero = int(input("ingresa un numero mas alto"))
    else:
        print("Es menor")
        numero = int(input("ingresa un numero mas bajo"))

print(f"\nPerfecto el numero aleatorio era {N}")
