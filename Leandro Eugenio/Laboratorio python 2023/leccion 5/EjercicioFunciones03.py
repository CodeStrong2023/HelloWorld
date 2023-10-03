""" 
Ejercicio 3: Funcion Recursiva
Impirmir numeros de 5 a 1 de manera descendente usando funciones recursivas
Puede ser cualquier valor positivo,por ejemplo, si pasamos 
el valor de 5 debe imprimir:
5
4
3
2
1
 """

def funcionRecursiva(numero):
    if numero >= 1:
        print(numero)
        funcionRecursiva(numero-1)
    
resultado = funcionRecursiva(int(input("Digite un numero: ")))
print(resultado)