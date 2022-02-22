num1 = int(input('Digite um numero: '))
num2 = int(input('Digite o segundo numero: '))

if num1 < num2:
    print('o numero {} é menor que o numero {}'.format(num1, num2))
elif num2 > num1:
    print('o numero {} é menor que o numero {}'.format(num2, num1))
else:
    print('O numero {} é igual ao numero digitado {}'.format(num1, num2))