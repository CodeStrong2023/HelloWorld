class Cubo:
    """
    Crear la clase cubo con los atributos ancho alto y profundidad,
    con 
    un metodo calcular_volumen que tendra la formula:
    volumen = ancho * alto * profundidad
    que le usuario ingrese los valores
    """

    def __init__(self,ancho,alto,prfundidad):
        self.ancho = ancho;
        self.alto = alto;
        self.profundidad = prfundidad;

    def calcular_volumen(self):
        return self.ancho * self.alto * self.profundidad

ancho =  int(input('Digite el ancho: '))
alto = int(input('Digite el alto'))
profundidad = int(input('Digite la profundidad: '))

cubo = Cubo(ancho,alto,profundidad);
print(f'El volumen del cubo es {cubo.calcular_volumen()}')


