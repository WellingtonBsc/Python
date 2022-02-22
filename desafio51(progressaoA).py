t = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razao: '))
decimo = t + (10 - 1) * r
for pa in range (t, decimo, r):
    print('{} '.format(pa), end=' > ')
print('Acabou')