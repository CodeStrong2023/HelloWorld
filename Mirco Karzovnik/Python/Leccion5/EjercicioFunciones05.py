# Ejercicio 5: Convertidor de temperaturas
# Realizar dos funciones para convertir de grados a celsius
# a fahrenheit a viseversa.

# Inverstigar las formulas

# Funcion que convierte de celsius a fahrenheit
def celsius_fahrenheit(celsius):
    return celsius * 9 / 5 + 32
# Funcionm que convierte  de fahrenheit a celsius
def fahrenheit_Celsius(fahrenhet):
    return (fahrenhet- 32) * 5 / 9

celsius = float(input("Digite el valor de celsius: "))
resultado = celsius_fahrenheit(celsius)
print(f"{celsius} C A F -> {resultado:.2f}")

fahrenheit = float(input("Dogote eñ vañpr de fahrenheit: "))
resultado = fahrenheit_Celsius(fahrenheit)
print(f"{fahrenheit} F a C ->  {resultado:.2f}")
