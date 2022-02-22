somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
for p in range(1,5):
     print('-----{}° Pessoa -----'.format(p))
     nome = str(input('Nome: ').strip())
     idade = int(input('Idade: '))
     sexo = str(input('Sexo [M/F]: ')).strip()
     somaidade += idade
     if p == 1 and sexo in 'Mm': #ou pode trocar por in
         maioridadehomem = idade
         nomevelho = nome
     if sexo in 'Mm' and idade > maioridadehomem:
         maioridadehomem =
mediaidade = somaidade / 4
print('A media de idade do grupo é de {} anos'.format(mediaidade))