#PROGARMA DE ADVINHAÇÃO DESENVOLVIDO POR @MATHMEDEIROS EM 26/03/2017#
import random
x=1
p=0
while x<=3:
    x=x+1
    print('Programa de advinhação!')
    print('Você tem 3 chances de advinhar o número sorteado pelo computador.')
    print('Lembrando que é de 1 à 9!!!')
    print()
    a=random.randint(1,9)
    b=int(input('Vamos lá! Digite um numero de 1 à 9, vamos ver se a sorte está do seu lado: '))
    if b>9:
        print('VocÊ digitou um número inválido.')
    elif a==b:
        print('Caramba, você teve muita sorte!! O número sorteado foi %d !! .' % a)
        print('Você recebeu 10 pontos por acertar de primeira.')
        p=p+10
    elif a!=b:
        print('Você errou na primeira chance, vamos continuar.')
        print()
        if a>b:
            print('Vou dar uma dica, o número sorteado é maior que o que você digitou...')
            print()
            print()
            c=int(input('Vamos lá, tente novamente: '))
            print()
            if c==a:
                print('Você acertou, não foi de primeira mas foi muito bem, parabéns. O numero sorteado foi %d !! .' % a)
                print('Você ganhou 9 pontos.')
                p=p+9
            elif a>c:
                 print('Você errou.')
                 print('Vou dar a última dica, o número sorteado é maior que o que você digitou...')
                 d=int(input('Vamos lá, tente novamente: '))
                 if d==a:
                     print('Você acertou na última chance. O numero sorteado foi %d !! .' % a)
                     print('Você ganhou 8 pontos.')
                     p=p+8
                 else:
                     print('Você errou nas 3 chances, você é muito ruim. O numero sorteado foi %d' % a)
                     print('Você ganhou 0 pontos.')
                     p=p
            elif c>a:
                print('Vou dar a última dica, o número sorteado é menor que o que você digitou...')
                e=int(input('Vamos lá, tente novamente: '))
                if e==a:
                     print('Você acertou na última chance. O numero sorteado foi %d !! .' % a)
                     print('Você ganhou 8 pontos.')
                     p=p+8
                else:
                    print('Você errou nas 3 chances, você é muito ruim. O numero sorteado foi %d' % a)
                    print('Você ganhou 0 pontos.')
                    p=p
        elif b>a:
            print('Vou dar uma dica, o número sorteado é menor que o que você digitou...')
            f=int(input('Vamos lá, tente novamente: '))
            if f==a:
                print('Você acertou, não foi de primeira mas foi muito bem, parabéns. O numero sorteado foi %d !! .' % a)
                print('Você ganhou 9 pontos.')
                p=p+9
            elif a>f:
                 print('Você errou.')
                 print('Vou dar a última dica, o número sorteado é maior que o que você digitou...')
                 g=int(input('Vamos lá, tente novamente: '))
                 if g==a:
                     print('Você acertou na última chance. O numero sorteado foi %d !! .' % a)
                     print('Você ganhou 8 pontos.')
                     p=p+8
                 else:
                     print('Você errou nas 3 chances, você é muito ruim. O numero sorteado foi %d' % a)
                     print('Você ganhou 0 pontos.')
                     p=p
            elif f>a:
                print('Vou dar a última dica, o número sorteado é menor que o que você digitou...')
                h=int(input('Vamos lá, tente novamente: '))
                if h==a:
                     print('Você acertou na última chance. O numero sorteado foi %d !! .' % a)
                     print('Você ganhou 8 pontos.')
                     p=p+8
                else:
                    print('Você errou nas 3 chances, você é muito ruim. O numero sorteado foi %d' % a)
                    print('Você ganhou 0 pontos.')
                    p=p
    print('Você está com %d pontos. ' % p )
    input()

