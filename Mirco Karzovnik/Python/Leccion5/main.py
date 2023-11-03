# Comennzamos con funciones

# Definimos una funcion
def mi_funcion():
    print("Buenaaas")
mi_funcion()
mi_funcion() # Se puede llamar una funcion N cantidad de veces

# Desempaquetado de listas o list Unpacking
def show(name, lastName):
    print(name+" "+lastName)
person = ["Mirco", "Karzovnik"]
show(person[0], person[1]) # pasamos uno por uno los datos de lista a la funcion
show(*person)
person2 = ("Trinidad", "Mori")
show(*person2)

numbers = [1, 2, 3, 4, 5]
for n in numbers:
    print(n)
    if n == 2:
        break
else:
    print("Esto se termina")

# list comprension , lista de comprension
names = ["Paolo", "Rodigro", "Lupe", "Pepe"]
alongP = [p for p in names if p[0] == "P"] # esto regresa una nueva lista
print(alongP)
bottleC = [ {"name": "Quielmes", "country": "Arg"},
           {"name": "Corona", "country": "Mx"},
           {"name": "Stella Artois", "country": "BEL"}
           ]
Arg = [b for  b in bottleC if b["country"] == "Arg"]
print(Arg)
print(bottleC)

# Paso de argumentos (funciones)
def mi_funcion2(name, lastName):
    print("Saludos a todos ahre que solo soy yo")
    print(f"Nombre: {name}, Apellido: {lastName}")
mi_funcion2("Mirco", "Karzovnik")
mi_funcion2("Nashe", "Karzovnik")
mi_funcion2("KUKA", "Karzovnik")

# La palabra return en funciones
# Creamos una funcion para sumar
def sumar(a, b):
    return a + b
# resultado = sumar(78,22)
# print(f"El resultado de la suma es: {resultado}")
print(f"El resultado de la suma es: {sumar(55,45)}")

def sumar2(a = 0, b = 0): # le damos un valor por df
    return a + b
resultado = sumar2()
print(f"Resultado de la suma: {resultado}")
print(f"Resultado de la suma: {sumar2(22,66)}")

# Argumentos, variables en funciones
def listarNombres(*nombres):
    for nombre in nombres:
        print(nombre)
listarNombres("Lucas", "Jose", "Eduardo")
listarNombres("keseyo", "Nashe", "Cuca")

def listarTerminos(nombre, *nombres, **terminos):
    for llave, valor in terminos.items():
        print(f"{llave} : {valor}")

listarTerminos()
listarTerminos(IDE="Integrated Devolment Enviroment", PK="Primaruy Key")
listarTerminos(Nombre="Leonel Messi")

def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombres)
nombres2 = ["Tito", "Pedro", "Carlos"]
desplegarNombres(nombres2)
desplegarNombres("Carla")

desplegarNombres((10, 11))
desplegarNombres([22, 55])

# Funciones recursivas
def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero-1)
numeroFactorial = int(input("Digite el numero para calcular el factorial: "))
resultado = factorial(numeroFactorial)
print(f"El factorial del numero  {numeroFactorial} es: {resultado}")



