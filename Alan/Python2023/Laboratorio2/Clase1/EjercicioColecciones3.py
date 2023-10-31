#ejercicio 3: agregar personajes a una lista
#escriba un programa donde cree una lista con los siguientes personajes del señor de los anillos

#Nombre: Aragorn
#Clase: Guerrero
#Raza: Dunadan del norte

#Nombre: Gandalf
#Clase: Mago
#Raza: Istar

#Nombre: Legolas
#Clase: Arquero
#Raza: Elfo Sindar

personajes = [] #creamos una lista vacia
P = {"Nombre ": "Aragorn", "Clase ": "Guerrero", "Raza": "Dunadan del norte"}
personajes.append(P)#agregamos un personaje a la lista
P = {"Nombre ": "Gandalf", "Clase ": "Mago", "Raza": "Istal"}
personajes.append(P)#agregamos un personaje a la lista
P = {"Nombre ": "Legolas", "Clase ": "Arquero", "Raza": "Elfo Sindar"}
personajes.append(P)#agregamos un personaje a la lista
P = {"Nombre ": "Gimli", "Clase ": "Guerrero", "Raza": "Enano"}
personajes.append(P)#agregamos un personaje a la lista
P = {"Nombre ": "Sauron", "Clase ": "Nigromante", "Raza": "Maiar"}
personajes.append(P)#agregamos un personaje a la lista
P = {"Nombre ": "Galadriel", "Clase ": "Maga", "Raza": "Elfo Noldor"}
personajes.append(P)#agregamos un personaje a la lista
#mostramos la lista
print(personajes)