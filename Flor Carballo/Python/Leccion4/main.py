# lista = Florencia , Regina , Rufina , Santiago
"""
nombres = ["Rufi","Santi","Regi","Flor"]
print(nombres)
print(nombres[0:2]) #Solo muestra el indice 0, 1 pero no el indice 2
# Ir del inicio de la lista al índice (SIN INCLUIRLO)
print(nombres[ :3]) # Indices a mostrar 0, 1, 2
# Desde el indice indicado hasta el final
print(nombres[1: ])
# Modificamos un valor
nombres[2] = "Regina"
nombres[0] = "Rufina"
print(nombres)
# Iterar una lista
for nombre in nombres: # nombre es singular, la lista es plural
    print(nombre)
else:
    print("Se acabaron los elementos de la lista")

# Preguntamos cuantos elementos tiene
print(len(nombres)) # Le pasamos como parámetro la lista

# Agregamos un elemento
nombres.append("Marcelo")
nombres.append([1, 2, 3])
nombres.append(True)
nombres.append(10.45)
nombres.append([4, 5])
nombres.append(7)
print(nombres)
#Insertar un elemento en un indice específico
nombres.insert(1,"Jorge")
print(nombres)
nombres.insert(3,"Facundo")
print(nombres)
# Eliminamos un elemento
nombres.remove("Facundo")
print(nombres)
# Eliminar el último elemento
nombres.pop()
print(nombres)
# Eliminar un índice específico
del nombres[2]
print(nombres)
# Eliminar, borrar o limpiar todos los elementos
nombres.clear()
print(nombres)
# Eliminar la lista
del nombres
print(nombres)


Sintaxis de Range(inicio<opcional>, fin <requerido>, incremento <opcional>)

# Ejercicio 1: Iterar un rango de 0 a 10 e imprimir números divisibles entre 3
# Ejemplo de ejecución: 0, 3, 6, 9
print("Rango de 0 a 10 con números divisibles entre 3")
for i in range(11):
    if i % 3 == 0:
        print(i)

# Ejercicio 2: Crear un rango de números de 2 a 6 e imprimelos
# Ejemplo de ejecución: 2, 3, 4, 5, 6
print("Rango con valores de inicio = 2 y fin = 6")
rango = range(2,7)
for i in rango:
    print(i)

# Ejercicio 3: Crear un rango de 3 a 10 pero con incremento de 2 en 2, en lugar de 1 en 1
# Ejemplo de ejecución: 3, 5, 7, 9
print("Rango con valores de inicio = 3, fin = 10, incremento = 2")
for i in range(3, 11 ,2):
    print(i)
"""
"""# Definimos una tupla
cocina = ("cuchara", "cuchillo", "tenedor")
print(len(cocina))

# Acceder a un elemento, para esto utilizamos corchetes no parentesís
print(cocina[0])
# mostrar manera inversa
print(cocina[-1])

# Acceder a un rango
print(cocina[0:2])

# Ejemplo
verduras = ("papa", ) # Una tupla aunque sea un elemento la coma
# De lo contrario, solo seria un tipo str cadena

# Recorremos los elementos de la tupla
for cocinar in cocina:
    print(cocinar, end= " ")

cocinaLista = list(cocina)
cocinaLista[0] = "plato"
cocina = tuple(cocinaLista)
print("\n", cocina)

# del cocina
print(cocina)
"""
"""
# Tipo set
planetas = {"Marte", "Júpiter", "Venus"}
print(len(planetas)) # Usamos la función len = length significa largo

# Revisar si un elemento existe dentro del set
print("Júpiter" in planetas)

# Agregar un elemento
planetas.add("Tierra") # add es una función
print(planetas)

# Eliminar elementos, puede arrojar un error si el elemento no existe
planetas.remove("Júpiter") # Esta función ante un mal ingreso u inexistencia del elemento da error
print(planetas)
planetas.discard("tierra") # Esta función no nos presenta ningún error
print(planetas)

# Limpiar set
planetas.clear()
print(planetas)

# Eliminar set o conjunto
del planetas
#print(planetas) # Al eliminar nos muestra error
"""

# "Maradona": 10 Un diccionario esta compuesto por dos elementos
# Una llave y un valor
# dict(key,value)
diccionario = {
    "IDE": "Integrated Development Enviroment",
    "POO": "Programación Orientadfa a Objetos",
    "SABD": "Sistema de Administración de Base de Datos"
}
# Verificar la cantidad de elementos del diccionario
print(len(diccionario))
print(diccionario)

# Acceder a un diccionario con la llave(key)
print(diccionario["IDE"])

# Otra forma de recuperar un elemento
print(diccionario.get("POOP"))
print(diccionario.get("SABD"))

# Modificamos elementos
diccionario["IDE"] = "Entorno de Desarrollo Integrado"
print(diccionario)

# Como recorrer los elementos
for termino in diccionario:
    print(termino)

for termino, valor in diccionario.items():
    print(termino, valor)
# Otras maneras de acceder a un diccionario
for termino in diccionario.keys():
    print(termino)

for valor in diccionario.values():
    print(valor)
# Comprobar la existencia de algún elemento
print("IDE" in diccionario) # Devuelve un booleano
# Agregar un elemento
diccionario["PK"] = "Primary Key"
print(diccionario)
# Eliminar un elemento
diccionario.pop("SABD")
print(diccionario)
# Vaciar un diccionario
diccionario.clear()
print(diccionario)

# Concatenamos listas
lista1 = [1, 2, 3, 1]
lista2 = [4, 5, 6, 1]
lista3 = lista1+lista2
print(lista3)

lista3.extend([7, 8, 9, 1]) # Función para agregar varios elementos a una lista
print(lista3)

print(lista3.index(5))

# Como saber cuantos valores repetidos hay dentro de una lista
print(lista3.count(1))

# Para poner al reves una lista
lista3.reverse()
print(lista3)

# Para que una lista se multiplique repitiendo sus elementos
lista3 = lista3 * 2
print(lista3)

# Métodos de ordenamiento
lista3.sort()
print(lista3)
lista3.sort(reverse=True)
print(lista3)

# Repaso de Tuplas
tupla = (4, "Hola", 6.78, [1, 2, 78], 4, "Hola") # Puede tener diferentes tipos de datos dentro
print(tupla)

print(4 in tupla) # Acción booleana, su respuesta es de tipo booleana
# Lo que podemos usar dentro de tuplas son: index, count, len
# En tuplas se puede convertir de tupla a lista y de lista a tupla

# Repaso de set o conjunto para definir un conjunto
conjunto2 = set()
conjunto1 = {"bye", }
conjunto2.add(7)
conjunto2.add("Hola")
print(conjunto2)
conjunto1.add("Hola")
print(conjunto1)
print(3 not in conjunto1)

# Como hacer la igualdad de dos conjuntos
print(conjunto1 == conjunto2) # Nos devuelve como respuesta un booleano

# Operaciones en conjuntos
conjunto3 = conjunto1 | conjunto2 # La línea une los dos conjuntos
print(conjunto3)

conjunto3 = conjunto1 & conjunto2 # Que elemento tienen en común
print(conjunto3)

conjunto3 = conjunto1 - conjunto2 # Asigna un valor que esta en el conjunto1 y no en el conjunto2
print(conjunto3)
conjunto3= conjunto2 - conjunto1
print(conjunto3)

conjunto3 = conjunto1 ^ conjunto2 # Elementos que no comparten o que son diferentes entre ambos
print(conjunto3)

conjunto3 = conjunto1 | conjunto2
print(conjunto2.issubset(conjunto3)) # Aqui preguntamos si un conjunto es un subconjunto dentro de otro
print(conjunto1.issubset(conjunto3))
print(conjunto3.issubset(conjunto1))
print(conjunto3.issubset(conjunto2))

print(conjunto3.issubset(conjunto1)) # Preguntamos si los elementos del conjunto1 estan dentro del 3
print(conjunto3.issubset(conjunto2)) # Si es verdadero quiere decir que el conjunto3 es un superconjunto
print(conjunto2.issubset(conjunto3))

# Como saber si ambos conjuntos son disconexos, esto es si no comparten elementos en común
print(conjunto1.isdisjoint(conjunto2)) # No hay cosas en común

# Convertir un conjunto totalmente en inmutable
conjunto1 = frozenset # Esto hace que el conjunto sea totalmente inmutable
# No se puede agregar, modificar ni eliminar elementos del conjunto

# Repaso Diccionarios
diccionarioNuevo = {"Azul": "Blue", "Rojo": "Red", "Verde": "Green", "Amarillo": "Yellow"}
print(diccionarioNuevo)

# Como eliminar
del (diccionarioNuevo["Azul"])
print(diccionarioNuevo)

# Los diccionarios pueden almacenar diferentes tipos de datos
diccionario2 = {"Flor": {"Edad": 20, "Altura": 1.64}, "Regina": [4, 35], "Rufina": [1, 25]}
print(diccionario2)

seleccionArgentina = {
    10: {"Nombre": "Lionel Messi", "Edad": 35, "Altura": 1.70, "Precio": "50 Millones", "Posicion": "Extremo Derecho"},
    11: {"Nombre": "Angel Di Maria", "Edad": 34, "Altura": 1.80, "Precio": "12 Millones", "Posicion": "Extremo Derecho"},
    21: {"Nombre": "Paulo Dybala", "Edad": 28, "Altura": 1.77, "Precio": "35 Millones", "Posicion": "Media Punta"},
    19: {"Nombre": "Nicolás Otamendi", "Edad": 34, "Altura": 1.83, "Precio": "3.5 Millones", "Posicion": "Defensa Central"},
    1: {"Nombre": "Franco Armani", "Edad": 35, "Altura": 1.89, "Precio": "3.5 Millones", "Posicion": "Portero"},
    23: {"Nombre": "Emiliano Martinez", "Edad": 31, "Altura": 1.95, "Precio": "40 Millones", "Posicion": "Portero"},
    5: {"Nombre": "Rodrigo De Paul", "Edad": 29, "Altura": 1.80, "Precio": "35 Millones", "Posicion": "Medio Campo"},
    8: {"Nombre": "Enzo Fernandez", "Edad": 22, "Altura": 1.78, "Precio": "35 Millones", "Posicion": "Medio Campo"},
    9: {"Nombre": "Julián Álvarez", "Edad": 23, "Altura": 1.70, "Precio": "35 Millones", "Posicion": "Delantero Centro"}
}
for llave, valor in seleccionArgentina.items():
    print(llave, valor)

print("Tenemos cargados en el diccionario la cantidad de: ", end=" ")
print(len(seleccionArgentina))

# Pilas usando Listas
pila = [1, 2, 3]

# Agregar elementos a la pila por el final
pila.append(4)
pila.append(5)
print(pila)

# Sacamos elementos desde el final
elementoBorrado = pila.pop()
print(f"Sacamos el elemento: {elementoBorrado}")
print(f"La pila ahora quedo así: {pila}")

# Colas con listas
# Estructura de datos de tipo fifo(first input / first output)
cola = ["Flor", "Regi", "Rufi", "Santi"]

# Agregamos elementos al final de la cola
cola.append("Vero")
cola.append("Jorge")
print(cola)

# Sacamos elementos de la cola
seRetira = cola.pop(0)
print(f"Atendido el cliente: {seRetira}")
print(cola)
seRetira = cola.pop(0)
print(f"Atendido el cliente: {seRetira}")
print(cola)
seRetira = cola.pop(0)
print(f"Atendido el cliente: {seRetira}")
print(cola)
seRetira = cola.pop(0)
print(f"Atendido el cliente: {seRetira}")
print(cola)

for i in seleccionArgentina:
    print(f"{i} -> {seleccionArgentina}")