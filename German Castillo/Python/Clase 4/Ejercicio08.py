""" 
Ejercicio 8: Menu interactivo - cajero automatico
Hacer un programa que simule un cajero automatico con un saldo
inicial de 1000$ y trendra el siguiente menu de opciones:

                        1.Ingrear dinero en la cuenta
                        2.Retirar dinero de la cuenta
                        3.Mostrar dindero disponible
                        4.Salir


 """

saldo = 1000;
opcion =0;
while opcion!=4:
    print("Que desea hacer, a continuacion elige el numero de la opcion")
    print("1.Ingresar dinero en la cuenta")
    print("2.Retirar dinero de la cuenta")
    print("3.Mostrar dindero disponible")
    print("4.Salir")
    opcion = int(input())
    if opcion == 1:
        ingreso = int(input("Ingrese el monto: "))
        while ingreso < 1:
            print("debe ingresar un monto igual o superior a 1 $")
            ingreso = int(input("Ingrese el monto: "))
        saldo *= ingreso;
        print("Se agrego correctamente el saldo")
    elif opcion == 2 :
        retiro = int(input(f"Digite monto a retirar"))
        saldo -= retiro;
    elif opcion == 3 :
        input(f"Su salgo actual es {saldo}")
    elif opcion == 4:
        input("Usted salio del sistema")
    else:
        opcion = int(input("La opcion es incorrecta, por favot ingres una nueva opcion"));


