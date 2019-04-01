a=int(input('Digite um número que quer extrair os multiplos : '))
b=int(input('até que numero voce quer multiplos: '))
b=b+1
for i in range (1,b):
    if i%a ==0:
        print('%d é multiplo de %d .' % (a,i))
