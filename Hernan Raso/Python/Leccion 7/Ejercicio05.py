# Ejercicio 5: Convertidor de temperaturas
# Realizar dos dunciones para convertir de grados celsius a farenheit y viseversa. Investigar las formulas

# Funcion que convierte de celsius a farenheit
def celsius_farenheit(celsius):
    return celsius * 9 / 5 + 32 # La presedencia: multiplicacion, division  y suma


# Funcion que convierte de farenheit a celsius
def farenheit_celsius(farenheit):
    return (farenheit - 32) * 5 / 9 # Respetar la presedencia utilizando parentesis

celsius = float(input('Ingrese el valor de celsius: '))
resultado = celsius_farenheit(celsius)
print(f'{celsius} C a F -> {resultado:.2f}')

farenheit = float(input('Ingrese el valor de Farenheit: '))
resultado = farenheit_celsius(farenheit)
print(f'{farenheit} F a C -> {resultado:.2f}')