ano = int(input('Digite o ano para saber se e bissexto: '))

if ano%4:
    print('Ano digitado: {} é bissexto'.format(ano))
else:
    print('Ano nao bissexto')