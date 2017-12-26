print('Programa para saber se o triângulo é isósceles, equilátero ou escaleno.')
a=float(input('Digite o valor do primeiro lado em CM. : '))
b=float(input('Digite o valor do segundo lado em CM. : '))
c=float(input('Digite o valor do terceiro lado em CM. : '))
if a+b>c and a+c>b and b+c>a:
    if a==b and b==c:
        print('Triângulo equilátero.')
    elif a==b and a!=c:
        print('Triângulo isósceles.')
    elif a==c and b!=c:
        print('Triângulo isósceles.')
    elif c==b and b!=a:
        print('Triângulo isósceles.')
    elif a!=b and b!=c and c!=a:
        print('Triângulo Escaleno.')
else:
    print('Essas medidas não formam um triângulo.')
    
