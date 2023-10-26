# Desempaquetado de listas o lis Unpacking
def show(name, lastName):
    print(name+' '+lastName)
persona = ["Ariel", "Betancud"]
show(persona[0], persona[1]) # Pasamos uno por uno los datos de la lista a la funcion
show(*persona) # Esto es lo mismo que lo anterior pero le pasamos todo junto
persona2 = ("Osvaldo", "Giordanini") # Desempaquetamos a traves de una tupla
show(*persona2)
persona3 = {"lastName": "Lucero", "name": "Natalia"}
show(**persona3)
