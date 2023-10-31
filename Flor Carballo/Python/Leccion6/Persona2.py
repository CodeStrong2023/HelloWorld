class Persona2:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalles(self):
        print(f"Los datos a mostrar son los siguientes: {self._nombre} {self._apellido} {self._edad}")

    @property # Decorador
    def nombre(self): # Método Getter
        print("Estamos utilizando el método get")
        return self._nombre

    @nombre.setter
    def nombre(self, nombre): # método Setter
        print("Estamos utilizando el método set")
        self._nombre = nombre
    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
       self._edad = edad

    def __del__(self):
        print(f'Persona2: {self._nombre} {self._apellido} {self._edad}')

if __name__ == "__main__":
    persona1 = Persona2("Regina", "Carballo", 4)
    print(persona1.nombre) # Llamamos al método Getter
    persona1.nombre = "Rufina" # Llamamos el método Setter
    print(persona1.nombre) # Otra vez con el método Getter
    print(persona1.mostrar_detalles()) # Llamamos el método mostrar_detalles
    # persona1._edad = 40 # ESTÁ MUY MAL
    # Atributo read-only (sería la edad porque el método set)
    print(persona1.edad)

    # Tarea crear tres objetos más, utilizando los métodos getter and setter
    # para modificar, y mostrar los cambios con el método mostrar_detalle

    # Objeto 1 de la tarea
    persona2 = Persona2("Santi", "Rodriguez", 20)
    persona2.nombre = "Santiago"
    persona2.apellido = "Rodrigues"
    persona2.edad = 21
    print(persona2.nombre)
    print(persona2.apellido)
    print(persona2.edad)
    print(persona2.mostrar_detalles())
    # Objeto 2
    persona3 = Persona2("Facu", "Carballo", 18)
    persona3.nombre = "Facundo"
    persona3.apellido = "Carbalo"
    persona3.edad = 19
    print(persona3.nombre)
    print(persona3.apellido)
    print(persona3.edad)
    print(persona3.mostrar_detalles())

    #Objeto 3
    persona4 = Persona2("Rami", "Carballo", 15)
    persona4.nombre = "Ramiro"
    persona4.apellido = "Carbalo"
    persona4.edad = 16
    print(persona4.nombre)
    print(persona4.apellido)
    print(persona4.edad)
    print(persona4.mostrar_detalles())

    print(__name__)







