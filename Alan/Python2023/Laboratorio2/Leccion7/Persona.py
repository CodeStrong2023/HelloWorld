class Persona: #esta clase hereda de la clase object
    def __init__(self, nombre,edad):
        self.nombre = nombre
        self.edad = edad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def __str__(self): #override = sobreescribir
        return f"Persona: [Nombre: {self._nombre} Edad: {self.edad}"

class Empleado(Persona): #esta clase hereda de la clase Persona
    def __init__(self,nombre,edad,sueldo):
        super().__init__(nombre,edad)
        self.sueldo = sueldo

    @property
    def sueldo(self):
        return self._sueldo

    @sueldo.setter
    def sueldo(self,sueldo):
        self._sueldo = sueldo

    def __str__(self):
        return f"Empleado: [ Sueldo: {self.sueldo}] {super().__str__()}"

empleado1 = Empleado("Ariel",40,75000)
print(empleado1.nombre)
print(empleado1.edad)
print(empleado1.sueldo)

#Tarea: encapsular los atributos y agregar los metodos getters and setters
#crear otro objeto, pasar los datos para nombre, edad y sueldo
#mostrar estos datos, luego modificar y mostrar nuevamente

empleado2 = Empleado("Alan", 20, 50000)
print(empleado2.nombre)
print(empleado2.edad)
print(empleado2.sueldo)
empleado2 = Empleado("German",20,55000)
print(empleado2.nombre)
print(empleado2.edad)
print(empleado2.sueldo)