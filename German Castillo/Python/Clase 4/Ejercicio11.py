""" 
Ejercicio 11: Agenda telefonica
Hcer un programa que simule un aagenda de contactos. Crear un
diccionario donde la clave sea el nombre del usaurio y el valor
sea el telefono, el programa tendra el siguiente emnu de opciones:
    1.Nuevo contacto
    2.Borrar contacto
    3.ver contactos existentes
    4.salir

 """
agenda = {};
while True:
    print('\t.:MENU:.')
    print('1.Nuevo contacto')
    print('2.Borrar contacto')
    print('3.ver contactos existentes')
    print(' 4.salir')
    opcion = int(input('Digite una opcion de menu'))
    if opcion ==1 :
        nombre= input('Digite el nombre del contacto: ')
        telefono = input('Digite el numero de telefono')
        if nombre not in agenda:
            agenda[nombre] = telefono
            print('Contacto agregao exitosamente')
        else:
            print('Elcontacto ya existe')
    elif opcion == 2:
        nombre = input('Cual es el nombre del contacto: ')
        if nombre in agenda:
            del (agenda[nombre])
            print('Contacto eliminado con exito')
        else:
            print('Este contacto no existe en la agenda')
    elif opcion == 3:
        print('Agenda de contactos')
        for clave, valor in agenda.items():
            print(f'Nombre: {clave}, telefono: {valor}')
    elif opcion == 4:
        print('usted salio de la agenda')
        break
    else:
        print('La opcion ingresada es incorecta')