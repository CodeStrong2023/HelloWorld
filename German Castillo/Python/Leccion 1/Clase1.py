'''
nombres = ['Naty','Osvaldo','Lily','Ariel']
print(nombres)
print(nombres[0])
print(nombres[1])
print(nombres[3])
print(nombres[-1])
print(nombres[-2])
'''
'''
nombres = ['Naty','Osvaldo','Lily','Ariel']
print(nombres)
## Mostraría solo la posición 0 y 1. El segundo número no se muestra.
print(nombres[0:2])
## Se va desde el inicio de la lista hasta el indicado (Sin incluirlo).
print(nombres[ :3])
## Se va desde el indice indicado hasta el final
print(nombres[1: ])
nombres[2] = 'Liliana'
nombres[0] = 'Natalia'
print(nombres)
## Iterar una lista
for nombre in nombres:
    print(nombre)
else:
    print('Se acabaron los elementos de la lista')
'''

nombres = ['Naty','Osvaldo','Lily','Ariel']

## Preguntamos cuantos elementos tiene
print(len(nombres))

## Agregamos un elemento
nombres.append('Marcelo')
print(nombres)

## Insertar un elemento en un lugar específico
nombres.insert(1,'Alberto')
print(nombres)
nombres.insert(3,'Debora')
print(nombres)

## Eliminamos un elemento
nombres.remove('Alberto')
print(nombres)

## Eliminar el último elemento
nombres.pop()
print(nombres)

## Eliminar un índice específico
del nombres[2]
print(nombres)

## Eliminar, borrar o limpiar todos los elementos
nombres.clear()
print(nombres)