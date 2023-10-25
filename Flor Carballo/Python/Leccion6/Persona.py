class Persona: # Creamos una clase
    def __init__(self, nombre, apellido, edad, *args, **kwargs): # Se lo llama método Init Dunder
        self.__nombre = nombre
        self.apellido = apellido
        self._dni = dni # Este atributos esta encapsulado de una manera sugerida
        self.edad = edad
        self.args = args
        self.kwargs = kwargs

    def mostrar_detalle(self): # self es igual a this
        print(f"La clase Persona tiene los siguientes datos: {self.__nombre} {self.apellido} {self._dni} {self.edad}, la dirección es: {self.args}, los datos importantes son: {self.kwargs}")

persona1 = Persona("Paulina", "Generale", 48237655, 14)
print(f"El objeto1 de la persona clase: {persona1.nombre} {persona1.apellido} Su edad es: {persona1.edad}")


persona2 = Persona("Francisco", "Generale", 44765487, 7)
print(f"El objeto2 de la persona clase: {persona2.nombre} {persona2.apellido} Su edad es: {persona2.edad}")

persona1.nombre = "Regina"
persona1.apellido = "Carballo"
persona1.edad = 1
print(f"El objeto 1 modificado de la clase persona: {persona1.nombre} {persona1.apellido} Su edad es: {persona1.edad}")

# Los atributos son: caracteristicas
# Los métodos son: el comportamiento que van a tener los objetos (acciones)
persona1.mostrar_detalle() # La referencia en este caso se pasa de manera automática
persona2.mostrar_detalle()

# Persona.mostrar_detalle() # Debemos pasarle una referencia para el self o dará error
persona1.telefono = "2604048615"
print(f"Este es el telefono: {persona1.nombre} {persona1.telefono}") # Hemos creado un atributo de un objeto

# print(persona2.telefono) el objeto persona2 no tiene este atributo, da error
persona3 = Persona("Rogelio", "Romero",27563854, 22, "Teléfono", "395746266", "Calle Lopez", 874, "Manzana", 8, Altura= 1.89, Peso=90, CFavorito="Azul", Auto="Citroen", Modelo=2023)
persona3.mostrar_detalle()
# print(persona3._dni) # esto no se debe utilizar (esta encapsulado), esto dice que lo desconocemos
# print(persona.3__nombre) # esta totalmente encapsulado