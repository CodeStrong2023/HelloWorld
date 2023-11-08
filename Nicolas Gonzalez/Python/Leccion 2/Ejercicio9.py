'''
calcular la suma de N primeros numeros
'''

n = int(input('Dame el valor de N '))
suma = 0;

for i in range(1, n+1):
    suma += i

print(f'La suma de los {n} primeros numeros es: {suma}')
