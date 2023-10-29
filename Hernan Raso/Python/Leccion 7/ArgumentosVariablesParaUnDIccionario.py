# Argumentos Variables para un diccionario

# Definimos la funcion

def listarTerminos(**terminos): # Lo mas utilizado es **kwargs para recibir los aegumentos
    for llave, valor in terminos.items():  # kwargs significa: Key word arguments
        print(f'{llave} : {valor}')

listarTerminos()  # No ricibe nada, nada se va a mostrar
listarTerminos(IDE='Integrated Develoment Enviroment', pk='Primaruy Key')
listarTerminos(Nombre='Leones Messi')
listarTerminos()

def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)
nombres2 = ['Tito', 'Pedro', 'Carlos']
desplegarNombres(nombres2)
desplegarNombres('Carla')
# desplegarNombres(10) # No es un objeto iteable
desplegarNombres((10, 11))  # La convertimos a una tupla para poder recorrerlo, en un solo elemento no olvidar la coma
desplegarNombres([22, 55])  # Lo convertimos en una lista

# Funciones Recursivas
def factorial(numero):
    if numero == 1:  # Caso Base
        return 1
    else:
        return numero * factorial(numero-1)  # Caso recursivo

resultado = factorial(5)  # Lo hacemos en codigo duro
print(f'El Factorial del numero 5 es: {resultado}')

# Tarea que el usuario ingrese el numero para calcular el factorial

numeroFactor = int(input("Ingrese el numero que desea calcular el Factorial: "))
def factorial(numero):
    if numero == 1:  # Caso Base
        return 1
    else:
        return numero * factorial(numero-1)  # Caso recursivo


resultado = factorial(numeroFactor)  # Lo hacemos en codigo duro
print(f'El Factorial de {numeroFactor} es: {resultado}')

