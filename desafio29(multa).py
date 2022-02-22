vel = int(input('Digite a velocidade que você passou: '))

multa = ((vel - 80) * 7)

if vel <= 80:
    print('Parabens voce passou com velocidade {}km'.format(vel))

else:
    print('Voce se lascou passando a {}km'.format(vel))
    print('O valor total da multa é de R$: {} '.format(multa))


