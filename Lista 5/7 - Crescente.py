n1=int(input('Digite o primeiro número inteiro: '))
n2=int(input('Digite o segundo numero inteiro: '))
n3=int(input('Digite o terceiro número inteiro: '))
if n1>n2>n3:
    print(n1,n2,n3)
elif n1>n3>n2:
    print(n1,n3,n2)
elif n2>n1>n3:
    print(n2,n1,n3)
elif n2>n3>n1:
    print(n2,n3,n1)
elif n3>n2>n1:
    print(n3,n2,n1)
elif n3>n1>n2:
    print(n3,n1,n2)
else:
    print('Inválido, existem números iguais, então não é possivel colocar em ordem.')
