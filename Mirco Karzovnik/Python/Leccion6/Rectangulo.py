class Rectangulo:
    def __init__(self, altura, base):
        self.altura = altura
        self.base = base

    def calcular_Area(self):
        return self.base * self.altura

base = int(input("Digite el numero para la base del rectangulo: "))
altura  = int(input("Digite el numero para la altura del rectangulo: "))
rectangulo1 = Rectangulo(base, altura)
print(f"fEl area del rectangulo es: {rectangulo1.calcular_Area()}")
