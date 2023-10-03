#Comezamos con funciones

#Definimos una funcion
def mi_funcion():
    print("Saludo a todos los alumnos de la tecniucatura")

mi_funcion() #INVOCAMOS A ALA FUNCION

mi_funcion(); #SE PUEDE LLAMR N CANTIDAD DE VECES

#Desempaquetado de listas o list unpacking
def show(name, lastName):
    print(name+' '+lastName)
person = ["Leandro","Eugenio"];
show(person[0],person[1]) #pasmaos uno por uno los datos a la lista a la funcion
show(*person)
person2 = ("Osvaldo", "Giordanini") #Desempaquetamos a travez de una tupla
show(*person2)
person3 = {"lastName": "Lucero", "name": "Natalia" }
show(**person3)

numbers = [1,2,3,4,5]
for n in numbers:
    print(n)
    #break es la unica manera para que no se ejecute el else
else:
    print('Esto se termina')

# List comprehension, lista de comprension
names = ["Paolo","Rodrigo", "Lupe", "Pepe"]
alongP = [p for p in names if p[0] == 'P'] #Esto regresa una nueva lista
print(alongP)

bottleC = [{"name": "Quilmes", "country": "Arg"},
           {"name": "Corona", "country": "Mx"},
           {"name": "Stella Artois", "country": "Belgium"}]

Arg = [b for b in bottleC if b["country"] == "Arg"]
print(bottleC)
print(Arg)

#Paso de argumentos (funciones)
def mi_funcion2(name, lastName):
    print("Saludos para todos")
    print(f'Nombre: {name}, Apellido: {lastName}')

mi_funcion2('Jorge','Lucero')
mi_funcion2('Leandro','Eugenio')
mi_funcion2('Lucas','Perez')

#La palabra return en funciones
#Creamos funcion para sumar
def sumar(a ,b):
    return a + b
#resultado = sumar(78, 22);
#print(f'el resultado de la suma es: {resultado}')
print(f'El resultado de la suma es: {sumar(55,45)}')


def sumar2(a=0, b=0): #Le damos un valor por default
    return a + b;
resultado = sumar2()
print(f'Resultado de la suma: {resultado}') 
print(f'Resultado de la suma: {sumar2(22,66)}')


#Argumentos, variables en funciones
def listaNombres(*nombres): #normalmente se utiliza: *args
    for nombre in nombres: #se convierte en una tupla
        print(nombre)
listaNombres('lucas','ramon','jose','nicolas','maria')
listaNombres('estela','romina','carlos')

def listarTerminos(**terminos): #lo mas utilizado es **kwargs para recibir los argumentos
    for llave, valor in terminos.items(): #kwargs significa key word argument
        print(f'{llave}:{valor}')
    
listarTerminos() #no recibe nada, nada se va a mostrar   
listarTerminos(IDE='Integrated Develoment Enviroment',PK='Primary Key')
listarTerminos(Nombre='Lionel Messi')

def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)
nombres2 = ['Tito','Pedro','Carlos']
desplegarNombres(nombres2)
desplegarNombres('Carlos')
#desplegarNombres(10,11) # No es un objeto iterable
desplegarNombres((10,11)) #lo convertimos en una tupla

# Funciones recursivas
def factorial(numero):
    if numero == 1: #caso base
        return 1
    else:
        return numero * factorial(numero-1) #Caso recursivo

resultado = factorial(5); #lo hacemos en codigo duro    
print(f'el factorial del numero 5 es: {resultado}') 
#Tarea que el usuario ingrese el numero para calcular el factorial

resultado = factorial(int(input("Digite un unmero: ")))
print(f'el resultado del factorial es {resultado}')