# Dada la siguiente tupla

tupla = (13, 1, 8, 3, 2, 5, 8) # Definimos la tupla

# Crear una lista que solo incluya los numeros menores a 5
# E imprima por consola [1, 3, 2]

lista = [] # Definimos la lista

# Filtramos los elemntos menors a 5 de la tupla
for elemento in tupla:
    if elemento < 5:
        lista.append(elemento)
print(lista)