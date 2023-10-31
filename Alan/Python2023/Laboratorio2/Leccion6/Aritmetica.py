class Aritmetica:
    """
    El nombre de este tipo de comentario es: DocString
    esto es documentacion de la clase en python
    vamos a hacer en esta clase algunas operaciones de: suma, resta, multiplicacion y mas
    """

    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB

    # metodo para sumar
    def sumar(self):
        return self.operandoA + self.operandoB

    def resta(self):
        return self.operandoA - self.operandoB

    def multiplicacion(self):
        return self.operandoA * self.operandoB

    def division(self):
        return self.operandoA / self.operandoB


aritmetica1 = Aritmetica(7, 9)  # le pasamos los argumentos
print(f"Suma: aritmetica1.sumar()")
print(f"Resta: aritmetica1.resta()")
print(f"Multiplicacion: aritmetica1.multiplicacion()")
print(f"Division: aritmetica1.division()")
