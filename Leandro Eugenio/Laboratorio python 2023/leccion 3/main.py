
'''
#ENesta clase veremos la sentencia if/else
condicion = False
if condicion:
    print('condicion verdadera')
elif condicion == False;
    print('Condicion Falsa')
else:
    print('condicion sin especificar')

'''

num = int(input('Digite un numero en el rango de 1 a 3'))
numText = '';
if num == 1:
    numText = 'Numero uno';
elif num == 2:
    numText = 'Numero dos';
elif num == 3:
    numText = 'Numero tres'
else:
    numText = 'has ingresadop un numero fuera de rango'

print(f'el nuemero ingresado es : {num} - {numText}');

