print('Programa para saber se um número é divisivel por outro.')
a=int(input('Digite o primeiro número: '))
b=int(input('Digite o segundo número: '))
if a>b:
    c=a%b
    if c==0:
        print('É divisível.')
        c=a/b
        print(c)
    elif c!= 0:
        print('Não é divisível.')
elif b>a:
    c=b%a
    if c==0:
        print('Divisivel.')
        c=b/a
        print(c)
    elif c!=0:
        print('Não é divisivel.')
else:
    print('1')
