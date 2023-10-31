class Persona: #creamos una clase
    #pass #no se procesa nada mas (no tiene contenido)
    def __init__(self, nombre, apellido, dni,edad, *args, **kwargs): #metodo init dunder
        self.nombre = nombre
        self.apellido = apellido
        self._dni = dni #estr atributo esta encapsulado de una manera sugerida
        self.edad = edad
        self.args = args
        self.kwargs = kwargs
    def mostrar_detalle(self): #self es igual a this (de java)
        print(f"La clase Persona tiene los siguientes datos: {self.nombre}, {self.apellido}, {self._dni},{self.edad}, la direccion es: {self.args}, los datos importantes son: {self.kwargs}")
        #para llamar atributos dentro de un metodo a otro, se usa la variable self(se usa en los metodos)


persona1 = Persona("Ariel", "Betancud", 32456987, 40) #necesitamos enviar argumentos
print(f"El objeto1 de la clase persona: nombre: {persona1.nombre}, apellido: {persona1.apellido}, edad: {persona1.edad}")

persona2 = Persona("Osvaldo", "Giordanini", 30321456,45)
print(f"El objeto2 de la clase persona: nombre: {persona2.nombre}, apellido: {persona2.apellido}, edad: {persona2.edad}")

persona1.nombre = "Liliana"
persona1.apellido = "Buccella"
persona1.edad = 40
print(f"El objeto1 modificado de la clase persona: nombre: {persona1.nombre}, apellido: {persona1.apellido}, edad: {persona1.edad}")

#los atributos son: caracteristicas para nuestros objetos (persona1, persona2)
#los metodos son: comportamientos que van a tener nuestros objetos (acciones)
#un metodo es igual que una funcion, la unica diferencia es que metodo esta asociado
#con una clase
persona1.mostrar_detalle() #la referencia en este caso se pasa de manera automatica
persona2.mostrar_detalle() #porque llamamos al objeto directamente

#Persona.mostrar_detalle(persona1) #en este caso tenemos que poner la referencia porque se llama a la clase
persona1.telefono = "44445555289"
print(f"Este es el numero de {persona1.nombre}: {persona1.telefono}") #creamos un atribut de un objeto

#print(persona2.objeto)#el objeto persona2 no tiene este atributo, da error

persona3 = Persona("Rogelio", "Romero", 35446685,22, "Telefono", "2614445557", "Calle Lopez", 823, "Manzana", 77, "casa", 18, altura=1.83, peso=105, Cfavorito= "Azul", auto= "Citroen", modelo=2021)
persona3.mostrar_detalle()
#print(persona3._dni) #esto no debe usarse en python, no es comun usarlo, aunque se puede.
#persona3.__nombre #esta totalmente encapsulado con __, no se muestra, tampoco acepta ningun cambio de valor