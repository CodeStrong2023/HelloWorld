def celsius_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

celsius= float(input("Ingrece los grados Celsius: "))
resultado = celsius_fahrenheit(celsius)
print(f"{celsius} C° a F° -> {resultado}")

fahrenheit = float(input("Ingrese los grados Fahrenheit: "))
resultado= fahrenheit_celsius(fahrenheit)
print(f"{fahrenheit} F° a C° -> {resultado}")