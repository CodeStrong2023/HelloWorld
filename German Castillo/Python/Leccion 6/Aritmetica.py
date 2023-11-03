class Aritmetica:
    """ 
    El nombre de este tipo de comentarios es: DocString
    esto es documentacion de la clase python
    vamos a hacer en esta clase algunas operacion de: suma,resta,multiplicaion y mas
    """
    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA;
        self.operandoB = operandoB;
    #Metodo apra sumar
    def sumar(self):
        return self.operandoA + self.operandoB
    
    def resta(self):
        return self.operandoA - self.operandoB
    
    def multiplicar(self):
        return self.operandoA * self.operandoB
    
    def dividir(self):
        return self.operandoA / self.operandoB

aritmetica1 = Aritmetica(7,9) #Le pasamamos los argumentos para los operandos
print(aritmetica1.sumar())
print(f'la resta de los numeros es: {aritmetica1.resta()}')
print(f'la multiplicaion de los numeros es: {aritmetica1.multiplicar()}')
print(f'la division de los numeros es: {aritmetica1.dividir():.2f}') #2.f es para que solo se muestren dos numeros despues de la coma
        
        
    