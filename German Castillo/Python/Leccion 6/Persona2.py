class Persona2:

    def __init__(self,nombre,apellido, edad) :
        self._nombre= nombre
        self._apellido = apellido
        self._edad = edad
    def mostrar_detalle(self):
        print(f'Los datos a mostrar son: {self._nombre}, {self._apellido}, {self._edad}')

    @property #Decorador
    def nombre(self): #metodo Getter
        print('Estamos mostrando el metodo get')
        return self._nombre
    
    @nombre.setter
    def nombre(self,nombre): #Metodo Setter
        print('Estamos mostrando el metodo set')
        self._nombre = nombre

    @property
    def apellido(self):
        print('Estamos mostrando el metodo get')
        return self._apellido;

    @apellido.setter
    def apellido(self,apellido):
        print('Estamos mostrando el metodo set')
        self._apellido = apellido;

    @property
    def edad(self):
        print('Estamos mostrando el metodo get')
        return self._edad
    
    @edad.setter
    def edad(self,edad):
        print('Estamos mostrando el metodo set')
        self._edad = edad;
    def __del__(self):
        print(f'Persona2: {self._nombre}{self._apellido} {self.edad}')

if __name__ == '__main__':
    persona1 =  Persona2('German','Castillo',19)
    print(persona1.nombre) #Llamamos al metodo gettter
    persona1.mostrar_detalle();
    persona1.nombre = 'Andres'
    print(persona1.nombre)
    print(persona1.mostrar_detalle())
    persona1.edad = 54
    #Atributo read-only seria la edad porque no tiene un metodo set
    print(persona1.edad)

    #Tarea :Crear tres objetos mas utilizando los metodos getter and setters
    #para modificar , y mostrar los cambios

    persona2 = Persona2('Mario','Vega',18)
    persona2.nombre = 'Fernanda'
    persona2.apellido = 'Lopez'
    persona2.edad = 20
    print(persona2.mostrar_detalle())

    persona3 = Persona2('Esteban','Hernandez',44)
    persona3.nombre = 'Maria'
    persona3.apellido = 'Gomez'
    persona3.edad = 32
    print(persona3.mostrar_detalle())

    persona4 = Persona2('Paola','Martinez',57)
    persona4.nombre = 'Manolo'
    persona4.apellido = 'Guerrero'
    persona4.edad = 70
    print(persona4.mostrar_detalle())

    print(__name__)