# Ejercicio 8: Menu interactivo - Cajero automatico
# Hacer un programa que simule un cajero automatico con un saldo inicia de $ 1000 y tendra el siguiente
# menu de opciones:
#                          1. Ingresar dinero en la cuenta
#                          2. Retirar Dinero de la cuenta
#                          3. Mostrar dinero disponible
#                          4. Salir

saldo = 1000
while True:
    print("\t.:MENU:.")
    print("1. Ingresar dinero en la cuenta")
    print("2. Retirar Dinero de la cuenta")
    print("3. Mostrar dinero disponible")
    print("4. Salir")
    opcion = int(input("Digite una opcion de Menu: "))
    print()
    if opcion == 1:
        extra = float(input("Cuanto dinero desea Ingresar -> "))
        saldo += extra
        print(f"Dinero en la cuenta al momento: ${saldo}")
    elif opcion == 2:
        retirar = float(input("Cuanto dinero desea retirar -> "))
        if retirar > saldo:
            print(f"No tiene esa cantidad de dinero disponible en su cuenta, su saldo es saldo {saldo}")
        else:
            saldo -= retirar
            print(f"Dinero en la cuenta al momento: ${saldo}")
    elif opcion == 3:
        print(f"Dinero en la cuenta al momento: ${saldo}")
    elif opcion == 4:
        print("Gracias por utilizar su cajero automatico, hasta pronto")
        break
    else:
        print("Opcion Invalidad")
        print()


