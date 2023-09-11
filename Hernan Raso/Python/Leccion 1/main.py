# lista = Ariel, Liliana, Natalia, Osvaldo

nombres = ['Naty', 'Osvaldo', 'Lily', 'Artiel']
print(nombres)

# Podemos ver la ubicacion que le pidamos
print(nombres[0])
print(nombres[1])

# Si no sabemos la cantidad y queremos ver el ultimo ponemos [-1] o [-2] el ante ultimo y asi...
print(nombres[-1])

# Recuperar un rango de la lista
print(nombres[0:2])  # Solo muestra el indice 0, 1 pero no el indice 2

# ir del inicio de la lista al indice indicado (sin incluirlo)
print(nombres[ :3])

# desde el indice indicado hasta el final
print(nombres[1: ])

# Modificar un valor
nombres[2] = 'Liliana'
nombres[0] = 'Natalia'
print(nombres)

# Iterar una lista

for nombre in nombres: # nombre es singular, lña lista es plural
    print(nombre)
else:
    print('Se acabaron los elementos de la lista')

# preguntamos cuantos elementos tiene una lista

print(len(nombres))  # le pasamos como parametro la lista

# Agregamos un elemento
nombres.append('Marcelo')
print(nombres)

# Insertar un elemento en un indice especifico
nombres.insert(1,'Alberto')
print(nombres)

nombres.insert(3, 'Debora')
print(nombres)

# Eliminamos un elemnto
nombres.remove('Alberto')
print(nombres)

# Eliminar el ultinmo elemento
nombres.pop() # Elimina el ultimo de la lista
print(nombres)

# Eliminar un indice especifico
del nombres[2] # Del significa delete (eliminar)
print(nombres)

# Eliminar, borrar o limpiar todos los elementos
nombres.clear()
print(nombres)

# Eliminar la lista
# del nombres
# print(nombres)

# Definimos una tupla

cocina = ('cuchara', 'cuchillo', 'tenedor')
print(cocina)

# Ver la canridad de elementos de la tupla
print(len(cocina))

# Acceder a un elemento, para esto utilizamos corchetes no parentesis

print(cocina[0])

# Mostrar de manera inversa
print(cocina[-1])

# Acceder a un rango
print(cocina[0:2])

#ejemplo
verduras = ('papa',) # Una tupla necesita la coma, aunque se aun solo elemento, de lo contrario solo seria String

# Recorremos los elementos de la tupla

for cocinar in cocina:
    print(cocinar)  # print esta usando \n para saltos d e lineas
    print(cocinar, end=' ')  # Esto es para evitar el salto de linea

cocinarLista = list(cocina)
cocinarLista[0] = 'plato'
print(cocina)

# Esto es para eliminar la tupla
#del cocina
#print(cocina)

