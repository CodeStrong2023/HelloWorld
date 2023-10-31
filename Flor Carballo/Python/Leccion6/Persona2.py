class Persona2:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalles(self):
        print(f"Los datos a mostrar son los siguientes: {self._nombre} {self._apellido} {self._edad}")

    @property # Decorador
    def nombre(self): # Método Getter
        return self._nombre

    @nombre.setter
    def nombre(self, nombre): # método Setter
        print("Estamos utilizando el método set")
        self._nombre = nombre

persona1 = Persona2("Regina", "Carballo", 4)
print(persona1.nombre()) # Llamamos al método Getter
