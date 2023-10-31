#lista = Ariel, Liliana, Natalia, Osvaldo
#las listas tambien se conocen como arreglos o vectores

nombres = ["Ariel", "Liliana", "Natalia", "Osvaldo"]
print(nombres)
print(nombres[0])
print(nombres[1])
print(nombres[3])
print(nombres[-1])
print(nombres[-2])
print(nombres[0:2])#muestra todo antes del 2

#ir del inicio de la lista al indice (sin incluirlo)
print(nombres[ :3]) #muestra todo antes del indice 3

#desde el indice indicado hasta el final
print(nombres[1: ])
#modificamos un valor
nombres[2] = "Liliana"
nombres[0] = "Natalia"
nombres[1] = "Ariel"
print(nombres)

#iterar una lista
for nombre in nombres:
    print(nombre)
else:
    print("se acabaron los elementos de la lista")

#Preguntamos cuantos elementos tiene la lista
print(len(nombres))#Le pasamos como parametro la lista

#agregamos un elemento
nombres.append("Marcelo")
nombres.append([1,2,3])
nombres.append(True)
nombres.append([10,45])
nombres.append([4,5])
nombres.append(7)
print(nombres)

#insertar un elemento en un indice especifico
nombres.insert(1,"Alberto")
print(nombres)
nombres.insert(3,"Debora")
print(nombres)

#eliminamos un elemento
nombres.remove("Alberto")
print(nombres)

#eliminar el ultimo elemento
nombres.pop()
print(nombres)

#eliminar indice especifico
del nombres[2] #del = delete
print(nombres)

#eliminar todos los elementos
nombres.clear()
print(nombres)

#eliminar lista
del nombres

#la diferencia entre tuplas y listas es que la tupla tiene elementos inmutables (no se borran)
#la lista se escribe con [] y la tupla con (), las funciones de lista y tupla son similares

#definimos una tupla
cocina = ("cuchara", "cuchillo", "tenedor")
print(cocina)
print("largo de la tupla", len(cocina))
#mostramos el primer elemento
print(cocina[0])
#mostramos el ultimo
print(cocina[-1])

#mostramos rango
print(cocina[0:1])
#aunque se vea un solo elemento, igual tiene que llevar una coma, ejemplo: verduras = ("papa",)
#de lo contrario seria solo un tipo string

#recorremos los elementos de la tupla
for cocinar in cocina:
    print(cocinar) #este print usa /n para saltos de linea,si no lo quiero pongo (, end=" ")

#pasamos la tupla a lista y la lista a tupla (la lista puede modificarse, la tupla no)
Cocinalista = list(cocina)
Cocinalista[0] = "plato"
cocina = tuple(Cocinalista)
print(cocina)

#del cocina = eliminar variable

#tipo set
planetas = {"marte", "jupiter", "venus"}
print(planetas)
print(len(planetas))#largo del set

#revisar si un elemento esta dentro de set
print("marte" in planetas) #si se agrega not antes de in seria lo contrario

#agregar un elemento
planetas.add("tierra")#add es una funcion, si agregamos dos repetidos no se agrega
print(planetas)

#eliminar elementos, puede haber error si el elemento no existe
planetas.remove("jupiter")#esta funcion da error si el elemento no existe
print(planetas)
planetas.discard("tierra")#esta funcion no da ningun error
print(planetas)

#limpiar set
planetas.clear()
print(planetas)

#eliminar set
del planetas

#"Maradona" :10 Un diccionario esta compuesto por dos elementos
#Una llave y un valor
#dict(key, value)
diccionario={
    "IDE":"integrated development enviroment",
    "POO":"Programacion orientada a objetos",
    "SABD":"Sistema de administracion de base de datos"
}
#Cantidad de elementos en el diccionario
print(diccionario)
print(len(diccionario))

#acceder a un diccionario con la llave (key)
print(diccionario["IDE"])

#otra forma de recuperar un elemento
print(diccionario.get("POO"))
print(diccionario.get("SABD"))

#modificamos los elementos
diccionario["IDE"] = "Entorno de desarrollo integrado"
print(diccionario)

# como recorrer los elementos
for termino in diccionario: #recorremos mostrando solo las llaves
    print(termino)

#necesitamos una funcion para recorrer un diccionario
for termino, valor in diccionario.items():
    print(termino, valor)

#otras maneras de acceder a un diccionario
for termino in diccionario.keys():
    print(termino)#muestra solo las llaves

for valor in diccionario.values(): #usamos una funcion para acceder al valor
    print(valor)

#comprobar la existencia de algun elemento
print("IDE" in diccionario) #devuelve un booleano

#agregar un elemento
diccionario["PK"] = "Primary key"
print(diccionario)

#eliminar un elemento
diccionario.pop("SABD")
print(diccionario)

#vaciar diccionario
diccionario.clear()
print(diccionario)

#eliminar diccionario
del diccionario

#concatenamos listas
lista1 = [1,2,3]
lista2 = [4,5,6]
lista3 = lista1 + lista2
print(lista3)

lista3.extend([7,8,9,1]) #funcion para agregar varios elementos a la lista
print(lista3)

print(lista3.index(5))#funcion para ubicar en que indice esta el valor ingresado
#print(lista3.index(0)) daroa error por no tener el elemento en la lista

#como saber cuantos valores estan repetidos en la lista
print(lista3.count(1))#cuenta cuantos valores repetidos hay en la lista

#para poner la lista al reves
lista3.reverse()
print(lista3)

#para que una lista se multiplique repitiendo sus elementos
lista = [1,2,3] * 2
print(lista)

#metodos de ordenamiento, en python es una funcion
lista3.sort()#ubica los elementos ascendentemente
print(lista3)
lista3.sort(reverse=True)#ubica los elementos descendentemente
print(lista3)

#repaso tupla
tupla = (4, "hola", 6.78, [1,2,78],4,"hola") #puede tener diferentes datos dentro
print(tupla)

print(4 in tupla)#accion tipo booleana
#dentro de tuplas podemos usar: index, count, len
#en tuplas se puede convertir en tupla a lista y de lista a tupla

#repaso de set o conjunto
#para definir un conjunto
conjunto2 = set()
conjunto1 = {"bye",}
conjunto2.add(7)
conjunto2.add("Hola")
print(conjunto2)
conjunto1.add("Hola")
print(conjunto1)
print(3 in conjunto1)# preguntamos si el 3 esta en conjunto1

#comparar dos conjuntos para saber si son iguales
print(conjunto1 == conjunto2) #nos devuelve como respuesta un booleano

#operaciones en conjuntos
conjunto3 = conjunto1 | conjunto2 #la linea une los dos conjuntos
print(conjunto3)

conjunto3 = conjunto1 & conjunto2 #que elemento tienen en comun
print(conjunto3)

conjunto3 = conjunto1 - conjunto2 #asigna el valor que esta en el conjunto 1 y no en el conjunto 2
print(conjunto3)
conjunto3 = conjunto2 - conjunto1 #asigna el valor que esta en el conjunto 2 y no en el conjunto 1
print(conjunto3)

conjunto3 = conjunto1 ^ conjunto2 #elementos que no comparten o que son diferentes entre ambos
print(conjunto3)

conjunto3 = conjunto1 | conjunto2
print(conjunto2.issubset(conjunto3))# aqui preguntamos si un conjunto es un subconjunto dentro de otro
print(conjunto1.issubset(conjunto3))
print(conjunto3.issubset(conjunto1))
print(conjunto3.issubset(conjunto2))

print(conjunto3.issuperset(conjunto1))# preguntamos si los elementos del conjunto1 estan dentro del 3
print(conjunto3.issuperset(conjunto2))# si es verdadero quiere decir que el conjunto3 es un superconjunto
print(conjunto2.issuperset(conjunto3))

#como saber si ambos conjuntos son disconexos, esto es si no comparten elementos en comun
print(conjunto1.isdisjoint(conjunto2))#no hay cosas en comun

#convertir un conjunto totalmente inmutable
conjunto1 = frozenset #esto hace que el conjuntos sea totalmente inmutable
#no se puede agregar, modificar ni eliminar los elementos del conjunto

#repaso diccionarios
diccionarioNuevo = {"azul":"blue","rojo":"red","verde":"green","amarillo":"yellow"}
print(diccionarioNuevo)

#como eliminar
del (diccionarioNuevo["azul"])
print(diccionarioNuevo)

#los diccionarios almacenan diferentes tipos de datos
diccionario2 = {"Ariel":{"edad":40,"altura":1.83}, "Osvaldo": [45, 1.85], "Natalia":[35, 1.67]}
print(diccionario2)

seleccionArgentina = {
    10: {"Nombre":"Lionel Messi", "Edad":35, "altura":1.70, "Precio":"50 millones", "posicion":"Extremos derecho"},
    11: {"Nombre":"Angel Di maria", "Edad":34, "altura":1.80, "Precio":"12 millones", "posicion":"Extremos derecho"},
    21: {"Nombre":"Paulo Dybala", "Edad":28, "altura":1.77, "Precio":"35 millones", "posicion":"Media Punta"},
    19: {"Nombre":"Nicolas Otamendi", "Edad":34, "altura":1.83, "Precio":"3.5 millones", "posicion":"Defensa central"},
    1: {"Nombre":"Franco Armani", "Edad":35, "altura":1.89, "Precio":"3.5 millones", "posicion":"Portero"},
    8: {"Nombre": "Marcos Acuña", "Edad": 32, "altura": 1.70, "Precio": "15 millones", "posicion": "Defensa"},
    23: {"Nombre": "Emiliano Martinez (Dibu)", "Edad": 31, "altura": 1.95, "Precio": "28 millones", "posicion": "Portero"},
    20: {"Nombre": "Alexis Mac Allister", "Edad": 24, "altura": 1.76, "Precio": "70 millones", "posicion": "Mediocampo"},
}
#muestra un elemento del arreglo
print(seleccionArgentina[10])

#los muestra de manera mas ordenada
for llave, valor in seleccionArgentina.items():
    print(llave, valor)

print("tenemos cargados en el diccionario la cantidad de jugadores: ",end="")
print(len(seleccionArgentina))

#pilas usando listas
pila = [1, 2, 3]

#Agregamos elementos a la pila por el final
pila.append(4)
pila.append(5)
print(pila)

#sacamos elementos desde el final
elementoBorrado = pila.pop() #quita el ultimo elemento y lo guarda en la variable
print(f"sacamos el elemento: {elementoBorrado}")
print(f"la pila ahora quedo asi: {pila}")

#colas con listas
#estructura de datos tipo fifo(first input / first output)
cola = ["Ariel", "Osvaldo", "Liliana", "Pilar"]

#agregamos elementos al final de la cola
cola.append("Natalia")
cola.append("Jose")
print(cola)

#sacamos elementos de la cola
seRetira= cola.pop(0)
print(f"Atendido el cliente: {seRetira}")
print(cola)

seRetira= cola.pop(0)
print(f"Atendido el cliente: {seRetira}")
print(cola)

seRetira= cola.pop(0)
print(f"Atendido el cliente: {seRetira}")
print(cola)

seRetira= cola.pop(0)
print(f"Atendido el cliente: {seRetira}")
print(cola)

seRetira= cola.pop(0)
print(f"Atendido el cliente: {seRetira}")
print(cola)

seRetira= cola.pop(0)
print(f"Atendido el cliente: {seRetira}")
print(cola)

#seguimos mostrando como recorrer un diccionario con el ciclo for
for i in  seleccionArgentina:
    print(f"{i} -> {seleccionArgentina[i]}")