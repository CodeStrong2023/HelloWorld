class Vehiculo:
    """
    Definir una clase padre llamada vehiculo y dos clases hijas
    llamadas auto y bicicleta, las cuales heredan de la clase padre
    vehiculo. la clase padre debe tener los siguientes atributos
    y metodos:

    Vehiculo (clase padre)
    -Atributos(color, ruedas)
    -metodos(__init__(color, ruedas) y __str__())

    Auto (clase hija de Vehiculo)
    -atributos (velocidad (km/hr))
    -metodos (__init__(color, ruedas, velocidad) y __str__())

    Bicicleta (clase hija de Vehiculo)
    -atributos (tipo(urbana/montaña/etc))
    -metodos (__init_(color, ruedas, tipo) y __str__())

    crear un objeto en cada clase
    """

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "Color: "+self.color+" Ruedas: "+ str(self.ruedas)

class Auto(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return super().__str__()+", Velocidad(km/hr): "+ str(self.velocidad)

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return super().__str__()+", Tipo: "+ self.tipo

#Primer objeto de la clase padre Vehiculo
vehiculo = Vehiculo("blanco /", 4)
print(vehiculo)

#Segundo objeto, clase hija Auto
auto = Auto("rojo", 4, 200)
print(auto)

#Tercer objeto, clase hija Bicicleta
bicileta = Bicicleta("negro", 2, "Mountain bike")
print(bicileta)
