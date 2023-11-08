""" ejercicio 10 : No repetir caracteres
hacer un programa que pida una cadena por teclado,luego
meter los caracteres en un alista sin reètior caracters.
"""
cadena = input('DIigte la cadena')
lista = []
for i in cadena:
    if i not in lista: #si el caracter no esy6a en la lista
        lista.append(i);
print(f'\nLista de caracteres sin repetir ninguno: \n {lista}')