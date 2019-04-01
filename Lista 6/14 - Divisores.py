print('Divisores entre A e B')
a=int(input('Digite o numero1: '))
b=int(input('Digite o número 2: '))
#for n in range (a,b+1):
#    print('D(%d)= ' % n)
#    for i in range(1,n+1):
#        if (n%i)== 0:
#            print('%d' % i)
#    print()


n=a
while n<=b:
    
    print('D(%d)= ' % n)
    x=1
    while x<=n:
        if (n%x) ==0:
            print('%d' %x)
        x=x+1
    n=n+1
