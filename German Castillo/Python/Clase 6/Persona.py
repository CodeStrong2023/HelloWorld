class Persona: #creamos una clase
    def __init__(self,nombre,apellido,dni,edad, *args, **kwargs ): #se lo llama metodo init dunder
        self.nombre = nombre;
        self.apellido = apellido;
        self._dni = dni #Este atributo esta encapsuladod e una amnera sugerida
        self.edad = edad;
        self.args = args
        self.kwargs = kwargs

    def mostrar_detalle(self):
        print(f'La clase Persona tiene los siguientes datos: {self.nombre} {self.apellido} {self._dni} {self.edad},la direccion es:  {self.args}, los datos importantes son:  {self.kwargs}') 

persona1 = Persona('German','Castillo',46061358,18)
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)
print(f'El objeto1 de la clase persona es: {persona1.nombre}  {persona1.apellido} su edad es {persona1.edad}')
perosna2 =Persona('Pedro','Martinez',12786214,31)
print(f'El objeto2 de la clase persona es: {perosna2.nombre}  {perosna2.apellido} su edad es {perosna2.edad}')

persona1.nombre = 'Carina'
persona1.apellido = 'Carrion'
persona1.edad = 52
print(f'El objeto1 de la clase persona es: {persona1.nombre}  {persona1.apellido} su edad es {persona1.edad}')

#Los atributos son: caracteristicas
#Los metodos son: el copmportamiento que vana a tenr los objetos
persona1.mostrar_detalle(); #la referencia en este caso se pasa de manerta automatica
perosna2.mostrar_detalle(); 

Persona.mostrar_detalle(persona1);
#Persona.mostrar_detalle(); debemos pasarle una referencia o dara error

persona1.telefono = 2604530553;
print(f'Este es el telefono de {persona1.nombre} : {persona1.telefono}'); #hemos creado un atributo de un objeto

persona3 = Persona('German','Castillo',46061358,18,'Telefono','2604530553','El Vencedor', 2171, 'Banana',77,Altrura=1.72,peso=60,Cfavorito='Azul',Auto='VW',Modelo=2017)
persona3.mostrar_detalle();

#print(persona3._dni) #Esto no se debe utilizar en python(esta encapsulado),sto dice que lo desconocemos
