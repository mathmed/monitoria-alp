print('Programa desenvolvido por @MateusMedeiros')
print()
print('Programa para converter graus Celsius em Fahrenheit e vise-versa.')
print()
print('Primeiro, digite qual temperatura você quer converter.')
tipo=input('Digite (C) para Celsius ou (F) para Fahrenheit: ')
print()
if tipo == 'c' or tipo =='C':
    temperatura1=float(input('Digite a temperatura a ser convertida: '))
    f=(temperatura1*1.8)+32
    print('A temperatura em Fahrenheit é de:%5.2f ' % f)
elif tipo == 'f' or tipo == 'F':
    temperatura2=float(input('Digite a temperatura a ser convertida: '))
    f2=(temperatura2-32)/1.8
    print('A temperatura em Celsius é de:%5.2f ' % f2)
else:
    print('Tipo de temperatura não encontrado, tente novamente')
input()
