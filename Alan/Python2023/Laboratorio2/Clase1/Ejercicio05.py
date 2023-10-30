#Ejercicio 5: factorial de un numero positivo
#hacer un programa para calcular el factorial de un numero positivo
numero = int(input("Digite un numero: "))
while numero < 0: #mientras el numero sea negativo
    print("Error -> el numero ingresado no es positivo")
    numero = int(input("Digite un numero: "))
factorial = 1 #la variable para calcular el factorial
for i in range(1, numero+1):
    factorial*=i
print(f"El factorial del numero {numero} positivo ingresado es: {factorial}")