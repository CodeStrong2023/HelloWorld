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

persona1.mostrar_detalle()
persona2.mostrar_detalle()