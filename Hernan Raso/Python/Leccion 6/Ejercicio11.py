# Ejercicio 11: Agenda telefonica
# Hacer un programa que simule una agenda de contactos. Crear un diccionario donde la clave sea el no,bre del usuario y
# y el valor sea el telefono, el programa tendra el siguiente menu de opcione:
#            1. Nuevo contacto
#            2. Borrar Contacto
#            3. Ver contactos existentes
#            4. Salir

agenda = {}
while True:
    print('\t.:MENU:.')
    print('1. Nuevo contacto')
    print('2. Borrar Contacto')
    print('3. Ver contactos existentes')
    print('4. Salir')
    opcion = int(input('Digite una opcion de menu: '))
    if opcion == 1:
        nombre = input("Ingrese el nombre del contacto: ")
        telefono= input("Ingrese el numero de telefono: ")
        if nombre not in agenda:
            agenda[nombre] = telefono
            print("Contacto agregado exitosamente! ")
        else:
            print("Este nombre de contacto ya existe")
    elif opcion == 2:
        nombre = input("Ingrese el nombre del contacto a borrar: ")
        if nombre in agenda:
            del (agenda[nombre])
            print("El contacto ha sido eliminado")
        else:
            print("Ese contacto no existe en la agenda")
    elif opcion == 3:
        print("Agenda de contactos")
        for clave, valor in agenda.items():
            print(f"Nombre: {clave}, Telefono: {valor}")
    elif opcion == 4:
        print("Gracias por utilizar su agenda de contactos")
        break
    else:
        print("Opcion Invalida")
    print()


