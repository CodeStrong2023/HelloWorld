#//////////////////clase 7 (sentencias de control)//////////////

#------------ejercicio 7.1------------------
# mes=int(input("Ingrese el numero de mes: "))
# if mes >=1 and mes <=3:
#     print("Estacion: Verano.")
# elif mes >=4 and mes <=6:
#     print("Estacion: Otoño.")
# elif mes >=7 and mes <=9:
#     print("Estacion: Invierno.")
# elif mes >=10 and mes <=12:
#     print("Estacion: Primavera.")

#-------------------ejercicio 7.2------------
# edad=int(input("Ingrese su edad: "))
# if edad >=0 and edad <=10:
#      print("La infancia es increible y bella")
# elif edad >=10 and edad <=19:
#      print("tienes muchos cambios, mucho que estudiar")
# elif edad >=20 and edad <=29:
#      print("amor y comienza el trabajo")
# elif edad >=30 and edad <=39:
#      print("trabajar duro y formar una familia")
# elif edad >=40 and edad <=49:
#     print("trabajar y disfrutar la infancia de tus hijos")
# elif edad >=50 and edad <=59:
#     print("trabajar y disfrutar de tus ultimos dias de trabajo")
# elif edad >=60 and edad <=69:
#     print("jubilarte")
# elif edad >=70 and edad <=100:
#     print("pasar el resto de tu vida con tu familia y haciendo lo que te gusta")

#-----------------ejercicio 7.3---------------
# calificacion=int(input("Ingrese la calificacion: "))
# if calificacion <=10 and calificacion >=9:
#     print("Su calificacion es: A")
# elif calificacion <9 and calificacion >=8:
#     print("Su calificacion es: B")
# elif calificacion <8 and calificacion >=7:
#     print("Su calificacion es: C")
# elif calificacion <7 and calificacion >=6:
#     print("Su calificacion es: D")
# elif calificacion <6 and calificacion >=0:
#     print("Su calificacion es: F")
# else:
#     print("El valor ingresado es incorrecto.")

#//////////////////clase 7 (ciclo while y for)////////////////

#------------ejercicio 7.1 (ciclo while)--------------
# contador=0
# while contador <5:
#     print("inicia el ciclo", + contador)
#     contador +=1
# else:
#     print("fin del ciclo")

#-------------ejercicio 7.2----------
# maximo=5
# contador=1
# while contador <= maximo:
#     print(contador)
#     contador+=1
# else:
#     print("fin")

#------------ejercicio 7.3-----------
# minimo=1
# contador=5
# while contador >= minimo:
#     print(contador)
#     contador -=1

#--------------ejercicio 7.4 (ciclo for o para)-------
# cadena ="hello"
# for letra in cadena:
#     print(letra)
# else:
#     print("fin")

#--------------ejercicio 7.5 (palabra reservada break)--------------
# for letra in "Alemania":
#     if letra == "a":
#         print("letra encontrada: ", letra)
#         break
# else:
#     print("fin")

#--------------ejercicio 7.6 (palabra reservada continue)----------
# for i in range(6):
#     if i % 2 == 0:
#         print("valor: ", i)
#
# for i in range (6):
#     if i % 2 != 0:
#         continue
#     print("valor: ", i)