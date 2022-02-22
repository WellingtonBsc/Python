v1 = int(input('Digite o 1 valor: '))
v2 = int(input('Digite o 2 valor: '))
op = 0
validador = 0
while op != 5:
    print('''DIGITE SUA OPÇÃO
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NUMEROS
    [5] SAIR DO PROGRAMA''')
    op = int(input('Escolha uma opção: '))
    if op == 1:
        print('total é {}'.format(v1 + v2))
    elif op == 2:
        print('total é {}'.format(v1 * v2))
    elif op == 3:
        if v1 > v2:
            validador = v1
            print(' O numero {} é maior'.format(validador))
        else:
            validador = v2
            print('O numero maior é {}'.format(validador))
    elif op == 4:
        print('informe os numero novamente': )
        v1 = int(input('Primeiro valor: '))
        v2 = int(input('Segundo valor: '))
    elif op == 5:
        print('Sair')
    else:
        print('Opcao invalida')

    print('---' * 10)


print('fim')

