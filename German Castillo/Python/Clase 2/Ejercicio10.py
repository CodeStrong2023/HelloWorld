'''
Leer 10 numeros e imprimir cuantos son positivos cuantos negativos y cuantos neutros
'''

num = 0
conteo_negativos = 0
conteo_positivos = 0
conteo_neutro = 0
print('Ingresa diez numeros')
for i in range(0, 10):
    num = int(input())
    if num>0:
        conteo_positivos += 1
    elif num<0:
        conteo_negativos += 1
    else:
        conteo_neutro += 1

print(f'La cantidad de numeros positivos es: {conteo_positivos}')
print(f'La cantidad de numeros negativos es: {conteo_negativos}')
print(f'La cantidad de numeros neutros es  : {conteo_neutro}')