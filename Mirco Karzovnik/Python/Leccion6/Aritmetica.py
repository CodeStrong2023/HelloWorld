class Aritmetica:
    """
    El nombre de este tipo de comentario es: DoctString
    Esto es documentacion de la clase de python
    vamos a hacer en esta clase algunas operaciones de: suma , restta, multiplicaciones y mas
    """
    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB

    # metodo para sumar
    def sumar(self):
        return self.operandoA + self.operandoB
    def resta(self):
        return self.operandoA - self.operandoB
    def multiplicar(self):
        return self.operandoA * self.operandoB
    def dividir(self):
        return self.operandoA / self.operandoB

aritmerica1 = Aritmetica(7, 9)
print(aritmerica1.sumar())
print(f"La resta de los numeros es: {aritmerica1.resta()}")
print(f"fLa multiplicaciopn de los numeros es: {aritmerica1.multiplicar()}")
print(f"La divicion de los numeros es:{aritmerica1.dividir():.2f}")
