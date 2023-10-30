#Ejercicio 10: no repetir caracteres
#hacer un programa que pida una cadena por teclado, luego metes los caracteres
#en una lista sin repetir caracteres.

cadena = input("Digite una cadena: ") #pedimos la cadena
lista = [] #creamos una lista vacia
for i in cadena:
    if i not in lista: #si el caracter no esta en la lista
        lista.append(i) #lo agregamos a la lista
print(f"Lista de caracteres sin repetir ninguno: {lista}")