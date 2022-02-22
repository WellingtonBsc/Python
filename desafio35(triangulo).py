#SISTEMA PARA CALCULAR AS AREAS DE UM TRIANGULO

a = int(input('digite o numero para formar o triangulo: '))
b = int(input('digite o numero para formar o triangulo: '))
c = int(input('digite o numero para formar o triangulo: '))

if (a + b < c) or (a + b < c) or (b + c < a):
    print('Não é um triangulo')
else:
    print('É um triangulo')
