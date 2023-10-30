#Ejercicio 04: calculadora de impuestos
#crear una funcion para calcular el total de un pago incluyendo un impuesto aplicado (IVA)
#Formula: pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
#proporcione el pago sin impuesto: 1000
#proporcione el monto del impuesto: 21%
#pago con impuesto: xxxxx

def calcular_pago_total(pago_sin_impuesto, impuesto):
    pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto / 100)
    return pago_total

pago_sin_impuesto = int(input("Ingrese el precio base del producto: "))
impuesto = int(input("Ingrese el impuesto: "))
pago_con_impuesto = calcular_pago_total(pago_sin_impuesto,impuesto)
print(f"El pago con impuesto es: {pago_con_impuesto}")