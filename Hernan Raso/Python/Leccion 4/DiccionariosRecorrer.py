# Seguiumos viendo formas de recorrer diccionarios

seleccionArgentina = {
    10: {'Nombre': 'Lionel Messi', 'Edad': 35, 'Altura': 1.70, 'Precio': '50 Millones', 'Posicion': 'Extremo Derecho'},
    11: {'Nombre': 'Angel Di Maria', 'Edad': 34, 'Altura': 1.80, 'Precio': '12 Millones', 'Posicion': 'Extremo Derecho'},
    24: {'Nombre': 'Paulo Dybala', 'Edad': 28, 'Altura': 1.77, 'Precio': '35 Millones', 'Posicion': 'Media Punta'},
    19: {'Nombre': 'Nicolas Otamendi', 'Edad': 34, 'Altura': 1.83, 'Precio': '3.5 Millones', 'Posicion': 'Defensa Central'},
    1: {'Nombre': 'Franco Armani', 'Edad': 35, 'Altura': 1.89, 'Precio': '3.5 Millones', 'Posicion': 'Portero'},
    18: {'Nombre': 'Guido Rodriguez', 'Edad': 29, 'Altura': 1.85, 'Precio': '28 Millones', 'Posicion': 'Pivote'},
    7: {'Nombre': 'Rodrigo de Paul', 'Edad': 29, 'Altura': 1.80, 'Precio': '40 Millones', 'Posicion': 'Mediocentro'},
    20: {'Nombre': 'Alexis Mac Allister', 'Edad': 24, 'Altura': 1.76, 'Precio': '65 Millones', 'Posicion': 'Mediocentro'},
    9: {'Nombre': 'Julian Alvarez', 'Edad': 23, 'Altura': 1.70, 'Precio': '60 Millones', 'Posicion': 'Delantero Centro'},

}

for i in seleccionArgentina:
    print(f'{i} -> {seleccionArgentina[i]}')