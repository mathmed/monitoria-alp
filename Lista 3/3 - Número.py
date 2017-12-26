n=int(input('Digite o seu número inteiro: '))
print()
print('Vamos ver!')
if n > 0:
    a=n%2
    if a== 0:
        print('O número é positivo e par.')
    else:
        print('O número é positivo e impar.')
elif n<0:
    a=n%2
    if a==0:
        print('O número é negativo e par.')
    else:
        print('O número é negativo e impar.')
else:
    print('O número é nulo.')
