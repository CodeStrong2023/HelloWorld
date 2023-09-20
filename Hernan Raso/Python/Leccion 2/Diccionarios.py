# 'Maradona' :10 Un diccionario esta compuesto por dos elementos
# Una llave y un valor
# dict(key, value)

diccionario = {
    'IDE':'Integrated Development Environment',
    'POO': 'Programacion Orientada a Objetos',
    'SABD':'Sistema de Administacion de Bases de Datos'
}
print(diccionario)
# Para ver la cantidad de elementos que contiene el diccionario
print(len(diccionario))

# Acceder a un diccionario con la llave (Key)

print(diccionario['IDE'])

# Otra forma de recuperar un elemento
print(diccionario.get('POO'))

print(diccionario.get('SABD'))

# Modificamos elementos
diccionario['IDE'] = 'Entorno de Desarrollo Integrado'
print(diccionario)

# Como recorrer los elementos
for termino in diccionario: # Recorremos mostrando solo las llaves
    print(termino)
# Necesitamos una funcion para recorrer un diccionario
for termino, valor in diccionario.items():
    print(termino, valor)

# Otras manerdas de acceder a un diccionario
for termino in diccionario.keys():  # Estamos usando una funcion
    print(termino)  # Muestra solo las llaves

for valor in diccionario.values():  # Usamos una funcion par aacceder al valor
    print(valor)

# Comprobar la existencia  de algun elemento

print('IDE' in diccionario) # Devuelve un booleano

# Agreagar un elemento al diccionario
diccionario['PK'] = 'Primary Key'
print(diccionario)

# Eliminar un elemento
diccionario.pop('SABD')
print(diccionario)

# Vaciar un diccionario
diccionario.clear()
print(diccionario)

# Eliminar diccionario
del diccionario # El diccionario se borro
#print(diccionario)

# Concatenamos listas
lista1 = [1, 2, 3, 1]

lista2 = [4, 5, 6, 1]

lista3 = lista1+lista2

print(lista3)

# Esto es una funcion para agregar varios elementos a la lista
lista3.extend([7, 8, 9, 1])
print(lista3)

print(lista3.index(5))  # Funcion para ubicar en que indice esta el valor ingresado
# print(lista3.index(0)) # Esto daria un error por no ser el elemento parte de la lista

# Como saber cuantos valores repetidos hay dentro de una lista
print(lista3.count(1))  # Cuenta cuantos valores iguales hay dentro de la lista


# Para poner al reves una lista
lista3.reverse()
print(lista3)

# Para que una lista se multiplique repitiendo sus elementos
lista = [1, 2, 3] * 2
print(lista)

lista3 = lista3 * 2
print(lista3)

# Metodos de ordenamiento
lista3.sort()  # Ordena los elemento de manera ascendente
print(lista3)

lista3.sort(reverse=True)  # Ordena descendentemente
print(lista3)

# Repaso de tuplas
tupla = (4, 'Hola', 6.78, [1, 2, 78], 4, 'Hola') # Puede tener difetentes tipos de datos dentro
print(tupla)

print(4 in tupla) # Accion booleana, su respuesta es de tipo booleana
# Lo que podemos usar dentro de las tuplas son: index, count, len
# En tuplas se puede convertit de tupla a lista y de lista a tupla

# Repaso de set o conjunto
# para definir un conjunto
conjunto = set()
conjunto1 = {'bye',}
conjunto.add(7)
conjunto.add('Hola')
print(conjunto)

conjunto1.add('Hola')
print(conjunto1)

print(3 not in conjunto1)  # Preguntamos si  el numero 3 No esta en el conjunto 1

# Como hacer la igualdad de dos conjuntos
print(conjunto1 == conjunto)  # Nos devuelve como respuesta un booleano

# Operaciones en conjuntos
conjunto3 = conjunto1 | conjunto  # La linea une los dos conjuntos
print(conjunto3)

conjunto3 = conjunto1 & conjunto  # Que elemento tienen en comun
print(conjunto3)

conjunto3 = conjunto1 - conjunto  # Asigna el valor que esta en el conjunto 1 y no en el conjunto
print(conjunto3)

conjunto3 = conjunto1 ^ conjunto  # Elementos que no comparten o que son diferentes entre ambos
print(conjunto3)

conjunto3 = conjunto1 | conjunto
print(conjunto1.issubset(conjunto3))  # Aqui preguntamos si un conjunto es un subconjunto dentro de otro
print(conjunto.issubset(conjunto3))
print(conjunto3.issubset(conjunto1))
print(conjunto3.issubset(conjunto))

print(conjunto3.issuperset(conjunto1))   # Preguntamos si los elementos del conjutno 1 estan dentro del 3
print(conjunto3.issuperset(conjunto))   # Si es verdadero quiere decir que el conjunto3 es un superconjunto
print(conjunto.issuperset(conjunto3))
print(conjunto1.issuperset(conjunto3))

# Como saber si ambos conjuntos son disconexos, esto es si no comparten elementos en comun
print(conjunto1.isdisjoint(conjunto))  # No hat cosas en comun

# Convertir un conjunto totalmente en inmutable
conjunto1 = frozenset  # Esto hace que el conjunto sea totalmente inmutable
# No se puede agregar, modificar ni eliminar elementos del conjunto

# Repaso Diccionarios

diccionarioNuevo = {'Azul' : 'Blue', 'Rojo' : 'Red', 'Verde' : 'Green', 'Amarillo' : 'Yellow'}
print(diccionarioNuevo)

# Como eliminar
del (diccionarioNuevo['Azul'])
print(diccionarioNuevo)

# Los diccionarios pueden almacenar diferentes tipos de datos
diccionario2 = {'Ariel' : {'Edad': 40, 'Altura' : 1.83}, 'Osvaldo' : [45, 1.85], 'Natalia' : [35, 1.67]}
print(diccionario2)

seleccionArgentina = {
    10: {'Nombre': 'Lionel Messi', 'Edad': 35, 'Altura': 1.70, 'Precio': '50 Millones', 'Posicion': 'Extremo Derecho'},
    11: {'Nombre': 'Angel Di Maria', 'Edad': 34, 'Altura': 1.80, 'Precio': '12 Millones', 'Posicion': 'Extremo Derecho'},
    24: {'Nombre': 'Paulo Dybala', 'Edad': 28, 'Altura': 1.77, 'Precio': '35 Millones', 'Posicion': 'Media Punta'},
    19: {'Nombre': 'Nicolas Otamendi', 'Edad': 34, 'Altura': 1.83, 'Precio': '3.5 Millones', 'Posicion': 'Defensa Central'},
    1: {'Nombre': 'Franco Armani', 'Edad': 35, 'Altura': 1.89, 'Precio': '3.5 Millones', 'Posicion': 'Portero'},

}
print(seleccionArgentina.values())

for llave, valor in seleccionArgentina.items():
    print(llave, valor)

# Como tarea Agregar por lo menos 4 jugadores mas al diccionario: seleccionArgentina

seleccionArgentina = {
    10: {'Nombre': 'Lionel Messi', 'Edad': 35, 'Altura': 1.70, 'Precio': '50 Millones', 'Posicion': 'Extremo Derecho'},
    11: {'Nombre': 'Angel Di Maria', 'Edad': 34, 'Altura': 1.80, 'Precio': '12 Millones', 'Posicion': 'Extremo Derecho'},
    24: {'Nombre': 'Paulo Dybala', 'Edad': 28, 'Altura': 1.77, 'Precio': '35 Millones', 'Posicion': 'Media Punta'},
    19: {'Nombre': 'Nicolas Otamendi', 'Edad': 34, 'Altura': 1.83, 'Precio': '3.5 Millones', 'Posicion': 'Defensa Central'},
    1: {'Nombre': 'Franco Armani', 'Edad': 35, 'Altura': 1.89, 'Precio': '3.5 Millones', 'Posicion': 'Portero'},
    18: {'Nombre': 'Guido Rodriguez', 'Edad': 29, 'Altura': 1.85, 'Precio': '28 Millones', 'Posicion': 'Pivote'},
    7: {'Nombre': 'Rodrigo de Paul', 'Edad': 29, 'Altura': 1.80, 'Precio': '40 Millones', 'Posicion': 'Mediocentro'},
    20: {'Nombre': 'Alexis Mac Allister', 'Edad': 24, 'Altura': 1.76, 'Precio': '65 Millones', 'Posicion': 'Mediocentro'},
    9: {'Nombre': 'Julian Alvarez', 'Edad': 23, 'Altura': 1.70, 'Precio': '60 Millones', 'Posicion': 'Delantero Centro'},

}

for llave, valor in seleccionArgentina.items():
    print(llave, valor)

print('Tenemos cargados en el diccionario la cantidad de jugadores: ', end= ' ')
print(len(seleccionArgentina))

# Pilas usando listas
pila = [1, 2, 3]

# Agregar elementos a la pila por el final
pila.append(4)
pila.append(5)
print(pila)

# Sacamos elementos desde el final
pila.pop()
print(pila)

# Quita el ultimo elemento y lo guarda en la variable
elementoBorrado = pila.pop()
print(f'Sacamos el elemento: {elementoBorrado}')
print(f'la Pila ahora quedo asi: {pila}')

# Colas con listas
# Estructura con datos de tipo fifo(first input / first output)

cola = ['Ariel', 'Osvaldo', 'Liliana', 'Pilar']

# Agregamos elementos al final de la cola
cola.append('Natalia')
cola.append('Jose')
print(cola)

# Sacamos elementos de la cola
seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)