print('Multiplos de de um número entre dois números, sacas??? ')
m=int(input('Digite seu múltiplo: '))
n1=int(input('Digite o número que a partir dele veremos o múltiplo: '))
n2=int(input('Digite o número correspondente ao fim da pesquisa dos múltiplos: '))
n2=n2+1
for n in range (n1,n2):
    if n%m == 0:
        print('Múltiplo : %d ' % n)
