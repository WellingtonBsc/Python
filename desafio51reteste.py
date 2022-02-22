r = int(input('Digite a razao: '))
n = int(input('Digite o PA: '))
total = r + (10 - 1) * n
for pa in range (r, total, n):
    print('{}'.format(pa), end='>')
print('Acabou')