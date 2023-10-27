# La palabra return en funciones
# Creamos una funcion para sumar

def sumar(a, b):
    return a + b
#  resultado = sumar(78, 22)
# print(f'El resultado de la suma es: {resultado}')
print(f'El resultado de la suma es: {sumar(55, 45)}') # Aca vemos que podemos llamar directamente a la funcion

# Valores por default en una funcion

def sumar2(a = 0, b = 0):  # Le damos un valor por default
    return a + b
resultado = sumar2()
print(f'Resultado de la suma {resultado}')
print(f'Resultado de la suma: {sumar2(22, 66)}')

# Argumentos, Variables en funciones
def listarNombres(*nombres):  # Normalmente se utiliza: *args
    for nombre in nombres: # Se va a convertir en una tupla
        print(nombre)
listarNombres('Lucas', 'Jose', 'Claudia', 'Rosa', 'Maria')
listarNombres('Marcos', 'Daniel', 'Romina', 'Pepe', 'Marcela', 'Carlos')


