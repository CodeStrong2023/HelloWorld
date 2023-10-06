# Comenzamos con Funciones

# Definimos una función
def mi_funcion():
    print("Saludos al profesor de la tecnicatura")

mi_funcion()
mi_funcion()
mi_funcion()

# Desempaquetado de listas o list Unpacking
def show(name, lastName):
    print(name+" "+lastName)
person = ["Flor", "Carballo"]
show(person[0], person[1])
show(*person)
person2 = ("Rufina", "Carballo")
show(*person2)
person3 = {"lastName": "Carballo", "name": "Regina"}
show(**person3)

numbers = [1, 2, 3, 4, 5]
for n in numbers:
    print(n)
    if n == 3:
        break
else:
    print("Esto se termino")

# List Comprehension: Lista de Comprensión
names = ["Porge", "Veronica", "Facundo", "Pamiro"]
alongP = [p for p in names if p[0] == "P"]
print(alongP)

bottleC = [{"name": "Quilmes", "country": "Arg"},
           {"name": "Corona", "country": "Mx"},
           {"name": "Stella Artois", "country": "Belgium"},
          ]
Arg = [b for b in bottleC if b ["country"] == "Arg"]
print(Arg)
print(bottleC)

# Paso de Argumentos (funciones)
def mi_funcion2(name, lastName):
    print("Saludo al profesor y tutores")
    print(f"Nombre: {name}, Apellido: {lastName}")
mi_funcion2("Regina", "Carballo")
mi_funcion2("Flor", "Carballo")
mi_funcion2("Rufina", "Carballo")

# La palabra return en funciones
# Creamos una función para sumar
def sumar(a,b):
    return a + b
# resultado = sumar(78, 22)
# print(f"El resultado de la suma es: {resultado}")
print(f"El resulado de la suma es: {sumar(55, 45)}")

def sumar2(a = 0, b = 0):
    return a + b
resultado = sumar2()
print(f"Resultado de la suma: {resultado}")
print(f"Resultado de la suma: {sumar2(22, 66)}")

# Argumentos, variables en funciones
def listarNombres(*nombres):
    for nombre in nombres:
        print(nombre)
listarNombres("Flor", "Regi", "Rufi", "Santi")
listarNombres("Jorge", "Vero", "Facu", "Rami", "Nere", "Pauli")

def listarTerminos(**terminos): #Lo mas utilizado es **kwargs para recibir los argumentos
    for llave, valor in terminos.items():
        print(f"{llave} : {valor}")

listarTerminos() # No recibe nada, nada se va a mostrar
listarTerminos(IDE="Integrated Develoment Enviroment", PK="Primaruy Key")
listarTerminos(Nombre="Lionel Messi")

def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)
nombres2= ["Tito", "Pedro", "Carlos"]
desplegarNombres(nombres2)
desplegarNombres("Carla")
# desplegarNombres(10) # No es un objeto iterable
desplegarNombres((10, 11)) # La convertimos a una tupla
desplegarNombres([22, 55]) # La convertimos en una lista

# Funciones Recursivas
def factorial(numero):
    if numero == 1: # Caso Base
        return 1
    else:
        return numero * factorial(numero-1) # Caso Recursivo

resultado = factorial(5) # Lo hacemos en código duro
print(f"El factorial del número 5 es: {resultado}") # Tarea que el usuario ingrese el número para calcular el factorial

# TAREA
def calcular_factorial(numero):
    factorial = 1
    if numero < 0:
        return "No se puede calcular el factorial de un número negativo"
    elif numero == 0:
        return "El factorial de 0 es 1"
    else:
        for i in range(1, numero + 1):
            factorial *= i
        return f"El factorial de {numero} es {factorial}"

while True:
    numero_str = input("Ingresa un número para calcular su factorial: ")
    if numero_str.isdigit():
        numero = int(numero_str)
        resultado2 = calcular_factorial(numero)
        print(resultado2)
        break
    else:
        print("ERROR. Ingrese un número entero válido")