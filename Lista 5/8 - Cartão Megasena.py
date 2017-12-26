     #Escreva um programa em Python que gere aleatoriamente N cartões de apostas da
     #MegaSena. Cada cartão deverá conter entre seis e dez dezenas escolhidas ao acaso entre
     #os números 1 e 60, utilizando a função ​random.randint(a,b)​. A quantidade de dezenas
     #do cartão é definida pelo usuário do programa. Lembre-se que não devem haver dezenas
     #repetidas em um mesmo cartão.

import random
num=int(input('Digite quantos cartões deseja: '))
d=int(input('Quantas dezenas deseja no cartão (de 6 à 10 por favor): '))
if d > 6 and d < 10:
    for i in range(num):
        cartao=[]
        cont=0
        while cont<d:
            a=random.randint(1,60)
            if a not in cartao:
                cartao.append(a)
                cont+=1
        print(cartao)
else:
    print('vc digito errado seu filha da pouta sabe le nao arrombado do kraralho vai toma no cu')
    
