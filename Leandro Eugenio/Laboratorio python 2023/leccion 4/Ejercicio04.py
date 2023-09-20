#Ejercicio 4: Sumar Números pares dentro de un rango
#hacer un programa àra sumar numeros pares dentro
#de un rango, por ejemplo:
#                           suma de numeros pares del 2 al 30
#                           suma = 240      

print("SUMARE LOS NUMEROS PARES DENTRO DEL RANGO QUE ELIJAS")
a = int(input("Digite el comienzo del rango"))
b = int(input("Digite el final del rango"))
suma = 0;
for i in range(a,b +1):
    if(i % 2 ==0):
        suma += i;
print(f"la suma es = {suma}")

