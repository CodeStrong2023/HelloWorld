#sintaxis de range (inicio<opcional>, fin <requerido>, incremento <opcional>)

#ejercicio 1: Iterar un rango de 0 a 10 e imprimir los numeros divisibles entre 3
#ejemplo: 0,3,6,9

print("rango de 0 a 10, numeros divisibles por 3 ")
for i in range(11):
    if i % 3 == 0:
        print(i)
print("-----------------------------------------")

#ejercicio 2: Crear un rango de numeros de 2 a 6 imprimelos
#ejemplo: 2,,3,4,5,6

for i in range(2,7):
    print(i)
print("-------------------------------------")

#ejercicio 3: Crear un rango de 3 a 10 pero con incremento de 2 en 2.
#ejemplo: 3,5,7,9

for i in range(3,10,2):
    print(i)