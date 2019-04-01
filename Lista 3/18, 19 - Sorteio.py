nome1=input('Digite o nome do jogador 1: ' )
nome2=input('Digite o nome do jogador 2: ' )
print()
print('Vamos começar com o jogador 1!')
import random
x1 = random.randint(1,6)
print("O primeiro númedo do dado do jogador 1 foi: ", x1)
import random
x2= random.randint(1,6)
print('O Segundo número do dado do jogador 1 foi: ' , x2)
j1=x1+x2
print('O Jogador 1 fez %d pontos! ' % j1)
print()
print('Vamos para o jogador 2!')
import random
x3 = random.randint(1,6)
print( 'O Primeiro número do jogador 2 foi: ', x3)
import random
x4= random.randint(1,6)
print('O Segundo número do jogador 2 foi: ',x4)
j2=x3+x4
print('O Jogador 2 fez %d pontos! ' % j2)
print()
if j1>j2:
    print('Jogador 1 venceu!')
elif j2>j1:
    print('Jogador 2 venceu! ' )
else:
    print('Empate!')
input()

