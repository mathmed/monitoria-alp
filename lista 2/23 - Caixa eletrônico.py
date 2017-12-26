
print('Programa para simular emissão de células de um caixa eletrônico.')
print('Desenvolvido por @MathMedeiros')
print()
print('Digite abaixo o valor a ser sacado, excluindo os centavos.')
valor=int(input('Digite o valor a ser sacado: ' ))
if valor >= 100:
    a=valor//100
    a1=valor%100
    print('Você receberá %d notas de R$ 100. ' % a)
    b=a1//50
    b1=a1%50
    print('Você receberá %d notas de R$ 50. ' % b)
    c=b1//20
    c1=b1%20
    print('Você receberá %d notas de R$ 20. ' % c)
    d=c1//10
    d1=c1%10
    print('Você receberá %d notas de R$ 1O. ' %d)
    e=d1//5
    e1=d1%5
    print('Você receberá %d notas de R$ 5. ' %e)
    f=e1//2
    f1=e1%2
    print('Você receberá %d notas de R$ 2. ' % f)
    g=f1//1
    print('Você receberá %d notas de R$ 1. ' % g)
elif valor >= 50 and valor < 100:
    b=valor//50
    b1=valor%50
    print('Você receberá %d notas de R$ 50. ' % b)
    c=b1//20
    c1=b1%20
    print('Você receberá %d notas de R$ 20. ' % c)
    d=c1//10
    d1=c1%10
    print('Você receberá %d notas de R$ 1O. ' %d)
    e=d1//5
    e1=d1%5
    print('Você receberá %d notas de R$ 5. ' %e)
    f=e1//2
    f1=e1%2
    print('Você receberá %d notas de R$ 2. ' % f)
    g=f1//1
    print('Você receberá %d notas de R$ 1. ' % g)
elif valor >=20 and valor < 50:
    c=valor//20
    c1=valor%20
    print('Você receberá %d notas de R$ 20. ' % c)
    d=c1//10
    d1=c1%10
    print('Você receberá %d notas de R$ 1O. ' %d)
    e=d1//5
    e1=d1%5
    print('Você receberá %d notas de R$ 5. ' %e)
    f=e1//2
    f1=e1%2
    print('Você receberá %d notas de R$ 2. ' % f)
    g=f1//1
    print('Você receberá %d notas de R$ 1. ' % g)
elif valor >=10 and valor < 20:
    d=valor//10
    d1=valor%10
    print('Você receberá %d notas de R$ 1O. ' %d)
    e=d1//5
    e1=d1%5
    print('Você receberá %d notas de R$ 5. ' %e)
    f=e1//2
    f1=e1%2
    print('Você receberá %d notas de R$ 2. ' % f)
    g=f1//1
    print('Você receberá %d notas de R$ 1. ' % g)
elif valor >=5 and valor <10:
    e=valor//5
    e1=valor%5
    print('Você receberá %d notas de R$ 5. ' %e)
    f=e1//2
    f1=e1%2
    print('Você receberá %d notas de R$ 2. ' % f)
    g=f1//1
    print('Você receberá %d notas de R$ 1. ' % g)
elif valor >= 2 and valor <5:
    f=valor//2
    f1=valor%2
    print('Você receberá %d notas de R$ 2. ' % f)
    g=f1//1
    print('Você receberá %d notas de R$ 1. ' % g)
elif valor ==1:
    print('Você receberá 1 nota de R$ 1. ')
else:
    print('Valor não correspondente, digite seu valor sem os centavos.')
input()
    
    
    
