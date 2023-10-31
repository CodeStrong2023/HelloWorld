class Rectangulo:
    """
    Crear una clase llamada rectangulo, debe tener 2 atributos:altura y base
    el nombre del metodo sera calcular_area utilizando la formula
    area = base * altura, la base y altura deben ser ingresadas por el usuario
    """
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

base = float(input("Ingrese la base del rectangulo: "))
altura = float(input("Ingrese la altura del rectangulo: "))
Area = Rectangulo(base, altura)
print(f"El area es: {Area.calcular_area()}")