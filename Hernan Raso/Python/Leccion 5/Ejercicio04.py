# Ejercicio 4: sumar numeros pares dentro de un rango, hacer un programa para sumar numeros pares dentro de
# un rango, por ejemplo:
# suma de numeros pares del 2 al 30
# Suma = 240

a = int(input("Ingrese desde donde va a comenzarl la suma: "))
b = int(input("Ingrese hasta donde quiere llegar a sumar: "))
suma = 0
for i in range(a, b+1):
    if i%2== 0: # Esti es si el numero es par
        suma += i
print(f"\nLa suma de numeros pares dentro del rango es: {suma}")
