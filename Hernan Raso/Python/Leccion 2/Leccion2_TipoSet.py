# Tipo set
planetas = {'Marte', 'Júpiter', 'Venus'}
print(len(planetas)) # Usamos la funcion len = length significa largo

# Revisar si un elemento existe dentro de set

print('Júpiter' in planetas)  # Es importante respetar la misma escritura (Mayusculas, minusculas, acentos etc)


# Revisar si un elemento no existe dentro de set
print('Júpiter' not in planetas)

# Agregar un elemento
planetas.add('Tierra') # add es una funcion (No admite duplicados, no se van agregar)
print(planetas)

# Eliminar elementos, puede arrojar un error si el elemento no existe
planetas.remove('Júpiter') # Esta funcion ante un mal ingreso u inexistencia del elemento da error
print(planetas)

planetas.discard('Tierra') # Esta funcion no nos presenta ningun error
print(planetas)

# Limpiar ser
planetas.clear()
print(planetas)

# Eliminar set o conjunto
# del planetas
# print(planetas)

