casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite seu salario: '))
ano = int(input('Digite em quantos anos ira pagar: '))
emprestimo = casa / (ano * 12)

if emprestimo <= (salario * 0.30):
    print('Aprovado com prestação no valor de: {}'.format(emprestimo))
else:
    print('Negado')

