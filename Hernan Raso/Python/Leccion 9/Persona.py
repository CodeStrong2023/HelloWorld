class Persona:  # Creamos una clase
    def __init__(self, nombre, apellido, edad):  # Se lo llama metodo Init Dunder
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad}')


persona1 = Persona('Ariel', 'Betancud', 40)  # Necesitamos enviar argumentos
# print(persona1.nombre)
# print(persona1.apellido)
# (persona1.edad)

persona2 = Persona('Oscaldo', 'Giordanini', 45)
print(f'El objeto 1 de la clase persona: {persona1.nombre} {persona1.apellido} Su edad es: {persona1.edad}')
print(f'El objeto 2 de la clase persona: {persona2.nombre} {persona2.apellido} Su edad es: {persona2.edad}')

# Modificar atributos
persona1.nombre = 'Liliana'
persona1.apellido = 'Buccella'
persona1.edad = 40
print(f'El objeto 1 Modificado de la clase persona: {persona1.nombre} {persona1.apellido} Su edad es: {persona1.edad}')

# Los atributos son: Caractetiricas
# Los metodos son: el comportmiento que van a tener los objetos (Acciones)

persona1.mostrar_detalle() # La referencia en este caso se pasa de manera automatica
persona2.mostrar_detalle()

# Persona.mostrar detalle(persona1) # Debemos pasarle una referencia para el self o dara error
persona1.telefono = '4445555289'
print(f'Este es el telefono de: {persona1.nombre} {persona1.telefono}')  # Hemos creado un atributo de un objeto

# print(persona2.telefono) El objeto persona2 no tiene este atributo, da error
