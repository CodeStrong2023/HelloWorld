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
