    x=1
while x==1:
    a=int(input('Digite o numero correspondente ao mês: '))
    if a==1:
        print('Janeiro.')
    elif a==2:
        print('Fevereiro.')
    elif a==3:
        print('Março.')
    elif a==4:
        print('Abril.')
    elif a==5:
        print('Maio.')
    elif a ==6:
        print('Junho.')
    elif a==7:
        print('Julho.')
    elif a ==8:
        print('Agosto.')
    elif a ==9:
        print('Setembro.')
    elif a ==10:
        print('Outubro.')
    elif a ==11:
        print('Novembro.')
    elif a==12:
        print('Dezembro.')
    else:
        print('Número invalido, tente novamente.')
    print('Deseja tentar novamente? Digite 1 para sim ou 2 para não.')
    x=int(input())
    print()
