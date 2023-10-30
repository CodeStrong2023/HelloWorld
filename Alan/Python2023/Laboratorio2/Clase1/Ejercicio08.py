#Ejercicio 8: menu interactivo - cajero automatico
#hacer un programa que simule un cajero automatico con un saldo inicial de 1000 y que tenga opciones en el menu:
# "1- Ingresar dinero en la cuenta"
# "2- Retirar dinero de la cuenta"
# "3- Mostrar dinero disponible"
#  "4- Salir"

saldo = 1000
while True:
    print("Menu")
    print("1- Ingresar dinero en la cuenta")
    print("2- Retirar dinero de la cuenta")
    print("3- Mostrar dinero disponible")
    print("4- Salir")
    opcion = int(input("Digite el numero de la opcion: "))
    if opcion ==1:
        extra = float(input("Cuanto dinero desea ingresar: "))
        saldo += extra
        print(f"Dinero en la cuenta al momento: {saldo}")
    elif opcion == 2:
        retirar = float(input("Cuanto dinero desea retirar"))
        saldo -= retirar
        print(f"Dinero actual en la cuenta: {saldo}")
    elif opcion == 3:
        print(f"Dinero disponible: {saldo}")
    elif opcion == 4:
        print("Saliendo....")
        break
    else:
        print("El numero de la opcion ingresada es incorrecto, ingreselo nuevamente")
