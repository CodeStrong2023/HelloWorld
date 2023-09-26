# Ejercicio 1: Eliminar duplicados de una lista
# Escriba un programa donde tenga una lista y que a continuación
# elimine los elementos repetidos, por último mostrar la lista.

# Creamos la lista
lista = [1, 2, 3, "Flor", 7, 7, 3, "Regina", 5, "Flor", 2, "Rufi", 8]
# conjunto = set(lista) # Convertimos la lista a un conjunto de tipo set
# lista = list(conjunto) # Convertimos el conjunto a una lista
lista = list(set(lista)) # La conversión hecha en una sola línea de código
print(lista)
