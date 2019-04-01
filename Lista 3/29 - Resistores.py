#PROGRAMA DESENVOLVIDO POR @MATHMEDEIROS EM 08/03/2017#
print('Programa para calcular o valor da resistência resultante!')
print()
valor1=float(input('Digite o valor do primeiro resistor:' ))
print()
valor2=float(input('Digite o valor do segundo resistor: '))
print('Digite se seu resistor é em série ou paralelo abaixo:')
print()
resistor=input('Digite aqui:')
if resistor == 'Série' or resistor == 'série' or resistor == 'Serie' or resistor == 'serie':
    total1=valor1+valor2
    print('O valor resultante do resistor é %5.2f.' % total1 )
elif resistor == 'Paralelo' or resistor == 'paralelo':
    total2=(valor1*valor2)/(valor1+valor2)
    print('O valor resultante do resistor é %5.2f. ' % total2)
else:
    print('Resistor não encontrado, tente novamente.')

