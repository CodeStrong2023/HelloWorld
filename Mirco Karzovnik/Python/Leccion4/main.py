# lista = Ariel, Liliana, Natalia, Osvaldo
#Colecciones en Python
# Las listas es lo que se conoce en otros lenguajes como arrreglos o vectores

nombres = ["Nati", "Osvaldo", "Lily", "Ariel"]
print(nombres)
print(nombres[0:2]) # Solo muestra el indice 0,1 pero no el indice 2
#ir del inivio de la lista al indice (sin incluirlo)
print(nombres[ :3]) # indices a mostrar 0,1 , 2
print(nombres[1: ])
#Modificamos un valor
nombres[2] = "Liliana"
nombres[0] = "Natalia"
print(nombres)
#Iterar una lista
for nombre in nombres: #nombre es singular , la lista es plural
    print(nombre)
else:
    print("Se acabaron los elementos de la lista")

#Preguntamos cunatos elementos  tiene
print(len(nombres))
#agregamos un elemento
nombres.append("Marcelo")
nombres.append([1, 2, 3])
nombres.append(True)
nombres.append(10.40)
nombres.append([1, 9])
nombres.append(7)
print(nombres)

#Insetar un elemento en un indice especifico
nombres.insert(1,"Alberto")
print(nombres)
nombres.insert(3, "Debora")
print(nombres)
#eliminamos un elemento
nombres.remove("Alberto")
print(nombres)

#Eliminar el ultimo elemento
nombres.pop()
print(nombres)
#eliminar un indice especifico
del nombres[2] #del significa detele
print(nombres)

#eliminar, borrar o limpiar todos los elementos
nombres.clear()
print(nombres)



#definicimos una tupla
cocina = ("cuchara", "cuchillo", "tenedor")
print(len(cocina))

#acceder a un elemento, para esto utilizamos corchetes no parentesiss
print(cocina[0])
# mostrar de manera inversa
print(cocina[-1])

#Acceder a un rango
print(cocina[0:2])
#ejemplo
verduras = ("papa",) #un tupla necesita aunque sea un elemento: la coma
# de lo contrario soslo seria un tipo str cadena

#Recorremos los elementos de la tupla
for cocinar in cocina: #print esta usando /n para saltos de lineas
    print(cocinar, end=" ")  #Usamos end= para eliminar los saltos de lineas

cocinaLista = list(cocina)
cocinaLista[0] = "Plato"
cocina = tuple(cocinaLista)
print("/n", cocina)
#del cocina puede eliminar una tupla

#tipo set
planetas = {"Marte", "Jupiter", "Venus"}
print(planetas)
print(len(planetas)) #usamos la funcion len = length significa largo

#revisar si un elemento existe dentro de set
print("Marte" in planetas)

#Agregar un elemento
planetas.add("tierra") #add es una funcion
print(planetas)

#eliminar elementos
planetas.remove("Jupiter")
print(planetas)
planetas.discard("Marte")
print(planetas)

# "Maradona":10 un diccionario esta compuesto por dos elementos
#Una llave y un valor
#dict(key,value)
diccionario = {
    "IDE" : "Integrated Development Environment",
    "POO" : "Programacion Orientada a Objetos",
    "SABD" : "Sistema de Administracion de Base de Datos"
}
# Verificar la cantidad de elementos del diccionario
print(len(diccionario))
print(diccionario)

# Acceder a un diccionario con la llave(key)
print(diccionario["IDE"])

# Otra forma de recuperar un elemento
print(diccionario.get("POO"))
print(diccionario.get("SABD"))

# MODIFICAMOS ELEMENTOS
diccionario["IDE"] = "Integrated Development Environment"
#Como reccorer los elementos
for termino in diccionario:
    print(termino)
#Necesitamos una funcion para recorrer un diccionario
for termino, valor in diccionario.items():
    print(termino, valor)
# Otrass maneras de acceder a un diccionario
for termino in diccionario.keys():
    print(termino) # solo muestra las llaves
for valor in diccionario.values():
    print(valor)
#Comprobar la existencia de algun elemento
print("IDE" in  diccionario)

#Agregar un elelemto
diccionario["OK"] =  "Primary key"
print(diccionario)

#Eliminar un elem
diccionario.pop("SABD")
print(diccionario)

#vaciar un diccionario
diccionario.clear()
print(diccionario)
#eliminar completamente
del diccionario

#Concatenamos listas
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = lista1+lista2
print(lista3)

lista3.extend([7, 8, 9]) #funcionar para agregar varios elelemtnos a la lista
print(lista3)

print(lista3.index(5)) #funcion para unbicar en que el indice esta el valor ingresando # print lista3.index(0) # esto daria error por nos ser el elelemtno de la parte

print(lista3.count(1))

lista3.reverse()
print(lista3)

#Para qeu una lista se multiplique repitiendo sus elementos
lista = lista3 * 2
print(lista3)

#metodo de ordenamiento
lista3.sort()
lista3.sort(reverse=True)
print(lista3)
tupla = (4, "Hola", 6,78, [1, 2, 78], 4, "Hola")
print(tupla) #pouede tener diferentes tipos de datos dentro

print(4 in tupla)
