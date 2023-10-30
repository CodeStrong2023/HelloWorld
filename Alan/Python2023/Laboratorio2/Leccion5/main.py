#comenzamos con funciones
#mi_funccion() #no se puede llamar antes de definir una funcion
#definimos una funcion
def mi_funccion(): #para identificar a la funcion utilizamos parentesis
    print("saludos a todos los alumnos de la tecnicatura")

mi_funccion() #estamos llamando a la funcion
mi_funccion() #se puede llamar muchas veces a una funcion

#desempaquetado de listas o list unpacking
def show (Name, Lastname):
    print(Name+" "+Lastname)
person = ["Ariel", "Betancud"]
show(person[0], person[1])
show(*person)
person2 = ("Osvaldo", "Giordanini")
show(*person2)
person3 = {"Lastname": "Lucero", "Name":"Natalia"}
show(**person3)

numbers = [1,2,3,4,5,] #aun con la lista vacia se va a ejecutar el else
for n in numbers:
    print(n)
    if n == 3:
        break #esta es la unica forma de que el else no se ejecute
else:
    print("esto se termino")

#list comprehension, lista de comprension
names = ["Paolo", "Rodrigo", "Lupe","Pepe"]
alongP = [p for p in names if p[0] == "P"] #esto regresa una nueva lista
print(alongP)

bottleC = [{"Name":"Quilmes", "Country": "Arg"},
            {"Name":"Corona", "Country": "Mx"},
            {"Name":"Stella Artois", "Country": "Belgium"},
            ]

Arg = [b for b in bottleC if b["Country"] == "Arg"]
print(Arg)
print(bottleC)

#paso de argumentos (funciones
def mi_funcion2(Name,Lastname):
    print("Saludos a todos los que me ven a traves del canal de YT")
    print(f"Nombre: {Name}, Apellido: {Lastname}")
mi_funcion2("Jorge","Lucero")
mi_funcion2("Analia","Pedrosa")

#palabra return en funciones
#creamos una funcion para sumar
def sumar (a,b):
    return a+b
# resultado = sumar(78,22)
# print(f"El resultado es: {resultado}")
print(f"El resultado es: {sumar(78,22)}") #esto es mas eficiente

#valores por default en una funcion
def sumar2(a = 0,b = 0): #le damos valor para que no de error
    return a+b
resultado = sumar2()
print(f"El resutado es: {sumar2()}")

#argumentos, variables en funciones
def listaNombres(*nombres): #normalmente se utiliza *args
    for nombre in nombres: #se convierte en tupla
        print(nombre)
listaNombres("Lucas", "Jose", "Claudia", "Rosa", "Maria")
listaNombres("Marcos","Daniel", "Pepe", "Romina")
