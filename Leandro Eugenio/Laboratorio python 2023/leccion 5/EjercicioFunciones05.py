""" 
Ejercicio 5: Convertidor de temperaturas
Realizar dos funciones para convertir de grados celcius a fhrenheit
y viseversa.
Investigar la formula
 """

def CelsiusAFahrenheit(celsius):
    calculo = celsius * 9/5 +32 
    return calculo

def FahrenheitACelsius(far):
    calculo = (far - 32) * 5/9
    return calculo

cel = float(input('Digite el valor de Celsius: '))
calculo = CelsiusAFahrenheit(cel)
print(f'{cel}º C es igual a {calculo}º Fahrenheir')

far = float(input('Digite el valor de Fahrenheit: '))
calculo = FahrenheitACelsius(far)
print(f'{far}º F es igual a {calculo}º Celsius')