class Persona2:
    def __init__(self, nombre, apellido, edad): #esta encapsulado por _
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalle(self):
        print(f"Los datos a mostrar son los siguientes: {self._nombre} {self._apellido} {self._edad}")

    @property #decorador
    def nombre(self): #metodo getter
        print("Estamos usando el metodo get")
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        print("Estamos usando el metodo set")
        self._nombre = nombre

    @property  # decorador
    def apellido(self):  # metodo getter
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property  # decorador
    def edad(self):  # metodo getter
        return self._edad

    @edad.setter                  #si el setter esta comentado, la edad pasa a ser read only
    def edad(self, edad):         #osea que no se puede modificar, solo se puede leer
        self._edad = edad

    def __del__(self):
        print(f"Persona2: {self._nombre}{self._apellido}{self._edad}")

if __name__ == "__main__":
    persona1 = Persona2("Ariel", "Betancud",41)
    print(persona1.nombre) #llamamos al metodo getter
    persona1.nombre = "Juan Pedro" #llamamos al metodo setter
    print(persona1.nombre) #otra vez llamamos al metodo getter
    print(persona1.mostrar_detalle()) #llamamos el metodo mostrar detalles
    print(persona1.edad)

    #Tarea: crear tres objetos mas, utilizando los metodos getter and setter para modificar, y los cambios
    #con el metodo mostrar_detalle

    persona2 =Persona2 ("Alan", "Garrido", 20)
    persona2.nombre = "Alan"
    persona2.apellido = "Garrido"
    persona2.edad = 20
    print(persona2.nombre)
    print(persona2.apellido)
    print(persona2.edad)
    print(persona2.mostrar_detalle())

    persona3 = Persona2 ("Bruce", "Wayne", 28)
    persona3.nombre = "Bruce"
    persona3.apellido= "Wayne"
    persona3.edad = 28
    print(persona3.nombre)
    print(persona3.apellido)
    print(persona3.edad)
    print(persona3.mostrar_detalle())

    persona4 = Persona2 ("Selina", "Kyle", 27)
    persona4.nombre = "Selina"
    persona4.apellido = "Kyle"
    persona4.edad = 28
    print(persona4.nombre)
    print(persona4.apellido)
    print(persona4.edad)
    print(persona4.mostrar_detalle())

    print(__name__)

