## Definimos una tupla
cocina = ('cuchara','cuchillo','tenedor')
print(len(cocina))

## Acceder a un elemento, para esto utilizamos corchetes no paréntesis.
print(cocina[0])
## Mostrar de manera inversa
print(cocina[-1])

## Acceder a un rango
print(cocina[0:2])

## Recorremos los elementos de la Tupla
for cocinar in cocina:
    print(cocinar, end=' ') ## end= hace que no se saltee la línea al utilizar la función print

cocinaLista = list(cocina)
cocinaLista[0] = 'Plato'
cocina = tuple(cocinaLista)
print('\n', cocina)

#del cocina Esto sirve para borrar una tupla