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
