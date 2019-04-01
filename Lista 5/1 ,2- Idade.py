
nome1=input('Digite o nome da primeira pessoa: ')
idade=int(input('Digite a idade da primeira pessoa: '))
a=idade
print()
nome2=input('Digite o nome da segunda pessoa: ')
idade2=int(input('Digite a idade da segunda pessoa: '))
b=idade2
print()
if a>b:
    print('%s é mais velho(a). ' % nome1)
elif b>a:
    print('%s é mais velho(a). ' %nome2)
else:
    print('Ambos tem a mesma idade.' )
print()
print('Vamos a diferença de idade. ')
if a>b:
    d=a-b
    print('A diferença de idade é %d anos. ' % d)
elif b>a:
    d=b-a
    print('A diferença de idade é %d anos. ' % d)
else:
    print('Não tem diferença de idade.')
