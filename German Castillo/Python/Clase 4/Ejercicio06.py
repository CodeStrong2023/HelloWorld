""" Ejercicio 6: Tabla de multiplicar
hacer un programa que piuda un unhmero por teclado y guarde
en una ista su tabla de multiplicar hasta le 10. por ejemplo
Si digita el 5 la lista tendra: 5,10,15,20,25,30,35,40,45,50 """

n = int(input("Digite un numero"))
lista = [];

for i in range(1,11):
    lista.append(i*n)
print(f"la lista es: {lista}")
