def maior (x, y, z, a, b):
    max = x

    if y > max:
        max = y
    if z > max:
        max = z
    if a > max:
        max = a
    if b > max:
        max = b

    return max

def menor(x,y,z,a,b)
    min = x

    if y < min:
        min = y
    if z < min:
        min = z
    if a < min:
        min = a
    if b < min:
        min = b
    return min
def menu():
    x = int(input('Primeiro numero: '))
    y = int(input('Segundo numero: '))
    z = int(input('Terceiro numero: '))
    a = int(input('Quarto numero: '))
    b = int(input('Quinto numero: '))

    print('Maior é: ', maior(x, y, z, a, b))
    print('Menor é: ', menor(x, y, z, a, b))
    print()

while True:
    menu()

