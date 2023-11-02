class Persona: # Creamos una clase
    def __init__(self, nombre, apellido, edad, *args, **kwargs):
        self.nombre = "Mirco"
        self.apellido = "Karzovnik"
        self.edad = 22
        self.args = args
        self.kwargs = kwargs
    def mostrar_detalle(self):
        print(f"Persona: {self.nombre} {self.apellido} {self.edad}, la direccion es: {self.args}, los datos importantes son: {self.kwargs}")

persona1 = Persona("Nashe", "Bent", 30)
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)

persona2 = Persona("Betania", "Lopez", 44)
print(f"El objeto2 de la clase persona: {persona2.nombre} {persona2.apellido} Su edad es: {persona2.edad}")

persona1.nombre = "Lili"
persona1.apellido = "Core"
persona1.edad  = 44
print(f"El objeto2 de la clase persona: {persona1.nombre} {persona1.apellido} Su edad es: {persona1.edad}")


# Los atributos son: caracteristicas
# los metodos son: el comportamiento que van a tener los objetos (acciones)
persona1.mostrar_detalle() # La referencia se pasa de manera automatica
persona2.mostrar_detalle()

persona1.telefono = "444445213"
print(f"Este es el telefono: {persona1.nombre} {persona1.telefono}")

persona3 = Persona("Rogelio", "Romero", 22, "Telefono", "235243", "Calle lopez", 823,"Manzana", 11, "Casa", 18, Altura=1.70, Peso= 90, CFavorito="Azul", Auto="Citroen", Modelo= 2003)
persona3.mostrar_detalle()
