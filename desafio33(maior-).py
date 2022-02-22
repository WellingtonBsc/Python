lista = []
while True:
    n = int(input('Digite o numero (0 para encerrar): '))
    lista.append(n)
    if n == 0:
        break
print('O numero maior da lista é: ',max(lista))

