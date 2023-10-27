""" 
Ejercicio 2: Calculadora de Impuestos
Crear una funcion para calcular el total de un pago incluyendo
un impuesto aplicado. (IVA)
formula: pago_total = pago_sin_impuesto + pago_sin_impuesto +(impuesto/100)
Proporcione el pago sin impuesto: 1000
Proporcione el monto del impuesto : 21 %
Pago con impuesto : xxxxxx
 """



def calculoImpuesto(pago,impuesto):
    pagoTotal = pago + pago *(impuesto/100)
    return pagoTotal

calculandoImpuesto = calculoImpuesto(float(input('Digite el pago sin impuesto: ')),
                                     float(input('Digite el monto del impuesto a aplicar')))

print(calculandoImpuesto)