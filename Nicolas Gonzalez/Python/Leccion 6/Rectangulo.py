class Rectangulo:
    """
    La clase llamada rectangfulo , debe tener dos atributos: altura y bas
    el nombre del metodo sera calcular area utilizando la formula:
    area= base * altura. pero la base y la altura deben ser ingresadas por el usuario
    """
    def __init__(self,altura, base):
        self.altura = altura;
        self.base = base;

    def calcular_area(self):
        return self.base * self.altura
    
base = int(input('Digite la base'))        
altura = int(input('Digite la altura'))
rectangulo = Rectangulo(altura,base);
print(f'El area del rctangulo es: {rectangulo.calcular_area()}')
