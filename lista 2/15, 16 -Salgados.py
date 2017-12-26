print('Programa desenvolvido por Mateus Medeiros :D')
print()
print('Digite a quantidade correspondente ao número de salgados a seguir!')
a1=int(input('Digite a quantidade de Pastel de Queijo de Manteiga que deseja: '))
a2=int(input('Digite a quantidade de Pastel de Carne de Sol  que deseja: ' ))
a3=int(input('Digite a quantidade de Pastel de Frango  que deseja: '))
a4=int(input('Digite a quantidade de Pastel de Camarão  que deseja: '))
a5=int(input('Digite a quantidade de Empadinha de Frango  que deseja: '))
a6=int(input('Digite a quantidade de Empadinha de Camarão que deseja: '))
a7=int(input('Digite a quantidade de Coxinha de Frango  que deseja: '))
a8=int(input('Digite a quantidade de Enroladinho de Salsicha  que deseja: '))
a9=int(input('Digite a quantidade de Massa Folhada de Queijo  que deseja: '))
print()
b1=a1*0.90
b2=a2*0.95
b3=a3*0.75
b4=a4*1.75
b5=a5*1.05
b6=a6*2.22
b7=a7*1.40
b8=a8*1.85
b9=a9*1.65
sub=b1+b2+b3+b4+b5+b6+b7+b8+b9
print('O Sub-Total deu:R$%5.2f ! ' % sub)
print()
a3=input('Deseja dar algum desconto?: ')
if a3 == 'Sim' or a3 == 'sim' or a3== 'SIM':
    porc=float(input('Digite a porcentagem de Desconto: '))
    desc=(porc/100)*sub
    preço=sub-desc
    print('O preço final é de: R$%5.2f ' % preço)
else:
    print('O preço final é de: R$%5.2f ' % sub)
input()
    
