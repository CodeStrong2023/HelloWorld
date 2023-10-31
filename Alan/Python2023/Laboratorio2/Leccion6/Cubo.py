class Cubo:
    """
    Crear la clase cubo con los atributos, ancho, alto y profundidad, con un metodo
    calcular_volumen que tendra la formula:
    volumen = ancho * altura * profundidad
    El usuario debe ingresar los valores
    """
    def __init__(self, ancho, altura, profundidad):
        self.ancho = ancho
        self.altura = altura
        self.profundidad = profundidad

    def calcular_volumen(self):
        return self.ancho * self.altura * self.profundidad

ancho = int(input("Ingrese el valor del ancho: "))
altura = int(input("Ingrese el valor de la altura: "))
profundidad = int(input("Ingrese el valor de la profundidad: "))
Volumen = Cubo(ancho, altura, profundidad)
print(f"El volumen del cubo es: {Volumen.calcular_volumen()}")