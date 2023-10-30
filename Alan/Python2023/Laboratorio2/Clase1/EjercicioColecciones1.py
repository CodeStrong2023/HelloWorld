#Ejercicio 1 = eliminar duplicados en una lista

lista =[1,2,3,"Ariel",7,7,3,"Alberto",5,"Ariel",2,"Alberto"]
# conjunto = set(lista) //convertimos la lista a un conjunto tipo set
# lista = list(conjunto) //convertimos el conjunto a una lista
lista = list(set(lista)) #conversion hecha en una sola linea(es mas eficiente)
print(lista)

#la lista borra los duplicados, el conjunto no