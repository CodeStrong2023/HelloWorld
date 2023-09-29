# Ejercicio 8: Menú interactivo - Cajero automático
# Hacer un programa que simule un cajero automático con un saldo
# inical de $1000 y tendrá el siguiente menú de opciones

saldo = 100
while True:
    print("\t MENÚ: ")
    print("1. Ingresar dinero en la cuenta")
    print("2. Retirar dinero de la cuenta")
    print("3. Mostrar dinero disponible")
    print("4. Salir")
    opcion = int(input("Digite una opción de menú: "))
    print()
    if opcion == 1:
        extra = float(input("Cuánto dinero desea ingresar -> "))
        saldo += extra
        print(f"Dinero en la cuenta al momento: ${saldo}")
    elif opcion == 2:
        retirar = float(input("Cuánto dinero desea retirar -> "))
        if retirar > saldo:
            print("No tiene esa cantidad de dinero")
        else:
            saldo -= retirar
            print(f"Dinero en la cuenta al momento: ${saldo} ")
    elif opciones == 3:
        print(f"Dinero en la cuenta al momento: ${saldo}")
    elif opciones == 4:
        print("Gracias por utilizar el cajero automático, hasta pronto")
        break
    else:
        print("Error. Se equivoco de opción de menú")
        print()