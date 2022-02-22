distancia = float(input('Digite quantos KM teve a sua viagem: '))
v1 = (distancia * 0.50)
v2 = (distancia * 0.45)

if distancia >= 200:
    print('valor total a se pagar é de {}R$'.format(v2))
else:
    print('valor total a se pagar é de {}R$'.format(v1))