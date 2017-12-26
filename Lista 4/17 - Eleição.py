print('Programa de votação.')
c1=0
c2=0
while True:
    a=int(input('Digite uma 1 para votar no candidato 1, 2 para votar no candidato 2, ou 0 para terrminar.'))
    if a==1:
        c1+=1
    elif a==2:
        c2+=1
    else:
        break
print('O candidato 1 teve %d votos e o candidato 2 teve %d votos. ' %(c1,c2))
