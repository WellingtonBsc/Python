num = int(input('Digite um numero inteiro: '))
mult= 0

for count in range(2, num):
    if(num % count == 0):
        print('Multiplo de',count)
        mult +=1

if(mult==0):
    print('é primo')
else:
    print('tem',m ult,'multiplos acima de 2 e abaixo de', num)