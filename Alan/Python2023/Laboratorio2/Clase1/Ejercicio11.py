#Ejercicio 11: Agenda telefonica
#hacer un programa que simule una agenda de contactos. crear un diccionario donde la clave sea
#el nombre del usuario y el valor sea el numero, el programa tendra el siguiente menu:
# Menu
# "1. Nuevo contacto
# "2. Borrar contacto
# "3. Ver contactos existentes
# "4. Salir

agenda = {}
while True:
    print("Menu")
    print("1. Nuevo contacto")
    print("2. Borrar contacto")
    print("3. Ver contactos existentes")
    print("4. Salir")
    opcion = int(input("Digite una opcion: "))
    if opcion == 1:
        nombre = input("Digite el nombre del contacto: ")
        numero = int(input("Digite el numero: "))
        if nombre not in agenda:
            agenda[nombre] = numero
            print("Contacto agendado")
        else:
            print("El contacto ya existe")
    elif opcion == 2:
        nombre = input("Cual es el contacto que desea borrar: ")
        if nombre in agenda:
            del (agenda[nombre])
            print("Contacto eliminado")
    elif opcion == 3:
        print("Agenda de contactos ")
        for clave, valor in agenda.items():
            print(f"Nombre: {clave}, Numero: {valor}")
    elif opcion == 4:
        print("Saliendo....")
        break
    else:
        print("La opcion elegida no existe, ingrese una nuevamente.")