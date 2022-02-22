salario = float(input('Digite o valor do seu salario: '))
sal1 = salario + (salario * 0.10)
sal2 = salario + (salario * 0.15)

if salario >= 1250:
    print('Seu salario é: {}'.format(salario))
    print('Seu salario com reajuste de 10% é de: {}'.format(sal1))
else:
    print('Seu salario é: {}'.format(salario))
    print('Seu salario com reajuste de 15% é de: {}'.format(sal2))