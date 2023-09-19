""" #Colecciones en Python

#Las listas son lo que se conoce como array o vectores en otros lenguajes
nombres= ['Ariel','Leandro', 'Marcos', 'Estela'];
print(nombres);
print(nombres[0])
print(nombres[-1])
print(nombres[-2])
print(nombres[0:2])

print(nombres[ :2])
print(nombres[2: ])

#Iterar una lista

for n in nombres:
    print(n)
else:
    print('Se acabaron los elementos de la lista')

#Agregamos un elemento 
nombres.append('Lucas')
print(nombres)
nombres.insert(3,'Fabricio')

#Eliminamos un elemnto

nombres.remove('Fabricio')
print(nombres)

#Eliminar el ultimo elemento
nombres.pop()
print(nombres)

#Eliminar indice especifico
del nombres[2] 

#Eliminar todos los elementos
nombres.clear()

#Eliminar la lista
del nombres

#Definimos un atupla
cocina = ('Cuchara','Cuchillo','Tenedor');
print(len(cocina))

#Acceder a un elemento dentro de la tupla, utilizamos corchetes
print(cocina[0])

#Acceder a un rango
print(cocina[0:2])

#Recorremos elementos de una tupla
for elemento in cocina:
    print(elemento, end='') #Usamos end para eleminar saltos de linea

cocinaLista = list(cocina)
cocinaLista[0] = 'plato'  
cocina = tuple(cocinaLista)
print('\n',cocina)

#Tipo set
planetas = {'marte', 'jupiter', 'venus'}
print(len(planetas))

#Revisar si un elemtno existe dentro de un set
print('Martes' in planetas)

#Agregar un elemtno
planetas.add('Tierra') #add es una funcion
planetas.add('Tierra') #No se puede duplICAR

#eLIMINAR ELEMENTOS, PUEDE ARROJAR UN ERROR SI EL ELEMENTO N O EXISTE

planetas.remove('Jupiter')
planetas.discard('Tierra')
print(planetas)

#limpiar set
planetas.clear()
#print(planetas)

#eliminar set
del planetas

#'Maradona' : 10 Un diccionario esta compuesto por dos elementos
#UNA LLAVE Y UN VALOR
#dic(key,value)
diccionario = {
    'IDE' : 'Integrated Development Environment',
    'POO' : 'Programacion orientada a objetos',
    'SABD': 'Sistema de administracion de base de datos'
}

print(diccionario)

#Verificar la cantidad de elementos
print(len(diccionario))
print(diccionario)

#Acceder a un diccionario con la llave(key)
print(diccionario['IDE'])

#oTRA FORMA DE RECUPERAR UN ELEMENTO
print(diccionario.get('POO'))
print(diccionario.get('SABD'))

#mODIFICAMOS ELEMENTOS
diccionario['IDE'] = 'Entorno de desarrollo integrado'
print(diccionario)

#como recorrer los elementos

for termino in diccionario: #recorremos mostrando solo las llaves
    print(termino)

for termino, valor in diccionario.items():
    print(termino,valor)

#Otras maneras de acceder a un diccionario
for termino in diccionario.keys():
    print(termino) #muestra solo las llaves

for valor in diccionario.values():
        print(valor) #usamos una funcion para acceder al valor()

#Comprobar la existencia de algun elemento
print('IDE' in diccionario)#devuelve un booleano

#Eliminamos un elemento
diccionario.pop('SABD')

#Vaciar un diccionario
diccionario.clear()
print(diccionario)

#Eliminar diccionario
del diccionario
 """
#concatenamos listas
listas1 = [1,2,3]
listas2 = [4,5,6]
listas3 = listas1 + listas2;
print(listas3)

listas3.extend([7,8,9]) #funcion para agregar varios elementos
print(listas3)

print(listas3.index(5)) #funcion para indicar en que indice esta el valor ubicado

#como saber cuantos valores se repiten
print(listas3.count(1))  #cuenta cuantos valores iguales hay dentro de la lista

#para poner al reves una lista
listas3.reverse()
print(listas3)

#Pasra que una lista se multiplique repitiendo sus elementos
listas3 = listas3 * 2
print(listas3)

#metodos de ordenamiento
listas3.sort() #Ordena ascendentemente todos los elementos
listas3.sort(reverse=True)
print(listas3)

tupla = (4, 'Hola', 6.78, [1,2,78],4, 'Hola') #Puedo tener elementos de diferentes tipos adentro
print(tupla)

print(4 in  tupla) #accion booleana, su respuesta es de tipo booleana
#lo que podemos uasr nadentro de tuplas son  : index,count, len
#En tuplas se puede convertir de tupla a lista y de lista a tupla

#Repaso de set o conjunto
#para definir un conjunto

conjunto = set();
conjunto1 = {'Bye'};
conjunto.add(7);
conjunto.add('Hola');
print(conjunto);
conjunto1.add('Hola');
print(conjunto1);
print(3 not in conjunto1) #preguntamos si el numero 3 no esta en el conjunto1

#Como hace rla igualdad de dos conjuntos
print(conjunto1 == conjunto) #Nos devulevo como respuesta un booleano

#Operaciones en conjuntos
conjunto3 = conjunto1 | conjunto #la linea une a los dos conjuntos
print(conjunto3)

conjunto3 = conjunto1 & conjunto #Que elementos tienen en comun
print(conjunto3)

conjunto3 = conjunto1 - conjunto #asigna el valor que esta en el conjunot 1 y no el conjunto
print(conjunto3)

conjunto3 = conjunto1 ^ conjunto #Elmentos que no comparten o son diferentes entre ambos

conjunto3 = conjunto1 | conjunto
print(conjunto.issubset(conjunto3)) #aqui preguntamos si un conjunto es subconjunto adentro de otro

#como saber si dos conjunot son disconexos, esto es si no compartene elemntos en comun
print(conjunto1.isdisjoint(conjunto)) #No hay cosas en comun

#Convertir un conjunot totalmente inmutabole
conjunto1 = frozenset #Esto hace que le conjunto sea totalmente inmutable
#No se puede agregar, modificar ni eleminar elementos del conjunto


#Repaso de Diccionario
diccionarioNuevo = {'Azul' : 'Blue', 'Rojo' : 'Red' , 'Verde' : 'Green', 'Amarillo' : 'Yellow'};
print(diccionarioNuevo)

#como eliminar
del (diccionarioNuevo['Azul'])
print(diccionarioNuevo)

#Los diccionarios pueden almacenar diferentes tipos de datos
dicciorio2 = {'Leandro' : {'edad' : 25, 'Altura' :1.83},'Ezequiel' : [45,1.76], 'Natalia' : [35, 1.67]}
print(dicciorio2);

seleccionArgentina ={
   10 : {'Nombre': 'Lionel Messi', 'Edad': 35, 'Altura': 1.70, 'Precio': '50 millones', 'Posicion': 'Extremo Derecho'},
   11 : {'Nombre': 'Angel Di Maria', 'Edad': 34, 'Altura': 1.80, 'Precio': '12 millones', 'Posicion': 'Extremo Izquierdo'},
   24 : {'Nombre': 'Paulo Dybala', 'Edad': 28, 'Altura': 1.77, 'Precio': '35 millones', 'Posicion': 'Media Punta'},
   19 : {'Nombre': 'Nicolas Otamendi', 'Edad': 35, 'Altura': 1.89, 'Precio': '3,5 millones', 'Posicion': 'Defensor Central'},
   23 : {'Nombre': 'Emiliano Martinez', 'Edad': 31, 'Altura': 1.95, 'Precio': '28 millones', 'Posicion': 'Arquero'},
   25 : {'Nombre': 'Lisandro Martinez', 'Edad': 25, 'Altura': 1.75, 'Precio': '50 millones', 'Posicion': 'Defensor Central'},
   20 : {'Nombre': 'Alexis Mac Allister', 'Edad': 24, 'Altura': 1.74, 'Precio': '65 millones', 'Posicion': 'Medio Centro'},
   10 : {'Nombre': 'Rodrigo de Paul', 'Edad': 29, 'Altura': 1.77, 'Precio': '40 millones', 'Posicion': 'Medio Centro'}

}

#Pilas usando listas
pila = [1,2,3]

#Agregar elementos a la pila po rle final
pila.append(4)
pila.append(5)
print(pila)

#Sacamos elementos desde el final
elementoBorrado = pila.pop() #  Quita el ultimo elemento y lo guarda en la variable
print(f'Sacamaos el elemento {elementoBorrado}')
print(f'La pila quedo asi: {pila}')

#Colas con listas
#Estructuras de datos de tipo fijo (first input / first output)
cola = ['Ariel', 'Osvaldo', 'Liliana', 'Pilar']

#Agregamos elementos al final de la cola
cola.append('Natalia')
cola.append('Jose')
print(cola)

#Sacamos elementos de la cola
SeRetira = cola.pop(0);
print(f'Atendido {SeRetira}')
print(cola)

SeRetira = cola.pop(0);
print(f'Atendido {SeRetira}')
print(cola)

SeRetira = cola.pop(0);
print(f'Atendido {SeRetira}')
print(cola)

SeRetira = cola.pop(0);
print(f'Atendido {SeRetira}')
print(cola)

SeRetira = cola.pop(0);
print(f'Atendido {SeRetira}')
print(cola)

#seguimos mostrando como recorrer un diccionario con el ciclo for
for i in seleccionArgentina:
    print(f'{i} -> {seleccionArgentina[i]}');





















