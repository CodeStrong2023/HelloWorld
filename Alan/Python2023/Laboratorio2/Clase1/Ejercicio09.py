#Ejercicio 9: mostrar una frase sin espacios y contar su longitud
#hacer un programa donde el usuario ingrese una frase, se le devolvera la misma frase pero sin espacios
#en blanco, y ademas un contador de cuantos caracteres tiene la frase(sin contar espacios)
#Ejemplo:   frase: vivir por siempre en paz
#           frase final: vivirporsiempreenpaz
#           cantidad de letras: 21

frase1 = input("Digite una frase: ")
frase2 = " "
for i in frase1:
    if i != " ":
        frase2 += i
frase1 = frase2
print(f"Frase final: {frase1}")
print(f"Numero de caracteres: {len(frase1)}")