print('Programa para calcular seu peso ideal!')
print()
print('Desenvolvido por Mateus Medeiros')
print()
sexo=input('Digite seu sexo! (M) para Masculino e (F) para feminino: ')
b=sexo
print()
if b == 'M' or b == 'm':
    print('Vamos calcular')
    h=float(input('Digite a sua altura, por exemplo, 1.78: '))
    peso_m=h*100
    peso_m2=(peso_m-100)-(peso_m-150)/4
    print('Seu peso ideal é:%5.2f Kilos! ' % peso_m2)
elif b== 'F'or b== 'f':
    
    h=float(input('Digite a sua altura, por exemplo, 1.56: '))
    peso_f=h*100
    peso_f2=(peso_f-100)-(peso_f-150)/2
    print('Seu peso ideal é:%5.2f Kilos! ' % peso_f2)
else:
    print('Sexo não correspondente, tente novamente')
input()
