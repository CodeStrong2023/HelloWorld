#Ejercicio 6: Tabla de multiplicar
#hacer un programa que pida un numero por teclado y lo guarde en una lista junto a su tabla de
#multiplicar hasta el 10. por ejemplo: si digita el 5 la lista sera: 5,10,15,20,25,30,35..50

numero = int(input("Digite un numero: "))
lista = [] #creamos una lista vacia
for i in range(1,11):
    lista.append(i*numero)

print(f"Tabla de multiplicar del {numero}: {lista}")

for indice,i in enumerate(lista):
    print(f"{numero} x {i} = {lista[indice]}") #este ciclo es para ver el formato de una tabla de multiplicar