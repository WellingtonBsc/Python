print('{:=^40}'.format('LOJAS WELLTECH'))
preco = float(input('Preco das compras: R$: '))
print(''' FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista cartao
[3] 2x no cartao
[4] 3x no cartao''')
opcao = int(input('Qual opcao?: '))

if opcao == 1:
    total = preco -(preco * 0.10)
elif opcao == 2:
    total = preco - (preco * 0.05)
elif opcao == 3:
    total = preco
elif opcao == 4:
    total = preco + (preco * 0.20)
else:
    print('opcão invalida tente novamente')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))