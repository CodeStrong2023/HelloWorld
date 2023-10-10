class Persona: # Creamos una clase
    def __init__(self, nombre, apellido, edad): # Se lo llama método Init Dunder
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    def mostrar_detalle(self):
        print(f"Persona: {self.nombre} {self.apellido} {self.edad}")

persona1 = Persona("Paulina", "Generale", 14)
print(f"El objeto1 de la persona clase: {persona1.nombre} {persona1.apellido} Su edad es: {persona1.edad}")


persona2 = Persona("Francisco", "Generale", 7)
print(f"El objeto2 de la persona clase: {persona2.nombre} {persona2.apellido} Su edad es: {persona2.edad}")

persona1.nombre = "Regina"
persona1.apellido = "Carballo"
persona1.edad = 1
print(f"El objeto 1 modificado de la clase persona: {persona1.nombre} {persona1.apellido} Su edad es: {persona1.edad}")

# Los atributos son: caracteristicas
# Los métodos son: el comportamiento que van a tener los objetos (acciones)
persona1.mostrar_detalle()
persona2.mostrar_detalle()