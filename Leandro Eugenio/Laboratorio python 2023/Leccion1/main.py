'''
condicion = True;
if condicion == True:
    print('Condicion Verdadera')
elif condicion == False:
    print('Condicion falsa')
else:
    print('Condicion sin especificar')
'''
''''
num = int(input("Digite un numero en el rango del 1 al 3 :"))
numTexto='';
if num == 1:
    numTexto = 'Número uno'
elif num == 2:
    numTexto = 'Número dos'
elif num == 3:
    numTexto = 'Número tres'
else:
    numTexto = 'Has ingresado un numero fuera de rango'
print(f'el numero ingresado es : {num} - {numTexto}')
'''
condicion = True

""" if condicion:
    print('Condicion verdadera')
else:
    print('Condicion falsa') """

print('Condicion Verdadera') if condicion else print('Condicion falsa')


