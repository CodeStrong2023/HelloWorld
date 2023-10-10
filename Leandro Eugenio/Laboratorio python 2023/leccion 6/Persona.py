class Persona: #creamos una clase
    def __init__(self,nombre,apellido,edad): #se lo llama metodo init dunder
        self.nombre = nombre;
        self.apellido = apellido;
        self.edad = edad;
    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad}')

persona1 = Persona('Leandro','Eugenio',25)
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)
print(f'El objeto1 de la clase persona es: {persona1.nombre}  {persona1.apellido} su edad es {persona1.edad}')
perosna2 =Persona('Ezequiel','Perez',30)
print(f'El objeto2 de la clase persona es: {perosna2.nombre}  {perosna2.apellido} su edad es {perosna2.edad}')

persona1.nombre = 'Liliana'
persona1.apellido = 'Garcia'
persona1.edad = 30
print(f'El objeto1 de la clase persona es: {persona1.nombre}  {persona1.apellido} su edad es {persona1.edad}')

#Los atributos son: caracteristicas
#Los metodos son: el copmportamiento que vana a tenr los objetos
persona1.mostrar_detalle();
perosna2.mostrar_detalle();