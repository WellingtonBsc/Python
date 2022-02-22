from random import randint

print('{:.2f}BEM VINDO AO JOKENPO')

jogo = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('''Digite uma das opções: 
[0] PEDRA 
[1] PAPEL 
[2] TESOURA
''')
jogador = int(input('Qual sua jogada? : '))
print('JO')
print('KEN')
print('PO')
print('-=' * 11)

print(f'Jogador jogou: {jogo[jogador]}')
print(f'Computador jogou: {jogo[computador]}')
print('-=' * 11)
if computador == 0:
    if jogador ==0:
       print('Empate')
    elif jogador ==1:
       print('Jogador vence!')
    elif jogador ==2:
        print('Computador venceu')
    else:
        print('Jogada invalida!')
elif computador == 1:
    if jogador ==0:
       print('Computador Venceu')
    elif jogador ==1:
       print('Empate!')
    elif jogador ==2:
        print('Jogador venceu')
    else:
        print('Jogada invalida!')
elif computador == 2:
    if jogador ==0:
       print('jogador Venceu')
    elif jogador ==1:
       print('Computador venceu!')
    elif jogador ==2:
        print('Empate')
    else:
        print('Jogada invalida!')

finalizar = input('''Deseja continuar digite sim ou sair para parar
[SIM]
[SAIR]
''')

