import random
print('Jogo zerinho ou um.')
l=input('Dê enter para continuar.')
print()
nome=input('Digite seu nome: ')
print()
x=1
while x==1:
    a=int(input('Escolha 0 ou 1: '))
    b=random.randint(0,1)
    print('Jogador 2 escolheu %d . ' % b)
    c=random.randint(0,1)
    print('Jogador 3 escolheu %d . ' % c)
    if a != b and a!= c:
        print('Parabéns %s, você venceu.' % nome)
    elif b!= a and b!= c:
        print('Jogador 2 venceu.')
    elif c!= a and c!= b:
        print('Jogador 3 venceu.')
    else:
        print('Empate.')
    print()
    x=int(input('Digite 1 para jogar novamente ou 2 para sair.'))
