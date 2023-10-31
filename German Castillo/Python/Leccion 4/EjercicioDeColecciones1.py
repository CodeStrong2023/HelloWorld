#Ejercicio 1: Eliminar duplicado de una lista
# Escriba un programa donde tenga una lista y que a continuacion
#Elimine los elementos repetidos, por ultimo mostrar la lista.

#Creamos una lista

lista = [1,2,3,'Leandro','Leandro',1,2,3,'Eugenio'];
#conjunto = set(lista);
#print(conjunto);
lista = list(set(lista));
print(lista);